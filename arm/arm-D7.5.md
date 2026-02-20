## D7.5 Cache support

This section describes the cache identification and control mechanisms, and the A64 cache maintenance instructions, in the following sections:

- General behavior of the caches.
- Cache identification.
- Cacheability, cache allocation hints, and cache transient hints.
- Enabling and disabling the caching of memory accesses.
- Behavior of caches at reset
- Non-cacheable accesses and instruction caches.
- About cache maintenance in AArch64 state.
- A64 Cache maintenance instructions
- Data cache zero instruction.
- Cache lockdown.
- System level caches.
- Branch prediction.
- Execution, data prediction and prefetching restriction System instructions.

See also Caches.

## D7.5.1 General behavior of the caches

When a memory location has a Normal Cacheable memory attribute, determining whether a copy of the memory location is held in a cache still depends on many aspects of the implementation. The following non-exhaustive list of factors might be involved:

- The size, line length, and associativity of the cache.
- The cache allocation algorithm.
- Activity by other elements of the system that can access the memory.
- Speculative instruction fetching algorithms.
- Speculative data fetching algorithms.
- Interrupt behaviors.

Given this range of factors, and the large variety of cache systems that might be implemented, the architecture cannot guarantee whether:

- Amemory location present in the cache remains in the cache.
- Amemory location not present in the cache is brought into the cache.

Instead, the following principles apply to the behavior of caches:

- The architecture has a concept of an entry locked down in the cache. How lockdown is achieved is IMPLEMENTATION DEFINED, and lockdown might not be supported by:
- -Aparticular implementation.
- -Some memory attributes.
- An unlocked entry in a cache might not remain in that cache. The architecture does not guarantee that an unlocked cache entry remains in the cache or remains incoherent with the rest of memory. Software must not assume that an unlocked item that remains in the cache remains dirty.
- Alocked entry in a cache is guaranteed to remain in that cache. The architecture does not guarantee that a locked cache entry remains incoherent with the rest of memory, that is, it might not remain dirty.

Note

For more information, see The interaction of cache lockdown with cache maintenance instructions.

- Any memory location that has a Normal Cacheable attribute at either the current Exception level or at a higher Exception level can be allocated to a cache at any time.

- It is guaranteed that no memory location will be allocated into a Data or Unified cache if that location does not have a Normal Cacheable attribute in either:

- The translation regime at the current Exception level.

- The translation regime at any higher Exception level.

- For data accesses, any memory location with a Normal Inner Shareable or Normal Outer Shareable attribute is guaranteed to be coherent with all Requesters in its shareability domain.

- Any memory location is not guaranteed to remain incoherent with the rest of memory.

- The eviction of a cache entry from a cache level can overwrite memory that has been written by another observer only if the entry contains a memory location that has been written to by an observer in the shareability domain of that memory location. The maximum size of the memory that can be overwritten is called the Cache Write-back Granule . In some implementations the CTR\_EL0 identifies the Cache Write-back Granule.

- The allocation of a memory location into a cache cannot cause the most recent value of that memory location to become invisible to an observer if it was previously visible to that observer.

Note The Cacheability attribute of an address is determined by the applicable translation table entry for that address, as modified by any applicable System register Cacheability controls, such as the SCTLR\_EL1.{I, C} controls.

For the purpose of these principles, a cache entry covers at least 16 bytes and no more than 2KB of contiguous address space, aligned to the size of the cache entry.

## D7.5.2 Cache identification

The cache identification registers describe the implemented caches that are affected by cache maintenance instructions executed on the PE. This includes the cache maintenance instructions that:

- Affect the entire cache, for example IC IALLU.

- Operate by VA, for example IC IVAU.

- Operate by set/way, for example DC ISW.

The cache identification registers are:

- The Cache Type Register, CTR\_EL0, that defines:

- The minimum line length of any of the instruction caches affected by the instruction cache maintenance instructions.

- The minimum line length of any of the data or unified caches, affected by the data cache maintenance instruction.

- The cache indexing and tagging policy of the Level 1 instruction cache.

Note

It is IMPLEMENTATION DEFINED whether caches beyond the PoC will be reported by this mechanism, and because of the possible existence of system caches some caches before the PoC might not be reported. For more information about system caches see System level caches.

- Asingle Cache Level ID Register, CLIDR\_EL1, that defines:

- The type of cache that is implemented and can be maintained using the architected cache maintenance instructions that operate by set/way or operate on the entire cache at each cache level, up to the maximum of seven levels.

- The Level of Coherence (LoC) for the caches. See Terms used in describing the cache maintenance instructions for the definition of LoC.

- The Level of Unification Uniprocessor (LoUU) for the caches. See Terms used in describing the cache maintenance instructions for the definition of LoUU.

- An optional ICB field to indicate the boundary between the caches use for caching Inner Cacheable memory regions and those used only for caching Outer Cacheable regions.

- Asingle Cache Size Selection Register, CSSELR\_EL1, that selects the cache level and sort of cache (Instruction, Data/Unified/Tag) of the current Cache Size Identification Register.

- For each implemented cache that is identifiable by this mechanism, across all the levels of caching, a Cache Size Identification Register, CCSIDR\_EL1, that defines:

- The number of sets, associativity and line length of the cache. See Terms used in describing the cache maintenance instructions for a definition of these terms.

Note

From Armv8.3, multiple formats of the Cache Size Identification Register are supported. For more information, see Possible formats of the Cache Size Identification Register, CCSIDR\_EL1.

To determine the cache topology associated with a PE:

1. Read the Cache Type Register to find the indexing and tagging policy used for the Level 1 instruction cache. This register also provides the size of the smallest cache lines used for the instruction caches, and for the data and unified caches. These values are used in cache maintenance instructions.
2. Read the Cache Level ID Register to find what caches are implemented. The register includes seven Cache type fields, for cache levels 1 to 7. Scanning these fields, starting from Level 1, identifies the instruction, data or unified caches implemented at each level. This scan ends when it reaches a level at which no caches are defined. The Cache Level ID Register also specifies the Level of Unification (LoU) and the Level of Coherence (LoC) for the cache implementation.
3. For each cache identified at stage 2:
- Write to the Cache Size Selection Register to select the required cache. A cache is identified by its level, and whether it is:
5. -An instruction cache.
6. -Adata or unified cache.
- Read the Cache Size Identification Register to find details of the cache.

## D7.5.2.1 Possible formats of the Cache Size Identification Register, CCSIDR\_EL1

From Armv8.3, the Cache Size Identification Register, CCSIDR\_EL1 has two different formats available for defining the number of sets and associativity of the cache. For a definition of these terms, see Terms used in describing the cache maintenance instructions.

When FEAT\_CCIDX is implemented:

- CCSIDR\_EL1 is a 64-bit register.
- The length of the CCSIDR\_EL1.Assoc field is 21 bits. This limits the associativity of the currently selected cache to 2 21 .
- The length of the CCSIDR\_EL1.NumSets field is 24 bits. This limits the number of sets in the currently selected cache to 2 24 .

This is the 64-bit format of the Cache Size Identification Register.

When FEAT\_CCIDX is not implemented:

- CCSIDR\_EL1 is a 32-bit register.
- The length of the CCSIDR\_EL1.Assoc field is 10 bits. This limits the associativity of the currently selected cache to 2 10 .
- The length of the CCSIDR\_EL1.NumSets field is 15 bits. This limits the number of sets in the currently selected cache to 2 15 .

This is the 32-bit format of the Cache Size Identification Register.

When one of these formats is implemented, it is implemented across all the levels of caching.

## D7.5.3 Cacheability, cache allocation hints, and cache transient hints

Cacheability applies only to Normal memory, and can be defined independently for Inner and Outer cache locations. All types of Device memory are always treated as Non-cacheable.

As described in Memory types and attributes, the memory attributes include a cacheability attribute that is one of:

- Non-cacheable.
- Write-Through cacheable.
- Write-Back cacheable.

Cacheability attributes other than Non-cacheable can be complemented by a cache allocation hint . This is an indication to the memory system of whether allocating a value to a cache is likely to improve performance. In addition, it is IMPLEMENTATION DEFINED whether a cache transient hint is supported, see Transient cacheability hint.

The cache allocation hints are assigned independently for read and write accesses, and therefore when the Transient hint is supported the following cache allocation hints can be assigned:

For read accesses: Read-Allocate, Transient Read-Allocate, or No Read-Allocate.

For write accesses: Write-Allocate, Transient Write-Allocate, or No Write-Allocate.

Note

- ACacheable location with both No Read-Allocate and No Write-Allocate hints is not the same as a Non-cacheable location. A Non-cacheable location has coherency guarantees for all observers within the system that do not apply for a location that is Cacheable, No Read-Allocate, No Write-Allocate.
- Implementations can use the cache allocation hints to limit cache pollution to a part of a cache, such as to a subset of ways.
- For VMSAv8-64 translation table walks, the TCR\_ELx.{IRGN n , ORGN n } fields define the memory attributes of the translation tables, including the cacheability. However, this assignment supports only a subset of the cacheability attributes described in this section.

The architecture does not require an implementation to make any use of cache allocation hints. This means an implementation might not make any distinction between memory locations with attributes that differ only in their cache allocation hint.

## D7.5.3.1 Transient cacheability hint

In Armv8, it is IMPLEMENTATION DEFINED whether a Transient hint is supported. In an implementation that supports the Transient hint, the Transient hint is a qualifier of the cache allocation hints, and indicates that the benefit of caching is for a relatively short period. It indicates that it might be better to restrict allocation of transient entries, to avoid possibly casting-out other, less transient, entries.

Note

The architecture does not specify what is meant by a relatively short period .

The description of the AArch64 MAIR\_EL1, MAIR\_EL2, and MAIR\_EL3 registers, and the AArch32 MAIR0, MAIR1, HMAIR0, and HMAIR1 registers, includes the assignment of the Transient hint in an implementation that supports this option. In this assignment:

- The Transient hint is defined independently for Inner Cacheable and Outer Cacheable memory regions.
- Asingle Transient hint applies to both read and write accesses to a memory region.

