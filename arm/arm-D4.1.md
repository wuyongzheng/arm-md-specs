## D4.1 About the Embedded Trace Extension

IJTPNL

FEAT\_ETE describes the operation of a trace unit. The trace unit provides details about software control flow running on a PE which can be used to aid debugging or optimization. The trace unit provides filtering functionality to allow the targeting of the information to specific code regions or periods of operation.

ILVKQS

FEAT\_ETE overlaps with the ETMv4 architecture, while also providing support for new architecture features. For more information on the ETMv4 architecture, see the Arm® Embedded Trace Macrocell Architecture Specification, ETMv4 (ARM IHI 0064) . FEAT\_ETE does not support all the features of ETMv4. For more information on the differences between FEAT\_ETE and the ETMv4 architecture, see Differences between ETM and ETE.

## D4.1.1 Attributes of tracing

## IRGLSR

The attributes of PE tracing are:

## Trace is generated in real time.

Trace provides a means of observing the PE operation while the PE is running. For diagnostic purposes, this is useful as some types of erroneous behavior are only solvable by observing the system during runtime. In addition, because the PE trace can include cycle counts, trace can be used for PE profiling purposes.

## Trace has a minimal effect on functional performance of the PE.

Usually, trace has no effect on the functional performance of the PE. This attribute does depend on the market use of the PE being debugged, however, and on the trace requirements for the PE and the trace solution that is adopted to meet those requirements. For some markets, some impact on PE performance is acceptable but for others, most notably in real-time systems, an impact on PE performance might be unacceptable.

## Trace is available for self-hosted analysis.

The trace from a PE or process is available for analysis by software running on the target. See Self-hosted Trace.

## Trace is deeply embedded in an SoC.

Trace provides a method of debugging software executing on PEs that are deeply embedded within an SoC.

## Trace is available for external analysis.

The trace from a PE or process can be exported off chip for analysis by external tools.

## D4.1.2 Self-hosted Trace

IFNMRL

Self-hosted trace is used for various purposes, including:

## Non-invasive single stepping:

The trace provides a history of execution similar to that obtained by single-stepping through code.

## Failure logging:

This is similar to a stack trace dump when a failure occurs.

## Performance analysis:

The trace might be used with other trace sources or performance analysis units to analyze program performance.

IVVSCJ

Capturing the trace on-chip involves one of the following:

## Use of system memory:

The trace output from the trace unit is directed to a buffer in main system memory through the Trace Buffer Unit defined by FEAT\_TRBE.

## Use of existing shared system memory, where some main system memory is reserved for trace capture:

The trace output from the trace unit is directed to the reserved memory over the main system bus, typically using CoreSight technology such as a CoreSight ETR.

## Use of a dedicated on-chip buffer:

The trace output from the trace unit is directed to the dedicated memory, typically using CoreSight technology such as a CoreSight ETB. A dedicated bus such as AMBA ATB is also usually implemented between the trace unit and the dedicated memory. Use of dedicated memory means that PE tracing can be performed with zero or minimal effect on system behavior.

AMBAATBisdefined by the AMBA®ATBProtocol Specification (ARM IHI 0032) .

## D4.1.3 External debug

ITQGBH

External debug is commonly used in trace applications that require long-term logging of behavior. In addition, external debug is more likely to be used when the impact of PE tracing on system performance must be minimized.

For example, external debug might be used:

- For debugging real-time systems.
- When analyzing programs that do not frequently vary their behavior.
- For debugging software, where a history of execution is required up to the point of failure.

Exporting the trace off-chip usually involves one of the following methodologies:

## D4.1.3.1 Real-time continuous export

This can be done using either:

- Adedicated trace port capable of sustaining the bandwidth of the trace.
- An existing interface on the SoC, such as a USB or other high-speed port.

Use of a dedicated trace port means that the trace can be exported off-chip with zero or minimum effect on system behavior. An existing interface is usually used when system constraints, such as cost or package size, mean that a dedicated trace port is not possible. However, use of an existing interface might affect system behavior, because both trace and normal interface traffic use the same port.

## D4.1.3.2 Short-term on-chip capture with subsequent low speed export

This option is used when a low-cost method of exporting the trace is required, or when system constraints prevent real-time continuous export. The trace output from the trace unit is stored temporarily on-chip, and then exported using either:

- An existing debug port on the SoC, such as a JTAG-DP or SW-DP.
- Another existing interface on the SoC, such as USB.

