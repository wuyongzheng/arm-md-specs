## D24.1 About the AArch64 System registers

The following sections describe common features of the AArch64 registers:

- Fixed values and reserved values in the System register descriptions.
- General behavior of accesses to the AArch64 System registers.
- Principles of the ID scheme for fields in ID registers.

## D24.1.1 Fixed values and reserved values in the System register descriptions

See Fixed values in AArch64 instruction and System register descriptions. This section defines how the glossary terms RAZ, RES0, RAO, and RES1 can be represented in the System register descriptions.

See Reserved values in System and memory-mapped registers and translation table entries. This section describes the behavior of reserved values in the System register descriptions.

## D24.1.2 General behavior of accesses to the AArch64 System registers

The following subsections give general information about the behavior of accesses to the System registers:

- Reset behavior of AArch64 System registers.
- Synchronization requirements for AArch64 System registers.

## D24.1.2.1 Reset behavior of AArch64 System registers

Reset values apply only to RW registers and fields, however:

- Some RO registers or fields, including feature ID registers and some status registers or register fields, always return a known value.
- Some RW and RO registers or register fields return status information about the PE. Unless the register description indicates that the value is UNKNOWN on reset, a read of the register immediately after a reset returns valid information.
- Some RW and RO registers and fields are aliases of other registers or fields. In these cases, the reset behavior of the aliased register or field determines the value returned by a read of the register immediately after a reset.
- WOregisters that only have an effect on writes do not have meaningful reset values. However, an access to a WOregister might affect underlying state, and that state might have a defined reset value.
- IMPLEMENTATION DEFINED registers have IMPLEMENTATION DEFINED reset behavior.

After a reset, only a limited subset of the PE state is guaranteed to be set to defined values. Also, for debug and trace System registers, reset requirements must take account of different levels of reset. For more information about the reset behavior of System registers when the PE resets into an Exception level that is using AArch64, see:

- Reset behavior.
- The appropriate Trace architecture specification, for the Trace System registers.

For a PE reset into an Exception level that is using AArch64, the architecture defines which AArch64 System registers have a defined reset value, and when that defined reset value applies. The register descriptions include this information, and Reset behavior summarizes these architectural requirements. Otherwise, RW registers that have a meaningful reset value reset to an architecturally UNKNOWN value.

Note

Whenthe PE resets into an Exception level that is using AArch32, no PE state that relates to execution in AArch64 state is accessible until another reset causes the Execution state to change to AArch64. Therefore, on a reset into AArch32 state, PE state that relates only to execution in AArch64 state cannot have a meaningful reset value.

## D24.1.2.1.1 Pseudocode description of resetting System registers

The AArch64.ResetSystemRegisters() pseudocode function resets all System registers, and register fields, that have defined reset values, as described in this section and Reset behavior.

Note

For debug and trace System registers, this function resets registers as defined for the appropriate level of reset.

## D24.1.2.2 Synchronization requirements for AArch64 System registers

Reads of the System registers can occur out of order with respect to earlier instructions executed on the same PE, provided that both:

- Any data dependencies between the instructions, including read-after-read dependencies, are respected.
- The reads to the register do not occur earlier than the most recent Context Synchronization event to its architectural position in the instruction stream.

Note

In particular, the values read from System registers that hold self-incrementing counts, such as the Performance Monitors counters or the Generic Timer counter or timers, could be accessed from any time after the previous Context Synchronization event. For example, where a memory access is used to communicate a read of such a counter, an ISB must be inserted between the read of the memory location that is known to have returned its data, either as a result of a condition on that data or of the read having completed, and the read of the counter, if it is necessary that the counter returns a count value after the memory communication.

Unless otherwise stated in its System register definition, a direct write to a System register requires synchronization before software can rely on the effects of that write to affect instructions appearing in program order after the write. This does not apply to Special-purpose registers; for more information, see Instructions for accessing Special-purpose registers. Direct writes to System registers are not allowed to affect any instructions appearing in program order before the direct write. The only exceptions are:

- All direct writes to the same register, that use the same encoding for that register, are guaranteed to occur in program order relative to each other.
- All direct writes to a register occur in program order with respect to all direct reads to the same register using the same encoding.
- Any System register access that an Arm Architecture Specification or equivalent specification defines as not requiring synchronization.
- When FEAT\_BRBE is implemented, execution of BRB INJ does not require explicit synchronization to use the result of direct writes to the Branch record injection data registers in program order before BRB INJ .

