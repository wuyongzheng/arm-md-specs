## D13.5 Controlling the PMU counters

This section describes the mechanisms available for controlling the PMU event and cycle counters. The following sections describe those mechanisms:

- Enabling PMU counters.
- Freezing PMU counters.
- Prohibiting counting.

## D13.5.1 Enabling PMU counters

ICFQVP

RKYBQW

Counters are enabled by a combination of the global enable control for the counter and a counter enable control, PMCNTENSET, as described in the following sections.

## D13.5.1.1 Enabling the event counters

The global enable controls for PMU event counters are defined as follows:

- The global enable control for PMU event counters in the third range is PMCCR.EPME.
- The global enable control for PMU event counters in the second range is HDCR.HPME.
- The global enable control for PMU event counters in the first range is PMCR.E.

ISTZYQ

PMCNTENSET.P&lt;n&gt; is the counter enable control for event counter n .

IHQHYY

Table D13-4 shows the combined effect of the counter enable controls.

## Table D13-4 Event counter enables

| PMCCR.EPME   | HDCR.HPME   | PMCR.E   | PMCNTENSET.P[n] == 0   | PMCNTENSET.P[n] == 1   | PMCNTENSET.P[n] == 1   | PMCNTENSET.P[n] == 1   |
|--------------|-------------|----------|------------------------|------------------------|------------------------|------------------------|
|              |             |          |                        | First range            | Second range           | Third range            |
| 0b0          | 0b0         | 0b0      | Disabled               | Disabled               | Disabled               | Disabled               |
| 0b0          | 0b0         | 0b1      | Disabled               | Enabled                | Disabled               | Disabled               |
| 0b0          | 0b1         | 0b0      | Disabled               | Disabled               | Enabled                | Disabled               |
| 0b0          | 0b1         | 0b1      | Disabled               | Enabled                | Enabled                | Disabled               |
| 0b1          | 0b0         | 0b0      | Disabled               | Disabled               | Disabled               | Enabled                |
| 0b1          | 0b0         | 0b1      | Disabled               | Enabled                | Disabled               | Enabled                |
| 0b1          | 0b1         | 0b0      | Disabled               | Disabled               | Enabled                | Enabled                |
| 0b1          | 0b1         | 0b1      | Disabled               | Enabled                | Enabled                | Enabled                |

IVQXCB

IQKDTZ

The global enable control is used, with other controls, for all of the following:

- Enabling counting of events by PMEVCNTR&lt;n&gt;.
- Generation of the PMU overflow interrupt request, PMUIRQ , by PMOVSCLR[n].
- Generation of the CTI overflow interrupt trigger by PMOVSCLR[n].
- When FEAT\_Debugv8p9 is implemented, generation of an External Debug Request, by PMOVSCLR[n].
- When FEAT\_EBEP is implemented, generation of an asynchronous PMU Profiling exception, by PMOVSCLR\_EL0[n].
- When FEAT\_SEBEP is implemented, pending a synchronous PMU Profiling exception, by PMOVSCLR[n].

The global enable controls for the other ranges do not affect whether the event counter PMEVCNTR&lt;n&gt; generates any of these.

The effect of HDCR.{HPME, HPMN} on the counter enables applies at all Exception levels and in all Security states.

ICTDHP

When FEAT\_SEBEP is implemented, if an event counter &lt;n&gt; is configured to count an event that is not a synchronous event, and PMEVTYPER&lt;n&gt;\_EL0.SYNC is 1, then counter &lt;n&gt; does not count.

## D13.5.1.2 Enabling the cycle counter

IBTGDJ

For the cycle counter, PMCCNTR, the global enable control is PMCR.E.

For the cycle counter, the counter enable control is PMCNTENSET.C.

PMCR.DP controls whether the cycle counter is disabled when event counting is prohibited, as described in Prohibiting counting.

## D13.5.1.3 Enabling the instruction counter

IWMNXT

When FEAT\_PMUv3\_ICNTR is implemented, for the instruction counter, PMICNTR\_EL0, the global enable control is PMCR.E and the counter enable control is PMCNTENSET\_EL0.F0.

## D13.5.2 Freezing PMU counters

## D13.5.2.1 Freezing on PMU overflow

RFGSDP

## RBHFSF

ILKVKF

RMZPBW

If FEAT\_PMUv3p7 is implemented, then all of the following apply:

- Affected counters do not count when PMCR.FZO is 1 and any of the following are true:
- -For any event counter &lt;m&gt; in the first range, PMOVSCLR.P&lt;m&gt; is 1, and either FEAT\_SEBEP is not implemented or PMEVTYPER&lt;m&gt;\_EL0.SYNC is 0.
- -FEAT\_PMUv3\_ICNTR is implemented, PMOVSCLR\_EL0.F0 is 1, and either FEAT\_SEBEP is not implemented or PMICFILTR\_EL0.SYNC is 0.
- All of the following counters are affected by this control:
- -Event counters PMEVCNTR&lt;n&gt; in the first range. This applies even when EL2 is disabled in the current Security state.
- -If FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0.
- -If PMCR.DP is 1, the cycle counter PMCCNTR.
- Other counters are not affected by this control. When PMCR.DP is 0, PMCCNTR is not affected by these controls.

If FEAT\_PMUv3p7 and EL2 are implemented, then all of the following apply:

- Affected counters do not count when HDCR.HPMFZO is 1 and any of the following are true:
- -For any event counter &lt;m&gt; in the second range, PMOVSCLR.P&lt;m&gt; is 1, and either FEAT\_SEBEP is not implemented or PMEVTYPER&lt;m&gt;\_EL0.SYNC is 0.
- All of the following counters are affected by this control:
- -Event counters PMEVCNTR&lt;n&gt;\_EL0 in the second range. This applies even when EL2 is disabled in the current Security state.
- Other counters are not affected by this control.

For any event counter PMEVCNTR&lt;n&gt;\_EL0 in the third range, all of the following apply:

- The following controls do not affect whether the event counter PMEVCNTR&lt;n&gt;\_EL0 counts events:
- -PMCR\_EL0.FZO, MDCR\_EL2.HPMFZO, and PMOVSCLR\_EL0[31:0].
- -PMCR\_EL0.FZS, MDCR\_EL2.HPMFZS, PMBSR\_ELx.S, and PMBLIMITR\_EL1.{PMFZ, E}.
- PMOVSCLR\_EL0[n] does not affect any of the following:
- -Whether any implemented event counter counts events.
- -Whether the cycle counter counts cycles.
- -Whether a BRBE freeze event occurs.
- Overflow of the event counter PMEVCNTR&lt;n&gt;\_EL0 never generates the CHAIN, PMU\_OVFS, or PMU\_HOVFS PMU events.

When the applicable PMCR\_EL0.FZO or MDCR\_EL2.HPMFZO bit is 1, it is CONSTRAINED UNPREDICTABLE whether any event happening at or about the same time as the event that caused the overflow is counted. This includes other instances of the same event.

## The Performance Monitors Extension D13.5 Controlling the PMU counters

IPPVQW

The architecture does not define when PMU events are counted relative to the instructions that caused the event. Events caused by an instruction might be counted before or after the instruction becomes architecturally executed, and events might be counted for operations that are not architecturally executed. Events can be counted speculatively, out-of-order, or both with respect to the simple sequential execution of the program. Events might also be counted simultaneously by other event counters when the overflow occurs, including events from different instructions. Multiple instances of an event might occur simultaneously, thus an event counter unsigned overflow can yield a nonzero value in the event counter.

Arm recommends that such counting anomalies are minimized when software uses the freeze on overflow feature. When the freeze on overflow feature is being used, software cannot assume that the event counter stops counting at zero when an overflow occurs.

IDKYFT

If FEAT\_SEBEP is implemented, then the PMCR\_EL0.FZO and MDCR\_EL2.HPMFZO controls ignore the overflow status bits for PMU counters in synchronous mode.

Whether a PMU counter is in synchronous mode or not does not change how it is affected by the freeze-on-overflow condition.

ITBJNR

To freeze the PMU counter values on taking a synchronous PMU Profiling exception, software should configure the relevant PMU counters to not count at the Exception level where the PMU Profiling exception is taken to and higher Exception levels. This has the effect of stopping counting when the PMU Profiling exception is taken.

Note

This mechanism can only be used when profiling software that only executes at lower Exception levels.

ITLHSZ If an event counter n overflows, where n is even and event counter n +1 is configured to count the CHAIN event, it is CONSTRAINED UNPREDICTABLE whether the CHAIN event observes the overflow event when the applicable PMCR\_EL0.FZO or MDCR\_EL2.HPMFZO bit is 1 and the corresponding PMCR\_EL0.LP or MDCR\_EL2.HLP bit is 0.

