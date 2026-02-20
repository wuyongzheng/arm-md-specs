## G8.1 About the AArch32 System registers

For general information about the AArch32 System registers, see:

## In The AArch32 Virtual Memory System Architecture:

- About the System registers for VMSAv8-32.
- Functional grouping of VMSAv8-32 System registers.

## In AArch32 System Register Encoding:

- Organization of registers in the ( coproc == 0b1110 ) encoding space.
- Organization of registers in the ( coproc == 0b1111 ) encoding space.
- Fixed values in the System register descriptions.
- General behavior of System registers.
- Principles of the ID scheme for fields in ID registers.
- About AArch32 System register accesses.

The remainder of this chapter describes the AArch32 System registers, in the following sections:

- General system control registers.
- Debug registers.
- Performance Monitors registers.
- Generic Timer registers.

## G8.1.1 Fixed values in the System register descriptions

See Fixed values in AArch32 instruction and System register descriptions. This section defines how the glossary terms RAZ, RES0, RAO, and RES1 can be represented in the System register descriptions.

## G8.1.2 General behavior of System registers

Except where indicated, System registers are 32-bits wide. As stated in About the System registers for VMSAv8-32, there are some 64-bit registers, and these include cases where software can access either a 32-bit view or a 64-bit view of a register. The register summaries, and the individual register descriptions, identify the 64-bit registers and how they can be accessed.

The following sections give information about the general behavior of these registers:

- Register names.
- Read-only bits in read/write registers.
- The CPUID identification scheme.
- IMPLEMENTATION DEFINED performance monitors.
- UNPREDICTABLE, CONSTRAINED UNPREDICTABLE, and UNDEFINED behavior for AArch32 System register accesses.
- Read-only and write-only register encodings.
- Reset behavior of AArch32 System registers.
- Synchronization of changes to AArch32 System registers.

Unless otherwise indicated, information in the listed sections applies to all AArch32 System registers

See also About AArch32 System register accesses.

## In this chapter:

## G8.1.2.1 Register names

The Arm architecture guarantees not to define any register name prefixed with IMP\_ as part of the standard Arm architecture.

Note

Arm strongly recommends that any register names created in the IMPLEMENTATION DEFINED register spaces be prefixed with IMP\_ , where appropriate.

## G8.1.2.2 Read-only bits in read/write registers

Some read/write registers include bits that are read-only. These bits ignore writes.

## G8.1.2.3 The CPUID identification scheme

The ID\_* registers were originally called the CPUID identification scheme registers. However, functionally, there is no value in separating these registers from the slightly larger Identification registers functional group. See Table K14-30 for a list of the ID\_ * registers.

## G8.1.2.4 IMPLEMENTATION DEFINED performance monitors

VMSAv8-32 reserves some additional System register encodings in the ( coproc == 0b1111 ) encoding space for optional additional IMPLEMENTATION DEFINED performance monitors. Table G8-1 shows the allocation of these encodings:

Table G8-1 Performance Monitors System register encoding allocations

| CRn   | opc1   | CRm     | opc2   | Name                                                                         | Type     |
|-------|--------|---------|--------|------------------------------------------------------------------------------|----------|
| c9    | 0-7    | c12-c14 | 0-7    | Performance Monitors Extension registers, see Performance monitors registers | RWorRO a |
|       |        | c15     | 0-7    | IMPLEMENTATION DEFINED                                                       | b        |

## G8.1.2.5 UNPREDICTABLE,CONSTRAINEDUNPREDICTABLE,andUNDEFINEDbehaviorforAArch32System register accesses

This section defines UNPREDICTABLE and UNDEFINED behaviors for accesses to System registers, including those cases where the Armv8 behavior is CONSTRAINED UNPREDICTABLE.

In AArch32 state, the following operations are UNDEFINED:

- All LDC and STC accesses, except for the LDC access to DBGDTRTXint and the STC access to DBGDTRRXint specified in Table G7-2.
- All MCRR and MRRC operations to the ( coproc == 0b111x ) encoding space, except for those explicitly defined as accessing 64-bit System registers specified in Table G7-1 and Table G7-3.

Unless otherwise indicated in the individual register descriptions:

- Reserved fields in registers are RES0.
- Assigning a reserved value to a field has a CONSTRAINED UNPREDICTABLE effect, see Reserved values in System and memory-mapped registers and translation table entries.

The following subsections give more information about UNPREDICTABLE, CONSTRAINED UNPREDICTABLE, and UNDEFINED behavior for accesses to the ( coproc == 0b111x ) encoding space:

- Accesses to unallocated encodings in the ( coproc == 0b111x ) encoding space.
- Additional rules for MCR and MRC accesses to System registers.
- Effects of EL3 and EL2 on System register accesses.

## G8.1.2.5.1 Accesses to unallocated encodings in the ( coproc == 0b111x ) encoding space

In Armv8-A, accesses to unallocated register encodings in the ( coproc == 0b111x ) encoding space are UNDEFINED.

Note

