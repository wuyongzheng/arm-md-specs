## H2.2 Halting the PE on debug events

For details of debug events, see Introduction to Halting debug events and Breakpoint and Watchpoint debug events.

On a debug event, the PE must do one of the following:

- Enter Debug state.
- Pend the debug event.
- Generate a debug exception.
- Ignore the debug event.

This behavior depends on both:

- Whether halting is allowed by the current state of the debug authentication interface. See Halting allowed and halting prohibited.
- The type of debug event and the programming of the debug control registers.
- -See Halting debug events for all Halting debug events.
- -See Breakpoint and Watchpoint debug events for Breakpoint and Watchpoint debug events.

See also Other debug exceptions.

This means that behavior can be CONSTRAINED UNPREDICTABLE if the conditions change. See Synchronization and Halting debug events.

Table H3-1 summarizes the possible outcomes of each type of debug event.

## H2.2.1 Halting allowed and halting prohibited

Halting can be either allowed or prohibited:

- Halting is always prohibited in Debug state.
- Halting is always prohibited when DoubleLockStatus() == TRUE.
- -This means that FEAT\_DoubleLock is implemented and OS Double lock is locked.
- Halting is also controlled by the IMPLEMENTATION DEFINED authentication interface, and is prohibited when all of the following apply:
- -The PE is in Non-secure state and ExternalInvasiveDebugEnabled() == FALSE.
- -The PE is in Secure state and ExternalSecureInvasiveDebugEnabled() == FALSE.
- -The PE is in Realm state and ExternalRealmInvasiveDebugEnabled() == FALSE.
- -The PE is in Root state and ExternalRootInvasiveDebugEnabled() == FALSE.
- Otherwise, halting is allowed.

For more information, see:

- Pseudocode description of Halting on debug events.
- Required debug authentication.
- Recommended External Debug Interface.

## H2.2.2 Halting debug events

The Halting debug events are described in Halting Debug Events.

When a Halting debug event is generated, it causes entry to Debug state if all of the following are true:

- Halting is allowed. See Halting allowed and halting prohibited.
- The Halting debug event is one of:
- -AHalt Instruction debug event and EDSCR.HDE == 1.
- -ASoftware Access debug event and OSLSR\_EL1.OSLK == 0, meaning that the OS Lock is unlocked.
- -Neither a Halt Instruction debug event nor a Software Access debug event.

Note

- AHalt Instruction debug event is the only Halting debug event that relies on EDSCR.HDE == 1.

- Halting on Breakpoint and Watchpoint debug events is also controlled by EDSCR.HDE. See Breakpoint and Watchpoint debug events.

- [ ] - EDSCR.HDE can be written by software when the OS Lock is locked. Privileged code can use MDCR\_EL3.TDOSA and HDCR.TDOSA to trap writes to OS Lock registers.

If a Halting debug event does not generate entry to Debug state because the conditions listed in this section do not hold, then:

- If the Halting debug event is a Halt Instruction debug event, the instruction that generated the Halting debug event is treated as UNDEFINED.
- If the Halting debug event is a Software Access debug event, it is ignored.
- If the Halting debug event is an Exception Catch debug event, it is ignored except when FEAT\_Debugv8p8 is implemented, in which case the event might be pended.

In all other cases the Halting debug event is pended, see Pending Halting debug events.

Summary of actions from debug events summarizes the possible outcome for each type of Debug event.

Note

Halting debug events never generate debug exceptions.

## H2.2.3 Breakpoint and Watchpoint debug events

Abreakpoint or watchpoint generates an entry to Debug state if all of the following conditions hold:

- Halting debug is enabled, that is EDSCR.HDE == 1.
- Halting is allowed. See Halting allowed and halting prohibited.
- The OS Lock is unlocked, that is OSLSR.OSLK == 0.

The Address Mismatch breakpoint type is reserved when all of these conditions are met.

MDSCR\_EL1.MDE or DBGDSCRext.MDBGen is ignored when determining whether to enter Debug state. A breakpoint or watchpoint that generates entry to Debug state is a Breakpoint or Watchpoint debug event and does not generate a debug exception.

Abreakpoint or watchpoint that does not generate an entry to Debug state either:

- Generates a Breakpoint or Watchpoint exception.
- Is ignored.

Note

EDSCR.HDE is ignored when determining whether to generate a debug exception. The debug exception is suppressed only if the PE enters Debug state. This means that the use of Halting debug mode in one Security state does not affect the Exception model in another Security state.

See AArch64 Self-hosted Debug, AArch32 Self-hosted Debug, and the Note in Other debug exceptions.

## H2.2.4 Other debug exceptions

The following events never generate entry to Debug state:

- Breakpoint Instruction exceptions.
- Software Step exceptions.

- Vector Catch exceptions.

The behavior of these events is unchanged when Halting debug mode is enabled, that is when EDSCR.HDE == 1. This means that these events can do one of the following:

- They can generate a debug exception.
- They can be ignored.

