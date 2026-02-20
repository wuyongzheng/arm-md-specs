## D13.1 About the Performance Monitors

The Performance Monitors Extension is an OPTIONAL feature of an implementation, but Arm strongly recommends that implementations include version 3 of the Performance Monitors Extension, FEAT\_PMUv3.

Note

No previous versions of the Performance Monitors Extension can be implemented in architectures from Armv8.0.

The Performance Monitors Extension provides:

- The 64-bit cycle counter, PMCCNTR\_EL0. The cycle counter is always implemented.
- The 64-bit instruction counter, PMICNTR\_EL0. The instruction counter is an optional feature, FEAT\_PMUv3\_ICNTR.
- The event counters, PMEVCNTR&lt;n&gt;\_EL0. The number of event counters is an IMPLEMENTATION DEFINED parameter, NUM\_PMU\_COUNTERS, between 0 and 31.

Note

The Performance Monitors Extension permits an implementation with zero event counters only if one of the following is true:

- -EL2 is not implemented.
- -FEAT\_HPMN0 is implemented.

This means only the cycle counter is implemented. Optionally, the instruction counter can also be implemented. Armrecommends that at least two event counters are implemented, and that hypervisors provide at least this many event counters to guest operating systems.

The event counters are either 64 or 32 bit counters:

- -If FEAT\_PMUv3p5 is implemented and the highest Exception level is using AArch64, then the event counters are 64 bit.
- -If FEAT\_PMUv3p5 is not implemented, the event counters are 32 bit.
- Controls for:
- -Enabling counters. See Enabling PMU counters.
- -Resetting counters. Resetting counters.
- -Flagging overflows. See Behavior on overflow.
- -Enabling interrupts on overflow. See Generating overflow interrupt requests.
- -Freezing counters. See Freezing PMU counters.
- -Prohibiting counting. See Prohibiting counting.
- -Threshold and edge counting. See Event threshold and edge counting.
- -Enabling access to the Performance Monitors from EL0. See EL0 access controls.
- -Partitioning the implemented event counters into ranges. See Event counter ranges.

The PMU architecture uses event numbers to identify an event. It:

- Defines event numbers for common events, for use across many architectures and microarchitectures. See Common event numbers.

Note

Implementations that include FEAT\_PMUv3 must, as a minimum requirement, implement a subset of the common events. See Common event numbers.

- Reserves a large event number space for IMPLEMENTATION DEFINED events. See IMPLEMENTATION DEFINED event numbers.

The full set of events for an implementation is IMPLEMENTATION DEFINED. Arm recommends that implementations include all of the events that are appropriate to the architecture profile and microarchitecture of the implementation. For more information, see PMU Event Descriptions.

When an implementation includes the Performance Monitors Extension, the architecture defines the following possible interfaces to the Performance Monitors Extension registers:

- ASystem register interface. This interface is mandatory.

Note

In AArch32 state, the interface is in the ( coproc == 0b1111 ) encoding space.

- An external debug interface which optionally supports memory-mapped accesses. Implementation of this interface is OPTIONAL. See Recommended External Interface to the Performance Monitors.

An operating system can use the System registers to access the counters.

Also, if required, the operating system can enable application software to access the counters. This enables an application to monitor its own performance with fine-grain control without requiring operating system support. For example, an application might implement per-function performance monitoring.

To enable interaction with external monitoring, an implementation might consider additional enhancements, such as providing:

- Aset of events, from which a selection can be exported onto a bus for use as external events.
- The ability to count external events. This enhancement requires the implementation to include a set of external event input signals.

The Performance Monitors Extension is common to AArch64 operation and AArch32 operation. This means the architecture defines both AArch64 and AArch32 System registers to access the Performance Monitors. For example, the Performance Monitors Cycle Count Register is accessible as:

- When executing in AArch64 state, PMCCNTR\_EL0.
- When executing in AArch32 state, PMCCNTR.

When executing in AArch32 state, if FEAT\_PMUv3p5 is implemented, bits [63:32] of the event counters are not accessible. If the implementation does not support AArch64 at any Exception level, 64-bit event counters are not required to be implemented.

