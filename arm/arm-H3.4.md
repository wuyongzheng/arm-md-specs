## H3.4 Exception Catch debug event

Exception Catch debug events:

- Are generated when the corresponding bit in the Exception Catch Control Register, EDECCR, is set to 1 on all entries to a given Exception level. This means:
- -Exceptions taken to the Exception level.
- -Exception returns to the Exception level.
- -It is IMPLEMENTATION DEFINED whether a reset into an Exception level generates an Exception Catch debug event.
- Might be taken synchronously, after the exception or reset entry or the exception return has been processed by the PE.
- Ignore the Execution state of the target Exception level.
- Might be ignored if halting is prohibited.
- If FEAT\_Debugv8p8 is implemented, might be pended.

The EDECCR register contains fields that control when Exception Catch debug events are generated.

See Controlling Exception Catch debug events when FEAT\_Debugv8p2 is implemented and Controlling Exception Catch debug events when FEAT\_Debugv8p2 is not implemented.

For exception returns, the final Exception level of the exception return determines whether an Exception Catch debug event is generated. On an illegal exception return, an Exception Catch debug event is generated only if EDECCR is programmed to generate an Exception Catch debug event for an exception return to the current Exception level.

## H3.4.1 Prioritization of Exception Catch debug events

The following rules define the prioritization of Exception Catch debug events:

- It is IMPLEMENTATION DEFINED whether Exception Catch debug events are higher or lower priority than Software Step exceptions and Halting Step debug events.
- Exception Catch debug events are higher priority than all synchronous exceptions other than Software Step exceptions and debug events other than Halting Step debug events.
- Exception Catch debug events are lower priority than Reset Catch debug events.
- When FEAT\_Debugv8p2 is implemented and FEAT\_Debugv8p8 is not implemented, Exception Catch debug events are higher priority than pending asynchronous exceptions. Otherwise, the prioritization between asynchronous exceptions, asynchronous debug events, and an Exception Catch debug event, is IMPLEMENTATION DEFINED.

Note

As described in Prioritization of Synchronous exceptions taken to AArch64 state, an exception trapping form of a Vector Catch debug event might generate a second debug exception as part of the exception entry, before the Exception Catch debug event is taken. See Vector Catch exceptions or Vector Catch exceptions.

## H3.4.2 Generating Exception Catch debug events when FEAT\_Debugv8p2 is not implemented

When an Exception Catch debug event is generated after exception entry and halting is allowed at the target of the exception, the PE halts and enters Debug state:

- The PE halts and enters Debug state before the first instruction at the handler is executed, after the exception entry has updated the program counter, PSTATE, and syndrome registers for the exception.
- The PE does not fetch instructions from the vector address before entering Debug state, if address translation is disabled in the translation regime at the target Exception level.
- Asecond unmasked asynchronous exception can be taken before the PE enters Debug state. If this second exception does not generate an Exception Catch debug event, the exception handler executed at the higher Exception level later returns to the trapped Exception level, causing the Exception Catch debug event to be generated again.

When an Exception Catch debug event is generated on exception return and halting is allowed at the target of the exception return:

- There is no prioritization between asynchronous exceptions, asynchronous debug events, and an Exception Catch debug event generated on an exception return.
- The PE halts and enters Debug state after the exception return has updated the program counter and PSTATE, and before the execution of the first instruction at the return address is completed.

Otherwise, when the PE is executing code at a given Exception level, and the corresponding EDECCR bit is 1, it is CONSTRAINED UNPREDICTABLE whether an Exception Catch debug event is generated.

Examples of this are:

- If the debugger writes to EDECCR so that the current Exception level is trapped.
- If the OS restore code writes to OSECCR so that the current Exception level is trapped.
- If the code executing in AArch32 state changes the Exception level or Security state other than by an exception return, and the target Exception level is trapped. See State and mode changes without explicit Context Synchronization events.

See also Debug state entry and debug event prioritization.

Note

It is possible to generate Exception Catch debug events:

- As a trap on all instruction fetches from the trapped Exception level as part of an instruction fetch.
- On entry to the Exception level, as described in Detailed Halting Step state machine behavior.

This is similar to the implementation options allowed for Vector Catch debug events. The architecture does not require that the event is generated following an ISB operation executed at the Exception level.

## H3.4.3 Generating Exception Catch debug events when FEAT\_Debugv8p2 is implemented and FEAT\_Debugv8p8 is not implemented

Exception Catch debug events are generated as described in Generating Exception Catch debug events when FEAT\_Debugv8p2 is not implemented, except:

- An Exception Catch debug event is generated only on exception entry or return.
- When an Exception Catch debug event is generated after exception entry and halting is allowed at the target of the exception, the PE halts and enters Debug state before any other asynchronous exception or debug event.

## H3.4.4 Generating Exception Catch debug events when FEAT\_Debugv8p8 is implemented

Exception Catch debug events are generated as described in Generating Exception Catch debug events when FEAT\_Debugv8p2 is not implemented, except:

- An Exception Catch debug event is generated only on exception entry or return.
- When an Exception Catch debug event is generated after exception entry and halting is allowed at the target of the exception, the PE sets EDESR.EC to 1, and one of the following occurs:
- -The PE halts immediately. On entry to Debug state, EDESR.EC might be 0 or 1.
- -The PE might take an unmasked asynchronous exception, changing Exception level. This means that the PE might enter a state where halting is prohibited before the PE halts and enters Debug state.
- When an Exception Catch debug event is generated on exception return and halting is allowed at the target of the exception, EDESR.EC is unchanged.
- When EDESR.EC is 1 and halting is allowed, the PE halts and enters Debug state before completing any instruction.
- When EDESR.EC is 1 and halting is prohibited, an Exception Catch debug event is pending.

- EDESR.EC is cleared to 0 upon:
- -Awrite of 1 to EDESR.EC.
- -Exit from Debug state.

Note

If EDESR.EC is 1 and the PE executes a Context synchronizing exception return from a state where halting is prohibited to a state where halting is allowed, then the Exception Catch debug event is prioritized over any synchronous exception or synchronous debug event generated by the first instruction after the Context synchronization event, other than possibly a Halting Step debug event or a Software Step exception.

## H3.4.5 Controlling Exception Catch debug events when FEAT\_RME is implemented

When FEAT\_RME is implemented, the fields EDECCR.{RLR, RLE, NSR, SR, NSE, SE} control generation of Exception Catch debug events:

- On exception entry but not on exception return.
- On exception return but not on exception entry.
- On exception entry and exception return.

Exception entry, reset and exception return Exception Catch debug events are enabled as shown in Table H3-6.

## Table H3-5 Summary of Exception Catch debug event control when FEAT\_RME is implemented

|   RLR<n> NSR<n> SR<n> |   RLE<n> NSE<n> SR<n> | Behavior on exception return to ELn   | Behavior on exception taken to ELn, and if resets are Exception Catch debug events, reset into ELn   |
|-----------------------|-----------------------|---------------------------------------|------------------------------------------------------------------------------------------------------|
|                     0 |                     0 | No action.                            | No action.                                                                                           |
|                     0 |                     1 | Halt if allowed.                      | Halt if allowed.                                                                                     |
|                     1 |                     0 | Halt if allowed.                      | No action.                                                                                           |
|                     1 |                     1 | No action.                            | Halt if allowed.                                                                                     |

## H3.4.6 Controlling Exception Catch debug events when FEAT\_Debugv8p2 is implemented

When FEAT\_Debugv8p2 is implemented and FEAT\_RME is not implemented, the fields EDECCR.{NSR, SR, NSE, SE} control generation of Exception Catch debug events:

- On exception entry but not on exception return.
- On exception return but not on exception entry.
- On exception entry and exception return.

Exception entry, reset and exception return Exception Catch debug events are enabled as shown in Table H3-6.

## Table H3-6 Summary of Exception Catch debug event control when FEAT\_Debugv8p2 is implemented and FEAT\_RME is not implemented

|   (N)SR<n> |   (N)SE<n> | Behavior on exception return to ELn   | Behavior on exception taken to ELn, and if resets are Exception Catch debug events, reset into ELn   |
|------------|------------|---------------------------------------|------------------------------------------------------------------------------------------------------|
|          0 |          0 | No action.                            | No action.                                                                                           |
|          0 |          1 | Halt if allowed.                      | Halt if allowed.                                                                                     |
|          1 |          0 | Halt if allowed.                      | No action.                                                                                           |
|          1 |          1 | No action.                            | Halt if allowed.                                                                                     |

## H3.4.7 Controlling Exception Catch debug events when FEAT\_Debugv8p2 is not implemented

When FEAT\_Debugv8p2 is not implemented and FEAT\_RME is not implemented, all Exception Catch debug events are enabled by a combination of the fields NSE and SE in EDECCR, as shown in Table H3-7.

Table H3-7 Summary of Exception Catch debug event control when FEAT\_Debugv8p2 and FEAT\_RME are not implemented

|   (N)SE<n> | Behavior on exception taken to ELn, return to ELn, and if resets are Exception Catch debug events, reset into ELn   |
|------------|---------------------------------------------------------------------------------------------------------------------|
|          0 | No action.                                                                                                          |
|          1 | Halt if allowed.                                                                                                    |

## H3.4.8 Examples of Exception Catch debug events

If EDECCR == 0x0020 , meaning that the Exception Catch debug event is enabled for Non-secure EL1, then the following exceptions generate Exception Catch debug events:

- An exception taken from Non-secure EL0 to Non-secure EL1.
- An exception return from EL2 to Non-secure EL1.
- An exception return from EL3 to Non-secure EL1.

For example, on taking a Data Abort exception from Non-secure EL0 to Non-secure EL1, using AArch64:

- ELR\_EL1 and SPSR\_EL1 are written with the preferred return address and PE state for a return to EL0.
- ESR\_EL1 and FAR\_EL1 are written with the syndrome information for the exception.
- DLR\_EL0 is set to VBAR\_EL1 + 0x400 , the synchronous exception vector.
- DSPSR\_EL0 is written with the PE state for an exit to EL1.

The following do not generate Exception Catch debug events:

- An exception taken from EL0 to EL2, in either Security state, or EL3.
- An exception return from EL2, in either Security state, to EL0.
- An exception taken from Secure EL0 to Secure EL1.
- An exception return from EL3 to Secure EL1.

## H3.4.9 Pseudocode description of Exception Catch debug events

The pseudocode functions CheckExceptionCatch() and CheckPendingExceptionCatch() are described in A-profile Architecture Pseudocode.