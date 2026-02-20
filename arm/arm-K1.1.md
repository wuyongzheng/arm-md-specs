## K1.1 AArch32 CONSTRAINED UNPREDICTABLE behaviors

From the introduction of Armv8, the architecture defines architecturally required constraints on many behaviors that are UNPREDICTABLE in Armv7. The following sections define those constraints:

- Overview of the constraints on Armv7 UNPREDICTABLE behaviors.
- Using R13 by instruction.
- Using R15 by instruction.
- Branching into an IT block.
- Branching to an unaligned PC.
- Loads and Stores to unaligned locations.
- CONSTRAINED UNPREDICTABLE behavior associated with IT instructions and PSTATE.IT.
- Unallocated System register access instructions.
- SBZ or SBO fields T32 and A32 in instructions.
- UNPREDICTABLE cases in immediate constants in T32 data-processing instructions.
- UNPREDICTABLE cases in immediate constants in Advanced SIMD instructions.
- CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.
- CONSTRAINED UNPREDICTABLE behavior due to inadequate context synchronization
- Translation Table Base Address alignment.
- Handling of System register control fields for Advanced SIMD and floating-point operation.
- Mapping of non-idempotent memory locations using the Normal memory type.
- The Performance Monitors Extension.

•

The Activity Monitors Extension.

- Syndrome register handling for CONSTRAINED UNPREDICTABLE instructions treated as UNDEFINED.
- Out of range VA.
- Instruction fetches from Device memory.
- Multi-access instructions that load the PC from Device memory.
- Programming CSSELR.Level for a cache level that is not implemented.
- Crossing a page boundary with different memory types or Shareability attributes.
- Crossing a 4KB boundary with a Device access.
- UNPREDICTABLE behaviors with Load-Exclusive/Store-Exclusive pairs.
- CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings.
- Out of range values of the Set/Way/Index fields in cache maintenance instructions.
- CONSTRAINED UNPREDICTABLE behavior for T32 and A32 System instructions in the base instruction set.
- CONSTRAINED UNPREDICTABLE behavior, T32 and A32 Advanced SIMD and floating-point instructions.
- CONSTRAINED UNPREDICTABLE behaviors associated with the VTCR.
- CONSTRAINED UNPREDICTABLE behavior of EL2 features.
- Reserved values in System and memory-mapped registers and translation table entries.
- CONSTRAINED UNPREDICTABLE behavior in Debug state.

## K1.1.1 Overview of the constraints on Armv7 UNPREDICTABLE behaviors

The term UNPREDICTABLE describes a number of cases where the architecture has a feature that software must not use. For execution in AArch32 state, where previous versions of the architecture define behavior as UNPREDICTABLE, from the introduction of Armv8-A the architecture specifies a narrow range of permitted behaviors. This range is the range of CONSTRAINED UNPREDICTABLE behavior. All implementations that are compliant with the architecture must follow the CONSTRAINED UNPREDICTABLE behavior.

Note

Software designed to be compatible with the Armv8-A and later architectures must not rely on these CONSTRAINED UNPREDICTABLE cases.

## K1.1.2 Using R13 by instruction

In prior versions of the architecture, the use of R13 by instruction as a named register specifier was described as UNPREDICTABLE in the pseudocode. From the introduction of the Armv8-A architecture, the use of R13 as a named register specifier is not UNPREDICTABLE, unless this is specifically stated, and R13 can be used in the regular form. Bits[1:0] of R13 are not treated as SBZP in the Armv7 architecture or RES0 in the Armv8 and later architectures, but can hold any values programmed into them.

## K1.1.3 Using R15 by instruction

All uses of R15 by instruction as a named register specifier for a source register that are described as CONSTRAINED UNPREDICTABLE in the pseudocode or in other places in this Manual must do one of the following:

- Cause the instruction to be treated as UNDEFINED.
- Cause the instruction to execute as a NOP.
- Read the Program Counter with the standard offset that applies for the current instruction set.
- Read the Program Counter with the standard offset that applies for the current instruction set with alignment to a word boundary.
- Read 0. This is Arm preferred behavior.
- Read or return an UNKNOWN value for the source register specified as R15.

All uses of R15 as a named register specifier for a destination register that are described as CONSTRAINED UNPREDICTABLE in the pseudocode or in other places in this reference manual must do one of the following:

- Cause the instruction to be treated as UNDEFINED.
- Cause the instruction to execute as a NOP.
- Ignore the write.
- Branch to an UNKNOWN location in either A32 or T32 state.

Instructions that are CONSTRAINED UNPREDICTABLE when the base register is R15 and the instruction specifies a writeback of the base register, are treated as having R15 as both a source register and a destination register.

For instructions that have two destination registers, for example LDRD , MRRC , and many of the multiply instructions, if Rt, Rt2, RdLo, or RdHi is R15, then the other destination register of the pair is UNKNOWN if the CONSTRAINED UNPREDICTABLE behavior for the write to R15 is either to ignore the write or to branch to an UNKNOWN location.

For instructions that affect any or all of PSTATE.{N, Z, C, V}, PSTATE.Q, and PSTATE.GE when the register specifier is not R15, any flags affected by an instruction that is CONSTRAINED UNPREDICTABLE when the register specifier is R15 become UNKNOWN.

In addition, for MRC instructions that use R15 as the destination register descriptor, and therefore target APSR\_nzcv where these are described as being CONSTRAINED UNPREDICTABLE, PSTATE.{N, Z, C, V} becomes UNKNOWN.

## K1.1.4 Branching into an IT block

Branching into an IT block leads to CONSTRAINED UNPREDICTABLE behavior. Execution starts from the address determined by the branch, but each instruction in the IT block is:

- Executed as if it were not in an IT block. This means that it is executed unconditionally.
- Executed as if it had passed its Condition code check within an IT block.
- Executed as a NOP. That is, it behaves as if it had failed the Condition code check.

## K1.1.5 Branching to an unaligned PC

In A32 state, when branching to an address that is not word-aligned and is defined to be CONSTRAINED UNPREDICTABLE, one of the following behaviors must occur:

- The unaligned location is forced to be aligned.

