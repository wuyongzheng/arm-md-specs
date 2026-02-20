## K1.2 AArch64 CONSTRAINED UNPREDICTABLE behaviors

It contains the following sections:

- Overview of the constraints on AArch64 UNPREDICTABLE behaviors.
- SBZ or SBO fields in A64 instructions.
- CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values.
- CONSTRAINED UNPREDICTABLE behavior due to inadequate context synchronization.
- Translation table base address alignment.
- The Performance Monitors Extension.
- The Activity Monitors Extension.
- Syndrome register handling for CONSTRAINED UNPREDICTABLE instructions treated as UNDEFINED.
- Out of range virtual address.
- Mapping of non-idempotent memory locations using the Normal memory type.
- Instruction fetches from Device memory.
- Programming the CSSELR\_EL1.{Level, InD, TnD} for a cache level that is not implemented.
- Crossing a page boundary with different memory types or Shareability attributes.
- Crossing a peripheral boundary with a Device access.
- CONSTRAINED UNPREDICTABLE behaviors with Load-Exclusive/Store-Exclusive pairs.
- CONSTRAINED UNPREDICTABLE behavior for A64 instructions.
- Out of range values of the Set/Way/Index fields in cache maintenance instructions.
- Reserved values in System and memory-mapped registers and translation table entries.
- CONSTRAINED UNPREDICTABLE behavior in Debug state.

## K1.2.1 Overview of the constraints on AArch64 UNPREDICTABLE behaviors

The term UNPREDICTABLE describes a number of cases where the architecture has a feature that software must not use. For execution in AArch64 state, the Armv8-A and later architectures specify a narrow range of permitted behaviors. This range is the range of CONSTRAINED UNPREDICTABLE behavior. All implementations that are compliant with the architecture must follow the CONSTRAINED UNPREDICTABLE behavior.

Note

Software designed to be compatible with the Armv8-A and later architectures must not rely on these CONSTRAINED UNPREDICTABLE cases being handled in any way other than those listed under the heading CONSTRAINED UNPREDICTABLE.

## K1.2.2 SBZ or SBO fields in A64 instructions

Some A64 instructions have (0) or (1) in the instruction decode to indicate Should-Be-Zero , SBZ, or Should-Be-One , SBO, as described in Fixed values in AArch64 instruction and System register descriptions. Except for specific cases identified in CONSTRAINED UNPREDICTABLE behaviors with Load-Exclusive/Store-Exclusive pairs, if the instruction bit pattern of an instruction is executed with these fields not having the should be values, one of the following must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction operates as if the bit had the should-be value.
- Any destination registers of the instruction become UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.3 CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values

The Arm architecture allows copies of control values or data values to be cached in a cache or TLB. This can lead to UNPREDICTABLE behavior if the cache or TLB has not been correctly invalidated following a change of the control or data values.

Unless explicitly stated otherwise, the behavior of the PE is consistent with one of:

- The old data or control value.
- The new data or control value.
- An amalgamation of the old and new data or control values.

In an implementation that includes FEAT\_TTCNP, this CONSTRAINED UNPREDICTABLE case can arise from misprogramming when setting TTBR.CnP to 1, as identified in the descriptions of the TTBR.CnP field. In this case, for a particular TTBR, the behavior of the PE is consistent with one of:

- The value of the translation table entry pointed to by that TTBR on one of the PEs within the Inner Shareable domain for which both the value of TTBR.CnP is 1 and the other conditions for sharing translation table entries pointed to by that TTBR are met.
- An amalgamation of the values of the translation table entries pointed to by that TTBR on two or more of the PEs within the Inner Shareable domain for which both the value of TTBR.CnP is 1 and the other conditions for sharing translation table entries pointed to by that TTBR are met.

Note

If the Effective value of a control or data value that determines the behavior of the PE results from the amalgamation of two or more values, then that Effective value must not generate a privilege violation. So, for example:

- Where the CONSTRAINED UNPREDICTABLE behavior occurs because inadequate invalidation of the TLB causes multiple hits in the TLB, the failure to invalidate the TLB by software executing at a given Exception level and Security state must not make it possible to access regions of memory with permissions or attributes that could not be accessed at that Exception level and Security state.
- Where the CONSTRAINED UNPREDICTABLE behavior occurs because of a programming error, on one or more PEs in the Inner Shareable domain, when using a TTBR.CnP value of 1 to share translation table entries, the misprogramming must not make it possible to access regions of memory with permissions or attributes that could not be accessed at the Exception level of that TTBR and the Security state corresponding to the translation table entries being shared.

Alternatively to this CONSTRAINED UNPREDICTABLE behavior, an implementation detecting multiple hits in a TLB might generate an exception, reporting the exception using the TLB conflict fault code, see TLB conflict abort.

The choice between the behaviors might, in some implementations, vary for each use of a control or data value.

## K1.2.4 CONSTRAINED UNPREDICTABLE behavior due to inadequate context synchronization

The Arm architecture requires that changes to System registers must be synchronized before they take effect. This can lead to UNPREDICTABLE behavior if the synchronization has not been performed.

In these cases, the behavior of the PE is consistent with the unsynchronized control value being either the old value or the new value.

Where multiple control values are updated but not yet synchronized, each control value might independently be the old value or the new value.

In addition, where the unsynchronized control value applies to different areas of functionality, or what an implementation has constructed as different areas of functionality, those areas might independently treat the control value as being either the old value or the new value.

The choice between these behaviors might, in some implementations, vary for each use of a control value.

## K1.2.5 Translation table base address alignment

In the translation table base registers TTBR0\_EL1, TTBR1\_EL1, TTBR0\_EL2, VTTBR\_EL2, and TTBR0\_EL3, register bits[48: x ] hold the translation table base address, where x depends on the translation table granule size and the size of the addressed translation table, as described in Translation granules. Register bits[( x -1):0], unless redefined for another purpose, correspond to bits[( x -1):0] of the translation table base address and therefore are RES0.

## Note

- When FEAT\_LPA is implemented and the 64KB granule size is used, register bits[5:2] are redefined to hold bits[51:48] of the translation table base address.
- When FEAT\_TTCNP is implemented register bit[0] is redefined as the CnP bit.

For these registers, if one or more RES0 bits in register bits [(x-1):0] does not have a value of 0, this can result in a misaligned translation table base address. In this case, one of the following behaviors must occur:

- The field that is defined to be RES0 is treated as if all the bits had a value of 0:
- -The value read back might be the value written or it might be zero.
- The calculation of an address for a translation table walk using those registers might be corrupted in those bits that are nonzero.

For more information, see the appropriate TTBR.BADDR field description.

## K1.2.6 The Performance Monitors Extension

IGTRGP

RTVKJV

The following subsections describe CONSTRAINED UNPREDICTABLE behaviors when accessing the Performance Monitors Extension in AArch64 state:

- CONSTRAINED UNPREDICTABLE accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0.
- CONSTRAINED UNPREDICTABLE accesses to PMEVCNTR&lt;n&gt;\_EL0 and PMEVTYPER&lt;n&gt;\_EL0.
- CONSTRAINED UNPREDICTABLE behavior caused by MDCR\_EL2.HPMN.

## K1.2.6.1 CONSTRAINED UNPREDICTABLE accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0

When FEAT\_FGT is not implemented, if the PE is using AArch64, and if PMSELR\_EL0.SEL is greater than the number of event counters accessible at the current Exception level, then accesses to PMXEVTYPER\_EL0 and PMXEVCNTR\_EL0 can cause CONSTRAINED UNPREDICTABLE behavior. This occurs when any of the following is true:

- If PMSELR\_EL0.SEL is not equal to 31, and PMSELR\_EL0.SEL is greater than or equal to PMCR\_EL0.N, and the PE is executing in EL2 or EL3.
- If FEAT\_SEL2 is disabled or is not implemented, PMSELR\_EL0.SEL is not 31, and PMSELR\_EL0.SEL is greater than or equal to PMCR\_EL0.N, and the PE is executing in Secure EL1 or Secure EL0.
- If PMSELR\_EL0.SEL is not 31, and PMSELR\_EL0.SEL is greater than or equal to MDCR\_EL2.HPMN, and the PE is executing in EL0 or EL1.