## D7.5.4 Cacheable MEC transactions

RKLLJD All statements in this section and subsections require implementation of FEAT\_MEC.

INWLXR

Each cache level is permitted to independently implement the behaviors described in this section.

| R NMSQG   | Any memory location that has a Normal Cacheable attribute can be allocated into a cache, associated with the MECID of the translation that provided the Normal Cacheable attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FKNTM   | In situations where Normal Non-cacheable memory is permitted to be cached in an instruction cache, it is associated with the MECID of the translation that provided the Non-cacheable attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I RDDXP   | Speculative allocation of Normal memory only occurs from the current Exception level or a higher Exception level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R MVGSH   | If a Normal memory location is allocated to a cache entry due to a write access or a cache writeback, then the cache entry is associated with the MECID of that write access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R KZCZX   | If a cache entry for a Normal memory location is updated due to a write access or a cache writeback, then it is optional to associate the cache entry with the MECID of that write access. If FEAT_RME_GDI is implemented, and the PA space is System Agent (SA) or Non-secure Protected (NSP), then the MECID value is updated on a write access or a cache writeback.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R PJNMC   | If a write access targets a location that is cached and associated with a different MECID, and the write access is smaller than the Cache writeback granule, then: • If the PA space is not SA or NSP, one of the following CONSTRAINED UNPREDICTABLE behaviors occur: - The write access succeeds, the location contents become UNKNOWN, and the MECID value associated with the cache entry is updated. - The write access succeeds as though the MECID values did not mismatch, and it is OPTIONAL whether the MECID value associated with the cache entry is updated. - The write access succeeds, the written location contents are updated, the unwritten locations within the Cache writeback granule become UNKNOWN, and the MECID value associated with the cache entry is updated. • If the PA space is SA or NSP, then the write access succeeds, the written location contents are updated, the |
| R VXMVW   | If a read access, including a data read, instruction fetch, or a translation table lookup, targets a location that is cached and associated with a different MECID, then: • If the PA space is not SA or NSP, one of the following CONSTRAINED UNPREDICTABLE behaviors occur: - The data returned by the read access is UNKNOWN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I HJXYJ   | Arm recommends that the value of all ones is used for the UNKNOWN data, inR PJNMC andR VXMVW .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| I MWGQN   | FEAT_RME_GDI promotes MECto a primary security mechanism across contexts within the NSP and SA PA spaces. R KZCZX ,R PJNMC ,R VXMVW and I HJXYJ are designed to prevent plain text data leakages in caches, across contexts. They do not prevent data corruption across contexts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R NTHZN   | AMECIDmismatch that results in UNKNOWN data does not cause a plaintext data leak between MECIDs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I TYGBH   | If a cache detects a MECID mismatch, then it is permitted to record the PA and mismatched MECIDs and generate an IMPLEMENTATION DEFINED interrupt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| R BSTPQ   | Associating Normal Cacheable memory accesses with a MECID is required whether or not the target location is encrypted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## D7.5.5 Enabling and disabling the caching of memory accesses

Cacheability control fields can force all memory locations with the Normal memory type to be treated as Non-cacheable, regardless of their assigned Cacheability attribute. Independent controls are provided for each stage of address translation, with separate controls for:

- Data accesses. These controls also apply to accesses to the translation tables.
- Instruction accesses.

Note

These Cacheability controls replace the cache enable controls provided in previous versions of the Arm architecture.

The Cacheability control fields and their effects are as follows:

## For the EL1&amp;0 translation regime

- When the value of SCTLR\_EL1.C is 0:
- -All stage 1 translations for data accesses to Normal memory are Non-cacheable.
- -All accesses to the EL1&amp;0 stage 1 translation tables are Non-cacheable.
- When the value of SCTLR\_EL1.I is 0:
- -All stage 1 translations for instruction accesses to Normal memory are Non-cacheable.
- When the value of HCR\_EL2.CD is 1:
- -All stage 2 translations for data accesses to Normal memory are Non-cacheable.
- -All accesses to the EL1&amp;0 stage 2 translation tables are Non-cacheable.
- When the value of HCR\_EL2.ID is 1:
- -All stage 2 translations for instruction accesses to Normal memory are Non-cacheable.
- When the value of HCR\_EL2.DC is 1, all stage 1 translations and all accesses to the EL1&amp;0 stage 1 translation tables, are treated as accesses to Normal Non-shareable Inner Write-Back Cacheable Read-Allocate Write-Allocate, Outer Write-Back Cacheable Read-Allocate Write-Allocate memory, regardless of the value of SCTLR\_EL1.{I, C}. This applies to translations for both data and instruction accesses.

## Note

- The stage 1 and stage 2 cacheability attributes are combined as described in Combining stage 1 and stage 2 Cacheability attributes for Normal memory.
- The SCTLR\_EL1.{C, I} and HCR\_EL2.DC fields have no effect on the EL2, EL2&amp;0, and EL3 translation regimes.
- The HCR\_EL2.{ID, CD} fields affect only stage 2 of the EL1&amp;0 translation regime.
- When FEAT\_XS is implemented, the SCTLR\_EL1.{C, I} and HCR\_EL2.{ID, CD} fields have no effect on the value of the XS attribute.
- When EL2 is using AArch64 and EL1 is using AArch32, the HCR\_EL2.{ID, CD, DC} controls apply as described here, but the EL1 controls are SCTLR.{C, I}.

## For the EL2 translation regime

- When the value of SCTLR\_EL2.C is 0:
- -All data accesses to Normal memory using the EL2 translation regime are Non-cacheable.
- -All accesses to the EL2 translation tables are Non-cacheable.
- When the value of SCTLR\_EL2.I is 0:
- -All instruction accesses to Normal memory using the EL2 translation regime are Non-cacheable.

## Note

- The SCTLR\_EL2.{I, C} fields have no effect on the EL1&amp;0 and EL3 translation regimes.
- When FEAT\_XS is implemented, the SCTLR\_EL2.{I, C} fields have no effect on the value of the XS attribute.

## For the EL2&amp;0 translation regime

- When the value of SCTLR\_EL2.C is 0:
- -All stage 1 translations for data accesses to Normal memory are Non-cacheable.
- -All accesses to the EL2&amp;0 stage 1 translation tables are Non-cacheable.
- When the value of SCTLR\_EL2.I is 0:
- -All stage 1 translations for instruction accesses to Normal memory are Non-cacheable.

## In addition:

- For translation regimes other than the EL1&amp;0 translation regime, if the value of SCTLR\_ELx.M is 0, indicating that stage 1 translations are disabled for that translation regime, then:
- -If the value of SCTLR\_ELx.I is 0, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Non-cacheable, Outer Non-cacheable.
- -If the value of SCTLR\_ELx.I is 1, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Write-Through cacheable, Outer Write-Through cacheable.
- For the EL1&amp;0 translation regime, if the value of SCTLR\_EL1.M is 0, indicating that stage 1 translations are disabled for that translation regime, and the value of HCR\_EL2.DC is 0:
- -If the value of SCTLR\_EL1.I is 0, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Non-cacheable, Outer Non-cacheable.
- -If the value of SCTLR\_EL1.I is 1, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Write-Through Cacheable, Outer Write-Through Cacheable.

The effect of SCTLR\_ELx.C, HCR\_EL2.DC and HCR\_EL2.CD is reflected in the result of the address translation instructions in the PAR when these bits have an effect on the stages of translation being reported in the PAR.

Note

- In conjunction with the requirements in Non-cacheable accesses and instruction caches, the requirements in this section mean the architecturally required effect of SCTLR\_ELx.I is limited to its effect on caching instruction accesses in unified caches.
- This specification can give rise to different cacheability attributes between instruction and data accesses to the same location. Where this occurs, the measures for mismatch memory attributes described in Mismatched memory attributes must be followed to manage the corresponding loss of coherency.

## D7.5.6 Behavior of caches at reset

The behavior of caches at reset is as follows:

- All caches reset to IMPLEMENTATION DEFINED states that might be UNKNOWN.
- The Cacheability control fields described in Enabling and disabling the caching of memory accesses reset to values that force all memory locations to be treated as Non-cacheable.

Note

When FEAT\_XS is implemented, the SCTLR\_EL2.{I, C} fields have no effect on the value of the XS attribute.

## For the EL3 translation regime

- When the value of SCTLR\_EL3.C is 0:
- -All data accesses to Normal memory using the EL3 translation regime are Non-cacheable.
- -All accesses to the EL3 translation tables are Non-cacheable.
- When the value of SCTLR\_EL3.I is 0:
- -All instruction accesses to Normal memory using the EL3 translation regime are Non-cacheable.

Note

- The SCTLR\_EL3{I, C} fields have no effect on the EL1&amp;0, EL2, and EL2&amp;0 translation regimes.
- When FEAT\_XS is implemented, the SCTLR\_EL3.{I, C} fields have no effect on the value of the XS attribute.

Note

This applies only to the controls that apply to the Translation regime that is used by the Exception level and Security state entered on reset.

- An implementation can require the use of a specific cache initialization routine to invalidate its storage array before caching is enabled. The exact form of any required initialization routine is IMPLEMENTATION DEFINED, and the routine must be documented clearly as part of the documentation of the device.
- If an implementation permits cache hits when the Cacheability control fields force all memory locations to be treated as Non-cacheable then the cache initialization routine must:
- -Provide a mechanism to ensure the correct initialization of the caches.
- -Be documented clearly as part of the documentation of the device.

In particular, if an implementation permits cache hits when the Cacheability controls force all memory locations to be treated as Non-cacheable, and the cache contents are not invalidated at reset, the initialization routine must avoid any possibility of running from an uninitialized cache. It is acceptable for an initialization routine to require a fixed instruction sequence to be placed in a restricted range of memory.

- Arm recommends that whenever an invalidation routine is required, it is based on the cache maintenance instructions.

See also TLB behavior at reset.

## D7.5.7 Non-cacheable accesses and instruction caches

In AArch64 state, instruction accesses to Non-cacheable Normal memory can be held in instruction caches.