- The unaligned address generates a Prefetch Abort on the first instruction using the unaligned PC value. If that instruction is executed at EL0 and either of the following applies, the exception is taken to EL2:
- -EL2 is using AArch32 and the value of HCR.TGE is 1.
- -EL2 is using AArch64 and the value of HCR\_EL2.TGE is 1.

If the instruction is executed at EL0 when the applicable TGE bit is 0 the exception is taken to EL1.

If the instruction is executed at an Exception level that is higher than EL0 the exception is taken to the Exception level at which the instruction was executed.

In all cases, the exception is generated only if the first instruction using the unaligned PC value is architecturally executed.

If the exception that results from a branch to an unaligned PC value:

- Is taken to an Exception level that is using AArch64, it is reported as a PC alignment fault exception, see ISS encoding for an exception from an Illegal Execution state, or a PC or SP alignment fault.
- Is taken to an Exception level that is using AArch32, it is reported as a Prefetch Abort exception, see Prefetch Abort exception reporting a PC alignment fault exception.

Note

Because bit[0] is used for interworking, it is impossible to specify a branch to A32 state when the bottom bit of the target address is 1. Therefore the bottom bit of IFAR, HIFAR, or FAR\_ELx is 0 for all these cases.

## K1.1.6 Loads and Stores to unaligned locations

Some unaligned loads and stores in the Armv8-A and later architectures are described as CONSTRAINED UNPREDICTABLE to do one of the following:

- Take an alignment fault.
- Perform the specified load or store to the unaligned memory location.

## K1.1.7 CONSTRAINED UNPREDICTABLE behavior associated with IT instructions and PSTATE.IT

Anumber of instructions in the architecture are described as being CONSTRAINED UNPREDICTABLE either:

- Anywhere within an IT block.
- As an instruction within an IT block, other than the last instruction within an IT block.

Unless otherwise stated in this manual, when these instructions are committed for execution, one of the following occurs:

- An UNDEFINED exception results.
- The instructions are executed as if they had passed the Condition code check.
- The instructions execute as NOPs. This means that they behave as if they had failed the Condition code check.

The behavior might in some implementations vary from instruction to instruction, or between different instances of the same instruction.

Many instructions that are CONSTRAINED UNPREDICTABLE in an IT block are branch instructions or other non-sequential instructions that change the PC. Where these instructions are not treated as UNDEFINED within an IT block, the remaining iterations of the PSTATE.IT state machine must be treated in one of the following ways:

- PSTATE.IT is cleared to 0.
- PSTATE.IT advances for either a sequential or a nonsequential change of the PC in the same way as it does for instructions that are not CONSTRAINED UNPREDICTABLE that cause a sequential change of the PC.

Note

This does not apply to an instruction that is the last instruction in an IT block.

The instructions addressed by the updated PC must do one of the following:

- Execute as if they had passed the Condition code check for the remaining iterations of the PSTATE.IT state machine.
- Execute as NOPs. That is, they behave as if they had failed the Condition code check for the remaining iterations of the PSTATE.IT state machine.
- Execute as if they were unconditional, or, if the instructions are part of another IT block, in accordance with the behavior described in Branching into an IT block.

The behavior might in some implementations vary from instruction to instruction, or between different instances of the same instruction.

For exception returns or Debug state exits that cause PSTATE.IT to be set to a reserved value in T32 state or that return to A32 state with a nonzero value in PSTATE.IT, the PSTATE.IT bits are forced to 0b00000000 . The reserved values are:

```
PSTATE.IT[7:4] != '0000' && PSTATE.IT[3:0] == '0000' PSTATE.IT[2:0] != '000' when SCTLR/SCTLR_EL_1.ITD == '1'
```

Exception returns or Debug state exits that set PSTATE.IT to a non-reserved value in T32 state can occur when the flow of execution returns to a point:

- Outside an IT block, but with the PSTATE.IT bits set to a value other than 0b00000000 .
- Inside an IT block, but with a different value of the PSTATE.IT bits than if the IT block had been executed without an exception return or Debug state exit.

In this case, the instructions at the target of the exception return or Debug state exit must do one of the following:

- Execute as if they passed the Condition code check for the remaining iterations of the PSTATE.IT state machine.
- Execute as NOPs. That is, they behave as if they failed the Condition code check for the remaining iterations of the PSTATE.IT state machine.
- Execute as if they were unconditional, or as if the instruction were part of another IT block, in accordance with the behavior in Branching into an IT block.

The remaining iterations of the PSTATE.IT state machine must behave in one of the following ways:

- The PSTATE.IT state machine advances as if it were in an IT block.
- The PSTATE.IT bits are ignored.
- The PSTATE.IT bits are forced to 0b00000000 .

## K1.1.8 Unallocated System register access instructions

From the introduction of the Armv8-A architecture, accesses to unallocated System register encodings are UNDEFINED.

This includes:

- Reads using encodings that are defined as WO.
- Writes using encodings that are defined as RO.
- MCR or MRC accesses to using a set of { coproc , CRn , opc1 , CRm , opc2 } values that the Armv7 architecture defined as UNPREDICTABLE.
- MCRR and MRRC instructions with unallocated values of opc1 or CRm that are described as UNPREDICTABLE are UNDEFINED in the Armv8-A and later architectures.

## K1.1.9 SBZ or SBO fields T32 and A32 in instructions

Many of the T32 and A32 instructions have (0) or (1) in the instruction decode to indicate Should-Be-Zero , SBZ, or Should-Be-One , SBO. If the instruction bit pattern of an instruction is executed with these fields not having the should be values, one of the following must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- The instruction operates as if the bit had the should-be value.
- Any destination registers of the instruction become UNKNOWN.

The exceptions to this rule are:

- LDM, LDMIA, LDMFD.
- LDMDB, LDMEA.
- LDR(literal).
- LDRB(literal).
- LDRD(immediate).
- LDRD(register).
- LDRD(literal).
- LDRH(literal).
- LDRSB (literal).
- LDRSH (literal).
- POP.
- PUSH.
- SDIV.
- STM, STMIA, STMEA.
- STMDB, STMFD.
- UDIV.

## K1.1.10 UNPREDICTABLE cases in immediate constants in T32 data-processing instructions

The description of immediate constants in T32 data processing Modified immediate constants in T32 instructions include constant values that were UNPREDICTABLE in Armv7. Instruction encodings describes 32-bit T32 instructions as { hw1 , hw2 }, where hw1 is the left-hand halfword in the 32-bit encoding diagram for the instruction. The UNPREDICTABLE cases are those where both:

- hw2 [7:0] == 0b0000000 .
- hw1 [10] == 0 and either:
- -hw2 [14:12] == 0b001 .
- -hw2 [14:12] == 0b010 .
- -hw2 [14:12] == 0b011 .

From the introduction of the Armv8 architecture, the CONSTRAINED UNPREDICTABLE behavior is that these encodings produce the value 0b0000000 .

## K1.1.11 UNPREDICTABLE cases in immediate constants in Advanced SIMD instructions

The description of immediate constants in Modified immediate constants in T32 and A32 Advanced SIMD instructions include constant values that were UNPREDICTABLE in Armv7. The UNPREDICTABLE cases are those where:

- The bits that the encoding diagram shows as abcd are all 0. In the A32 encoding these are bits[24, 18:6, 3:0]. In the T32 encoding they are bits { hw1 [12, 2:0], hw2 [3:0]}.

- The bits that the encoding diagram shows as cmode[3:1] are one of { 0b001 , 0b010 , 0b011 , 0b101 , 0b110 }. In the A32 encoding these are bits[11:9]. In the T32 encoding they are bits hw2 [11:9].

From the introduction of the Armv8 architecture, the CONSTRAINED UNPREDICTABLE behavior is that these encodings produce an immediate constant value of zero.

## K1.1.12 CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values

The Arm architecture allows copies of System register control or data values to be cached in a cache or TLB. This can lead to CONSTRAINED UNPREDICTABLE behavior if the cache or TLB has not been correctly invalidated following a change of the control or data values.

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

Alternatively to this CONSTRAINED UNPREDICTABLE behavior, an implementation detecting multiple hits within a TLB might generate an exception, reporting the exception using the TLB Conflict fault code, see TLB conflict aborts.

The choice between the behaviors might, in some implementations, vary for each use of a control or data value.

## K1.1.13 CONSTRAINED UNPREDICTABLE behavior due to inadequate context synchronization

The Arm architecture requires that changes to System registers must be synchronized before they take effect. This can lead to CONSTRAINED UNPREDICTABLE behavior if the synchronization has not been performed.

In these cases, the behavior of the PE is consistent with the unsynchronized control value being either the old value or the new value.

Where multiple control values are updated but not yet synchronized, each control value might independently be the old value or the new value.

In addition, where the unsynchronized control value applies to different areas of functionality, or what an implementation has constructed as different areas of functionality, those areas might independently treat the control value as being either the old value or the new value.

The choice between these behaviors might, in some implementations, vary for each use of a control value.

## K1.1.14 Unallocated values with register fields of CP15 registers and Translation Table entries

Unless stated elsewhere, all unallocated or reserved values of fields with allocated values within CP15 registers and Translation Table entries be have in one in one of the following ways:

- The encoding maps onto any of the allocated values but otherwise does not cause UNPREDICTABLE behavior.
- The encodings cause effects that could be achieved by a combination of more than one of the allocated encodings.
- The encodings cause the field to have no functional effect.

## K1.1.15 Translation Table Base Address alignment

Amisaligned Translation Table Base Address can occur if:

- The VMSAv8-32 Short-descriptor translation table format is enabled and TTBR0[13-N:7], which is defined to be RES0, contains a nonzero value.
- The VMSAv8-32 Long-descriptor translation table format is enabled, and TTBR0[x-1:3], TTBR1[x-1:3], HTTBR[x-1:3], or VTTBR[x-1:3], which are defined to be RES0, contains a nonzero value.

In the event of a misaligned Translation Table Base Address, one of the following behaviors must occur:

- The field that is defined to be RES0 is treated as if all bits were zero:
- -The value that is read back might be the value written or it might be zero.
- The calculation of an address for a translation table walk using that register might be corrupted in those bits that are nonzero.

## K1.1.16 Handling of System register control fields for Advanced SIMD and floating-point operation

For historical reasons described in Background to the System register interface, each of the CPACR, HCPTR, and NSACRhas a pair of control fields that were defined to have identical functionality for controlling Advanced SIMD and floating-point operation. These fields are:

- CPACR.{cp10, cp11}.
- HCPTR.{TCP10, TCP11}.
- NSACR.{cp10, cp11}.

The architecture requires that both fields in one of these pairs are programmed to the same value. If this is not done, then the CONSTRAINED UNPREDICTABLE behavior is that behavior is the same as if the cp11 or TCP11 control field was equal to the cp10 or TCP10 field.This is in all respects except for the value read back by a direct read of the register. After a register write that writes different values to the two fields of a pair, a direct read of the register might return an UNKNOWN value for the cp11 or TCP11 field.

Note

This means that, when different values are written to the {cp10, cp11} fields in a single register, the architecture permits but does not require that a read of that register returns the value written to the cp11 field.

## K1.1.16.1 CONSTRAINED UNPREDICTABLE CPACR and NSACR settings

If CPACR.cp&lt;n&gt; contains the encoding '10' , then one of the following behaviors must occur:

- The encoding maps onto any of the allocated values, but otherwise does not cause UNPREDICTABLE behavior.
- The encoding causes effects that could be achieved by a combination of more than one of the allocated encodings.

Note

In Armv7, CPACR had a D32DIS bit, and NSACR had an NSD32DIS bit. There is no CPACR.D32DIS or NSACR.NSD32DIS in Armv8-A and later architectures, and the corresponding bits in the two registers are RES0.

## K1.1.17 Mapping of non-idempotent memory locations using the Normal memory type

If non-idempotent memory locations are mapped using the Normal memory type, the state of the non-idempotent memory location may become corrupted in the following circumstances:

- Speculative read accesses may cause accesses to the non-idempotent memory locations that would not occur as part of a simple sequential execution.
- Writes to non-idempotent memory locations might be merged or split. In this case, the number and size of writes seen by the memory location might not be the number and size that occur as part of a simple sequential execution.

## K1.1.18 The Performance Monitors Extension

IWKXBB

RXSVNC

The following subsections describe CONSTRAINED UNPREDICTABLE behaviors when accessing the Performance Monitors Extension in AArch32 state:

- CONSTRAINED UNPREDICTABLE accesses to PMXEVTYPER or PMXEVCNTR.
- CONSTRAINED UNPREDICTABLE accesses to PMEVCNTR&lt;n&gt; and PMEVTYPER&lt;n&gt;.
- CONSTRAINED UNPREDICTABLE behavior caused by HDCR.HPMN.

## K1.1.18.1 CONSTRAINED UNPREDICTABLE accesses to PMXEVTYPER or PMXEVCNTR

When FEAT\_FGT is not implemented and if PMSELR.SEL is greater than the number of event counters accessible at the current Exception level, then accesses to PMXEVTYPER or PMXEVCNTR can cause CONSTRAINED UNPREDICTABLE behavior. This occurs when any of the following is true:

- If PMSELR.SEL is not equal to 31, and PMSELR.SEL is greater than or equal to PMCR.N, and the PE is executing in EL2 or EL3.
- If FEAT\_SEL2 is disabled or is not implemented, PMSELR.SEL is not 31, and PMSELR.SEL is greater than or equal to PMCR.N, and the PE is executing in Secure EL1 or Secure EL0.
- If PMSELR.SEL is not 31, and PMSELR.SEL is greater than or equal to HDCR.HPMN, and the PE is executing in EL1 or EL0.

In these cases, the PE does one of the following:

- Accesses to PMXEVTYPER or PMXEVCNTR are UNDEFINED.
- Accesses to PMXEVTYPER or PMXEVCNTR behave as RAZ/WI.
- Accesses to PMXEVTYPER or PMXEVCNTR execute as NOPs.
- Accesses to PMXEVTYPER or PMXEVCNTR behave as if PMSELR.SEL contains an UNKNOWN value that is less than the number of counters accessible at the current Exception level and Security state.
- Accesses to PMXEVTYPER or PMXEVCNTR behave as if PMSELR.SEL is 31.
- If EL2 is implemented and enabled in the current Security state, and PMSELR.SEL is less than the number of accessible event counters but greater than the number of accessible counters at this Exception level, access to PMXEVTYPERor PMXEVCNTR from EL1 or permitted access from EL0 is trapped to EL2.

IHNSSP

RZLGPG

Note

If EL2 is implemented and enabled in the current Security state, HDCR.HPMN, or MDCR\_EL2.HPMN, identifies the number of accessible counters at EL0 or EL1. Otherwise, the number of accessible counters is the number of accessible event counters.

Accesses from EL0 to PMXEVCNTR are permitted when:

- EL1 is using AArch32 and the values of PMUSERENR.{ER, EN} are both 1.
- EL1 is using AArch64 and the values of PMUSERENR\_EL0.{ER, EN} are both 1.

Accesses from EL0 to PMXEVTYPER are permitted when:

- EL1 is using AArch32 and the value of PMUSERENR.EN is 1.
- EL1 is using AArch64 and the value of PMUSERENR\_EL0.EN is 1.

When FEAT\_FGT is not implemented and if PMSELR.SEL is equal to 31, the PE does one of the following:

- Accesses to PMXEVCNTR are UNDEFINED.
- Accesses to PMXEVCNTR behave as RAZ/WI.
- Accesses to PMXEVCNTR execute as NOPs.
- Accesses to PMXEVCNTR behave as if PMSELR.SEL contains an UNKNOWN value that is less than the number of counters accessible at the current Exception level and Security state.
- If EL2 is implemented and enabled in the current Security state, for an access to PMXEVCNTR from EL1 or a permitted access from EL0, if the counter is implemented but not accessible at the current Exception level, the register access is trapped to EL2.

## K1.1.18.2 CONSTRAINED UNPREDICTABLE accesses to PMEVCNTR&lt;n&gt; and PMEVTYPER&lt;n&gt;

IGRBYY If FEAT\_FGT is implemented, and EL2 is implemented in the current Security state, and EL1 is using AArch64, permitted access to PMEVCNTR&lt;n&gt; and PMEVTYPER&lt;n&gt; are not CONSTRAINED UNPREDICTABLE.

IGRBHK When FEAT\_FGT is not implemented and if &lt;n&gt; is greater than the number of event counters available in the current Exception level and state, reads and writes of PMEVCNTR&lt;n&gt; and PMEVTYPER&lt;n&gt; are CONSTRAINED UNPREDICTABLE, and the PE does one of the following:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.
- If EL2 is implemented and enabled in the current Security state, for an access to PMEVCNTR&lt;n&gt; or PMEVTYPER&lt;n&gt; from EL1 or a permitted access from EL0, if the counter is implemented but not accessible at the current Exception level, the register access is trapped to EL2.

Accesses from EL0 are permitted to PMEVCNTR&lt;n&gt; when:

- -EL1 is using AArch32 and the values of PMUSERENR.{ER, EN} are both 1.
- -EL1 is using AArch64 and the values of PMUSERENR\_EL0.{ER, EN} are both 1.

Accesses from EL0 are permitted to PMEVTYPER&lt;n&gt; when:

- -EL1 is using AArch32 and the value of PMUSERENR.EN is 1.
- -EL1 is using AArch64 and the value of PMUSERENR\_EL0.EN is 1.

Note

If EL2 is implemented and enabled in the current Security state, at EL0 and EL1, HDCR.HPMN, or MDCR\_EL2.HPMN, identifies the number of accessible counters. Otherwise, the number of accessible counters is the number of accessible event counters.

## K1.1.18.3 CONSTRAINED UNPREDICTABLE behavior caused by HDCR.HPMN

If EL2 is implemented, NUM\_PMU\_COUNTERS is nonzero, and any of the following is true:

- FEAT\_HPMN0 is not implemented and HDCR.HPMN is 0.
- FEAT\_PMUv3\_EXTPMN is not implemented and HDCR.HPMN is set to a value greater than NUM\_PMU\_COUNTERS.

Then the following CONSTRAINED UNPREDICTABLE behaviors apply:

RSMXTG

- The value returned by a direct read of HDCR.HPMN is UNKNOWN.
- Either:
- -An UNKNOWN number of counters are reserved for EL2 use. That is, the PE behaves as if HDCR.HPMN is set to an UNKNOWN nonzero value less than or equal to NUM\_PMU\_COUNTERS.
- -All counters are reserved for EL2 and EL3 use, meaning no counters are accessible from EL1 and EL0.

