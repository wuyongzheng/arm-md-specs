## G4.4 AArch32 cache and branch predictor support

The following sections describe the support for caches and branch predictors in AArch32 state:

- General behavior of the caches.
- Cache identification.
- Cacheability, cache allocation hints, and cache transient hints.
- Enabling and disabling the caching of memory accesses in AArch32 state.
- Behavior of caches at reset.
- About cache maintenance in AArch32 state.
- AArch32 cache and branch predictor maintenance instructions.
- Execution and data prediction restriction System instructions.
- Cache lockdown.
- System level caches.

See also The AArch32 Virtual Memory System Architecture, and in particular Caches in VMSAv8-32.

Note

- Branch predictors typically use a form of cache to hold branch target data. Therefore, they are included in this section.
- In the instruction mnemonics, MVA is a synonym for VA.

## G4.4.1 General behavior of the caches

When a memory location is marked with a Normal Cacheable memory attribute, determining whether a copy of the memory location is held in a cache still depends on many aspects of the implementation. The following non-exhaustive list of factors might be involved:

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

For more information, see The interaction of cache lockdown with cache maintenance instructions.

- Any memory location that has a Normal Cacheable attribute at either the current Exception level or at a higher Exception level can be allocated to a cache at any time.

- It is guaranteed that no memory location that does not have a Normal Cacheable attribute is allocated into the cache.

- It is guaranteed that no memory location is allocated to the cache if it has a Normal Non-cacheable attribute or any type of Device memory attribute in both:

- The translation regime at the current Exception level.

- The translation regime at any higher Exception level.

- For data accesses, any memory location with a Normal Inner Shareable or Normal Outer Shareable attribute is guaranteed to be coherent with all Requesters in its Shareability domain.

- Any memory location is not guaranteed to remain incoherent with the rest of memory.

- The eviction of a cache entry from a cache level can overwrite memory that has been written by another observer only if the entry contains a memory location that has been written to by an observer in the Shareability domain of that memory location. The maximum size of the memory that can be overwritten is called the Cache Write-back Granule . In some implementations the CTR identifies the Cache Write-back Granule.

- The allocation of a memory location into a cache cannot cause the most recent value of that memory location to become invisible to an observer, if it was previously visible to that observer.

Note

The Cacheability attribute of an address is determined by the applicable translation table entry for that address, as modified by any applicable System register Cacheability controls, such as the SCTLR.{I, C} controls.

For the purpose of these principles, a cache entry covers at least 16 bytes and no more than 2KB of contiguous address space, aligned to the size of the cache entry.

## G4.4.2 Cache identification

The cache identification consists of a set of registers that describe the implemented caches that are affected by cache maintenance instructions executed on the PE. This includes cache maintenance instructions that:

- Affect the entire cache, for example ICIALLUIS.

- Operate by VA, for example ICIMVAU.

- Operate by set/way, for example DCISW.

The cache identification registers are:

- Asingle Cache Type Register, CTR, that defines:

- The minimum line length of any of the instruction caches affected by the instruction cache maintenance instructions.

- The minimum line length of any of the data or unified caches, affected by the data cache maintenance instructions.

- The cache indexing and tagging policy of the Level 1 instruction cache.

- [ ] Note

It is IMPLEMENTATION DEFINED whether caches beyond the PoC will be reported by this mechanism, and because of the possible existence of system caches some caches before the PoC might not be reported. For more information about system caches, see System level caches.

- Asingle Cache Level ID Register, CLIDR, that defines:

- The type of cache that is implemented and can be maintained using the architected cache maintenance instructions that operate by set/way or operate on the entire cache at each cache level, up to the maximum of seven levels.

- The Level of Unification Inner Shareable (LoUIS), Level of Coherence (LoC) and the Level of Unification (LoU) for the caches. See Terms used in describing the cache maintenance instructions for a definition of these terms.

- An optional ICB field to indicate the boundary between the caches use for caching Inner Cacheable memory regions and those used only for caching Outer Cacheable regions.

- Asingle Cache Size Selection Register, CSSELR, that selects the cache level and sort of cache (Instruction, Data/Unified/Tag) of the current Cache Size Identification Register.

- For each implemented cache that is identifiable by this mechanism, across all the levels of caching, a Cache Size Identification Register, that defines:

- The number of sets, associativity, and line length of the cache. See Terms used in describing the cache maintenance instructions for a definition of these terms.

- [ ] Note

From Armv8.3, it is possible to have multiple Cache Size Identification Registers. For more details, see Possible formats of the Cache Size Identification Registers, CCSIDR and CCSIDR2.

To determine the cache topology associated with a PE:

1. Read the Cache Type Register to find the indexing and tagging policy used for the Level 1 instruction cache. This register also provides the size of the smallest cache lines used for the instruction caches, and for the data and unified caches. These values are used in cache maintenance instructions.
2. Read the Cache Level ID Register to find what caches are implemented. The register includes seven Cache type fields, for cache levels 1 to 7. Scanning these fields, starting from Level 1, identifies the instruction, data or unified caches implemented at each level. This scan ends when it reaches a level at which no caches are defined. The Cache Level ID Register also specifies the Level of Unification (LoU) and the Level of Coherence (LoC) for the cache implementation.
3. For each cache identified at stage 2:
- Write to the Cache Size Selection Register to select the required cache. A cache is identified by its level, and whether it is:
5. -An instruction cache.
6. -Adata or unified cache.
- Read the Cache Size Identification Register to find details of the cache.

## G4.4.2.1 Possible formats of the Cache Size Identification Registers, CCSIDR and CCSIDR2

From Armv8.3, two different formats are available for defining the number of sets and associativity of the currently selected cache. For a definition of these terms, see Terms used in describing the cache maintenance instructions.

When FEAT\_CCIDX is implemented:

- There are two Cache Size Identification Registers, CCSIDR and CCSIDR2.
- The length of the CCSIDR.Assoc field is 21 bits. This limits the associativity of the currently selected cache to 2 21 .
- The length of the CCSIDR2.NumSets field is 24 bits. This limits the number of sets in the currently selected cache to 2 24 .

This is the 64-bit format of the Cache Size Identification Register.

When FEAT\_CCIDX is not implemented:

- There is a single Cache Size Identification Register, CCSIDR.
- The length of the CCSIDR.Assoc field is 10 bits. This limits the associativity of the currently selected cache to 2 10 .
- The length of the CCSIDR.NumSets field is 15 bits. This limits the number of sets in the currently selected cache to 2 15 .

This is the 32-bit format of the Cache Size Identification Register.

When one of these formats is implemented, it is implemented across all the levels of caching.

## G4.4.3 Cacheability, cache allocation hints, and cache transient hints

Cacheability applies only to Normal memory, and is defined independently for Inner and Outer cache locations. All types of Device memory are always treated as Non-cacheable.

As described in Memory types and attributes, the memory attributes include a Cacheability attribute that is one of:

- Non-cacheable.
- Write-Through cacheable.
- Write-Back cacheable.

Cacheability attributes other than Non-cacheable can be complemented by a cache allocation hint . This is an indication to the memory system of whether allocating a value to a cache is likely to improve performance. In addition, it is IMPLEMENTATION DEFINED whether a cache transient hint is supported, see Transient Cacheability hint.

The cache allocation hints are assigned independently for read and write accesses, and therefore when the Transient hint is supported the following cache allocation hints can be used:

For read accesses: Read-Allocate, Transient Read-Allocate, or No Read-Allocate.

For write accesses: Write-Allocate, Transient Write-Allocate, or No Write-Allocate.

Note

- ACacheable location with both No Read-Allocate and No Write-Allocate hints is not the same as a Non-cacheable location. A Non-cacheable location has coherency guarantees for all observers within the system that do not apply for a location that is Cacheable, No Read-Allocate, No Write-Allocate.
- Implementations can use the cache allocation hints to limit cache pollution to a part of a cache, such as to a subset of ways.
- For VMSAv8-32 translation table walks using the Long-descriptor translation table format, the appropriate TCR.{IRGN n , ORGN n } fields define the memory attributes of the translation tables, including the Cacheability. However, this assignment supports only a subset of the Cacheability attributes described in this section.