Correspondingly, the sequence for ensuring that modifications to instructions are available for execution must include invalidation of the modified locations from the instruction cache, even if the instructions are held in Normal Non-cacheable memory. This includes cases where System register Cacheability control fields force instruction accesses to memory to be Non-cacheable.

Therefore when using self-modified code in Non-cacheable space in a uniprocessor system, the following sequence is required:

```
; Enter this code with <Wt> containing the new 32-bit instruction ; to be held at a location pointed to by <Xn> in Normal Non-cacheable memory. STR <Wt>, [Xn] DSB ISH; Ensure visibility of the data stored IC IVAU, [Xn] ; Invalidate instruction cache by VA to PoU DSB ISH; Ensure completion of the invalidations ISB ;
```

In a multiprocessor system, the IC IV AU for a non-cacheable location is broadcast to all PEs within the Inner Shareable domain of the PE running this sequence. This is despite non-cacheable normal memory locations being treated as Outer Shared in other parts of the architecture.

Additional software steps might be required to synchronize the threads with other PEs. This might be necessary so that the PEs executing the modified instructions can execute an ISB after completing the invalidation, and to avoid issues associated with concurrent modification and execution of instruction sequences. See also Concurrent modification and execution of instructions and Concurrent modification and execution of instructions.

Larger blocks of instructions can be modified using the IC IALLU instruction for a uniprocessor system, or an IC IALLUIS for a multiprocessor system.

Note

This section applies even when the Cacheability control fields force instruction accesses to memory in AArch64 state to be Non-cacheable, as described in Enabling and disabling the caching of memory accesses.

## D7.5.8 About cache maintenance in AArch64 state

The following sections give general information about cache maintenance:

- Terms used in describing the cache maintenance instructions.
- Abstraction of the cache hierarchy.

The following sections describe the A64 cache maintenance instructions:

- The instruction cache maintenance instruction ( IC ).
- The data cache maintenance instruction ( DC ).

Note

Some descriptions of the cache maintenance instructions refer to the cacheability of the address on which the instruction operates. The Cacheability of an address is determined by the applicable translation table entry for that address, as modified by any applicable System register Cacheability controls, such as the SCTLR\_EL1.{I, C} controls.

## D7.5.8.1 Terms used in describing the cache maintenance instructions

A memory location is a byte that is associated with an address in a particular address space. For example, address 0x1000 in the Root physical address space is a different memory location from address 0x1000 in the Secure physical address space.

The term Resource means a physical entity that can be accessed at one or more memory locations. A Resource associated with a physical address space is accessible in that physical address space.

Note

Examples of a Resource include:

- AnMMIOregister that is accessible at both the memory location with address 0x2000 in the Non-secure physical address space, and at memory location with address 0x2000 in the Secure address space.
- AnSRAMthatis accessible only at the memory location with address 0x3000 in the Root physical address space.
- Abyte of memory that can be accessible at a fixed address but in different physical address spaces, determined by a configuration option.

Cache maintenance instructions are defined to act on particular memory locations. Depending on the instruction type, the scope is defined as one of:

- By the virtual address of the memory location to be maintained, referred to as operating by VA .
- By the physical address of the memory location to be maintained, referred to as operating by PA .
- By a mechanism that describes the location in the hardware of the cache, referred to as operating by set/way .

In addition, for instruction caches, there are instructions that invalidate all entries.

The following subsections define the terms used in the descriptions of the cache maintenance instructions:

- Terminology for cache maintenance instructions operating by set/way.
- Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

Note

There is no terminology specific to cache maintenance instructions that operate by V A. When all applicable stages of translation are disabled, the V A used is identical to the PA. For more information about memory system behavior when address translation is disabled, see The effects of disabling an address translation stage.

## D7.5.8.1.1 Terminology for cache maintenance instructions operating by set/way

Cache maintenance instruction that operate by set/way refer to the particular structures in a cache. Three parameters describe the location in a cache hierarchy that an instruction works on. These parameters are:

Level

The cache level of the hierarchy. The number of levels of cache is IMPLEMENTATION DEFINED. The cache levels that can be managed using the architected cache maintenance instructions that operate by set/way can be determined from the CLIDR\_EL1.

In the Arm architecture, the lower numbered cache levels are those closest to the PE. See Memory hierarchy.

| Set   | Each level of a cache is split up into a number of sets . Each set is a set of locations in a cache level to which an address can be assigned. Usually, the set number is an IMPLEMENTATION DEFINED function of an address.   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Way   | The associativity of a cache is the number of locations in a set to which a specific address can be assigned. The way number specifies one of these locations. In the Arm architecture, ways are numbered from 0.             |

Note

Because the allocation of a memory address to a cache location is entirely IMPLEMENTATION DEFINED, Arm expects that most portable software will use only the cache maintenance instructions by set/way as single steps in a routine to perform maintenance on the entire cache.

## D7.5.8.1.2 Terminology for Clean, Invalidate, and Clean and Invalidate instructions

Caches introduce coherency problems in two possible directions:

1. An update to a memory location by a PE that accesses a cache might not be visible to other observers that can access memory. This can occur because new updates are still in the cache and are not visible yet to the other observers that do not access that cache.
2. Updates to memory locations by other observers that can access memory might not be visible to a PE that accesses a cache. This can occur when the cache contains an old, or stale , copy of the memory location that has been updated.

The Clean and Invalidate instructions address these two issues. The definitions of these instructions are:

## Clean

## Invalidate

Acache clean instruction ensures that updates made by an observer that controls the cache are made visible to other observers that can access memory at the point to which the instruction is performed. Once the Clean has completed, the new memory values are guaranteed to be visible to the point to which the instruction is performed, for example to the Point of Unification.

The cleaning of a cache entry from a cache can overwrite memory that has been written by another observer only if the entry contains a location that has been written to by an observer in the shareability domain of that memory location.

Acache invalidate instruction ensures that updates made visible by observers that access memory at the point to which the invalidate is defined, are made visible to an observer that controls the cache. This might result in the loss of updates to the locations affected by the invalidate instruction that have been written by observers that access the cache, if those updates have not been cleaned from the cache since they were made.

If the address of an entry on which the invalidate instruction operates is Normal, Non-cacheable or any type of Device memory then an invalidate instruction also ensures that this address is not present in the cache.

Note

Entries for addresses that are Normal Cacheable can be allocated to the cache at any time, and so the cache invalidate instruction cannot ensure that the address is not present in a cache.

## Clean and Invalidate

Acache clean and invalidate instruction behaves as the execution of a clean instruction followed immediately by an invalidate instruction. Both instructions are performed to the same location.

The points to which a cache maintenance instruction can be defined differ depending on whether the instruction operates by VA or by set/way:

- For instructions operating by set/way, the point is defined to be to the next level of caching. For the All operations, the point is defined as the Point of Unification for each location held in the cache.
- For instructions operating by V A:
- -The instructions that FEAT\_OCCMO implements operate to the outer cache level.
- -For all other instructions operating by V A, the following conceptual points are defined:

## Point of Coherency (PoC)

The point at which all agents that can access memory are guaranteed to see the same copy of a memory location for accesses of any memory type or cacheability attribute. In many cases this is effectively the main system memory, although the architecture does not prohibit the implementation of caches beyond the PoC that have no effect on the coherency between memory system agents.

Note

The presence of system caches can affect the determination of the Point of Coherency as described in System level caches.

## Point of Physical Aliasing (PoPA)

The point at which updates to one memory location of a Resource are visible to all other memory locations of that Resource, for accesses to that point of any memory type or cacheability attribute, for all agents that can access memory. The relationship between the PoPA and the PoC is such that a clean of a written memory location to the PoPA means that no agent in the system can subsequently reveal an old value of the memory location by performing an invalidate operation to the PoC.

## Point of Encryption (PoE)

The point in the memory system where any write that has reached that point is encrypted with the context associated with the MECID that is associated with that write.

Cache maintenance operations to the PoPA are sufficient to affect all caches before the PoE.

## Point of Unification (PoU)

The PoU for a PE is the point by which the instruction and data caches and the translation table walks of that PE are guaranteed to see the same copy of a memory location. In many cases, the Point of Unification is the point in a uniprocessor memory system by which the instruction and data caches and the translation table walks have merged.

The PoU for an Inner Shareable shareability domain is the point by which the instruction and data caches and the translation table walks of all the PEs in that Inner Shareable shareability domain are guaranteed to see the same copy of a memory location. Defining this point permits self-modifying software to ensure future instruction fetches are associated with the modified version of the software by using the standard correctness policy of:

1. Clean data cache entry by address.
2. Invalidate instruction cache entry by address.

## Point of Persistence (PoP)

When FEAT\_DPB is implemented: The point in a memory system, if it exists, at or beyond the Point of Coherency, where a write to memory is maintained when system power is removed, and reliably recovered when power is restored to the affected locations in memory.

When FEAT\_DPB and FEAT\_DPB2 are implemented: The point in a memory system where there is a system guarantee that there is sufficient energy within the system to ensure that a write to memory will be persistent if system power is removed.

Note

Such memory is sometimes called non-volatile memory. For example, the Storage-class memory shown in Figure B2-1 could be used as target memory for this feature.

## Point of Deep Persistence (PoDP)

The point in a memory system where any writes that have reached that point are persistent, even in the event of an instantaneous hardware failure of the power system.

## Point of Physical Storage (PoPS)

The point in the memory hierarchy from where, following a clean and invalidate of a Location to the Point of Physical Storage, the first subsequent read of the Location will always return data.

Note

The Point of Physical Storage is usually after all caches in the system, including system caches that are invisible to the software for the purpose of managing coherency, such as those described in System level caches.

The following fields in the CLIDR\_EL1 relate to the PoC and PoU:

## LoC, Level of Coherence

This field defines the last level of cache that must be cleaned or invalidated when cleaning or invalidating to the Point of Coherency. The LoC value is a cache level, so, for example, if LoC contains the value 3:

- Aclean to the Point of Coherency operation requires the level 1, level 2 and level 3 caches to be cleaned.
- Level 4 cache is the first level that does not have to be maintained.

If the LoC field value is 0x0 , this means that no levels of cache need to cleaned or invalidated when cleaning or invalidating to the Point of Coherency.

If the LoC field value is a nonzero value that corresponds to a level that is not implemented, this indicates that all implemented caches are before the Point of Coherency.

## LoUU, Level of Unification, uniprocessor

This field defines the last level of data cache that must be cleaned, or the last level of instruction cache that must be invalidated, when cleaning or invalidating to the Point of Unification for the PE. As with LoC, the LoUU value is a cache level.

If the LoUU field value is 0x0 , this means that no levels of data cache need to be cleaned or invalidated when cleaning or invalidating to the Point of Unification.

If the LoUU field value is a nonzero value that corresponds to a level that is not implemented, this indicates that all implemented caches are before the Point of Unification.

## LoUIS, Level of Unification, Inner Shareable

In any implementation:

- This field defines the last level of data or unified cache that must be cleaned, or the last level of instruction or unified cache that must be invalidated, when cleaning or invalidating to the Point of Unification for the Inner Shareable shareability domain. As with LoC, the LoUIS value is a cache level.
- If the LoUIS field value is 0x0 , this means that no levels of data or unified cache need to cleaned or invalidated when cleaning or invalidating to the Point of Unification for the Inner Shareable shareability domain.
- If the LoUIS field value is a nonzero value that corresponds to a level that is not implemented, this indicates that all implemented caches are before the Point of Unification.

## D7.5.8.2 Abstraction of the cache hierarchy

The following subsections describe the abstraction of the cache hierarchy:

- Cache maintenance instructions that operate by V A.
- Cache maintenance instructions that operate by set/way.

## D7.5.8.2.1 Cache maintenance instructions that operate by VA

The VA-based cache maintenance instructions are described as operating by V A. Each of these instructions is always qualified as being one of:

- Performed to the Point of Coherency.
- Performed to the Point of Unification.
- When FEAT\_DPB is implemented, performed to the Point of Persistence.
- When FEAT\_DPB2 is implemented, performed to the Point of Deep Persistence.
- When FEAT\_PoPS is implemented, performed to the Point of Physical Storage.
- When FEAT\_OCCMO is implemented, performed to the Outer Cache level.

See Terms used in describing the cache maintenance instructions for definitions of these terms, and for more information about possible meanings of V A.

A64 Cache maintenance instructions lists the V A-based maintenance instructions.

The CTR\_EL0 holds minimum line length values for:

- The instruction caches.
- The data and unified caches.

These values support efficient invalidation of a range of V As, because this value is the most efficient address stride to use to apply a sequence of V A-based maintenance instructions to a range of V As.

For the Invalidate data or unified cache line by V A instruction, the Cache Write-back Granule field of the CTR\_EL0 defines the maximum granule that a single invalidate instruction can invalidate. This meaning of the Cache Write-back Granule is in addition to its defining the maximum size that can be written back.

## D7.5.8.2.2 Cache maintenance instructions that operate by set/way

A64 Cache maintenance instructions lists the set/way-based maintenance instructions. Some encodings of these instructions include a required field that specifies the cache level for the instruction:

- Aclean instruction cleans from the level of cache specified through to at least the next level of cache, moving further from the PE.
- An invalidate instruction invalidates only at the level specified.

## D7.5.9 A64 Cache maintenance instructions

The A64 cache maintenance instructions are part of the A64 System instruction class in the register encoding space. For encoding details and other general information on these System instructions, see System instructions, SYS and Cache maintenance instructions, and data cache zero operations.

The following subsections give more information about these instructions:

- The instruction cache maintenance instruction ( IC ).
- The data cache maintenance instruction ( DC ).
- EL0 accessibility of cache maintenance instructions.
- General requirements for the scope of maintenance instructions.
- Effects of instructions that operate by V A to the PoC.
- Effects of instructions that operate by V A to the Outer Cache level.
- Effects of instructions that operate by V A to the PoP.
- Effects of instructions that operate by V A to the PoPS.
- Effects of instructions that operate by V A to the PoU.
- Effects of All and set/way maintenance instructions.
- Effects of virtualization and Security state on the cache maintenance instructions.

- Boundary conditions for cache maintenance instructions.
- Ordering and completion of data and instruction cache instructions.
- Performing cache maintenance instructions.

## D7.5.9.1 The instruction cache maintenance instruction ( IC )

System instructions describes the A64 assembly syntax for this instruction.

When an IC instruction requires an address argument this takes the form of a 64-bit register that holds the V A argument. No alignment restrictions apply for this address.

Any cache maintenance instruction operating by V A includes as part of any required V A to PA translation:

- For an instruction executed at EL1, or at EL2 when the Effective value of HCR\_EL2.E2H is 1, the current ASID.
- The current Security state.
- Whether the instruction was executed at EL1 or EL2.
- For an instruction executed at EL1, the current VMID.

That VA to PA translation might fault. However, for an instruction cache maintenance instruction that operates by V A:

- It is IMPLEMENTATION DEFINED whether the instruction can generate:
- -An Access flag fault.
- -ATranslation fault.
- The instruction cannot generate a Permission fault, except for:
- -The possible generation of a Permission fault by the execution of an IC IV AU instruction at EL0 when the specified address does not have read access at EL0, as described in EL0 accessibility of cache maintenance instructions.
- -When FEAT\_CMOW is implemented, the possible generation of a Permission fault by:
- -The execution of an IC IV AU instruction at EL0 when the specified address has stage 1 read permission, but does not have stage 1 write permission.
- -The execution of an IC IV AU instruction at EL1 or EL0 when the specified address does not have stage 2 write permission.
- -The possible Permission fault on a Stage 2 fault on a stage 1 translation table walk.

For more information about possible faults on a cache maintenance instruction that operates by V A, see Memory aborts.

See also Ordering and completion of data and instruction cache instructions.

If CTR\_EL0.DIC is 1, then it is IMPLEMENTATION DEFINED whether each of the IC instructions is treated as a NOP .

If an IC instruction that operates by V A is treated as a NOP , it does not perform translation and all the following apply:

- No MMU faults can be generated.
- If hardware update of AF is enabled, AF is not required to be set.

If an IC instruction is treated as a NOP , then it is IMPLEMENTATION DEFINED whether the execution of the instruction can be trapped.

## D7.5.9.2 The data cache maintenance instruction ( DC )

System instructions describes the A64 assembly syntax for this instruction.

When a DC instruction requires a set/way/level argument this takes the form of a 64-bit register, the upper 32 bits of which are RES0.

If a data cache maintenance by set/way instruction specifies a set, way, or level argument that is larger than the value supported by the implementation then the instruction is CONSTRAINED UNPREDICTABLE, see Out of range values of the Set/Way/Index fields in cache maintenance instructions or the instruction description.

When a DC instruction requires an address argument this takes the form of a 64-bit register that holds the V A argument. No alignment restrictions apply for this address.

Any cache maintenance instruction operating by V A includes as part of any required V A to PA translation:

- For an instruction executed at EL1, or at EL2 when the Effective value of HCR\_EL2.E2H is 1, the current ASID.
- The current Security state.
- Whether the instruction is executed at EL1 or EL2.
- For an instruction executed at EL1, the current VMID.

That VA to PA translation might fault. However, a data or unified cache maintenance instruction that operates by V A cannot generate a Permission fault except in the following cases:

- The possible generation of a Permission fault by:
- -The execution of a DC IVAC instruction when the specified address does not have write permission.
- -The execution of an enabled DC instruction at EL0 when the specified address does not have read access at EL0, as described in EL0 accessibility of cache maintenance instructions.

The description of Permission faults includes possible constraints on the generation of Permission faults on cache maintenance by VA instructions.

- When FEAT\_CMOW is implemented, the possible generation of a Permission fault by:
- -The execution of a DC instruction that operates by V A and performs clean and invalidate at EL0 when the specified address does not have stage 1 write permission.
- -The execution of a DC instruction that operates by V A and performs clean and invalidate at EL1 or EL0 when the specified address does not have stage 2 write permission.
- The possible Permission fault on a Stage 2 fault on a stage 1 translation table walk.

For more information about possible faults on a V A to PA translation, see Memory aborts.

When executed at EL1, a DC ISW instruction performs a clean and invalidate, meaning it performs the same maintenance as a DC CISW instruction, if all of the following apply:

- EL2 is implemented and enabled in the current Security state.
- Either:
- -The value of HCR\_EL2.SWIO is 1, forcing a cache clean to perform a clean and invalidate.
- -The value of HCR\_EL2.VM is 1, meaning EL1&amp;0 stage two address translation is enabled.

When executed at EL1, a DC IVAC instruction performs a clean and invalidate, meaning it performs the same maintenance as a DC CIVAC instruction, if all of the following apply:

- EL2 is implemented and enabled in the current Security state.
- The value of HCR\_EL2.VM is 1, meaning EL1&amp;0 stage two address translation is enabled.

Note

The forcing of a clean instruction to perform a clean invalidate applies to the AArch32 cache maintenance instructions DCIMVAC and DCISW. See AArch32 data cache maintenance instructions (DC*).

When FEAT\_DPB is implemented, meaning the DC CVAP instruction is implemented, if the memory system does not support the Point of Persistence, a data cache clean to the PoP, DC CV AP, behaves as a data cache clean to the PoC, DC CVAC.

Note

- Support for the Point of Persistence does not change the definition or behavior of the CLIDR\_EL1 System register.
- Because a DSB SYS instruction will not complete until all previous DC CV AP instructions have completed, the following sequence can be used to ensure the completion of any store to the Point of Persistence, where the store might be to Non-cacheable memory:
- If caches that are invisible to the programmer exist beyond the Point of Coherency but before the Point of Persistence and hold data that is marked as Non-cacheable, the DC CVAP operation causes the Non-cacheable locations to be cleaned from those caches.

```
DMB ; Note this can be any DMB that applies to both loads and stores DC CVAP, Xt DSB SYS
```