ILMSFT If a direct read of PMOVSCLR\_EL0 returns a nonzero value for a subset of the overflow flags, which means an event counter n should not count, then a sequence of direct reads of PMEVCNTR&lt;n&gt;\_EL0 ordered after the read of PMOVSCLR\_EL0 and before the PMOVSCLR\_EL0 flags are cleared to zero, will return the same value for each read, because the event counter has stopped counting.

Note

Direct reads of System registers require explicit synchronization for following direct reads of other System registers to be ordered after the first direct read.

## D13.5.2.2 Freezing on an SPE management event

RHSGZX

When all of the following are true, a PMU counter is frozen and does not count:

- FEAT\_SPEv1p2 is implemented.

- PMBLIMITR\_EL1.{PMFZ, E} is {1, 1}.

- SPE profiling is stopped. See Enabling profiling.

- One of the following applies:

- The counter is an event counter PMEVCNTR&lt;n&gt;\_EL0 in the first range and PMCR\_EL0.FZS is 1.

- The counter is an event counter PMEVCNTR&lt;n&gt;\_EL0 in the second range and MDCR\_EL2.HPMFZS is 1. This also applies when EL2 is disabled in the current Security state.

- FEAT\_PMUv3\_ICNTR is implemented, the counter is the instruction counter PMICNTR\_EL0, and PMCR\_EL0.FZS is 1.

- FEAT\_SPE\_DPFZS is implemented, the counter is the cycle counter PMCCNTR\_EL0 and PMCR\_EL0.{FZS, DP} is {1, 1}. If FEAT\_SPE\_DPFZS is not implemented, then the cycle counter is not affected by PMCR\_EL0.FZS.

The pseudocode function SPEFreezeOnEvent() shows this.

See also Profiling Buffer management.

IHMLGP

If the highest implemented Exception level is using AArch32, then the Effective value of PMBLIMITR\_EL1.E is 0 and FEAT\_SPEv1p2 does not affect the PMU event counters. Otherwise, the effect of FEAT\_SPEv1p2 on PMU event counters applies in AArch32 state.

## D13.5.3 Resetting counters

Software can reset all the event counters and/or the cycle counter in a single operation by writing 1 to PMCR.C and/or PMCR.P.

If FEAT\_PMUv3p9 is implemented, then counters can be individually reset together in a single operation using PMZR\_EL0.

## D13.5.4 Prohibiting counting

RWVDWZ

If EL3 is not implemented, the current Security state does not affect the counting of events.

RJRYNM

If EL3 is implemented and FEAT\_Debugv8p2 is not implemented

Counting Attributable events is prohibited in Secure state unless any of the following is true:

- EL3 is using AArch32 and the value of SDCR.SPME is 1.

- EL3 is using AArch64 and the value of MDCR\_EL3.SPME is 1.

- EL3 or EL1 is using AArch32, the PE is executing at EL0, and the value of SDER32\_EL3.SUNIDEN is 1.

- Counting is permitted by an IMPLEMENTATION DEFINED authentication interface, and ExternalSecureNoninvasiveDebugEnabled() == TRUE.

Note

Software can read the Authentication Status register, DBGAUTHSTATUS to determine the state of an IMPLEMENTATION DEFINED authentication interface.

## RJDWFF If EL3 is implemented and FEAT\_Debugv8p2 is implemented and FEAT\_PMUv3p7 is not implemented

Counting Attributable events is prohibited in Secure state unless any of the following is true:

- EL3 is using AArch64 and the value of MDCR\_EL3.SPME is 1.

- EL3 is using AArch32 and the value of SDCR.SPME is 1.

- EL3 or EL1 is using AArch32, the PE is executing at EL0, and the value of SDER32\_EL3.SUNIDEN is 1.

## RGNGCW If EL3 is implemented and FEAT\_PMUv3p7 is implemented

Counting Attributable events is prohibited at EL3 unless any of the following is true:

- EL3 is using AArch64 and the value of MDCR\_EL3.{SPME, MPMX} is {1, 0}.

- EL3 is using AArch64, the value of MDCR\_EL3.{SPME, MPMX} is {1, 1}, the event is being counted by an event counter &lt;n&gt; in the second range.

- EL3 is using AArch32 and the value of SDCR.SPME is 1.

Counting Attributable events is prohibited at EL2, EL1, and EL0 in Secure state unless any of the following is true:

- EL3 is using AArch64 and the value of MDCR\_EL3.{SPME, MPMX} is not {0, 0}.

- EL3 is using AArch32 and the value of SDCR.SPME is 1.

- EL3 or EL1 is using AArch32, the PE is executing at EL0, and the value of SDER32\_EL3.SUNIDEN is 1.

RMMZLZ

