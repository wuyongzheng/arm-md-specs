## D1.7 Mechanisms for entering a low-power state

IRTNZD The architecture provides the following mechanisms that software can use to indicate that the PE can enter low-power state:

- Wait for Event.
- Wait for Interrupt.

## D1.7.1 Wait for Event

IZZQGW

The Wait for Event mechanism behavior depends on the interaction of all of the following:

- The Event Register for the PE. See The Event Register.
- The Wait for Event (WFE) or Wait for Event with Timeout (WFET) instruction. See The Wait for Event and Wait for Event with Timeout instructions.
- WFEwakeup events. See WFE wakeup events in AArch64 state.
- The Send Event instructions, SEV and SEVL, that can cause WFE wakeup events. See The Send Event instructions.

RTJTFC The architecture does not define the exact nature of the low-power state entered by WFE or WFET, except that when a WFEor WFET instruction is executed, memory coherency and architectural state are not lost.

IWBMQQ The Wait for Event mechanism is associated with suspending execution on a PE for power saving, therefore Arm recommends that the Event Register is set infrequently. Software must only use the setting of the Event Register as a hint, and must not assume that any particular message is sent as a result of the setting of the Event Register.

## D1.7.1.1 The Event Register

RPVKKP The Event Register is a single bit register for each PE.

ITZVVM The event register is a conceptual register and cannot be explicitly accessed.

IPDJMB If the Event Register is 1, then an event has occurred since the register was last cleared and the event might require some action by the PE.

RRJYVC

When the PE executes a WFE or WFET instruction, all of the following apply:

- If the Event Register is 0, then the PE can enter the low-power state.
- If the Event Register is 1, then all of the following apply:
- -The PE does not suspend operation.
- -The Event Register is cleared to 0.
- -The WFE or WFET instruction completes immediately.

RDDGLZ The reset value of the Event Register is UNKNOWN.

RXRZRK The Event Register for a PE is set by any of the following:

- ASend Event instruction, SEV, executed by any PE in the system.
- ASend Event Local instruction, SEVL, executed by the PE.
- An exception return.
- The clearing of the global monitor for the PE.
- An event from a Generic Timer event stream, see Event streams.
- An event sent by some IMPLEMENTATION DEFINED mechanism.

IPJZBB The Event Register is cleared only by a Wait for Event (WFE) instruction or a Wait for Event with Timeout (WFET) instruction.

IZXJPD

Software cannot read or write the value of the Event Register directly.

RQRXWZ

## D1.7.1.2 The Wait for Event and Wait for Event with Timeout instructions

If FEAT\_WFxT is implemented, the Wait for Event with Timeout (WFET) instruction is implemented

RCSKPF If the Event Register is 0, when a WFE or WFET instruction is executed, the PE can suspend execution and enter a low-power state.

RGZZQM

IQGHTM

If the PE enters a low-power state, the PE remains in the lower-power state until one of the following occurs:

- The PE detects a WFE wakeup event.
- An IMPLEMENTATION DEFINED wake event that is architecturally permitted to occur at any time.
- Areset is asserted.

The architecture permits all of the following:

- The PE is permitted to leave the low-power state for any reason.
- The PE is permitted to treat WFE as a NOP, but this is not recommended for lowest power operation.

RSLQVQ If the PE is in a low-power state, when the PE detects a WFE wakeup event, or earlier if the implementation chooses, the WFEor WFET instruction completes. If the wakeup event sets the Event Register, when execution is restarted, the state of the Event Register is IMPLEMENTATION DEFINED.

IDRSJV Software using the Wait for Event mechanism must tolerate spurious wakeup events, including multiple wakeup events.

## D1.7.1.3 Trapping of WFE and WFET

- IKMHTB The WFE and WFET instructions are available at all Exception levels. Attempts to enter a low-power state made by software executing at EL0, EL1, or EL2 can be configured to trap to a higher Exception level.

RJWKTL If FEAT\_TWED is implemented, then all of the following apply:

- Adelay before taking a WFE or WFET trap can be configured.
- If a delay before taking a WFE or WFET trap is configured, then the delay does not affect the priority of the traps.

IRDYQK For example, if execution is subject to a trap at EL1 because SCTLR\_EL1.nTWE is 0 and HCR\_EL2.TWE is 1, the only trap that will be taken is a trap to EL1, even if the delay at EL1 is longer than the delay at EL2.

## D1.7.1.4 WFE wakeup events in AArch64 state

IRJRLR In this section, AllIntMask refers to the value described in RXZPDT.

ILRPVP If a WFE or WFET instruction puts a PE into low-power state, a WFE wakeup event received by the PE causes that PE to exit low-power state.

RKBMFC All of the following are WFE wakeup events:

- The execution of an SEV instruction on any PE in a multiprocessor system.
- Any physical SError exception, physical IRQ interrupt, or physical FIQ interrupt received by the PE that is not disabled by EDSCR.INTdis and either of the following is true:
- -The interrupt is marked as A in the tables in Asynchronous exception masking, regardless of the value of the corresponding PSTATE.{A, I, F} mask bit.
- -The interrupt is marked as B in the tables in Asynchronous exception masking and any of the following are true:
- -The value of the corresponding PSTATE.{A, I, F} mask bit is 0.
- -AllIntMask is 0 and the IRQ or FIQ interrupt has Superpriority. See RMHWBP and RGFXKY.
- If all of the following apply, any virtual SError exception, virtual IRQ interrupt, or virtual FIQ interrupt received by the PE:
- -The PE is executing at EL1 or EL0.
- -The interrupt is not disabled by EDSCR.INTdis.

- -The interrupt or exception is marked as B in the table in Virtual asynchronous exception masking and any of the following are true:
- -The value of the corresponding PSTATE.{A, I, F} mask bit is 0.
- -AllIntMask is 0 and the vIRQ or vFIQ interrupt has Superpriority. See RSNLJH and RXSPSG.
- If all the following apply, any delegated SError exception received by the PE:
- -The PE is executing at EL2, EL1, or EL0.
- -The exception is not disabled by EDSCR.INTdis.
- -Either of the following is true:
- -The exception is marked as A in the table in Delegated SError exception masking.
- -The exception is marked as B in the table in Delegated SError exception masking and PSTATE.A is 0.
- If halting is allowed, an asynchronous External Debug Request debug event. For the definition of halting, see Halting allowed and halting prohibited and External Debug Request debug event.
- An event sent by the timer event stream for the PE. See Event streams.
- An event caused by the clearing of the global monitor for the PE.
- An event sent by some IMPLEMENTATION DEFINED mechanism.
- When FEAT\_WFxT is implemented, for WFET instructions, a local timeout event caused by the virtual count threshold value, expressed in CNTVCT\_EL0, being equaled or exceeded.

| FRZZX   | KBMFC                                                                                                                                                                                                                                                                                                            |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R DQRMZ | The Send Event instructions are: • SEV , Send Event: Causes an event to be signaled to all PEs in a multiprocessor system. • SEVL , Send Event Local: Causes an event to be signaled locally without requiring the event to be signaled to other PEs in a multiprocessor system.                                 |
| I FVQBK | An SEVL instruction might signal an event to other PEs by an IMPLEMENTATION DEFINED mechanism, but it is not required to do so.                                                                                                                                                                                  |
| R HTDFW | The mechanism that signals an event to other PEs is IMPLEMENTATION DEFINED.                                                                                                                                                                                                                                      |
| R RLHHM | When an event is signaled by an SEV instruction, the ordering of the event with respect to the completion of memory accesses by instructions before the SEV instruction is not guaranteed.                                                                                                                       |
| I DVZXD | Arm recommends that software includes a DSB instruction before any SEV instruction. DSB instruction ensures that no instructions, including any SEV instructions, that appear in program order after the DSB instruction, can execute until the DSB instruction has completed. See Data Synchronization Barrier. |
| R QJDQV | The SEVL instruction appears to execute in program order relative to any subsequent WFEor WFETinstruction executed on the same PE.                                                                                                                                                                               |
| I HWHBP | The behavior inR QJDQV applies without the need for any explicit insertion of barrier instructions.                                                                                                                                                                                                              |