If there are caches after the Point of Coherency and FEAT\_PoPS is not implemented, then the DC CIV AC and DC CIGDVAC instructions are not sufficient to remove all copies of a poisoned Location and it is IMPLEMENTATION DEFINED whether any IMPLEMENTATION DEFINED mechanism exists to remove poison from a Location.

See Clearing Deferred errors from poisoned Locations for more information on removing poison from a Location.

If a memory fault that sets the FAR for the translation regime applicable for the cache maintenance instruction is generated from a data cache maintenance instruction, the FAR holds the address specified in the register argument of the instruction.

Note

Despite its mnemonic, DC ZVA is not a cache maintenance instruction.

See also EL0 accessibility of cache maintenance instructions and Ordering and completion of data and instruction cache instructions.

For all the following DC instructions, it is IMPLEMENTATION DEFINED whether the instruction is treated as a NOP :

- ADCtothe PoU and the LoUIS and LoUU are 0.
- ADCtothe PoC and the LoC is 0.
- ADCtothe PoP and the memory system does not support the Point of Persistence, and the LoC is 0.
- ADCtothe PoDP and the memory system does not support the Point of Deep Persistence, and does not support the Point of Persistence, and the LoC is 0.

If FEAT\_OCCMO is implemented, and in the system the PoC is before any levels of cache, then Arm expects it is possible to implement DC CIVAOC, DC CIGDVAOC, DC CVAOC, and DC CGDVAOC as NOP s. In systems with no Outer cache levels, these instructions can be implemented respectively as DC CIV AC, DC CIGDV AC, DC CVAC, and DCCGDVAC.

If a DC instruction that operates by V A is treated as a NOP , it does not perform translation and all the following apply:

- No MMU faults can be generated.
- If hardware update of AF is enabled, AF is not required to be set.

If a DC instruction is treated as a NOP , then it is IMPLEMENTATION DEFINED whether the execution of the instruction can be trapped.

## D7.5.9.3 EL0 accessibility of cache maintenance instructions

Software executing at EL0 can access data cache maintenance instructions and instruction cache maintenance instructions that operate by virtual address. When EL0 use of these instructions is disabled because SCTLR\_EL1.UCI is 0, executing one of these instructions at EL0 generates a trap to EL1, which is reported using EC = 0x18 . When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the control is from SCTLR\_EL2.

Note

DCCVAPis implemented only if FEAT\_DPB is implemented.

For these instructions read access permission for the virtual address is required. When the value of SCTLR\_EL1.UCI is 1:

- If the DC instruction is executed at EL0 and the address specified in the argument cannot be read at EL0, a Permission fault might be generated.
- For the IC IV AU instruction, if the instruction is executed at EL0 and the address specified in the argument cannot be read at EL0, it is IMPLEMENTATION DEFINED whether a Permission fault is generated.
- When FEAT\_CMOW is implemented, for the DC instructions that operate by VA and perform clean and invalidate, and the IC instructions that operate by V A, write access permission is also required as follows:
- -When SCTLR\_EL1.CMOW is 1, if the instruction executed at EL0 does not have stage 1 write permission, a Permission fault is generated.
- -When HCRX\_EL2.CMOW is 1, if the instruction executed at EL0 does not have stage 2 write permission, a Permission fault is generated.

Note

This stage 2 access permission also applies to the DCCIMVAC and ICIMVAU AArch32 cache maintenance instructions.

For more information, see the description of Permission faults, In the case of a DC instruction executed at EL0 when the address specified cannot be read at EL0 the Permission fault is generated unless one of the permitted constraints described in that section applies and means the fault cannot be generated.

Software can read the CTR\_EL0 to discover the stride needed for cache maintenance instructions. The SCTLR\_EL1.UCT bit enables EL0 access to the CTR\_EL0. When EL0 access to the Cache Type register is disabled, a register access instruction executed at EL0 is trapped to EL1 using EC = 0x18 .

## D7.5.9.4 General requirements for the scope of maintenance instructions

The specification of the cache maintenance instructions describes what each instruction is guaranteed to do in a system. It does not limit other behaviors that might occur, provided they are consistent with the requirements described in General behavior of the caches, Behavior of caches at reset, and Prefetching into cache.

This means that as a side-effect of a cache maintenance instruction:

- Any location in the cache might be cleaned.
- Any unlocked location in the cache might be cleaned and invalidated.

Note

Arm recommends that, for best performance, such side-effects are kept to a minimum. Arm strongly recommends that the side-effects of operations performed in one Security state do not have a significant performance impact on execution in another Security state.

If an implementation can overwrite Allocation Tags in memory that have been written by another observer, where the Allocation Tags have not been written by an observer in the Shareability domain of that memory location, then:

- Acache maintenance operation which cleans data from a cache level must also clean the associated Allocation Tags.
- Acache maintenance operation which invalidates, or cleans and invalidates data from a cache level, must also clean and invalidate the associated Allocation Tags.

## D7.5.9.5 Effects of instructions that operate by VA to the PoC

For Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, cache maintenance instructions that operate by VA to the PoC affect the caches of other PEs in the shareability domain described by the shareability attributes of the VA supplied with the instruction.

For Device memory or Normal memory that is Inner Non-cacheable, Outer Non-cacheable, these instructions affect the caches of all PEs in the Outer Shareable shareability domain of the PE on which the instructions are operating.

In all cases, for any affected PE, these instructions affect all data and unified caches to the PoC. Table D7-3 shows the scope of these Data and unified cache maintenance instructions.

## Table D7-3 PEs affected by cache maintenance instructions to the PoC

| Shareability    | PEs affected                                                                                | Effective to                 |
|-----------------|---------------------------------------------------------------------------------------------|------------------------------|
| Non-shareable   | The PE executing the instruction                                                            | The PoC of the entire system |
| Inner Shareable | All PEs in the same Inner Shareable shareability domain as the PE executing the instruction | The PoC of the entire system |
| Outer Shareable | All PEs in the same Outer Shareable shareability domain as the PE executing the instruction | The PoC of the entire system |

Note

It is IMPLEMENTATION DEFINED by the system whether the cache maintenance instructions have an effect on the caches of observers that are not PEs within the affected shareability domain to which the cache maintenance instructions apply.

## D7.5.9.6 Effects of instructions that operate by VA to the Outer Cache level

The behaviors in this section apply if FEAT\_OCCMO is implemented.

For Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, cache maintenance instructions that operate by VA to the Outer cache level affect the caches of other PEs in the shareability domain described by the shareability attributes of the V A supplied with the instruction.

For Device memory and Normal memory that is Inner Non-cacheable, Outer Non-cacheable, these instructions affect the caches of all PEs in the Outer Shareable shareability domain of the PE on which the instruction is operating.

In all cases, for any affected PE, these instructions affect all data caches to the Outer cache level. Table D7-4 shows the scope of these Data cache maintenance instructions.

## Table D7-4 PEs affected by cache maintenance instructions to the Outer cache level

| Shareability    | PEs affected                                                                                | Effective to          |
|-----------------|---------------------------------------------------------------------------------------------|-----------------------|
| Non-shareable   | The PE executing the instruction                                                            | The Outer cache level |
| Inner Shareable | All PEs in the same Inner Shareable shareability domain as the PE executing the instruction | The Outer cache level |
| Outer Shareable | All PEs in the same Outer Shareable shareability domain as the PE executing the instruction | The Outer cache level |

Note

It is IMPLEMENTATION DEFINED by the system whether the cache maintenance instructions have an effect on the caches of observers that are not PEs within the affected shareability domain to which the cache maintenance instructions apply.

## D7.5.9.7 Effects of instructions that operate by PA to the PoPA

Caches are affected by cache maintenance instructions to the PoPA. For those caches, the operations behave as a clean and invalidate. Data cache maintenance instructions that operate by PA to the PoPA have all of the following properties:

- The instructions affect all caches in the Outer Shareable shareability domain to the PoPA for all copies of the memory location specified by the instruction.
- The instructions are permitted to affect other memory locations of the same Resource, For example, a cached copy of the same Resource that is associated with a different PA space. If multiple memory locations of the Resource have been written, it is CONSTRAINED UNPREDICTABLE which additional copies are cleaned to the PoPA. This CONSTRAINED UNPREDICTABLE behavior is guaranteed to be avoided if granule protection checks are configured to ensure that only one memory location of the Resource is writable at any time.
- The instructions affect all caches before the PoPA, even if the caches are after the PoC and are otherwise invisible to the programmer.
- The instructions have the same ordering, observability, and completion behavior as V A-based cache maintenance instructions issued to the Outer Shareable shareability domain. This includes aspects relating to the minimum size of cache lines, indicated by CTR\_EL0.DminLine.
- The instructions are not subject to granule protection checks.
- If the instructions target a PA above the implemented PA size, then no cache entries are required to be cleaned or invalidated.

In a system that contains caches associated with observers outside the Outer Shareable domain, for each of those caches at least one of the following properties must apply:

RJBRCM

- The cache is affected by DC PAPA operations. For that cache, it is permitted for DC PAPA operations to be treated as invalidate operations rather than clean and invalidate operations.
- Any accesses from the cache that propagate into the Outer Shareable domain are subject to granule protection checks, and the system additionally provides one of the following properties:
- -The cache can only store memory locations from the Non-secure physical address space.
- -Accesses from the cache are subject to translation controlled by the Security state associated with the cache line.

## D7.5.9.8 Effects of instructions that operate by PA to the PoE

Data cache maintenance instructions that operate by PA to the PoE have all of the following properties:

- The instructions affect all caches in the Outer Shareable shareability domain to the PoE for all copies of the memory location specified by the instruction.
- The instructions affect all caches before the PoE, even if the caches are after the PoC and are otherwise invisible to the programmer.
- The instructions have the same ordering, observability, and completion behavior as V A-based cache maintenance instructions issued to the Outer Shareable shareability domain. This includes aspects relating to the minimum size of cache lines, indicated by CTR\_EL0.DminLine.
- The instructions clean and invalidate all copies of the memory location specified by the instruction, irrespective of any MECID associated with the memory location. Memory accesses resulting from the Clean operation use the MECID associated with the cache entry.
- It is IMPLEMENTATION DEFINED whether the instructions are subject to granule protection checks.
- If HCR\_EL2.NV is 1, then executing the instructions at Realm EL1 is trapped to Realm EL2. Exceptions generated by these traps are reported using EC = 0x18 with its associated ISS field.

