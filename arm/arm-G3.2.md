## G3.2 Prohibited regions in self-hosted trace

Trace is not generated in prohibited regions. The pseudocode function TraceAllowed () indicates whether tracing is allowed in the current Security state and Exception level.

The IMPLEMENTATION DEFINED debug authentication interface can allow an external agent to disable the self-hosted trace extension.

If self-hosted trace is enabled, tracing is prohibited in Secure state when SDCR.STE == 0.

If self-hosted trace is enabled, tracing is prohibited in Realm state when MDCR\_EL3.RLTE == 0.

## G3.2.1 Controls to prohibit trace at Exception levels

If self-hosted trace is enabled, TRFCR, TRFCR\_EL1, TRFCR\_EL2 and HTRFCR control whether trace is prohibited at an Exception level. While self-hosted trace is disabled, these registers are ignored.

If self-hosted trace is enabled, tracing is prohibited at EL0 if one of the following is true:

- The Effective value of HCR\_EL2.TGE == 0 and TRFCR\_EL1.E0TRE == 0.
- The Effective value of HCR.TGE == 0 and TRFCR.E0TRE == 0.
- The Effective value of HCR\_EL2.TGE == 1 and TRFCR\_EL2.E0HTRE == 0.

If self-hosted trace is enabled, tracing is prohibited at EL1 if TRFCR.E1TRE == 0.

If self-hosted trace is enabled, tracing is prohibited at EL2 if HTRFCR.E2TRE == 0.

If self-hosted trace is enabled, tracing is prohibited at EL3 if one of the following is true:

- EL3 is in AArch64 state.
- EL3 is in AArch32 state and TRFCR.E1TRE == 0.

The pseudocode TraceAllowed () shows the preceding rules.

If FEAT\_ETE is not implemented, when self-hosted trace is enabled, no events are exported to the trace unit when tracing is prohibited.

If FEAT\_ETE is not implemented, when self-hosted trace is disabled, no events are exported to the trace unit when the PE is in Secure state and counting in Secure state is prohibited.

If FEAT\_ETE is not implemented, when PMCR\_EL0.X==0 or PMCR.X==0, no PMU events are exported to the trace unit.

If FEAT\_ETE is implemented, see External inputs for the rules governing export of events to the trace unit.

Otherwise, PMU events are exported to the trace unit.

## G3.2.2 Self-hosted trace and address translation

Ahypervisor can use HTRFCR.CX to control visibility of VTTBR.VMID.

If self-hosted trace is enabled, and HTRFCR.CX == 0, or if EL2 is not implemented:

- The value of VTTBR.VMID is not traced.
- Comparisons with VTTBR.VMID do not match and results of comparison are not exposed through the comparators.

The trace unit may either prohibit trace for these values, or may record a VTTBR.VMID value of zero in the trace.