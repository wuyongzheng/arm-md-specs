## G8.2.137 TLBIALL, TLB Invalidate All

The TLBIALL characteristics are:

## Purpose

Invalidate all cached copies of translation table entries from TLBs that are from any level of the translation table walk. The entries that are invalidated are as follows:

- If executed at EL1, all entries that:
- Would be required for the EL1&amp;0 translation regime.
- Match the current VMID, if EL2 is implemented and enabled in the current Security state.
- If executed in Secure state when EL3 is using AArch32, all entries that would be required for the Secure PL1&amp;0 translation regime.
- If executed at EL2, and if EL2 is enabled in the current Security state, the stage 1 or stage 2 translation table entries that would be required for the PL1&amp;0 translation regime and matches the current VMID.

The invalidation only applies to the PE that executes this System instruction.

## Configuration

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TLBIALL are UNDEFINED.

## Attributes

TLBIALL is a 32-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Rt&gt; is ignored.

## Executing TLBIALL

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1000 | 0b0111 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T8 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T8 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TTLB == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TTLB == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.FB == ↪ → '1' then if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then AArch32.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBI_ExcludeXS); else AArch32.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBI_AllAttr); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.FB == '1' then AArch32.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBI_AllAttr); else if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) ↪ → && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && HCRX_EL2.FnXS == '1' then AArch32.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBI_ExcludeXS); else AArch32.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBI_AllAttr); elsif PSTATE.EL == EL2 then AArch32.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBI_AllAttr); elsif PSTATE.EL == EL3 then AArch32.TLBI_ALL(SecurityStateAtEL(EL3), Regime_EL30, Broadcast_NSH, TLBI_ExcludeXS);
```