## K1.1.18.4 CONSTRAINED UNPREDICTABLE behavior caused by PMCCR.EPMN

If FEAT\_PMUv3\_EXTPMN is implemented and PMCCR.EPMN is greater than NUM\_PMU\_COUNTERS, then all of the following apply:

- External reads of PMCCR.EPMN returns an UNKNOWN value that is less than or equal to 31.
- For the purposes of indirect reads of PMCCR.EPMN as a result of the following reads, the Effective value of PMCCR.EPMN is an UNKNOWN value that is less than or equal to 31:
- -Direct reads of PMCR.N.
- -Direct reads of HDCR.HPMN.
- -External reads of PMCFGR.N.
- -If FEAT\_PMUv3\_ICNTR is implemented, external reads of PMCGCR0.CG0NC.
- For all other purposes, the Effective value of PMCCR.EPMN is an UNKNOWN value that is less than or equal to NUM\_PMU\_COUNTERS.

## K1.1.19 The Activity Monitors Extension

The following subsections describe CONSTRAINED UNPREDICTABLE behaviors when accessing the Activity Monitors registers in AArch32 state:

- CONSTRAINED UNPREDICTABLE accesses to AMEVCNTR0&lt;n&gt; and AMEVTYPER0&lt;n&gt;.
- CONSTRAINED UNPREDICTABLE accesses to AMEVCNTR1&lt;n&gt; and AMEVTYPER1&lt;n&gt;.
- CONSTRAINED UNPREDICTABLE accesses to AMCNTENCLR1 and AMCNTENSET1.

## K1.1.19.1 CONSTRAINED UNPREDICTABLE accesses to AMEVCNTR0&lt;n&gt; and AMEVTYPER0&lt;n&gt;

If &lt;n&gt; is greater than the number of architected activity monitor event counters, reads and writes of AMEVCNTR0&lt;n&gt; and AMEVTYPER0&lt;n&gt; are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.

Note

AMCGCR.CG0NC identifies the number of architected activity monitor event counters.

## K1.1.19.2 CONSTRAINED UNPREDICTABLE accesses to AMEVCNTR1&lt;n&gt; and AMEVTYPER1&lt;n&gt;

If &lt;n&gt; is greater than the number of auxiliary activity monitor event counters, reads and writes of AMEVCNTR1&lt;n&gt; and AMEVTYPER1&lt;n&gt; are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP.

Note

AMCGCR.CG1NC identifies the number of auxiliary activity monitor event counters.

## K1.1.19.3 CONSTRAINED UNPREDICTABLE accesses to AMCNTENCLR1 and AMCNTENSET1

If the number of auxiliary activity monitor event counters that are implemented is zero, reads and writes of AMCNTENCLR1and AMCNTENSET1 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.

- Accesses to the register behave as RAZ/WI.

- Accesses to the register execute as a NOP.

Note

The number of auxiliary activity monitor event counters that are implemented is zero exactly when AMCFGR.NCG is 0b0000 .

## K1.1.20 Syndrome register handling for CONSTRAINED UNPREDICTABLE instructions treated as UNDEFINED

When a CONSTRAINED UNPREDICTABLE instruction is treated as UNDEFINED, this generates an exception:

- If this exception is taken to an Exception level that is using AArch64, then ESR\_ELx is UNKNOWN.
- If this exception is taken to EL2 and EL2 is using AArch32, then the HSR is unknown.

Note

The value written to ESR or HSR must be consistent with a value that could be created as the result of an exception from the same Exception level that generated the exception, but resulted from a situation that is not CONSTRAINED UNPREDICTABLE at that Exception level. This is to avoid a possible privilege violation.

## K1.1.21 Out of range VA

If the PE executes an instruction for which the instruction address, size, and alignment mean it contains the bytes 0xFFFF\_FFFF and 0x0000\_0000 , then the bytes that wrap around and appear to be from 0x0000\_0000 onwards come from an UNKNOWN address.

If the PE executes a load or store instruction for which the computed address, total access size, and alignment mean it accesses bytes 0xFFFF\_FFFF and 0x0000\_0000 , then the bytes that wrap around and appear to be from 0x0000\_0000 onwards come from an UNKNOWN address.

## K1.1.22 Instruction fetches from Device memory

Instruction fetches from Device memory are CONSTRAINED UNPREDICTABLE.

If a location in memory has the Device attribute and is not marked as execute-never, then an implementation might perform speculative instruction accesses to this memory location when address translation is enabled.

If a branch causes the Program Counter to point to a location in memory with the Device attribute that is not marked as execute-never for the current Exception level for instruction fetches, then an implementation must perform one of the following behaviors:

- It treats the instruction fetch as if it were to a memory location with the Normal, Non-cacheable attribute.
- It generates a Permission fault.

## K1.1.23 Multi-access instructions that load the PC from Device memory

Multi-access instructions that load the PC from Device memory when address translation is enabled are UNPREDICTABLE in AArch32 state. From the introduction of the Armv8-A architecture in AArch32 state an implementation must perform one of the following behaviors:

- It loads the PC from the memory location as if the memory location had the Normal Non-cacheable attribute.
- It generates a Permission fault.

## K1.1.24 Programming CSSELR.Level for a cache level that is not implemented

If CSSELR.Level is programmed to a cache level that is not implemented, then a read of CSSELR returns an UNKNOWN value in CSSELR.Level.

If CSSELR.Level is programmed to a cache level that is not implemented, then on a read of CCSIDR an implementation must perform one of the following behaviors:

- The CCSIDR read is treated as a NOP.
- The CCSIDR read is UNDEFINED.
- The CCSIDR read returns an UNKNOWN value.

When FEAT\_CCIDX is implemented, CCSIDR2 is implemented. If CSSELR.Level is programmed to a cache level that is not implemented, then on a read of CCSIDR2 an implementation must perform one of the following behaviors:

- The CCSIDR2 read is treated as a NOP.
- The CCSIDR2 read is UNDEFINED.
- The CCSIDR2 read returns an UNKNOWN value.

## K1.1.25 Crossing a page boundary with different memory types or Shareability attributes

If a single load or store instruction generates multiple memory accesses, such that the total set of accesses crosses a page boundary to a memory location that has a different memory type, Normal or Device, or Shareability attribute results in CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation must perform one of the following behaviors:

- Each memory access generated by the instruction uses the memory type and Shareability attribute associated with its own address.
- •
- The instruction generates an alignment fault caused by the memory type.

For the Non-secure PL1&amp;0 translation regime:

- -If the stage 1 translation causes the mismatch, the resulting exception is taken to PL1.
- -If the stage 2 translation causes the mismatch, the resulting exception is taken to PL2.
- -If both stages of translation cause the mismatch, the resulting exception can be taken to either PL1 or PL2.
- The instruction executes as a NOP.

## K1.1.26 Crossing a 4KB boundary with a Device access

Amemory access from a load or store instruction to Device memory that crosses a 4KB boundary results in CONSTRAINED UNPREDICTABLE behavior. In this case, the implementation must perform one of the following behaviors:

- All memory accesses generated by the instruction are performed as if the presence of the boundary had no effect on the memory accesses.
- All memory accesses generated by the instruction are performed as if the presence of the boundary had no effect on the memory accesses, except that there is no guarantee of ordering between memory accesses.
- The instruction generates an Alignment fault caused by the memory type.

For the Non-secure PL1&amp;0 translation regime:

- -If the stage 1 translation causes the boundary to be crossed, the resulting exception is taken to PL1.
- -If the stage 2 translation causes the boundary to be crossed, the resulting exception is taken to PL2.
- -If both stages of translation cause the boundary to be crossed, the resulting exception can be taken to either PL1 or PL2.
- The instruction executes as a NOP.

Note

The boundary referred to is between two Device memory regions that are both of 4KB and aligned to 4KB.

## K1.1.27 UNPREDICTABLE behaviors with Load-Exclusive/Store-Exclusive pairs

Load-Exclusive and Store-Exclusive instruction usage restrictions defines a Load-Exclusive/Store-Exclusive pair, and identifies various CONSTRAINED UNPREDICTABLE behaviors associated with using Load-Exclusive/Store-Exclusive pairs. These cases were UNPREDICTABLE in Armv7. In summary, these cases are:

- The target virtual address of a StoreExcl instruction is different from the virtual address of the preceding LoadExcl instruction in the same thread of execution.
- The transaction size of a StoreExcl instruction is different from the transaction size of the preceding LoadExcl instruction in the same thread of execution.
- The memory attributes for a StoreExcl instruction are different from the memory attributes for the preceding LoadExcl instruction in the same thread of execution, either:
- -Because the translation of the accessed address changes between the LoadExcl instruction and the StoreExcl instruction.
- -Because the LoadExcl instruction and the StoreExcl instruction use different virtual addresses, with different attributes, that point to the same physical address.

In addition, the effect of a data or unified cache invalidate, clean, or clean and invalidate instruction on a local or global Exclusives monitor that is in the Exclusive Access state is CONSTRAINED UNPREDICTABLE.

See the descriptions in Load-Exclusive and Store-Exclusive instruction usage restrictions for the permitted behavior in each of these cases, and any constraints that might apply to whether the case is CONSTRAINED UNPREDICTABLE.

Note

Additional CONSTRAINED UNPREDICTABLE cases can apply to Load-Exclusive and Store-Exclusive instructions, see CONSTRAINED UNPREDICTABLE behavior for T32 and A32 System instructions in the base instruction set.

## K1.1.28 CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings

The T32 and A32 instruction sets include encodings that result in CONSTRAINED UNPREDICTABLE behavior when they are decoded.

## K1.1.28.1 CONSTRAINED UNPREDICTABLE behavior of CRC32 instruction encodings

In the T32 and A32 instruction sets, there are encodings of the CRC32 and CRC32C instructions that result in CONSTRAINED UNPREDICTABLE behavior. These encodings are listed in the following places in the T32 and A32 instruction sets:

- Cyclic Redundancy Check for the A32 instruction set, with sz = 11 .
- Data-processing (two source registers) for the T32 instruction set, with op1 = 10x and op2 = 11 .

The CONSTRAINED UNPREDICTABLE behavior for these encodings is described in CRC32 and CRC32C.

## K1.1.28.2 CONSTRAINED UNPREDICTABLE behavior of other A32 instruction encodings

In the A32 instruction set, there are encodings that result in CONSTRAINED UNPREDICTABLE behavior. These encodings are listed in:

- Miscellaneous.
- Memory hints and barriers.
- Barriers.

The CONSTRAINED UNPREDICTABLE behavior is that an implementation must treat the encodings in one of the following ways:

- The instruction encoding is UNDEFINED.
- The instruction encoding executes as a NOP.

## K1.1.29 Out of range values of the Set/Way/Index fields in cache maintenance instructions

In the cache maintenance by set/way instructions DCCISW, DCCSW, and DCISW, if any set/way/index argument is larger than the value supported by the implementation, then the behavior is CONSTRAINED UNPREDICTABLE and one of the following occurs:

- The instruction is UNDEFINED.

- The instruction performs cache maintenance on one of:

- No cache lines.

- Asingle arbitrary cache line.

- Multiple arbitrary cache lines.

Note

This CONSTRAINED UNPREDICTABLE behavior applies, also, to the A64 cache maintenance by set/way instructions DC CISW, DC CSW, and DC ISW.

## K1.1.30 CONSTRAINED UNPREDICTABLE behavior for T32 and A32 System instructions in the base instruction set

This section lists the CONSTRAINED UNPREDICTABLE behavior for the different T32 and A32 System instructions.

Note

If an instruction can result in CONSTRAINED UNPREDICTABLE behavior that is not specific to that particular instruction, see the relevant section in this appendix for a description of the CONSTRAINED UNPREDICTABLE behavior.

## K1.1.30.1 SRS (T32)

For a description of this instruction and the encoding, see SRS, SRSDA, SRSDB, SRSIA, SRSIB.

## K1.1.30.1.1 CONSTRAINED UNPREDICTABLE behavior

For all encodings:

- If the instruction specifies an illegal mode field, then one of the following behaviors must occur:

- The instruction is UNDEFINED.

- The instruction executes as a NOP.

- R13 of the current mode is used.

- The store occurs to an UNKNOWN address, and if the instruction specifies writeback, any general-purpose register that can be accessed without privilege violation from the current Exception level become UNKNOWN.