When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0 is added, but is not accessible in AArch32 state.

## D13.1.1 Event counter ranges

DXWVNH

ISTBND

The event counters are partitioned into three ranges, as follows:

- If epmn is less-than NUM\_PMU\_COUNTERS, then event counters [ epmn ..(NUM\_PMU\_COUNTERS-1)] are in the third range .

If epmn is equal to NUM\_PMU\_COUNTERS, then no event counters are in the third range .

- If hpmn is less-than epmn , then event counters [ hpmn ..(epmn-1)] are in the second range . If hpmn is equal to epmn , then no event counters are in the second range .
- If hpmn is not zero, then event counters [0..( hpmn -1)] are in the first range . If hpmn is zero, then no event counters are in the first range .

Where epmn and hpmn are defined as follows:

## epmn

## hpmn

Is the Effective value of HDCR.HPMN, as described in RMFYQC. If EL2 is not implemented, then hpmn has the same value as epmn , meaning no counters are in the second range.

This does not depend on whether EL2 is enabled in the current Security state. Each range of event counters has its own global controls.

Counters in the second range are also described as reserved for EL2 .

Counters in the third range are also described as reserved for an external agent .

If any of the following apply, then the behavior is CONSTRAINED UNPREDICTABLE:

Is the Effective value of PMCCR.EPMN. If FEAT\_PMUv3\_EXTPMN is not implemented, then the Effective value of PMCCR.EPMN is NUM\_PMU\_COUNTERS, meaning no counters are in the third range.

|         | • FEAT_HPMN0 is not implemented and HDCR.HPMN is 0. • FEAT_PMUv3_EXTPMN is not implemented and HDCR.HPMN is greater-than NUM_PMU_COUNTERS. • FEAT_PMUv3_EXTPMN is implemented and PMCCR.EPMN is greater-than NUM_PMU_COUNTERS. See: • The Performance Monitors Extension when accessing the Performance Monitors Extension in AArch64 state.                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I SBQGJ | When EL2 is enabled in the current Security state, self-hosted software executing at EL1 and, if enabled by PMUSERENR, EL0 only has access through System registers to event counters in the first range, the cycle counter PMCCNTR, and, if FEAT_PMUv3_ICNTR is implemented, the instruction counter, PMICNTR_EL0. This software is not able to directly determine that event counters in the second range are implemented. Self-hosted software executing at EL2 and EL3, and other Exception levels when EL2 is disabled in the current Security state, additionally has access through System registers to event counters in the second range. Self-hosted software executing on the PE has no access through System registers to event counters in the third range. |
| R NNBYQ | If all of the following are true, then direct reads of PMCR_EL0.N or PMCR.N return the Effective value of HDCR.HPMN: • PE is executing at EL0 or EL1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| R ZCCDD | If FEAT_PMUv3_EXTPMN is implemented and any of the following are true, then direct reads of PMCR_EL0.N or PMCR.N return the Effective value of PMCCR.EPMN: • PE is executing at EL2 or EL3. • PE is executing at EL0 or EL1 and EL2 is either disabled or not implemented in the current Security state. • The access does not generate an exception.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| S HVGXL | An external agent reserving event counters should perform one of the following actions: • Halt the PE immediately after reset and write to PMCCR.EPMN while the PE is in Debug state so that software running on the PE does not observe PMCR.N prior to the configuration of PMCCR.EPMN. • Use an IMPLEMENTATION DEFINED mechanism such that PMCCR.EPMN is set to an intended value. An external agent should not modify PMCCR.EPMN after any software starts running on the PE. Similar guidance applies for EL2 to not modifyHDCR.HPMN for a Guest OS after the Guest has been started.                                                                                                                                                                               |

## D13.1.2 Interaction with EL3

Software executing at EL3 can trap attempts by lower Exception levels to access the PMU. This means that the Monitor can identify any software which is using the PMU and switch contexts, if required.

Software executing at EL3 can:

- Prohibit counting of events Attributable to Secure state.
- If FEAT\_PMUv3p5 is implemented, prohibit the cycle counter from counting cycles in Secure state and at EL3.
- If FEAT\_PMUv3p7 is implemented:
- -Prohibit event counters from counting events at EL3.
- -Prohibit the cycle counter from counting cycles at EL3.
- If FEAT\_PMUv3\_ICNTR is implemented, prohibit the instruction counter from counting architecturally-executed instructions in Secure state and at EL3.

For more information, see Controlling the PMU counters.

In AArch32 state, the Performance Monitors registers are Common registers, see Classification of System registers.

If FEAT\_MTPMU is implemented and EL3 is implemented, MDCR\_EL3.MTPME and SDCR.MTPME enable and disable the PMEVTYPER&lt;n&gt;.MT bit.

## D13.1.3 Interaction with EL2

| I FZHQW   | Software executing at EL3 or EL2 can programHDCR.HPMN to partition the event counters into a first range and a second range. See Event counter ranges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I GZYQM   | Software executing at EL3 or EL2 can: • Trap an access at EL0 or EL1 to the PMU. This means the hypervisor can identify which Guest OSs are using the PMUand intelligently employ switching of the PMUstate. There is a separate trap for the PMCRregister, and if FEAT_FGT is implemented and enabled, fine-grained traps are provided. • If FEAT_PMUv3p1 is implemented, prohibit counting of events Attributable to EL2 by the event counters in the first range. • If FEAT_PMUv3p5 is implemented, prohibit the cycle counter from counting cycles at EL2. • If FEAT_PMUv3_ICNTR is implemented, prohibit the instruction counter from counting instructions at EL2. When EL2 is implemented and enabled in the current Security state, software executing at EL1 and, if enabled by PMUSERENR, EL0: • Will read the Effective value of HDCR.HPMN for PMCR.N. • Cannot access the event counters in the second range, or the controls associated with them. |
| R MFYQC   | If FEAT_PMUv3_EXTPMN is implemented, EL2 is implemented, and MDCR_EL2.HPMN is greater-than the Effective value of PMCCR.EPMN, then all of the following apply: • Direct reads of MDCR_EL2.HPMN return the Effective value of PMCCR.EPMN. • The Effective value of MDCR_EL2.HPMN is the Effective value of PMCCR.EPMN. This includes indirect reads of MDCR_EL2.HPMN as a result of direct reads from PMCR_EL0.N or PMCR.N. If FEAT_PMUv3_EXTPMN is implemented and EL2 is not implemented, then the Effective value of MDCR_EL2.HPMN is the Effective value of PMCCR.EPMN.                                                                                                                                                                                                                                                                                                                                                                                      |
| I MVYJY   | For more information, see: • Enabling PMUcounters. • Counter access. • Controlling the PMUcounters. • Multithreaded implementations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## D13.1.4 Interaction with trace

When FEAT\_ETE is implemented, the trace unit uses the PMU events as External Inputs. See External inputs.

When FEAT\_ETMv4 is implemented, it is IMPLEMENTATION DEFINED whether the implementation exports PMU events to the ETM trace unit, and the form of any exporting is also IMPLEMENTATION DEFINED. If implemented, this exporting is controlled by PMCR.X.

For more information about when the trace unit is permitted to observe PMU events, see Controls to prohibit trace at Exception levels and External inputs.

When FEAT\_ETE is implemented, the PMU implements a set of events for importing external events from the trace unit and the cross-trigger interface. See Required events. Arm recommends similar functionality is implemented when FEAT\_ETMv4 is implemented, and further recommends reusing the events defined for FEAT\_ETE. When implemented, this functionality enables the trace unit to pass in events to be counted.

## D13.1.5 Export of PMU events

It is IMPLEMENTATION DEFINED whether the implementation exports counter events to any other external monitoring agent to provide triggering information. The form of any exporting is also IMPLEMENTATION DEFINED. If implemented, this exporting is controlled by PMCR.X.