## D7.5.9.9 Effects of instructions that operate by VA to the PoP

For Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, cache maintenance instructions that operate by VA to the PoP affect the caches of other PEs in the shareability domain described by the shareability attributes of the VA supplied with the instruction.

For Device memory or Normal memory that is Inner Non-cacheable, Outer Non-cacheable, these instructions affect the caches of all PEs in the Outer Shareable shareability domain of the PE on which the instructions are operating.

In all cases, for any affected PE, these instructions affect all data and unified caches to the PoP. Table D7-5 shows the scope of these Data and unified cache maintenance to the PoP instructions.

## Table D7-5 PEs affected by cache maintenance instructions to the PoP

| Shareability    | PEs affected                                                                                | Effective to                 |
|-----------------|---------------------------------------------------------------------------------------------|------------------------------|
| Non-shareable   | The PE executing the instruction                                                            | The PoP of the entire system |
| Inner Shareable | All PEs in the same Inner Shareable shareability domain as the PE executing the instruction | The PoP of the entire system |
| Outer Shareable | All PEs in the same Outer Shareable shareability domain as the PE executing the instruction | The PoP of the entire system |

Note

It is IMPLEMENTATION DEFINED by the system whether the cache maintenance instructions have an effect on the caches of observers that are not PEs within the affected shareability domain to which the cache maintenance instructions apply.

## D7.5.9.10 Effects of instructions that operate by VA to the PoPS

For Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, cache maintenance instructions that operate by VA to the PoPS affect the caches of other PEs in the shareability domain described by the shareability attributes of the VA supplied with the instruction.

For Device memory or Normal memory that is Inner Non-cacheable, Outer Non-cacheable, these instructions affect the caches of all PEs in the Outer Shareable shareability domain of the PE on which the instructions are operating.

In all cases, for any affected PE, these instructions affect all data and unified caches to the PoPS. Table D7-6 shows the scope of these Data and unified cache maintenance to the PoPS instructions.

## Table D7-6 PEs affected by cache maintenance instructions to the PoPS

| Shareability    | PEs affected                                                                                 | Effective to                   |
|-----------------|----------------------------------------------------------------------------------------------|--------------------------------|
| Non-shareable   | The PE executing the instruction.                                                            | The PoPS of the entire system. |
| Inner Shareable | All PEs in the same Inner Shareable shareability domain as the PE executing the instruction. | The PoPS of the entire system. |
| Outer Shareable | All PEs in the same Outer Shareable shareability domain as the PE executing the instruction. | The PoPS of the entire system. |

Note

It is IMPLEMENTATION DEFINED by the system whether the cache maintenance instructions have an effect on the caches of observers that are not PEs within the affected shareability domain to which the cache maintenance instructions apply.

## D7.5.9.11 Effects of instructions that operate by VA to the PoU

For cache maintenance instructions that operate by V A to the PoU, Table D7-7 shows how, for a V A in a Normal or Device memory location, the shareability attribute of the V A determines the minimum set of PEs affected, and the point to which the instruction must be effective.

## Table D7-7 PEs affected by cache maintenance instructions to the PoU

| Shareability                       | PEs affected                                                                                | Effective to                                                                                                                                                                                      |
|------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Non-shareable                      | The PE executing the instruction                                                            | The PoU of instruction cache fills, data cache fills and write-backs, and translation table walks, on the PE executing the instruction                                                            |
| Inner Shareable or Outer Shareable | All PEs in the same Inner Shareable shareability domain as the PE executing the instruction | The PoU of instruction cache fills, data cache fills and write-backs, and translation table walks, of all PEs in the same Inner Shareable shareability domain as the PE executing the instruction |

## Note

- The set of PEs guaranteed to be affected is never greater than the PEs in the Inner Shareable shareability domain containing the PE executing the instruction.
- It is IMPLEMENTATION DEFINED by the system whether the cache maintenance instructions have an effect on the caches of observers that are not PEs within the affected shareability domain to which the cache maintenance instructions apply.

## D7.5.9.12 Effects of All and set/way maintenance instructions

The DC set/way instructions apply only to the caches of the PE that performs the instruction. IC IALLU instructions apply only to the caches of the PE that performs the instruction, unless HCR\_EL2.FB=1, which causes the instructions to be broadcast within the Inner Shareable domain when executed from EL1.

The IC IALLUIS instruction can affect the caches of all PEs in the same Inner Shareable shareability domain as the PE that performs the instruction. This instruction has an effect to the Point of Unification of instruction cache fills, data cache fills, and write-backs, and translation table walks, of all PEs in the same Inner Shareable shareability domain.

## Note

- The possible presence of system caches, as described in System level caches, means architecture does not guarantee that all levels of the cache can be maintained using set/way instructions.
- It is IMPLEMENTATION DEFINED by the system whether the cache maintenance instructions have an effect on the caches of observers that are not PEs within the affected shareability domain to which the cache maintenance instructions apply.

## D7.5.9.13 Effects of virtualization and Security state on the cache maintenance instructions

Each Security state has its own physical address (PA) space, therefore cache entries are associated with PA space.

Table D7-8 shows the effects of virtualization and security on the cache maintenance instructions. In the table, the Specified entries are entries that the architecture requires the instruction to affect.

Note

The rules described in General behavior of the caches mean that an instruction might also affect other entries.

Table D7-8 Effects of virtualization and security on the maintenance instructions

| Cache maintenance instructions                                                                                                                                    | Security state                                                       | Specified entries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data or unified cache maintenance instructions                                                                                                                    | Data or unified cache maintenance instructions                       | Data or unified cache maintenance instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Invalidate, Clean, or Clean and Invalidate by VA: DCIVAC, DCCVAC, DCCVAP, DCCVAU, DCCIVAC, DCCVAP, DCCIVAPS, DCCIGDVAPS,DC CIVAOC, DCCIGDVAOC,DC CVAOC,DCCGDVAOC. | Non-secure and Secure. When FEAT_RME is implemented, Realm and Root. | All lines that hold the PA that, in the current Security state, is mapped to by the combination of all of: • The specified VA. • For an instruction executed at EL1, EL0, or at EL2 when the Effective value of HCR_EL2.E2H is 1, the current ASID if the location is mapped to by a non-global page. • For an instruction executed at EL1 when SCR_EL3.NS is 1 or SCR_EL3.EEL2 is 1, the current VMID. a • For an instruction executed at EL0 when (SCR_EL3.NS is 1 or SCR_EL3.EEL2 is 1) and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, the current VMID. a |
| Invalidate, Clean, or Clean and Invalidate by set/way: DCISW, DCCSW,DCCISW, DCIGSW,DCCGSW,DCCIGSW, DCIGDSW,DCCGDSW,DC CIGDSW                                      | Non-secure                                                           | Line specified by set/way provided that the entry comes from the Non-secure PA space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Invalidate, Clean, or Clean and Invalidate by set/way: DCISW, DCCSW,DCCISW, DCIGSW,DCCGSW,DCCIGSW, DCIGDSW,DCCGDSW,DC CIGDSW                                      | Secure                                                               | Line specified by set/way provided that the entry comes from the Secure or Non-secure PA space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Invalidate, Clean, or Clean and Invalidate by set/way: DCISW, DCCSW,DCCISW, DCIGSW,DCCGSW,DCCIGSW, DCIGDSW,DCCGDSW,DC CIGDSW                                      | When FEAT_RME is implemented, the following cases are added:         | When FEAT_RME is implemented, the following cases are added:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Invalidate, Clean, or Clean and Invalidate by set/way: DCISW, DCCSW,DCCISW, DCIGSW,DCCGSW,DCCIGSW, DCIGDSW,DCCGDSW,DC CIGDSW                                      | Realm                                                                | Line specified by set/way provided that the entry comes from the Realm or Non-secure PA space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Invalidate, Clean, or Clean and Invalidate by set/way: DCISW, DCCSW,DCCISW, DCIGSW,DCCGSW,DCCIGSW, DCIGDSW,DCCGDSW,DC CIGDSW                                      | Root                                                                 | Line specified by set/way regardless of the PA space that the entry has come from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Cache maintenance instructions       | Security state                                                       | Specified entries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invalidate by VA: IC IVAU            | Non-secure and Secure. When FEAT_RME is implemented, Realm and Root. | All lines corresponding to the specified VA b in the current translation regime and: • For an instruction executed at EL1, EL0, or at EL2 when the Effective value of HCR_EL2.E2H is 1, the current ASID. • For an instruction executed at EL1 when SCR_EL3.NS is 1 or SCR_EL3.EEL2 is 1, the current VMID. a • For an instruction executed at EL0 when (SCR_EL3.NS is 1 or SCR_EL3.EEL2 is 1) and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, the current VMID. a                                                                                                                                                                                                                                     |
| Invalidate All: IC IALLU, IC IALLUIS | Non-secure and Secure.                                               | For an instruction executed at: • EL1 when the Effective value of SCR_EL3.{NSE, NS} is {0, 0} and SCR_EL3.EEL2 == 1, all instruction cache lines containing Secure or Non-secure entries associated with the current VMID. • EL1 when the Effective value of SCR_EL3.{NSE, NS} is {0, 1}, all instruction cache lines containing Non-secure entries associated with the current VMID. • EL2 when the Effective value of SCR_EL3.{NSE, NS} is {0, 1}, all instruction cache lines containing Non-secure entries. • EL1 when the Effective value of SCR_EL3.{EEL2, NSE, NS} is {0, 0, 0}, EL2 when SCR_EL3.{EEL2, NSE, NS} is {1, 0, 0}, or EL3, all instruction cache lines containing Secure or Non-secure entries. |
|                                      | Realm                                                                | For an instruction executed at: • EL1 when the Effective value of SCR_EL3.{NSE, NS} is {1, 1}, all instruction cache lines containing Realm or Non-secure entries associated with the current VMID. • EL2 when the Effective value of SCR_EL3.{NSE, NS} is {1, 1}, all instruction cache lines containing Realm or Non-secure entries.                                                                                                                                                                                                                                                                                                                                                                              |
|                                      | Root                                                                 | For an instruction executed at EL3, all instruction cache lines regardless of the PA space that the entries have come from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