In Armv7, except for 32-bit registers encoded with a CRn value of c12 , accesses to unallocated 32-bit registers were UNPREDICTABLE. The Armv8 CONSTRAINED UNPREDICTABLE behavior of these accesses is that they are UNDEFINED, see Unallocated System register access instructions.

## G8.1.2.5.2 Additional rules for MCR and MRC accesses to System registers

The following operations are CONSTRAINED UNPREDICTABLE for all encodings in the ( coproc == 0b111x ) encoding space:

- All MCR operations from the PC.
- All MRC operations to APSR\_nzcv , except for the ( coproc == 0b1110 ) MRC operation to APSR\_nzcv from DBGDSCRint.

The CONSTRAINED UNPREDICTABLE behavior of these operations is described in Using R15 by instruction.

For registers and operations that are accessible from a particular Privilege level, any attempt to access those registers from a lower Privilege level is UNDEFINED.

Some individual registers can be made inaccessible by setting configuration bits, possibly including IMPLEMENTATION DEFINED configuration bits, to disable access to the register. The effects of the architecturally-defined configuration bits are defined individually in this manual. Unless explicitly stated otherwise in this manual, setting a configuration bit to disable access to a register results in the register becoming UNDEFINED for MRC and MCR accesses.

See also Read-only and write-only register encodings.

## G8.1.2.5.3 Effects of EL3 and EL2 on System register accesses

EL2 and EL3 introduce classes of System registers, described in Classification of System registers. Some of these classes of register are either:

- Accessible only from certain modes or states.
- Accessible from certain modes or states only when configuration settings permit the access.

Accesses to these registers that are not permitted are UNDEFINED, meaning execution of the register access instruction generates an Undefined Instruction exception.

Note

This section applies only to registers that are accessible from some modes and states. That is, it applies only to register access instructions using an encoding that, under some circumstances, would perform a valid register access.

The following register classes restrict access in this way:

## Restricted access System registers

This register class is defined in any implementation that includes EL3.

Restricted access registers other than the NSACR are accessible only from Secure EL3 modes. All other accesses to these registers are UNDEFINED.

The NSACR is a special case of a Restricted access register and:

- The NSACR is:
- -Read/write accessible from Secure PL1 modes.
- -Is Read-only accessible from Non-secure PL2 and PL1 modes.
- All other accesses to the NSACR are UNDEFINED.

For more information, including behavior when EL3 is using AArch64 or is not implemented, see Restricted access System registers.

## Configurable access System registers

This register class is defined in any implementation that includes EL3.

Most Configurable access registers are accessible from Non-secure state only if control bits in the NSACRpermit Non-secure access to the register. Otherwise, a Non-secure access to the register is UNDEFINED.

For other Configurable access registers, control bits in the NSACR control the behavior of bits or fields in the register when it is accessed from Non-secure state. That is, Non-secure accesses to the register are permitted, but the NSACR controls how they behave. The only architecturally-defined register of this type is the CPACR.

For more information, see Configurable access System registers.

## EL2-mode System registers

This register class is defined only in an implementation that includes EL2.

EL2-mode registers are accessible only from:

- The Non-secure EL2 mode, Hyp mode.
- Secure Monitor mode when SCR.NS is set to 1.

All other accesses to these registers are UNDEFINED.

For more information, see Hyp mode read/write registers in the ( coproc == 0b1111 ) encoding space and Hyp mode encodings for shared ( coproc == 0b1111 ) System registers.

## EL2-mode write-only operations

This register class is defined only in an implementation that includes EL2.

EL2-mode write-only operations are accessible only from:

- The Non-secure EL2 mode, Hyp mode.
- Secure Monitor mode, regardless of the value of SCR.NS.

Write accesses to these operations are:

- CONSTRAINED UNPREDICTABLE in Secure EL3 modes other than Monitor mode.
- UNDEFINED in Non-secure modes other than Hyp mode.

For more information, see Hyp mode ( coproc == 0b1111 ) write-only System instructions.

In addition, in any implementation that includes EL3, when EL3 is using AArch32, if write access to a register is disabled by the CP15SDISABLE signal then any MCR access to that register is UNDEFINED.

## G8.1.2.6 Read-only and write-only register encodings

Some System registers are read-only (RO) or write-only (WO). For example:

- Most identification registers are read-only.
- Most encodings that perform an operation, such as a cache maintenance instruction, are write-only.

If a particular Privilege level defines a register to be:

- RO, then any attempt to write to that register, at that Privilege level, is UNDEFINED. This means that any access to that register with L == 0 is UNDEFINED.
- WO, then any attempt to read from that register, at that Privilege level, is UNDEFINED. This means that any access to that register with L== 1 is UNDEFINED.

For IMPLEMENTATION DEFINED encoding spaces, the treatment of the encodings is IMPLEMENTATION DEFINED.

Note

This section applies only to registers that this manual defines as RO or WO. It does not apply to registers for which other access permissions are explicitly defined.

## G8.1.2.7 Reset behavior of AArch32 System registers

Reset values apply only to RW registers and fields, however:

