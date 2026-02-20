## D1.8 Self-hosted debug

IMJGPY

The architecture supports both of the following:

Self-hosted debug

The PE itself hosts a debugger. The debugger programs the PE to generate debug exceptions. Debug exceptions are accommodated in the Arm Exception model.

External debug

The PE is controlled by an external debugger. The debugger programs the PE to generate debug events, that cause the PE to enter Debug state. In Debug state, the PE is halted.

## D1.8.1 Debug exceptions

IPWPHY

If a debugger has programmed the PE to generate Debug exceptions, the Debug exceptions occur during normal program flow.

IDSWBH

For example, a software developer might use a debugger contained in an operating system to debug an application. To do this, the debugger might enable one or more debug exceptions.

IBXVCF

The debug exceptions are all of the following:

- Breakpoint Instruction exceptions.

- Breakpoint exceptions.

- Watchpoint exceptions.

- Vector Catch exceptions.

- Software Step exceptions.

IVYKHK

IGRWSG

The PE can only generate a particular debug exception if all of the following are true:

- Debug exceptions are enabled from the current Exception level and Security state. See Enabling debug exceptions from the current Exception level and Security state. Breakpoint Instruction exceptions are always enabled from the current Exception level and Security state.
- Adebugger has enabled that particular debug exception. All of the debug exceptions except for Breakpoint Instruction exceptions have an enable control contained in the MDSCR\_EL1. See The debug exception enable controls.

Breakpoints and watchpoints can cause entry to Debug state instead of causing debug exceptions. See About External Debug.

## D1.8.2 The PSTATE debug mask bit, D

| R DYRLS   | The debug exception mask bit, PSTATE.D, can mask Watchpoint, Breakpoint, and Software Step exceptions if the target Exception level is the current Exception level.                                    |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R RDYDM   | If in AArch64 state and the target Exception level of a debug exception is lower than the current Exception level, the debug exception is masked.                                                      |
| R JWZFQ   | If the target Exception level is higher than the current Exception level, debug exceptions are not masked by PSTATE.D.                                                                                 |
| R KCHGM   | If PSTATE.D is 1 and the PE is already handling an exception in AArch64 state, the Watchpoint, Breakpoint, and Software Step exceptions are masked.                                                    |
| I LVYYH   | If an exception is already being handled, masking prevents software from generating another instance of an exception and prevents recursive entry into the exception handler and loss of return state. |
| R NCHXS   | Masking debug interrupts with PSTATE.D prevents the generation of new debug exceptions, therefore, any masked debug exceptions are not taken if PSTATE.D is later set to 0.                            |
| I VSTYD   | The behavior described inR NCHXS differs from the behavior for interrupts, where the PSTATE.{A, I, F} mask prevents the interrupt from being taken, but instead the interrupt remains pending.         |
| I KWFMZ   | When an exception is taken, PSTATE.D is set to 1.                                                                                                                                                      |