## K1.1.30.2 SRS (A32)

For a description of this instruction and the encoding, see SRS, SRSDA, SRSDB, SRSIA, SRSIB.

## K1.1.30.2.1 CONSTRAINED UNPREDICTABLE behavior

For all encodings:

- If the instruction specifies an illegal mode field, then one of the following behaviors must occur:

- The instruction is UNDEFINED.

- The instruction executes as a NOP.

- R13 of the current mode is used.

- The store occurs to an UNKNOWN address, and if the instruction specifies writeback, any general-purpose register that can be accessed without privilege violation from the current Exception level become UNKNOWN.

## K1.1.30.3 SUBS PC, LR and related instructions (T32)

For a description of this instruction and the encoding, see the exception return form of SUB, SUBS (immediate).

## K1.1.30.3.1 CONSTRAINED UNPREDICTABLE behavior

For all encodings:

- If this instruction is executed in User mode or in System mode, then one of the following behaviors must occur:

- The instruction is UNDEFINED.

- The instruction executes as a NOP.

- If the instruction transfers an illegal mode encoding to PSTATE.M, then this invokes the illegal exception return.

Note

An illegal mode encoding is either an unallocated mode encoding or one that is not accessible at the current Exception level.

For encoding T5:

- If hw1 [3:0] are not 0b1110 , and the instruction is executed when not in Hyp mode, System mode, or User mode, then one of the following behaviors must occur:

- The instruction is UNDEFINED.

- The instruction is treated as a NOP.

- The instruction is treated as if hw1 [3:0] are 0b1110 .

- The Program Counter is set using the value in the register specified by hw1 [3:0].

## K1.1.30.4 SUBS PC. LR and related instructions (A32)

For a description of this instruction and the encoding, see the exception return forms of MOV , MOVS (register) and SUB, SUBS (immediate).

## K1.1.30.4.1 CONSTRAINED UNPREDICTABLE behavior

For all encodings:

- If this instruction is executed in User mode or in System mode, then one of the following behaviors must occur:

- The instruction is UNDEFINED.

- The instruction executes as a NOP.

- If the instruction transfers an illegal mode encoding to PSTATE.M, then this invokes the illegal exception return.

Note

An illegal mode encoding is either an unallocated mode encoding or one that is not accessible at the current Exception level.

## K1.1.31 CONSTRAINED UNPREDICTABLE behavior, T32 and A32 Advanced SIMD and floating-point instructions

This section lists the CONSTRAINED UNPREDICTABLE behavior for the different T32 and A32 Advanced SIMD and floating-point instructions listed in Alphabetical list of Advanced SIMD and floating-point instructions.

Note

- The pseudocode used in this section to describe cases that can result in CONSTRAINED UNPREDICTABLE behavior does not necessarily match the encoding specific pseudocode for a specific instruction.
- If an instruction can result in CONSTRAINED UNPREDICTABLE behavior that is not specific to that particular instruction, see the relevant section in this appendix for a description of the CONSTRAINED UNPREDICTABLE behavior.

## K1.1.31.1 VCVT (between floating-point and fixed-point)

For a description of this instruction and the encoding, see VCVT (between floating-point and fixed-point, floating-point).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.2 VLD1 (multiple single elements)

For a description of this instruction and the encoding, see VLD1 (multiple single elements).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.3 VLD1 (single element to all lanes)

For a description of this instruction and the encoding, see VLD1 (single element to all lanes).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.4 VLD2 (multiple 2-element structures)

For a description of this instruction and the encoding, see VLD2 (multiple 2-element structures).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.5 VLD2 (single 2-element structure to one lane)

For a description of this instruction and the encoding, see VLD2 (single 2-element structure to one lane).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.6 VLD2 (single 2-element structure to all lanes)

For a description of this instruction and the encoding, see VLD2 (single 2-element structure to all lanes).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.7 VLD3 (multiple 3-element structures)

For a description of this instruction and the encoding, see VLD3 (multiple 3-element structures).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.8 VLD3 (single 3-element structure to one lane)

For a description of this instruction and the encoding, see VLD3 (single 3-element structure to one lane).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.9 VLD3 (single 3-element structure to all lanes)

For a description of this instruction and the encoding, see VLD3 (single 3-element structure to all lanes).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.10 VLD4 (multiple 4-element structures)

For a description of this instruction and the encoding, see VLD4 (multiple 4-element structures).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.11 VLD4 (single 4-element structure to one lane)

For a description of this instruction and the encoding, see VLD4 (single 4-element structure to one lane).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.12 VLD4 (single 4-element structure to all lanes)

For a description of this instruction and the encoding, see VLD4 (single 4-element structure to all lanes).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.13 VLDM

For a description of this instruction and the encoding, see VLDM, VLDMDB, VLDMIA.

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.14 VMOV (between two general-purpose registers and two single-precision registers)

For a description of this instruction and the encoding, see VMOV (between two general-purpose registers and two single-precision registers).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.15 VMOV (between two general-purpose registers and a doubleword floating-point register)

For a description of this instruction and the encoding, see VMOV (between two general-purpose registers and a doubleword floating-point register).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.16 VST1 (multiple single elements)

For a description of this instruction and the encoding, see VST1 (multiple single elements).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.17 VST2 (multiple 2-element structures)

For a description of this instruction and the encoding, see VST2 (multiple 2-element structures).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.18 VST2 (single 2-element structure from one lane)

For a description of this instruction and the encoding, see VST2 (single 2-element structure from one lane).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.19 VST3 (multiple 3-element structures)

For a description of this instruction and the encoding, see VST3 (multiple 3-element structures).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.20 VST3 (single 3-element structure from one lane)

For a description of this instruction and the encoding, see VST3 (single 3-element structure from one lane).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.21 VST4 (multiple 4-element structures)

For a description of this instruction and the encoding, see VST4 (multiple 4-element structures).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.22 VST4 (single 4-element structure from one lane)

For a description of this instruction and the encoding, see VST4 (single 4-element structure from one lane).

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.31.23 VSTM

For a description of this instruction and the encoding, see VSTM, VSTMDB, VSTMIA.

