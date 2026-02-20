## D4.5 About the ETE trace unit

IGBYNF

Figure D4-10 shows the stages of trace generation:

Figure D4-10 Stages of trace generation

<!-- image -->

## D4.5.1 Resetting the trace unit

RPCXJC

Atrace unit includes a trace unit reset, which resets all of the:

- Trace unit trace registers.

- Trace unit management registers.

RPTZDH

When the trace unit Core power domain is powered up, a trace unit reset is applied.

IZXRHG

It is IMPLEMENTATION DEFINED whether the system has a mechanism to initiate a trace unit reset on demand.

SWVMHS

In a PE with FEAT\_TRF, a PE Cold reset causes EDSCR.TFO to be reset to 0 which means that tracing is prohibited after the Cold reset until explicitly permitted by software. If tracing from a Cold reset is required, the debugger needs to ensure any relevant controls, including EDSCR.TFO, are programmed to permit tracing. Programming such registers might involve causing the PE to enter Debug state to ensure the registers can be programmed before the PE starts executing instructions.

RWKLGX

When a trace unit reset is applied, the trace unit resets the values of all trace unit registers to the values described in the individual register descriptions.

ICQWFH

Some other Arm trace architectures support multiple types of reset for the trace unit.

## D4.5.2 System behaviors

RGFMRH

The trace unit outputs all of the trace byte stream, without external stimulus, within finite time.

## D4.5.2.1 Behavior on enabling

RVBMLV

While both of the following are true, the trace unit is enabled:

- TRCPRGCTLR.EN is set to 1.

- The OS Lock is unlocked.

ILFBBP

Some Arm trace architectures have a dedicated trace unit OS Lock, whereas ETE depends on the PE OS Lock.

RKBFFQ

While the trace unit is enabled, the trace unit can trace all PE execution, except when any of the following are true:

- Atrace unit buffer overflow occurs.

- The authentication interface prohibits the tracing of certain pieces of code.

- FEAT\_TRF or FEAT\_TRBE prohibit the tracing of certain pieces of code.

IKCDMH

No sequences of code or PE operations are exempt from this requirement. However, while the trace unit is transitioning from an enabled to a disabled state, or from a disabled to an enabled state, some loss of trace is permitted.

IGDNWY

While the trace unit is enabled, writes to most trace unit trace registers might be ignored. It is UNKNOWN whether writes to these registers succeed. When the writes are successful, the behavior of the trace unit is UNPREDICTABLE.

SBXQJH

Trace analyzers must not write to most trace unit trace registers while the trace unit is enabled, or if TRCSTATR.IDLE indicates that the trace unit is not idle.

ITPTRW

While the trace unit is enabled or idle, all resources that are visible in the programmers' model might have unstable values. Therefore, a trace analysis tool must be aware that the following values might be dynamically changing as they are being read:

- The Counter values, indicated by the TRCCNTVR&lt;n&gt;.
- The Sequencer state, indicated by TRCSEQSTR.
- The ViewInst start/stop function, indicated by TRCVICTLR.
- The Single-shot Comparator Control status, indicated by the TRCSSCSR&lt;n&gt;.

RVNGFG When the trace unit becomes enabled, the trace unit does not reset the state of any of the resources in the trace unit, including the Counters, the Sequencer, and the ViewInst start/stop function.

SLMPNV While the trace unit is disabled, and before it is enabled, a trace analyzer ensures the trace unit resources are programmed with a valid initial state.

## D4.5.2.2 Behavior on disabling

IGZPBM While the trace unit is disabled:

- The trace unit cannot generate trace.
- The trace unit resources are disabled.

For more information, see Behavior of the resources while in the Pausing state.

RTMLTF While either of the following is true, the trace unit is disabled:

- TRCPRGCTLR.EN is set to 0.
- The OS Lock is locked.

IWSFFP Some Arm trace architectures have a dedicated trace unit OS Lock. ETE depends on the PE OS Lock.

- RZDTLK When the trace unit becomes disabled, the trace unit stops generating trace and empties the trace buffers by outputting any data in them.
- RTNYDD When the trace buffers are empty, after the trace unit has become idle after becoming disabled, TRCSTATR.IDLE indicates that the trace unit is idle.
- RTMVLW When the trace unit becomes disabled, all resources that are visible in the programmers' model retain their values and become stable at those values.
- RQVYMJ When the trace unit becomes disabled, when the resources are stable, TRCSTATR.PMSTABLE indicates that the programmers' model is stable.

RGLBHL When the trace unit becomes disabled after the trace unit has generated Event elements, the trace unit outputs the Event elements before TRCSTATR.IDLE indicates that the trace unit is idle.

RYFLJT While the trace unit is disabled, the following are true:

- No trace is generated.
- All trace unit resources and ETEEvents are disabled.

## D4.5.2.3 Behavior on flushing

IXRMWS The trace unit is allowed to buffer the trace byte stream to make efficient use of system infrastructure.

IWHZBD As the trace unit is allowed to delay the output of the trace byte stream to the system infrastructure, there are system events that require all of the trace byte stream to be observable to other observers in the system.

ICXLCR Making the trace byte stream visible to other observers is known as a trace unit flush.

RJLRQH

When any of the following occur, a trace unit flush is requested:

- The trace unit transitions from an enabled to a disabled state.
- The trace capture infrastructure requests a trace unit flush.

IKGJRL

RLHDSS

- A TSB CSYNC instruction is executed in a Trace Prohibited region while the Trace Buffer Extension is implemented and enabled.

Atrace unit flush might be requested for IMPLEMENTATION DEFINED reasons. For example:

- Before the trace unit enters either:
- -The low-power state.
- -Apowerdown state.
- The PE enters Debug state.

IZWHKM An example of a trace unit flush is one requested on an Arm AMBA ATB interface. For more information on the Arm AMBAATBinterface, see the AMBA®ATBProtocol Specification (ARM IHI 0032) .

RHGYLG

When a trace unit flush is requested, the trace unit performs the following tasks before responding to the flush request:

1. Encode any remaining elements into trace packets.
2. Complete any packets that are in the process of being generated.
3. Output all trace packets for all PE execution that occurred before the flush request was received.

ILMVMT An example of when the trace unit might need to encode remaining elements into trace packets before a trace unit flush is when there are Commit elements that are not yet encoded.

RTWBVY When a trace unit flush occurs while the trace unit is recovering from a trace unit buffer overflow, the trace unit outputs the corresponding Overflow element before responding to the flush request.

IGHKFH When a trace unit flush occurs, the trace unit either continues to generate trace or stops generating trace, depending on what condition caused the trace flush. For example, if a flush occurs because the trace unit is entering a disabled state, then tracing becomes inactive after the trace flush.

RTTDBB When a condition causes both a trace unit flush and the trace unit to stop generating trace, the trace unit stops generating trace before responding to the flush request, and before indicating that the trace unit is idle.

INHBMZ On entry to Debug state, Arm recommends that the Exception element indicating entry to Debug state is included in the flushed trace data if tracing is active.

RPFHWW When a trace unit flush is requested, the trace unit outputs the data within a finite period.

RDKFRL When a trace unit flush is requested and the cause of the flush request requires an acknowledgment, the trace unit generates the acknowledgment within a finite period.

ISCBMG The flush request mechanism on AMBA ATB is an example of a cause of a flush request that also requires an acknowledgment.

## D4.5.2.4 Low-power state

IGHHNW The low-power state in the trace unit is a mechanism to improve energy efficiency during periods where trace generation is limited.

Scenarios where the trace unit might be in the low-power state are any of the following:

- The PE is in a low-power state.
- The PE is in Debug state.

The trace unit is only permitted to be in the low-power state when any of the following are true:

- The PE is in a low-power state due to the Wait for Event mechanism.
- The PE is in a low-power state due to the Wait for Interrupt mechanism.
- The PE is in Debug state.
- The trace unit is Disabled.

## D4.5.2.5 Trace unit behavior when the PE is in a low-power state

| I MSTWP   | The PE that is being traced might support a low-power state where no execution occurs. This low-power state might be invoked, for example, when the PE executes a WFI , WFIT , WFE , or WFET instruction.                                                                                                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I DPFXN   | When the PE is in a low-power state, it might be advantageous if the trace unit also enters a low-power state.                                                                                                                                                                                                                                                                                              |
| R FBMYZ   | It is IMPLEMENTATION DEFINED whether a trace unit supports the low-power state.                                                                                                                                                                                                                                                                                                                             |
| R WMPTL   | While the trace unit is in the disabled state, the trace unit does not stop the PE from entering a low-power state.                                                                                                                                                                                                                                                                                         |
| R YLDDV   | While the trace unit is in Low-power Override Mode, the trace unit does not affect the operation of the PE.                                                                                                                                                                                                                                                                                                 |
|           | D4.5.2.6 Trace unit behavior in the low-power state                                                                                                                                                                                                                                                                                                                                                         |
| R FMXFM   | While the trace unit is enabled, when the trace unit enters the low-power state, the trace unit continues to appear enabled throughout the time it is in the low-power state.                                                                                                                                                                                                                               |
| R KQVNN   | When the trace unit enters or leaves the low-power state, the trace unit does not lose resource events that are in transition through the trace unit, except those permitted when moving through the Pausing state of the resources. For more information on the resource events that are permitted to be lost when in the Pausing state, see Behavior of the resources while in the Pausing state.         |
| I RVKHK   | Observation of resource events that are in transition through the trace unit when it enters the low-power state might not occur until after the trace unit leaves the low-power state.                                                                                                                                                                                                                      |
| R RGFJY   | While the trace unit is not in the low-power state, and before it enters the low-power state, the resources enter the Paused state. For more information on the pausing of resources, see Behavior of the resources while in the Paused state.                                                                                                                                                              |
| I MXHHN   | If WFI and WFE instructions are classified as P0 instructions, see TRCIDR2.WFXMODE, and the trace unit enters the low-power state as a result of a WFI or WFE instruction, Arm strongly recommends that the following elements are generated before the trace unit enters the low-power state: • The Atom element that represents a WFI , WFIT , WFE , or WFET instruction. • Any pending Commit elements . |
| R LBDSM   | While the trace unit is in the low-power state, the trace unit does not generate trace, including ETEEvent trace.                                                                                                                                                                                                                                                                                           |
| R MFBDT   | While the trace unit is in the low-power state, the resources remain in the state that they were in before the trace unit entered the low-power state.                                                                                                                                                                                                                                                      |
| I QXBYK   | The resources are: • The Counters. • The Sequencer. • The ViewInst start/stop function.                                                                                                                                                                                                                                                                                                                     |
| R FHYHC   | While the trace unit is in the low-power state, the trace unit drives all External Outputs low.                                                                                                                                                                                                                                                                                                             |
| R DNKDV   | While the trace-unit is in the low-power state, the PE and external debuggers ability to access the trace unit trace registers and trace unit management registers is unaffected.                                                                                                                                                                                                                           |
| R XTBQX   | While the trace unit is in the low-power state, when a trace protocol synchronization request occurs, the trace unit handles the trace protocol synchronization request correctly. For more information on how the trace unit handles trace protocol synchronization requests, see Trace protocol synchronization.                                                                                          |
| R TWQJT   | While the trace unit is in a retention state, external debugger accesses to the trace unit behave as if there is no power to the trace unit Core power domain.                                                                                                                                                                                                                                              |
| I RCXZX   | While the trace unit is in the low-power state, the trace unit might not recognize external events, such as the assertion of any External Inputs.                                                                                                                                                                                                                                                           |

| I BPQTL   | While the trace unit is in the low-power state, it is IMPLEMENTATION DEFINED whether the cycle counter continues to count or not.                                                                                                                                                                                                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VTRBC   | While the trace unit is in the low-power state, timestamp requests might be ignored.                                                                                                                                                                                                                                                                                                                                                                                 |
| I ZTDMB   | It is possible that the trace unit might intermittently leave and reenter the low-power state while the PE is in a low-power state. If this happens, the trace unit resources might become intermittently active during this time. In addition, trace generation might also become intermittently active, and this means that the trace unit might output some packets. This behavior is IMPLEMENTATION DEFINED.                                                     |
| I ZVDSF   | There is no additional requirement for the trace unit to generate a Trace Info element or Trace On element when leaving the low-power state. However, if the trace unit entered the low-power state because the PE was in Debug state, the normal requirements for restarting trace after leaving Debug state apply, including generation of a Trace On element. For more information on the PE Debug state, see Trace unit behavior while the PE is in Debug state. |
| I LQFRD   | The trace unit can be programmed so that it does not enter the low-power state, by enabling Low-power Override Mode. Low-power Override Mode is selected using TRCEVENTCTL1R.LPOVERRIDE.                                                                                                                                                                                                                                                                             |
| R VHSFL   | When Low-power Override Mode is enabled, the resources continue operating and the trace unit can generate trace.                                                                                                                                                                                                                                                                                                                                                     |
| I FRMMP   | Low-power Override Mode does not affect the operation of the PE, however it is not required to prevent the PE from entering a low-power state. This means that even though the trace unit can generate trace, it might only generate Event elements.                                                                                                                                                                                                                 |

## D4.5.3 Trace unit behavior while the PE is in Debug state

| R XJXQS   | While ViewInst is active, when the PE enters Debug state, the trace unit generates an Exception element which indicates that the PE has entered Debug state.                                                                                                                                                                                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R YMJFJ   | When the PE enters Debug state, ViewInst becomes inactive, and remains inactive throughout the time the PE is in Debug state.                                                                                                                                                                                                                                             |
| R DPKSC   | While the PE is in Debug state, the trace unit does not trace: • Instructions that are executed. • The effects of instructions that are executed. • Exceptional occurrences.                                                                                                                                                                                              |
| R HBNFJ   | When the PE exits Debug state and ViewInst becomes active, the trace unit generates a Trace On element.                                                                                                                                                                                                                                                                   |
| R TGFHM   | While the PE is in Debug state, the ViewInst start/stop function maintains its state.                                                                                                                                                                                                                                                                                     |
| I WFYLQ   | If an Exceptional occurrence occurs between the PE exiting Debug state and the PE executing the first instruction, the value of TRCRSR.TA is used to determine if the Exceptional occurrence is traced. In general, if the entry to Debug state was traced then TRCRSR.TA will be set to 1, and therefore this Exceptional occurrence on exit from Debug state is traced. |
| I NPQLT   | If a PE Reset occurs when the PE is in Debug state this is treated as leaving Debug state. This means that a Trace On element and an Exception element indicating a PE Reset are traced if tracing is not prohibited and either of the following are true: • TRCRSR.TA is 1. • Forced tracing of PE Resets is active.                                                     |

## D4.5.4 Trace unit behavior on a trace unit buffer overflow

| R PQGXB   | When a trace unit buffer overflow occurs, trace generation becomes inoperative until the trace unit can recover from the overflow.                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R RQHFH   | When a trace unit buffer overflow occurs, the trace unit does not output a partial trace packet, that is, the trace unit can only output complete packets.                                                                  |
| I TDCNT   | The Overflow element indicates to a trace analyzer that a trace unit buffer overflow has occurred. For more details on the generation of an Overflow element , see Overflow element.                                        |
| R DQBDH   | When the trace unit recovers from a trace unit buffer overflow, the following occur: • Trace protocol synchronization is requested. • Trace protocol synchronization occurs before the trace unit outputs any packets.      |
| I VQYYH   | When an Overflow packet is generated, the trace unit might output any of the following packets before it outputs an Alignment Synchronization packet: • Event packet. • Overflow packet. • Discard packet. • Ignore packet. |
| I YYNRQ   | Arm recommends that the Alignment Synchronization packet is the first packet output after the Overflow packet.                                                                                                              |

## D4.5.5 Instrumentation extension

ITLZTW

- IGRJLV

FEAT\_ITE provides a mechanism to allow software to inject instrumentation information into the ETE trace stream, allowing the ETE trace to be augmented with software-defined information that can aid with debugging and interpretation of the ETE trace.