The architecture does not require an implementation to make any use of cache allocation hints. This means an implementation might not make any distinction between memory locations with attributes that differ only in their cache allocation hint.

## G4.4.3.1 Transient Cacheability hint

It is IMPLEMENTATION DEFINED whether a Transient hint is supported for the VMSAv8-32 translation scheme when using the Long-descriptor translation table format. In an implementation that supports the Transient hint, the Transient hint is a qualifier of the cache allocation hints, and indicates that the benefit of caching is for a relatively short period. It indicates that it might be better to restrict allocation of transient entries, to avoid possibly casting-out other, less transient, entries.

Note

The architecture does not specify what is meant by a relatively short period .

When using the Short-descriptor translation table format, VMSAv8-32 cannot support the Transient hint.

The description of the MAIR0, MAIR1, HMAIR0, and HMAIR1 registers includes the assignment of the Transient attribute in an implementation that supports this option. In this assignment:

- The Transient hint is defined independently for Inner Cacheable and Outer Cacheable memory regions.
- Asingle Transient hint applies to both read and write accesses to a memory region.

## G4.4.4 Enabling and disabling the caching of memory accesses in AArch32 state

Cacheability control fields can force all memory locations with the Normal memory type to be treated as Non-cacheable, regardless of their assigned Cacheability attribute. Independent controls are provided for each stage of address translation, with separate controls for:

- Data accesses. These controls also apply to accesses to the translation tables.
- Instruction accesses.

Note

These Cacheability controls replace the cache enable controls provided in previous versions of the Arm architecture.

In AArch32 state, the Cacheability control fields and their effects are as follows:

## For the Non-secure PL1&amp;0 translation regime

The Non-secure instance of SCTLR holds the EL1 controls that affect Cacheability:

- When the value of SCTLR.C is 0:
- -All stage 1 translations for data accesses to Normal memory are Non-cacheable.
- -All accesses to the PL1&amp;0 stage 1 translation tables are Non-cacheable.
- When the value of SCTLR.I is 0:
- -All stage 1 translations for instruction accesses to Normal memory are Non-cacheable.
- When the value of HCR2.CD is 1:
- -All stage 2 translations for data accesses to Normal memory are Non-cacheable.
- -All accesses to the PL1&amp;0 stage 2 translation tables are Non-cacheable.
- When the value of HCR2.ID is 1:
- -All stage 2 translations for instruction accesses to Normal memory are Non-cacheable.
- When the value of HCR.DC is 1, all Non-secure stage 1 translations and all accesses to the Non-secure EL1&amp;0 stage 1 translation tables, are treated as accesses to Normal Non-shareable Inner Write-Back Cacheable Read-Allocate Write-Allocate, Outer Write-Back Cacheable Read-Allocate Write-Allocate memory, regardless of the value of SCTLR.C. This applies to translations for both data and instruction accesses.

In addition, when the value of SCTLR.M is 0, indicating that the stage 1 translations are disabled for the translation regime, then if EL2 is using AArch32 and the value of HCR.DC is 0 or if EL2 is using AArch64 and the value of HCR\_EL2.DC is 0, then:

- If the value of SCTLR.I is 0, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Non-cacheable, Outer Non-cacheable.
- If the value of SCTLR.I is 1, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Write-Through cacheable, Outer Write-Through cacheable.

## Note

- In Non-secure state, the stage 1 and stage 2 Cacheability attributes are combined as described in Combining the Cacheability attribute.
- The Non-secure SCTLR.{C, I} and HCR.DC fields have no effect on the Secure PL1&amp;0 and EL2 translation regimes.
- The HCR2.{ID, CD} fields affect only stage 2 of the Non-secure PL1&amp;0 translation regime.
- In Non-secure state, the PL1&amp;0 translation regime can be described as the Non-secure EL1&amp;0 translation regime. This is consistent with the equivalent AArch64 descriptions.
- When FEAT\_XS is implemented SCTLR.{C, I} and HCR2.{ID, CD} fields have no effect on the value of the XS attribute.

## For the Secure PL1&amp;0 translation regime

The Secure instance of SCTLR holds the controls that determine Cacheability:

- When the value of SCTLR.C is 0:
- -All data accesses to Normal memory using the Secure PL1&amp;0 translation regime are Non-cacheable.
- -All accesses to the Secure PL1&amp;0 translation tables are Non-cacheable.
- When the value of SCTLR.I is 0:

- -All instruction accesses to Normal memory using the Secure PL1&amp;0 translation regime are Non-cacheable.

In addition, when the value of SCTLR.M is 0, indicating that stage 1 translations are disabled, then:

- If the value of SCTLR.I is 0, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Non-cacheable, Outer Non-cacheable.
- If the value of SCTLR.I is 1, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Write-Through cacheable, Outer Write-Through cacheable.

## Note

- The Secure SCTLR.{I, C, M} fields have no effect on the Non-secure PL1&amp;0 and EL2 translation regimes.
- When FEAT\_XS is implemented, the SCTLR.{I, C} fields have no effect on the value of the XS attribute.

## For the EL2 translation regime

- When the value of HSCTLR.C is 0:
- -All data accesses to Normal memory using the EL2 translation regime are Non-cacheable.
- -All accesses to the EL2 translation tables are Non-cacheable.
- When the value of HSCTLR.I is 0:
- -All instruction accesses to Normal memory using the EL2 translation regime are Non-cacheable.

In addition, when the value of HSCTLR.M is 0, indicating that stage 1 translations are disabled, then:

- If the value of HSCTLR.I is 0, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Non-cacheable, Outer Non-cacheable.
- If the value of HSCTLR.I is 1, instruction accesses to Normal memory from stage 1 of the translation regime are Outer Shareable, Inner Write-Through cacheable, Outer Write-Through cacheable.

## Note

- The HSCTLR.{I, C, M} fields have no effect on the PL1&amp;0 and EL3 translation regimes.
- When FEAT\_XS is implemented, the HSCTLR.{I, C} fields have no effect on the value of the XS attribute.

The effect of the SCTLR.C or HSCTLR.C and HCR2.CD bits is reflected in the result of the address translation instructions in the PAR.

## Note

- The requirements in this section mean the architecturally required effects of SCTLR.I and HSCTLR.I are limited to their effects on caching instruction accesses in unified caches.
- This specification can give rise to different Cacheability attributes between instruction and data accesses to the same location. Where this occurs, the measures for mismatch memory attributes described in Mismatched memory attributes must be followed to manage the corresponding loss of coherency.

## G4.4.5 Behavior of caches at reset

The following rules apply to caches at reset:

- All caches reset to IMPLEMENTATION DEFINED states that might be UNKNOWN.
- The Cacheability control fields described in Enabling and disabling the caching of memory accesses in AArch32 state reset to values that force all memory locations to be treated as Non-cacheable.

Note

This applies only to the controls that apply to the Translation regime that is used by the Exception level, PE mode, and Security state entered on reset.

- An implementation can require the use of a specific cache initialization routine to invalidate its storage array before caching is enabled. The exact form of any required initialization routine is IMPLEMENTATION DEFINED, and the routine must be documented clearly as part of the documentation of the device.

- If an implementation permits cache hits when the Cacheability control fields force all memory locations to be treated as Non-cacheable then the cache initialization routine must:

- Provide a mechanism to ensure the correct initialization of the caches.

- Be documented clearly as part of the documentation of the device.

In particular, if an implementation permits cache hits when the Cacheability controls force all memory locations to be treated as Non-cacheable, and the cache contents are not invalidated at reset, the initialization routine must avoid any possibility of running from an uninitialized cache. It is acceptable for an initialization routine to require a fixed instruction sequence to be placed in a restricted range of memory.

- Arm recommends that whenever an invalidation routine is required, it is based on the cache maintenance instructions.

## Similar rules apply to:

- Branch predictor behavior, see Behavior of the branch predictors at reset.

- TLB behavior, see TLB behavior at reset.

## G4.4.6 About cache maintenance in AArch32 state

The following sections give general information about cache maintenance:

- Terms used in describing the cache maintenance instructions.

- Abstraction of the cache hierarchy.

The following sections describe the AArch32 state cache maintenance instructions:

- AArch32 instruction cache maintenance instructions (IC*).

- AArch32 data cache maintenance instructions (DC*).

Note

Some descriptions of the cache maintenance instructions refer to the Cacheability of the address on which the instruction operates. The Cacheability of an address is determined by the applicable translation table entry for that address, as modified by any applicable System register Cacheability controls, such as the SCTLR.{I, C} controls.

## G4.4.6.1 Terms used in describing the cache maintenance instructions

Cache maintenance instructions are defined to act on particular memory locations. Instructions can be defined:

- By the virtual address of the memory location to be maintained, referred to as operating by VA .

- By a mechanism that describes the location in the hardware of the cache, referred to as operating by set/way .

In addition, for instruction caches and branch predictors, there are instructions that invalidate all entries.

The following subsections define the terms used in the descriptions of the cache maintenance instructions:

- Terminology for cache maintenance instructions operating by set/way.

- Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

Note

There is no terminology specific to cache maintenance instructions that operate by V A. When all applicable stages of translation are disabled, the V A used is identical to the PA. For more information about memory system behavior when address translation is disabled, see The effects of disabling address translation stages on VMSAv8-32 behavior.

## G4.4.6.1.1 Terminology for cache maintenance instructions operating by set/way

Cache maintenance instruction that operate by set/way refer to the particular structures in a cache. Three parameters describe the location in a cache hierarchy that an instruction works on. These parameters are:

Level

The cache level of the hierarchy. The number of levels of cache is IMPLEMENTATION DEFINED. The cache levels that can be managed using the architected cache maintenance instructions that operate by set/way can be determined from the CLIDR.

In the Arm architecture, the lower numbered cache levels are those closest to the PE. See Memory hierarchy.

- Set Each level of a cache is split up into a number of sets . Each set is a set of locations in a cache level to which an address can be assigned. Usually, the set number is an IMPLEMENTATION DEFINED function of an address.

In the Arm architecture, sets are numbered from 0.

The associativity of a cache is the number of locations in a set to which a specific address can be assigned. The way number specifies one of these locations.

In the Arm architecture, ways are numbered from 0.

Way

Note

Because the allocation of a memory address to a cache location is entirely IMPLEMENTATION DEFINED, Arm expects that most portable software will use only the cache maintenance instructions by set/way as single steps in a routine to perform maintenance on the entire cache.

## G4.4.6.1.2 Terminology for Clean, Invalidate, and Clean and Invalidate instructions

Caches introduce coherency problems in two possible directions:

1. An update to a memory location by a PE that accesses a cache might not be visible to other observers that can access memory. This can occur because new updates are still in the cache and are not visible yet to the other observers that do not access that cache.
2. Updates to memory locations by other observers that can access memory might not be visible to a PE that accesses a cache. This can occur when the cache contains an old, or stale , copy of the memory location that has been updated.

The Clean and Invalidate instructions address these two issues. The definitions of these instructions are:

## Clean

## Invalidate

Acache clean instruction ensures that updates made by an observer that controls the cache are made visible to other observers that can access memory at the point to which the instruction is performed. Once the Clean has completed, the new memory values are guaranteed to be visible to the point to which the instruction is performed, for example to the Point of Unification.

The cleaning of a cache entry from a cache can overwrite memory that has been written by another observer only if the entry contains a location that has been written to by an observer in the Shareability domain of that memory location.

Acache invalidate instruction ensures that updates made visible by observers that access memory at the point to which the invalidate is defined, are made visible to an observer that controls the cache. This might result in the loss of updates to the locations affected by the invalidate instruction that have been written by observers that access the cache, if those updates have not been cleaned from the cache since they were made.

If the address of an entry on which the invalidate instruction operates is Normal, Non-cacheable or any type of Device memory then an invalidate instruction also ensures that this address is not present in the cache.

Note

Entries for addresses that are Normal Cacheable can be allocated to the cache at any time, and so the cache invalidate instruction cannot ensure that the address is not present in a cache.

## Clean and Invalidate

Acache clean and invalidate instruction behaves as the execution of a clean instruction followed immediately by an invalidate instruction. Both instructions are performed to the same location.

The points to which a cache maintenance instruction can be defined differ depending on whether the instruction operates by VA or by set/way:

- For instructions operating by set/way, the point is defined to be to the next level of caching. For the All operations, the point is defined as the Point of Unification for each location held in the cache.
- For instruction operating by V A, two conceptual points are defined:

## Point of Coherency (PoC)

The point at which all agents that can access memory are guaranteed to see the same copy of a memory location for accesses of any memory type or Cacheability attribute. In many cases this is effectively the main system memory, although the architecture does not prohibit the implementation of caches beyond the PoC that have no effect on the coherency between memory system agents.

Note

The presence of system caches can affect the determination of the point of coherency as described in System level caches.

## Point of Unification (PoU)

The PoU for a PE is the point by which the instruction and data caches and the translation table walks of that PE are guaranteed to see the same copy of a memory location. In many cases, the Point of Unification is the point in a uniprocessor memory system by which the instruction and data caches and the translation table walks have merged.

The PoU for an Inner Shareable Shareability domain is the point by which the instruction and data caches and the translation table walks of all the PEs in that Inner Shareable Shareability domain are guaranteed to see the same copy of a memory location. Defining this point permits self-modifying software to ensure future instruction fetches are associated with the modified version of the software by using the standard correctness policy of:

1. Clean data cache entry by address.
2. Invalidate instruction cache entry by address.

The following fields in the CLIDR relate to these conceptual points:

## LoC, Level of Coherence

This field defines the last level of cache that must be cleaned or invalidated when cleaning or invalidating to the Point of Coherency. The LoC value is a cache level, so, for example, if LoC contains the value 3:

- -Aclean to the Point of Coherency operation requires the level 1, level 2 and level 3 caches to be cleaned.
- -Level 4 cache is the first level that does not have to be maintained.

If the LoC field value is 0x0 , this means that no levels of cache need to cleaned or invalidated when cleaning or invalidating to the Point of Coherency.

If the LoC field value is a nonzero value that corresponds to a level that is not implemented, this indicates that all implemented caches are before the Point of Coherency.

## LoUU, Level of Unification, uniprocessor

This field defines the last level of cache that must be cleaned or invalidated when cleaning or invalidating to the Point of Unification for the PE. As with LoC, the LoUU value is a cache level.

If the LoUU field value is 0x0 , this means that no levels of cache need to cleaned or invalidated when cleaning or invalidating to the Point of Unification.

If the LoUU field value is a nonzero value that corresponds to a level that is not implemented, this indicates that all implemented caches are before the Point of Unification.

## LoUIS, Level of Unification, Inner Shareable

In any implementation:

- -This field defines the last level of cache that must be cleaned or invalidated when cleaning or invalidating to the Point of Unification for the Inner Shareable Shareability domain. As with LoC, the LoUIS value is a cache level.

- If the LoUIS field value is 0x0 , this means that no levels of cache need to cleaned or invalidated when cleaning or invalidating to the Point of Unification for the Inner Shareable Shareability domain.

- If the LoUIS field value is a nonzero value that corresponds to a level that is not implemented, this indicates that all implemented caches are before the Point of Unification.

For more information, see the CLIDR description.

## G4.4.6.2 Abstraction of the cache hierarchy

The following subsections describe the abstraction of the cache hierarchy:

- Cache maintenance instructions that operate by V A.
- Cache maintenance instructions that operate by set/way.

## G4.4.6.2.1 Cache maintenance instructions that operate by VA

The VA-based cache maintenance instructions are described as operating by V A. Each of these instructions is always qualified as being either:

- Performed to the Point of Coherency.
- Performed to the Point of Unification.

See Terms used in describing the cache maintenance instructions for definitions of Point of Coherency and Point of Unification, and more information about possible meanings of V A.

AArch32 cache and branch predictor maintenance instructions lists the V A-based maintenance instructions.

The CTR holds minimum line length values for:

- The instruction caches.
- The data and unified caches.