When EL2 is implemented, counting Attributable events is prohibited at EL2 unless any of the following is true:

- FEAT\_PMUv3p1 is not implemented.

- HDCR.HPMD is 0.

- The event is being counted by an event counter &lt;n&gt; in the second range.

RMMZLZ

If FEAT\_SEL2 is implemented, counting Attributable events at Secure EL2 is allowed if and only if counting events is allowed in Secure state, and counting events is allowed at EL2.

For each Unattributable event, it is IMPLEMENTATION DEFINED whether it is counted when counting Attributable events is prohibited.

RTDGMF

The accessibility of Performance Monitors registers is unaffected by whether event counting is enabled or prohibited.

RCSRMB

All of the following apply to the instruction counter, PMICNTR\_EL0:

- Counting is prohibited at EL3 unless any of the following is true:

- EL3 is using AArch64 and the value of MDCR\_EL3.{SPME, MPMX} is {1, 0}.

RGKPZH

RKQDQS

ILNLLM

IFZPQV

- -EL3 is using AArch64, the value of MDCR\_EL3.{SPME, MPMX} is {1, 1}, and EL2 is implemented.
- Counting is prohibited at EL2 unless MDCR\_EL2.HPMD is 0.
- Counting is prohibited at EL2, EL1, and EL0 in Secure state unless EL3 is using AArch64 and the value of MDCR\_EL3.{SPME, MPMX} is not {0, 0}.

The cycle counter, PMCCNTR, counts unless any of the following is true:

- The cycle counter is disabled by PMCR\_EL0.E or PMCNTENSET\_EL0.C.
- PMCR.DP is 1 and any of the following is true:
- -Event counting by event counters in first range is prohibited.
- -Event counting by event counters in first range is frozen by PMCR.FZO.
- -FEAT\_SPE\_DPFZS is implemented and event counting by event counters in first range is frozen by PMCR.FZS.

Note

When FEAT\_HPMN0 is implemented and HDCR.HPMN is 0, the cycle counter is disabled by PMCR.DP under the same conditions that would prohibit or freeze event counting by event counters in the first range when HDCR.HPMN is not 0.

- The PE is in Debug state.
- FEAT\_PMUv3p5 is implemented, EL3 is implemented, the PE is in Secure state, and SDCR.SCCD is 1.
- FEAT\_PMUv3p5 is implemented, EL2 is implemented, the PE is executing at EL2, and HDCR.HCCD is 1.
- FEAT\_PMUv3p7 is implemented, the PE is at EL3, EL3 is using AArch64, and MDCR\_EL3.{SCCD, MCCD} is not {0, 0}.

The following controls do not affect whether event counting is prohibited for the event counters in the third range:

- MDCR\_EL3.SPME.
- MDCR\_EL3.MPMX.
- MDCR\_EL2.HPMD.

Counters in the third range can observe all events in all Security states, including Secure state, and, when FEAT\_RME is implemented, Root and Realm states, but these counters are only accessible to an observer that has read or write access to the Root PAS if FEAT\_RME is implemented, or the Secure PAS otherwise.

However, using this feature does extend the attack surface to include to include these observers. For example, if the FEAT\_RME is being used by an external agent to collect telemetry data that is passed to a less secure agent, this might be used to leak information about software executing in Root or Realm states.

Software executing on the PE is unaware that the counters are being used in this way.

The software that configures the counters in the third range should use the PMEVTYPER&lt;n&gt;\_EL0 registers to configure the counters to not count in certain PE states such as Root or Realm or Secure states based on the trust level of agents that consume the event counter data.

The CountPMUEvents(n) function returns TRUE if any of the following apply:

- PMEVCNTR&lt;n&gt; is enabled and allowed to count events at the current Exception level or state.
- n is 31 and the cycle counter is enabled and allowed to count cycles at the current Exception level and state.
- n is 32 and the instruction counter is enabled and allowed to count instructions at the current Exception level and state.
- Otherwise, the function returns FALSE.

However, this function do not completely describe the behavior for Unattributable events.

For more information, see CountPMUEvents() in A-profile Architecture Pseudocode.

IBTVLD The Performance Monitors are intended to be broadly accurate and statistically useful, see Accuracy of the Performance Monitors. Some inaccuracy is permitted at the point of changing between a state where counting is prohibited and a state where counting is allowed, however. To avoid the leaking of information, the permitted inaccuracy is that transactions that are not prohibited can be uncounted. Where possible, prohibited transactions must not be counted, but if they are counted, then that counting must not degrade security.