## G8.2.143 TLBIASID, TLB Invalidate by ASID match

The TLBIASID characteristics are:

## Purpose

Invalidate all cached copies of translation table entries from TLBs that meet the following requirements:

- The entry is a stage 1 translation table entry.
- The entry would be used for the specified ASID, and either:
- Is from a level of lookup above the final level.
- Is a non-global entry from the final level of lookup.
- If EL2 is implemented and enabled in the current Security state, the entry would be used with the current VMID.

From the entries that match these requirements, the entries that are invalidated are required for the following translation regime:

- If executed at Secure EL1 when EL3 is using AArch64, the Secure EL1&amp;0 translation regime.
- If executed in Secure state when EL3 is using AArch32, the Secure PL1&amp;0 translation regime.
- If executed in Non-secure state, the Non-secure PL1&amp;0 translation regime.

The invalidation only applies to the PE that executes this System instruction.

## Configuration

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TLBIASID are UNDEFINED.

## Attributes

TLBIASID is a 32-bit System instruction.

## Field descriptions

<!-- image -->

| 31   | 8 7   |
|------|-------|
|      | ASID  |

## Bits [31:8]

Reserved, RES0.

## ASID, bits [7:0]

ASID value to match. Any TLB entries for non-global pages that match the ASID values will be affected by this System instruction.

## Executing TLBIASID

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1000 | 0b0111 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T8 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T8 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TTLB == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TTLB == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.FB == ↪ → '1' then if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then AArch32.TLBI_ASID(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBI_ExcludeXS, R[t]); else AArch32.TLBI_ASID(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBI_AllAttr, R[t]); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.FB == '1' then AArch32.TLBI_ASID(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBI_AllAttr, R[t]); else if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) ↪ → && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && HCRX_EL2.FnXS == '1' then AArch32.TLBI_ASID(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBI_ExcludeXS, R[t]); else AArch32.TLBI_ASID(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBI_AllAttr, ↪ → R[t]); elsif PSTATE.EL == EL2 then AArch32.TLBI_ASID(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBI_AllAttr, R[t]); elsif PSTATE.EL == EL3 then AArch32.TLBI_ASID(SecurityStateAtEL(EL3), Regime_EL30, VMID_NONE, Broadcast_NSH, TLBI_AllAttr, R[t]);
```