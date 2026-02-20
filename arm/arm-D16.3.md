## D16.3 AMU events and event numbers

The Activity Monitors architecture uses the event number space defined by the Performance Monitors architecture to identify events.

The Activity Monitors architecture defines additional events and adds them to the event number space defined by the Performance Monitors architecture for common events.

If the event is counting an IMPLEMENTATION DEFINED event, it must use an event number from the IMPLEMENTATION DEFINED event space.

When an implementation supports monitoring of an event that is assigned a common architectural or microarchitectural event number, Arm strongly recommends that it uses that number for the event.

When a common event is available to both the Performance Monitors architecture and the Activity Monitors architecture within one implementation, both architectures use the same event number.

## D16.3.1 Architected event counters

Version 1 of the Activity Monitors architecture, AMUv1, requires four events to be counted by the architected activity monitor event counters.

The events required to be counted are:

## 0x0011 , CPU\_CYCLES, Processor frequency cycles

The counter increments on every cycle when the PE is not in WFI or WFE state. When the PE is in WFI or WFE state, this counter does not increment.

This event is counted by AMEVCNTR0&lt;n&gt;, where n is 0.

## 0x4004 , CNT\_CYCLES, Constant frequency cycles

The counter increments at a constant frequency when the PE is not in WFI or WFE state, equal to the rate of increment of the System counter, CNTPCT\_EL0. When the PE is in WFI or WFE state, this counter does not increment.

This event is counted by AMEVCNTR0&lt;n&gt;, where n is 1.

## 0x0008 , INST\_RETIRED, Instructions retired

This event is defined identically to INST\_RETIRED in the FEAT\_PMUv3 architecture.

This event is counted by AMEVCNTR0&lt;n&gt;, where n is 2.

## 0x4005 , STALL\_BACKEND\_MEM, Memory stall cycles

The counter counts cycles in which the PE is unable to dispatch instructions from the frontend to the backend of the PE due to a backend stall caused by a demand data miss in the last level of data or unified cache within the PE clock domain or, if Armv8.7 is implemented, a Non-cacheable data access in progress.

If Armv8.7 is not implemented, it is IMPLEMENTATION DEFINED whether the counter counts backend stall cycles when a Non-cacheable data access is in progress.

This event is counted by AMEVCNTR0&lt;n&gt;, where n is 3.

## D16.3.2 Auxiliary event counters

Auxiliary event counters can count events defined by the Performance Monitors architecture and IMPLEMENTATION DEFINED events defined specifically for activity monitoring.

Implementations must not reuse an IMPLEMENTATION DEFINED event number for different hardware events across the Performance Monitors architecture and the Activity Monitors architecture.

## Chapter D17 The Statistical Profiling Extension

This chapter describes the Statistical Profiling Extension. It contains the following sections:

- About the Statistical Profiling Extension.
- Defining the sample population.
- Controlling when an operation is sampled.
- Enabling profiling.
- Filtering sample records.
- The profiling data.
- The Profiling Buffer.
- Profiling Buffer management.
- Synchronization and Statistical Profiling.