## H5.4 Description and allocation of CTI triggers

Table H5-1 shows the output trigger events defined by the architecture and the related trigger numbers.

Table H5-1 Allocation of CTI output trigger events

| Number   | Source   | Destination    | Event description                                                                 |
|----------|----------|----------------|-----------------------------------------------------------------------------------|
| 0        | CTI      | PE             | Debug request trigger event                                                       |
| 1        | CTI      | PE             | Restart request trigger event                                                     |
| 2        | CTI      | IRQ controller | Generic CTI interrupt trigger event                                               |
| 3        | -        | -              | Reserved                                                                          |
| 4 - 7    | CTI      | Trace unit     | OPTIONAL Generic trace external input trigger events                              |
| 8 - 15   | -        | -              | If FEAT_TRBE_EXT is implemented, then Reserved. Otherwise IMPLEMENTATION DEFINED. |

Note

Output triggers from the CTI are inputs to other blocks.

Table H5-2 shows the input trigger events defined by the architecture and the related trigger numbers.

## Table H5-2 Allocation of CTI input trigger events

| Number   | Source     | Destination   | Event description                                                                 |
|----------|------------|---------------|-----------------------------------------------------------------------------------|
| 0        | PE         | CTI           | Cross-halt trigger event                                                          |
| 1        | PE         | CTI           | Performance Monitors overflow trigger event                                       |
| 2        | PE         | CTI           | Statistical Profiling Extension sample trigger event                              |
| 3        | -          | -             | Reserved                                                                          |
| 4 - 7    | Trace unit | CTI           | OPTIONAL Generic trace external output trigger events                             |
| 8        | PETRBU     | CTI           | If FEAT_TRBE_EXT is implemented, Trace buffer stopped trigger event               |
| 9        | PETRBU     | CTI           | If FEAT_TRBE_EXT is implemented, Trace buffer management trigger event            |
| 10       | PETRBU     | CTI           | If FEAT_TRBE_EXT is implemented, Trace buffer wrap trigger event                  |
| 11 - 15  | -          | -             | If FEAT_TRBE_EXT is implemented, then Reserved. Otherwise IMPLEMENTATION DEFINED. |

Note

Input triggers to the CTI are outputs from other blocks.

Table H5-1 and Table H5-2 show the minimum set of trigger events defined by the architecture. However:

- The Generic trace external input and output trigger events are required only if the OPTIONAL trace unit is implemented. If the OPTIONAL trace unit is not implemented, these trigger events are reserved.
- Support for the generic CTI interrupt trigger event is IMPLEMENTATION DEFINED because details of interrupt handling in the system, including any interrupt controllers, are IMPLEMENTATION DEFINED. Details regarding how the CTI interrupt is connected to an interrupt controller and its allocated interrupt number lie outside the scope of

the architecture. Arm strongly recommends that implementations provide a means to generate interrupts based on external debug events.

- If FEAT\_TRBE\_EXT is implemented, then CTI input triggers 8-15 and output triggers 11-15 are reserved for use by the architecture.

If FEAT\_TRBE\_EXT is not implemented, then CTI input triggers 8-15 and output triggers 8-15 are IMPLEMENTATION DEFINED.

- The other trigger events are required by the architecture.

From the introduction of Armv8-A, an implementation can extend the CTI with additional triggers. When FEAT\_TRBE\_EXT is not implemented, these start with number eight. When FEAT\_TRBE\_EXT is implemented, these start with number 16.

## H5.4.1 Debug request trigger event

This is an output trigger event from the CTI, and an input trigger event to the PE, asserted by the CTI to force the PE into Debug state. The trigger event is asserted until acknowledged by the debugger. The debugger acknowledges the trigger event by writing 1 to CTIINTACK[0].

Note

Adebugger must poll CTITRIGOUTSTATUS[0] until it reads as 0, to confirm that the output trigger has been deasserted before generating any event that must be ordered after the write to CTIINTACK, such as a write to CTIAPPPULSE to activate another trigger.

If the PE is already in Debug state, the PE ignores the trigger event, but the CTI continues to assert it until it is removed by the debugger. See also External Debug Request debug event.

## H5.4.2 Restart request trigger event

This is an output trigger event from the CTI, and an input trigger event to the PE, asserted by the CTI to request the PE to exit Debug state. If the PE is in Non-debug state, the request is ignored by the PE.

If a Restart request trigger event is received at or about the same time as the PE enters Debug state, it is CONSTRAINED UNPREDICTABLE whether:

- The request is ignored by the PE. In this case the PE enters Debug state and remains in Debug state.
- The PE enters Debug state and then immediately restarts.

Debuggers must program the CTI to send Restart request trigger events only to PEs that are halted. To enable the PE to disambiguate discrete Restart request trigger events, after sending a Restart request trigger event, the debugger must confirm that the PE has restarted and halted before sending another Restart request trigger event. Debuggers can use EDPRSR.{SDR, HALTED} to determine the Execution state of the PE.

Note

Before generating a Restart request trigger event for a PE, a debugger must ensure any Debug request trigger event targeting that PE is cleared. Debug request trigger event describes how to do this.

The trigger event is self-acknowledging, meaning that the debugger requires no further action to remove the trigger event. The trigger event is acknowledged even if the request is ignored by the PE. See also Exiting Debug state.

## H5.4.3 Cross-halt trigger event

This is an input trigger event to the CTI, and an output trigger event from the PE, asserted by a PE when it is entering Debug state.

Note

To reduce the latency of halting, Arm recommends that an implementation issues the Cross-halt trigger event early in the committed process of entering Debug state. This means that there is no requirement to wait until all aspects of entry to Debug state have completed before issuing the trigger event. Speculative emission of Cross-halt trigger events is not allowed. The Cross-halt trigger event must not be issued early enough for a subsequent Debug request trigger event, which might be derived from the Cross-halt trigger event, to be recorded in the EDSCR.STATUS field. This applies to Debug request trigger events that are acting as inputs to the PE.