In these cases, the PE does one of the following:

- Accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0 are UNDEFINED.
- Accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0 behave as RAZ/WI.
- Accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0 execute as NOPs.
- Accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0 behave as if PMSELR\_EL0.SEL contains an UNKNOWN value that is less than the number of counters accessible at the current Exception level and Security state.
- Accesses to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0 behave as if PMSELR\_EL0.SEL is 31.
- If EL2 is implemented and enabled in the current Security state, and PMSELR\_EL0.SEL is less than the number of accessible event counters but greater than or equal to the number of accessible counters at this Exception level, access to PMXEVTYPER\_EL0 or PMXEVCNTR\_EL0 from EL1 or a permitted access from EL0 is trapped to EL2.

RCJXGK

IMBTNR

RQRHGP

RLGBTC

Note

If EL2 is implemented and enabled in the current Security state, MDCR\_EL2.HPMN identifies the number of accessible counters at EL0 or EL1. Otherwise, the number of accessible counters is the number of accessible event counters. Accesses from EL0 to PMXEVCNTR\_EL0 are permitted when:

- EL1 is using AArch32 and the values of PMUSERENR.{ER, EN} are both 1.
- EL1 is using AArch64 and the values of PMUSERENR\_EL0.{ER, EN} are both 1.

Accesses from EL0 to PMXEVTYPER\_EL0 are permitted when:

- EL1 is using AArch32 and the value of PMUSERENR.EN is 1.
- EL1 is using AArch64 and the value of PMUSERENR\_EL0.EN is 1.

When FEAT\_FGT is not implemented, if the PE is using AArch64, and if PMSELR\_EL0.SEL is equal to 31, the PE does one of the following:

- Accesses to PMXEVCNTR\_EL0 are UNDEFINED.
- Accesses to PMXEVCNTR\_EL0 behave as RAZ/WI.
- Accesses to PMXEVCNTR\_EL0 execute as NOPs.
- Accesses to PMXEVCNTR\_EL0 behave as if PMSELR\_EL0.SEL contains an unknown value that is less than the number of counters accessible at the current Exception level and Security state.

## K1.2.6.2 CONSTRAINED UNPREDICTABLE accesses to PMEVCNTR&lt;n&gt;\_EL0 and PMEVTYPER&lt;n&gt;\_EL0

If FEAT\_FGT is implemented, and EL2 is implemented in the current Security state, and EL1 is using AArch64, permitted access to PMEVCNTR&lt;n&gt;\_EL0 and PMEVTYPER&lt;n&gt;\_EL0 are not CONSTRAINED UNPREDICTABLE.

When FEAT\_FGT is not implemented, if the PE is using AArch64, and if &lt;n&gt; is greater than the number of event counters available in the current Exception level and state, reads and writes of PMEVCNTR&lt;n&gt;\_EL0 and

PMEVTYPER&lt;n&gt;\_EL0 are CONSTRAINED UNPREDICTABLE, and the PE does one of the following:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.
- If EL2 is implemented and enabled in the current Security state, for an access to PMEVCNTR&lt;n&gt;\_EL0 or PMEVTYPER&lt;n&gt;\_EL0 from EL1 or a permitted access from EL0, if the counter is implemented but not accessible at the current Exception level, the register access is trapped to EL2.

Accesses from EL0 to PMEVCNTR&lt;n&gt;\_EL0 are permitted when:

- -EL1 is using AArch32 and the value of PMUSERENR.{ER, EN} are both 1.
- -EL1 is using AArch64 and the value of PMUSERENR\_EL0.{ER, EN} are both 1.

Accesses from EL0 to PMEVTYPER&lt;n&gt;\_EL0 are permitted when:

- -EL1 is using AArch32 and the value of PMUSERENR.EN is 1.
- -EL1 is using AArch64 and the value of PMUSERENR\_EL0.EN is 1.

## K1.2.6.3 CONSTRAINED UNPREDICTABLE behavior caused by MDCR\_EL2.HPMN

If EL2 is implemented, NUM\_PMU\_COUNTERS is nonzero, and any of the following is true:

- FEAT\_HPMN0 is not implemented and MDCR\_EL2.HPMN is 0.
- FEAT\_PMUv3\_EXTPMN is not implemented and MDCR\_EL2.HPMN is greater than NUM\_PMU\_COUNTERS.

Then the following CONSTRAINED UNPREDICTABLE behaviors apply:

- The value returned by a direct read of MDCR\_EL2.HPMN is UNKNOWN.
- Either:
- -An UNKNOWN number of counters are reserved for EL2 use. That is, the PE behaves as if MDCR\_EL2.HPMN is an UNKNOWN nonzero value less than or equal to NUM\_PMU\_COUNTERS.
- -All counters are reserved for EL2 and EL3 use, meaning no counters are accessible from EL1 and EL0.

RKJLJH

## K1.2.6.4 CONSTRAINED UNPREDICTABLE behavior caused by PMCCR.EPMN

If FEAT\_PMUv3\_EXTPMN is implemented and PMCCR.EPMN is greater-than NUM\_PMU\_COUNTERS, then all of the following apply:

- External reads of PMCCR.EPMN returns an UNKNOWN value that is less than or equal to 31.
- For the purposes of indirect reads of PMCCR.EPMN as a result of the following reads, the Effective value of PMCCR.EPMN is an UNKNOWN value that is less than or equal to 31:
- -Direct reads of PMCR\_EL0.N or PMCR.N.
- -Direct reads of MDCR\_EL2.HPMN.
- -External reads of PMCFGR.N.
- -If FEAT\_PMUv3\_ICNTR is implemented, external reads of PMCGCR0.CG0NC.
- For all other purposes, the Effective value of PMCCR.EPMN is an UNKNOWN value that is less than or equal to NUM\_PMU\_COUNTERS.

## K1.2.7 The Activity Monitors Extension

If &lt;n&gt; is greater than the number of architected activity monitor event counters, reads and writes of AMEVCNTR0&lt;n&gt;\_EL0 and AMEVTYPER0&lt;n&gt;\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.

Note

AMCGCR\_EL0.CG0NC identifies the number of architected activity monitor event counters.

If &lt;n&gt; is greater than the number of auxiliary activity monitor event counters, reads and writes of AMEVCNTR1&lt;n&gt;\_EL0and AMEVTYPER1&lt;n&gt;\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.

Note

AMCGCR\_EL0.CG1NC identifies the number of auxiliary activity monitor event counters.

If the number of auxiliary activity monitor event counters that are implemented is zero, reads and writes of AMCNTENCLR1\_EL0 and AMCNTENSET0\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.

Note

The number of auxiliary activity monitor event counters that are implemented is zero exactly when AMCFGR\_EL0.NCG is 0b0000 .

## K1.2.8 Syndrome register handling for CONSTRAINED UNPREDICTABLE instructions treated as UNDEFINED

## K1.2.9 Out of range virtual address

When a CONSTRAINED UNPREDICTABLE instruction is treated as UNDEFINED, ESR\_ELx is UNKNOWN.

Note

The value written to ESR\_ELx must be consistent with a value that could be created as the result of an exception from the same Exception level that generated the exception, but was the result of a situation that is not CONSTRAINED UNPREDICTABLE at that Exception level. This is to avoid a possible privilege violation.

If the PE executes a load or store instruction with tagged addressing disabled in the current translation regime, and where the computed virtual address, total access size, and alignment mean that it accesses the bytes at 0xFFFF\_FFFF\_FFFF\_FFFF and 0x0000\_0000\_0000\_0000 , then the bytes that appear to be from 0x0000\_0000\_0000\_0000 onwards are accessed at an UNKNOWN address. It is permitted for the UNKNOWN address used to be a fixed value such that it always generates an MMU fault.

If the PE executes a load or store instruction with tagged addressing enabled in the current translation regime, and where the computed address, total access size, and alignment mean that it accesses the bytes at 0xFFFF\_FFFF\_FFFF\_FFFF and 0x0000\_0000\_0000\_0000 , then the bytes that appear to be from 0x0000\_0000\_0000\_0000 onwards are accessed at an UNKNOWN address and the tags associated with address also become UNKNOWN. It is permitted for the UNKNOWN address used to be a fixed value such that it always generates an MMU fault.

