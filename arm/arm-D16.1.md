## D16.1 About the Activity Monitors Extension

The Activity Monitors Extension is an OPTIONAL extension to the Armv8.4 architecture.

The Activity Monitors Extension implements version 1 of the Activity Monitors architecture, AMUv1, and interfaces to the registers defined by AMUv1, the Activity Monitors registers.

Version 1 of the Activity Monitors architecture implements:

- Acounter group of four architected 64-bit event counters. The events counted by the architected event counter are fixed and architecturally defined.

Note

The Activity Monitors architecture provides space for up to 16 architected event counters. Future versions of the Activity Monitors architecture might use this space to implement additional architected event counters.

- Acounter group of up to 16 auxiliary 64-bit event counters. The event counted for each auxiliary event counter can be fixed or programmable, and whether it is fixed or programmable is IMPLEMENTATION DEFINED. When the event counted by an auxiliary event counter is fixed, this event is IMPLEMENTATION DEFINED.
- Controls for enabling and disabling counters.
- When the event counted by an auxiliary event counter is programmable, controls for assigning an event to the counter.
- Controls that determine whether the activity monitor counters continue to count while the PE is halted in Debug state.

The read-only registers AMCFGR and AMCGCR provide information about features supported by the Activity Monitors Extension, the number of counter groups implemented, the total number of counters implemented, the number of counters implemented within each group, and the size of the counters.

The Activity Monitors Extension provides:

- Amandatory System register interface to the Activity Monitors registers, for both AArch64 and AArch32 states. AArch64 Activity Monitors registers lists the AArch64 Activity Monitors registers, and AArch32 Activity Monitors registers lists the AArch32 Activity Monitors registers. Table K14-3 shows the relationship between the AArch64 and the AArch32 Activity Monitors registers.
- Controls that allow software to enable or disable access by software running at lower Exception levels to the Activity Monitors registers.
- When FEAT\_AMUv1p1 is implemented, and the hypervisor is using AArch64, offset registers that support virtualization of the Activity Monitor event counters.
- An optional external interface providing read-only memory-mapped access to the Activity Monitors registers. Alphabetical index of memory-mapped registers lists the Activity Monitors memory-mapped registers. For more information on the recommended external interface, see Recommended External Interface to the Activity Monitors.