- Some RO registers or fields, including feature ID registers and some status registers or register fields, always return a known value.
- Some RW and RO registers or register fields return status information about the PE. Unless the register description indicates that the value is UNKNOWN on reset, a read of the register immediately after a reset returns valid information.
- Some RW and RO registers and fields are aliases of other registers or fields. In these cases, the reset behavior of the aliased register or field determines the value returned by a read of the register immediately after a reset.
- WOregisters that only have an effect on writes do not have meaningful reset values. However, an access to a WOregister might affect underlying state, and that state might have a defined reset value.
- IMPLEMENTATION DEFINED registers have IMPLEMENTATION DEFINED reset behavior.

After a reset, only a limited subset of the PE state is guaranteed to be set to defined values. Also, for debug and trace System registers, reset requirements must take account of different levels of reset. For more information about the reset behavior of System registers when the PE resets into an Exception level that is using AArch32, see:

- PE state on reset into AArch32 state.
- The appropriate Trace architecture specification, for the Trace System registers.

When the PE resets into an Exception level that is using AArch64, PE state that relates to execution in AArch32 state, including the System register values, is UNKNOWN. The only exception to this is state that applies to execution in both AArch64 state and AArch32 state and that has a defined reset value on the reset into AArch64 state. An example of such PE state is the EDPRSR.SR bit.

For a PE reset into an Exception level that is using AArch32, the architecture defines which AArch32 System registers have a defined reset value, and when that defined reset value applies. The register descriptions include this information, and PE state on reset into AArch32 state summarizes these architectural requirements. Otherwise, RW registers reset to an architecturally unknown value.

Note

In an implementation that includes EL3, unless this manual explicitly states otherwise, only the Secure instance of a banked register is reset to the defined value. This means that software must program the Non-secure instance of the register with the required values. Typically, this programming is part of the PE boot sequence.

## G8.1.2.7.1 Pseudocode description of resetting System registers

The AArch32.ResetControlRegisters() pseudocode function resets all System registers, and register fields, that have defined reset values, as described in this section and PE state on reset into AArch32 state.

Note

For debug and trace System registers, this function resets registers as defined for the appropriate level of reset.

## G8.1.2.8 Synchronization of changes to AArch32 System registers

In this section, this PE means the PE on which accesses are being synchronized.

Note

See Definitions of direct and indirect reads and writes and their side-effects for definitions of the terms direct write , direct read , indirect write , and indirect read .

A direct write to a System register might become visible at any point after the change to the register, but without a Context Synchronization event there is no guarantee that the change becomes visible.

Any direct write to a System register is guaranteed not to affect any instruction that appears, in program order, before the instruction that performed the direct write, and any direct write to a System register must be synchronized before any instruction that appears after the direct write, in program order, can rely on the effect of that write. The only exceptions to this are:

- All direct writes to the same register, using the same encoding, are guaranteed to occur in program order.
- All direct writes to a register are guaranteed to occur in program order relative to all direct reads of the same register using the same encoding.
- Any System register access that an Arm Architecture Specification or equivalent specification defines as not requiring synchronization.
- If an instruction that appears in program order before the direct write performs a memory access, such as a memory-mapped register access, that causes an indirect read or write to a register, that memory access is subject to the memory order model. In this case, if permitted by the memory order model, the instruction that appears in program order before the direct write can be affected by the direct write. For information about the memory order model, see Definition of the memory model.

These rules mean that an instruction that writes to one of the address translation instructions described in Address translation instructions must be explicitly synchronized to guarantee that the result of the address translation instruction is visible in the PAR.

Note

In this case, the direct write to the encoding of the address translation instruction causes an indirect write to the PAR. Without a Context Synchronization event after the direct write, there is no guarantee that the indirect write to the PAR is visible.

Conceptually, the explicit synchronization occurs as the first step of any Context Synchronization event. This means that if the operation uses the state that had been changed but not synchronized before the operation occurred, the operation is guaranteed to use the state as if it had been synchronized.

Note

- This explicit synchronization is applied as the first step of the execution of any instruction that causes the synchronization operation. This means it does not synchronize any effect of changes to the System registers that might affect the fetch and decode of the instructions that cause the operation, such as breakpoints or changes to translation tables.

- For a synchronous exception, the control state in use at the time the exception is generated determines the exception syndrome information, and this syndrome information is not changed by this synchronization at the start of taking the exception.

Except for the register reads listed in Registers with some architectural guarantee of ordering or observability, if no Context Synchronization event is performed, direct reads of System registers can occur in any order.

Table G8-2 shows the synchronization requirement between two reads or writes that access the same System register. In the column headings, First and Second refer to:

- Program order, for any read or write caused by the execution of an instruction by this PE, other than a read or write caused by a memory access made by that instruction.
- The order of arrival of asynchronous reads or writes made by this PE relative to the execution of instructions by this PE.

## In addition:

- For indirect reads or writes caused by an external agent, such as a debugger, the mechanism that determines the order of the reads or writes is defined by that external agent. The external agent can provide mechanisms that ensure that any read or write it makes arrives at the PE. These indirect reads and writes are asynchronous to software execution on the PE.
- For indirect reads or writes caused by memory-mapped reads or writes made by this PE, the ordering of the memory accesses is subject to the memory order model, including the effect of the memory type of the accessed memory address. This applies, for example, if this PE reads or writes one of its registers in a memory-mapped register interface.

The mechanism for ensuring completion of these memory accesses, including ensuring the arrival of the asynchronous read or write at the PE, is defined by the system.

Note

Such accesses are likely to be given a Device memory attribute, but requiring this is outside the scope of the architecture.

- For indirect reads or writes caused by autonomous asynchronous events that are counted, for example events caused by the passage of time, the events are ordered so that:
- -Counts progress monotonically.
- -The events arrive at the PE in finite time and without undue delay.

Table G8-2 Synchronization requirements for updates to System registers

| First read or write   | Second read or write   | Context Synchronization event required             |
|-----------------------|------------------------|----------------------------------------------------|
| Direct read           | Direct read            | No                                                 |
| Direct read           | Direct write           | No                                                 |
| Direct read           | Indirect read          | No a                                               |
| Direct read           | Indirect write         | No a , but see text in this section for exceptions |
| Direct write          | Direct read            | No                                                 |
| Direct write          | Direct write           | No                                                 |
| Direct write          | Indirect read          | Yes a                                              |
| Direct write          | Indirect write         | No, but see text in this section for exceptions    |
| Indirect read         | Direct read            | No                                                 |
| Indirect read         | Direct write           | No                                                 |
| Indirect read         | Indirect read          | No                                                 |
| Indirect read         | Indirect write         | No                                                 |
| Indirect write        | Direct read            | Yes, but see text in this section for exceptions   |
| Indirect write        | Direct write           | No, but see text in this section for exceptions    |
| Indirect write        | Indirect read          | Yes, but see text in this section for exceptions   |
| Indirect write        | Indirect write         | No, but see text in this section for exceptions    |

a. Although no synchronization is required between a Direct write and a Direct read, or between a Direct read and an Indirect write, this does not imply that a Direct read causes synchronization of a previous Direct write. This means that the sequence Direct write followed by Direct read followed by Indirect read, with no intervening context synchronization, does not guarantee that the Indirect read observes the result of the Direct write.

If the indirect write is to a register that Registers with some architectural guarantee of ordering or observability shows as having some guarantee of the visibility of an indirect write, synchronization might not be required.

If a direct read or a direct write to a register is followed by an indirect write to that register that is caused by an external agent, or by an autonomous asynchronous event, or as a result of a memory-mapped write, then synchronization is required to guarantee the ordering of the indirect write relative to the direct read or direct write.

If an indirect write caused by a direct write is followed by an indirect write caused by an external agent, or by an autonomous asynchronous event, or as a result of a memory-mapped write, then synchronization is required to guarantee the ordering of the two indirect writes.

Where an indirect write occurs as a side-effect of an access, this happens atomically with the access, meaning no other accesses are allowed between the register access and its side-effect. For other information about indirect writes after a direct read or a direct write, see Definitions of direct and indirect reads and writes and their side-effects.

Note

Where a register has more that one encoding, a direct write to the register using a particular encoding is not an indirect write to the same register with a different encoding.

Where an indirect write is caused by the action of an external agent, such as a debugger, or by a memory-mapped read or write by the PE, then an indirect write by that agent to a register using a particular access mechanism, followed by an

indirect read by that agent to the same register using the same access mechanism and address does not need synchronization.

Without explicit synchronization to guarantee the order of the accesses, where the same register is accessed by two or more of a System register access instruction, and external agent, and autonomous asynchronous event, or as a result of a memory-mapped access, the behavior must be as if the accesses occurred atomically and in any order. This applies even if the accesses occur simultaneously.

For information about the additional synchronization requirements for memory-mapped registers, see Synchronization requirements for AArch64 System registers.

To guarantee the visibility of changes to some registers, additional operations might be required before the Context Synchronization event. For such a register, the definition of the register identifies these additional requirements.

In this manual, unless the context indicates otherwise:

- Accessing a System register refers to a direct read or write of the register.
- Using a System register refers to an indirect read or write of the register.

## G8.1.2.8.1 Registers with some architectural guarantee of ordering or observability

For the registers for which Table G8-3 shows that the ordering of direct reads is guaranteed, multiple direct reads of a single register, using the same encoding, occur in program order without any explicit ordering.

For the registers for which Table G8-3 shows that some observability of indirect writes is guaranteed, an indirect write to the register caused by an external agent, an autonomous asynchronous event, or as a result of a memory-mapped write, is both:

- Observable to direct reads of the register, in finite time, without explicit synchronization.
- Observable to subsequent indirect reads of the register without explicit synchronization.

These two sets of registers are similar, as Table G8-3 shows:

Table G8-3 Registers with a guarantee of ordering or observability, VMSAv8-32