Note

Because of Program Counter alignment constraints, it is impossible for a PE to fetch an A64 instruction that includes both the byte at virtual address 0xFFFF\_FFFF\_FFFF\_FFFF and the byte at virtual address 0x0000\_0000\_0000\_0000 .

## K1.2.10 Mapping of non-idempotent memory locations using the Normal memory type

If non-idempotent memory locations are mapped using the Normal memory type, the state of the non-idempotent memory location may become corrupted in following circumstances:

- Speculative read accesses may cause accesses to the non-idempotent memory locations that would not occur as part of a simple sequential execution.
- Writes to non-idempotent memory locations might be merged or split. In this case, the number and size of writes seen by the memory location might not be the number and size that occur as part of a simple sequential execution.

## K1.2.11 Instruction fetches from Device memory

Instruction fetches from Device memory are CONSTRAINED UNPREDICTABLE.

If a location in memory has the Device attribute and is not marked as execute-never, then an implementation might perform speculative instruction accesses to this memory location at times when address translation is enabled.

For an instruction fetch from a memory location with the Device attribute that is not marked as execute-never for the current Exception level, an implementation can either:

- Treat the instruction fetch as if it were to a memory location with the Normal, Non-cacheable attribute.
- Take a Permission fault.

## K1.2.12 Programming the CSSELR\_EL1.{Level, InD, TnD} for a cache level that is not implemented

If the CSSELR\_EL1.{Level, InD, TnD} is programmed to a cache level that is not implemented, then a read of CSSELR\_EL1 returns an UNKNOWN value in CSSELR\_EL1.{Level, InD, TnD}.

If CSSELR\_EL1.{Level, InD, TnD} is programmed to a cache level that is not implemented, then on a read of CCSIDR\_EL1 an implementation must perform one of the following behaviors:

- The CCSIDR\_EL1 read is treated as a NOP.
- The CCSIDR\_EL1 read is UNDEFINED.
- The CCSIDR\_EL1 read returns an UNKNOWN value.

When FEAT\_CCIDX is implemented, CCSIDR2\_EL1 is implemented. If CSSELR\_EL1.{Level, InD, TnD} is programmed to a cache level that is not implemented, then on a read of CCSIDR2\_EL1 an implementation must perform one of the following behaviors:

- The CCSIDR2\_EL1 read is treated as a NOP.
- The CCSIDR2\_EL1 read is UNDEFINED.
- The CCSIDR2\_EL1 read returns an UNKNOWN value.

## K1.2.13 Crossing a page boundary with different memory types or Shareability attributes

If a single load or store instruction generates multiple memory accesses, such that the total set of accesses crosses a page boundary to a memory location that has a different memory type, Normal or Device, or Shareability attribute results in CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation must perform one of the following behaviors:

- Each memory access generated by the instruction uses the memory type and Shareability attribute associated with its own address.
- The instruction generates an Alignment fault caused by the memory type.

For the EL1&amp;0 translation regime, when EL2 is enabled in the current Security state:

- -If the stage 1 translation generated the mismatch, the resulting exception is taken to EL1.
- -If the stage 2 translation generated the mismatch, the resulting exception is taken to EL2.
- -If both stages of translation generate the mismatch, the exception can be taken to either EL1 or EL2.
- The instruction executes as a NOP.

Memory accesses from a Memory Copy and Memory Set CPY* or Memory Copy and Memory Set SET* instruction that cross a page boundary to a memory location that has a different memory type or Shareability attribute results in CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation must perform one of the following behaviors:

- Each memory access generated by the instruction uses the memory type and Shareability attribute associated with its own address.
- The instruction generates an Alignment fault caused by the memory type. For the EL1&amp;0 translation regime, when EL2 is enabled in the current Security state:
- -If the stage 1 translation generated the mismatch, the resulting exception is taken to EL1.
- -If the stage 2 translation generated the mismatch, the resulting exception is taken to EL2.
- -If both stages of translation generate the mismatch, the exception can be taken to either EL1 or EL2.

## K1.2.14 Crossing a peripheral boundary with a Device access