These values support efficient invalidation of a range of addresses, because this value is the most efficient address stride to use to apply a sequence of V A-based maintenance instructions to a range of V As.

For the Invalidate data or unified cache line by V A instruction, the Cache Write-back Granule field of the CTR defines the maximum granule that a single invalidate instruction can invalidate. This meaning of the Cache Write-back Granule is in addition to its defining the maximum size that can be written back.

## G4.4.6.2.2 Cache maintenance instructions that operate by set/way

AArch32 cache and branch predictor maintenance instructions lists the set/way-based maintenance instructions. Some encodings of these instructions include a required field that specifies the cache level for the instruction:

- Aclean instruction cleans from the level of cache specified through to at least the next level of cache, moving further from the PE.
- An invalidate instruction invalidates only at the level specified.

## G4.4.7 AArch32 cache and branch predictor maintenance instructions

The instruction and data cache maintenance instructions have the same functionality in AArch32 state and in AArch64 state. Table G4-3 shows the AArch32 System instructions. Instructions that take an argument include Rt in the instruction description.

If FEAT\_CLRBHB is not implemented, then the architecture does not define any branch predictor maintenance instructions for AArch32 state.

When FEAT\_CLRBHB is implemented, the CLRBHB instruction is available. When the CLRBHB instruction is executed, the branch history is cleared for the current context to the extent that branch history information created before the CLRBHB instruction cannot be used by code before the CLRBHB instruction to exploitatively control the execution of any code in the current context appearing in program order after the instruction.

## Note

- In Table G4-3 the Point of Unification is the Point of Unification of the PE executing the cache maintenance instruction.
- In AArch32 state, all of the maintenance instructions are available from EL1 or higher.
- In AArch64 state, branch predictors are always invisible to software, and therefore AArch64 state does not provide any branch predictor maintenance instructions.

## Table G4-3 AArch32 System instructions for cache maintenance

| Register                                   | Instruction                                                    |
|--------------------------------------------|----------------------------------------------------------------|
| Instruction cache maintenance instructions | Instruction cache maintenance instructions                     |
| ICIALLUIS                                  | Invalidate all to Point of Unification, Inner Shareable        |
| ICIALLU                                    | Invalidate all to Point of Unification                         |
| ICIMVAU, Rt                                | Invalidate by virtual address to Point of Unification          |
| Data cache maintenance instructions        | Data cache maintenance instructions                            |
| DCIMVAC, Rt                                | Invalidate by virtual address to Point of Coherency            |
| DCISW, Rt                                  | Invalidate by set/way                                          |
| DCCMVAC, Rt                                | Clean by virtual address to Point of Coherency                 |
| DCCSW, Rt                                  | Clean by set/way                                               |
| DCCMVAU, Rt                                | Clean by virtual address to Point of Unification               |
| DCCIMVAC, Rt                               | Clean and invalidate by virtual address to Point of Coherency  |
| DCCISW, Rt                                 | Clean and invalidate by set/way                                |
| Branch prediction maintenance instructions | Branch prediction maintenance instructions                     |
| BPIMVA, Rt                                 | Invalidate the virtual address from the branch predictors      |
| BPIALLIS, Rt                               | Invalidate all entries from branch predictors, Inner Shareable |
| BPIALL, Rt                                 | Invalidate all entries from branch predictors                  |
| CLRBHB                                     | Clear branch history                                           |

A DSB instruction intended to ensure the completion of cache or branch predictor maintenance instructions must have an access type of both loads and stores.

In an implementation where the branch predictors are architecturally invisible, the BPIMV A, BPIALLIS, and BPIALL instructions can execute as NOP s.

The following subsections give more information about these instructions:

- AArch32 instruction cache maintenance instructions (IC*).
- AArch32 data cache maintenance instructions (DC*).
- Branch predictors.
- General requirements for the scope of cache and branch predictor maintenance instructions.
- Effects of instructions that operate by V A to the Point of Coherency.
- Effects of instructions that operate by V A but not to the Point of Coherency.
- Effects of All and set/way maintenance instructions.
- Effects of virtualization and security on the AArch32 cache maintenance instructions.
- Boundary conditions for cache maintenance instructions.

- Ordering of cache and branch predictor maintenance instructions.
- Performing cache maintenance instructions.

## G4.4.7.1 AArch32 instruction cache maintenance instructions (IC*)

Where an address argument for these instructions is required, it takes the form of a 32-bit register that holds the virtual address argument. No alignment restrictions apply for this address.

Any cache maintenance instruction operating by V A includes as part of any required V A to PA translation:

- For an instruction executed at EL1, the current system ASID.
- The current Security state.
- Whether the instruction was performed from Hyp mode, or at EL1.
- For an instruction executed at EL1, the VMID.

That VA to PA translation might fault. However for an instruction cache maintenance instruction that operates by V A:

- It is IMPLEMENTATION DEFINED whether the operation can generate a Data Abort exception for a Translation fault or an Access flag fault.
- The operation cannot generate a Data Abort exception for a Domain fault or a Permission fault, except for the Permission fault case on a Stage 2 fault on a stage 1 translation table walk.

For more information about the possible faults on an instruction that operates by V A, see Types of MMU faults.

An instruction cache maintenance instruction can complete at any time after it is executed, but is only guaranteed to be complete, and its effects visible to other observers, following a DSB instruction executed by the PE that executed the cache maintenance instruction. See also the completion requirements for cache and branch predictor maintenance instructions in Completion and endpoint ordering.

See also Ordering of cache and branch predictor maintenance instructions.

## G4.4.7.2 AArch32 data cache maintenance instructions (DC*)

Data cache maintenance instructions that take a set/way/level argument take a 32-bit register.

If a data cache maintenance by set/way instruction specifies a set, way, or level argument that is larger than the value supported by the implementation then the instruction is CONSTRAINED UNPREDICTABLE, see Out of range values of the Set/Way/Index fields in cache maintenance instructions or the instruction description.

DCISW instructions executed at EL1 perform a clean and invalidate, meaning it performs the same maintenance as a DCCISW instruction, if all of the following apply:

- EL2 is implemented and enabled in the current Security state.
- Either:
- -EL2 is using AArch32 and the value of HCR.SWIO is 1.
- -EL2 is using AArch64 and the value of HCR\_EL2.SWIO is 1.

Where an address argument for these instructions is required, it takes the form of a 32-bit register that holds the virtual address argument. No alignment restrictions apply for this address.

Any cache maintenance instruction operating by V A includes as part of any required V A to PA translation:

- For an instruction executed at EL1, the current system ASID.
- The current Security state.
- Whether the instruction was performed from Hyp mode, or from EL1.
- For an instruction executed from EL1, the VMID.

That VA to PA translation might fault. However a data or unified cache maintenance instruction that operates by V A cannot generate a Data Abort exception for a Domain fault, and cannot generate a Data Abort exception for a Permission fault, except for the Permission fault case on a Stage 2 fault on a stage 1 translation table walk.

For more information about the possible faults on an instruction that operates by V A, see Types of MMU faults.

DCIMVAC and DCISW instructions executed at EL1 perform a clean and invalidate, meaning they perform the same maintenance as a DCCIMVAC or DCCISW instruction respectively, if all of the following apply:

- EL2 is implemented and enabled in the current Security state.
- PL1&amp;0 stage two address translation is enabled, meaning either:
- -EL2 is using AArch32 and the value of HCR.VM is 1.
- -EL2 is using AArch64 and the value of HCR\_EL2.VM is 1.

If a memory fault that sets FAR for the translation regime applicable for the cache maintenance instruction is generated from a data cache maintenance instruction, the FAR holds the address specified in the register argument of the instruction.

See also Ordering of cache and branch predictor maintenance instructions.

## G4.4.7.3 Branch predictors

In AArch32 state it is IMPLEMENTATION DEFINED whether branch prediction is architecturally visible. This means that under some circumstances software must perform branch predictor maintenance to avoid incorrect execution caused by out-of-date entries in the branch predictor. For example, to ensure correct operation it might be necessary to invalidate branch predictor entries on a change to instruction memory, or a change of instruction address mapping. For more information, see Specific requirements for branch predictor maintenance instructions.