| Register                   | Ordering of direct reads   | Observability of indirect writes   | Notes                                                                                  |
|----------------------------|----------------------------|------------------------------------|----------------------------------------------------------------------------------------|
| ISR                        | Guaranteed                 | Guaranteed                         | Interrupt Status Register                                                              |
| DBGCLAIMCLR                | Guaranteed                 | Guaranteed                         | Debug CLAIM registers                                                                  |
| DBGCLAIMSET                | -                          | Guaranteed                         |                                                                                        |
| DBGDTRRXint                | Guaranteed                 | Guaranteed                         | Debug Communication Channel registers                                                  |
| DBGDTRTXint                | -                          | Guaranteed                         |                                                                                        |
| The DCCflags in DBGDSCRint | Guaranteed                 | Guaranteed                         |                                                                                        |
| CNTPCT                     | Guaranteed                 | Guaranteed                         | Generic Timer registers                                                                |
| CNTP_TVAL                  | Guaranteed                 | Guaranteed                         |                                                                                        |
| CNTVCT                     | Guaranteed                 | Guaranteed                         |                                                                                        |
| CNTV_TVAL                  | Guaranteed                 | Guaranteed                         |                                                                                        |
| CNTHP_TVAL                 | Guaranteed                 | Guaranteed                         |                                                                                        |
| PMCCNTR                    | Guaranteed                 | Guaranteed                         | Performance Monitors Extension registers, if the implementation includes the extension |
| PMEVCNTR<n>                | Guaranteed                 | Guaranteed                         |                                                                                        |
| PMXEVCNTR                  | Guaranteed                 | Guaranteed                         |                                                                                        |
| PMOVSSET                   | Guaranteed                 | Guaranteed                         |                                                                                        |

| Register                                | Ordering of direct reads   | Observability of indirect writes   | Notes                                                    |
|-----------------------------------------|----------------------------|------------------------------------|----------------------------------------------------------|
| PMOVSR                                  | Guaranteed                 | Guaranteed                         |                                                          |
| EDSCR.PipeAdv and theDCC flags in EDSCR | -                          | Guaranteed                         | Fields of the External Debug Status and Control Register |

In addition to the requirements shown in Table G8-3:

- Indirect writes to the following registers as a result of memory-mapped writes, including accesses by external agents, are required to be observable to the indirect read made in determining the response to a subsequent memory-mapped access without explicit synchronization:

- -

- OSLAR\_EL1. OSLAR\_EL1 is indirectly read to determine whether the subsequent access is permitted. Note OSLAR\_EL1 maps to the AArch32 System register DBGOSLAR.

- EDLAR, if implemented. EDLAR is indirectly read to determine whether a subsequent write or side-effect of an access is ignored.

Note

This requirement is stricter than the general requirement for the observability of indirect writes.

- The requirement that an indirect write to the registers in Table G8-3 is observable to direct reads in finite time does not imply that all observers will observe the indirect write at the same time. For example, an increment of the system counter is an autonomous asynchronous event that performs an indirect write to the counter. This asynchronous event might generate a timer interrupt request, resulting in a Context Synchronization event. When a GIC is used, the timer interrupt might arrive at the GIC after the PE has taken an interrupt request from another source, but before software reads the current interrupt ID from the GIC. This means that the GIC might identify the timer interrupt as the current interrupt. Software must not assume that a subsequent direct read of the counter register is guaranteed to observe the updated value of that register. Although this example uses the counter-timer registers, it applies equally to other registers that might be linked to interrupt requests, including the PMU and Statistical Profiling status registers.
- •
- When the PE is in Debug state, there are synchronization requirements for the Debug Communication Channel and Instruction Transfer registers. See DCC and ITR access in Debug state.

The possibility that direct reads can occur early , in the absence of context synchronization, described in Ordering of reads of System registers, still applies to the registers listed in Table G8-3.

## G8.1.2.8.2 Definitions of direct and indirect reads and writes and their side-effects

Direct and indirect reads and writes are defined as follows:

## Direct read

## Direct write

Is a read of a register, using an MRC , MRRC , or STC instruction, that the architecture permits for the current PE state.

If a direct read of a register has a side-effect of changing the value of a register, the effect of a direct read on that register is defined to be an indirect write , and has the synchronization requirements of an indirect write. This means the indirect write is guaranteed to have occurred, and to be visible to subsequent direct or indirect reads and writes only if synchronization is performed after the direct read.

Note

The indirect write described here can affect either the register written to by the direct write, or some other register. The synchronization requirement is the same in both cases.

Is a write to a register, using an MCR , MCRR , or LDC instruction, that the architecture permits for the current PE state.

In the following cases, the side-effect of the direct write is defined to be an indirect write of the affected register, and has the synchronization requirements of an indirect write:

## Indirect read

- If the direct write has a side-effect of changing the value of a register other than the register accessed by the direct write.
- If the direct write has a side-effect of changing the value of the register accessed by the direct write, so that the value in that register might not be the value that the direct write wrote to the register.

In both cases, this means that the indirect write is not guaranteed to be visible to subsequent direct or indirect reads and writes unless synchronization is performed after the direct write.