Performing memory accesses from one load or store instruction to Device memory that crosses a boundary corresponding to the smallest translation granule size of the implementation causes CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation performs one of the following behaviors:

- All memory accesses generated by the instruction are performed as if the boundary has no effect on the memory accesses.
- All memory accesses generated by the instruction are performed as if the boundary has no effect on the memory accesses except that there is no guarantee of ordering between memory accesses.
- The instruction generates an alignment fault caused by the memory type.

For the EL1&amp;0 translation regime, when EL2 is enabled in the current Security state:

- -If the stage 1 translation causes the boundary to be crossed, the resulting exception is taken to EL1.
- -If the stage 2 translation causes the boundary to be crossed, the resulting exception is taken to EL2.
- -If both stages of translation cause the boundary to be crossed, the resulting exception can be taken to either EL1 or EL2.
- The instruction executes as a NOP.

Note

The boundary referred to is between two Device memory regions that are both:

- Of the size of the smallest implemented translation granule.

- Aligned to the size of the smallest implemented translation granule.

## K1.2.15 CONSTRAINED UNPREDICTABLE behaviors with SVE memory accesses

The CONSTRAINED UNPREDICTABLE behaviors that are associated with memory accesses due to loads and stores also apply to SVE vector load and store instructions. The CONSTRAINED UNPREDICTABLE behaviors are described in Crossing a page boundary with different memory types or Shareability attributes and Crossing a peripheral boundary with a Device access.

The CONSTRAINED UNPREDICTABLE behaviors apply to the following SVE memory accesses:

- When an SVE unpredicated contiguous load or store instruction accesses an address range that crosses a boundary between memory types, Shareability attributes, or peripherals.
- When an SVE predicated contiguous load or store instruction performs memory accesses that are associated with Active elements on both sides of a boundary between different memory types, Shareability attributes, or peripherals.
- When an SVE predicated non-contiguous load or store instruction performs a memory access that is associated with an Active element that crosses a boundary between memory types, Shareability attributes, or peripherals.

Memory addresses that are associated with Inactive elements cannot trigger CONSTRAINED UNPREDICTABLE behaviors.

If SVE vector loads and stores trigger a CONSTRAINED UNPREDICTABLE behavior that then generates an alignment fault, the fault is handled in the same as any other synchronous memory fault caused by an SVE load or store instruction.

## K1.2.16 CONSTRAINED UNPREDICTABLE behaviors with Load-Exclusive/Store-Exclusive pairs

Load-Exclusive and Store-Exclusive instruction usage restrictions defines a Load-Exclusive/Store-Exclusive pair, and identifies various CONSTRAINED UNPREDICTABLE behaviors associated with using Load-Exclusive/Store-Exclusive pairs. In summary, these cases are:

- The target virtual address of a StoreExcl instruction is different from the virtual address of the preceding LoadExcl instruction in the same thread of execution.
- The transaction size of a StoreExcl instruction is different from the transaction size of the preceding LoadExcl instruction in the same thread of execution.
- The StoreExcl instruction accesses a different number of registers than the preceding LoadExcl instruction in the same thread of execution.
- The memory attributes for a StoreExcl instruction are different from the memory attributes for the preceding LoadExcl instruction in the same thread of execution, either:
- -Because the translation of the accessed address changes between the LoadExcl instruction and the StoreExcl instruction.
- -Because the LoadExcl instruction and the StoreExcl instruction use different virtual addresses, with different attributes, that point to the same physical address.

In addition, the effect of a data or unified cache invalidate, clean, or clean and invalidate instruction on a local or global Exclusives monitor that is in the Exclusive Access state is CONSTRAINED UNPREDICTABLE.

See the descriptions in Load-Exclusive and Store-Exclusive instruction usage restrictions for the permitted behavior in each of these cases, and any constraints that might apply to whether the case is CONSTRAINED UNPREDICTABLE.

## K1.2.17 CONSTRAINED UNPREDICTABLE behavior for A64 instructions

This section lists the CONSTRAINED UNPREDICTABLE behavior for the different A64 instructions listed in A64 Base Instruction Descriptions and A64 Advanced SIMD and Floating-point Instruction Descriptions.

