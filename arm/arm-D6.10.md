## D6.10 Synchronization litmus tests

IDJJBQ

This section details example synchronization scenarios and litmus tests for TSB CSYNC . These are derived from FEAT\_TRF and Trace Synchronization event.

This section uses the terms program order, Reads-from and Coherence-after to define the ordering of System register and memory accesses made by trace operations. These terms are defined for memory accesses in Ordering requirements defined by the formal concurrency model. For the purposes of this section, these terms are used for System registers as well as memory accesses.

The terms external agent, Observer, and Observed-by, also used in this section, are also defined in Ordering requirements defined by the formal concurrency model.

This section does not describe the synchronization rules in Debug state defined in Trace in Debug state. In general, litmus tests for Debug state can be derived by applying the following modifications:

- Where a rule mentions a Context synchronization event (CSE) coming before a TSB CSYNC operation, if the TSB CSYNC is executed in Debug state, then the entry to Debug state can replace that CSE for the rule.
- Where a rule mentions the PE executing instructions in a Trace Prohibited region following the CSE, then executing the instructions in Debug state with the trace unit disabled is sufficient for the rule.

Exit from Debug state is a Context synchronization event.

IFVBPF Figure D6-3 shows RBFJKD and RMJQXM.

Figure D6-3 Indirect read or indirect write by Trace operation after direct write

<!-- image -->

Figure D6-4 Direct write after indirect read or indirect write by Trace operation

<!-- image -->

In RVTNCS, the second Context synchronization event CSE2 is required to ensure the direct read B is not executed before the synchronization barrier TSB. Figure D6-5 shows this.

IMQTRQ

ISLWRW

Figure D6-4 shows RTSPXF.

IJBRHG

Figure D6-5 Direct read after indirect write by Trace operation

<!-- image -->

ILPPFQ If the trace is not prohibited after the Context synchronization event, further trace operations might be generated that are not guaranteed to be synchronized by the TSB CSYNC . For ISLWRW, this applies to the first Context synchronization event CSE1.

Trace is prohibited at higher Exception levels than the owning Exception level. This means that if the PE takes an exception to a higher Exception level than the owning Exception level then trace is prohibited at by taking the exception.

INWRPJ Figure D6-6 shows RDFHWV for an explicit read or a write M1 of a Location made by an instruction B in program order before DSB.

Figure D6-6 Trace operation observing memory operation

<!-- image -->

If all of the following are true, RVLWDM requires that a DSB with required access types of reads and writes does not complete until at least all reads or writes RW made by the Trace Buffer Unit for all trace operations tA relating to a traced instruction A are complete for the set of the observers in the required Shareability domain:

- Either A is executed in program order before a Context synchronization event CSE, or A is CSE.
- The PE is executing in a Trace Prohibited region after CSE.
- CSE is in program order before a Trace synchronization barrier TSB.
- TSB is executed in program order before the DSB .

Figure D6-7 shows a read or a write RW1 of a Location made by the Trace Buffer Unit for a trace operation tA relating to a traced instruction A is complete and therefore will be Observed-by a read or a write RW2 of the same Location made by an instruction B executed in program order after a DSB ISH instruction.

IWLLQH

IJGXWM

Figure D6-7 Observation of Trace operation memory access

<!-- image -->

RHCVVS defines Trace synchronization for Speculative instructions.

For example, an indirect read r1 of a System register made by a trace operation tS for a traced Speculative instruction S Reads-from a direct write W2 to the same System register made by an instruction B, if all of the following are true:

- S is executed in speculative execution-order after a Resolved instruction A.
- Ais executed in program order after a Context synchronization event CSE.
- Bis executed in program order before CSE.

Figure D6-8 shows this.

Figure D6-8 Speculative indirect read or indirect write by Trace operation after direct write

<!-- image -->

RHCVVS defines Trace synchronization for Speculative instructions.

For example, if all of the following are true, a DSB with required access types of reads and writes does not complete until at least all reads or writes RW made by the Trace Buffer Unit for all trace operations tS relating to a traced Speculative instructions S are complete for the required Shareability domain:

- S is executed in speculative execution-order after a Resolved instruction A.
- Ais executed in program order before a Context synchronization event CSE.
- S is not in speculative execution-order after CSE.
- CSE is in program order before a Trace synchronization barrier TSB.
- The PE is executing in a Trace Prohibited region after CSE.
- TSB is executed in program order before the DSB .

Figure D6-9 shows a read or a write RW1 of a Location made by the Trace Buffer Unit for a trace operation tS relating to a traced Speculative instruction S is Complete and therefore will be Observed-by a read or a write RW2 of the same Location made by an instruction B executed in program order after a DSB ISH instruction.

Figure D6-9 Observation of Speculative Trace operation memory access

<!-- image -->