b. The type of instruction cache used affects the interpretation of the specified entries in this table such that:

- For a PIPT instruction cache, the cache maintenance applies to all entries whose physical address corresponds to the specified address.
- For a VIPT instruction cache, the cache maintenance applies to entries whose virtual index and physical tag corresponds to the specified address.

For information on types of instruction cache see Instruction caches.

For locked entries and entries that might be locked, the behavior of cache maintenance instructions described in The interaction of cache lockdown with cache maintenance instructions applies.

With an implementation that generates aborts if entries are locked or might be locked in the cache, when the use of lockdown aborts is enabled, these aborts can occur on any cache maintenance instructions.

In an implementation that includes EL2:

- The architecture does not require cache cleaning when switching between virtual machines. Cache invalidation by set/way must not present an opportunity for one virtual machine to corrupt state associated with a second virtual machine. To ensure this requirement is met, invalidate by set/way instructions can, instead, perform a clean and invalidate by set/way.

- As described in The data cache maintenance instruction ( DC ), the AArch64 Data cache invalidate instructions, DCIVAC and DC ISW, when executed at EL1 and EL0, and the AArch32 Data cache invalidate instructions DCIMVAC and DCISW, when executed at EL1, can be configured to perform a cache clean as well as a cache invalidation.
- TLB invalidate instructions and IC IALLU instructions executed at EL1 are broadcast across the Inner Shareable domain when all of the following are true:
- -EL2 is implemented and enabled in the current Security state.
- -The value of HCR\_EL2.FB is 1.

For more information about the cache maintenance instructions, see About cache maintenance in AArch64 state, A64 Cache maintenance instructions, and The AArch64 Virtual Memory System Architecture.

## D7.5.9.14 Boundary conditions for cache maintenance instructions

Cache maintenance instructions operate on the caches regardless of whether the System register Cacheability controls force all memory accesses to be Non-cacheable.

For VA-based cache maintenance instructions, the instruction operates on the caches regardless of the memory type and cacheability attributes marked for the memory address in the VMSA translation table entries. This means that the effects of the cache maintenance instructions can apply regardless of:

- Whether the address accessed:
- -Is Normal memory or Device memory.
- -Has the Cacheable attribute or the Non-cacheable attribute.
- Any applicable domain control of the address accessed.
- The access permissions for the address accessed, other than the effect of the stage two write permission on data or unified cache invalidation instructions.

## D7.5.9.15 Ordering and completion of data and instruction cache instructions

All data cache instructions, other than DC ZV A, DC GV A, and DC GZVA that specify an address:

- Execute in program order relative to loads or stores that have all of the following properties:
- -Access an address in Normal memory with either Inner Write Through or Inner Write Back attributes within the same cache line of minimum size, as indicated by CTR\_EL0.DMinLine.
- -Use an address with the same cacheability attributes as the address passed to the data cache instruction.
- Can execute in any order relative to loads or stores that have all of the following properties:
- -Access an address in Normal memory with either Inner Write Through or Inner Write Back attributes within the same cache line of minimum size, as indicated by CTR\_EL0.DMinLine.
- -Use an address with different cacheability attributes as the address passed to the data cache instruction.
- -Do not have a DMB or DSB executed between the load or store instruction and the data cache instruction.
- Can execute in any order relative to loads or stores that access any address with the Device memory attribute, or with Normal memory with Inner Non-cacheable attribute unless a DMB or DSB is executed between the instructions.
- Execute in program order relative to other data cache instructions, other than DC ZV A, DC GV A, and DC GZV A that specify an address within the same cache line of minimum size, as indicated by CTR\_EL0.DMinLine.
- Can execute in any order relative to loads or stores that access an address in a different cache line of minimum size, as indicated by CTR\_EL0.DMinLine, unless a DMB or DSB is executed between the instructions.
- Can execute in any order relative to other data cache instructions, other than DC ZV A, DC GV A, and DC GZV A that specify an address in a different cache line of minimum size, as indicated by CTR\_EL0.DMinLine, unless a DMB or DSB is executed between the instructions.
- Can execute in any order relative to instruction cache maintenance instructions unless a DSB is executed between the instructions.
- Can execute in any order relative to data cache maintenance instructions that do not specify an address unless a DMB or DSB is executed between the instructions.

Note

Despite their mnemonics, the DC ZVA, DC GVA, and DC GZVA instructions are not data cache maintenance instructions.

Note

- Data cache ordering rules by address are consistent with physically indexed physically tagged caches. See Data and unified caches.

- Data cache zero instruction describes the ordering and completion rules for Data Cache Zero.

All data cache maintenance instructions that do not specify an address:

- Can execute in any order relative to data cache maintenance instructions that do not specify an address unless a DMB or DSB is executed between the instructions.

- Can execute in any order relative to data cache maintenance instructions that specify an address, other than DC ZVA , DC GVA , and DC GZVA , unless a DMB or DSB is executed between the instructions.

- Can execute in any order relative to loads or stores unless a DMB or DSB is executed between the instructions.

- Can execute in any order relative to instruction cache maintenance instructions unless a DSB is executed between the instructions.

All instruction cache maintenance instructions can execute in any order relative to other instruction cache instructions, data cache instructions, loads, and stores unless a DSB is executed between the instructions.

Acache maintenance instruction can complete at any time after it is executed, but is only guaranteed to be complete, and its effects visible to other observers, following a DSB instruction executed by the PE that executed the cache maintenance instruction. See also the requirements for cache maintenance instructions in Completion and endpoint ordering.

In all cases, where the text in this section refers to a DMB or a DSB , this means a DMB or DSB whose required access type is both loads and stores.

Note

This section specifies the memory ordering requirements of DMB and DSB based on the required access type as specified by the &lt;option&gt; parameter. DSB has additional requirements with respect to execution of instructions appearing in program order after the DSB as described in Data Synchronization Barrier. These additional requirements create the effect of additional memory ordering beyond what is specified in this section.

Note

These ordering requirements are extended from the requirements in AArch32 state given in:

- Ordering of cache and branch predictor maintenance instructions.

- AArch32 instruction cache maintenance instructions (IC*).

## D7.5.9.15.1 Ordering and completion of Data Cache Clean to Point of Persistence

The update of the persistent memory as a result of Data Cache Clean to the Point of Persistence is guaranteed to have occurred either after:

- The execution of a DSB applying to both reads and writes after the execution of the Data Cache Clean to the Point of Persistence.

- The update to persistent memory caused by a different Data Cache Clean to the Point of Persistence that is ordered after a DMB applying to both reads and writes that appears after the original Data Cache Clean to the Point of Persistence.

Note

This second point is an aspect of the fact that the Data Cache Clean to the Point of Persistence instructions are ordered by DMB , and this controls the order of arrival in persistent memory.

The ordering effect for the Data Cache Clean to the Point of Persistence by DMB applying to both read and writes is not sufficient to ensure that in Example D7-1, observation of the value '1' in the memory location X3 implies that the Data Cache Clean to the Point of Persistence has caused an update of persistent memory:

<!-- image -->

However, in Example D7-2, the ordering effects of the DMB instruction will ensure that the location pointed by P0: X1 will reach the Point of Persistence before, or at the same time as, the location pointed by P1:X8.

<!-- image -->

## D7.5.9.15.2 Ordering and completion of Data Cache Clean to Point of Deep Persistence

The update of the deep persistent memory as a result of Data Cache Clean to the Point of Deep Persistence is guaranteed to have occurred either after:

- The execution of a DSB applying to both reads and writes after the execution of the Data Cache Clean to the Point of Deep Persistence.
- The update to deep persistent memory caused by a different Data Cache Clean to the Point of Deep Persistence that is ordered after a DMB applying to both reads and writes that appears after the original Data Cache Clean to the Point of Deep Persistence.

Note

This second point is an aspect of the fact that the Data Cache Clean to the Point of Deep Persistence instructions are ordered by DMB, and this controls the order of arrival in deep persistent memory.

The ordering effect for the Data Cache Clean to the Point of Deep Persistence by DMB applying to both read and writes is not sufficient to ensure that in Example D7-3, observation of the value '1' in the memory location X3 implies that the Data Cache Clean to the Point of Deep Persistence has caused an update of deep persistent memory:

<!-- image -->

However, in Example D7-4, the ordering effects of the DMB instruction will ensure that the location pointed by P0: X1 will reach the Point of Deep Persistence before, or at the same time as, the location pointed by P1: X8.

<!-- image -->

## D7.5.9.16 Performing cache maintenance instructions

To ensure all cache lines in a block of address space are maintained through all levels of cache Arm strongly recommends that software:

- For data or unified cache maintenance, uses the CTR\_EL0.DMinLine value to determine the loop increment size for a loop of data cache maintenance by V A instructions.
- For instruction cache maintenance, uses the CTR\_EL0.IMinLine value to determine the loop increment size for a loop of instruction cache maintenance by V A instructions.

## D7.5.9.16.1 Example code for cache maintenance instructions

The cache maintenance instructions by set/way can clean or invalidate, or both, the entirety of one or more levels of cache attached to a PE. However, unless all PEs attached to the caches regard all memory locations as Non-cacheable, it is not possible to prevent locations being allocated into the cache during such a sequence of the cache maintenance instructions.

Note