If this instruction is not UNDEFINED, then whether it is affected by traps or enables relating to the use of the SIMD&amp;FP registers when it is CONSTRAINED UNPREDICTABLE, is IMPLEMENTATION DEFINED. The implementation must ensure that the CONSTRAINED UNPREDICTABLE behavior does not corrupt registers that are not accessible at the current Exception level by instructions that are not CONSTRAINED UNPREDICTABLE.

## K1.1.32 CONSTRAINED UNPREDICTABLE behaviors associated with the VTCR

The following subsections describe the CONSTRAINED UNPREDICTABLE behavior associated with programming the VTCR:

- Misprogramming VTCR.S.
- Misprogramming VTCR.{SL0, T0SZ}.

## K1.1.32.1 Misprogramming VTCR.S

VTCR.S must be programmed to the value of T0SZ[3], or the effect is CONSTRAINED UNPREDICTABLE. From the introduction of the Armv8-A architecture, if VTCR.S is not programmed correctly, then the VTCR.T0SZ value is treated as an UNKNOWN value.

Note

The CONSTRAINED UNPREDICTABLE behavior described in Misprogramming VTCR.{SL0, T0SZ} means the UNKNOWN VTCR.T0SZ value might generate a Translation fault.

## K1.1.32.2 Misprogramming VTCR.{SL0, T0SZ}

If the stage 2 input address size, as programmed in VTCR.T0SZ, is out of range with respect to the starting level, as programmed in the VTCR.SL0 field, or the VTCR.SL0 field is programmed to a reserved value, then at the time of a translation walk that uses the stage 2 translation, a stage 2 level 1 Translation Fault is generated.

## K1.1.33 CONSTRAINED UNPREDICTABLE behavior of EL2 features

The following sections, and the instruction descriptions, describe CONSTRAINED UNPREDICTABLE behavior that can occur in an implementation that includes EL2 where EL2 can use AArch32:

- ERET in User mode or System mode.
- Illegal entry into, or exit from, Hyp mode.
- Exception return to Hyp mode.
- Stage 1 default memory type.
- Trapping of general exceptions to Hyp mode.
- MSR(banked register) and MRS (banked register).

## K1.1.33.1 ERET in User mode or System mode

If ERET is executed in User mode or System mode, it behaves as described in SUBS PC, LR and related instructions (T32).

## K1.1.33.2 Illegal entry into, or exit from, Hyp mode

Illegal entry to Hyp mode or exit from Hyp mode might be due to, for example:

- Modifying PSTATE.M when in Hyp mode.
- Secure state use of Hyp mode.

Attempting to change into Hyp mode or out of Hyp mode using the MSR or CPS instruction invokes the illegal exception return by not changing the mode, and setting PSTATE.IL to 1.

SRS using the Hyp mode SP from Non-secure modes other than Hyp mode, or from Secure state, is handled as described in SRS (T32) and SRS (A32).

## K1.1.33.3 Exception return to Hyp mode

Exception returns to Hyp mode when SCR.NS == 0 or from a Non-secure PL1 mode invokes the illegal exception return.

## K1.1.33.4 Stage 1 default memory type

If HCR.DC == 1, then the behavior of the PE when executing in a Non-secure mode other than Hyp mode is consistent with:

- SCTLR.M == 0, regardless of the actual value of SCTLR.M, other than for the value returned by an explicit read of SCTLR.M.
- HCR.VM == 1, regardless of the actual value of HCR.VM, other than for an explicit read of this bit.

## K1.1.33.5 Trapping of general exceptions to Hyp mode

Attempting to perform an exception return to a Non-secure PL1 mode when HCR.TGE == 1 invokes an illegal exception return.

Attempting to change from Monitor mode to a Non-secure PL1 mode when HCR.TGE == 1 by executing a CPS or MSR instruction generates an Illegal Execution state exception, by not changing the mode, and setting PSTATE.IL to 1.

When EL3 is using AArch32, attempting to change from a Secure PL1 mode to a Non-secure PL1 mode when HCR.TGE is 1, by changing SCR.NS from 0 to 1, results in no change of SCR.NS.

Because taking an exception into Non-secure PL1 modes leads to a CONSTRAINED UNPREDICTABLE situation, the following additional properties apply when HCR.TGE == 1:

- All exceptions that would be routed to EL1 are routed to EL2.
- Non-secure SCTLR.M is treated as being 0, regardless of its actual value, other than for an explicit read of this bit.
- HCR.FMO, HCR.IMO, and HCR.AMO are treated as being 1, regardless of their actual value, other than for an explicit read of these bits.
- All virtual interrupts are disabled.
- Any IMPLEMENTATION DEFINED mechanisms for signaling virtual interrupts are disabled.

## K1.1.33.6 MSR (banked register) and MRS (banked register)

If the target register specified by the { R , SYSm } fields of the instruction encoding is not accessible from the PE mode in which the instruction was executed (see Usage restrictions on the banked register transfer instructions), then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- For MRS (banked register) instructions, the destination general-purpose register becomes UNKNOWN.

- For MSR (banked register) instructions, if the register specified could be accessed from the current mode by other mechanisms, then this register is UNKNOWN. Otherwise, the instruction is a NOP.

If the instruction was executed specifying an unallocated { R , SYSm } field value or an unimplemented register (see Encoding the register argument in the banked register transfer instructions), then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as a NOP.
- An allocated MRS (banked register) or MSR (banked register) instruction is executed.

## K1.1.34 Reserved values in System and memory-mapped registers and translation table entries

Unless otherwise stated, all unallocated or reserved values of fields with allocated values within the AArch32 System registers, memory-mapped registers, and translation table entries behave in one of the following ways:

- The encoding maps onto any of the allocated values, but otherwise does not cause CONSTRAINED UNPREDICTABLE behavior.
- The encoding causes effects that could be achieved by a combination of more than one of the allocated encodings.
- The encoding causes the field to have no functional effect.

Note

These constraints are identical to those for the equivalent AArch64 definitions, as given in Reserved values in System and memory-mapped registers and translation table entries.

Unless otherwise stated, when a direct write of a System register or memory-mapped register writes an unallocated value to a field, if that value is unallocated in all contexts then a subsequent read of the field returns an UNKNOWN value.

## K1.1.35 CONSTRAINED UNPREDICTABLE behavior in Debug state

Behavior in Debug state of this manual describes the CONSTRAINED UNPREDICTABLE behaviors that are specifically associated with Debug state.