Examples of instrumentation information include the following:

- Context information about the program being executed.
- Parameters to functions.
- Data addresses and values of variables and other data structures.

All of the following registers control the behavior of FEAT\_ITE:

- TRCITECR\_EL1, providing EL1 with controls over FEAT\_ITE.
- TRCITECR\_EL2, providing EL2 with controls over FEAT\_ITE.
- TRCITEEDCR, TRCCONFIGR and EDSCR.TFO, providing an external debugger with controls over FEAT\_ITE.
- MDCR\_EL3.EnITE, providing an EL3 trap control over access to TRCITECR\_EL1 and TRCITECR\_EL2.
- HDFGRTR2\_EL2.nTRCITECR\_EL1 and HDFGWTR2\_EL2.nTRCITECR\_EL1, providing EL2 trap controls over access to TRCITECR\_EL1.

ICMDFW The controls provided in TRCITECR\_EL1 and TRCITECR\_EL2 are similar in function to TRFCR\_ELx provided for FEAT\_TRF.

RFLGVJ

RRTKDL

RDKCFL

If self-hosted trace is enabled, then the controls in TRCITECR\_EL1 and TRCITECR\_EL2 control when Instrumentation trace is prohibited.

See TraceInstrumentationAllowed() .

If self-hosted trace is disabled and TRCCONFIGR.ITO is 1, then the fields in TRCITEEDCR control when Instrumentation trace is prohibited.

See TraceInstrumentationAllowed() .

If self-hosted trace is disabled and TRCCONFIGR.ITO is 0, then the fields in TRCITEEDCR, TRCITECR\_EL1, and TRCITECR\_EL2 control when Instrumentation trace is prohibited.

See TraceInstrumentationAllowed() .

ISRTGR

TRCCONFIGR.ITO and TRCITEEDCR allow an external debugger to one of the following:

- Completely control when Instrumentation trace is allowed and prohibited.
- Share control of when Instrumentation trace is allowed with software running on the PE.

## D4.5.6 Trace unit power states

| I GNFXM   | The Arm architecture defines the following power states: Normal                                                                                                                 |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I MNDVQ   | Atrace unit might support a low-power state, which is equivalent to the standby state.                                                                                          |
| I BMSVN   | Atrace unit might support a retention state or a powerdown state, and both of these states are considered to be a state where the trace unit Core power domain is powered down. |
| I ZVBZF   | If the trace unit is implemented in a power domain which is separate from the PE power domain, all of the following are                                                         |
|           | true: • The trace unit Core power domain might be able to be powered down without powering down the PE power domain.                                                            |
| I CNZJH   | Aread of TRCPDSR returns information about the current state of the trace unit. Table D4-21 describes the meanings of the returned value.                                       |

## Table D4-21 Meaning of TRCPDSR values

| STICKYPD   | POWER                                                                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | 0b1                                                                                                                                                                                                                                                                                                           | The trace unit Core power domain is powered and the trace unit registers are accessible.                                                                                                                                                                                                                      |
| 0b1        | 0b1                                                                                                                                                                                                                                                                                                           | The trace unit Core power domain is powered and the trace unit registers are accessible. Atrace unit reset or power interruption has occurred so the trace unit register state might not be valid.                                                                                                            |
| R CMKXK    | When the trace unit Core power domain transitions from powered down to powered up, if the trace unit register state has been preserved over the powerdown, then TRCPDSR.STICKYPD is restored to the value before powerdown.                                                                                   | When the trace unit Core power domain transitions from powered down to powered up, if the trace unit register state has been preserved over the powerdown, then TRCPDSR.STICKYPD is restored to the value before powerdown.                                                                                   |
| R FQMXQ    | When the trace unit Core power domain transitions from powered down to powered up, if the trace unit register state has not been preserved over the power down then TRCPDSR.STICKYPD is set to 0b1 . Note                                                                                                     | When the trace unit Core power domain transitions from powered down to powered up, if the trace unit register state has not been preserved over the power down then TRCPDSR.STICKYPD is set to 0b1 . Note                                                                                                     |
| I FRMBB    | Asystem might support a Debug power domain that contains the interface between the trace unit and the external debugger. The Debug power domain usually needs to be powered up when the external debugger needs to connect to the system. Such a Debug power domain is described in Resets and power domains. | Asystem might support a Debug power domain that contains the interface between the trace unit and the external debugger. The Debug power domain usually needs to be powered up when the external debugger needs to connect to the system. Such a Debug power domain is described in Resets and power domains. |

| R GYLKD   | If the trace unit Core power domain can be powered down independently of the Debug power domain, Arm recommends that the system implements an external debug component with a powerup request mechanism which can request the trace unit Core power domain to be powered up.                                                                                                                                    |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZNSNS   | Arm strongly recommends the powerup request mechanism is a CoreSight Class 0x9 ROMTable containing a parent entry for the trace unit. Aparent entry of a component is one of: • An entry in the ROMtable that locates the component. • An entry in a first ROMtable that locates a second ROMtable that includes a parent entry for the component. The second ROMtable is a descendant of the first ROMtable.   |
| I TLYXG   | This definition of a parent entry is recursive, and therefore the powerup request mechanism might be high up in a hierarchy of ROMtables. The ROMtable and any descendants might describe other debug components, including debug components for other PEs. The ROMtable might have parent entries in other ROMtables, and those parent entries might also have a powerup request mechanism in those ROMtables. |
| R ZPCZC   | If the powerup request mechanism is implemented, in the Class 0x9 ROMTable containing the powerup request mechanism for the trace unit: • The POWERIDVALID bit in the parent entry must be 0b1 . • The POWERID field in the parent entry has an IMPLEMENTATION DEFINED value.                                                                                                                                   |
| I DXHPS   | It is IMPLEMENTATION DEFINED whether the trace unit Core power domain is the PE Core power domain or some other power domain. For more information on the CoreSight Class 0x9 ROMTable, see the Arm ® CoreSight™ Architecture Specification (ARM IHI 0029).                                                                                                                                                     |

## D4.5.7 Visibility of the PE operation

| I BMPFH   | This section describes the ability of the trace unit to trace the execution of the operation of the PE.                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QCFMC   | When the trace unit performs indirect reads of PE System registers, the trace unit complies with the rules associated with Context synchronization events.                                                                                                                                                                                                                                                                                                                                      |
| R QHTYC   | When the trace unit performs indirect reads of PE System registers, the trace unit complies with the rules associated with the TSB CSYNC instruction as defined in The Trace Buffer Extension.                                                                                                                                                                                                                                                                                                  |
| R QCFSS   | When instructions are executed outside of any Trace Prohibited region, the trace unit observes the execution.                                                                                                                                                                                                                                                                                                                                                                                   |
| R CDNKX   | When observable instructions are executed, the trace unit observes all execution before a PE Context synchronization event occurs, as defined in The Trace Buffer Extension.                                                                                                                                                                                                                                                                                                                    |
| R QMBKJ   | When an Exceptional occurrence occurs outside of any Trace Prohibited region, the trace unit observes the Exceptional occurrence .                                                                                                                                                                                                                                                                                                                                                              |
| I XBJFP   | Executing a TSB CSYNC instruction generates a Trace synchronization event as defined in The Trace Buffer Extension.                                                                                                                                                                                                                                                                                                                                                                             |
| R FCBLJ   | When a TSB CSYNC instruction is executed in a Trace Prohibited region, the TSB CSYNC instruction does not become microarchitecturally-finished until the resources are in the Paused state or the trace unit is in the Idle or Stable state.                                                                                                                                                                                                                                                    |
| I JYJDZ   | While the PE is outside a transaction, after a TSB CSYNC instruction executed inside a Trace Prohibited region generates a Trace synchronization event, the Trace synchronization event is microarchitecturally-finished when the trace operation has microarchitecturally-finished for every instruction before the Context synchronization event before the TSB CSYNC instruction that generated the Trace synchronization event. For more details on the TSB CSYNC instruction, seeR MRVPT . |
| R TSLRT   | While the PE is inside a transaction, when a Trace synchronization event occurs, the Trace synchronization event becomes microarchitecturally-finished within a finite period.                                                                                                                                                                                                                                                                                                                  |
| I HNSGS   | While the PE is inside a transaction, the completion of a Trace synchronization event is not dependent on the resolution of the transaction. It might still depend on other aspects of the trace operation.                                                                                                                                                                                                                                                                                     |

| R XLVQM   | When a TSB CSYNC instruction executed in a Trace Prohibited region becomes microarchitecturally-finished, the trace unit generates no more trace until the PE leaves the Trace Prohibited region.                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I CZLXW   | When a TSB CSYNC is executed in a Trace Prohibited region, the rules around generation of a trace flush and requiring no more trace to be generated in the Trace Prohibited region mean that only whole trace packets are output, and the last byte output is the end of a packet. |
| I GSXJJ   | These rules ensure that no new trace is generated and allows various System registers to be changed, such as those controlling the Trace Buffer Extension, without the risk of any trace being generated while those registers are being changed.                                  |
| R XRWPV   | When the trace unit becomes enabled in a Trace Prohibited region, the trace unit generates no trace until the PE leaves the Trace Prohibited region. Note                                                                                                                          |
| I KXDDS   | The trace operation as defined in The Trace Buffer Extension can be split into operations that are performed by one of the following: • The PE. • The ETE trace unit. • The trace buffer. The operation of the trace unit is defined by the ETE trace operation .                  |
| R RFJQN   | If the Trace Buffer Unit is implemented and enabled, when a Trace synchronization event occurs, and after all of the trace byte stream generated by the trace unit is flushed to the trace buffer, the Trace synchronization event completes.                                      |
| I CNJYL   | Table D4-22 describes the labels used in the ordering diagrams present in this Chapter.                                                                                                                                                                                            |

## Table D4-22 Labels for ordering diagrams

| Notation   | Name                        | Description                                                                                                                                                                                                                              |
|------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| po         | program-order               | head is in program order after tail .                                                                                                                                                                                                    |
| rf         | Reads-from                  | tail Reads-from head .                                                                                                                                                                                                                   |
| co         | Coherence-after             | head is Coherence-after tail .                                                                                                                                                                                                           |
| fr         | from-read                   | As co , except that the operation at head is a read.                                                                                                                                                                                     |
| ob         | Observed-by                 | tail is Observed-by head . Only applies for different Observers.                                                                                                                                                                         |
| tb         | traced-by                   | head is the trace operation for the instruction at tail .                                                                                                                                                                                |
| gb         | generated by                | head is an operation generated by the instruction at tail .                                                                                                                                                                              |
| seo        | speculative execution-order | The PE speculated that the instruction at head was executed after tail , but the instruction was later Canceled or was part of a Transaction that Failed or was Canceled. An seo arrow might be paired with a can arrow that shows this. |
| can        | canceled                    | The instruction at tail was Canceled when the instruction at head was resolved, or the Transaction containing tail Failed or was Canceled.                                                                                               |

## D4.5.7.1 ETE trace operation

Each instruction has all of the following state information:

- PC.
- PSTATE.T.

RYCJXC

IJTLPL

IFKTKY

ILLKFT

- PSTATE.EL.
- The Security state.
- CONTEXTIDR\_EL1.PROCID.
- CONTEXTIDR\_EL2.PROCID.
- TRFCR\_EL1.
- TRFCR\_EL2.
- MDCR\_EL3.STE.
- TxNestingLevel.

IGCLMS The trace information generated contains Address information in Target Address elements , Source Address elements , Exception elements , and Qelements . The Address information contains:

- The virtual address of an instruction.
- The instruction set, known as the sub\_isa.

The trace information generated contains Context information in Context elements . The Context information contains:

- The current Security state.
- The current Exception level.
- The current Execution state.
- The current Context identifier, as stored in CONTEXTIDR\_EL1.PROCID.
- The current Virtual context identifier, as stored in CONTEXTIDR\_EL2.PROCID.

RWBCRN When an instruction is executed and all the trace elements for the instruction have been generated, the trace operation for the instruction is complete.

- IWXNXB Trace elements generated for an instruction might include:
- Global timestamp elements.
- Cycle count elements.
- Speculation resolution elements.
- Transaction resolution elements.

For example, the tracing of PE execution is where:

- Resolved instruction A is executed in program order before a Resolved instruction B.
- tA is all the trace elements that are generated due to the tracing of instruction A.
- tB is all the trace elements that are generated due to the tracing of instruction B.
- The trace elements for tA must be observed before tB.

This is shown in Figure D4-11.

## D4.5.7.2 Impact on PE behavior

The ETE architecture places no requirements on the impact that trace generation has on the functional performance of a PE. Arm expects that trace unit implementations are designed according to the market requirements of the PEs being traced, and according to the trace requirements for those PEs. For some markets and trace requirements, the trace solution might always have some performance impact on the PE and the ETE architecture does not prohibit this.

Figure D4-11 Trace operation

<!-- image -->

## D4.5.7.3 Behavior on a PE Warm reset

| R YYHBF   | APEWarmreset does not cause a Trace unit reset. Note This ensures that tracing is possible through a PE Warm reset.                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I QBSCX   | APEWarmreset might occur at the same time as a Trace unit reset, however, these are asynchronous and unrelated events.                                                                                                                                                                       |
| I TYXHR   | How instructions are executed can vary significantly between PE designs. To allow for these variations the ETE architecture allows some flexibility within the filtering model. Rather than applying the filtering model to individual instructions it is applied to blocks of instructions. |
| R BQTBL   | An instruction block contains one or more instructions.                                                                                                                                                                                                                                      |
| R GDZBX   | An instruction block can contain zero or one P0 instruction .                                                                                                                                                                                                                                |
| R CVJQH   | When an instruction block is generated which contains a P0 instruction , the instruction block has the P0 instruction as the last instruction in the block.                                                                                                                                  |
| R HPJTP   | Exceptional occurrences do not occur between instructions in an instruction block.                                                                                                                                                                                                           |
| R LDJXZ   | The addresses of the instructions within an instruction block are sequential.                                                                                                                                                                                                                |
| I JCQHC   | The number of instructions in a block can vary from block to block and can vary each time the same sequence of instructions are executed.                                                                                                                                                    |
| I HRBJG   | For example, the tracing of an instruction block is where:                                                                                                                                                                                                                                   |

- Resolved instruction A is executed in program order before a Resolved instruction B.
- tA is all the trace elements that are generated due to the tracing of instruction A.
- tA is all the trace elements that are generated due to the tracing of instruction B.

This is shown in Figure D4-12.

## D4.5.7.5 Exposing speculation

| I DCDNQ   | For some PE microarchitectures, the tracing of execution-order only might not be achievable. The ETE architecture provides the ability to trace speculatively executed instructions.   |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R TRVLX   | When speculative instructions are observed, the trace unit indicates whether each instruction is resolved or canceled with a resolve operation or a cancel operation.                  |
| R PPJSK   | Aresolve operation indicates that one or more instructions have, or will be, architecturally executed.                                                                                 |
| R WZBLY   | Acancel operation indicates that one or more instructions, although observed by the trace unit, did not architecturally execute.                                                       |

Figure D4-12 Instruction block trace operation

<!-- image -->

IKQYZB

There is no requirement to expose any speculation to the trace unit.

IDKDHD

For example, the tracing of speculation execution is where:

- S is executed in speculative execution-order after a Resolved instruction A.
- Ais executed in program order before a Resolved instruction B.
- S is not in speculative execution-order after B.
- Qis executed in speculative execution-order after a Resolved instruction B.

This is shown in Figure D4-13.

## D4.5.7.6 Trace Prohibited Regions

