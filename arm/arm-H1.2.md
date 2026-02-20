## H1.2 External debug

Debug events allow an external debugger to halt the PE. The A-profile provides the following debug events:

- Halting Step debug events:
- -The debugger can use this resource to make the PE step through code one line at a time.
- Halt Instruction debug event:
- -This might occur when software executes the Halting breakpoint instruction, HLT .
- Exception Catch debug event:
- -This can be programmed to occur on all entries to a given Exception level.
- External Debug Request debug event:
- -An embedded cross-trigger can signal this debug event.
- OS Unlock Catch debug event:
- -This might occur when the state of the OS Lock changes from locked to unlocked.
- Reset Catch debug events:
- -This might occur when the PE exits reset state.
- Software Access debug event:
- -This can be programmed to occur when software tries to access the Breakpoint Value registers, the Breakpoint Control registers, the Watchpoint value registers, or the Watchpoint Control registers. It caused a trap to Debug state.

Breakpoints and watchpoints can also halt the PE.

When the PE is in Debug state:

- It stops executing instructions from the location indicated by the program counter, and is instead controlled through the external debug interface.
- The Instruction Transfer Register, ITR, passes instructions to the PE to execute in Debug state:
- -The ITR contains a single register, EDITR, and associated flow-control flags.
- The Debug Communications Channel , DCC, passes data between the PE and the debugger:
- -The DCC includes the data transfer registers, DTRRX and DTRTX, and associated flow-control flags.
- -Although the DCC is an essential part of Debug state operation, it can also be used in Non-debug state.
- The PE cannot service any interrupts in Debug state.

Debug State describes Debug state in more detail.