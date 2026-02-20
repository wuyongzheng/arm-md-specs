## D6.11 UNPREDICTABLE behavior

- RPFJJZ In the absence of correct synchronization events, it is UNPREDICTABLE whether an indirect read made by a trace operation of a System register updated by a direct write will return the old or the new values. A trace operation might make multiple indirect reads of a System register, and each might return a different one of the old or the new values.

IGGGPH

INRQQF

For example, a trace operation might read MDCR\_EL2.E2TB twice, as follows:

1. When the trace operation is first generated, to evaluate TraceAllowed() and determine whether trace is prohibited.
2. When the trace operation is complete and ready to be written to memory, to evaluate TraceBufferOwner() to determine the context for TRBPTR\_EL1.

If MDCR\_EL2.E2TB is updated without proper synchronization between these two events, both the old and new value might be used.

In the absence of correct synchronization events, it is UNPREDICTABLE whether a direct read of a System register updated by an indirect write made by a trace operation will return the old or the new values.

- ITRWFM If an instruction is traced because the Trace Buffer Unit is enabled and running , but a later indirect read of a System register by the trace operation for the instruction determines that the trace data cannot be written to memory, because the Trace Buffer Unit now appears to be disabled, then one of the following occurs, and it is CONSTRAINED UNPREDICTABLE which:
- The trace data is written to memory.
- The trace data is sent to an IMPLEMENTATION DEFINED trace bus.
- The trace data is written to memory and sent to an IMPLEMENTATION DEFINED trace bus.
- The Trace Buffer Unit discards the trace data.

This also includes any trace data that might be flushed by the trace unit, for example due to a TSB CSYNC operation. If the Trace Buffer Unit discards the trace data, a trace buffer management event might be generated:

- TRBSR\_ELx.EC is set to a CONSTRAINED UNPREDICTABLE choice of the following values:
- -0x00 , other buffer management event. TRBSR\_ELx.BSC is set to 0b000000 , access not allowed.
- -0x1F , IMPLEMENTATION DEFINED buffer management event.

It is also CONSTRAINED UNPREDICTABLE whether any of the following occur, whether or not the trace data is written to memory:

- The current write pointer and, if TRBSR\_ELx.TRG is 1, the Trigger Counter are updated for the trace data.
- Atrace buffer management event that would have been generated is observed and/or generated.
- APMUevent that would have been generated is generated.

If the Effective value of SCR\_EL3.{NSE, NS} does not match the owning Security state, it is CONSTRAINED UNPREDICTABLE whether any trace data:

- Is written to memory using a virtual address translated using the owning translation regime.
- Is written to memory using a virtual address translated using the translation regime formed from the owning Exception level and the Security state selected by the Effective value of SCR\_EL3.{NSE, NS}.
- Is silently discarded and not written to memory.
- Is discarded and not written to memory and a trace buffer management event is generated as follows:
- -TRBSR\_ELx.IRQ is set to 1, where ELx is defined by RBNQRP.
- -If TRBSR\_ELx.S is 0, then all of the following occur:
- -TRBSR\_ELx.S is set to 1, collection is stopped.
- -TRBSR\_ELx.EC is set to 0x00 , other buffer management event.
- -TRBSR\_ELx.BSC is set to 0b000000 , access not allowed.
- -The other fields in TRBSR\_ELx and the other TRBSR\_ELx registers are unchanged.

RRRCNN means that if software executing at EL3 changes the value of SCR\_EL3.NS or SCR\_EL3.NSE before ensuring all trace operations are complete, this might cause CONSTRAINED UNPREDICTABLE behaviors. This means that software must execute a TSB CSYNC instruction to force any trace to be written to the Trace Buffer before changing context.

When FEAT\_RME and FEAT\_TRBE are implemented, if the Trace Buffer Unit is enabled and using Self-hosted mode, and MDCR\_EL3.{NSTB, NSTBE} selects a reserved value, then the behavior is CONSTRAINED UNPREDICTABLE, and the Trace Buffer Unit does one of:

RRRCNN

IMJMWG

RRTGLJ

- Behaves as if the Trace Buffer Unit is disabled.
- Selects an implemented Security state as the owning Security state.
- When trace data is received from the trace unit, it is not written to memory and the Trace Buffer Unit generates a trace buffer management event:
- -TRBSR\_ELx.IRQ is set to 1' where ELx is defined by RBNQRP.
- -If TRBSR\_ELx.S is 0, then all of the following occur:
- -TRBSR\_ELx.S is set to 1, collection is stopped.
- -TRBSR\_ELx.EC is set to 0x00 , other buffer management event.
- -TRBSR\_ELx.BSC is set to 0b000000 , access not allowed .
- -The other fields in TRBSR\_ELx and the other TRBSR\_ELx registers are unchanged.

ILLCLK See also Context switching.

## Chapter D7 The AArch64 System Level Memory Model

This chapter provides a system level view of the general features of the memory system. It contains the following sections:

- About the memory system architecture.
- Address space.
- Mixed-endian support in AArch64.
- Memory Encryption Contexts.
- Cache support.
- External aborts.
- Memory barrier instructions.
- Pseudocode description of general memory System instructions.