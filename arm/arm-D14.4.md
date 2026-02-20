## D14.4 Cycle event counting

The CPU\_CYCLES event and the cycle counter, PMCCNTR, count cycles. The duration of a cycle is subject to any changes in clock frequency, including clock stopping caused by the WFI and WFE instructions.

It is IMPLEMENTATION SPECIFIC whether CPU\_CYCLES and PMCCNTR count when the PE is in WFI or WFE state, even if the clocks are not stopped.

In addition, events such as STALL, STALL\_FRONTEND and STALL\_BACKEND that are defined to only count cycles that are counted by the CPU\_CYCLES event have the same limitation.

## D14.4.1 Cycle event counting in multithreaded implementations

Multithreaded implementations can have various forms, some examples of these are:

- Simultaneous Multithreading (SMT), where every PE thread is active on every Processor cycle.
- Fine-grained Multithreading (FGMT), also known as a Barrel processor, where one PE thread is active on each Processor cycle, and this changes regularly.
- Switch on Event Multithreading (SoEMT), also known as Coarse-grained Multithreading (CGMT), where high latency events cause the processor to switch the active PE thread.

In the above examples, active means that the PE might execute the instructions. A PE can be active but not executing instructions when no instruction is available or because of limited execution resources.

It is IMPLEMENTATION SPECIFIC whether a thread is active when the thread is in WFE or WFI state. This applies for all forms of multithreaded implementation.

When the PMU implementation supports multithreading, the Effective value of PMEVTYPER&lt;n&gt;\_EL0.MT bit is 0, and the thread is not in WFE or WFI state, the CPU\_CYCLES event only counts Processor cycles when the thread is active. For the example multithreaded implementations, this means that, if the event counter is enabled, event counting is not prohibited, and the thread is not in WFE or WFI state:

- For an SMT implementation, the CPU\_CYCLES event counts every Processor cycle.
- For a particular FGMT implementation, that alternates between two threads on each Processor cycle, the CPU\_CYCLES event counts every other Processor cycle.
- For a particular SoEMT implementation, that is waiting for a long latency operation, the CPU\_CYCLES event does not count Processor cycles, as the PE thread is not active.

It is IMPLEMENTATION SPECIFIC whether CPU\_CYCLES event counts Processor cycles when the Effective value of PMEVTYPER&lt;n&gt;\_EL0.MT bit is 0, the thread is active, and the thread is in WFE or WFI state.

If the Effective value of PMEVTYPER&lt;n&gt;\_EL0.MT bit is 1 and at least one thread is not in WFE or WFI state, then the CPU\_CYCLES event counts each Processor cycle, and can only count a maximum of one for each Processor cycle.

If the Effective value of PMEVTYPER&lt;n&gt;\_EL0.MT bit is 1, then all of the following apply for events that count PE cycles when a condition applies:

- The event does not count Processor cycles when all threads are in WFE or WFI state.
- If the event counts PE cycles when a stall condition is true and a second condition is true, then the counter counts Processor cycles when the stall condition is true for all of these PEs, and the second condition is true for any of these PEs.
- If the event counts PE cycles when any other condition is true, then the counter counts Processor cycle when the condition is true for any of these PEs.
- Otherwise, the event counts by the sum of the count across all of these PEs.

For the stall events, the stall condition means the applicable condition described by the STALL, STALL\_FRONTEND, or STALL\_BACKEND event. The second condition is any condition in addition to this. For example, for the STALL\_FRONTEND\_L1I event, the stall condition is STALL\_FRONTEND, and the second condition is when there is a demand instruction miss in the first level of instruction cache. For the STALL, STALL\_FRONTEND, and STALL\_BACKEND events themselves, the second condition is the null TRUE condition.

Note

The cycle counter, PMCCNTR, is not affected by whether the thread is active or inactive. When enabled, PMCCNTR counts every processor cycle.

See Multithreaded implementations,MDCR\_EL3.MTPME, SDCR.MTPME, MDCR\_EL2.MTPME, and HDCR.MTPME for more information about when the Effective value of PMEVTYPER&lt;n&gt;\_EL0.MT is 0.

## D14.4.2 Time as measured by the Performance Monitors cycle counter

The Performance Monitors cycle counter, accessed through PMCCNTR\_EL0 or PMCCNTR, increments from the hardware processor clock, not PE clock cycles.

The relationship between the count recorded by the Performance Monitors cycle counter and the passage of real time is IMPLEMENTATION DEFINED.

See Controlling the PMU counters for information about when the cycle counter does not increment.

Note

- This means that, in an implementation where PEs are multithreaded, when enabled, the cycle counter continues to increment across all PEs, rather than only counting cycles for which the current PE is active.
- Although the architecture requires that direct reads of PMCCNTR\_EL0 or PMCCNTR occur in program order, there is no requirement that the count increments between two such reads. Even when the counter is incrementing on every clock cycle, software might need check that the difference between two reads of the counter is nonzero.

The architecture requires that an indirect write to the PMCCNTR\_EL0 or PMCCNTR is observable to direct reads of the register in finite time. The counter increments from the hardware processor clock are indirect writes to these registers.