| I THCBC   | Trace Prohibited regions are instruction address regions or periods of execution by the PE that are not to be traced. Instructions and Exceptional occurrences which are not prohibited are not necessarily traced because the trace unit has a number of trace filtering functions to limit the amount of trace generated to the sections or periods of interest.                                                                                                                             |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I RJYNL   | An executable program might contain regions of code that are prohibited to trace. These regions might be associated with another Security state, or with the PE entering a privileged mode so that it can execute the instructions that are contained within them. Tracing might be prohibited while the PE is operating in certain states or modes. For example: • Non-invasive debug might be prohibited while the PE is in Secure, Realm, or Root state. • FEAT_TRF might prohibit tracing. |
| I ZPXRJ   | The Trace Buffer Extension describes when FEAT_TRBE prohibits tracing.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| R HYZLQ   | If an optional authentication interface is implemented, while non-invasive debug is disabled in a Security state other than Non-secure state according to that optional authentication interface and while self-hosted trace is disabled, then for execution in that Security state, the PE executes in a Trace Prohibited region.                                                                                                                                                             |
| I NVSDD   | An example of an optional authentication interface is the CoreSight Authentication interface. For more information, see the Arm ® CoreSight™ Architecture Specification (ARM IHI 0029).                                                                                                                                                                                                                                                                                                        |
| R FFVYM   | While the PE is executing code from a Trace Prohibited region, the trace unit does not trace instructions or Exceptional occurrences, including PE Resets.                                                                                                                                                                                                                                                                                                                                     |
| R KTMLZ   | While the PE is executing code from a Trace Prohibited region, instruction Address Comparators do not match on any instructions in the Trace Prohibited region.                                                                                                                                                                                                                                                                                                                                |
| R SZRZR   | While cycle counting is enabled and the PE is executing code from a Trace Prohibited region, the cycle counter continues to count.                                                                                                                                                                                                                                                                                                                                                             |

po

Figure D4-13 Observation of Speculative Trace operation

<!-- image -->

| I MCCBH   | When the PE leaves a Trace Prohibited region and tracing restarts, the cycle counter includes cycles spent in the Trace Prohibited region in the cycle count.                                                                                                                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I SDSGK   | The behavior of the resources when entering a Trace Prohibited region is defined in Behavior of the resources while in the Paused state.                                                                                                                                                                                                                                                                                                                                               |
| R VHRGM   | While the PE is executing code from a Trace Prohibited region, the trace unit does not output any trace that might provide information about the execution in the Trace Prohibited region.                                                                                                                                                                                                                                                                                             |
| I JSKLD   | Examples of information about execution in a Trace Prohibited region that trace might provide are the context of execution, instruction addresses, and the address of the first instruction in the Trace Prohibited region.                                                                                                                                                                                                                                                            |
| I MKQWS   | The most common cause of an entry into a Trace Prohibited region is an Exceptional occurrence or Context synchronization event.                                                                                                                                                                                                                                                                                                                                                        |
| R THBVD   | When an Exceptional occurrence that must be traced causes the PE to enter a Trace Prohibited region, the trace unit generates an Exception element that indicates the exception type.                                                                                                                                                                                                                                                                                                  |
| R CKZMR   | When the PE enters a Trace Prohibited region and there are unresolved speculative P0 elements remaining in the trace byte stream, when the resolution of the speculative elements is known the trace unit generates the appropriate Commit elements or Cancel elements .                                                                                                                                                                                                               |
| R RXMJF   | When the PE leaves a Trace Prohibited region and ViewInst is active, that is, any filtering applied dictates that ViewInst is active, the trace unit generates a Trace On element .                                                                                                                                                                                                                                                                                                    |
| I QGFJF   | The purpose of the trace unit generating a Trace On element when the PE exits a Trace Prohibited region and ViewInst active is to indicate to the trace analyzer that there has been a discontinuity in the trace element stream.                                                                                                                                                                                                                                                      |
| I JBFTB   | If the PE leaves a Trace Prohibited region other than when a Context synchronization event occurs, the Trace Prohibited region is permitted to extend up to the next Context synchronization event. Typically, a PE leaves a Trace Prohibited region via a Context synchronization event, but a PE might leave a Trace Prohibited region when the authentication interface changes, or when moving from a higher Security state to a lower Security state without an exception return. |
| I DMXPF   | If an Exceptional occurrence occurs between the PE exiting a Trace Prohibited region and the PE executing the first instruction, the value of TRCRSR.TA is used to determine if the Exceptional occurrence is traced.                                                                                                                                                                                                                                                                  |
|           | D4.5.7.7 Multi-threaded processor                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R KBZTZ   | Processors with multiple threads or PEs have a trace unit for each thread or PE.                                                                                                                                                                                                                                                                                                                                                                                                       |
| I KHSWQ   | The processor might support enabling and disabling of threads, either at PE Reset time or dynamically. The trace units for the threads that are disabled might behave in one of the following ways: • The trace unit Core power domain is powered down.                                                                                                                                                                                                                                |
| I RFSNL   | Arm recommends that the trace units for threads that are permanently disabled are not visible: either they are not included, or they are marked as not present in any ROMtables that describe the system.                                                                                                                                                                                                                                                                              |
|           | D4.5.7.8 Sharing between multiple PEs                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| I TSWXS   | Previous Trace architectures have allowed the trace unit to be shared between multiple PEs.                                                                                                                                                                                                                                                                                                                                                                                            |
| R TLJSQ   | Atrace unit only traces a single PE, that is, it cannot be shared between multiple PEs.                                                                                                                                                                                                                                                                                                                                                                                                |

## D4.5.8 Speculation resolution

IRKYCD

The trace unit implements a maximum speculation depth, that is, the maximum permitted number of P0 elements that can be speculative at any instance. TRCIDR8.MAXSPEC indicates the IMPLEMENTATION DEFINED maximum speculation depth.

RGLQPL

IKCFGW

IQLKDL

IHRDQL

ISMGSG

The trace unit never outputs more speculative P0 elements than the maximum speculation depth.

If a trace unit is not exposed to any speculative execution, then Arm recommends that the trace unit implements a maximum speculation depth of zero, and in this case:

- Cancel elements are not generated.
- Commit elements are generated after each P0 element , causing each P0 element to be immediately resolved when it is generated. The instruction trace protocol implicitly generates these Commit elements for each P0 element , meaning that explicit Commit packets are not required.
- Mispredict elements are not generated.

The ETE architecture defines Commit element and Cancel elements to allow the speculation of the P0 elements to be resolved by the trace analyzer. The trace unit is required to calculate the number of P0 elements which are committed or canceled. There are many methods by which these numbers can be calculated, but in the generic case the trace unit can use the following mathematical procedure.

The PE can speculatively indicate blocks of instructions to the trace unit. Each block of instructions is given a tag where tag belongs to 0 . . . m and m is the number of rewind points supported by the PE.

The number of instructions per block can be random from the set N and there is a maximum of one P0 instruction per block. The order in which the tags are used can be random, but a tag cannot be reused until the previous block with that tag has been resolved, canceled or merged.

This procedure generates a transform from the potentially random sequence of core tags to a more usable space. The transform T evolves over time as the tags are reused and provides the mapping onto the new space,

<!-- formula-not-decoded -->

ci is the mapping for core tag i .

ci belongs to 0 . . . q , where q is greater than m .

## D4.5.8.1 Initialization

To perform the necessary calculations, the trace unit tracks the transform of the last resolved block. γ t is the last committed indicator. The algorithm is initialized at t=0 to

<!-- formula-not-decoded -->

## D4.5.8.2 New block operation

The sequence of the numbers in the transformed space, xt, is defined by the following equation:

IBJFLR

IHJYQH

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## D4.5.8.3 Resolved operation

The PE can resolve one or more blocks in an atomic operation. This is performed by indicating the youngest block's tag to be resolved, and by inference all older blocks.

The number required by the Commit element is calculated by

The state of the transform is updated by where l is the youngest block' s tag .

## D4.5.8.4 Cancel operation

The PE can cancel one or more blocks in an atomic operation. This is performed by indicating the oldest block to be canceled.

The number required by the Cancel element is calculated by

The state of the transform is updated by where r is the oldest block' s tag .

If a traced P0 instruction

Otherwise

If a traced P0 instruction

Otherwise

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## D4.5.9 Filtering trace generation

ICCWZG

The amount of trace that can be generated by the trace unit can be significant. Not all the operations of the PE are always relevant. The amount of trace generated can be reduced by the use of the trace unit filter functions.

## D4.5.9.1 ViewInst function

RGQFSB

The filtering function of the instruction trace is expressed as a calculation evaluated for each instruction.

<!-- formula-not-decoded -->

<!-- image -->

S i = ViewInst start/stop function

I i = ViewInst include/exclude function

E i = Exception level filtering

N i = Resource event based filtering

RBZXFH

While ViewInst is high, the trace unit traces all instructions.

IMJMCV

Instructions for which ViewInst is low might be traced. This might be as a result of tracing the next P0 element or optimizations in the trace unit.

RXPNZL

When ViewInst is high for an instruction in an instruction block, the trace unit traces the entire instruction block.

RKHDNX When ViewInst becomes high, the trace unit traces the next P0 instruction or Exceptional occurrence.

INSMSV

Some instruction types cause the trace unit to generate P0 elements , so that they are explicitly traced. Other instruction types however are not explicitly traced. The execution of these other instruction types can be inferred from the P0 elements . This means that the following scenario is possible:

- While ViewInst is high, some instructions are executed. This means that ViewInst is indicating that those instructions must be traced. However, none of the executed instructions cause the trace unit to generate a P0 element , therefore none of the instructions are traced.

- ViewInst then goes low.

- The PE then executes an instruction that, whenever ViewInst is high, causes the trace unit to generate a P0 element .

In this scenario, although ViewInst is low when the instruction in step 3 is executed, indicating that the instruction is not traced, tracing of the instruction is permitted because this is the only way that the preceding instructions can be traced.

IFGSBW

There is no requirement for the target address of a P0 instruction or Exceptional occurrence to be traced if ViewInst has transitioned to a low state by the time program execution has moved to the target.

ILCXHX

Unless the target instruction block is traced, any Target Address elements indicating the target address of a P0 instruction or Exceptional occurrence cannot be relied on.

## D4.5.9.1.1 Resource event based filtering

RBQNWP

The resource event based filtering part of the ViewInst function is expressed as the following equation:

## N i = Fn(TRCVICTLR.EVENT.SEL , TRCVICTLR.EVENT.TYPE)

Where Fn(TRCVICTLR.EVENT.SEL, TRCVICTLR.EVENT.TYPE) selects the combination of Resource Selectors used for resource event based filtering.

IKMXNS The timing of the resource event based filtering is IMPLEMENTATION SPECIFIC.

IDWWVR

Resource event based filtering can be used to make ViewInst active based on system conditions or on trace unit resources. For example:

- Sampling based on cycle counts.

- Activating tracing on the n th function call.

- Performance Monitoring Unit events.

RNBYKR When an instruction block is processed by the trace unit during a cycle, the trace unit samples the ViewInst function resource event input during that cycle.

RSRMMD When no instruction blocks are processed by the trace unit during a cycle, the trace unit does not sample the ViewInst function resource event input during that cycle.

## D4.5.9.1.2 Exception level filtering

IHNPYV This function provides a simple method of filtering out information about different Exception levels without the need to use of additional resources.

RLWYJR The Exception level based filtering part of the ViewInst function is expressed as the following equation:

|   ¬ TRCVICTLR.EXLEVEL S EL0                                             | Secure EL0     |
|---------------------------------------------------------------------------|----------------|
|      ¬ TRCVICTLR.EXLEVEL S EL1                                       | Secure EL1     |
|      ¬ TRCVICTLR.EXLEVEL S EL2                                       | Secure EL2     |
|     ¬ TRCVICTLR.EXLEVEL S EL3                                         | EL3            |
|      ¬ TRCVICTLR.EXLEVEL NS EL0                                      | Non-secure EL0 |
|      ¬ TRCVICTLR.EXLEVEL NS EL1                                      | Non-secure EL1 |
|   ¬ TRCVICTLR.EXLEVEL NS EL2                                            | Non-secure EL2 |
|         ¬ (TRCACATRn.EXLEVEL RL EL0 ⊕ TRCACATRn.EXLEVEL NS EL0)   | Realm EL0      |
|         ¬ (TRCACATRn.EXLEVEL RL EL1 ⊕ TRCACATRn.EXLEVEL NS EL1)   | Realm EL1      |
|          ¬ (TRCACATRn.EXLEVEL RL EL2 ⊕ TRCACATRn.EXLEVEL NS EL2) | Realm EL2      |

IPJQSC

## D4.5.9.2 ViewInst start/stop function filtering

The ViewInst start/stop function is useful when the requirement is to trace a particular piece of code with all the functions that the piece of code calls.

The ViewInst start/stop function uses the Single Address Comparators and the PE Comparator Inputs to define start points and stop points.

Astart point is any of the following:

- The instruction address which matches a Single Address Comparator selected for the ViewInst start/stop function using TRCVISSCTLR.START.
- The instruction address which matches a PE Comparator selected for the ViewInst start/stop function using TRCVIPCSSCTLR.START.

Astop point is any of the following:

- The instruction address which matches a Single Address Comparator selected for the ViewInst start/stop function using TRCVISSCTLR.STOP.
- The instruction address which matches a PE Comparator selected for the ViewInst start/stop function using TRCVIPCSSCTLR.STOP.

Multiple start points can be selected. Multiple stop points can be selected.

RMVDJT When a start point is encountered, the ViewInst start/stop function becomes active for the instruction at the start point.

RCDFBP When a stop point is encountered, the ViewInst start/stop function becomes inactive immediately after the instruction at the stop point.

RLMQPR When the ViewInst start/stop function causes ViewInst to become active, the trace unit traces the instruction at the start address.

RBWXLS When the ViewInst start/stop function causes ViewInst to become inactive, the trace unit traces up to and including the instruction at the stop address.

RXHFYQ While a ViewInst start/stop function start address is the same as a stop address, the behavior of the ViewInst start/stop function is UNPREDICTABLE.

RKCYTR The ViewInst start/stop function part of the ViewInst function is expressed as the following equations:

<!-- formula-not-decoded -->

If TRCIDR4.NUMPC == 0b0000 , then:

If TRCIDR4.NUMPC != 0b0000 , then:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

| R MVFYN   | The following have no effect on the ViewInst start/stop function:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GRSVY   | When disabling the trace unit, the ViewInst start/stop function becomes static and retains its state until the trace unit is enabled again.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| S XMMLP   | For each of TRCVICTLR.SSSTATUS, TRCVISSCTLR, and TRCVIPCSSCTLR, if the register is implemented, it must be programmed with an initial state when the trace unit is programmed before a trace session.                                                                                                                                                                                                                                                                                                                                                                          |
| R HYLDM   | If an implementation makes speculation visible to the trace unit, the ViewInst start/stop function behaves as if no speculation has occurred. That is, when the instruction at a start or stop point is executed speculatively and is canceled, the ViewInst start/stop function behaves as if the instruction at the start or stop point was not                                                                                                                                                                                                                              |
|           | later executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| R BZSXR   | When the trace unit becomes disabled and there are instructions at start points or stop points which are still speculative, the behavior of the ViewInst start/stop function is IMPLEMENTATION DEFINED and one of the following: • The ViewInst start/stop function behaves as if the instructions at the start points or stop points were incorrectly speculated. That is, the trace unit behaves as if those start points and stop points did not occur. • The ViewInst start/stop function behaves as if the instructions at the start points or stop points were correctly |
| R HMKSZ   | When mis-speculation occurs and the PE returns to a point in execution before the trace unit was enabled, the ViewInst start/stop function reverts to the state it was in when the trace unit became enabled.                                                                                                                                                                                                                                                                                                                                                                  |
| R CYQZV   | When a transaction failure occurs the ViewInst start/stop function reverts back to the state to point immediately after the TSTART instruction for the outer transaction. This is the value of TRCVICTLR.SSSTATUS for the instruction block that contains the TSTART instruction for the outer transaction.                                                                                                                                                                                                                                                                    |
| R ZBTPF   | When a transaction failure causes the PE to return to a point in execution before the trace unit was enabled, the ViewInst start/stop function reverts to the state it was in when the trace unit became enabled.                                                                                                                                                                                                                                                                                                                                                              |
| R LRBDC   | When the trace unit becomes disabled and the PE is executing in Transactional state, the behavior of the ViewInst start/stop function is IMPLEMENTATION DEFINED and one of the following:                                                                                                                                                                                                                                                                                                                                                                                      |