Note

- As an example of a direct write to a register having an effect that is an indirect write of that register, writing 1 to a PMCNTENCLR.P x bit is also an indirect write, because if the P x bit had the value 1 before the direct write, the side-effect of the write changes the value of that bit to 0.
- The indirect write described here can affect either the register written to by the direct write, or some other register. The synchronization requirement is the same in both cases.

For example, writing 1 to a PMCNTENCLR.P x bit that is set to 1 also changes the corresponding PMCNTENSET.P x bit from 1 to 0. This means that the direct write to the PMCNTENCLR defines indirect writes to both itself and to the PMCNTENSET.

Is a use of the register by an instruction to establish the operating conditions for the instruction. Examples of operating conditions that might be determined by an indirect read are the translation table base address, or whether memory accesses are forced to be Non-cacheable.

Indirect reads include situations where the value of one register determines what value is returned by a second register. This means that any read of the second register is an indirect read of the register that determines what value is returned.

Indirect reads also include:

- Reads of the System registers by external agents, such as debuggers, as described in Debug registers.
- Memory-mapped reads of the System registers made by the PE on which the System registers are implemented.

Where an indirect read of a register has a side-effect of changing the value of a register, that change is defined to be an indirect write, and has the synchronization requirements of an indirect write.

Indirect write Is an update to the value of a register as a consequence of either:

- An exception, operation, or execution of an instruction that is not a direct write to that register.
- The asynchronous operation of an external agent.

This can include:

- The passage of time, as seen in counters or timers, including performance counters.
- The assertion of an interrupt.
- Awrite from an external agent, such as a debugger.

However, for some registers, the architecture gives some guarantee of visibility without any explicit synchronization, see Registers with some architectural guarantee of ordering or observability.

Note

Taking an exception is a Context Synchronization event. Any indirect write performed as part of an exception entry does not require additional synchronization. This includes the indirect writes to the registers that report the exception, as described in Exception reporting in a VMSAv8-32 implementation.

## G8.1.3 Principles of the ID scheme for fields in ID registers

The Arm architecture specifies a number of ID registers that are characterized as comprising a set of 4-bit ID fields, Each ID field identifies the presence, and possibly the level of support for, a particular feature in an implementation of the architecture. These fields follow an architectural model that aids their use by software and provides future

compatibility. This section describes that model. AArch32 ID registers to which this scheme applies identifies the set of ID registers that are accessible from AArch32 state.

Asmall number of ID fields do not follow the scheme described in this section. In these cases, the field description states that it does not follow this scheme.

## Note

- The ID fields described here are unlike the ones that enumerate the number of resources, such as the number of breakpoints, watchpoints, or performance monitors.
- ID fields that do not follow this scheme include the ID\_AA64DFR0\_EL1.PMUVer, ID\_DFR0\_EL1.PerfMon, ID\_DFR0.PerfMon and EDDFR.PMUVer fields, see Alternative ID scheme used for the Performance Monitors Extension version.
- The presence of an ID field for a feature does not imply that the feature is optional.

To provide forward compatibility, software can rely on the features of these fields that are described in this section.

The ID fields, which are either signed or unsigned, use increasing numerical values to indicate increases in functionality. Therefore, if a value of 0x1 indicates the presence of some instructions, then the value 0x2 will indicate the presence of those instructions plus some additional instructions or functionality. This means software can be written in the form:

```
if (value >= number) { // do something that relies on the value of the feature }
```

For ID fields where the value 0x0 defines that a feature is not present, the field holds an unsigned value. This covers the vast majority of such fields.

In a few cases, the architecture has been changed to permit implementations to exclude a feature that has previously been required and for which no ID field has been defined. In these cases, a new ID field is defined and:

- The field holds a signed value.
- The field value 0xF indicates that the feature is not implemented.
- The field value 0x0 indicates that the feature is implemented.
- Software that depends on the feature can use the test:

```
if value >= 0 { // Software features that depend on the presence of the hardware feature }
```

In some cases, it has been decided retrospectively that the increase in functionality between two consecutive numerical values is too great, and it is desirable to permit an intermediate degree of functionality, and the means to discover this. This is done by the introduction of a fractional field that both:

- Is referred to in the definition of the original field.
- Applies only when the original field is at the lower value of the step.

In principle, a fractional field can be used for two different fractional steps, with different meanings associated with each of these steps. For this reason, a fractional field must be interpreted in the context of the field to which it relates and the value of that field. Example G8-1 shows the use of such a field.

## Example G8-1 Example of the use of a fractional field

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

## G8.1.3.1 AArch32 ID registers to which this scheme applies

- The Auxiliary Feature register ID\_AFR0.
- The Processor Feature registers ID\_PFR0 and ID\_PFR1.
- The Debug Feature register ID\_DFR0.
- The Memory Model Feature registers ID\_MMFR0, ID\_MMFR1, ID\_MMFR2, ID\_MMFR3, and ID\_MMFR4.
- The Instruction Set Attribute registers ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, ID\_ISAR4, and ID\_ISAR5.
- The Media and VFP Feature registers MVFR0, MVFR1, and MVFR2.

