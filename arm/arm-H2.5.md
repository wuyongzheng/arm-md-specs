## H2.5 Exiting Debug state

The PE exits Debug state when it receives a Restart request trigger event. If EDSCR.ITE == 0, when the PE receives a Restart Request trigger event, the behavior of any instruction issued through the ITR in Normal access mode or an operation issued by a DTR access in Memory access mode that has not completed execution is one of the following:

- The instruction completes execution in Debug state and the PE ignores the restart request and remains in Debug state.
- The instruction completes execution in Debug state before the PE executes the restart sequence.
- The instruction completes execution in Non-debug state after the PE executes the restart sequence.
- The instruction is abandoned. This means that the instruction does not execute. Any registers or memory accessed by the instruction are left in an UNKNOWN state.

Note

- Implementations can set EDSCR.ITE to 1 to indicate that further instructions can be accepted by ITR before the previous instructions have completed. If any previous instruction has not completed and EDSCR.ITE == 1, then the PE must complete these instructions in Debug state before executing the restart sequence. EDSCR.ITE == 0 indicates that the PE is not ready to restart.
- A debugger must observe that any instructions issued through EDITR that might generate a synchronous exception, as complete, before issuing a restart request. It can do this by observing the completion of a later instruction, as synchronous exceptions must occur in program order. For example, a debugger can observe that an instruction that reads or writes a DTR register is complete because of its effect on the EDSCR.{TXfull, RXfull} flags.

On exiting Debug state, the PE sets the Program Counter to the address in DLR, where:

- If exiting to AArch32 state:
- -Bits[31:1] of the PC are set to the value of bits[31:1] of DLR.
- -Bit[0] of the PC is set to a CONSTRAINED UNPREDICTABLE choice of 0 or the value of bit[0] in DLR.
- If exiting to AArch64 state:
- -Bits[63:56] of DLR\_EL0 might be ignored as part of tagged address handling. See Address tagging.
- -Otherwise the PC is set from DLR\_EL0.

Note

Bits[63:32] of DLR\_EL0 are ignored when exiting to AArch32 state.

Exit from Debug state can give rise to a PC alignment fault exception when the Program Counter is used. Unlike an exception return, this might also happen when returning to AArch32 state. For more information, see PC alignment checking.

On exiting Debug state, PSTATE is set from DSPSR in the same way that an exception return sets PSTATE from SPSR\_ELx:

- The same illegal exception return checks that apply to an exception return also apply to exiting Debug state. If the return from Debug state is an illegal exception return then the effect on PSTATE and the PC is the same as for any other illegal exception return. See Exception return and Exception return to an Exception level using AArch32.
- The checks on the PSTATE.IT bits that apply to exiting Debug state into AArch32 state are the same as those that apply to an exception return. See Architectural Constraints on UNPREDICTABLE Behaviors.
- PSTATE.SS is copied from DSPSR.SS if all of the following hold:
- -MDSCR\_EL1.SS == 1.
- -The debug target Exception level is using AArch64.
- -Software step exceptions from the restart Exception level are enabled.

Otherwise PSTATE.SS is set to 0.

Note

Unlike a return using ERET , PSTATE.SS must be restored from DSPSR.SS because otherwise it is UNKNOWN.

However, if OSDLR.DLK == 1 and DBGPRCR.CORENPDRQ == 0, meaning FEAT\_DoubleLock is implemented and locked in Non-debug state and therefore Software Step exceptions are disabled, but otherwise Software Step exceptions would be enabled from the restart Exception level, it is CONSTRAINED UNPREDICTABLE whether PSTATE.SS is copied from DSPSR.SS.

- If FEAT\_SSBS is implemented, DSPSR.SSBS is copied to PSTATE.SSBS.
- If FEAT\_PAN is implemented, DSPSR.PAN is copied to PSTATE.PAN.
- If FEAT\_UAO is implemented, on exit from Debug state to AArch64 state, DSPSR\_EL0.UAO is copied to PSTATE.UAO. On exit from Debug state to AArch32 state, PSTATE.UAO is not updated.
- If FEAT\_DIT is implemented, on exit from Debug state, DSPSR.DIT is copied to PSTATE.DIT.
- If FEAT\_UINJ is implemented, DSPSR.UINJ is copied to PSTATE.UINJ.
- If FEAT\_MTE is implemented, on exit from Debug state to AArch64 state, DSPSR\_EL0.TCO is copied to PSTATE.TCO. On exit from Debug state to AArch32 state, PSTATE.TCO is not updated.
- If FEAT\_BTI is implemented, DSPSR\_EL0.BTYPE is copied to PSTATE.BTYPE.
- If FEAT\_NMI is implemented, DSPSR\_EL0.ALLINT is copied to PSTATE.ALLINT.
- If FEAT\_GCS is implemented, DSPSR\_EL0.EXLOCK is copied to PSTATE.EXLOCK.
- If FEAT\_EBEP, FEAT\_SPE\_EXC or FEAT\_TRBE\_EXC is implemented, on exit from Debug state to AArch64 state, DSPSR\_EL0.PM is copied to PSTATE.PM. On exit from Debug state to AArch32 state, PSTATE.PM is not updated.
- If FEAT\_SEBEP is implemented, and all of the following apply, then PSTATE.PPEND is copied from DSPSR.PPEND:
- -PMUexceptions from the restart Exception level are enabled.
- -The PMU exception will be unmasked in Non-debug state after the Debug state exit.

Otherwise, PSTATE.PPEND is set to 0.

- If FEAT\_PAuth\_LR is implemented, all of the following apply:
- -For a trivial implementation of PSTATE.PACM, PSTATE.PACM is set to 0.
- -If the effects of PACM instructions are disabled at the target Exception level, PSTATE.PACM is set to 0.
- -Otherwise, DSPSR\_EL0.PACM is copied to PSTATE.PACM.

Note

- One important difference between Debug state exit and an exception return is that the PE can exit Debug state at EL0. Despite this, the behavior of an exit from Debug state is similar to an exception return. For example, PSTATE.{D, A, I, F} is updated regardless of the value of SCTLR\_EL1.UMA.
- Exit from Debug state has no architecturally-defined effect on the Event Register and Exclusives monitors. An exit from Debug state might set the Event Register or clear the Exclusives monitors, or both, but this is not a requirement and debuggers must not rely on any IMPLEMENTATION SPECIFIC behavior.

The ExitDebugState() function is described in A-profile Architecture Pseudocode.

## Chapter H3 Halting Debug Events

This chapter describes a particular class of debug events. It contains the following sections:

- Introduction to Halting debug events.
- Halting Step debug events.
- Halt Instruction debug event.
- Exception Catch debug event.
- External Debug Request debug event.
- OS Unlock Catch debug event.
- Reset Catch debug events.
- Software Access debug event.
- Synchronization and Halting debug events.

Note

Table K14-1 disambiguates the general register references used in this chapter.