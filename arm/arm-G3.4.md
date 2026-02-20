## G3.4 Synchronization in self-hosted trace

The trace unit is an indirect observer of the trace control registers.

While self-hosted trace is enabled, indirect reads of the trace filter control fields, TRFCR.{E1TRE, E0TRE} and HTRFCR.{E2TRE, E0HTRE} are treated as indirect reads made by the instruction being traced, and are subject to the standard requirements for synchronization of System register accesses.

The TSB CSYNC operation is used to ensure that a trace operation, due to a trace unit generating trace for an instruction has completed. The TSB CSYNC operation may be reordered with respect to other instructions, so must be combined with at least one Context synchronization event to ensure the operations are executed in the required order. This means that a direct write to TRFCR or HTRFCR is guaranteed to be observed by the trace unit only after a subsequent Context synchronization event. For more information, see Trace Synchronization Barrier.

While self-hosted trace is disabled, the trace unit might impose stronger synchronization requirements.

## Chapter G4 The AArch32 System Level Memory Model

This chapter provides a system level view of the general features of the memory system. It contains the following sections:

- About the memory system architecture.
- Address space.
- Mixed-endian support in AArch32.
- AArch32 cache and branch predictor support.
- System register support for IMPLEMENTATION DEFINED memory features.
- External aborts.
- Memory barrier instructions.
- Pseudocode description of general memory System instructions.