Note

Principles of the ID scheme for fields in ID registers includes information about the AArch64 System registers and the memory-mapped registers to which this scheme applies.

## G8.1.3.2 Alternative ID scheme used for the Performance Monitors Extension version

The ID\_AA64DFR0\_EL1.PMUVer, ID\_DFR0\_EL1.PerfMon, ID\_DFR0.PerfMon, and EDDFR.PMUVer fields, which identify the version of the Performance Monitors Extension, do not follow the standard ID scheme. Software must treat these fields as follows:

- The value 0xF indicates that the Arm-architected Performance Monitors Extension is not implemented.
- If the field value is not 0xF the field is treated as an unsigned value, as described for the standard ID scheme.

This means that software that depends on the implementation of a particular version of the Arm Performance Monitors Extension must be written in the form:

```
if (value != 0xF and value >= number) { // do something that relies on version 'number' }
```

```
of the feature
```

For these fields, Arm deprecates use of the value 0xF in new implementations.

## G8.1.4 About AArch32 System register accesses

The following subsections give more information about accesses to the AArch32 System registers:

- Ordering of reads of System registers.
- Accessing 32-bit System registers.
- Accessing 64-bit System registers.

## G8.1.4.1 Ordering of reads of System registers

Reads of the System registers can occur out of order with respect to earlier instructions executed on the same PE, provided that both:

- Any data dependencies between the instructions, as specified in Synchronization of changes to AArch32 System registers, including read-after-read dependencies, are respected.
- The reads to the register do not occur earlier than the most recent Context Synchronization event to its architectural position in the instruction stream.

Note

In particular, the values read from System registers that hold self-incrementing counts, such as the Performance Monitors counters or the Generic Timer counter or timers, could be accessed from any time after the previous Context Synchronization event. For example, where a memory access is used to communicate a read of such a counter, an ISB must be inserted between the read of the memory location that is known to have returned its data, either as a result of a condition on that data or of the read having completed, and the read of the counter, if it is necessary that the counter returns a count value after the memory communication.

## G8.1.4.2 Accessing 32-bit System registers

Software accesses most 32-bit System registers using the generic MCR and MRC System register access instructions, specifying some or all of the parameters { coproc , CRn , opc1 , CRm , opc2 }, where:

| coproc   | Identifies the primary region of the System register encoding space. Takes one of the values:                                                                                                       | Identifies the primary region of the System register encoding space. Takes one of the values:                                                                                                       |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | p14                                                                                                                                                                                                 | Encoded as 0b1110 .                                                                                                                                                                                 |
|          | p15                                                                                                                                                                                                 | Encoded as 0b1111 .                                                                                                                                                                                 |
| CRn      | Takes a value in the range c0 - c15 , encoded the corresponding 4-bit binary value, 0b0000 - 0b1111                                                                                                 | Takes a value in the range c0 - c15 , encoded the corresponding 4-bit binary value, 0b0000 - 0b1111                                                                                                 |
|          | In the ( coproc == 0b1110 ) encoding space, the opc1 value identifies the System register functional group, and CRn is the most significant identifier for the required register within that group. | In the ( coproc == 0b1110 ) encoding space, the opc1 value identifies the System register functional group, and CRn is the most significant identifier for the required register within that group. |
|          | In the ( coproc == 0b1111 ) encoding space, CRn is the most significant identifier for the required register.                                                                                       | In the ( coproc == 0b1111 ) encoding space, CRn is the most significant identifier for the required register.                                                                                       |
| opc1     | Takes a value in the range 0 - 7, encoded as its 3-bit binary value.                                                                                                                                | Takes a value in the range 0 - 7, encoded as its 3-bit binary value.                                                                                                                                |
|          | In the ( coproc == 0b1110 ) encoding space, the opc1 value identifies the System register functional group, and can take the following values:                                                      | In the ( coproc == 0b1110 ) encoding space, the opc1 value identifies the System register functional group, and can take the following values:                                                      |
|          | 0                                                                                                                                                                                                   | Debug System registers.                                                                                                                                                                             |
|          | 1                                                                                                                                                                                                   | Trace System registers.                                                                                                                                                                             |
|          | 7                                                                                                                                                                                                   | Legacy Jazelle System registers.                                                                                                                                                                    |
|          | In the ( coproc == 0b1111 ) encoding space, opc1 can take any value in the range 0 - 7.                                                                                                             | In the ( coproc == 0b1111 ) encoding space, opc1 can take any value in the range 0 - 7.                                                                                                             |
| CRm      | Takes a value in the range c0 - c15 , encoded the corresponding 4-bit binary value, 0b0000 - 0b1111                                                                                                 | Takes a value in the range c0 - c15 , encoded the corresponding 4-bit binary value, 0b0000 - 0b1111                                                                                                 |
| opc2     | Takes a value in the range 0 - 7, encoded as its 3-bit binary value.                                                                                                                                | Takes a value in the range 0 - 7, encoded as its 3-bit binary value.                                                                                                                                |