Explicit synchronization occurs as a result of a Context Synchronization event, which is one of the following events:

- Execution of an ISB instruction.
- Exception entry, if FEAT\_ExS is not implemented, or if FEAT\_ExS is implemented and defines that exception entries to this Exception level are Context Synchronization events.
- Exception return, if FEAT\_ExS is not implemented, or if FEAT\_ExS is implemented and defines that exception returns from this Exception level are Context Synchronization events.
- Execution of a DCPS instruction in Debug state.
- Execution of a DRPS instruction in Debug state.
- Exit from Debug state.

Note

The ISB and exception entry events are applicable both in Debug state and in Non-debug state.

The pseudocode for each of these events defines the point at which the explicit synchronization takes effect, as a result of a call to the SynchronizeContext() function or InstructionSynchronizationBarrier() function. The principle behind the position of the call to SynchronizeContext() or InstructionSynchronizationBarrier()

is that it occurs before indirect reads of System registers that are used in the construction of the target context, but is permitted to occur after indirect reads of System registers that apply to the context in which the instruction is executed or from which the event is taken.

Note

For some instructions, this means that some System registers are indirectly read before the explicit synchronization, and therefore changes to those System registers might need an explicit Context synchronization event before the instruction. For example, changes to some fields of HCR\_EL2 at EL2 need an explicit ISB in program order before an ERET instruction.

In addition, any system instructions that cause a write to a System register must be synchronized before the result is guaranteed to be visible to subsequent direct reads of that System register.

Direct and indirect reads and writes to RGSR\_EL1, Random Allocation Tag Seed Register, appear to occur in program order relative to other instructions, without the need for any explicit synchronization.

Direct reads to any one of the following registers, using the same encoding, occur in program order relative to each other:

- ISR\_EL1.
- The Generic Timer registers, that is, CNTPCT\_EL0 and CNTVCT\_EL0, and the Counter registers CNTP\_TVAL\_EL0, CNTV\_TVAL\_EL0, CNTHP\_TVAL\_EL2, and CNTPS\_TVAL\_EL1.
- DBGCLAIMCLR\_EL1.
- The PMU Counters, that is, PMCCNTR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMXEVCNTR\_EL0, PMOVSCLR\_EL0, and PMOVSSET\_EL0.
- The System PMU Counters, that is, SPMEVCNTR&lt;n&gt;\_EL0, SPMOVSCLR\_EL0, and SPMOVSSET\_EL0.
- The Debug Communications Channel registers, that is, DBGDTRRX\_EL0, DBGDTR\_EL0, and MDCCSR\_EL0.

All other direct reads of System registers can occur in any order if synchronization has not been performed.

Table D24-1 describes the synchronization requirements between two successive read or write accesses to the same register, where the ordering of the read or write accesses is:

1. Program order, in the event that both the reads or writes are caused by an instruction executed on this PE, other than one caused by a memory access by this PE.
2. The order of arrival of asynchronous reads and writes at the PE relative to the execution of instructions that cause reads or writes.
3. The order of arrival of asynchronous reads and writes at the PE relative to each other.

Table D24-1 Synchronization requirements

| First read/write   | Second read/write   | Synchronization requirement   |
|--------------------|---------------------|-------------------------------|
| Direct read        | Direct read         | None                          |
| Direct read        | Direct write        | None                          |
| Direct read        | Indirect read       | None                          |
| Direct read        | Indirect write      | None, see Notes               |
| Direct write       | Direct read         | None                          |
| Direct write       | Direct write        | None                          |
| Direct write       | Indirect read       | Required                      |
| Direct write       | Indirect write      | None, see Notes               |
| Indirect read      | Direct read         | None                          |
| Indirect read      | Direct write        | None                          |

| First read/write   | Second read/write   | Synchronization requirement   |
|--------------------|---------------------|-------------------------------|
|                    | Indirect read       | None                          |
|                    | Indirect write      | None                          |
| Indirect write     | Direct read         | Required, see Notes           |
| Indirect write     | Direct write        | None, see Notes               |
| Indirect write     | Indirect read       | Required, see Notes           |
| Indirect write     | Indirect write      | None, see Notes               |

D24.1.2.2.1

## Notes

The terms Direct read, Direct write, Indirect read, and Indirect write, as used in Table D24-1, are defined as follows:

## Direct read

## Direct write

## Indirect read

## Indirect write