## H5.4.4 Performance Monitors overflow trigger event

This is an input trigger event to the CTI, and an output trigger event from the PE, asserted each time the PE records a Performance Monitors counter overflow. See The Performance Monitors Extension.

If the CTI supports multicycle trigger events, then the trigger event remains asserted while any of the following are true, and deasserted otherwise:

- An event counter &lt;n&gt; is implemented, the global enable control for the event counter is 1, PMINTENSET.P[n] is 1, and PMOVSSET.P[n] is 1. The global enable control is defined in Enabling PMU counters.
- PMCR.E is 1, PMINTENSET.C is 1, and PMOVSSET.C is 1.
- FEAT\_PMUv3\_ICNTR is implemented, PMCR\_EL0.E is 1, PMINTENSET\_EL1.F0 is 1 and PMOVSSET\_EL0.F0 is 1.

Note

- This does not replace the recommended connection of Performance Monitors overflow trigger event to an interrupt controller. Software must be able to program an interrupt on Performance Monitors overflow without programming the CTI.
- Events can be counted when ExternalNoninvasiveDebugEnabled() == FALSE, and, in Secure state, when ExternalSecureNoninvasiveDebugEnabled() == FALSE. Secure software must be aware that overflow trigger events are nevertheless visible to the CTI.
- This applies in both AArch64 and AArch32 states.

If the CTI does not support multicycle trigger events, then the trigger event is asserted whenever a counter overflows, causing the PE to set PMOVSSET.P[n] to 1, or a direct write to a System register means the above conditions become true.

If FEAT\_SEBEP is implemented and the overflow trigger event is asserted, PMEVTYPER&lt;n&gt;\_EL0.SYNC is ignored and the trigger event is not required to be synchronous under any circumstances.

For more information, see An ECT that supports multicycle trigger events.

## H5.4.5 Statistical Profiling Extension sample trigger event

If the Statistical Profiling Extension is implemented, and a sample record is written to memory, CTI input trigger 2 is asserted. This trigger might also be directly connected to other IMPLEMENTATION DEFINED debug features.

For more information, see The Statistical Profiling Extension.

## H5.4.6 Generic trace external input trigger events

These are output trigger events from the CTI, and input trigger events to the OPTIONAL trace unit, that are used in conjunction with the Generic trace external output trigger events to pass trigger events between:

- The PE and the OPTIONAL trace unit.
- The OPTIONAL trace unit and any other component attached to the CTM, including other Trace Units.

There are four Generic trace external input trigger events.

The trigger events are self-acknowledging. This means that the debugger does not have to take any further action to remove the events.

## H5.4.7 Generic trace external output trigger events

These are input trigger events to the CTI, and output trigger events from the OPTIONAL trace unit, used in conjunction with the Generic trace external input trigger events to pass trigger events between:

- The PE and the OPTIONAL trace unit.
- The OPTIONAL trace unit and any other component attached to the CTM, including other Trace Units.

There are four Generic trace external output trigger events.

## H5.4.8 Generic CTI interrupt trigger event

This is an output trigger event from the CTI, and an input to an IMPLEMENTATION DEFINED interrupt controller, and can transfer trigger events from the PE, trace units, or any other component attached to the CTI and CTM to software as an interrupt. The Generic CTI interrupt trigger event must be connected to the interrupt controller as an interrupt that can target the originating PE.

Note

- Armrecommendsthat the Generic CTI interrupt trigger event is a private peripheral interrupt, but implementations might instead make this trigger event available as a shared peripheral interrupt or a local peripheral interrupt.
- GICv3 reserves a private peripheral interrupt number for this interrupt.

It is IMPLEMENTATION DEFINED whether this trigger event is:

- Self-acknowledging. This means that the debugger is not required to take any further action, and that the interrupt controller must treat the trigger event as a pulse or edge-sensitive interrupt.
- Acknowledged by the debugger. The debugger acknowledges the trigger event by writing 1 to CTIINTACK[2]. This means that the interrupt controller must treat the trigger event as a level-sensitive interrupt.

Arm recommends that the Generic CTI interrupt trigger event is a self-acknowledging trigger event.

## H5.4.9 Trace buffer stopped trigger event

If FEAT\_TRBE\_EXT is implemented, the Trace buffer stopped trigger event is defined.

The Trace buffer stopped trigger event is asserted when Collection is stopped. The trigger is asserted when an event causes the PE to set TRBSR\_EL1.S to 1 and TRBSR\_EL1.S was previously 0.

This is an output trigger from the Trace Buffer Unit, and an input trigger to the CTI.

## H5.4.10 Trace buffer management trigger event

If FEAT\_TRBE\_EXT is implemented, the Trace buffer management trigger event is defined.

The Trace buffer management trigger event is asserted when a trace buffer management event occurs. The trigger is asserted when an event causes the PE to set TRBSR\_EL1.IRQ to 1 and TRBSR\_EL1.IRQ was previously 0.

This is an output trigger from the Trace Buffer Unit, and an input trigger to the CTI.

## H5.4.11 Trace buffer wrap trigger event

If FEAT\_TRBE\_EXT is implemented, the Trace buffer wrap trigger event is defined.

The Trace buffer wrap trigger event is asserted when the current write pointer wrapped to the Base pointer. The trigger is asserted when an event causes the PE to set TRBSR\_EL1.WRAP to 1, including when TRBSR\_EL1.WRAP was previously 1. The trigger is asserted regardless of the trace buffer mode.

This is an output trigger from the Trace Buffer Unit, and an input trigger to the CTI.