## B2.4 Additional ordering requirements outside of the scope of the formal concurrency model

The following sections present ordering rules which have been architected but not yet formalized. As a consequence they do not appear in the formal concurrency model, nor in the corresponding transliteration in Ordering requirements defined by the formal concurrency model. They will be integrated into Ordering requirements defined by the formal concurrency model in due course.

## B2.4.1 Completion and endpoint ordering

For all memory, the completion rules are defined as:

- AMemory Read effect E1 to a Location is complete for a shareability domain when all of the following are true:
- -Any Memory Write Effect to the same Location by an observer within the shareability domain will be Coherence-after E1.
- -All Implicit TTD Memory Read Effects associated with E1 are complete for that shareability domain.
- AMemory Write effect E1 to a Location is complete for a shareability domain when all of the following are true:
- -Any Memory Write Effect to the same Location by an observer within the shareability domain will be Coherence-after E1.
- -Any Memory Read Effect to the same Location by an observer within the shareability domain will be such that either Reads-from E1 or Reads-from a Memory Write effect that is Coherence-after E1.
- -All Implicit TTD Memory Read Effects associated with E1 are complete for that shareability domain.
- An Implicit TTD Memory Read Effect is complete for a shareability domain when the memory accesses associated with the Implicit TTD Memory Read Effect, including Hardware Update Effects, are complete for that shareability domain, and the TLB is updated.
- Acache maintenance instruction is complete for a shareability domain when the memory effects of the instruction are complete for that shareability domain, and Implicit TTD Memory Read Effects that arise from the instruction are complete for that shareability domain.
- ATLBinvalidate instruction is complete when all memory accesses using the TLB entries that have been invalidated are complete.

The completion of any cache or TLB maintenance instruction includes its completion on all PEs that are affected by both the instruction and the DSB operation that is required to guarantee visibility of the maintenance instruction.

Additionally, for Device-nGnRnE memory, a read or write of a Location in a Memory-mapped peripheral that exhibits side effects is complete only when the read or write both:

- Can begin to affect the state of the Memory-mapped peripheral.
- Can trigger all associated side effects, whether they affect other peripheral devices, PEs, or memory.

Interaction between observers in a system is not restricted to communication via shared variables in coherent memory. For example, an observer could configure an interrupt controller to raise an interrupt on another observer as a form of message passing. These interactions typically involve an additional agent, which defines the instruction sequence that is required to establish communication links between different observers. When these forms of interaction are used in conjunction with shared variables, a DSB instruction can be used to enforce ordering between them.

Note

This requirement for Device-nGnRnE memory is consistent with the memory access having reached the peripheral endpoint.

Note

These completion rules mean that, for example, a cache maintenance instruction that operates by V A to the PoC completes only after memory at the PoC has been updated.

## B2.4.1.1 Peripherals

This section defines a Memory-mapped peripheral and the total order of reads and writes to a peripheral which is defined as the Peripheral arrival order:

## Memory-mapped peripheral

A Memory-mapped peripheral occupies a memory region of IMPLEMENTATION DEFINED size and can be accessed using load and store instructions. Memory effects to a Memory-mapped peripheral can have side effects, such as causing the peripheral to perform an action. Values that are read from addresses within a Memory-mapped peripheral might not correspond to the last data value written to those addresses. As such, Memory effects to a Memory-mapped peripheral might not appear in the Reads-from or Coherence order relations.

## Peripheral arrival order

The Peripheral arrival order of a Memory-mapped peripheral is a total order on all Memory Read Effects and Memory Write Effects to that peripheral.

For a Memory Effect E1 and a Memory Effect E2 to the same peripheral if any of the following applies:

- All of the following apply:
- -Any of the following applies:
- -E1 is to Device-nGnRE Memory.
- -E1 is to Device-nGnRnE Memory.
- -Any of the following applies:
- -E2 is to Device-nGnRE Memory.
- -E2 is to Device-nGnRnE Memory.
- -Any of the following applies:
- -FEAT\_XS is not implemented.
- -All of the following apply:
- ꞏ FEAT\_XS is implemented.
- ꞏ E1 has the XS attribute.
- ꞏ E2 has the XS attribute.
- -All of the following apply:
- ꞏ FEAT\_XS is implemented.
- ꞏ E1 does not have the XS attribute.
- ꞏ E2 does not have the XS attribute.
- -E1 is in program-order before E2.
- All of the following apply:
- -Any of the following applies:
- -E1 is to Device-nGRE Memory.
- -E1 is to Device-nGnRE Memory.
- -E1 is to Device-nGnRnE Memory.
- -Any of the following applies:
- -E2 is to Device-nGRE Memory.
- -E2 is to Device-nGnRE Memory.
- -E2 is to Device-nGnRnE Memory.
- -E1 is Ordered-before E2.
- All of the following apply:
- -Any of the following applies:
- -E1 is to Device Memory.
- -E1 is to Non-cacheable Normal Memory.
- -Any of the following applies:
- -E2 is to Device Memory.
- -E2 is to Non-cacheable Normal Memory.
- -E1 is Barrier-ordered-before E2.

Then E1 is inserted in the Peripheral arrival order for the peripheral before E2 and it is not permitted that E1 and E2 are gathered into a single transaction. Otherwise, exactly one of following applies:

- E1 and E2 are gathered into a single transaction and appear as one Effect in Peripheral arrival order for the peripheral.
- E1 is inserted in the Peripheral arrival order for the peripheral before E2.
- E2 is inserted in the Peripheral arrival order for the peripheral before E1.

Note

Arm expects that, in most systems with early acknowledgments, those acknowledgments will come from a point at or after the point that establishes global visibility. This is expected in such systems to enable the acknowledgments to be used as part of the mechanisms to implement the ordering requirements of the Arm memory model.

## B2.4.2 Metadata Dependencies

| I YRYHC   | The execution of the following instructions create ordering relations for the purposes of the Arm memory model:                                                                                                                                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R TVHSL   | If FEAT_MTE is implemented, the execution of an IRG Xd,Xn,Xm instruction creates: • ADependency through registers and memory from the Register Read Effect of Xn to Register Write Effect of Xd. • If Allocation Tag Access is not prevented for the current Exception level, a Dependency through registers and memory from the Register Read Effect of Xmto Register Write Effect of Xd. |
| R MSWTM   | If FEAT_PAuth is implemented, the execution of a PACDA Xd,Xn instruction creates: • ADependency through registers and memory from the Register Read Effect of Xd to Register Write Effect of Xd. • If authentication using the APDAKey_EL1 key is enabled, a Dependency through registers and memory from the Register Read Effect of Xn to Register Write Effect of Xd.                   |
| R JMNSC   | If FEAT_FPAC is implemented, the execution of a PACDB Xd,Xn instruction creates: • ADependency through registers and memory from the Register Read Effect of Xd to Register Write Effect of Xd. • If authentication using the APDBKey_EL1 key is enabled, a Dependency through registers and memory from Register Read Effect of Xn to Register Write Effect of Xd.                        |
| R XYRJT   | If FEAT_FPAC is implemented, the execution of an AUTDA Xd,Xn instruction creates: • If authentication using the APDAKey_EL1 key is enabled, a Pick dependency through registers and memory from the Register Read Effect of Xn to Register Write Effect of Xd. • ADependency through registers and memory from the Register Read Effect of Xd to Register Write Effect of Xd.              |

Note

When FEAT\_XS is implemented, if E1 and E2 are to Device-nGnRE Memory or to Device-nGnRnE Memory and E1 and E2 are within the same Memory-mapped peripheral, but E1 and E2 use different XS attribute, the order of arrival at the endpoint is not defined by the architecture.

## Out-of-band-ordered-before

An Effect E1 is Out-of-band-ordered-before an Effect E2 if and only if all of the following apply:

- E1 is a Memory Effect.
- Any of the following applies:
- -E1 is DSB-ordered-before E3.
- -E1 is Instruction-fetch-barrier-ordered-before E3.
- There is an IMPLEMENTATION DEFINED instruction sequence beginning with E3 indirectly leading to the generation of E2.
- E2 is a Memory Effect.

If an Effect E1 is Out-of-band-ordered-before an Effect E2, then E1 is Ordered-before E2.

RSPBZX

If FEAT\_FPAC is implemented, the execution of an AUTDB Xd,Xn instruction creates:

- If authentication using the APDBKey\_EL1 key is enabled, a Pick dependency through registers and memory from the Register Read Effect of Xn to Register Write Effect of Xd.
- ADependency through registers and memory from the Register Read Effect of Xd to Register Write Effect of Xd.

## B2.4.3 Limited ordering regions

FEAT\_LOR introduces limited ordering regions (LORegions), which allow large systems to perform special load-acquire and store-release instructions that provide order between the memory accesses to a region of the PA map as observed by a set of observers.

LORegions are defined in the Non-secure physical address space. LORegions cannot be defined in the Secure, Realm, or Root physical address spaces.

This feature is supported in AArch64 state only.

## B2.4.3.1 Specification of the LORegions

The LORegions are defined in the Non-secure physical memory map using a set of LORegion descriptors. The number of LORegion descriptors is IMPLEMENTATION DEFINED, and can be discovered by reading the LORID\_EL1 register.

Each LORegion descriptor consists of:

- Atuple of the following values:
- -AStart Address.
- -An End Address.
- -An LORegion Number.
- Valid bit which indicates whether that LORegion descriptor is valid.

Amemory location lies within the LORegion identified by the LORegion Number if the PA lies between the Start Address and the End Address, inclusive. The Start Address must be defined to be aligned to 64KB and the End Address must be defined as the top byte of a 64KB block of memory.

It is permitted for multiple LORegion descriptors with non-overlapping address ranges to be configured with the same LORegion Number.

The LORegion descriptors are programmed using the LORSA\_EL1, LOREA\_EL1, LORN\_EL1, and LORC\_EL1 registers in the System register space. These registers describe only memory addresses in the Non-secure memory map. These registers are UNDEFINED if accessed when SCR\_EL3.NS == 0.

If a LoadLOAcquire or a StoreLORelease does not match with any LORegion, then:

- The LoadLOAcquire will behave as a Load-Acquire, and will be ordered in the same way with respect to all accesses, independent of their LORegions.
- The StoreLORelease will behave as a Store-Release, and will be ordered in the same way with respect to all accesses, independent of their LORegions.

Note

If no LORegions are implemented, then the LoadLOAcquire and StoreLORelease will therefore behave as a LoadAcquire and Store-Release.

## B2.4.4 SVE memory ordering relaxations

ICTNGV

The Arm memory model is relaxed for reads and writes generated by SVE load and store instructions.

RQLJPC

When two reads generated by SVE vector load instructions have an address dependency, the dependency does not contribute to the dependency-ordered-before relation.

| R YMBMZ   | When a pair of reads access the same location, and at least one of the reads is generated by an SVE load instruction, for a given observer, the hazard-ordered-before relation does not apply to the pair of reads.                                                                                                                                    |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R CJHWV   | When a single SVE vector store instruction generates multiple writes to the same location, the instruction ensures that these writes appear in the coherence order for that location, in order of increasing vector element number. No other ordering restrictions apply to memory effects generated by the same SVE store instruction.                |
| R LVXTJ   | If a single SVE load instruction generates multiple reads, the order in which the reads for different elements and registers appear is not architecturally defined.                                                                                                                                                                                    |
| R VMDYZ   | If an address dependency exists between two Read Memory and an SVE non-temporal vector load instruction generated the second read, then in the absence of any other barrier mechanism to achieve order, the memory accesses can be observed in any order by the other observers within the shareability domain of the memory addresses being accessed. |
| I CCWGN   | For any SVE load or store instruction that generates multiple single-copy atomic accesses to Normal or Device memory, there is no requirement for the memory system beyond the PE to be able to identify the single-copy atomic memory element access sizes.                                                                                           |

## B2.4.5 Streaming SVE mode memory ordering relaxations

RHBBTV

If a pair of memory reads access the same location, and at least one of the reads is generated by an Advanced SIMD&amp;FP load instruction, for a given observer, the hazard-ordered-before relation does not apply to the pair of reads when the PE is in Streaming SVE mode and FEAT\_SME\_FA64 is not implemented or not enabled at the current Exception level. See also:

- Streaming SVE mode.

## B2.4.6 Ordering rules for GCS

IQNKNL

If FEAT\_GCS is implemented, see Guarded Control Stack data accesses for relevant ordering rules.