In an implementation where the branch predictors are architecturally invisible, the branch predictor maintenance instructions can execute as NOP s.

An invalidate all operation on the branch predictor ensures that any location held in the branch predictor has no functional effect on execution. An invalidate branch predictor by V A instruction operates on the address of the branch instruction, but can affect other branch predictor entries.

Note

The architecture does not make visible the range of addresses in a branch predictor to which the invalidate operation applies. This means the address used in the invalidate by V A operation must be the address of the branch to be invalidated.

If branch prediction is architecturally visible, an instruction cache invalidate all operation also invalidates all branch predictors.

See also Ordering of cache and branch predictor maintenance instructions.

## G4.4.7.3.1 Specific requirements for branch predictor maintenance instructions

If, for a given translation regime and a given ASID and VMID as appropriate, the instructions at any virtual address change, then branch predictor maintenance instructions must be performed to invalidate entries in the branch predictor, to ensure that the change is visible to subsequent execution. This maintenance is required when writing new values to instruction locations. It can also be required as a result of any of the following situations that change the translation of a virtual address to a physical address, if, as a result of the change to the translation, the instructions at the virtual addresses change:

- For any translation regime other than the Non-secure PL1&amp;0 translation regime, enabling or disabling stage 1 translations.
- For the Non-secure PL1&amp;0 translation regime:
- -When stage 2 translations are enabled, enabling or disabling stage 1 translations unless accompanied by a change of VMID.
- -When stage 2 translations are disabled, enabling or disabling stage 1 translations.
- -Enabling or disabling stage 2 translations.
- Writing new mappings to the translation tables.
- Any change to the TTBR0, TTBR1, or TTBCR registers, unless:
- -For a change to the Secure PL1&amp;0 translation regime, the change is accompanied by a change to the ASID.
- -For a change to the stage 1 translations of the Non-secure PL1&amp;0 translation regime, the change is accompanied by a change to the ASID or a change to the VMID.

- Any change to the VTTBR or VTCR registers, unless accompanied by a change to the VMID.

Note

Invalidation is not required if the changes to the translations are such that the instructions associated with the non-faulting translations of a virtual address, for a given translation regime and a given ASID and VMID, as appropriate, remain unchanged throughout the sequence of changes to the translations. Examples of translation changes to which this applies are:

- Changing a valid translation to a translation that generates an MMU fault.

- Changing a translation that generates an MMU fault to a valid translation.

Failure to invalidate entries might give CONSTRAINED UNPREDICTABLE results, caused by the execution of old branches. For more information, see Ordering of cache and branch predictor maintenance instructions.

Note

- There is no requirement to use the branch predictor maintenance operations to invalidate the branch predictor after:

- Changing the ContextID or VMID.

- A cache maintenance instruction that is identified as also flushing the branch predictors, see AArch32 cache and branch predictor maintenance instructions.

Cache maintenance system instructions shows the branch predictor maintenance operations in a VMSA implementation.

## G4.4.7.3.2 Behavior of the branch predictors at reset

In AArch32 state:

- If branch predictors are not architecturally invisible:

- The branch predictors reset to an IMPLEMENTATION DEFINED state that might be UNKNOWN.

- The branch predictors are disabled at reset.

- An implementation can require the use of a specific branch predictor initialization routine to invalidate the branch predictor storage array before it is enabled. The exact form of any required initialization routine is IMPLEMENTATION DEFINED, but the routine must be documented clearly as part of the documentation of the device.

- Arm recommends that whenever an invalidation routine is required, it is based on the AArch32 branch predictor maintenance operations.

## Similar rules apply:

- To cache behavior, see Behavior of caches at reset.

- To TLB behavior, see TLB behavior at reset.

## G4.4.7.4 General requirements for the scope of cache and branch predictor maintenance instructions

The specification of the cache maintenance and branch predictor instructions describes what each instruction is guaranteed to do in a system. It does not limit other behaviors that might occur, provided they are consistent with the requirements described in General behavior of the caches, Behavior of caches at reset, and Prefetching into cache.

This means that as a side-effect of a cache maintenance instruction:

- Any location in the cache might be cleaned.

- Any unlocked location in the cache might be cleaned and invalidated.

As a side-effect of a branch predictor maintenance instruction, any entry in the branch predictor might be invalidated.

Note

Arm recommends that, for best performance, such side-effects are kept to a minimum. Arm strongly recommends that the side-effects of operations performed in Non-secure state do not have a significant performance impact on execution in Secure state.

## G4.4.7.5 Effects of instructions that operate by VA to the Point of Coherency

For Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, these instructions must affect the caches of other PEs in the Shareability domain described by the Shareability attributes of the V A supplied with the instruction.

For Device memory and Normal memory that is Inner Non-cacheable, Outer Non-cacheable, these instructions must affect the caches of all PEs in the Outer Shareable Shareability domain of the PE on which the instruction is operating.

In all cases, for any affected PE, these instructions affect all data and unified caches to the Point of Coherency.

## Table G4-4 PEs affected by cache maintenance instructions to the Point of Coherency

| Shareability    | PEs affected                                                                               | Effective to                                |
|-----------------|--------------------------------------------------------------------------------------------|---------------------------------------------|
| Non-shareable   | The PE performing the operation                                                            | The Point of Coherency of the entire system |
| Inner Shareable | All PEs in the same Inner Shareable Shareability domain as the PE performing the operation | The Point of Coherency of the entire system |
| Outer Shareable | All PEs in the same Outer Shareable Shareability domain as the PE performing the operation | The Point of Coherency of the entire system |

## G4.4.7.6 Effects of instructions that operate by VA but not to the Point of Coherency

The following instruction operate by V A but not to the Point of Coherency:

- Clean data or unified cache line by MV A to the Point of Unification, DCCMV AU.
- Invalidate instruction cache line by MV A to Point of Unification, ICIMV AU.
- Invalidate by MVA from branch predictors, BPIMVA.

For these instructions, Table G4-5 shows how, for a V A in a Normal or Device memory location, the Shareability attribute of the V A determines the minimum set of PEs affected, and the point to which the instruction must be effective.

## Table G4-5 PEs affected by cache maintenance instructions to the Point of Unification

| Shareability                       | PEs affected                                                                                | Effective to                                                                                                                                                                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Non-shareable                      | The PE executing the instruction                                                            | The Point of Unification of instruction cache fills, data cache fills and write-backs, and translation table walks, on the PE executing the instruction                                                            |
| Inner Shareable or Outer Shareable | All PEs in the same Inner Shareable Shareability domain as the PE executing the instruction | The Point of Unification of instruction cache fills, data cache fills and write-backs, and translation table walks, of all PEs in the same Inner Shareable Shareability domain as the PE executing the instruction |

Note

The set of PEs guaranteed to be affected is never greater than the PEs in the Inner Shareable Shareability domain containing the PE executing the instruction.

## G4.4.7.7 Effects of All and set/way maintenance instructions

The ICIALLU, BPIALL and DC * set/way instructions apply only to the caches and branch predictors of the PE that performs the instruction. If the branch predictors are architecturally-visible, ICIALLU also performs a BPIALL operation.

The ICIALLUIS and BPIALLIS instructions can affect the caches and branch predictors of all PEs in the same Inner Shareable Shareability domain as the PE that performs the instruction. If the branch predictors are architecturally-visible, ICIALLUIS also performs a BPIALLIS operation. These instructions have an effect to the Point of Unification of instruction cache fills, data cache fills, and write-backs, and translation table walks, of all PEs in the same Inner Shareable Shareability domain.

Note

The possible presence of system caches, as described in System level caches, means architecture does not guarantee that all levels of cache can be maintained using set/way instructions.

## G4.4.7.8 Effects of virtualization and security on the AArch32 cache maintenance instructions

Each Security state has its own physical address space, and therefore cache entries are associated with physical address space. In addition, cache maintenance and branch predictor instructions performed in Non-secure state have to take account of:

- Whether the instruction was performed at EL1 or at EL2.
- For instructions that operate by V A, the current VMID.

