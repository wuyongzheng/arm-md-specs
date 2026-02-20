## G1.9 AArch32 state PE modes

Table G1-5 shows the PE modes defined by the Arm architecture, for execution in AArch32 state. In this table:

- The PE mode column gives the name of each mode and the abbreviation used, for example, in the general-purpose register name suffixes used in AArch32 general-purpose registers, the PC, and the Special-purpose registers.
- The Encoding column gives the corresponding PSTATE.M field.
- The Exception level column gives the Exception level at which the mode is implemented, including dependencies on the current Security state and on whether EL3 is using AArch32, see Exception levels.

## Table G1-5 AArch32 PE modes

| PE mode    |     |   Encoding | Security state    | Exception level   | Implemented                          |
|------------|-----|------------|-------------------|-------------------|--------------------------------------|
| User       | usr |      10000 | Both              | EL0               | Always                               |
| FIQ        | fiq |      10001 | Non-secure Secure | EL1 EL1 or EL3 a  | Always                               |
| IRQ        | irq |      10010 | Non-secure Secure | EL1 EL1 or EL3 a  | Always                               |
| Supervisor | svc |      10011 | Non-secure Secure | EL1 EL1 or EL3 a  | Always                               |
| Monitor    | mon |      10110 | Secure            | EL3               | If EL3 implemented and using AArch32 |
| Abort      | abt |      10111 | Non-secure Secure | EL1 EL1 or EL3 a  | Always                               |
| Hyp        | hyp |      11010 | Non-secure        | EL2               | If EL2 implemented and using AArch32 |
| Undefined  | und |      11011 | Non-secure Secure | EL1 EL1 or EL3 a  | Always                               |
| System     | sys |      11111 | Non-secure Secure | EL1 EL1 or EL3 a  | Always                               |

Note

FEAT\_SEL2 is not supported if EL2 is using AArch32.

Mode changes can be made under software control, or can be caused by an external or internal exception.

## G1.9.1 Notes on the AArch32 PE modes

PE modes are defined only in AArch32 state. Because each mode is implemented as part of a particular Exception level that is using AArch32, the set of available modes depends on which Exception levels are implemented and using AArch32, as described in Effect of the EL3 Execution state on the PE modes and Exception levels.

This section gives more information about each of the modes, when it is implemented.

## User mode

Software executing in User mode executes at EL0. Execution in User mode is sometimes described as unprivileged execution. Application programs normally execute in User mode, and any program executed in User mode:

- Makes only unprivileged accesses to system resources, meaning it cannot access protected system resources.

## System mode

## Abort mode

## Undefined mode

## FIQ mode

## IRQ mode

## Hyp mode

## Monitor mode

- Makes only unprivileged access to memory.
- Cannot change mode except by causing an exception, see Handling exceptions that are taken to an Exception level using AArch32.

System mode is implemented at EL1 or EL3, see Effect of the EL3 Execution state on the PE modes and Exception levels.

System mode has the same registers available as User mode, and is not entered by any exception.

## Supervisor mode

Supervisor mode is implemented at EL1 or EL3, see Effect of the EL3 Execution state on the PE modes and Exception levels.

Supervisor mode is the default mode to which a Supervisor Call exception is taken. Executing an SVC (Supervisor Call) instruction generates a Supervisor Call exception.

In an implementation where the highest implemented Exception level is using AArch32, if that Exception level is EL3 or EL1, a PE enters Supervisor mode on reset.

Abort mode is implemented at EL1 or EL3, see Effect of the EL3 Execution state on the PE modes and Exception levels.

Abort mode is the default mode to which a Data Abort exception or Prefetch Abort exception is taken.

Undefined mode is implemented at EL1 or EL3, see Effect of the EL3 Execution state on the PE modes and Exception levels.

Undefined mode is the default mode to which an instruction-related exception, including any attempt to execute an UNDEFINED instruction, is taken.

FIQ mode is implemented at EL1 or EL3, see Effect of the EL3 Execution state on the PE modes and Exception levels.

FIQ mode is the default mode to which an FIQ interrupt is taken.

IRQ mode is implemented at EL1 or EL3, see Effect of the EL3 Execution state on the PE modes and Exception levels.

IRQ mode is the default mode to which an IRQ interrupt is taken.

Hyp mode is the Non-secure EL2 mode.

Hyp mode is entered on taking an exception from Non-secure state that must be taken to EL2.

In an implementation where the highest implemented Exception level is EL2 and EL2 uses AArch32 on reset, a PE enters Hyp mode on reset.

The Hypervisor Call exception and Hyp Trap exception are implemented as part of EL2 and are always taken to Hyp mode when EL2 is using AArch32.

Executing an HVC (Hypervisor Call) instruction generates a Hypervisor Call exception. See Hypervisor Call (HVC) exception.

For more information, see Hyp mode.

Monitor mode is the Secure EL3 mode. This means it is always in the Secure state, regardless of the value of the SCR.NS bit.

Monitor mode is the mode to which a Secure Monitor Call exception is taken. In a Non-secure EL1 mode, or a Secure EL3 mode, executing an SMC (Secure Monitor Call) instruction generates a Secure Monitor Call exception.

When EL3 is using AArch32, some exceptions that are taken to a different mode by default can be configured to be taken to EL3, see PE mode for taking exceptions.

When EL3 is using AArch32, software executing in Monitor mode:

- Has access to both the Secure and Non-secure copies of System registers.
- Can perform an exception return to Secure state, or to Non-secure state.

This means that, when EL3 is using AArch32, Monitor mode provides the only recommended method of changing between the Secure and Non-secure Security states.

## Secure and Non-secure modes

In an implementation that includes EL3, the names of most implemented modes can be qualified as Secure or Non-secure, to indicate whether the PE is also in Secure state or Non-secure state. For example:

- If a PE is in Supervisor mode and Secure state, it is in Secure Supervisor mode .
- If a PE is in User mode and Non-secure state, it is in Non-secure User mode .

Note

As indicated in the appropriate Mode descriptions:

- Monitor mode is a Secure mode, meaning it is always in the Secure state.
- Hyp mode is a Non-secure mode, meaning it is accessible only in Non-secure state.

## G1.9.1.1 Effect of the EL3 Execution state on the PE modes and Exception levels

Figure G1-1 shows the PE modes, Exception levels, and Security states, for an implementation that includes all of the Exception levels, when EL3 is using AArch32. Figure G1-2 shows how the implemented modes change when EL3 is using AArch64.

<!-- image -->

Figure G1-2 Exception levels, and PE modes, when EL3 is using AArch64

Comparing Figure G1-1 and Figure G1-2 shows how, in Secure state only, the implementation of System, FIQ, IRQ, Supervisor, Abort, and Undefined mode depends on the Execution state that EL3 is using. That is, these modes are implemented as follows:

## Non-secure state

## Secure state

## G1.9.2 Hyp mode

Hyp mode is the Non-secure EL2 mode. When EL2 is using AArch32, it provides the usual method of controlling the virtualization of Non-secure execution at EL1 and EL0.

If Non-secure EL1 is using AArch32, then System, FIQ, IRQ, Supervisor, Abort, and Undefined modes are implemented as part of EL1. Otherwise, these modes are not implemented in Non-secure state.

The implementation of these modes depends on the Execution state that EL3 is using, as follows:

## EL3 using AArch64

If Secure EL1 is using AArch32, then System, FIQ, IRQ, Supervisor, Abort, and Undefined modes are implemented as part of EL1. Otherwise, these modes are not implemented in Secure state.

## EL3 using AArch32

In Secure state, System, FIQ, IRQ, Supervisor, Abort, and Undefined modes are implemented as part of EL3, see Figure G1-1.

Note

The alternative method of controlling this functionality is by accessing the EL2 controls from EL3 with the SCR\_EL3.NS or SCR.NS bit set to 1.

This section summarizes how Hyp mode differs from the other modes, and references where this part of the manual describes the features of Hyp mode in more detail:

- Software executing in Hyp mode executes at EL2, see Figure G1-1.
- Hyp mode is accessible only in Non-secure state. In Secure state, an attempt by a CPS or an MSR instruction to change PSTATE.M to Hyp mode is an illegal change to PSTATE.M, as described in Illegal changes to PSTATE.M.
- In Non-debug state, the only mechanisms for changing to Hyp mode are:
- -An exception taken from a Non-secure EL1 or EL0 mode.
- -When EL3 is using AArch32, an exception return from Secure Monitor mode.
- -When EL3 is using AArch64, an exception return from EL3.
- In Hyp mode, the only exception return is execution of an ERET instruction, see ERET.
- In Hyp mode, the CPACR has no effect on the execution of:
- -System register access instructions.
- -Advanced SIMD and floating-point instructions.

The HCPTR controls execution of these instructions in Hyp mode.

- If software running in Hyp mode executes an SVC instruction, the Supervisor Call exception generated by the instruction is taken to Hyp mode, see SVC.
- An exception return with restored PSTATE specifying Hyp mode is an illegal return event , as described in Illegal return events from AArch32 state, if any of the following applies:
- -EL3 is using AArch64 and the value of SCR\_EL3.NS is 0.
- -EL3 is using AArch32 and the value of SCR.NS is 0.
- -The return is from a Non-secure EL1 mode.
- The instructions described in the following sections are UNDEFINED if executed in Hyp mode:
- -SRS. See SRS, SRSDA, SRSDB, SRSIA, SRSIB.
- -RFE. See RFE, RFEDA, RFEDB, RFEIA, RFEIB.
- -LDM(exception return).
- -LDM(User registers).
- -STM(User registers).
- -The SUBS PC, LR forms of the instructions described in SUB, SUBS (immediate).

Note

In T32 state, ERET is encoded as SUBS PC, LR, #0 , and therefore this is a valid instruction.

- -The exception return form of the instructions described in MOV , MOVS (register).

In addition, deprecated forms of the A32 ADCS , ADDS , ANDS , BICS , EORS , MOVS , MVNS , ORRS , RSBS , RSCS , SBCS , and SUBS instructions with the PC as the destination register are UNDEFINED if executed in Hyp mode. The instruction descriptions identify these UNDEFINED cases.

- The Load unprivileged and Store unprivileged instructions LDRT , LDRSHT , LDRHT , LDRBT , STRT , STRHT , and STRBT , are CONSTRAINED UNPREDICTABLE if executed in Hyp mode.

To permit entry to Hyp mode using the Hypervisor Call exception, Secure software must enable use of the HVC instruction:

- By setting the SCR\_EL3.HCE bit to 1, if EL3 is using AArch64.
- By setting the SCR.HCE bit to 1, if EL3 is using AArch32.

If EL3 is implemented and using AArch32, and SCR.HCE is set to 0, the HVC instruction is UNPREDICTABLE in Hyp mode. The instruction is either UNDEFINED or executes as a NOP .

If EL3 is implemented and using AArch64, and SCR\_EL3.HCE is set to 0, the HVC instruction is UNDEFINED in Hyp mode.

If EL3 is not implemented and HCR.HCD is set to 1, the HVC instruction is UNDEFINED in Hyp mode.

## G1.9.3 Pseudocode description of mode operations

The BadMode() function tests whether a 5-bit mode number corresponds to one of the permitted modes.

The BadMode() function is defined in A-profile Architecture Pseudocode.