## G2.11 Synchronization and debug exceptions

The behavior of debug depends on all of the following:

- The state of the external debug authentication interface.
- Indirect reads of:
- -External debug registers.
- -System registers, including system debug registers.
- -Special-purpose registers.

If a change is made to any of these, the effect of that change on debug exception generation cannot be relied on until after a Context Synchronization event has occurred.

For any instructions executed between the time when the change is made and the time when the next Context Synchronization event occurs, it is CONSTRAINED UNPREDICTABLE whether debug uses the state of the PE before the change, or the state of the PE after the change.

## Example G2-4 Example of synchronization and Breakpoint exception generation

1. Software changes DBGDSCRext.MDBGen from 0 to 1.
2. An instruction is executed, that would cause a Breakpoint exception if self-hosted debug uses the state of the PE after the change.
3. AContext Synchronization event occurs.

In this case, it is CONSTRAINED UNPREDICTABLE whether the instruction generates a Breakpoint exception.

## Example G2-5 Example of synchronization and debug exceptions generation

1. Software unlocks the OS Lock.
2. The PE executes some instructions.
3. AContext Synchronization event occurs.

During the time when the PE is executing some instructions, step 2, it is CONSTRAINED UNPREDICTABLE whether debug exceptions other than Breakpoint Instruction exceptions can be generated.

Note

For more information, see:

- Synchronization of changes to AArch32 System registers.
- Accessing PSTATE fields.
- Synchronization of changes to the external debug registers.

## G2.11.1 State and mode changes without explicit Context Synchronization events

Most changes to the Exception level, and most changes to the Security state if EL3 is implemented, happen as a result of operations that are an explicit Context Synchronization event. This is because taking an exception and returning from an exception are both explicit Context Synchronization events, and the Privilege level and Security state can only change as a result of taking or returning from an exception.

However, some Security state and AArch32 mode changes can happen because of operations that are not an explicit Context Synchronization event. These are:

- AArch32 mode changes caused by MSR and CPS instructions. A mode change might be to a mode at a lower Privilege level.
- If EL3 is using AArch32, a Security state change caused by a direct write to the SCR in a privileged mode other than Monitor mode, to set SCR.NS to 1.

## Chapter G3 AArch32 Self-hosted Trace

This chapter describes the AArch32 self-hosted trace:

## Introductory information:

- About self-hosted trace.
- Trace Sinks.
- Register controls to enable self-hosted trace.

## Prohibited regions in trace:

- Controls to prohibit trace at Exception levels.
- Self-hosted trace and address translation.

## Timestamps and Synchronization:

- Self-hosted trace timestamps.
- Synchronization in self-hosted trace.