For additional information, see AArch64 Self-hosted Debug and AArch32 Self-hosted Debug.

## H2.2.5 Debug state entry and debug event prioritization

The following are synchronous debug events:

- Breakpoint debug event.
- Watchpoint debug event.
- Halting Step debug event.
- Halt Instruction debug event.
- Exception Catch debug event.
- Software Access debug event.
- Reset Catch debug event.

Each of these synchronous debug events are treated as a synchronous exception generated by an instruction, or by the taking of an exception or reset. That is, if halting is allowed, the synchronous debug event must be taken before any subsequent instructions are executed. Reset Catch debug events must be taken before the PE executes the instruction at the reset vector.

## Note

- Reset Catch and Exception Catch debug events might be generated asynchronously, because they can result from an asynchronous exception. However, if halting is allowed after the reset or asynchronous exception has been processed, the Reset Catch or Exception Catch debug event is taken synchronously.
- The Halting Step debug event is generated by the instruction after the stepped instruction. Therefore, if the stepped instruction generates any other synchronous exceptions or debug events these are taken first.

If halting is prohibited then Halting Step debug events and Reset Catch debug events might be pended and taken asynchronously. OS Unlock Catch debug events are always pended and taken asynchronously. See Pending Halting debug events.

The architecture does not define when asynchronous debug events are taken, and therefore the prioritization of asynchronous debug events is IMPLEMENTATION DEFINED. See Synchronization and Halting debug events.

The following list shows how the synchronous debug events are prioritized, with 1 being the highest priority.

Note

The priority numbering is the same as the numbering for AArch64 synchronous exception priorities listed in Synchronous exception types, and in particular Prioritization of asynchronous exceptions. This numbering correlates with the equivalent AArch32 list in Exception prioritization for exceptions taken to AArch32 state.

The priority for synchronous debug events is as follows:

| Reset Catch debug event. See Reset Catch debug events.                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This debug event has a higher priority than the synchronous exceptions listed in Synchronous exception types.                                                                        |
| Exception Catch debug event if it has a priority of 2. See Exception Catch debug event.                                                                                              |
| This debug event can be assigned one of two priorities, 2 or 6. When it has a priority of 2, it has a higher priority than the synchronous exceptions listed in the Exception model. |

| 3     | Halting Step debug event. See Halting Step debug events.                                |
|-------|-----------------------------------------------------------------------------------------|
| 4-5   | These events are not debug events.                                                      |
| 6     | Exception Catch debug event if it has a priority of 6. See Exception Catch debug event. |
|       | This debug event can be assigned one of two priorities, 2 or 6.                         |
| 7-9   | These events are not debug events.                                                      |
| 10    | Breakpoint debug events. See Breakpoint and Watchpoint debug events.                    |
| 11-12 | These events are not debug events.                                                      |
| 13    | Halt Instruction debug event. See Halt Instruction debug event.                         |
| 14-39 | These events are not debug events.                                                      |
| 40    | Software Access debug event. See Software Access debug event.                           |
| 41-45 | These events are not debug events.                                                      |
| 46    | Watchpoint debug events. See Breakpoint and Watchpoint debug events.                    |
| 47-48 | These events are not debug events.                                                      |

For Reset Catch debug events and Halting Step debug events, the priorities listed in this section apply only when halting is allowed at the time the event is generated. This means that the event is taken synchronously and not pended.

For more information on the prioritization of exceptions, see:

- Synchronous exception types.
- Prioritization of asynchronous exceptions.
- Exception prioritization for exceptions taken to AArch32 state. This section covers synchronous and asynchronous exceptions.

## H2.2.5.1 Breakpoint debug events and Vector Catch exception

An Address Matching Vector Catch exception has the same priority as a Breakpoint debug event. See Prioritization of Synchronous exceptions taken to AArch64 state.

The prioritization of these events is unchanged even if the breakpoint generates entry to Debug state instead of a Breakpoint exception. This means that if a single instruction generates both an Address Matching Vector Catch exception and a Breakpoint debug event, there is a CONSTRAINED UNPREDICTABLE choice of:

- The PE entering Debug state due to the Breakpoint debug event.
- AVector Catch exception.

This applies only if all of the following are true:

- Halting debug is enabled.
- Halting is allowed.
- The OS Lock is unlocked.

An Exception Trapping Vector Catch exception must be generated immediately following the exception that generated it. This means that it does not appear in the priority table.

## H2.2.6 Imprecise entry to Debug state

Debug state entry is normally precise . This means that the PE cannot enter Debug state if it can neither complete nor abandon all currently executing instructions and leave the PE in a precise state. See Definition of a precise exception and imprecise exception.

Adebugger can write a value of 1 to EDRCR.CBRRQ to allow imprecise entry to Debug state. An External Debug Request debug event must be pending before writing 1 to this bit. Support for this feature is OPTIONAL and it is IMPLEMENTATION DEFINED when it is effective at forcing entry to Debug state.

The PE ignores writes to this bit in all the following cases:

- ExternalInvasiveDebugEnabled() == FALSE.
- FEAT\_RME is not implemented and ExternalSecureInvasiveDebugEnabled() == FALSE, and either:
- -EL3 is not implemented and the implemented Security state is Secure state.
- -EL3 is implemented.
- FEAT\_RME is implemented and ExternalRootInvasiveDebugEnabled() == FALSE.

Example H2-1 shows how entry to Debug state can be forced.

Means one of:

- Software Step exceptions.
- Breakpoint Instruction exceptions.
- Vector Catch exceptions for AArch64 state or Vector Catch exceptions for AArch32 state.

Means one of the following:

- Halting Step debug events.
- External Debug Request debug event.
- Reset Catch debug events.
- OS Unlock Catch debug event.

## Example H2-1 Forcing entry to Debug state

The debugger pends an External Debug Request debug event through the CTI to halt a program that has stopped responding. However, the memory system is not responding and a memory access instruction cannot complete. This means that Debug state cannot be entered precisely. The debugger writes a value of 1 to EDRCR.CBRRQ. The PE cancels all outstanding memory accesses and enters Debug state. As some instructions might not have completed correctly, entry to Debug state is imprecise.

When Debug state is entered imprecisely, all memory access instructions executed through the ITR have CONSTRAINED UNPREDICTABLE behavior. The value of all registers is UNKNOWN, but might be useful for diagnostic purposes.

## H2.2.7 Summary of actions from debug events

Table H2-1 shows the Software and Halting debug events. In Table H2-1, the columns have the following meaning:

## Debug event type

This means the type of debug event where:

## Other software

## Other Halting

## Authentication

Other debug events are referred to explicitly.

This means halting is allowed by the IMPLEMENTATION DEFINED external authentication interface. It is the result of one of the following pseudocode functions:

In Non-secure state ExternalInvasiveDebugEnabled() .

In Secure state ExternalSecureInvasiveDebugEnabled() .

In Realm state ExternalRealmInvasiveDebugEnabled() .

In Root state

ExternalRootInvasiveDebugEnabled() .

DLK

This indicates whether FEAT\_DoubleLock is implemented and locked, DoubleLockStatus() == TRUE.

OSLK

This is the value of OSLSR.OSLK. It indicates whether the OS Lock is locked.

HDE

This is the value of EDSCR.HDE. It indicates whether Halting debug is enabled.

The letter X in Table H2-1 indicates that the value can be either 0 or 1.

Table H2-1 Debug authentication for external debug

| Debug event type                     | Authentication   | DLK   | OSLK   | HDE   | Behavior                                 |
|--------------------------------------|------------------|-------|--------|-------|------------------------------------------|
| Other software                       | X                | X     | X      | X     | Handled by the Exception model           |
| Breakpoint or Watchpoint debug event | X                | TRUE  | X      | X     | Handled by the Exception model (ignored) |
| Breakpoint or Watchpoint debug event | X                | FALSE | 1      | X     | Handled by the Exception model (ignored) |
| Breakpoint or Watchpoint debug event | FALSE            | FALSE | 0      | X     | Handled by the Exception model           |
| Breakpoint or Watchpoint debug event | TRUE             | FALSE | 0      | 0     | Handled by the Exception model           |
| Breakpoint or Watchpoint debug event | TRUE             | FALSE | 0      | 1     | Entry to Debug state                     |
| Halt Instruction debug event         | FALSE            | X     | X      | X     | UNDEFINED                                |
| Halt Instruction debug event         | TRUE             | TRUE  | X      | X     | UNDEFINED                                |
| Halt Instruction debug event         | TRUE             | FALSE | X      | 0     | UNDEFINED                                |
| Halt Instruction debug event         | TRUE             | FALSE | X      | 1     | Entry to Debug state                     |
| Exception Catch debug event          | FALSE            | X     | X      | X     | Might be pended a                        |
| Exception Catch debug event          | TRUE             | TRUE  | X      | X     | Ignored                                  |
| Exception Catch debug event          | TRUE             | FALSE | X      | X     | Entry to Debug state                     |
| Software Access debug event          | FALSE            | X     | X      | X     | Ignored                                  |
| Software Access debug event          | TRUE             | TRUE  | X      | X     | Ignored                                  |
| Software Access debug event          | TRUE             | FALSE | 1      | X     | Ignored                                  |
| Software Access debug event          | TRUE             | FALSE | 0      | X     | Entry to Debug state                     |
| Other Halting                        | FALSE            | X     | X      | X     | Debug event is pended                    |
| Other Halting                        | TRUE             | TRUE  | X      | X     | Debug event is pended                    |
| Other Halting                        | TRUE             | FALSE | X      | X     | Entry to Debug state                     |

a. See Exception Catch debug event.

## H2.2.8 Pseudocode description of Halting on debug events

The Halted() , Restarting() , HaltingAllowed() , and HaltOnBreakpointOrWatchpoint() functions are described in the pseudocode.