|         | • The ViewInst start/stop function behaves as if the transaction failed. That is, the trace unit behaves as if those start points and stop points did not occur. • The ViewInst start/stop function behaves as if the transaction was successful. That is, the trace unit updates the                                                                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FFZDC | state of the ViewInst start/stop function as if those start points and stop points occurred. When tracing becomes prohibited and the PE is executing in Transactional state, the behavior of the ViewInst start/stop function is IMPLEMENTATION DEFINED and one of the following: • The ViewInst start/stop function behaves as if the transaction failed. That is, the trace unit behaves as if those              |
| R PBFMY | When the state of the ViewInst start/stop function is changed by anything other than a direct write to TRCVICTLR, the PE considers the write to be an indirect write to TRCVICTLR.SSSTATUS.                                                                                                                                                                                                                         |
| I BVYPM | In many common usage scenarios, entry to a Trace Prohibited region or disabling of the trace unit does not occur while in a transaction.                                                                                                                                                                                                                                                                            |
|         | D4.5.9.2.1 Instruction blocks                                                                                                                                                                                                                                                                                                                                                                                       |
| R PTTKL | When an instruction block that contains instructions at ViewInst start points and no instructions at ViewInst stop points is executed, the ViewInst start/stop function remains active for the entire instruction block.                                                                                                                                                                                            |
| R WJLMR | While the ViewInst start/stop function is active, when an instruction block is executed that contains at least one ViewInst stop address and no ViewInst start addresses, the ViewInst start/stop function remains active for the whole instruction block and becomes inactive for the next instruction block, unless the next instruction block contains a ViewInst start address.                                 |
| R SMGJZ | When an instruction block that contains at least one instruction at a ViewInst start point and at least one instruction at a ViewInst stop point is executed, the ViewInst start/stop function obeys the order of the start and stop points in the block, with the following consequences:                                                                                                                          |
| R SFXZB | The trace analyzer ensures that for all of the SACs selected for ViewInst start points or stop points, any SAC programmed with a lower address than another SAC is a lower-numbered SAC than the other SAC. That is, the SACs contain addresses in address order.                                                                                                                                                   |
| I RYPMM | While the SACs selected for ViewInst do not contain addresses in address order, the behavior of the ViewInst start/stop function is UNPREDICTABLE.                                                                                                                                                                                                                                                                  |
| R ZLDKC | The trace analyzer ensures that for all of the PE Comparator Inputs selected for ViewInst start points or stop points, any PE comparator programmed with a lower address than another PE comparator is a lower-numbered PE comparator than the other PE comparator. That is, the PE comparators contain addresses in address order.                                                                                 |
| I CKTWT | While the PE Comparator Inputs selected for ViewInst do not contain addresses in address order, the behavior of the ViewInst start/stop function is UNPREDICTABLE.                                                                                                                                                                                                                                                  |
| R VFFWS | If more than one instruction Address Comparator is programmed with the same instruction address, then programming one or more of those comparators as start comparators, and one or more as stop comparators, results in the following CONSTRAINED UNPREDICTABLE behavior of the ViewInst start/stop function: • The ViewInst start/stop function is either active or inactive for the instruction at that address. |

INDYFG

ILDDGL

## D4.5.9.3 ViewInst include/exclude function filtering

The ViewInst include/exclude function is useful if:

- Specific ranges of instructions are required to be included in the trace.
- Specific ranges of instructions are required to be excluded from the trace.
- Acombination of including and excluding instruction ranges is required.

The ViewInst include/exclude function is comprised of two functions:

| Function                  | Meaning                                         |
|---------------------------|-------------------------------------------------|
| ViewInst include function | Includes one or more instruction address ranges |
| ViewInst exclude function | Excludes one or more instruction address ranges |

There are between zero and eight instruction Address Range Comparators available for the ViewInst include/exclude function. Some of these comparators can be selected for the ViewInst include function, and some for the ViewInst exclude function.

SVNWYT

INKLJR

RSKZHH

For example, if all instructions in the address range from 0x00 to 0x2C are required, but no other instructions are required, an Address Range Comparator can be selected for the ViewInst include function and be programmed with these two addresses. All instructions that are in this address range, including those at the start and end addresses, are traced.

The ViewInst include/exclude function differs from the ViewInst start/stop function in the following ways:

- When the ViewInst start/stop function is used, the trace unit starts tracing on a specified start instruction address and stops tracing on a specified stop instruction address. However, if execution branches or jumps to an address between the start and stop points, without first accessing the instruction at the start address, then the instruction that it has branched or jumped to is not traced. Instructions in the start/stop range are only traced if the instruction at the start address is accessed, so that the trace unit is triggered to start tracing. When triggered, and as execution continues sequentially towards the stop address, all functions that the piece of code calls are traced.
- When the ViewInst include/exclude function is used, for example by programming an Address Range Comparator with an include address range, then if execution branches or jumps to any instruction address anywhere in that range, that instruction is always traced. This is true regardless of whether the instruction at the start address has been accessed or not.

In addition, unlike the ViewInst start/stop function, as program execution continues through the address range towards the end address, no functions that the piece of code calls are traced.

The ViewInst include/exclude function part of the ViewInst function is expressed as the following equations:

<!-- formula-not-decoded -->

## D4.5.9.3.1 Instruction blocks

RRNPWD

When an instruction in an instruction block is included to be traced by the ViewInst include/exclude function, the ViewInst include/exclude function includes all of the instruction block.

RPLCQJ

When an instruction block contains at least one instruction excluded by the ViewInst include/exclude function, and only when all the instructions in the instruction block are excluded, the ViewInst include/exclude function excludes the instruction block.

ILBNVM

IGMYYC

IRVCQT

IYXGLK

IVFYXG

ICDLHB

IFJMHL

RCGVJD

IVFDMQ

If a block of instructions is not entirely covered by at least one individual ARC selected by TRCVIIECTLR.EXCLUDE, it is CONSTRAINED UNPREDICTABLE whether the block is excluded or not. This applies even if other ARCs selected by TRCVIIECTLR.EXCLUDE cover the rest of the block.

## D4.5.9.4 Guidelines for interpreting the ViewInst function result

ITCGMV

The result of the ViewInst function is either:

| Result   | Meaning                                                        |
|----------|----------------------------------------------------------------|
| High     | Indicates that instructions being executed must be traced      |
| Low      | It is expected that instructions being executed are not traced |

If it is expected that instructions being executed are not traced, then there are occasions when it is permitted to trace some of those instructions. This section provides guidelines for when it is permitted to trace instructions that ViewInst indicates are not traced.

## D4.5.9.4.1 When ViewInst transitions from low to high

If execution occurs while ViewInst is low, it is permitted for a trace unit to trace instructions in certain circumstances. For more information on ViewInst low, see Occasions when tracing instructions when ViewInst is low is permitted.

Tracing of instructions is permitted while ViewInst is low, but if no instructions or Exceptional occurrences that occur are traced, then there is a discontinuity in the trace. When a discontinuity in the trace occurs, when ViewInst becomes high, a Trace On element must be generated.

Any instructions that are executed while ViewInst is high must be traced.

## D4.5.9.4.2 Occasions when tracing instructions when ViewInst is low is permitted

ETE permits tracing of instructions when ViewInst is low, in the following scenarios:

- When the instruction that ViewInst indicates is not to be traced is in the same instruction block as an instruction that ViewInst indicates must be traced. This is because the only way to trace the instruction that must be traced is to trace the whole instruction block.
- When the instruction that ViewInst indicates is not to be traced is in an instruction block that precedes or follows an instruction block containing an instruction that ViewInst indicates must be traced.

An implementation always traces the instruction block that contains an instruction that must be traced. However, additional blocks of instructions might also be traced. This is more likely to occur when many instructions are executed in close proximity.

Except for the scenarios that are mentioned, if the ViewInst function indicates that an instruction is not to be traced, then in general it is expected that it is not traced.

In Figure D4-14, the instruction block 1 is in execution order before instruction block 2. The ViewInst calculation for the second block returns true, as indicated by the transition labeled ( a ). As ViewInst is true for this instruction block then all the instructions in this block must be traced, as indicated by the transition labeled ( b ). Instruction block 1 might be traced as it is in the same PE cycle as block 2, as indicated by the transition labeled ( c ).

: diagram conversion failed.

## D4.5.9.5 Rules for tracing Exceptional occurrences

When an Exceptional occurrence occurs, the Exceptional occurrence does not affect the comparators used by the ViewInst function, and none of the comparators used by the ViewInst function match.

The comparators used by the ViewInst function include the following:

- Single Address Comparators.

## Figure D4-14 Example of close proximity

|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Address Range Comparators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Context Identifier Comparators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I VFNZR | When an Exception element is traced, it might indicate execution of instructions up to a specified address. These instructions might have an impact on the comparators, but the Exceptional occurrence itself does not. This means that when an Exceptional occurrence occurs, the ViewInst function does not indicate whether the Exceptional occurrence must be traced. However, it is useful to trace Exceptional occurrences, to determine why execution has departed from the normal program flow. | When an Exception element is traced, it might indicate execution of instructions up to a specified address. These instructions might have an impact on the comparators, but the Exceptional occurrence itself does not. This means that when an Exceptional occurrence occurs, the ViewInst function does not indicate whether the Exceptional occurrence must be traced. However, it is useful to trace Exceptional occurrences, to determine why execution has departed from the normal program flow. |
| I BVGXZ | When an instruction executes or Exceptional occurrence occurs outside a Trace Prohibited region, the trace unit remembers whether the instruction or Exceptional occurrence was traced. The trace unit performs indirect writes to TRCRSR.TA to store this state. When an Exceptional occurrence occurs, the trace unit uses TRCRSR.TA to determine whether to trace the Exceptional occurrence.                                                                                                        | When an instruction executes or Exceptional occurrence occurs outside a Trace Prohibited region, the trace unit remembers whether the instruction or Exceptional occurrence was traced. The trace unit performs indirect writes to TRCRSR.TA to store this state. When an Exceptional occurrence occurs, the trace unit uses TRCRSR.TA to determine whether to trace the Exceptional occurrence.                                                                                                        |
| R BFSWZ | When an instruction executes or Exceptional occurrence occurs outside a Trace Prohibited region and the instruction or Exceptional occurrence is traced, TRCRSR.TA is set to 1.                                                                                                                                                                                                                                                                                                                         | When an instruction executes or Exceptional occurrence occurs outside a Trace Prohibited region and the instruction or Exceptional occurrence is traced, TRCRSR.TA is set to 1.                                                                                                                                                                                                                                                                                                                         |
| R MLTTK | When an instruction executes or Exceptional occurrence occurs outside a Trace Prohibited region and the instruction or Exceptional occurrence is not traced, TRCRSR.TA is set to 0.                                                                                                                                                                                                                                                                                                                     | When an instruction executes or Exceptional occurrence occurs outside a Trace Prohibited region and the instruction or Exceptional occurrence is not traced, TRCRSR.TA is set to 0.                                                                                                                                                                                                                                                                                                                     |
| R CJTJM | When an instruction or Exceptional occurrence is canceled, TRCRSR.TA is set to the value of TRCRSR.TA immediately before the canceled instruction or Exceptional occurrence.                                                                                                                                                                                                                                                                                                                            | When an instruction or Exceptional occurrence is canceled, TRCRSR.TA is set to the value of TRCRSR.TA immediately before the canceled instruction or Exceptional occurrence.                                                                                                                                                                                                                                                                                                                            |
| R DPMBQ | When an Exceptional occurrence occurs, it is traced if all of the following are true:                                                                                                                                                                                                                                                                                                                                                                                                                   | When an Exceptional occurrence occurs, it is traced if all of the following are true:                                                                                                                                                                                                                                                                                                                                                                                                                   |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The PE is not in Debug state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R BJQDP | While any of the following are true, TRCRSR.TA is unchanged by any execution:                                                                                                                                                                                                                                                                                                                                                                                                                           | While any of the following are true, TRCRSR.TA is unchanged by any execution:                                                                                                                                                                                                                                                                                                                                                                                                                           |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The PE is in Debug state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | The PE is in a Trace Prohibited region.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| R QZPJD | When a trace unit buffer overflow occurs, the behavior of TRCRSR.TA is IMPLEMENTATION DEFINED and is one of the following:                                                                                                                                                                                                                                                                                                                                                                              | When a trace unit buffer overflow occurs, the behavior of TRCRSR.TA is IMPLEMENTATION DEFINED and is one of the following:                                                                                                                                                                                                                                                                                                                                                                              |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | TRCRSR.TA is set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | TRCRSR.TA is set to the value of TRCRSR.TA for the most recent instruction or Exceptional occurrence before the trace unit buffer overflow occurred.                                                                                                                                                                                                                                                                                                                                                    |
|         | D4.5.9.6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Forced tracing of Exceptional occurrences                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| I MFQND | The trace unit can be programmed so that it always traces certain Exceptional occurrences, regardless of whether the instruction or Exceptional occurrence immediately before the Exceptional occurrence must be traced. This option is enabled by setting either or both:                                                                                                                                                                                                                              | The trace unit can be programmed so that it always traces certain Exceptional occurrences, regardless of whether the instruction or Exceptional occurrence immediately before the Exceptional occurrence must be traced. This option is enabled by setting either or both:                                                                                                                                                                                                                              |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | TRCVICTLR.TRCERR to 1. This forces the trace unit to trace System Error exceptions regardless of the value of ViewInst.                                                                                                                                                                                                                                                                                                                                                                                 |
|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | TRCVICTLR.TRCRESET to 1. This forces the trace unit to trace PE Resets regardless of the value of ViewInst.                                                                                                                                                                                                                                                                                                                                                                                             |
|         | •                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| R SJXYS | While the PE is executing in a Trace Prohibited region, forced tracing of System Error exceptions is inactive.                                                                                                                                                                                                                                                                                                                                                                                          | While the PE is executing in a Trace Prohibited region, forced tracing of System Error exceptions is inactive.                                                                                                                                                                                                                                                                                                                                                                                          |
| R VLNMN | While the PE is not executing a Trace Prohibited region and forced tracing of System Error exceptions is enabled, forced tracing of System Error exceptions is active.                                                                                                                                                                                                                                                                                                                                  | While the PE is not executing a Trace Prohibited region and forced tracing of System Error exceptions is enabled, forced tracing of System Error exceptions is active.                                                                                                                                                                                                                                                                                                                                  |
| R LTLBB | While forced tracing of System Error exceptions is active, when a System Error exception occurs, the trace unit generates an Exception element indicating a System Error exception, regardless of the value of ViewInst.                                                                                                                                                                                                                                                                                | While forced tracing of System Error exceptions is active, when a System Error exception occurs, the trace unit generates an Exception element indicating a System Error exception, regardless of the value of ViewInst.                                                                                                                                                                                                                                                                                |
| R NCXJN | While the PE is executing in a Trace Prohibited region, forced tracing of PE Resets is inactive, regardless of whether the PE Reset causes the PE to leave a Trace Prohibited region or not.                                                                                                                                                                                                                                                                                                            | While the PE is executing in a Trace Prohibited region, forced tracing of PE Resets is inactive, regardless of whether the PE Reset causes the PE to leave a Trace Prohibited region or not.                                                                                                                                                                                                                                                                                                            |

## The Embedded Trace Extension D4.5 About the ETE trace unit