Where software uses an MRS or MRRS system register access instruction to read that register into a general purpose register.

Where a direct read of a register has a side-effect that changes the contents of a register, the effect of a direct read on that register is defined to be an indirect write. In this case, the indirect write is only guaranteed to have occurred, and be visible to subsequent direct or indirect reads or writes, if synchronization is performed after the direct read.

Where software uses an MSR (register) or MSRR access instruction to write to that register from a general purpose register.

Where a direct write to a register has an effect on the register that means that the value in the register is not always the last value that is written (as is the case with set and clear registers), the effect of a direct write on that register is defined to be an indirect write. In this case, the indirect write is only guaranteed to be visible to subsequent direct or indirect reads or writes if synchronization is performed after the direct write and before the subsequent direct or indirect reads or writes.

Where an instruction uses a System register to establish operating conditions for the instruction, for example, the TTBR\_ELx address or whether memory accesses are forced to be Non-cacheable. This includes situations where the contents of one System register selects what value is read or written using a different register. Indirect reads also include reads of the System register by external agents such as debuggers. Instruction execution from MDSTEPOP\_EL1 is an indirect read of MDSTEPOP\_EL1. Where an indirect read of a register has a side-effect that changes the contents of that register, that is defined to be an indirect write.

Where a System register is written as the consequence of some other instruction, exception, operation, or by the asynchronous operation of an external agent, including the passage of time as seen in counters, timers, or performance counters, the assertion of interrupts, or writes from an external debugger.

Note

Registers such as the Exception Syndrome registers that are indirectly written as part of exception entry do not require additional synchronization. This behavior is independent of the value of SCTLR\_ELx.EIS, and the list of affected registers is described in the definition of that field.

The value of a system register does not change unless one of the following occurs:

- As the result of a direct write to the register, that is not specified as being trapped, UNDEFINED or IGNORED.
- As the result of one of the specified indirect writes to the register.
- Areset, if the register has a specified reset behavior for that reset.
- The register holds an UNKNOWN value as the result of one of the above.

Where a direct read or write to a register is followed by an indirect write caused by an external agent, autonomous asynchronous event, or as a result of memory mapped write, synchronization is required to guarantee the order of those two accesses.

Where an indirect write caused by a direct write is followed by an indirect write caused by an external agent, autonomous asynchronous event, or as a result of memory mapped write, synchronization is required to guarantee the order of those two indirect accesses.

Where a direct read to one register causes a bit or field in a different register (or the same register using a different encoding) to be updated, the change to the different register (or same register using a different encoding) is defined to be an indirect write. In this case, the indirect write is only guaranteed to be visible to subsequent direct or indirect reads or writes if synchronization is performed after the direct read and before the subsequent direct or indirect reads or writes.

Where a direct write to one register causes a bit or field in a different register (or the same register using a different encoding) to be updated as a side-effect of that direct write (as opposed to simply being a direct write to the different encoding), the change to the different register (or same register using a different encoding) is defined to be an indirect write. In this case, the indirect write is only guaranteed to be visible to subsequent direct or indirect reads or writes if synchronization is performed after the direct write and before the subsequent direct or indirect reads or writes.

Where indirect writes are caused by the actions of external agents such as debuggers, or by memory-mapped reads or writes by the PE, then an indirect write by that agent and mechanism to a register, followed by an indirect read by that agent and mechanism to the same register using the same address, does not require synchronization.

Where an indirect write occurs as a side-effect of an access, this happens atomically with the access, meaning no other accesses are allowed between the register access and its side-effect.

Note

Even though the 64-bit and 128-bit form of a system register share the same values of {op0, op1, CRn, CRm, op2} , they are considered to be distinct encodings. Therefore, explicit synchronization is required to guarantee ordering in all of the following cases:

- MSRRfollowed by an MRS from the same register.
- MSR(register) followed by an MRRS from the same register.

Where indirect writes to GCSPR\_ELx are made by the following instructions, explicit synchronization is not required to be visible to direct reads, indirect reads, and indirect writes in program order after the initial indirect write:

- All Branch with Link instructions.
- All procedure return instructions.
- GCSPOPM and GCSPUSHM .
- GCSPOPX , GCSPOPCX , and GCSPUSHX .
- GCSSS1 and GCSSS2 .

Indirect writes caused by external agents, autonomous asynchronous events, or as a result of memory-mapped writes, to the registers shown in Table D24-2, are required to be observable to:

- Direct reads in finite time without explicit synchronization.
- Subsequent indirect reads without explicit synchronization.

Without explicit synchronization to guarantee the order of the accesses, where the same register is accessed by two or more of a System register access instruction, and external agent, and autonomous asynchronous event, or as a result of a memory-mapped access, the behavior must be as if the accesses occurred atomically and in any order. This applies even if the accesses occur simultaneously.

## Table D24-2 Registers with a guarantee of observability, VMSAv8-64

| Registers                        | Notes                     |
|----------------------------------|---------------------------|
| ISR_EL1                          | Interrupt Status Register |
| DBGCLAIMCLR_EL1, DBGCLAIMSET_EL1 | Debug CLAIM registers     |

| Registers                                                                            | Notes                                      |
|--------------------------------------------------------------------------------------|--------------------------------------------|
| CNTPCT_EL0, CNTVCT_EL0, CNTP_TVAL_EL0, CNTV_TVAL_EL0, CNTHP_TVAL_EL2, CNTPS_TVAL_EL1 | Generic Timer registers                    |
| PMCCNTR_EL0, PMEVCNTR<n>_EL0, PMXEVCNTR_EL0, PMOVSCLR_EL0, PMOVSSET_EL0              | PMUCounters                                |
| SPMEVCNTR<n>_EL0, SPMOVSCLR_EL0, SPMOVSSET_EL0                                       | System PMUCounters                         |
| DBGDTRTX_EL0, DBGDTRRX_EL0, DBGDTR_EL0, and the DCCflags in MDCCSR_EL0 and EDSCR     | Debug Communication Channel registers      |
| EDSCR.PipeAdv                                                                        | External Debug Status and Control Register |

In addition to the requirements shown in Table D24-2:

- Indirect writes to the following registers as a result of memory-mapped writes, including accesses by external agents, are required to be observable to the indirect read made in determining the response to a subsequent memory-mapped access without explicit synchronization:
- -OSLAR\_EL1. OSLAR\_EL1 is indirectly read to determine whether the subsequent access is permitted.
- -EDLAR, if implemented. EDLAR is indirectly read to determine whether a subsequent write or side-effect of an access is ignored.

## Note

This requirement is stricter than the general requirement for the observability of indirect writes.

- The requirement that an indirect write to the registers in Table D24-2 is observable to direct reads in finite time does not imply that all observers will observe the indirect write at the same time. For example, an increment of the system counter is an autonomous asynchronous event that performs an indirect write to the counter. This asynchronous event might generate a timer interrupt request, resulting in a Context Synchronization event. When a GIC is used, the timer interrupt might arrive at the GIC after the PE has taken an interrupt request from another source, but before software reads the current interrupt ID from the GIC. This means that the GIC might identify the timer interrupt as the current interrupt. Software must not assume that a subsequent direct read of the counter register is guaranteed to observe the updated value of that register. Although this example uses the counter-timer registers, it applies equally to other registers that might be linked to interrupt requests, including the PMU and Statistical Profiling status registers.
- When the PE is in Debug state, there are synchronization requirements for the Debug Communication Channel and Instruction Transfer registers. See DCC and ITR access in Debug state.

## Note

- The provision of explicit synchronization requirements to System registers is provided to allow the direct access to these registers to be implemented in a small number of cycles, and that updates to multiple registers can be performed quickly with the synchronization penalty being paid only when the updates have occurred.
- Since toolkits might use registers such as the thread-local storage registers within compiled code, it is recommended that access to these registers is implemented to take a small number of cycles.
- While no synchronization is required between a direct write and a direct read, or between a direct read and an indirect write, this does not imply that a direct read causes synchronization of a previous direct write. That is, the sequence direct write → direct read → indirect read, with no intervening context synchronization, does not guarantee that the indirect read observes the result of the direct write.
- If FEAT\_MTE\_ASYNC is implemented, one of the following is required between an indirect write to TFSRE0\_EL1, or any TFSR\_ELx accessible at ELy, and a direct read or direct write of that register:
- -A DSB instruction with the LD qualifier, or neither the LD nor ST qualifier.
- -An exception entry to ELy with SCTLR\_ELy.ITFSB set to 1.

## D24.1.3 Principles of the ID scheme for fields in ID registers

The Arm architecture specifies a number of ID registers that are characterized as comprising a set of 4-bit ID fields, Each ID field identifies the presence, and possibly the level of support for, a particular feature in an implementation of

