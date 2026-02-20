## D2.12 Synchronization and debug exceptions

The behavior of debug depends on all of the following:

- The state of the external debug authentication interface.
- Indirect reads of:
- -External debug registers.
- -System registers, including system debug registers.
- -Special-purpose registers.

If a change is made to any of these, the effect of that change on debug exception generation cannot be relied on until after a Context Synchronization event has occurred. Similarly, the effect of the change on the software step state machine cannot be relied on until after a Context Synchronization event has occurred.

For any instructions executed between the time when the change is made and the time when the next Context Synchronization event occurs, it is CONSTRAINED UNPREDICTABLE whether debug uses the state of the PE before the change, or the state of the PE after the change.

Example D2-12 Example of synchronization and Breakpoint exception generation

1. Software changes MDSCR\_EL1.MDE from 0 to 1.
2. An instruction is executed, that would cause a Breakpoint exception if self-hosted debug uses the state of the PE after the change.
3. AContext Synchronization event occurs.

In this case, it is CONSTRAINED UNPREDICTABLE whether the instruction generates a Breakpoint exception.

## Example D2-13 Example of synchronization and debug exceptions generation

1. Software unlocks the OS Lock.
2. The PE executes some instructions.
3. AContext Synchronization event occurs.

During the time when the PE is executing some instructions, step 2, it is CONSTRAINED UNPREDICTABLE whether debug exceptions other than Breakpoint Instruction exceptions can be generated.

## Note

For more information, see:

- Accessing PSTATE fields.
- Synchronization requirements for AArch64 System registers.
- Synchronization of changes to the external debug registers.

## Chapter D3 AArch64 Self-hosted Trace

This chapter describes the AArch64 self-hosted trace:

## Introductory information:

- About self-hosted trace.
- Trace sinks.
- Register controls to enable self-hosted trace.

## Prohibited regions in trace:

- Controls to prohibit trace at Exception levels.
- Self-hosted trace and visibility of virtual data.

## Timestamps and Synchronization:

- Self-hosted trace timestamps.
- Synchronization in self-hosted trace.