## K1.2.17.1 Memory Copy and Memory Set CPY*

For a list of these instructions, see Memory Copy and Memory Set instructions.

## K1.2.17.1.1 CONSTRAINED UNPREDICTABLE behavior

If s == n || s == d || n == d || d == 31 || s == 31 || n == 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.2 LD64B

For a description of this instruction and encoding, see LD64B.

## K1.2.17.2.1 CONSTRAINED UNPREDICTABLE behavior

If a memory location does not support this instruction, then one of the following behaviors must occur:

- Astage 1 Data Abort, reported using the DFSC code of 110101, is generated.
- The instruction performs the memory accesses, but the accesses are not single-copy atomic above the byte level.

## K1.2.17.3 LDAXP

For a description of this instruction and the encoding, see LDAXP.

## K1.2.17.3.1 CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the transfer register is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.4 LDNP

For a description of this instruction and the encoding, see LDNP.

## K1.2.17.4.1 CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the transfer register is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.5 LDNP (SIMD&amp;FP)

For a description of this instruction and the encoding, see LDNP (SIMD&amp;FP).

## K1.2.17.5.1 CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the transfer register is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.6 LDP and LDIAPP

For a description of these instructions and the encoding, see LDP and LDIAPP.

## K1.2.17.6.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and (t == n || t2 == n) &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If t == t2, then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs all of the loads using the specified addressing mode, and the transfer register is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.7 LDP (SIMD&amp;FP)

For a description of this instruction and the encoding, see LDP (SIMD&amp;FP).

## K1.2.17.7.1 CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the transfer register is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.8 LDPSW

For a description of this instruction and the encoding, see LDPSW.

## K1.2.17.8.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and (t == n || t2 == n) &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs all of the loads using the specified addressing mode, and the register loaded is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.9 LDR (immediate)

For a description of this instruction and the encoding, see LDR (immediate).

## K1.2.17.9.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.10 LDRB (immediate)

For a description of this instruction and the encoding, see LDRB (immediate).

## K1.2.17.10.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.11 LDRH (immediate)

For a description of this instruction and the encoding, see LDRH (immediate).

## K1.2.17.11.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.12 LDRSB (immediate)

For a description of this instruction and the encoding, see LDRSB (immediate).

## K1.2.17.12.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.13 LDRSH (immediate)

For a description of this instruction and the encoding, see LDRSH (immediate).

## K1.2.17.13.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.14 LDRSW (immediate)

For a description of this instruction and the encoding, see LDRSW (immediate).

## K1.2.17.14.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the load using the specified addressing mode, and the base register is set to an UNKNOWN value. In addition, if an exception occurs during such an instruction, the base register might be corrupted so that the instruction cannot be repeated.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.15 LDXP

For a description of this instruction and the encoding, see LDXP.

## K1.2.17.15.1 CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a load using the specified addressing mode, and the transfer register is set to an UNKNOWN value.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.16 Memory Copy and Memory Set SET*

For a list of these instructions, see Memory Copy and Memory Set instructions.

## K1.2.17.16.1 CONSTRAINED UNPREDICTABLE behavior

If s == n || s == d || n == d || d == 31 || n == 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.17 ST64B

For a description of this instruction and encoding, see ST64B.

## K1.2.17.17.1 CONSTRAINED UNPREDICTABLE behavior

If a memory location does not support this instruction, then one of the following behaviors must occur:

- Astage 1 Data Abort, reported using the DFSC code of 110101, is generated.
- The instruction performs the memory accesses, but the accesses are not single-copy atomic above the byte level.

## K1.2.17.18 STP and STILP

For a description of these instructions and the encoding, see STP and STILP.

## K1.2.17.18.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and (t == n || t2 == n) &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a store using the specified addressing mode but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.19 STLXP

For a description of this instruction and the encoding, see STLXP.

## K1.2.17.19.1 CONSTRAINED UNPREDICTABLE behavior