| R NQJNL   | While the PE is not executing in a Trace Prohibited region, while forced tracing of PE Resets is enabled, forced tracing of PE Resets is active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GPKSH   | While forced tracing of PE Resets is active, when a PE Reset occurs, the trace unit generates an Exception element indicating a PE Reset, regardless of the value of ViewInst.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| R BBBBT   | While tracing is inactive, before an Exception element is generated due to forced tracing of either a PE Reset of a System Error exception, the trace unit generates a Trace On element and then a Target Address element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| I LXLKS   | When an Exception element is generated as a result of forced tracing, the Trace On element generated before the Exception element indicates that tracing becomes active, and the Target Address element indicates where tracing becomes active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R NZNDM   | When a System Error exception occurs and TRCRSR.TA is 0 and the exception is traced because forced tracing of System Error exceptions is enabled, then it is IMPLEMENTATION DEFINED whether TRCRSR.TA is set to 1 or remains at 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| R YFKGM   | When a PE Reset occurs and TRCRSR.TA is 0 and the PE Reset is traced because forced tracing of PE Resets is enabled, then it is IMPLEMENTATION DEFINED whether TRCRSR.TA is set to 1 or remains at 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I GWHRM   | In scenarios where a System Error exception occurs at approximately the same time as an exit from a Trace Prohibited region, after all execution inside the Trace Prohibited region and before any instruction execution outside the Trace Prohibited region, it is UNPREDICTABLE whether the System Error exception is considered to have occurred inside or outside the Trace Prohibited region. It is also UNPREDICTABLE whether the forced tracing of System Error exceptions is active for this exception. These scenarios do not include scenarios where the System Error exception caused the exit from a Trace Prohibited region, because the System Error exception occurred inside the Trace Prohibited region. |
| I JGVSY   | In scenarios where a System Error exception occurs at approximately the same time as an entry to a Trace Prohibited region, after all execution before the Trace Prohibited region and before any instruction execution inside the Trace Prohibited region, it is UNPREDICTABLE whether the System Error exception is considered to have occurred inside or outside the Trace Prohibited region. It is also UNPREDICTABLE whether the forced tracing of System Error exceptions is active for this exception. These scenarios do not include scenarios where the System Error exception caused the entry to a Trace Prohibited region, because the System Error exception occurred outside the Trace Prohibited region.   |
| R TSVKN   | When a System Error exception occurs immediately after the PE exits a Trace Prohibited region and the System Error exception is traced, the preferred exception return address in the Exception element indicating the System Error exception does not include information about the Trace Prohibited region.                                                                                                                                                                                                                                                                                                                                                                                                             |
| I PXJWM   | In scenarios where a PE Reset occurs at approximately the same time as an exit from a Trace Prohibited region, after all execution inside the Trace Prohibited region and before any instruction execution outside the Trace Prohibited region, it is UNPREDICTABLE whether the PE Reset is considered to have occurred inside or outside the Trace Prohibited region. It is UNPREDICTABLE whether the forced tracing of PE Resets is active for this PE Reset. These scenarios do not include scenarios where the PE Reset caused the exit from a Trace Prohibited region, because the                                                                                                                                   |
| I JKQHF   | In scenarios where a PE Reset occurs at approximately the same time as an entry to a Trace Prohibited region, after all execution before the Trace Prohibited region and before any instruction execution inside the Trace Prohibited region, it is UNPREDICTABLE whether the PE Reset is considered to have occurred inside or outside the Trace Prohibited region. It is UNPREDICTABLE whether the forced tracing of PE Resets is active for this PE Reset. These scenarios do not include scenarios where the PE Reset caused the entry to a Trace Prohibited region, because the PE Reset occurred outside the Trace Prohibited region.                                                                               |
| R NRNFS   | When a PE Reset occurs immediately after the PE exits a Trace Prohibited region and the PE Reset is traced, the preferred exception return address in the Exception element indicating the PE Reset does not include information about the Trace Prohibited region.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## D4.5.10 Element Generation

## D4.5.10.1 Trace Info element generation

| R TFQRM   | When a trace protocol synchronization request is serviced, the trace unit generates a Trace Info element to indicate where program execution trace analysis can start. A Trace Info element is not required to indicate where Event element and Instrumentation element analysis can start.                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R WJJNK   | While the PE is in Transactional state and the trace unit has previously generated a Transaction Start element for this transaction, when a Trace Info element is generated, the trace unit sets the Transactional state indicator in the Trace Info element to 1.                                              |
| R WMXVM   | While the PE is not in Transactional state, or the PE is in Transactional state but the trace unit has not generated a Transaction Start element for this transaction, when a Trace Info element is generated, the trace unit sets the Transactional state indicator in the Trace Info element to 0.            |
| R QMTSR   | When the trace unit generates the first Trace Info element after an Overflow element , the Transactional state indicator is set to 0.                                                                                                                                                                           |
| R CRPJZ   | When an Overflow element is generated, before any subsequent P0 elements indicating execution in Transactional state are traced, the trace unit generates a new Transaction Start element , even if a Transaction Start element has previously been traced for this transaction prior to the Overflow element . |
|           | D4.5.10.2 Atom element                                                                                                                                                                                                                                                                                          |
| R XCJGD   | When a P0 instruction is taken, the trace unit generates one of the following:                                                                                                                                                                                                                                  |
| R SRYKV   | When a P0 instruction is not taken, the trace unit generates one of the following: • AnN Atom element . • Nothing.                                                                                                                                                                                              |
| R TZZRH   | When a P0 instruction is not taken and the trace unit does not generate anN Atom element , for all future not taken P0 instructions until the next taken P0 instruction or Exceptional occurrence, the trace unit does not generate anN Atom element .                                                          |
| R NZTGQ   | When a P0 instruction is not taken and the trace unit does not generate anN Atom element , when an Exceptional occurrence occurs before the next taken P0 instruction , the trace unit generates an Exception element .                                                                                         |
| R FWCQR   | When a P0 instruction is not taken and the trace unit does not generate anN Atom element , when no Exceptional occurrence occurs before the next taken P0 instruction , the trace unit generates a Source Address element for the next taken P0 instruction .                                                   |
| R NTMMM   | When a P0 instruction is not taken and the trace unit does not generate anN Atom element , and the P0 instruction is subsequently mispredicted, the trace unit generates a Source Address element and does not generate a Mispredict element .                                                                  |
| R ZRYPK   | The trace unit generates Atom elements in the program order in which they occur, and the trace protocol encode and decode process maintains this order.                                                                                                                                                         |
| I TGQNB   | For conditional branch instructions, an E Atom element indicates that the instruction passed its condition code check, and anN Atom element indicates that the instruction failed its condition code check, although a trace unit might use a Mispredict element to modify the Atom element .                   |
| I BXBNQ   | The trace unit might trace unconditional P0 instructions using an E Atom element or anN Atom element .                                                                                                                                                                                                          |

## The Embedded Trace Extension D4.5 About the ETE trace unit

| R RNYNV   | When an unconditional P0 instruction is traced using anN Atom element , the trace unit generates either a Mispredict element or a Cancel element to correct theN Atom element .                                                                                                                                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LMDZV   | When an ISB instruction does not pass the condition code check, and the ISB instruction does not perform a Context synchronization event, the trace unit treats the ISB instruction as a not taken instruction.                                                                                                                                                                                                                    |
| R NZPLB   | When an ISB instruction does not pass the condition code check, and the ISB instruction performs a Context synchronization event, the trace unit treats the ISB instruction as a taken instruction.                                                                                                                                                                                                                                |
| R CPFBS   | When an ISB instruction passes the condition code check, the trace unit treats the ISB instruction as a taken instruction. Note For an ISB instruction, a trace analyzer must not infer the value of the PSTATE condition flags from an Atom element .                                                                                                                                                                             |
| R QBGXJ   | It is IMPLEMENTATION DEFINED whether the trace unit classifies WFI , WFIT , WFE , and WFET instructions as P0 instructions When WFI , WFIT , WFE , and WFET are classified as P0 instructions , execution of these instructions generates an Atom element . See Low-power state and TRCIDR2.WFXMODE.                                                                                                                               |
| R HJHHV   | When WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions and a conditional WFE or WFI instruction is executed, if the instruction passes its condition code check then an E Atom element is generated.                                                                                                                                                                                                      |
| R BMXDT   | When WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions and a conditional WFE or WFI instruction is executed, if the instruction fails its condition code check then either an E Atom element or anN Atom element is generated.                                                                                                                                                                            |
|           | Note                                                                                                                                                                                                                                                                                                                                                                                                                               |
|           | For a WFI , WFIT , WFE , or WFET instruction which is classified as a P0 instruction , a trace analyzer must not infer the value of the PSTATE condition flags from an E Atom element .                                                                                                                                                                                                                                            |
| I PZRCT   | P0 instructions that fail or are predicted to fail their condition code check either generate an Undefined Instruction exception or are executed as a NOP, if the instruction is also UNDEFINED.                                                                                                                                                                                                                                   |
| R YCRVD   | When a P0 instruction fails or is predicted to fail its condition code check, and the P0 instruction is executed as a NOP, the trace unit generates anN Atom element for the P0 instruction .                                                                                                                                                                                                                                      |
| R TSQGH   | When a P0 instruction fails or is predicted to fail its condition code check, and the P0 instruction generates an Undefined Instruction exception, the trace unit does not generate an Atom element for the instruction and generates an Exception element instead. The preferred exception return address for the generated Exception element is the UNDEFINED instruction, which indicates that the instruction did not execute. |
| R NQPPX   | The trace unit generates all Atom elements speculatively, and explicitly resolves or cancels each Atom element by generating Commit elements or Cancel elements .                                                                                                                                                                                                                                                                  |
| I NGJYB   | Atrace analyzer can infer execution from an Atom element , but only after the Atom element has been resolved by a Commit element .                                                                                                                                                                                                                                                                                                 |
| S MFDNZ   | For taken direct P0 instructions , a trace analyzer must infer the target address and instruction set of the instruction from the opcode in the program image.                                                                                                                                                                                                                                                                     |
| S TJSRY   | If a taken direct P0 instruction is from a branch broadcasting region, the trace analyzer does not need to infer the target address and instruction set because this is explicitly traced using a Target Address element .                                                                                                                                                                                                         |
|           | D4.5.10.3 Exception element                                                                                                                                                                                                                                                                                                                                                                                                        |
| R QHRVX   | When an Exceptional occurrence occurs, if the Exceptional occurrence is required to be traced, the trace unit generates an Exception element .                                                                                                                                                                                                                                                                                     |
| R LYYMG   | The trace unit generates Exception elements in program order relative to other P0 elements .                                                                                                                                                                                                                                                                                                                                       |

| I PCMYT   | To be consistent with the rules for generating Target Address elements , under the following scenarios the trace unit must generate a Target Address element before an Exception element , unless the Target Address element would be removed due to a return stack match: • The Exceptional occurrence is taken from the target of a taken indirect P0 instruction . • The Exceptional occurrence is taken from the target of a taken direct P0 instruction in a branch broadcasting   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XGXKK   | When an Exceptional occurrence occurs, if the Context information changes at the target of the P0 element preceding the Exceptional occurrence, then the trace unit generates a Context element before the Exception element . The Context element provides Context information about the address and context where the Exceptional occurrence was taken from.                                                                                                                          |
| I CMRCN   | An invalid address is one where bits [63:P] are not all zeros or all ones, where P is defined as one of the following: • When FEAT_LVA3 is implemented, 56. • When FEAT_LVA is implemented, 52. • Otherwise, 48.                                                                                                                                                                                                                                                                        |
| R RJCBT   | When the PE attempts to execute an instruction at an invalid address and the trace unit generates an Exception element , the preferred exception return address in the Exception element indicates one of the following: • The full 64-bit invalid address.                                                                                                                                                                                                                             |
| I GYJKB   | When a branch to an invalid address occurs and an Exception element is generated for an exception taken from that invalid address, Arm recommends that the preferred exception return address in the Exception element is the same as the invalid address indicated by the Target Address element for the branch.                                                                                                                                                                       |
| R DCHPQ   | When a P0 instruction which must be traced is not taken and the trace unit does not generate anN Atom element , then when a subsequent P0 instruction is taken, the trace unit generates a Source Address element .                                                                                                                                                                                                                                                                     |
| I KDTRV   | Atrace unit can generate a Source Address element to imply that at least one instruction has been executed, including a taken P0 instruction .                                                                                                                                                                                                                                                                                                                                          |
| R WVBQW   | When the trace unit generates a Source Address element to imply that a taken P0 instruction has been executed, the address associated with the Source Address element is the virtual address of the taken P0 instruction .                                                                                                                                                                                                                                                              |
| R FZTZP   | Atrace unit can generate a Qelement to imply that at least one instruction has been executed, possibly including P0 instructions .                                                                                                                                                                                                                                                                                                                                                      |
| R WHLPS   | When a Qelement is generated, the trace unit generates a Target Address element that indicates where execution is to continue after all the instructions that are implied by the Qelement have been executed.                                                                                                                                                                                                                                                                           |
| R MNWCK   | When a Qelement is generated and the last instruction implied by the Qelement is a P0 instruction , the trace unit generates a Target Address element that indicates the target of the P0 instruction .                                                                                                                                                                                                                                                                                 |
| R BJLRS   | When a Qelement is generated and the last instruction implied by the Qelement is not a P0 instruction , the trace unit generates a Target Address element that indicates the instruction address immediately following the last instruction that is implied by the Qelement .                                                                                                                                                                                                           |
| R FPHFM   | When the PE leaves a region where Qelements are permitted, either by a P0 instruction or by sequential execution out of the region, and a Qelement implies the execution of the last instruction in the region, the Qelement does not imply any more instructions after the last instruction in the region.                                                                                                                                                                             |
| R DTWYZ   | When the PE enters a region where Qelements are permitted, either by a P0 instruction or by an Exceptional occurrence, the trace unit traces the P0 instruction or Exceptional occurrence using elements other than Qelements .                                                                                                                                                                                                                                                         |

|         | Note                                                                                                                                                                                                                                                                                                    |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         | Although the trace unit does not trace with Qelements a P0 instruction or Exceptional occurrence that causes the PE to enter a region where Qelements are permitted, any subsequent instructions in the region where Qelements are permitted might be traced using Qelements .                          |
| I YRZWY | When the PE enters by sequential execution a region where Qelements are permitted, any instructions that are executed since the last P0 element outside the permitted region might be traced using a Qelement . These instructions can always be inferred unambiguously from the Qelement .             |
| R SJSGX | When the PE enters by sequential execution a region where Qelements are permitted, and P0 instructions executed since the last P0 element outside the permitted region are traced by a Qelement , the Qelement does not indicate execution of any P0 instructions outside the permitted region.         |
|         | D4.5.10.6 Event element                                                                                                                                                                                                                                                                                 |
| R WJPTB | The trace unit generates Event elements independently of ViewInst.                                                                                                                                                                                                                                      |
| R KKLYB | While TRCEVENTCTL1R.INSTEN<n> is 1 and the resource event selected by TRCEVENTCTL0R.EVENT<n> is active, while trace generation is operative, the trace unit generates an Event element <n> on each PE clock cycle.                                                                                      |
| R SPYTT | When an Event element is generated between two P0 elements or at the same time as a P0 element that follows another, the trace unit inserts the Event element after the first P0 element but before the P0 element that is an IMPLEMENTATION DEFINED number of P0 elements after the first P0 element . |
| I XLJKP | Arm recommends that the IMPLEMENTATION DEFINED number of P0 elements is less than or equal to the number of P0 elements the PE can process simultaneously.                                                                                                                                              |
| R SHYMY | While trace generation is inoperative due to a trace unit buffer overflow, when a programmed ETEEvent <n> occurs, the trace unit generates at least one Event element <n> before it generates the Overflow element corresponding to the trace unit buffer overflow.                                     |
|         | D4.5.10.7 Cancel element generation                                                                                                                                                                                                                                                                     |
| R HYCXR | When one or more P0 elements are canceled, the trace unit generates a Cancel element .                                                                                                                                                                                                                  |
| R GKDYR | The trace unit generates Cancel elements in execution order relative to P0 elements .                                                                                                                                                                                                                   |
| R KDTVX | When a Cancel element causes execution to return to a point in the program flow that is not adjacent to a P0 instruction , the trace unit generates an Exception element that indicates which instructions were executed up to that point in the program flow before it generates any P0 elements .     |
|         | D4.5.10.8 Commit element generation                                                                                                                                                                                                                                                                     |
| R QNLYJ | When one or more traced P0 elements are resolved for execution, the trace unit generates a Commit element .                                                                                                                                                                                             |
| I MDSCN | An Atom element might be corrected using a Mispredict element after it has been resolved.                                                                                                                                                                                                               |
| R MNXTW | The trace unit never generates more speculative P0 elements than the maximum speculation depth of the trace unit.                                                                                                                                                                                       |
| R XXFBC | When trace generation becomes inoperative due to the trace unit being disabled, the trace unit outputs any Commit elements which have not been output.                                                                                                                                                  |
| I BNLZT | If cycle counting is enabled some Commit elements have Cycle Count elements associated with them, that provide counts of processor clock cycles. The cycle count values given in Cycle Count elements can be used to obtain a cumulative count.                                                         |
| R ZHWDD | Commit elements with associated Cycle Count elements cannot be merged with later Commit elements .                                                                                                                                                                                                      |
| I PSFTD | For more information, see Cycle Count element.                                                                                                                                                                                                                                                          |

