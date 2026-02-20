## F2.5 PSTATE and banked register access instructions

These instructions transfer PE state information to or from a general-purpose register.

## F2.5.1 PSTATE access instructions

PSTATE holds process state information, see Process state, PSTATE. In AArch32 state:

- At EL1 or higher, PSTATE is accessible using the Current Program Status Register (CPSR).
- At EL0, a subset of the CPSR is accessible as the Application Program Status Register (APSR).
- On taking an exception, the contents of the CPSR are copied to the Saved Program Status Register (SPSR) of the mode from which the exception is taken.

The MRS and MSR instructions move the contents of the CPSR, APSR, or the SPSR of the current mode to or from a general-purpose register, see:

- MRS.
- MSR(immediate).
- MSR(register).

When executed at EL0, MRS and MSR instructions can only access the APSR.

The PSTATE Condition flags, PSTATE.{N, Z, C, V} are set by the execution of data-processing instructions, and can control the execution of conditional instructions. However, software can set the Condition flags explicitly using the MSR instruction, and can read the current state of the Condition flags explicitly using the MRS instruction.

In addition, at EL1 or higher, software can use the CPS instruction to change the PSTATE.M field and the PSTATE.{A, I, F} interrupt mask bits, see CPS, CPSID, CPSIE.

## F2.5.2 Banked register access instructions

At EL1 or higher, the MRS (banked register) and MSR (banked register) instructions move the contents of a banked general-purpose register, the SPSR, or the ELR\_hyp, to or from a general-purpose register. See:

- MRS(Banked register).
- MSR(Banked register).