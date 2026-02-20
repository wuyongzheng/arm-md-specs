## D3.4 Synchronization in self-hosted trace

The trace unit is an indirect observer of the System registers.

If FEAT\_TRBE is implemented, the requirements in this section are extended. See Synchronization and the Trace Buffer Unit.

While self-hosted trace is enabled, indirect reads of the trace filter control fields, TRFCR\_EL1.{E1TRE, E0TRE} and TRFCR\_EL2.{E2TRE, E0HTRE} are treated as indirect reads made by the instruction being traced. For these register fields, in addition to the standard requirements for synchronization of System register accesses, when a trace filter control value is changed and synchronization is not explicitly specified, one of the following occurs:

- The behavior of the PE must be consistent with the control value having the old value.
- The behavior of the PE must change the control value at a point in the simple sequential execution of the program, so that before that point, the behavior of the PE is consistent with the control value having the old value, and after that point the behavior of the PE is consistent with the control value having the new value.

If there are multiple direct writes to the register without explicit synchronization, the behavior is consistent with the writes occurring in program order.

The TSB CSYNC operation is used to ensure that a trace operation, due to a trace unit generating trace for an instruction has completed. The TSB CSYNC operation can be reordered with respect to other instructions, so must be combined with at least one Context synchronization event to ensure the operations are executed in the required order. This means that a direct write to TRFCR\_EL1 or TRFCR\_EL2 is guaranteed to be observed by the trace unit only after a subsequent Context synchronization event. For more information, see Trace Synchronization Barrier.

While self-hosted trace is disabled, the trace unit might impose stronger synchronization requirements.

## Chapter D4 The Embedded Trace Extension

This chapter describes the Embedded Trace Extension (ETE). It contains the following sections:

- About the Embedded Trace Extension.
- Programmers' model.
- Trace elements.
- Instruction and exception classification.
- About the ETE trace unit.
- Resource operation.