## D1.7.2 Wait for Interrupt mechanism

| I LMJGQ   | APEcan use the Wait for Interrupt mechanism to enter a low-power state.                                                                                                                                  |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R JHZBN   | When FEAT_WFxT is implemented, the Wait for Interrupt with Timeout (WFIT) instruction is implemented.                                                                                                    |
| R DBXLJ   | Software can use the Wait for Interrupt (WFI) and Wait for Interrupt with Timeout (WFIT) instructions to cause the PE to enter a low-power state.                                                        |
| R HSPJD   | If a Wait for Interrupt (WFI) and Wait for Interrupt with Timeout (WFIT) instructions causes the PE to enter a low-power state, the PE remains in that low-power state until any of the following occur: |

IMFLXH

- The PE detects a WFI wakeup event.
- An IMPLEMENTATION DEFINED wake event that is architecturally permitted to occur at any time.
- Areset is asserted.

The architecture permits all of the following:

- The PE is permitted to leave the low-power state for any reason.
- The PE is permitted to treat WFI as a NOP, but this is not recommended for lowest power operation.
- RMRVLC When the PE leaves a low-power state that was entered because of a WFI or WFIT instruction, the WFI or WFIT instruction completes.

RHJPJY

Except for all or the following, the architecture does not define the exact nature of the low-power state:

- When a WFI or WFIT instruction is executed, the architecture requires that memory coherency is not lost.
- If the system is configured such that the WFI or WFIT instruction can be completed, then the architecture requires that the architectural state is not lost.
- IWWYXS In some implementations, based on the configuration of system specific registers, WFI can be used as part of a powerdown sequence where no interrupts will cause WFI wakeup events, and restoration of power involves resetting of the PE. In those cases, the WFI is permitted to cause a loss of architectural state, as it is assumed that this state will have been saved by software as part of the powerdown sequence before the WFI.
- ICHMWP The WFI and WFIT instructions are available at all Exception levels. Attempts to enter a low-power state made by software executing at EL0, EL1, or EL2 can be configured to trap to a higher Exception level.

## D1.7.2.1 WFI wakeup events

- ICYKVZ In this section, AllIntMask refers to the value described in RXZPDT.

RVRLPB All of the following are WFI wakeup events:

- Any physical SError exception, physical IRQ interrupt, or physical FIQ interrupt received by the PE that is marked as A or B in the tables in Asynchronous exception masking, regardless of the value of the corresponding PSTATE.{A, I, F} mask bit.
- If the PE is executing at EL1 or EL0, any virtual SError exception, virtual IRQ interrupt, or virtual FIQ interrupt received by the PE, that is marked as B in the tables in Virtual asynchronous exception masking, regardless of the value of the corresponding PSTATE.{A, I, F} mask bit.
- If the PE is executing at EL2, EL1, or EL0, any delegated SError exception received by the PE that is marked as Aor B in the table in Delegated SError exception masking, regardless of the value of PSTATE.A.
- If halting is allowed, an asynchronous External Debug Request debug event. For the definition of halting, see Halting allowed and halting prohibited and External Debug Request debug event.
- An event sent by an IMPLEMENTATION DEFINED mechanism.
- When FEAT\_WFxT is implemented, for WFIT instructions, a local timeout event caused by the virtual count threshold value, expressed in CNTVCT\_EL0, being equaled or exceeded.

