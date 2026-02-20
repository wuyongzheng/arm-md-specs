## D3.2 Prohibited regions in self-hosted trace

Trace is not generated in prohibited regions. The pseudocode function TraceAllowed () indicates whether tracing is allowed in the current Security state and Exception level.

The IMPLEMENTATION DEFINED debug authentication interface can allow an external agent to disable the self-hosted trace extension.

If self-hosted trace is enabled and EL3 is implemented, tracing is prohibited in Secure state when MDCR\_EL3.STE == 0.

If self-hosted trace is enabled, tracing is prohibited in Realm state when MDCR\_EL3.RLTE == 0.

If self-hosted trace is enabled, tracing is prohibited in Root state.

## D3.2.1 Controls to prohibit trace at Exception levels

If self-hosted trace is enabled, TRFCR\_EL1 and TRFCR\_EL2 control whether trace is prohibited at an Exception level. While self-hosted trace is disabled, the registers TRFCR\_EL1 and TRFCR\_EL2 are ignored.

If self-hosted trace is enabled, tracing is prohibited at EL0 if one of the following is true:

- The Effective value of HCR\_EL2.TGE == 0 and TRFCR\_EL1.E0TRE == 0.
- The Effective value of HCR\_EL2.TGE == 1 and TRFCR\_EL2.E0HTRE == 0.

If self-hosted trace is enabled, tracing is prohibited at EL1 if TRFCR\_EL1.E1TRE == 0.

If self-hosted trace is enabled, tracing is prohibited at EL2 if TRFCR\_EL2.E2TRE == 0.

If self-hosted trace is enabled, tracing is prohibited at EL3 if one of the following is true:

- EL3 is using AArch64 state.
- EL3 is using AArch32 state and TRFCR.E1TRE == 0.

The pseudocode TraceAllowed() shows the above rules.

If FEAT\_ETE is not implemented, when self-hosted trace is enabled, no events are exported to the trace unit when tracing is prohibited.

If FEAT\_ETE is not implemented, when self-hosted trace is disabled, no events are exported to the trace unit when the PE is in Secure state and counting in Secure state is prohibited.

If FEAT\_ETE is implemented, see External inputs for the rules governing export of events to the trace unit.

If FEAT\_ETE is not implemented, when PMCR\_EL0.X==0 or PMCR.X==0, no PMU events are exported to the trace unit.

Otherwise, PMU events are exported to the trace unit.

If self-hosted trace is enabled, Table D3-1 shows the prohibited regions by Exception level and state.

In the table:

| RLTE   | Means the Effective value of MDCR_EL3.RLTE.                           |
|--------|-----------------------------------------------------------------------|
| STE    | Means the Effective value of MDCR_EL3.STE or SDCR.STE, as applicable. |
| EEL2   | Means the Effective value of SCR_EL3.EEL2.                            |
| TGE    | Means the Effective value of HCR_EL2.TGE.                             |
| P      | Means prohibited.                                                     |
| E2TRE  | Means prohibited if TRFCR_EL2.E2TRE == 0.                             |
| E1TRE  | Means prohibited if TRFCR_EL1.E1TRE == 0.                             |
| E0HTRE | Means prohibited if TRFCR_EL2.E0HTRE == 0.                            |

E0TRE

Means prohibited if TRFCR\_EL1.E0TRE == 0.

n/a

Not applicable.

If FEAT\_TRBE is not implemented, trace is allowed unless otherwise prohibited in Table D3-1.

If FEAT\_TRBE is implemented, the requirements in this section are extended. See The owning translation regime.

Table D3-1 Prohibited regions

| Controls   |      |     |           | Tracing prohibited at   | Tracing prohibited at   | Tracing prohibited at   | Tracing prohibited at   | Tracing prohibited at   | Tracing prohibited at   |
|------------|------|-----|-----------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| State      | RLTE | STE | EL3 using | EEL2                    | TGE                     | EL3                     | EL2                     | EL1                     | EL0                     |
| Non-secure | X    | X   | X         | X                       | 0                       | n/a                     | E2TRE                   | E1TRE                   | E0TRE                   |
| Non-secure | X    | X   | X         | X                       | 1                       | n/a                     | E2TRE                   | n/a                     | E0HTRE                  |
| Secure     | X    | 0   | X         | X                       | X                       | P                       | P                       | P                       | P                       |
| Secure     | X    | 1   | AArch64   | 0                       | X                       | P                       | n/a                     | E1TRE                   | E0TRE                   |
| Secure     |      |     |           | 1                       | 0                       | P                       | E2TRE                   | E1TRE                   | E0TRE                   |
| Secure     |      |     |           | 1                       | 1                       | P                       | E2TRE                   | n/a                     | E0HTRE                  |
| Secure     | n/a  |     | AArch32   | X                       | X                       | E1TRE                   | n/a                     | n/a                     | E0TRE                   |
| Realm      | 0    | X   | X         | X                       | X                       | n/a                     | P                       | P                       | P                       |
| Realm      | 1    | X   | X         | X                       | 0                       | n/a                     | E2TRE                   | E1TRE                   | E0TRE                   |
| Realm      |      |     |           |                         | 1                       | n/a                     | E2TRE                   | n/a                     | E0HTRE                  |
| Root       | X    | X   | X         | X                       | X                       | P                       | n/a                     | n/a                     | n/a                     |

## D3.2.2 Self-hosted trace and visibility of virtual data

Ahypervisor can use TRFCR\_EL2.CX to control visibility of CONTEXTIDR\_EL2 and VTTBR\_EL2.VMID.

If self-hosted trace is enabled and TRFCR\_EL2.CX == 0, or if EL2 is not implemented:

- The values of CONTEXTIDR\_EL2 and VTTBR\_EL2.VMID are not traced.
- Comparisons between CONTEXTIDR\_EL2 and VTTBR\_EL2.VMID do not match and results of comparison are not exposed through the comparators.

The trace unit can either prohibit trace for these values, or can record a CONTEXTIDR\_EL2 or VTTBR\_EL2.VMID value of zero in the trace.