## D4.5.10.9 Transaction Start element

| R DGRTZ   | When the PE enters an outer transaction, before the first instruction is traced, the trace unit generates a Transaction Start element .                                                                                                                                                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I QLXNC   | A Transaction Start element is not required for each Trace On element if the instructions are all part of the same outer transaction.                                                                                                                                                                                                                                                 |
| R TWNQP   | When the PE leaves Transactional state and a Transaction Start element was generated for the transaction, the trace unit traces the result of the transaction using one of the following: • A Transaction Commit element , if the transaction was successful. • A Transaction Failure element , if the transaction failed.                                                            |
| I GWZDH   | The trace element stream only indicates that the PE is in Transactional state. It does not indicate the transactional nesting depth.                                                                                                                                                                                                                                                  |
| R BGMKL   | When the PE exits Transactional state successfully, and a Transaction Start element was generated for the transaction, the trace unit generates a Transaction Commit element .                                                                                                                                                                                                        |
| R PCKKS   | When a Transaction Commit element is generated, the trace unit traces the Transaction Commit element after the P0 element which is generated before the TCOMMIT instruction, and before the next Transaction Start element is traced.                                                                                                                                                 |
| I CQLFV   | Arm recommends that the Transaction Commit element is generated and output as soon as possible after the PE leaves Transactional state.                                                                                                                                                                                                                                               |
| I LVPTL   | The rules on the Transaction Commit element mean that a Transaction Commit element is permitted to be output later than the P0 element which implies execution of the TCOMMIT instruction. The TCOMMIT instruction is not a P0 instruction . This means that the Transaction Commit element might be traced before the P0 element which implies execution of the TCOMMIT instruction. |
| R MHBCG   | When a transaction failure occurs, and a Transaction Start element was generated for the transaction, the trace unit generates a Transaction Failure element .                                                                                                                                                                                                                        |
| R XQSPC   | When the PE enters a Trace Prohibited region and is in Transactional state, and a Transaction Start element was generated for the transaction, the trace unit generates a Transaction Failure element .                                                                                                                                                                               |
| R ZJXHP   | When the trace unit becomes disabled and the PE is in Transactional state, and a Transaction Start element was generated for the transaction, the trace unit generates a Transaction Failure element .                                                                                                                                                                                |
| R YTKLN   | When a trace unit buffer overflow occurs and the PE is in Transactional state, and a Transaction Start element was generated for the transaction, the trace unit generates a Transaction Failure element .                                                                                                                                                                            |
| I DLKJR   | A Transaction Failure element is encoded as an Exception packet with a type of Transaction Failure.                                                                                                                                                                                                                                                                                   |
| I FBFDB   | When a Transaction Failure element is generated, the following behavior applies: • The target address and target context of the previous P0 element might be UNKNOWN. • If there are no P0 elements between a Trace On element and the Transaction Failure element , the initial address and context after the previous Trace On element might be UNKNOWN.                            |
| R QWGXL   | When a PE reset occurs and the PE is in Transactional state, and a Transaction Start element was generated for the transaction, the trace unit generates a Transaction Failure element .                                                                                                                                                                                              |
| I LTJDG   | A Transaction Failure element caused by a PE reset might be traced using any of the following: • Asingle Exception packet with TYPE indicating PE reset. This packet can imply the Transaction element .                                                                                                                                                                              |
|           | Failure • An Exception packet with TYPE indicating Transaction Failure. • An Exception packet with TYPE indicating PE reset, if the PE reset is required to be traced.                                                                                                                                                                                                                |

## D4.5.10.12 Context element

RBDFDQ

The trace unit generates a Context element in the following situations:

- While tracing is active, when any of the Context information changes, before any P0 element which indicates execution from the new context.

- After a Trace Info element is generated due to a non-periodic trace protocol synchronization request, and before any P0 element .

- After a Trace Info element is generated due to a periodic trace protocol synchronization request.

- When mis-speculation results in an incorrect Context element being output, before any P0 element which indicates execution from the correct context.

RJNXJT While Virtual context identifier tracing is enabled and TRFCR\_EL2.CX disallows the tracing of the Virtual context identifier, when the trace unit generates a Context element , the Virtual context identifier in the Context element has the

value 0x0 .

ITBJPL A Context element might also be output at other points, which might include after all Context synchronization events, or at any other point at which the Context information changes.

RMKKZN If the highest implemented Exception level is using AArch64, the Context identifier value is the value of CONTEXTIDR\_EL1.

IWXVHT Some of the Context information might change at points other than at Context synchronization events. These changes occur when system instructions are used to change a piece of Context information , including:

- Writes to the current CONTEXTIDR\_EL1.

- Writes to the CONTEXTIDR\_EL2.

- Changes from a higher Security state to a lower Security state without using an exception return.

- Changes in Exception level other than due to an exception or an exception return.

- RHXNXF When a System instruction writes to a System register and the Context information changes, the trace unit generates a Context element containing the new context value, after the P0 element prior to the System instruction but before the P0 element following a Context synchronization event after the System instruction.

Note

If the Context element is output before the first P0 element after the System instruction, this might imply that some instructions before the System instruction were executed with the new context. This is acceptable because the code which changes the context is usually executed in a state where it does not matter whether the old or new context values are used.

IWTSTB If the PE takes an exception after performing a write to a System register that changes the context, but a P0 element has not been generated since the write, then a Context element indicating the new context is not required to be output before the Exception element . This is because no instructions or Exceptional occurrences are indicated to have been executed from the new context. A Context element indicating the new context must be generated after the Exception element if the Exceptional occurrence is a Context synchronization event. If the Exceptional occurrence changes the context, then the Context element must indicate the new context. This might happen if, for example, the Security state changes.

RHTYGF When a PE reset occurs, until the relevant PE registers are updated, the trace unit traces the Context identifier and Virtual context identifier as zero.

IKTPVJ Atrace unit is not required to generate a Context element if tracing becomes inactive before any instructions are executed in the new context.

IQWSVJ Additional Context elements might be output by a trace unit in some scenarios, but these must only be output where they do no affect the analysis of the trace element stream. Such a scenario might include when a change in the Context information is incorrectly speculated and a subsequent Context element corrects the value of a previous incorrect Context element . Arm recommends that the generation of additional unnecessary Context elements is minimized to ensure trace bandwidth is minimized.

## D4.5.10.13 Target Address element

RHLRZJ

When the trace analyzer cannot infer the address or instruction set from the trace, the trace unit generates a Target Address element .

## The Embedded Trace Extension D4.5 About the ETE trace unit

| I FRTGM         | Occasions when the trace analyzer might not be able to infer the address or instruction set from previous trace include:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZRYSN         | When the trace analyzer cannot infer the address or instruction set from the trace, the trace unit generates the resulting Target Address element before the next P0 element , unless any of the following are true:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R               | • The Target Address element can be omitted because of a return stack match. • Tracing is inactive at the target of the P0 instruction or Exceptional occurrence. • Atransaction failure occurs and tracing is inactive at the target of the transaction failure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I GBMWG         | indicate the target of a P0 element from before the Trace Info element . Typically, a Target Address element is required after an Exception element to indicate the target of the Exceptional occurrence, since a trace analyzer is not usually able to infer the target of an Exceptional occurrence.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| RGPTK           | When non-periodic trace protocol synchronization occurs, the trace unit generates a Target Address element after the Trace Info element and Trace On element corresponding to the non-periodic trace protocol synchronization, and before the next P0 element is generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R MDTYL I YMLXQ | When periodic trace protocol synchronization occurs, after the corresponding Trace Info element has been generated, the trace unit generates a Target Address element containing the address of the target of the most recent P0 element before the Target Address element . When non-periodic trace protocol synchronization occurs, the Target Address element does not need to indicate the target of the most recent P0 element , since tracing might not become active at the target of a P0 element . When periodic trace protocol synchronization occurs, the Target Address element needs to indicate the target of the most recent P0 element , since tracing is continuing from that P0 element . Furthermore, the Target Address element might |
| R               | When a Trace On element is generated, the trace unit generates a Target Address element before the next P0 element .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| I DTQDH         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| QCSJJ           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| I YHQGL         | In some scenarios, an Exception element might be generated in the trace where the Exceptional occurrence target address is the next sequential instruction from the last instruction before the Exceptional occurrence. This behavior depends on many factors and might only occur for IMPLEMENTATION DEFINED Exceptional occurrences. If an occurrence is taken to the next sequential instruction, the trace unit is not required to output a Target Address element                                                                                                                                                                                                                                                                                    |
| I GVZJZ         | Exceptional indicating the target address of the Exceptional occurrence because this can be inferred from the previous execution. Atrace analyzer needs both a Target Address element and a Context element before it can determine the instruction set in use, because the Target Address element provides the instruction set and the Context element provides information on                                                                                                                                                                                                                                                                                                                                                                           |
| R RHDMW         | which Execution state the PE is in. When a change of instruction set occurs that switches between AArch32 state and AArch64 state, the trace unit generates a Context element indicating the new state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| I               | An invalid address is one where bits [63:P] are not all zeros or all ones, where P is defined as one of the following:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                 | • When FEAT_LVA3 is implemented, 56. • When FEAT_LVA is implemented, 52.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| KZXQW           | • Otherwise, 48.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                 | When the PE attempts to execute an instruction at an invalid address and the trace unit generates a Target Address element , the Target Address element indicates one of the following:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| R VWVWR         | • The full 64-bit invalid address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

- Any other invalid address, with address bits [P-1:0] the same as the full invalid address.

IYJYFM When a branch to an invalid address occurs and an Exception element is generated for an exception taken from that invalid address, Arm recommends that the preferred exception return address in the Exception element is the same as the invalid address indicated by the Target Address element for the branch.

RSBCPK While tagged addresses are in use, the virtual address in the trace element stream does not include the tag and is the PC value, that is, depending on the state of the PE at the address, bits[63:56] are one of the following:

- The sign-extension of bit[55].
- Zero.

IYGGGK The Translation Control Registers, TCR\_ELx, contain the TBI field for controlling whether to ignore the top byte of an address. If the current TBI field is changed from 0 to 1, and before the next Context synchronization event the PE takes an exception because of an invalid top address byte, the branch target address to the invalid address or the preferred exception return address of the Exception element might not contain the full invalid address and might contain the address with the top byte masked. Furthermore, the branch target address might be the invalid address and therefore might be different from the preferred exception return address. Trace analysis tools must be aware that if a branch target address is substantially different from a preferred exception return address which follows, then there might have been a change in the TBI field which caused this large change in address.

RHHKGB When a pointer authentication check fails and an exception is taken from the resulting invalid address, the preferred exception return address is one of the following:

- The full 64-bit invalid address.
- Any other invalid address, with address bits [P-1:0] the same as the full invalid address.
- ICRSTX Arm recommends that when a pointer authentication check fails and an exception is taken from the resulting invalid address, the preferred exception return address is the full 64-bit invalid address.

RFSWRC The bottom bits of an address are ignored, in the following way:

- Bits[1:0] of addresses that are used in A64 or A32 instructions are always traced as zero.
- Bit[0] of addresses that are used in T32 instructions is always traced as zero.
- IMDZJL Additional Target Address elements might be output by a trace unit in some scenarios, but these must only be output where they do not affect the analysis of the trace element stream. These scenarios include, but are not limited to:
- When an instruction address is incorrectly speculated, and a subsequent Target Address element corrects the value of a previous incorrect Target Address element .
- When an instruction address can be inferred by the trace analyzer, for example for the target of a direct P0 instruction , but a Target Address element is output anyway with the same address.

Arm recommends that the generation of additional unnecessary Target Address elements is minimized to ensure trace bandwidth is minimized.

## D4.5.10.14 Mispredict element

RYJCNT When the status of the last non-canceled Atom element has been changed by the PE, the trace unit generates a Mispredict element .

RSCKBZ The trace unit only generates a Mispredict element to change the status of an Atom element .

- IXYDNP Atrace unit might generate multiple Mispredict elements for the same Atom element . Atrace analyzer must use each Mispredict element to determine the final status of the Atom element . For example, if an E Atom element has two Mispredict elements , the first Mispredict element indicates the Atom element is an N Atom element and the second Mispredict element indicates it is an E Atom element .
- IHVWCN If a PE mispredicts only the target address of a P0 element , then it does not generate a Mispredict element . The trace unit uses a Target Address element to correct the mispredicted target address. When analyzing a Mispredict element , any Target Address elements between the mispredicted Atom element and the Mispredict element must be discarded.

## D4.5.10.15 Overflow element