| R NLVGY   | WFI wakeup events are never disabled by EDSCR.INTdis, and are never masked by the PSTATE.{A, I, F} mask bits, or by the state of AllIntMask. If wakeup is invoked by an interrupt that is disabled or masked, the interrupt is not taken.                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VCDGW   | Because debug events are WFI wakeup events, Arm recommends that Wait for Interrupt is used as part of an idle loop rather than waiting for a single specific interrupt event to occur and then moving forward. This ensures that the intervention of debug while waiting does not significantly change the function of the program being debugged. |
| I FXRXC   | If the PE is in WFxstate when a PMUCapture event occurs, it must wake-up to service the request. Arm recommends the Capture event is not treated as an IMPLEMENTATION DEFINED WFxwake-up event and the PE returns to standby after. See PMUsnapshots.                                                                                              |
| I ZQWXZ   | The architecture does not require the WFI mechanism to drain down any pending memory activity before suspending execution, and software must not rely on the WFI mechanism operating in this way.                                                                                                                                                  |

## D1.7.3 Pending Profiling exceptions

IWNMSV

IVPTQY

Apending asynchronous Profiling exception is not required to be a WFE wakeup event or WFI wakeup event. Arm recommends that a pending unmasked asynchronous Profiling exception is treated as an IMPLEMENTATION DEFINED wakeup event, to allow timely processing of the profiling event. For example, if other telemetry data needs to be collected by software from the system. However, if a Profiling exception becomes pending as the PE enters a low-power WFxstate, then the PE might not have registered the pending Profiling exception before entering the WFx state. request to the interrupt controller before entering the WFx state for it to be a wakeup event. This is due to IMPLEMENTATION SPECIFIC timings that determine whether a profiling event causes a WFx wakeup or prevents the PE

Asimilar condition applies when using PMU, SPE, or TRBE interrupts, because the PE has to have asserted the interrupt from entering the WFx state.

Note

A pending synchronous PMU Profiling exception, as described by FEAT\_SEBEP, must be taken before the WFI or WFE instruction is executed.

In IWNMSV, pending means that, if the Profiling exception were unmasked, a Profiling exception would be taken by a simple sequential execution of the program before the execution of the next instruction.

## D1.7.4 Using WFI to indicate an idle state on bus interfaces

| R TZPSV   | When all of the following are true, the IMPLEMENTATION DEFINED mechanism for entering powerdown state can be completed:                                                                                                                                                                                                                            |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R VWDWJ   | The mechanism for entering powerdown state is IMPLEMENTATION DEFINED.                                                                                                                                                                                                                                                                              |
| I FFGGG   | Although the mechanism for entering powerdown state is IMPLEMENTATION DEFINED, the WFI and WFEmechanisms are often used to enter powerdown state.                                                                                                                                                                                                  |
| R RMBKR   | If a WFI powerdown mechanism is implemented, when a WFI or WFIT instruction is executed, the PE completes all current operations and any associated bus activity also completes. When all current PE operations and associated bus activity are complete, the PE can signal to an external power controller that there is no ongoing bus activity. |
| R CLTZY   | After a WFI instruction is executed and all currently executing instructions and related bus activity has completed, the PE is waiting for an interrupt and is in idle state . If in idle state, the PE can process memory-mapped or external debug interface accesses to debug registers.                                                         |
| I CYBLG   | The indication of idle state to the system normally only applies to the non-debug functional interfaces used by the PE, not the debug interfaces.                                                                                                                                                                                                  |
| R DHHKY   | If OSDLR_EL1.DLK is 1, the PE does not signal the idle state to the control logic unless it can also guarantee that the debug interface is idle. For more information about the OS Double Lock, see Debug behavior when the OS Double Lock is locked.                                                                                              |
| I WRZGC   | In a PE that implements separate Core and Debug power domains, the debug interface referred to in this section is the interface between the Core and Debug power domains, since the signal to the power controller indicates that the Core power domain is idle. For more information about the power domains, see Power domains and debug.        |
| I RFLDH   | The exact nature of the debug interface is IMPLEMENTATION DEFINED, but the use of Wait for Interrupt as the only architecturally-defined mechanism that completely suspends execution makes it suitable as the preferred powerdown entry mechanism.                                                                                                |