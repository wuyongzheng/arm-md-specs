## G3.1 About self-hosted trace

Atrace unit generates trace data to describe the program flow of the PE.

The trace unit can be an implementation of any of the following:

- In Armv8, a standard Arm Embedded Trace Macrocell (ETM). See Arm ® Embedded Trace Macrocell Architecture Specification, ETMv4.
- In Armv9, the Embedded Trace Extension (ETE). See The Embedded Trace Extension.
- An IMPLEMENTATION DEFINED trace function.

If an Armv8.4-compliant PE implements an ETM Architecture trace unit that includes the ETM System register interface, FEAT\_TRF must be implemented.

If an Armv9-compliant PE implements FEAT\_ETE, FEAT\_TRF must be implemented.

If any of the following are true, then Arm recommends that FEAT\_TRF is implemented, but this is not mandatory:

- An Armv8.4-compliant PE or Armv9-compliant PE implements an IMPLEMENTATION DEFINED trace unit.
- An Armv8.4-compliant PE implements an ETM Architecture trace unit but does not implement the ETM System register interface.

Self-hosted trace happens when the agent controlling the trace collection is part of the same software stack as the software being traced. The agent controls prohibited regions. The information collected by the agent is sent to a trace sink.

The trace unit and the PE must have the same view of the debug authentication interface. If FEAT\_TRF is implemented, ExternalNoninvasiveDebugEnabled () is always TRUE.

## G3.1.1 Trace Sinks

The trace unit sends the trace data to a trace sink. A system might include multiple trace sinks, and allow software to configure which trace sink or sinks are used.

An example of an internal trace sink is an Embedded Trace Router (ETR), which allows software to define a buffer in memory. Trace data is written to this buffer.

If FEAT\_TRBE is implemented, the PE includes a Trace Buffer Unit. Trace data is written directly to memory by the Trace Buffer Unit. See The Trace Buffer Extension.

In Armv8, Arm recommends that a system that includes FEAT\_TRF incorporates an ETR, and follows the system architecture described by the CoreSight Base System Architecture (CS-BSA) .

## G3.1.2 Register controls to enable self-hosted trace

| R QFYNM   | For EL1 using AArch64, see AArch64 Self-hosted Trace. If FEAT_TRF is implemented, self-hosted trace is enabled if any of the following are true, and disabled otherwise: • EDSCR.TFO == 0. • EDSCR.TFO == 1, EL3 is implemented, SDCR.STE == 1, and ExternalSecureNoninvasiveDebugEnabled() () == FALSE. • EDSCR.TFO ==1, EL3 is not implemented, the PE executes in Secure state, and ExternalSecureNoninvasiveDebugEnabled() () = FALSE. • EDSCR.TFO ==1, FEAT_RME is implemented, MDCR_EL3.RLTE == 1, and ExternalRealmNoninvasiveDebugEnabled() () = FALSE. The pseudocode function SelfHostedTraceEnabled() shows these rules.   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I QNXVJ   | If FEAT_TRF is not implemented, self-hosted trace is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| I ZJMLF   | While self-hosted trace is disabled, ExternalNoninvasiveDebugAllowed() controls whether tracing is prohibited or allowed in each Security state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

ITTFDJ

The self-hosted trace extensions do not provide any mechanism to control software access to the trace unit external debug interface.