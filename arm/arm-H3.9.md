## H3.9 Synchronization and Halting debug events

The behavior of external debug depends on:

- Indirect reads of:
- -External debug registers.
- -System registers, including system debug registers.
- -Special-purpose registers.
- The state of the external authentication interface.

For some registers, all read and write accesses that update the register occur in program order, without any additional synchronization, but others require an explicit Context Synchronization event. For more information on the synchronization of register updates, see:

- Synchronization requirements for AArch64 System registers.
- Synchronization of changes to the external debug registers.
- State and mode changes without explicit Context Synchronization events.

Changes to the external authentication interface do not require explicit synchronization to affect External Debug Request debug events. See Synchronization and External Debug Request debug events.

For changes that require explicit synchronization, it is CONSTRAINED UNPREDICTABLE whether instructions between the change and the Context Synchronization event observe the old state or the new state.

This means that any change to these registers or the external authentication interface requires explicit synchronization by a Context Synchronization event before the change takes effect. This ensures that for instructions appearing in program order after the change, the change affects the following:

- The generation and behavior of Breakpoint and Watchpoint debug events. See Synchronization and debug exceptions for exceptions taken from AArch64 state, or Synchronization and debug exceptions for exceptions taken from AArch32 state.
- The generation of all Halting debug events by instructions.
- Taking a pending Halting debug event or other asynchronous debug event. See:
- -Pending Halting debug events.
- -Synchronization and External Debug Request debug events.
- The behavior of the Halting Step state machine. See Synchronization and the Halting Step state machine.

## H3.9.1 Pending Halting debug events

AHalting debug event might be pending:

- If Halting Step of an instruction sets EDESR.SS to 1, and halting is prohibited following the step, then the Halting Step state machine is inactive but a Halting Step debug event is pending.
- If a Reset Catch debug event sets EDESR.RC to 1, and halting is prohibited following reset, then a Reset Catch debug event is pending.
- If an OS Unlock Catch debug event sets EDESR.OSUC to 1, then an OS Unlock Catch debug event is pending.
- If FEAT\_Debugv8p8 is implemented and an Exception Catch debug event sets EDESR.EC to 1, and before the PE takes the Exception Catch debug event, the PE takes an asynchronous exception, then an Exception Catch debug event is pending.
- If FEAT\_Debugv8p9 and FEAT\_ETEv1p3 are implemented, and an ETE external debug request is generated, and the PE enters a state where halting is prohibited before the PE halts and enters Debug state.
- If FEAT\_Debugv8p9 and FEAT\_TRBE\_EXT are implemented, and a Trace Buffer Unit external debug request is generated, and the PE enters a state where halting is prohibited before the PE halts and enters Debug state.
- If FEAT\_Debugv8p9 and FEAT\_PMUv3p9 are implemented, and a PMU overflow external debug request is generated, and the PE enters a state where halting is prohibited before the PE halts and enters Debug state.

Pending Halting debug events are taken asynchronously when halting is allowed.

Pending Halting debug events are discarded by a Cold reset. The debugger can also force a pending event to be dropped by writing to EDESR.

Any Halting debug event that is observed as pending in the EDESR before a Context Synchronization event is taken and the PE enters Debug state before the first instruction following the Context Synchronization event completes its execution. This is possible only if halting is allowed after completion of the Context Synchronization event.

If the first instruction after the Context Synchronization event generates a synchronous exception then the architecture does not define the order in which the debug event and the exception or exceptions are taken, unless both:

- AHalting Step debug event is pending. EDESR.SS == 1.
- The Context Synchronization event is an exception return from EL3 when halting is prohibited at EL3 to a state where halting is allowed.

Example H3-4

Context synchronization event

When FEAT\_RME is not implemented, FEAT\_ExS is implemented, and SCTLR\_EL3.EOS is 0b1 , an exception return from EL3 using AArch64 with ExternalSecureInvasiveDebugEnabled () == FALSE to Non-secure state with ExternalInvasiveDebugEnabled () == TRUE is such an event.

In this case the order in which the debug events are handled is specified to avoid a double-step. See Entering the active-pending state.

If FEAT\_Debugv8p8 is implemented and EDESR.EC is 1, when a pending Exception Catch debug event is taken following a Context Synchronization event, the PE enters Debug state before fetching any instruction:

- At ELn in Non-secure state, if EDECCR.NSE&lt;n&gt; is 1 and address translation is disabled at ELn.
- At ELn in Secure state, if EDECCR.SE&lt;n&gt; is 1 and address translation is disabled at ELn.
- At ELn in Realm state, if EDECCR.RLE&lt;n&gt; is 1 and address translation is disabled at ELn.

If an asynchronous exception is also pending after the Context Synchronization event then the architecture does not define the order in which the debug event and the exception or exceptions are taken.

Note

These rules are based on the rules that apply to taking asynchronous exceptions. See Asynchronous exception types.

## Chapter H4 The Debug Communication Channel and Instruction Transfer Register

This chapter describes communication between a debugger and the implemented debug logic, using the Debug Communications Channel (DCC) and the Instruction Transfer Register (ITR), and associated control flags. It contains the following sections:

- Introduction.
- DCCand ITR registers.
- DCCand ITR access modes.
- Flow control of the DCC and ITR registers.
- Synchronization of DCC and ITR accesses.
- Interrupt-driven use of the DCC.
- Pseudocode description of the operation of the DCC and ITR registers.

Note

Where necessary, Table K14-1 disambiguates the general register references used in this chapter.