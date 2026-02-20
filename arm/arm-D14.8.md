## D14.8 IMPLEMENTATION DEFINED event numbers

Arm recommends that implementers establish a standardized numbering scheme for their IMPLEMENTATION DEFINED events, with common definitions, and common event numbers, applied to all of their implementations. In general, the recommended approach is for standardization across implementations with common features. However, Arm recognizes that attempting to standardize the encoding of microarchitectural features across too wide a range of implementations is not productive.

The Arm architecture guarantees not to define any event prefixed with IMP\_ as part of the standard Arm architecture.

Arm strongly recommends that at least the following classes of event are identified in the IMPLEMENTATION DEFINED events:

- Separating each of the STALL\_FRONTEND and STALL\_SLOT\_FRONTEND events to count holes in instruction availability.
- Separating each of the STALL\_BACKEND and STALL\_SLOT\_BACKEND events, to count, for example, cumulative duration of stalls, unavailability of execution resources, or missed superscalar issue opportunities.
- Miss rates for additional levels of caches and TLBs.
- Any external events passed to the PE through an IMPLEMENTATION DEFINED mechanism.
- Cumulative duration of a PSTATE.{A, I, F} interrupt mask set to 1.
- Cumulative occupancy for resource queues, such as data access queues, and entry/exit counts, so that average latencies can be determined, separating out counts for key resources that might exist. An implementation might also provide registers in the IMPLEMENTATION DEFINED space to further extend such counts, for example by specifying a minimum latency for an event to be counted.
- Any other microarchitectural features that the implementer considers are valuable to count.

If FEAT\_RME is implemented, IMPLEMENTATION DEFINED events are permitted to count all of:

- Granule Protection Table (GPT) accesses.
- For address translations subject to Granule Protection Checks (GPC):
- -TLB hits. These are called GPT-related TLB hits .
- -TLB misses. These are called GPT-related TLB misses .

The range of possible IMPLEMENTATION DEFINED event numbers is described in The PMU event number space and common events.

It is not required that implementations document the behavior of all IMPLEMENTATION DEFINED PMU events, including which PMU event numbers are used for these IMPLEMENTATION DEFINED events. However, Arm strongly recommends that implementations do include and document IMPLEMENTATION DEFINED PMU events. In particular events related to microarchitectural characteristics of the implementation not covered by Common events.

## Chapter D15 The System Performance Monitors Extension

This chapter describes the implementation of the Arm System Performance Monitors that are an OPTIONAL non-invasive debug component. It contains the following sections:

- About the System Performance Monitors.
- System PMU configuration.
- Accessing System PMUs.
- Accessing System PMU registers.
- Accessing System PMU counters.
- Generating System PMU overflow interrupt requests.