the architecture. These fields follow an architectural model that aids their use by software and provides future compatibility. This section describes that model. ID registers to which this scheme applies identifies the set of ID registers.

Asmall number of ID fields do not follow the scheme described in this section. In these cases, the field description states that it does not follow this scheme.

Note

- The ID fields described here are unlike the ones that enumerate the number of resources, such as the number of breakpoints, watchpoints, or performance monitors.
- ID fields that do not follow this scheme include the ID\_AA64DFR0\_EL1.PMUVer, ID\_DFR0\_EL1.PerfMon, ID\_DFR0.PerfMon and EDDFR.PMUVer fields, see Alternative ID scheme used for the Performance Monitors Extension version.
- The presence of an ID field for a feature does not imply that the feature is optional.

To provide forward compatibility, software can rely on the features of these fields that are described in this section.

The ID fields, which are either signed or unsigned, use increasing numerical values to indicate increases in functionality. Therefore, for an unsigned ID field, if the value 0x1 indicates the presence of some instructions, then the value 0x2 will indicate the presence of those instructions plus some additional instructions or functionality. This means software can be written in the form:

```
if (value >= number) { // do something that relies on the value of the feature }
```

For ID fields where the value 0x0 defines that a feature is not present, the field holds an unsigned value. This covers the vast majority of such fields.

In a few cases, the architecture has been changed to permit implementations to exclude a feature that has previously been required and for which no ID field has been defined. In these cases, a new ID field is defined and:

- The field holds a signed value.
- The field value 0x0 indicates that the feature is implemented.
- The field value 0xF indicates that the feature is not implemented.
- Increasingly negative values indicate additional aspects of the architecture that are not implemented as a result of the feature not being implemented.
- Software that depends on the feature can use the test:

```
if value >= 0 { // Software features that depend on the presence of the hardware }
```

```
feature
```

In some cases, it has been decided retrospectively that the increase in functionality between two consecutive numerical values is too great, and it is desirable to permit an intermediate degree of functionality, and the means to discover this. This is done by the introduction of a fractional field that both:

- Is referred to in the definition of the original field.
- Applies only when the original field is at the lower value of the step.

In principle, a fractional field can be used for two different fractional steps, with different meanings associated with each of these steps. For this reason, a fractional field must be interpreted in the context of the field to which it relates and the value of that field. Example D24-1 shows the use of such a field.

Example D24-1 Example of the use of a fractional field

For a field describing some class of functionality:

- The value 0x1 was defined as indicating that item A is present.
- The value 0x2 was defined as indicating that items B and C are present, in addition to item A.

Subsequently, it might be necessary to introduce a second ID field to indicate that A and B only are present. This new field is a fractional field, and might be defined as having the value 0x1 when A and B only are present. This fractional field is valid only when the original ID field has the value 0x1 .

This approach means that:

- Software that depends on the test if (value &gt;= 0x2) can rely on features A, B, and C being present,
- Software that depends on the test if (value &gt;= 0x1) can rely on feature A being present.
- If new software needs to check only that features A and B are present, then it can test:

```
if (value >= 0x2 || (value == 0x1 && fractional_value >= 0x1)) { // Software features that depend on A and B only }
```

Afractional field uses the same approach of increasing numerical values indicating increasing functionality, and the fractional approach can also be applied recursively to fractional fields.

Unused ID fields, and fractional fields that are not applicable, are RES0 to allow their future use when features, or fractional implementation options, are added.

## D24.1.3.1 ID registers to which this scheme applies

This scheme applies to the following registers:

## AArch64 System registers