| R HRYKY   | When a trace unit buffer overflow occurs, after all trace elements that were generated prior to the trace unit buffer overflow are output, the trace unit outputs an Overflow element .                                                                                                                                                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R RPSPH   | When a trace unit buffer overflow occurs, and the trace unit is disabled after recovering from the trace unit buffer overflow, the trace unit outputs the corresponding Overflow element before the trace unit becomes idle.                                                                                                                                                                                |
|           | D4.5.10.16 Timestamp element                                                                                                                                                                                                                                                                                                                                                                                |
| R YYWTR   | While TRCCONFIGR.TS is 1 and any of the following occur, a timestamp request occurs:                                                                                                                                                                                                                                                                                                                        |
|           | • The trace unit generates a Trace Info element .                                                                                                                                                                                                                                                                                                                                                           |
|           | • The trace unit recovers from a trace unit buffer overflow.                                                                                                                                                                                                                                                                                                                                                |
|           | • When not in a Trace Prohibited region and a Context synchronization event is caused by any of the following:                                                                                                                                                                                                                                                                                              |
|           | - The PE takes an exception. - The PE returns from an exception.                                                                                                                                                                                                                                                                                                                                            |
|           | - An ISB instruction is executed. • Atrace unit flush is requested.                                                                                                                                                                                                                                                                                                                                         |
| R CKNFV   | While TRCCONFIGR.TS is 1 and when not in a Trace Prohibited region, a timestamp request might occur when any of the following occur but do not cause a Context synchronization event:                                                                                                                                                                                                                       |
|           | • The PE takes an exception.                                                                                                                                                                                                                                                                                                                                                                                |
|           | • The PE returns from an exception.                                                                                                                                                                                                                                                                                                                                                                         |
|           | An ISB instruction is executed.                                                                                                                                                                                                                                                                                                                                                                             |
|           | •                                                                                                                                                                                                                                                                                                                                                                                                           |
| R NGXNQ   | The state of the ViewInst function does not affect whether a timestamp request occurs.                                                                                                                                                                                                                                                                                                                      |
| R HZSYP   | When a timestamp request occurs and ViewInst is inactive, the timestamp request is permitted to be delayed until after the first of the following occurs:                                                                                                                                                                                                                                                   |
|           | • A P0 element is generated.                                                                                                                                                                                                                                                                                                                                                                                |
|           | • An Event element is generated.                                                                                                                                                                                                                                                                                                                                                                            |
|           | • An Instrumentation element is generated.                                                                                                                                                                                                                                                                                                                                                                  |
| I WFXVV   | There is no requirement for a Timestamp element to be generated in the trace element stream on each occasion that ViewInst becomes active.                                                                                                                                                                                                                                                                  |
| R RMSVV   | When a timestamp request occurs and is not ignored, the trace unit generates a Timestamp element .                                                                                                                                                                                                                                                                                                          |
| R DWCYP   | When a timestamp request occurs but the trace unit does not have the capacity to generate the Timestamp element immediately, then the generation of the Timestamp element is delayed until there is capacity.                                                                                                                                                                                               |
| I TQDHQ   | Atrace unit might not have the capacity to generate a Timestamp element for multiple reasons, including avoiding a trace unit buffer overflow. Adelayed Timestamp element means that a timestamp value might not be the exact time of the incident that resulted in the timestamp request. Atimestamp is only a time indicator inserted in the trace element stream somewhere near the time of the request. |
| R XMJGY   | When a timestamp request occurs while in a Trace Prohibited region, then the generation of the Timestamp element is delayed until the PE leaves the Trace Prohibited region.                                                                                                                                                                                                                                |
| R CWHHW   | When the first timestamp request occurs after trace generation becomes operative, the trace unit delays generation of the corresponding Timestamp element until after the trace unit has generated either a P0 element , an Event element , or an Instrumentation element .                                                                                                                                 |
| I SDPZZ   | This is so that the timestamp value can correspond to the most recent of these elements.                                                                                                                                                                                                                                                                                                                    |
| R SZNMB   | Atimestamp request is permitted to be ignored if a previous timestamp request has not yet generated a Timestamp element , due to a delay in the generation.                                                                                                                                                                                                                                                 |

| R DWFTT   | Atrace unit might ignore the second request of two successive timestamp requests if all of the following are true: • The second request is not caused as a result of a trace protocol synchronization request. • No P0 elements , Event elements , or Instrumentation elements have been generated between the two requests.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZMQLT   | While TRCCONFIGR.CCI is 1, each Timestamp element contains a cycle count that indicates the number of cycles between the element with which the Timestamp is associated and the most recent Cycle Count element before that element.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R MWJHD   | The cycle count associated with a Timestamp element is different from the Cycle Count element in the following ways: • The cycle count does not affect the cumulative cycle count. • The cycle count value can be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I HTGCM   | When the cycle count associated with a Timestamp element is zero, this indicates that no cycles passed between the previous Cycle Count element and the element with which the Timestamp element is associated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| I TYVDN   | The cycle count associated with a Timestamp element is not a Cycle Count element , and therefore has no effect on the cycle counter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R JNSWW   | When the trace unit is first enabled, while cycle counting is enabled, when a Timestamp element is generated before any Cycle Count elements , the Timestamp element reports the cycle count as UNKNOWN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R NPYKS   | When a Timestamp element is generated and the cycle counter has exceeded the maximum supported value, the Timestamp element reports the cycle count as UNKNOWN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R LMLSN   | D4.5.10.17 Trace On element When an instruction block is traced immediately after an instruction block was not traced or a trace unit buffer overflow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| I GPQZW   | When an Exception element indicating a PE reset is traced, the preferred exception return address is UNKNOWN. Any instructions since the most recent unresolved P0 element are not traced. If ViewInst was active for these instructions, this is not considered a gap in the trace element stream and a Trace On element is not required. In some scenarios where mis-speculation occurs or instructions are canceled, after Cancel elements have been processed there might be Trace On elements in the trace element stream even though no trace discontinuity occurred in the architecturally-executed instruction trace. This typically only occurs when the trace is filtered using the ViewInst function, which causes the Trace On element to be inserted. |
| I MHFJB   | Trace analyzers must be aware that these additional Trace On elements might be traced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R TYNZR   | The cycle counter has an IMPLEMENTATION DEFINED size of between 12 and 20 bits, as indicated by TRCIDR2.CCSIZE. The cycle counter therefore supports values from 1 to 2 20 -1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R GWQGS   | While TRCCONFIGR.CCI is 1 and the cycle count is equal to or greater than the value of TRCCCCTLR.THRESHOLD, when a Commit element is generated, a Cycle Count element request occurs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| R KJXDK   | While TRCCCCTLR.THRESHOLD is programmed with a value less than TRCIDR3.CCITMIN, the generation of Cycle Count elements is CONSTRAINED UNPREDICTABLE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| R GDTBW   | When a request for a Cycle Count element occurs, one of the following occurs: • The trace unit generates a Cycle Count element immediately and before any future Commit element . • The trace unit delays generation of the Cycle Count element until after one or more further Commit elements                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| I TCFRL   | Arm recommends that when a request for a Cycle Count element occurs, the Cycle Count element is generated immediately, and that Cycle Count element generation is only delayed in rare and non-repetitive circumstances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

| R BMVKB   | When a Cycle Count element is generated, the Cycle Count element contains the value of the cycle counter at the time the most recent Commit element was generated, and the cycle counter is reset to the number of cycles since the most recent Commit element was generated.                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R PFZXK   | Avalue of 0 indicates that the cycle count value is UNKNOWN.                                                                                                                                                                                                                                                                                                                                    |
| R YVWJW   | When the cycle counter exceeds the maximum supported value, the cycle count value is UNKNOWN.                                                                                                                                                                                                                                                                                                   |
| R YFMWB   | When the trace unit becomes enabled, an UNKNOWN cycle count value occurs for the first Cycle Count element generated.                                                                                                                                                                                                                                                                           |
| R HQKWH   | When a trace unit buffer overflow occurs, an UNKNOWN cycle count value occurs for the first Cycle Count element generated.                                                                                                                                                                                                                                                                      |
| I PDBDY   | The first Cycle Count element after the PE clock has been restarted should have an UNKNOWN cycle count.                                                                                                                                                                                                                                                                                         |
| R WDWGV   | When trace generation becomes inoperative and any of the following are true, the trace unit generates a Discard element : • P0 elements have been generated but the trace unit is unable to output the resolution of those P0 elements . • A Transaction Start element has been generated and trace generation becomes inoperative before the transaction                                       |
| R FHQDX   | When trace generation becomes inoperative due to the trace unit becoming disabled, and a Discard element is generated, the trace unit outputs the Discard element after all other elements.                                                                                                                                                                                                     |
| R NSMJF   | When a PE reset occurs and any of the following are true, the trace unit generates a Discard element : • P0 elements have been generated but the trace unit is unable to output the resolution of those P0 elements . • A Transaction Start element has been generated and the PE reset occurs before the transaction either succeeds or fails.                                                 |
| I SKJSP   | Atrace unit might not generate a Discard element if no P0 elements are speculative.                                                                                                                                                                                                                                                                                                             |
| I TGXKV   | Atrace unit might generate a Discard element even if no P0 elements are speculative.                                                                                                                                                                                                                                                                                                            |
| R CTYFK   | When a Discard element is generated, all uncommitted P0 elements are discarded, that is, the current speculation depth is set to zero.                                                                                                                                                                                                                                                          |
| I TYXLL   | When a Discard element is generated, and a Transaction Start element has been traced but the transaction has not succeeded or failed, the trace unit does not indicate the resolution of the transaction.                                                                                                                                                                                       |
| R WXTQS   | When a Discard element is generated and tracing subsequently becomes operative for the same transaction, the trace unit generates a new Transaction Start element before any P0 elements are generated for the transaction.                                                                                                                                                                     |
| R STQSN   | D4.5.10.20 Instrumentation element The Instrumentation element for a first TRCIT instruction is generated before the Instrumentation element for any TRCIT                                                                                                                                                                                                                                      |
| R WYYPN   | The Instrumentation element contains the following information: • The doubleword contained in the Xt register parameter of the TRCIT instruction. • The Exception level at which the TRCIT instruction was executed.                                                                                                                                                                            |
| I XWZNW   | If Instrumentation tracing is prohibited and tracing is not prohibited, then Arm recommends that the behavior of the TRCIT instruction is unaffected by the state of the trace unit.                                                                                                                                                                                                            |
| I KGBZX   | The TRCIT instruction is added to the list of instructions that support concurrent modification and execution, to allow live patching of the TRCIT instruction. A TRCIT instruction is only permitted to be modified to be a NOP instruction or another encoding of the TRCIT instruction. Only a NOP instruction or a TRCIT instruction is permitted to be modified to be a TRCIT instruction. |

| R SRSGF   | The architecture guarantees that for NOP and TRCIT instructions, after modification of the instruction, behavior is consistent with execution of either: • The instruction originally fetched. • Afetch of the modified instruction.                   |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LGWQF   | Each Instrumentation element generates an Instrumentation packet.                                                                                                                                                                                      |
| I BXHZM   | When non-periodic trace protocol synchronization occurs, the trace unit generates an Alignment Synchronization packet before any Instrumentation packet. SeeR TTLJC .                                                                                  |
| I YWJZW   | There are no requirements on the order between Instrumentation packets and other ETE packets, except for the requirements around an Alignment Synchronization packet and the requirements for ordering Timestamp packets and Timestamp Marker packets. |

## D4.5.11 Trace unit features

IBFHRC

The architecture defines a number of optional and mandatory features that are provided to modify the trace element stream to provide additional information to aid debugging. These features include the following:

- Qelement regions.
- Branch broadcasting.
- Context identifier tracing.
- Cycle counting.
- Event trace.
- No overflow.
- PE Stalling and overflow avoidance.
- Timestamping.
- Virtual context identifier tracing.

For the optional features, the inclusion of these optional features is indicated in TRCIDR0-TRCIDR13.

## D4.5.11.1 Q regions

| I XFPKH   | The support for Qelement is OPTIONAL, as indicated by TRCIDR0.QSUPP.                                                                                                                                                                                |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FSXRY   | The use of Qelements must be explicitly enabled if the trace unit is to use them.                                                                                                                                                                   |
| I CGQZJ   | While Qelements are enabled, the trace element stream might not contain enough information to determine the complete program flow, because some changes in flow might not be explicitly indicated.                                                  |
| I QLVSG   | Arm recommends that Qelements are only used in cases where generating the full ETE instruction trace element stream might cause the performance of the PE being traced to degrade significantly.                                                    |
| I TNPWC   | The use of Qelements degrades the information that can be extracted from the trace element stream. Arm recommends that Qelement filtering, as indicated by TRCIDR0.QFILT, is also implemented.                                                      |
| I CBKXZ   | If TRCQCTLR is implemented, the trace unit supports the ability to control when Qelements are permitted in the trace element stream using ARCs. The Qelement filtering operates in either Exclude mode, or Include mode, selected by TRCQCTLR.MODE. |
| R DSFJZ   | If Qelements are enabled and Qelement filtering is in Include mode, the ARCs selected by TRCQCTLR.RANGE define where Qelements are permitted.                                                                                                       |
| R WXRDY   | If Qelements are enabled and Qelement filtering is in Exclude mode, the ARCs selected by TRCQCTLR.RANGE define where Qelements are not permitted.                                                                                                   |
| R RBPJF   | When an instruction block contains at least one instruction where Qelements are permitted, the entire instruction block is permitted to generate Qelements .                                                                                        |

RNQSLS

RSGFHP

RCGHSK

IWLPLZ

IDCYQT

The following equation is calculated for each instruction block and defines when Qelements are permitted.

<!-- image -->

While TRCCONFIGR.QE indicates that Qelements are disabled, the trace unit does not generate any Qelements .

While TRCCONFIGR.QE indicates that Qelements are disabled, the trace unit is able to generate all of the elements required to trace the instruction sequence.

## D4.5.11.2 Branch broadcasting

The branch broadcasting feature forces the trace unit to explicitly trace the target addresses of taken direct P0 instructions .

The target addresses are traced using Target Address elements in the instruction trace stream.

Branch broadcasting is enabled by performing both of the following actions:

- Setting TRCCONFIGR.BB to 1.
- Programming TRCBBCTLR to specify how branch broadcasting behaves. TRCBBCTLR selects Address Range Comparators to define when branch broadcasting is active, and selects the operating mode of branch broadcasting:
- -Branch broadcasting is active for all instructions inside the selected ranges. This is known as Include mode.
- -Branch broadcasting is active for all instructions outside the selected ranges. This is known as Exclude mode.

RMHYFV When a direct P0 instruction for which branch broadcasting is active is taken, the trace unit generates a Target Address element to explicitly trace the target of the instruction, regardless of whether the P0 instruction is mispredicted.

RVQTVR

While branch broadcasting is enabled, while the return stack is enabled, the trace unit prioritizes branch broadcasting over the return stack, that is, the return stack does not match on the target of any instruction for which branch broadcasting is active.

RXSVSX

IRJJZW

RGVMFG

IMKQVC

IBMCMB

If TRCBBCTLR is not implemented, while branch broadcasting is enabled, branch broadcasting is active for all instructions.

## D4.5.11.3 Context identifier tracing

The trace unit can be programmed to include information about the current execution context of the program being executed on the PE, including:

- The current process identifier, stored in CONTEXTIDR\_EL1. This is known as the Context identifier .
- The current VMID, stored in CONTEXTIDR\_EL2. This is known as the Virtual context identifier .

The trace unit supports tracing of the Context identifier, with TRCIDR2.CIDSIZE indicating a 32-bit Context identifier size.

## D4.5.11.4 Cycle counting

The use of the cycle counting feature introduces Cycle Count elements into the trace element stream to indicate the passage of PE clock cycles.

Counting the number of clock cycles the PE uses to perform a certain function can be useful as a way of measuring program performance, or for profiling the PE.

| R JMLLY   | While cycle counting is enabled, the trace unit outputs Cycle Count packets that contain processor clock cycle count values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TVCCV   | Cycle Count elements are associated with Commit elements , so that when a Commit element is generated, a Cycle Count element might also be generated. Whether a Cycle Count element is generated when a Commit element is generated depends on what cycle count threshold has been specified when programming TRCCCCTLR.THRESHOLD. When a Commit element is generated and the cycle count value is equal to or more than the threshold value, then a Cycle Count element is generated and a Cycle Count packet is output. The cycle count value that is contained in that packet is associated with the Commit element that triggered it. |
| R BHYWB   | While cycle counting is enabled, and when a Commit element is generated and the cycle count value is greater than or equal to the threshold value that is programmed in TRCCCCTLR.THRESHOLD, the trace unit generates a Cycle Count element .                                                                                                                                                                                                                                                                                                                                                                                             |
| I LFLCZ   | Also, because cycle counting is associated with Commit elements , a Cycle Count packet might imply the generation of Commit elements , and so in addition to the cycle count value, some Cycle Count packets also contain a value for the number of Commit elements that the trace unit has generated.                                                                                                                                                                                                                                                                                                                                    |
| I MWQNZ   | The value of cycle count that is given in a new Cycle Count packet indicates the number of processor clock cycles between the new Commit element that the packet is associated with, and the most recent Commit element prior to the new Commit element that had a Cycle Count element associated with it. This means that if there is a requirement for a cumulative cycle count total, the cycle count values from the successive Cycle Count packets can be added together to obtain this.                                                                                                                                             |
|           | D4.5.11.5 Event trace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I GGMQT   | The ETE architecture supports the tracing of additional information in the trace stream. These are known as ETEEvents , also known as Event trace. The trace unit supports up to 4 ETEEvents . The generation of ETEEvents is controlled by selecting resources selectors. The occurrence of ETEEvents can be communicated in the following ways: • To the system by External Outputs.                                                                                                                                                                                                                                                    |
|           | D4.5.11.6 No overflow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| I DJCLX   | Atrace unit might include an optional feature to prevent overflows, which is indicated by TRCIDR3.NOOVERFLOW.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R YSPHL   | TRCSTALLCTLR.NOOVERFLOW controls the no overflow feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| S BSPDF   | Enabling the no overflow feature might have a significant impact on PE performance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R LCGZJ   | While the no overflow feature is enabled, and while the number or frequency of ETEEvents is below an IMPLEMENTATION DEFINED threshold, the trace unit does not overflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| R VHMZX   | The threshold is greater than or equal to one of each numbered ETEEvent , for each trace session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| R MYMKW   | When TRCIDR3.SYSSTALL is 0 the Effective value of TRCSTALLCTLR.NOOVERFLOW is 0 which means the no overflow feature is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R JYYLV   | When TRCSTALLCTLR.ISTALL is 0 and TRCSTALLCTLR.NOOVERFLOW is 1, it is CONSTRAINED UNPREDICTABLE whether any stalling is disabled or whether the no overflow feature is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|           | D4.5.11.7 Stalling the execution of the PE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I MPBVQ   | The trace unit can be programmed to reduce the likelihood of a trace unit buffer overflow. If the trace unit is configured to support PE stalling, TRCIDR3.STALLCTL indicates that PE stalling is implemented and TRCIDR3.SYSSTALL indicates that PE stalling is permitted, then the execution of the PE can be slowed.                                                                                                                                                                                                                                                                                                                   |
| I HPFQP   | It is permissible that the operation of the PE can be affected by the programming of the trace unit. The amount of intrusion and when stalling occurs is IMPLEMENTATION DEFINED. Additional stalling of the PE execution can be achieved by enabling this feature.                                                                                                                                                                                                                                                                                                                                                                        |