- Rt

Ageneral-purpose register to hold a 32-bit value to transfer to or from the System register. Takes a value in the range R0 -R14 , encoded as the corresponding 4-bit binary value, 0b0000 -0b1110 .

This means an MCR or MRC access to a specific 32-bit System register uses:

- Aunique combination of coproc , CRn , opc1 , CRm , and opc2 , to specify the required System register.
- Ageneral-purpose register, Rt , for the transferred 32-bit value.

## See also:

- MCR.
- MRC.

Asmall number of AArch32 debug System registers are accessed using LDC or STC instructions. In these cases, the register to be accessed is identified in the instruction syntax by the use of p14, c5 where:

p14

Identifies that the access is to the ( coproc == 0b1110 ) encoding space.

- c5

Identifies the target debug System register.

See the instruction descriptions:

- LDC(immediate).
- LDC(literal).
- STC.

The only uses of LDC and STC permitted in Armv8-A are:

- An LDC access to load data from memory to DBGDTRTXint, see LDC (immediate) and LDC (literal).
- An STC access to store data to memory from DBGDTRRXint, see STC.

Asmall number of AArch32 System registers are accessed using MRS , MSR , VMRS , or VMSR instructions, see the appropriate register and instruction description for more information, see:

- MRS.
- MSR(immediate),
- MSR(register).
- VMRS.
- VMSR.

## Note

- For example:
- -The APSR, CPSR, and SPSR are accessed using MRS or MSR instructions.
- -The MVFR0, MVFR1, and MVFR2 are accessed using VMRS or VMSR instructions.
- In addition, the banked register forms of the MRS and MSR instructions can be used to access some System registers associated with PE modes other than the mode in which the PE is currently executing, see MRS (Banked register) and MSR (Banked register).

## G8.1.4.3 Accessing 64-bit System registers

Software accesses a 64-bit System register using the generic MCRR and MRRC System register access instructions, specifying the parameters { coproc , CRm , opc1 }, where:

coproc

Identifies the primary region of the System register encoding space. Takes one of the values:

p14 Encoded as 0b1110 .

p15 Encoded as 0b1111 .

|      | p15 Encoded as 0b1111 .                                                                                                                                                                                         |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRm  | Takes a value in the range c0 - c15 , encoded the corresponding 4-bit binary value, 0b0000 - 0b1111                                                                                                             |
|      | In the ( coproc == 0b1110 ) encoding space, the opc1 value identifies the System register functional group, and CRm is the most significant identifier for the required register within that group.             |
|      | In the ( coproc == 0b1111 ) encoding space, CRm is the most significant identifier for the required register.                                                                                                   |
| opc1 | Takes a value in the range 0 - 15, encoded as its 3-bit binary value.                                                                                                                                           |
|      | In the ( coproc == 0b1110 ) encoding space, the opc1 value identifies the System register functional group, and can take the following values:                                                                  |
|      | 0 Debug System registers.                                                                                                                                                                                       |
|      | 1 Trace System registers.                                                                                                                                                                                       |
|      | In the ( coproc == 0b1111 ) encoding space, opc1 can take any value in the range 0 - 15.                                                                                                                        |
| Rt   | Ageneral-purpose register to hold bits[31:0] of the value to transfer to or from the System register. Takes a value in the range R0 - R14 , encoded as the corresponding 4-bit binary value, 0b0000 - 0b1110 .  |
| Rt2  | Ageneral-purpose register to hold bits[63:32] of the value to transfer to or from the System register. Takes a value in the range R0 - R14 , encoded as the corresponding 4-bit binary value, 0b0000 - 0b1110 . |

This means an MCRR or MRRC access to a specific 64-bit System register uses:

- Aunique combination of coproc , CRm and opc1 , to specify the required 64-bit System register.
- Two general-purpose registers, each holding 32 bits of the value to transfer.

This means a PE can access a 64-bit System register using:

- An MCRR instruction to write to a System register, see MCRR.
- An MRRC instruction to read a System register, see MRRC.

When using an MCRR or MRRC instruction the System register access is 64-bit atomic.

Some 64-bit registers also have an MCR and MRC encoding. The MCR and MRC encodings for these registers access the least significant 32 bits of the register. For example, to access the PAR, software can:

- Use the following instructions to access all 64 bits of the register:
- Use the following instructions to access the least-significant 32 bits of the register:

```
MRRC p15, 0, <Rt>, <Rt2>, c7 ; Read 64-bit PAR into Rt (low word) and Rt2 (high word) MCRR p15, 0, <Rt>, <Rt2>, c7 ; Write Rt (low word) and Rt2 (high word) to 64-bit PAR
```

MRC p15, 0, &lt;Rt&gt;, c7, c4, 0 ; Read PAR[31:0] into

MCR p15, 0, &lt;Rt&gt;, c7, c4, 0 ; Write

```
Rt
```

```
Rt to PAR[31:0]
```