Since the set/way instructions are performed only locally, there is no guarantee of the atomicity of cache maintenance between different PEs, even if those different PEs are each executing the same cache maintenance instructions at the same time. Since any cacheable line can be allocated into the cache at any time, it is possible for a cache line to migrate from an entry in the cache of one PE to the cache of a different PE in a way that means the line is not affected by set/way based cache maintenance. Therefore, Arm strongly discourages the use of set/way instructions to manage coherency in coherent systems. The expected use of the cache maintenance instructions that operate by set/way is limited to the cache maintenance associated with the powerdown and powerup of caches, if this is required by the implementation.

The limitations of cache maintenance by set/way mean maintenance by set/way does not happen on multiple PEs, and cannot be made to happen atomically for each address on each PE. Therefore in multiprocessor or multithreaded systems, the use of cache maintenance by set/way to clean, or clean and invalidate, the entire cache for coherency management with very large buffers or with buffers with unknown address can fail to provide the expected coherency results because of speculation by other PEs, or possibly by other threads. The only way that these instructions can be used in this way is to first ensure that all PEs that might cause speculative accesses to caches that need to be maintained are not capable of generating speculative accesses. This can be achieved by ensuring that those PEs have no memory locations with a Normal Cacheable attribute. Such an approach can have very large system performance effects, and Arm advises implementers to use hardware coherency mechanisms in systems where this will be an issue.

System level caches refers to other limitations of cache maintenance by set/way.

The following example code for cleaning a data or unified cache to the Point of Coherency illustrates a generic mechanism for cleaning the entire data or unified cache to the Point of Coherency. It assumes that the current Cache Size Identification Register is in 32-bit format. For more information, see Possible formats of the Cache Size Identification Register, CCSIDR\_EL1.

```
MRS X0, CLIDR_EL1 AND W3, W0, #0x07000000 // Get 2 x Level of Coherence LSR W3, W3, #23 CBZ W3, Finished MOV W10, #0 // W10 = 2 x cache level MOV W8, #1 // W8 = constant 0b1 Loop1: ADD W2, W10, W10, LSR #1 // Calculate 3 x cache level LSR W1, W0, W2 // extract 3-bit cache type for this level AND W1, W1, #0x7 CMP W1, #2 B.LT Skip // No data or unified cache at this level MSR CSSELR_EL1, X10 // Select this cache level ISB // Synchronize change of CSSELR MRS X1, CCSIDR_EL1 // Read CCSIDR AND W2, W1, #7 // W2 = log2(linelen)-4 ADD W2, W2, #4 // W2 = log2(linelen) UBFX W4, W1, #3, #10 // W4 = max way number, right aligned CLZ W5, W4 // W5 = 32-log2(ways), bit position of way in DC operand LSL W9, W4, W5 // W9 = max way number, aligned to position in DC operand LSL W16, W8, W5 // W16 = amount to decrement way number per iteration Loop2: UBFX W7, W1, #13, #15 // W7 = max set number, right aligned LSL W7, W7, W2 // W7 = max set number, aligned to position in DC operand LSL W17, W8, W2 // W17 = amount to decrement set number per iteration Loop3: ORR W11, W10, W9 // W11 = combine way number and cache number ... ORR W11, W11, W7 // ... and set number for DC operand DC CSW, X11 // Do data cache clean by set and way SUBS W7, W7, W17 // Decrement set number B.GE Loop3 SUBS X9, X9, X16 // Decrement way number B.GE Loop2 Skip: ADD W10, W10, #2 // Increment 2 x cache level CMP W3, W10 DSB // Ensure completion of previous cache maintenance instruction B.GT Loop1 Finished:
```

Similar approaches can be used for all cache maintenance instructions.

## D7.5.10 Data cache zero instruction

The Data Cache Zero by Address instruction, DC ZVA, writes 0x00 to each byte of a block of N bytes, aligned in memory to N bytes in size, where:

- The block in memory is identified by the address supplied as an argument to the DC ZV A instruction. There are no alignment restrictions on this address.

Note

This means that each byte of the block of memory that includes the supplied address is set to zero.

- The DCZID\_EL0 register indicates the block size, N bytes, that is written with byte values of zero.

Software can restrict access to this instruction. See Configurable instruction controls and the description of the DC ZV A instruction.

The DC ZVA instruction behaves as a set of stores to the location being accessed, and:

- Generates a Permission fault if the translation regime being used when the instruction is executed does not permit writes to the locations.
- Requires the same considerations for ordering and the management of coherency as any other store instruction.

In addition:

- When the instruction is executed, it can generate memory faults or watchpoints that are prioritized in the same way as other memory related faults or watchpoints. Where a synchronous Data Abort fault or a watchpoint is generated, the CM bit in the syndrome field is not set to 1, which would be the case for all other cache maintenance instructions. See ISS encoding for an exception from a Data Abort for more information about the encoding of the associated ESR\_ELx.ISS field.
- If the memory region being zeroed is any type of Device memory, then DC ZVA generates an Alignment fault which is prioritized in the same way as other alignment faults that are determined by the memory type.

Note

The architecture makes no statements about whether or not a DC ZV A instruction causes allocation to any particular level of the cache, for addresses that have a cacheable attribute for those levels of cache.

Despite its mnemonic, the DC ZVA instruction is not a data cache maintenance instruction.

## D7.5.11 Cache lockdown

The concept of an entry locked in a cache is allowed, but not architecturally defined. How lockdown is achieved is IMPLEMENTATION DEFINED and might not be supported by:

- An implementation.
- Some memory attributes.

An unlocked entry in a cache might not remain in that cache. The architecture does not guarantee that an unlocked cache entry remains in the cache or remains incoherent with the rest of memory. Software must not assume that an unlocked item that remains in the cache remains dirty.

Alocked entry in a cache is guaranteed to remain in that cache. The architecture does not guarantee that a locked cache entry remains incoherent with the rest of memory, that is, it might not remain dirty.

## D7.5.11.1 The interaction of cache lockdown with cache maintenance instructions

The interaction of cache lockdown and cache maintenance instructions is IMPLEMENTATION DEFINED. However, an architecturally-defined cache maintenance instruction on a locked cache line must comply with the following general rules:

- Cache maintenance operations to the PoPA affect cache entries regardless of lockdown status.

- The effect of the following instructions on locked cache entries is IMPLEMENTATION DEFINED:
- -Cache clean by set/way, DC CSW.
- -Cache invalidate by set/way, DC ISW.
- -Cache clean and invalidate by set/way, DC CISW.
- -Instruction cache invalidate all, IC IALLU and IC IALLUIS.

However, one of the following approaches must be adopted in all these cases:

1. If the instruction specified an invalidation, a locked entry is not invalidated from the cache.
2. If the instruction specified a clean it is IMPLEMENTATION DEFINED whether locked entries are cleaned.
3. If an entry is locked down, or could be locked down, an IMPLEMENTATION DEFINED Data Abort exception is generated, using the DFSC value defined for this purpose, see ISS encoding for an exception from a Data Abort.

This permits a usage model for cache invalidate routines to operate on a large range of addresses by performing the required operation on the entire cache, without having to consider whether any cache entries are locked.

- The effect of the following instructions on locked cache entries is IMPLEMENTATION DEFINED:
- -Cache clean by virtual address, DC CV AC, DC CVAP, and DC CVAU.
- -Cache invalidate by virtual address, DC IV AC.
- -Cache clean and invalidate by virtual address, DC CIV AC.

However, one of the following approaches must be adopted in all these cases:

1. If the instruction specified an invalidation, a locked entry is invalidated from the cache. For the clean and invalidate instructions, the entry must be cleaned before it is invalidated.
2. If the instruction specified an invalidation, a locked entry is not invalidated from the cache. If the instruction specified a clean it is IMPLEMENTATION DEFINED whether locked entries are cleaned.
3. If an entry is locked down, or could be locked down, an IMPLEMENTATION DEFINED Data Abort exception is generated, using the DFSC value defined for this purpose. See ESR\_ELx.

In an implementation that includes EL2 enabled in the current Security state, if HCR\_EL2.TIDCP is set to 1, any exception relating to lockdown of an entry is routed to EL2.

Note

An implementation that uses an abort mechanism for entries that can be locked down but are not actually locked down must:

- Document the IMPLEMENTATION DEFINED instruction sequences that perform the required operations on entries that are not locked down.
- Implement one of the other permitted alternatives for the locked entries.

Arm recommends that, when possible, such IMPLEMENTATION DEFINED instruction sequences use architecturally-defined instructions. This minimizes the number of customized instructions required.

In addition, an implementation that uses an abort to handle cache maintenance instructions for entries that might be locked must provide a mechanism that ensures that no entries are locked in the cache.

The reset setting of the cache must be that no cache entries are locked.

## D7.5.11.1.1 Additional cache functions for the implementation of lockdown

An implementation can add additional cache maintenance functions for the handling of lockdown in the IMPLEMENTATION DEFINED spaces reserved for Cache Lockdown, see Reserved encodings for IMPLEMENTATION DEFINED registers.

## D7.5.12 System level caches

The Arm Architecture defines a system cache as a cache that is not described in the PE Cache Identification registers, CCSIDR\_EL1 and CLIDR\_EL1, and for which the set/way cache maintenance instructions do not apply.

Conceptually, three classes of system cache can be envisaged:

1. System caches which lie before the Point of Coherency and cannot be managed by any cache maintenance instructions. Such systems fundamentally undermine the concept of cache maintenance instructions operating to the Point of Coherency, as they imply the use of non-architecture mechanisms to manage coherency. The use of such systems in the Arm architecture is explicitly prohibited.

2. System caches which lie before the Point of Coherency and can be managed by cache maintenance by address instructions that apply to the Point of Coherency, but cannot be managed by cache maintenance by set/way instructions. Where maintenance of the entirety of such a cache must be performed, as in the case for power management, it must be performed using non-architectural mechanisms.
3. System caches which lie beyond the Point of Coherency and so are invisible to the software for the purpose of managing coherency.

Note

If maintenance of the entirety of such a cache is supported, it is an IMPLEMENTATION DEFINED property of the system.

## D7.5.13 Branch prediction

In the AArch64 architecture, branch predictors are not architecturally visible.

For details on the restrictions on the effects of speculation for branch predictors, see Restrictions on the effects of speculation.