- The AArch64 views of the AArch32 feature ID registers given by:
- -The AArch32 Auxiliary Feature register ID\_AFR0\_EL1.
- -The AArch32 Processor Feature registers ID\_PFR0\_EL1, ID\_PFR1\_EL1, and ID\_PFR2\_EL1.
- -The AArch32 Debug Feature register ID\_DFR0\_EL1 and ID\_DFR1\_EL1.
- -The AArch32 Memory Model Feature registers ID\_MMFR0\_EL1, ID\_MMFR1\_EL1, ID\_MMFR2\_EL1, ID\_MMFR3\_EL1, ID\_MMFR4\_EL1, and ID\_MMFR5\_EL1.
- -The AArch32 Instruction Set Attribute registers ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1, ID\_ISAR5\_EL1, and ID\_ISAR6\_EL1.
- -The AArch32 Media and VFP Feature registers MVFR0\_EL1, MVFR1\_EL1, and MVFR2\_EL1.
- The AArch64 Auxiliary Feature registers ID\_AA64AFR0\_EL1 and ID\_AA64AFR1\_EL1.
- The AArch64 Processor Feature registers ID\_AA64PFR0\_EL1, ID\_AA64PFR1\_EL1, and ID\_AA64PFR2\_EL1.
- The AArch64 Debug Feature registers ID\_AA64DFR0\_EL1, ID\_AA64DFR1\_EL1, and ID\_AA64DFR2\_EL1.
- The AArch64 Memory Model Feature registers ID\_AA64MMFR0\_EL1, ID\_AA64MMFR1\_EL1, ID\_AA64MMFR2\_EL1, ID\_AA64MMFR3\_EL1, and ID\_AA64MMFR4\_EL1.
- The AArch64 Instruction Set Attribute registers ID\_AA64ISAR0\_EL1, ID\_AA64ISAR1\_EL1, ID\_AA64ISAR2\_EL1, and ID\_AA64ISAR3\_EL1.
- The AArch64 SVE Feature ID register ID\_AA64ZFR0\_EL1.

## AArch32 System registers

- The AArch32 Auxiliary Feature register ID\_AFR0.
- The AArch32 Processor Feature registers ID\_PFR0, ID\_PFR1, and ID\_PFR2.
- The AArch32 Debug Feature register ID\_DFR0 and ID\_DFR1.
- The AArch32 Memory Model Feature registers ID\_MMFR0, ID\_MMFR1, ID\_MMFR2, ID\_MMFR3, ID\_MMFR4, and ID\_MMFR5.
- The AArch32 Instruction Set Attribute registers ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, ID\_ISAR4, ID\_ISAR5, and ID\_ISAR6.
- The AArch32 Media and FP Feature registers MVFR0, MVFR1, and MVFR2.

## Memory-mapped registers

- The External Debug Processor Feature register EDPFR.
- The External Debug Feature register EDDFR, EDDFR1, and EDDFR2.
- The External Debug Auxiliary Processor Feature register EDAA32PFR.

## D24.1.3.2 Alternative ID scheme used for the Performance Monitors Extension version

The ID\_AA64DFR0\_EL1.PMUVer, ID\_DFR0\_EL1.PerfMon, ID\_DFR0.PerfMon and EDDFR.PMUVer fields, that identify the version of the Performance Monitors Extension, do not follow the standard ID scheme. Software must treat these fields as follows:

- The value 0xF indicates that the Arm-architected Performance Monitors Extension is not implemented.
- If the field value is not 0xF , the field is treated as an unsigned value, as described for the standard ID scheme.

This means that software that depends on the implementation of a particular version of the Arm Performance Monitors Extension must be written in the form:

```
if (value != 0xF and value >= number) { // do something that relies on version 'number' of the feature }
```

For these fields, Arm deprecates use of the value 0xF in new implementations.

## D24.1.3.3 Alternative ID scheme used for ID\_AA64MMFR0\_EL1 stage 2 granule sizes

The ID\_AA64MMFR0\_EL1.{TGran4\_2, TGran64\_2, TGran16\_2} fields that identify the memory translation stage 2 granule size, do not follow the standard ID scheme. Software must treat these fields as follows:

- The value 0x0 indicates that support is identified by another field.
- If the field value is not 0x0 , the value indicates the level of support provided.

This means that software should use a test of the form:

```
if (field !=0 and field > value) { // do something that relies on the value of the feature }
```

## D24.1.3.4 Alternative ID scheme used for ID\_AA64SMFR0\_EL1 and ID\_AA64FPFR0\_EL1

Apart from the ID\_AA64SMFR0\_EL1.SMEver field, which is a 4-bit unsigned integer conforming to the standard scheme, software must treat the other fields in these registers as follows:

- A1-bit field value where the bit is 0b0 indicates that the specified feature or instructions described by this field are not implemented.
- A1-bit field value where the bit is 0b1 indicates that the specified feature or instructions described by this field are implemented.
- In ID\_AA64SMFR0\_EL1, a 4-bit field indicates whether a group of related SME instructions is implemented, with permitted values defined in the field description. Bits within such a field which only permit the value 0b0000 might be used to identify new instructions in a future version of SME, without changing the meaning of those bits that permit the value 0b0001 .