If s == t || (s == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.

- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.20 STLXR

For a description of this instruction and the encoding, see STLXR.

## K1.2.17.20.1 CONSTRAINED UNPREDICTABLE behavior

If s == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.21 STLXRB

For a description of this instruction and the encoding, see STLXRB.

## K1.2.17.21.1 CONSTRAINED UNPREDICTABLE behavior

If s == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.22 STLXRH

For a description of this instruction and the encoding, see STLXRH.

## K1.2.17.22.1 CONSTRAINED UNPREDICTABLE behavior

If s == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.23 STR (immediate)

For a description of this instruction and the encoding, see STR (immediate).

## K1.2.17.23.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a store using the specified addressing mode but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.24 STRB (immediate)

For a description of this instruction and the encoding, see STRB (immediate).

## K1.2.17.24.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a store using the specified addressing mode but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.25 STRH (immediate)

For a description of this instruction and the encoding, see STRH (immediate).

## K1.2.17.25.1 CONSTRAINED UNPREDICTABLE behavior

If the instruction encoding specifies pre-indexed addressing or post-indexed addressing, and n == t &amp;&amp; n != 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs a store using the specified addressing mode but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

Note

Pre-indexed addressing and post-indexed addressing imply writeback.

## K1.2.17.26 STXP

For a description of this instruction and the encoding, see STXP.

## K1.2.17.26.1 CONSTRAINED UNPREDICTABLE behavior

If s == t || (s == t2) , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.27 STXR

For a description of this instruction and the encoding, see STXR.

## K1.2.17.27.1 CONSTRAINED UNPREDICTABLE behavior

If s == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.28 STXRB

For a description of this instruction and the encoding, see STXRB.

## K1.2.17.28.1 CONSTRAINED UNPREDICTABLE behavior

If s == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.17.29 STXRH

For a description of this instruction and the encoding, see STXRH.

## K1.2.17.29.1 CONSTRAINED UNPREDICTABLE behavior

If s == t , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to the specified address, but the value stored is UNKNOWN.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

If s == n &amp;&amp; n != 31 then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction performs the store to an UNKNOWN address.
- For execution at EL0 or EL1, when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TIDCP is 1, the instruction is trapped to EL2 with EC syndrome value 0x0 . When FEAT\_TIDCP1 is implemented, for execution at EL0, this also applies when SCTLR\_EL1.TIDCP or SCTLR\_EL2.TIDCP is 1.

## K1.2.18 Out of range values of the Set/Way/Index fields in cache maintenance instructions

In the cache maintenance by set/way instructions DC CISW, DC CSW, and DC ISW, if any set/way/index argument is larger than the value supported by the implementation, then the behavior is CONSTRAINED UNPREDICTABLE and one of the following occurs:

- The instruction is UNDEFINED.

- The instruction performs cache maintenance on one of:

- No cache lines.

- Asingle arbitrary cache line.

- Multiple arbitrary cache lines.

Note

This CONSTRAINED UNPREDICTABLE behavior applies, also, to the AArch32 cache maintenance by set/way instructions DCCISW, DCCSW, and DCISW.

## K1.2.19 Reserved values in System and memory-mapped registers and translation table entries

Unless otherwise stated in this manual, all unallocated or reserved values of fields with allocated values within AArch64 System registers, memory-mapped registers, and translation table entries behave in one of the following ways:

- The unallocated value maps onto any of the allocated values, but otherwise does not cause CONSTRAINED UNPREDICTABLE behavior.
- The unallocated value causes effects that could be achieved by a combination of more than one of the allocated values.
- The unallocated value causes the field to have no functional effect.

Note

These constraints are identical to those for the equivalent AArch32 definitions, as given in Reserved values in System and memory-mapped registers and translation table entries.

Unless otherwise stated, when a direct write of a System register or memory-mapped register writes an unallocated value to a field, if that value is unallocated in all contexts then a subsequent read of the field returns an UNKNOWN value.

## K1.2.20 CONSTRAINED UNPREDICTABLE behavior in Debug state

Behavior in Debug state of this manual describes the CONSTRAINED UNPREDICTABLE behaviors that are specifically associated with Debug state.

## Recommendations for Reporting Memory Attributes on

## Appendix K2 an Interconnect

This appendix describes the Arm recommendations for reporting the memory attributes that are assigned by the PE. It contains the following section:

- Arm recommendations for reporting memory attributes on an interconnect.