IVZSVK

Trace unit stalling of the PE is independent of the operation of the PE.

RNVBGS

PE operations which explicitly interact with the trace unit complete independently of the programming of the ability of the trace unit to stall the PE.

RSCLVV

The trace unit does not stall the PE while any of the following are true:

- The trace unit is in the Disabled state.

- The PE is executing in a Trace Prohibited region (see Trace Prohibited Regions).

- The PE is in Debug State.

- The PE does not allow stalling, that is, TRCIDR3.SYSSTALL == 0b0 .

- Self-hosted trace is disabled and ExternalInvasiveDebugEnabled() == FALSE.

- When TRCSTALLCTLR.ISTALL == 0b0 and TRCSTALLCTLR.NOOVERFLOW == 0b0 .

- Trace output is disabled.

RRWTYJ

When all of the following are true, the trace unit is permitted to stall the PE:

- Stalling of the PE is not prohibited by RSCLVV.

- TRCSTALLCTLR.ISTALL == 0b1 .

- Any of the following are true:

- TRCSTALLCTLR.NOOVERFLOW == 0b1 .

- The available space in the internal storage of the trace unit is below the level indicated in TRCSTALLCTLR.LEVEL.

Otherwise, the trace unit does not stall the PE due to the stalling feature or no overflow feature.

RNVKXX

The trace unit does not indefinitely stall the operation of the PE.

IXPRQJ

In a multi-threaded processor, if the trace unit stalls a PE, Arm recommends that stalling or disruption of the processing of other PEs is minimized. In particular, if tracing of one or more PEs in a multi-threaded processor is enabled but tracing of other PEs in the multi-threaded processor is disabled, Arm recommends that if the PEs being traced are stalled by their respective trace units then the stall has minimal effect on the PEs which are not being traced.

IKBXXH The levels indicated in TRCSTALLCTLR.LEVEL are the levels of intrusion allowed.

IZRQBK

Asummary of the stalling and no overflow scenarios is shown in Table D4-25, when TRCIDR3.STALLCTL is 1 and TRCIDR3.SYSSTALL is 1.

## Table D4-25 Summary of TRCSTALLCTLR stalling and no overflow features

|   ISTALL |   NOOVERFLOW | LEVEL   | Description                                                                                                                                        |
|----------|--------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------|
|        0 |            0 | x       | Stalling is disabled.                                                                                                                              |
|        0 |            1 | x       | It is CONSTRAINED UNPREDICTABLE whether the no overflow feature is enabled or stalling is disabled.                                                |
|        1 |            0 | Zero    | Stalling is enabled at the minimum level.                                                                                                          |
|        1 |            0 | Nonzero | Stalling is enabled and is based on the value in TRCSTALLCTLR.LEVEL.                                                                               |
|        1 |            1 | Zero    | The no overflow feature is enabled, preventing overflows.                                                                                          |
|        1 |            1 | Nonzero | The no overflow feature is enabled, preventing overflows, and TRCSTALLCTLR.LEVEL might cause stalling earlier than necessary to prevent overflows. |

## D4.5.11.8 Timestamping

The trace unit supports timestamping, where a common global time value is inserted in to the trace stream. These timestamps may be used to correlate between multiple trace streams, including those from other PEs or other sources of trace. These timestamps may be used to determine the passage of time, for analyzing performance.

IYVBBW

| I VFWQS   | When timestamping is enabled, the trace unit inserts Timestamp elements in to the trace stream. Each Timestamping element indicates the time that a recent P0 element , Event element , or Instrumentation element occurred, and can be used to accurately determine when that element occurred.                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I YFPDZ   | The time value included in Timestamp elements is selected by TRFCR_EL1 and TRFCR_EL2 and is one of: • Physical time, as seen by the generic timers in the PE. • Virtual time, as seen by the generic timers in the PE. • An IMPLEMENTATION DEFINED time value, often supplied by a CoreSight system.                        |
| I CLZKR   | The insertion of Timestamp elements is controlled by TRCCONFIGR.TS and TRCTSCTLR.                                                                                                                                                                                                                                           |
| I VMGBJ   | Whether an implementation supports Virtual context identifier tracing is IMPLEMENTATION DEFINED. If it does, the trace unit can be programmed to output the identifier of a virtual machine that the PE is executing.                                                                                                       |
| I FDDXM   | This option is enabled by setting TRCCONFIGR.VMID to 0b1 .                                                                                                                                                                                                                                                                  |
| R PTVYD   | If the PE implements EL2, the trace unit supports a 32-bit Virtual context identifier, with TRCIDR2.VMIDSIZE indicating a 32-bit Virtual context identifier size. The source of the Virtual context identifier is CONTEXTIDR_EL2.PROCID.                                                                                    |
| R BRDYF   | If the PE does not implement EL2, the trace unit does not support a Virtual context identifier, with TRCIDR2.VMIDSIZE indicating Virtual context identifier tracing is not supported.                                                                                                                                       |
|           | Previous trace architectures from Arm supported the ability to select the source of the Virtual context identifier. This specification does not support Virtual context identifier selection, and only permits CONTEXTIDR_EL2.PROCID as the source of the Virtual context identifier. See TRCIDR2.VMIDOPT for more details. |

## D4.5.12 Compression

IWVBMT

Additional compression of the trace byte stream is achieved by the following methods:

- Removing elements that can be implied by the trace analyzer:
- -Implying the existence of Commit elements based on the tracing of other elements.
- -Removing Target Address elements that can be calculated by the trace analyzer by analysis of previous traced PE execution.
- Combining multiple elements together into a single packet:
- -Combining Atom elements into a single packet.
- -Combining Cancel elements and Mispredict elements into a single packet.

## D4.5.12.1 Implied commits

The ETE trace protocol provides mechanisms to minimize the number of Commit elements which need to be explicitly output in the trace byte stream. When a P0 element is output in the trace byte stream, if the number of speculative P0 elements output exceeds TRCIDR8.MAXSPEC, then a Commit element is implied which resolves the oldest speculative P0 element .

The trace unit does not generate commit packets for Commit elements that have been implied by the trace protocol.

## D4.5.12.2 Atom packing

The ETE trace protocol provides packets which allow groups of consecutive Atom elements to be packed into a single trace packet. Figure D4-15 shows the decision tree for generating the different formats of Atom packets.

IBTGGX

RYKLRM

IQMVNP

Figure D4-15 Atom packing

<!-- image -->

IXXSGS Cancel Packets can indicate a number of Atom elements and the Cancel element

.

IKWWHP

The Mispredict Packets can indicate a number of Atom elements and the Mispredict element .

## D4.5.12.3 Address compression

The trace unit can remove program addresses from the trace stream. The trace analyzer can infer the addresses from the program image and previous history.

This includes the targets of direct P0 instructions , where the target address is encoded in the instruction itself.

The trace unit retains the Address information of up to the last three addresses that were explicitly output in the trace protocol, as contained in:

- Target Address packets.
- Source Address packets.
- Exception packets.

ILFFCR

RSJPYH

- Transaction Failure packets.
- The sub\_isa from the instruction set encoding.

|         | • PE Reset packets. • Qpackets.                                                                                                                                                                                                                                                                                                             |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I SXNYK | The explicitly output addresses that the trace unit retains are known as the address history buffer.                                                                                                                                                                                                                                        |
| I LPYRK | For optimized trace protocol efficiency, Arm recommends that the address history buffer is three entries deep.                                                                                                                                                                                                                              |
| R LMHFW | When any of the following packets are generated, the trace unit pushes the address value and sub_isa to the address history buffer:                                                                                                                                                                                                         |
| R CMCRT | When an Exception packet is generated, the trace unit pushes the preferred exception return address value and sub_isa to the address history buffer.                                                                                                                                                                                        |
| R FPDFJ | When one of the following packets is generated with an UNKNOWN address, the trace unit pushes an address value of 0x0 and sub_isa of IS0 to the address history buffer. • Transaction Failure packet. • PE Reset packet.                                                                                                                    |
| R BPRDC | When a Target Address packet is generated, the trace unit uses the address history buffer to identify when a Target Address Exact Match packet can be used. When a Target Address Exact Match packet cannot be used, the most recent entry in the address history buffer is used for the Target Address packet selection.                   |
| R GWKFD | When a Source Address packet is generated, the trace unit uses the address history buffer to identify when a Source Address Exact Match packet can be used. When a Source Address Exact Match packet cannot be used, the most recent entry in the address history buffer is used for the Source Address packet selection.                   |
| R YLXFK | When an Exception packet is generated, the trace unit uses the address history buffer to identify when an Exception Exact Match Address packet can be used. When an Exception Exact Match Address packet cannot be used, the most recent entry in the address history buffer is used for the Exception Address packet selection.            |
| R YCMCG | When a Qpacket is generated which implies a Target Address element , the trace unit uses the address history buffer to identify when a Qwith Exact Match Address packet can be used. When a Qwith Exact Match Address packet cannot be used, the most recent entry in the address history buffer is used for the QAddress packet selection. |
| R BTWGD | When a Trace Info packet is generated, the trace unit sets all entries of the address history buffer to have an address value of 0x0 and sub_isa of IS0.                                                                                                                                                                                    |
|         | D4.5.12.4 Return stack address matching                                                                                                                                                                                                                                                                                                     |
| R HNDJJ | The depth of the return stack is IMPLEMENTATION DEFINED from 0 to 15 entries.                                                                                                                                                                                                                                                               |
| I BLYHW | For optimized trace protocol efficiency, Arm recommends the trace unit implements the return stack with at least 3 entries.                                                                                                                                                                                                                 |
| R HFCTC | While TRCCONFIGR.RS is 1, when a Branch with Link instruction is predicted as taken and is traced, the trace unit pushes the following Address information to the return stack: • The instruction address + the instruction size, that is, the return address for the Branch with Link instruction.                                         |

## The Embedded Trace Extension D4.5 About the ETE trace unit

RZKTHK

When a return stack push occurs, all existing entries are shifted down one place on the return stack and the new entry is pushed to the top entry of the return stack.

RZSVDQ

While the return stack is full, when a return stack push occurs, the oldest entry on the return stack is discarded.

RFFXPW

When a Branch with Link instruction is predicted as taken and traced with an E Atom element , when a return stack push occurs, the trace unit pushes to the return stack, even if the prediction is incorrect and is subsequently corrected to an N Atom element .

RNYHFH

When a Branch with Link instruction is predicted as not taken and traced with an N Atom element , the trace unit does not push to the return stack, even if the prediction is incorrect and is subsequently corrected to an E Atom element .

RGVLKJ

When a Branch with Link instruction is implied by a Qelement , the trace unit does not push to the return stack.

RWRXCW

When a Branch with Link instruction is executed in a branch broadcasting region, the trace unit does not push to the

return stack.

RFVRPZ When a Branch with Link instruction is speculatively executed and generates an E Atom element , if that Atom element is subsequently cancelled by a Cancel element then any corresponding entry on the trace unit return stack must be popped from the trace unit return stack.

Note

Discarding the entire contents of the trace unit return stack meets this obligation.

RQHSBN

When an indirect P0 instruction is taken and traced, and the Address information in the resultant Target Address element matches the address and sub\_isa on the top of the return stack, the trace unit performs a return stack pop.

RHTKJS

When a return stack pop occurs, both of the following occur:

- The trace unit discards the Target Address element that matches the address and sub\_isa on the top of the return stack.

- The trace unit removes the top entry of the return stack, and shifts each older entry up one position.

RWBCJG

When an indirect P0 instruction is implied by a Qelement , the trace unit does not perform a return stack pop.

IBCWSQ

When an indirect P0 instruction is taken, it is possible that the target address is predicted incorrectly by the PE.

RYMRGB

When the target address of a taken indirect P0 instruction is incorrectly predicted, and the incorrect target address is traced with a Target Address element , the trace unit corrects the incorrect address by generating a new Target Address element with the correct target address, and neither of the target addresses cause a return stack pop.

RGBHNP When the target address of a taken indirect P0 instruction is incorrectly predicted, and the incorrect target address matches the top entry of the return stack, the trace unit subsequently generates a Target Address element with the correct target address, and neither of the target addresses cause a return stack pop.

RZCCBS

When the final status of the Atom element corresponding to an indirect P0 instruction is E, including when one or more Mispredict elements change the status of the Atom element , the trace unit performs a return stack pop.

Note

Areturn stack push only occurs if the initial Atom element state for the Branch with Link instruction is E. Conversely, a return stack pop only occurs if the final Atom element state for the indirect P0 instruction is E.

RSLDXR

When an instruction that is both a Branch with Link instruction and an indirect P0 instruction is executed, the trace unit performs the following actions on the return stack, in order:

1. Determine whether a return stack push is possible and push if required.

2. Determine whether a return stack pop is possible and pop if required.

Note

Some Arm trace architectures use a different order of operations.

| R SBZJB   | When any of the following occur, the trace unit discards the contents of the return stack: • The trace unit generates a Trace Info element .                                                                                                                                                                                                                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I XRQHQ   | Atrace unit might discard the contents of the return stack at any time.                                                                                                                                                                                                                                                                                                                              |
| I DCNGF   | When the return stack contents are discarded, there is no requirement for the trace analyzer to be aware that this discard operation has occurred. This is because even though the contents of the trace unit return stack are discarded, there are no adverse consequences if the contents of the trace analyzer return stack are retained, but never used.                                         |
| R GZSSX   | After a Trace Info element , a Target Address element and a Context element are required but might not be generated immediately. If the Target Address element and the Context element are not generated before the next P0 element , then any Branch with Link instructions must not push on to the return stack until both the Target Address element and the Context element have been generated. |
| I GYYNG   | The trace analyzer maintains a copy of the last Timestamp element value broadcast. The Timestamp element value might be compressed relative to the last value and only the bits that have changed need to be encoded.                                                                                                                                                                                |
| R GPGQQ   | When a Trace Info packet is generated, the trace unit sets its maintained value of the last Timestamp element to zero, and when the trace unit generates a subsequent Timestamp packet the value is compressed relative to this new zero value. This means that the first Timestamp packet after a Trace Info packet contains all nonzero bits of the Timestamp value.                               |