Typically, the temporary storage is a circular buffer. If the buffer is full, newer trace overwrites older trace, which means that the buffer always contains the most recent trace. In SoCs that employ Arm CoreSight technology, a dedicated Embedded Trace Buffer (ETB) is provided for the on-chip capture of trace.

## D4.1.4 Trace output

| R SVDBD   | The trace unit outputs the trace byte stream to one or more of the following:                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R LGVCX   | If the Trace Buffer Unit is enabled, the trace byte stream is output solely to the Trace Buffer Unit.                                                                                                                                 |
| R FJFNS   | If the Trace Buffer Unit is disabled, the trace byte stream is output to one or more of the other interfaces.                                                                                                                         |
| R HBBDV   | The ETE Trace Output Enable is always implemented when FEAT_ETEv1p3 is implemented and an IMPLEMENTATION DEFINED trace output interface is present.                                                                                   |
| R RPHPJ   | The ETE Trace Output Enable is optional when FEAT_ETE is implemented and an IMPLEMENTATION DEFINED trace output interface is present.                                                                                                 |
| R FTSZG   | When the ETE Trace Output Enable is not implemented and the Trace Buffer Unit is disabled, trace is output to an IMPLEMENTATION DEFINED trace output interface unless such output is disabled by an IMPLEMENTATION DEFINED mechanism. |
| R PJYKY   | When the ETE Trace Output Enable is implemented and TRCEVENTCTL1R.OE is 0 or the Trace Buffer Unit is enabled, trace is never output to any IMPLEMENTATION DEFINED trace output interface.                                            |
| R MMCKW   | When the ETE Trace Output Enable is implemented and TRCEVENTCTL1R.OE is 1 and the Trace Buffer Unit is disabled, trace is output to an IMPLEMENTATION DEFINED trace output interface.                                                 |

## IVJBMM

IPXSSB

Note

|         | The addition of TRCEVENTCTL1R.OE is not backward compatible, and requires a trace analyzer to explicitly enable trace output to any IMPLEMENTATION DEFINED trace output interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I TVDMT | If the trace output is captured by a single capture point dedicated to a PE, and does not mix with any other trace streams, then the value programmed into TRCTRACEIDR.TRACEID does not need to be unique among all values programmed into all trace units in the system. For example, the value 0x01 could be programmed into all trace units that have their own dedicated trace capture point. • One example of a dedicated trace capture point is the Trace Buffer Extension. When FEAT_TRBE is implemented and enabled, the value of TRCTRACEIDR.TRACEID can be the same for all PEs that are using the Trace Buffer Extension. For more information, see The Trace Buffer Extension. • Another example of a dedicated trace capture point is a CoreSight ETR connected throughanAMBAATB interface and dedicated to a PE. If the AMBAATBinterface connects to the ETR without mixing with any other trace streams, TRCTRACEIDR.TRACEID does not need to be unique when using the ETR, and when ensuring |
| R RWPFG | If an AMBAATBinterface is implemented, the trace unit must support all of the following: • ATB triggers, indicated by TRCIDR5.ATBTRIG. • A7-bit trace ID, indicated by TRCIDR5.TRACEIDSIZE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| I QJKVW | Arm recommends that if the trace unit implements either an AMBAATBinterface, or an IMPLEMENTATION DEFINED interface for trace output, then the path from the interface is not affected by a Warm reset of the PE. This ensures tracing is possible through a Warm reset of the PE, which is useful for low level debugging scenarios.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| R NLSSL | While all trace outputs are disabled, the trace unit considers any generated trace data as having been output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## D4.1.5 Trace sessions