Table G4-6 shows the effects of virtualization and security on these maintenance instructions.

Table G4-6 Effects of virtualization and security on the AArch32 cache maintenance instructions

| Cache maintenance instructions                                                        | Specified entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data or unified cache maintenance instructions                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Invalidate, Clean, or Clean and Invalidate by VA: DCIMVAC, DCCMVAC, DCCMVAU, DCCIMVAC | All lines that hold the PA that, in the current translation regime, are mapped to by the combination of all of : • The specified VA. • For an instruction executed at EL1, the current ASID if the location is mapped to by a non-global page. • For a Non-secure instruction executed at EL1, the current VMID a . • For a Non-secure instruction executed at EL0, when EL2 is using AArch32 or when EL2 is using AArch64 and the Effective value of HCR_EL2.{E2H, TGE} is not {1,1}, the currentVMID a . • For a Secure instruction executed at EL1, when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, the currentVMID a . • For a Secure instruction executed at EL0, when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, and the Effective value of HCR_EL2.{E2H, TGE} is not {1,1}, the currentVMID a . |
| Invalidate, Clean, or Clean and Invalidate by set/way: DCISW, DCCSW, DCCISW           | For a Non-secure instruction, the line specified by set/way provided that the entry comes from the Non-secure PA space. For a Secure instruction, the line specified by set/way regardless of the PA space that the entry has come from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Instruction cache maintenance instructions                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Cache maintenance instructions     | Specified entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invalidate by VA: ICIMVAU          | All lines corresponding to the specified VA b in the current translation regime and: • For an instruction executed at EL1 or EL0, the current ASID. • For a Non-secure instruction executed at EL1 or EL0, the currentVMID a . • For a Secure instruction executed at EL1 when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, the currentVMID a . • For a Secure instruction executed at EL0 when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, and the Effective value of HCR_EL2.{E2H, TGE} is not {1,1}, the currentVMID a                                                                                                                                                    |
| Invalidate All: ICIALLU, ICIALLUIS | . Can invalidate any unlocked entry in the instruction cache, and are required to invalidate: • For a Non-secure instruction executed at EL1, all instruction cache lines containing Non-secure entries associated with the current VMID. • For a Non-secure instruction executed at EL2, all instruction lines containing Non-secure entries. • For a Secure instruction executed at EL1 when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, all instruction cache lines containing entries associated with the current VMID. • For a Secure instruction executed at EL1 when EL3 is using AArch64 and the Effective value of SCR_EL3.EEL2 is 0, all instruction cache lines. |
| Branch predictor instructions c    | cache lines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Invalidate by VA: BPIMVA           | All lines that, in the current translation regime, are mapped to by the combination of all of: • The specified VA. • For an instruction executed at EL1 or EL0, the current ASID. • For a Non-secure instruction executed at EL1 or EL0, the currentVMID a . • For a Secure instruction executed at EL1, when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, the currentVMID a . • For a Secure instruction executed at EL0, when EL3 is using                                                                                                                                                                                                                                 |

| Cache maintenance instructions   | Specified entry                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Invalidate all: BPIALL, BPIALLIS | Can invalidate any unlocked entry in the branch predictor, and are required to invalidate:                                                                 |
|                                  | • For a Non-secure instruction executed at EL1, all lines containing Non-secure entries associated with the current VMID.                                  |
|                                  | • For a Non-secure instruction executed at EL2, all lines containing Non-secure entries.                                                                   |
|                                  | • For a Secure instruction executed at EL1 when EL3 is using AArch64 and SCR_EL3.EEL2 is 1, all lines containing entries associated with the current VMID. |
|                                  | • For a Secure instruction executed at EL1 when EL3 is using AArch64 and the Effective value of SCR_EL3.EEL2 is 0, all lines.                              |
|                                  | • For a Secure instruction executed at EL3, all lines.                                                                                                     |

a. Dependencies on the VMID apply even when either EL2 is using AArch32 and the value of HCR.VM is 0 or EL2 is using AArch64 when enabled for the current Security state, and the value of HCR\_EL2.VM is 0. If the PE resets into an Exception level that is using AArch32, VTTBR.VMID resets to zero, meaning there is a valid VMID from reset. However, if the PE resets into an Exception level that is using AArch64, VTTBR\_EL2.VMID resets to a value that is architecturally UNKNOWN, and the VTTBR\_EL2.VMID field must be set to a known value, that might be zero, as part of the PE initialization sequence.

b. The type of instruction cache used affects the interpretation of the specified entries in this table such that:

- For a PIPT instruction cache, the cache maintenance applies to all entries whose physical address corresponds to the specified address.
- For a VIPT instruction cache, the cache maintenance applies to entries whose virtual index and physical tag corresponds to the specified address.

For information of types of instruction cache, see Instruction caches.

c. In an implementation where the branch predictors are architecturally invisible, these instructions can execute as NOP s.

For locked entries and entries that might be locked, the behavior of cache maintenance instructions described in The interaction of cache lockdown with cache maintenance instructions applies.

With an implementation that generates aborts if entries are locked or might be locked in the cache, when the use of lockdown aborts is enabled, these aborts can occur on any cache maintenance instructions.

In an implementation that includes EL2:

- The architecture does not require cache cleaning when switching between virtual machines. Cache invalidation by set/way must not present an opportunity for one virtual machine to corrupt state associated with a second virtual machine. To ensure this requirement is met, EL1 invalidate by set/way instructions executed in at EL1 when HCR\_EL2.VM or HCR.VM is 1 and EL2 is enabled can, instead, perform a clean and invalidate by set/way.
- The AArch32 Data cache invalidate instructions DCIMVAC and DCISW perform a cache clean as well as a cache invalidate, meaning DCIMVAC performs the same invalidation as a DCCIMVAC instruction, and DCISW performs the same invalidation as a DCCISW instruction, if both of the following apply:
- -EL2 is using AArch32, the value of HCR.VM is 1, and the instruction is executed at Non-secure EL1.
- -EL2 is using AArch64, the value of HCR\_EL2.VM is 1, EL2 is enabled, and the instruction is executed at EL1.
- The AArch32 Data cache invalidate by set/way instruction DCISW performs a cache clean as well as a cache invalidate, meaning it performs the same invalidation as a DCCISW instruction, if either of the following apply:
- -EL2 is using AArch32, the value of HCR.SWIO is 1, and the instruction is executed at Non-secure EL1.
- -EL2 is using AArch64, the value of HCR\_EL2.SWIO is 1, EL2 is enabled, and the instruction is executed at EL1.
- TLB and instruction cache invalidate instructions are broadcast across the Inner Shareable domain when either:
- -EL2 is using AArch32, the value of HCR.FB is 1, and execution is at Non-secure EL1.
- -EL2 is using AArch64, the value of HCR\_EL2.FB is 1, EL2 is enabled, and the instruction is executed at EL1.

When EL1 is using AArch32, this applies to the TLBIMVA, TLBIASID, TLBIMVAA, TLBIMVAL, TLBIMVAAL, and ICIALLU instructions. This means the instruction performs the invalidation that would be performed by the corresponding Inner Shareable instruction, for example ICIALLU performs the invalidation that would be performed by ICIALLUIS, and BPIALL performs the invalidation that would be performed by BPIALLIS.

For more information about the cache maintenance instructions, see About cache maintenance in AArch32 state, AArch32 cache and branch predictor maintenance instructions, and The AArch32 Virtual Memory System Architecture.

## G4.4.7.9 Boundary conditions for cache maintenance instructions

Cache maintenance instructions operate on the caches regardless of whether the System register Cacheability controls force all memory accesses to be Non-cacheable.

For VA-based cache maintenance instructions, the instructions operate on the caches regardless of the memory type and Cacheability attributes marked for the memory address in the VMSA translation table entries. This means that the effects of the cache maintenance instructions can apply regardless of:

- Whether the address accessed:
- -Is Normal memory or Device memory.
- -Has the Cacheable attribute or the Non-cacheable attribute.
- Any applicable domain control of the address accessed.
- The access permissions for the address accessed, other than the effect of the stage two write permission on data or unified cache invalidation instructions.

