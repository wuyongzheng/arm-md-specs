## D16.2 Properties and behavior of the activity monitors

## D16.2.1 Basic characteristics of the activity monitor event counters

Every activity monitor event counter is a 64-bit wrapping counter. When an activity monitor event counter wraps, the counter overflows.

Note

The Activity Monitor architecture does not provide support for overflow status indication or interrupts.

The state of the authentication signals do not affect counting.

Any change in clock frequency, including when a WFI and WFE instruction stops the clock, can affect any counter.

If FEAT\_AMUv1p1 is implemented, for the architected event counters 0, 2 and 3, and each auxiliary event counter configured to use an offset, there is an offset register which is used to virtualize the count on a read from EL1 or EL0. At EL2, EL3 or from the memory-mapped view, permitted accesses to the counters use the physical view without any offset. See Virtualization

## D16.2.2 Counter configuration and controls

For each architected event counter AMEVCNTR0&lt;n&gt;, there is a corresponding event type register AMEVTYPER0&lt;n&gt; which provides information on the event counted by that counter. The event type registers AMEVTYPER0&lt;n&gt; are read-only.

For each auxiliary event counter AMEVCNTR1&lt;n&gt;, there is a corresponding event type register AMEVTYPER1&lt;n&gt; which provides information on the event counted by that counter. When the event counted by an auxiliary event counter is fixed, the corresponding event type register AMEVTYPER1&lt;n&gt; is read-only. When the event counted by an auxiliary event counter is programmable, the corresponding event type register AMEVTYPER1&lt;n&gt; is read/write.

For each counter group, there is a pair of separate controls to enable and disable the counters in that counter group. AMCNTENCLR0and AMCNTENSET0 are used to disable and enable the architected event counters.

AMCNTENCLR1and AMCNTENSET1 are used to disable and enable the auxiliary event counters.

While the PE is halted in Debug state, AMCR.HDBG controls whether activity monitor counting is halted.

AMUSERENR.EN controls access from EL0 to the Activity Monitor Extension System registers. CPTR\_EL2.TAM and HCPTR.TAM control access from EL0 and EL1 to the Activity Monitor Extension System registers. CPTR\_EL3.TAM control access from EL0, EL1, and EL2 to the Activity Monitor Extension System registers.

Note

These controls obey the priority order described in Prioritization of Synchronous exceptions taken to AArch64 state and Synchronous exception prioritization for exceptions taken to AArch32 state.

AMUSERENR.EN is configurable at EL1, EL2, and EL3. All other controls, as well as the value of the counters, are configurable only at the highest implemented Exception level.

If FEAT\_AMUv1p1 is implemented, AMCG1IDR\_EL0 defines which auxiliary counters are implemented, and if virtual offsets are enabled, indicates which of the implemented auxiliary counters have a virtual offset when read from EL0 and EL1.

If FEAT\_AMUv1p1 is implemented, AMCR.CG1RZ controls whether the auxiliary event counters read as zero if they are accessed at an Exception level lower than the highest implemented Exception level.

## D16.2.3 Power and reset domains

The power domain of the Activity Monitoring Unit is IMPLEMENTATION DEFINED and named the AMU domain.

The reset domain of the Activity Monitoring Unit is IMPLEMENTATION DEFINED and named the AMU reset.

The AMU power domain may be the Core power domain.

When an AMU reset of the AMU power domain occurs, the Activity Monitoring Unit is reset and the counters are reset to zero.

When the PE is not in reset, the Activity Monitoring Unit is available.

## D16.2.4 Accuracy and non-invasive behavior

The activity monitors are a non-invasive component which must provide broadly accurate and statistically useful count information.

The implementation of an architecturally required event might create a conflict between the requirement to be non-invasive and the requirement to present an accurate value of the count under normal operating conditions. An implementation might provide an IMPLEMENTATION DEFINED control that disables accurate count of the event to restore performance and document the impact on performance of accurate counting. The expectations for non-invasive behavior and the degree of inaccuracy of the activity monitors are otherwise as described for the Performance Monitors architecture.

Note

For information on the expectations for non-invasive behavior and the degree of inaccuracy of the Performance Monitors, see Non-invasive behavior and A reasonable degree of inaccuracy.

## D16.2.5 Virtualization

FEAT\_AMUv1p1 supports virtualized access to the Activity Monitors event counters at EL1 and EL0.

The fields HCR\_EL2.AMVOFFEN and SCR\_EL3.AMVOFFEN enable and disable virtualization. When enabled, the architected event counters 0, 2 and 3 have counter offsets. Architected event counter 1 does not have an offset. The register AMCG1IDR\_EL0 indicates which of the implemented auxiliary event counters has implemented counter offsets. An implemented event counter that does not have a defined offset has an effective offset of zero. The offset registers can be accessed only at EL2 or EL3, and affect views of the event counters at EL1 and EL0 from the System register interfaces only.

The AMEVCNTVOFF0&lt;n&gt;\_EL2 registers hold the offsets for the implemented and enabled architected event counters.

The AMEVCNTVOFF1&lt;n&gt;\_EL2 registers hold the offsets for the implemented and enabled auxiliary event counters.