| R GLTKQ   | At any one time, the trace unit is either enabled or disabled. For more information on the possible states of the trace unit, see Trace unit programming states.                                                                                                         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XBPSQ   | A trace session is the period between the trace unit becoming enabled, and when the trace unit next becomes disabled.                                                                                                                                                    |
| R MTLFH   | While the trace unit is enabled, the ViewInst() function is either active or inactive . While ViewInst() is active , the trace unit generates trace for instructions that are executed, unless trace generation is inoperative .                                         |
| R MFNWB   | Whether ViewInst() is active or inactive is independent of whether trace generation is operative or inoperative .                                                                                                                                                        |
| R ZVNKV   | Trace generation is operative while neither of the following are true: • The trace unit is disabled. • The trace unit is recovering from a trace unit buffer overflow.                                                                                                   |
| R RDPSW   | Trace generation becomes operative when trace generation transitions from being inoperative to operative , and occurs when any of the following occur: • When the trace unit transitions from being disabled to being enabled.                                           |
| R BDRKW   | Trace generation becomes inoperative when trace generation transitions from being operative to inoperative , and occurs either: • When the trace unit transitions from being enabled to being disabled.                                                                  |
| R LDDLP   | When the trace unit is unable to generate at least one trace packet which is required by the architecture, a trace unit buffer overflow occurs.                                                                                                                          |
| I HDJWW   | Atrace unit buffer overflow is typically caused when any buffering in the trace unit is unable to receive more trace packets. Inability to receive trace packets is often caused by being unable to sustain output of trace packets to any trace capture infrastructure. |

Note

Atrace unit buffer overflow is independent of the Trace Buffer Unit filling or wrapping a trace buffer in memory. However a trace unit buffer overflow might be caused by the Trace Buffer Unit rejecting trace data due to insufficient capacity, and the limit of any trace unit internal buffers is subsequently reached.

## D4.1.6 Trace unit programming states

RWMGGP The trace unit is always in one of the states shown in Figure D4-1 and Table D4-1.

Figure D4-1 Trace unit programming states

<!-- image -->

Table D4-1 Trace unit programming states

| State    | TRCSTATR.IDLE   | TRCSTATR.PMSTABLE   | Trace unit enabled   |
|----------|-----------------|---------------------|----------------------|
| Idle     | 0b1             | 0b1                 | No                   |
| Enabling | 0b1             | UNKNOWN             | Yes                  |
| Running  | 0b0             | UNKNOWN             | Yes                  |
| Unstable | 0b0             | 0b0                 | No                   |
| Stable   | 0b0             | 0b1                 | No                   |

| R DXFFN   | When the trace unit becomes enabled, the trace unit transitions from the Idle state to the Enabling state.                                              |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| R ZFPHC   | The trace unit transitions from the Enabling state to the Running state in a finite amount of time.                                                     |
| R TZSRP   | When the trace unit becomes disabled, the trace unit transitions from the Running state to the Unstable state.                                          |
| R CZHWF   | The trace unit transitions from the Unstable state to the Stable state in a finite amount of time.                                                      |
| R BPTKT   | While the trace unit is in the Stable and Idle states, the states of the following fields do not change other than by direct writes or external writes: |

IPRQRD

- TRCVICTLR.SSSTATUS.
- TRCSEQSTR.STATE.
- TRCCNTVR&lt;n&gt;.VALUE.
- TRCSSCSR&lt;n&gt;.STATUS.
- TRCRSR.EVENT.
- TRCRSR.EXTIN.
- TRCRSR.TA.

ITDLZL The trace unit programmers' model state can be safely read when in any of the Stable or Idle states.

RTRZCP When the trace unit becomes fully idle and both of the following are true, the trace unit transitions from the Stable state to the Idle state:

- The trace unit is drained of any trace.
- With the exception of the programming interfaces, all external interfaces on the trace unit are quiescent.

RRWYQD While the trace unit is not in the Idle state, direct writes and external writes to the trace unit registers are CONSTRAINED UNPREDICTABLE, except for the following registers:

- TRCPRGCTLR.
- TRCCLAIMSET.
- TRCCLAIMCLR.

This CONSTRAINED UNPREDICTABLE behavior is one of the following:

- The write is ignored.
- The register takes an UNKNOWN value.

The trace byte stream might also be corrupted and analysis of the byte stream might be impossible.

RMDZDN While the trace unit is not in the Idle or Running states, changing the value of TRCPRGCTLR.EN is CONSTRAINED UNPREDICTABLE.

This CONSTRAINED UNPREDICTABLE behavior is one of the following:

- The write is ignored.
- The register takes an UNKNOWN value.

For more information, see:

- Behavior on enabling.
- Behavior on disabling.
- Access permissions on the corresponding register page.

IFJPCN Figure D4-2 shows the procedure that must be used when programming the trace unit registers using the external debug interface.

IZGJRF

Figure D4-2 External debug interface programming procedure

<!-- image -->

Figure D4-3 shows the procedure that is used when programming the trace unit registers using the System instruction interface.

Figure D4-3 System instruction programming procedure

<!-- image -->