## G4.4.7.10 Ordering of cache and branch predictor maintenance instructions

The following rules describe the effect of the memory order model on the cache and branch predictor maintenance instructions:

- All cache and branch predictor maintenance instructions that do not specify an address execute, relative to each other, in program order.

All cache and branch predictor instructions that specify an address:

- -Execute in program order relative to all cache and branch predictor operations that do not specify an address.
- -Execute in program order relative to all cache and branch predictor operations that specify the same address.
- -Can execute in any order relative to cache and branch predictor operations that specify a different address.
- Where a cache maintenance or branch predictor instruction appears in program order before a change to the translation tables, the architecture guarantees that the cache or branch predictor maintenance instruction uses the translations that were visible before the change to the translation tables.
- Where a change of the translation tables appears in program order before a cache maintenance or branch predictor instruction, software must execute the sequence outlined in Ordering and completion of TLB maintenance instructions before performing the cache or branch predictor maintenance instruction, to ensure that the maintenance operation uses the new translations.
- A DMB instruction causes the effect of all data or unified cache maintenance instructions appearing in program order before the DMB to be visible to all explicit memory read and write effects appearing in program order after the DMB .

Also, a DMB instruction ensures that the effects of any data or unified cache maintenance instruction appearing in program order before the DMB are observable by any observer in the same required Shareability domain before any data or unified cache maintenance or explicit memory operations appearing in program order after the DMB are observed by the same observer. Completion of the DMB does not guarantee the visibility of all data to other observers. For example, all data might not be visible to a translation table walk, or to instruction fetches.

- A DSB is required to guarantee the completion of all cache maintenance instruction that appear in program order before the DSB instruction.
- AContext Synchronization event is required to guarantee the effects of any branch predictor maintenance operation. This means a Context Synchronization event causes the effect of all completed branch predictor maintenance operations appearing in program order before the Context Synchronization event to be visible to all instructions after the Context Synchronization event.

This means that, if a branch instruction appears after an invalidate branch predictor operation and before any Context Synchronization event, it is CONSTRAINED UNPREDICTABLE whether the branch instruction is affected by the invalidate. Software must avoid this ordering of instructions, because it might cause CONSTRAINED UNPREDICTABLE behavior.

- Any data or unified cache maintenance instruction by V A must be executed in program order relative to any explicit memory read or write effect on the same PE to an address covered by the V A of the cache instruction if that load or store is to Normal Cacheable memory. The order of memory accesses that result from the cache maintenance instruction, relative to any other memory accesses to Normal Cacheable memory, are subject to the memory ordering rules. For more information, see Definition of the memory model.
- Any data or unified cache maintenance instruction by V A can be executed in any order relative to any explicit memory read or write effect on the same PE to an address covered by the V A of the cache maintenance instruction if that load or store is not to Normal Cacheable memory.
- There is no restriction on the ordering of data or unified cache maintenance instruction by V A relative to any explicit memory read or write effect on the same PE where the address of the explicit memory read or write effect is not covered by the V A of the cache instruction. Where the ordering must be restricted, a DMB instruction must be inserted to enforce ordering.
- There is no restriction on the ordering of a data or unified cache maintenance instruction by set/way relative to any explicit memory read or write effect on the same PE. Where the ordering must be restricted, a DMB instruction must be inserted to enforce ordering.
- Software must execute a Context Synchronization event after the completion of an instruction cache maintenance instruction, to guarantee that the effect of the maintenance instruction is visible to any instruction fetch.

A DSB instruction intended to ensure the completion of cache maintenance instructions or branch predictor instructions must have an access type of both loads and stores.

See also the completion requirements for cache and branch predictor maintenance instructions in Completion and endpoint ordering.

The scope of instruction cache maintenance depends on the type of the instruction cache. For more information, see Instruction caches.

## Example G4-1 Cache cleaning operations for self-modifying code

## The sequence of cache cleaning operations for a line of self-modifying code on a uniprocessor system is:

```
; Coherency example for data and instruction accesses within the same Inner Shareable domain. ; Enter this code with <Rt> containing a new 32-bit instruction, ; to be held in Cacheable space at a location pointed to by Rn. Use STRH in the first line ; instead of STR for a 16-bit instruction. STR Rt, [Rn] DCCMVAU Rn ; Clean data cache by MVA to point of unification (PoU) DSB ; Ensure visibility of the data cleaned from cache ICIMVAU Rn ; Invalidate instruction cache by MVA to PoU BPIMVA Rn ; Invalidate branch predictor by MVA to PoU DSB ; Ensure completion of the invalidations ISB ; Synchronize the fetched instruction stream
```

## G4.4.7.11 Performing cache maintenance instructions

To ensure all cache lines in a block of address space are maintained through all levels of cache Arm strongly recommends that software:

- For data or unified cache maintenance, uses the CTR.DMinLine value to determine the loop increment size for a loop of data cache maintenance by V A instructions.
- For instruction cache maintenance, uses the CTR.IMinLine value to determine the loop increment size for a loop of instruction cache maintenance by V A instructions.

## G4.4.7.11.1 Example code for cache maintenance instructions

The cache maintenance instructions by set/way can be used to clean or invalidate, or both, the entirety of one or more levels of cache attached to a PE. However, unless all PEs attached to the caches regard all memory locations as

Non-cacheable, it is not possible to prevent locations being allocated into the cache during such a sequence of the cache maintenance instructions.

Note

Because the set/way instructions operate only locally, there is no guarantee of the atomicity of cache maintenance between different PEs, even if those different PEs are each executing the same cache maintenance instructions at the same time. Because any cacheable line can be allocated into the cache at any time, it is possible for a cache line to migrate from an entry in the cache of one PE to the cache of a different PE in a way that means the cache line is not affected by set/way based cache maintenance. Therefore, Arm strongly discourages the use of set/way instructions to manage coherency in coherent systems. The expected use of the cache maintenance instructions that operate by set/way is limited to the cache maintenance associated with the powerdown and powerup of caches, if this is required by the implementation.

The limitations of cache maintenance by set/way mean maintenance by set/way does not happen on multiple PEs, and cannot be made to happen atomically for each address on each PE. Therefore in multiprocessor or multithreaded systems, the use of cache maintenance by set/way to clean, or clean and invalidate, the entire cache for coherency management with very large buffers or with buffers with unknown address can fail to provide the expected coherency results because of speculation by other PEs, or possibly by other threads. The only way that these instructions can be used in this way is to first ensure that all PEs that might cause speculative accesses to caches that need to be maintained are not capable of generating speculative accesses. This can be achieved by ensuring that those PEs have no memory locations with a Normal Cacheable attribute. Such an approach can have very large system performance effects, and Arm advises implementers to use hardware coherency mechanisms in systems where this will be an issue.

System level caches refers to other limitations of cache maintenance by set/way.

The following example code for cleaning a data or unified cache to the Point of Coherency illustrates a generic mechanism for cleaning the entire data or unified cache to the Point of Coherency. It assumes the current Cache Size Identification Register is in 32-bit format. For more information, see Possible formats of the Cache Size Identification Registers, CCSIDR and CCSIDR2.

```
MRC p15, 1, R0, c0, c0, 1 ; Read CLIDR into R0 ANDS R3, R0, #0x07000000 MOV R3, R3, LSR #23 ; Cache level value (naturally aligned) BEQ Finished MOV R10, #0 Loop1 ADD R2, R10, R10, LSR #1 ; Work out 3 x cache level MOV R1, R0, LSR R2 ; bottom 3 bits are the Cache type for this level AND R1, R1, #7 ; get those 3 bits alone CMP R1, #2 BLT Skip ; no cache or only instruction cache at this level MCR p15, 2, R10, c0, c0, 0 ; write CSSELR from R10 ISB ; ISB to sync the change to the CCSIDR MRC p15, 1, R1, c0, c0, 0 ; read current CCSIDR to R1 AND R2, R1, #7 ; extract the line length field ADD R2, R2, #4 ; add 4 for the line length offset (log2 16 bytes) MOV R4, #0x3FF ANDS R4, R4, R1, LSR #3 ; R4 is the max number on the way size (right aligned) CLZ R5, R4 ; R5 is the bit position of the way size increment MOV R9, R4 ; R9 working copy of the max way size (right aligned) Loop2 MOV R7, #0x00007FFF ANDS R7, R7, R1, LSR #13 ; R7 is the max number of the index size (right aligned) Loop3 ORR R11, R10, R9, LSL R5 ; factor in the way number and cache number into R11 ORR R11, R11, R7, LSL R2 ; factor in the index number MCR p15, 0, R11, c7, c10, 2 ; DCCSW, clean by set/way SUBS R7, R7, #1 ; decrement the index BGE Loop3 SUBS R9, R9, #1 ; decrement the way number BGE Loop2 Skip ADD R10, R10, #2 ; increment the cache number CMP R3, R10 DSB ; ensure completion of previous cache maintenance instruction BGT Loop1 Finished
```

