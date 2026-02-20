## D1.9 Event monitors

IYVDTB

The architecture supports the following non-invasive architectural components that allow for event monitoring:

Performance Monitors

The Performance Monitors have a wide feature set, flexible selection of counted events, and are read/write in operation.

Activity Monitors

The Activity Monitors have a narrow feature set, limited selection of counted events, and are read-only in operation.

## D1.9.1 The Performance Monitors Extension

IZSPVV

The System registers provide access to a Performance Monitoring Unit (PMU), defined as the OPTIONAL Performance Monitors Extension to the architecture, a non-invasive debug resource that provides information about the operation of the PE.

The PMU provides:

- A64-bit cycle counter.
- An IMPLEMENTATION DEFINED number of event counters. If FEAT\_PMUv3p5 is implemented, the event counters are 64-bit unsigned counters, otherwise the event counters are 32-bit event counters.Each event counter can be configured to count occurrences of a specified event. The events that can be counted are:
- -Architectural and microarchitectural events that are likely to be consistent across many microarchitectures. The PMU architecture uses event numbers to identify an event, and the PMU specification defines which event number must be used for each of these architectural and microarchitectural events.
- -IMPLEMENTATION SPECIFIC events. The PMU specification reserves event numbers for IMPLEMENTATION SPECIFIC events.
- An OPTIONAL 64-bit instructions counter.

For more information, see The Performance Monitors Extension.

## D1.9.2 The Activity Monitors Extension

IPCKDC

If the OPTIONAL Activity Monitors Extension is implemented, the System registers provide access to controls and counters for the Activity Monitors Unit (AMU).

For more information, see The Activity Monitors Extension.