Similar approaches can be used for all cache maintenance instructions.

## G4.4.8 Execution, prefetching and data prediction restriction System instructions

When FEAT\_SPECRES is implemented, either alone or alongside FEAT\_SPECRES2, the System instructions for prediction restriction listed in Table G4-7 prevent predictions based on information gathered from earlier execution within a particular execution context (CTX), from affecting the later speculative execution within that CTX, to the extent that the speculation execution is observable through side-channels.

The prediction restriction System instructions being used by a particular CTX apply to:

- All control flow prediction resources that predict execution addresses.
- Data value prediction.
- Cache allocation prediction.

Table G4-7 Prediction restriction System instructions

|               | Register   | Instruction                                               |
|---------------|------------|-----------------------------------------------------------|
| FEAT_SPECRES  | CFPRCTX    | Control Flow Prediction Restriction by Context            |
|               | CPPRCTX    | Cache Prefetch Prediction Restriction by Context          |
|               | DVPRCTX    | Data Value Prediction Restriction by Context              |
| FEAT_SPECRES2 | COSPRCTX   | Clear Other Speculative Prediction Restriction by Context |

For these System instructions, the CTX is defined by:

- The Security state.
- The Exception level.
- When executing at EL1, the VMID.
- When executing at EL0 when using the PL1&amp;0 translation regime, the ASID and VMID.

## Note

- The data value prediction applies to all prediction resources that use some form of training to speculate data values as part of an execution.
- The cache allocation applies to all instruction and data caches, and TLB prefetching hardware used by the executing PE that applies to the supplied context.

The context information is passed as a register argument, and is restricted so that:

- Execution of the System instruction at EL0 applies only to the current hardware defined context.
- Execution of the System instruction at EL1 applies only to the current VMID and Security state, and does not apply to EL2 or EL3.
- Execution of the System instruction at EL2 can apply only to the current Security state, and does not apply to EL3.

If the System instruction is specified to apply to a combination of Security state and Exception level that is not implemented, or an Exception level which is higher than the Exception level that the System instruction is executed at, then the System instruction is treated as a NOP .

When the System instruction is complete and synchronized, no predictions of the restricted type for the affected context are influenced by the execution of the program before the System instruction in a manner that can be observed by the use of any side channels.

Note

- Prediction restriction System instructions do not require the invalidation of prediction structures so long as the behavior described for completion is met by an implementation.
- Prediction restriction System instructions are permitted to invalidate more prediction information than is defined by the supplied CTX.

These System instructions are guaranteed to be complete following a DSB that covers both read and write behavior on the same PE that executed the original instruction. A subsequent Context synchronization event is required to ensure that the effect of the completion of the instructions is synchronized to the current execution.

In AArch32 state, EL0 access to the System instructions is controlled by SCTLR.EnRCTX.

## G4.4.9 Cache lockdown

The concept of an entry locked in a cache is allowed, but not architecturally defined. How lockdown is achieved is IMPLEMENTATION DEFINED and might not be supported by:

- An implementation.
- Some memory attributes.

An unlocked entry in a cache might not remain in that cache. The architecture does not guarantee that an unlocked cache entry remains in the cache or remains incoherent with the rest of memory. Software must not assume that an unlocked item that remains in the cache remains dirty.

Alocked entry in a cache is guaranteed to remain in that cache. The architecture does not guarantee that a locked cache entry remains incoherent with the rest of memory, that is, it might not remain dirty.

## G4.4.9.1 The interaction of cache lockdown with cache maintenance instructions

The interaction of cache lockdown and cache maintenance instructions is IMPLEMENTATION DEFINED. However, an architecturally-defined cache maintenance instruction on a locked cache line must comply with the following general rules:

- The effect of the following instructions on locked cache entries is IMPLEMENTATION DEFINED:
- -Cache clean by set/way, DCCSW.
- -Cache invalidate by set/way, DCISW.
- -Cache clean and invalidate by set/way, DCISW.
- -Instruction cache invalidate all, ICIALLU and ICIALLUIS.

However, one of the following approaches must be adopted in all these cases:

1. If the instruction specified an invalidation, a locked entry is not invalidated from the cache.
2. If the instruction specified a clean it is IMPLEMENTATION DEFINED whether locked entries are cleaned.
3. If an entry is locked down, or could be locked down, an IMPLEMENTATION DEFINED Data Abort exception is generated, using the Fault status code defined for this purpose. See Data Abort exception.

This permits a usage model for cache invalidate routines to operate on a large range of addresses by performing the required operation on the entire cache, without having to consider whether any cache entries are locked.

The effect of the following instructions is IMPLEMENTATION DEFINED:

- Cache clean by virtual address, DCCMVAC and DCCMVAU.
- Cache invalidate by virtual address, DCIMVAC.
- Cache clean and invalidate by virtual address, DCCIMVAC.

However, one of the following approaches must be adopted in all these cases:

1. If the instruction specified an invalidation, a locked entry is invalidated from the cache. For the clean and invalidate instructions, the entry must be cleaned before it is invalidated.

2. If the instruction specified an invalidation, a locked entry is not invalidated from the cache. If the instruction specified a clean it is IMPLEMENTATION DEFINED whether locked entries are cleaned.
3. If an entry is locked down, or could be locked down, an IMPLEMENTATION DEFINED Data Abort exception is generated, using the Fault status code defined for this purpose. See DFSR or HSR.

In an implementation that includes EL2, if HCR.TIDCP is set to 1, any exception relating to lockdown of an entry associated with Non-secure memory is routed to EL2.

Note

An implementation that uses an abort mechanism for entries that can be locked down but are not actually locked down must:

- Document the IMPLEMENTATION DEFINED instruction sequences that perform the required operations on entries that are not locked down.
- Implement one of the other permitted alternatives for the locked entries.

Arm recommends that, when possible, such IMPLEMENTATION DEFINED instruction sequences use architecturally-defined instructions. This minimizes the number of customized instructions required.

In addition, an implementation that uses an abort to handle cache maintenance instructions for entries that might be locked must provide a mechanism that ensures that no entries are locked in the cache.

The reset setting of the cache must be that no cache entries are locked.

## G4.4.9.1.1 Additional cache functions for the implementation of lockdown

An implementation can add additional cache maintenance functions for the handling of lockdown in the IMPLEMENTATION DEFINED space.

## G4.4.10 System level caches

The Arm Architecture defines a system cache as a cache that is not described in the PE Cache Identification registers, CCSIDR, CCSIDR2, and CLIDR, and for which the set/way cache maintenance instructions do not apply.

Conceptually, three classes of system cache can be envisaged:

1. System caches which lie before the point of coherency and cannot be managed by cache maintenance instructions. Such systems fundamentally undermine the concept of cache maintenance instructions operating to the point of coherency, as they imply the use of non-architecture mechanisms to manage coherency. The use of such systems in the Arm architecture is explicitly prohibited.
2. System caches which lie before the point of coherency and can be managed by cache maintenance by address instructions that apply to the point of coherency, but cannot be managed by cache maintenance by set/way instructions. Where maintenance of the entire system cache must be performed, as is the case for power management, it must be performed using non-architectural mechanisms.
3. System caches which lie beyond the point of coherency and so are invisible to software. The management of such caches is outside the scope of architecture.