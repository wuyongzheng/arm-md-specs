## G8.2.152 TLBIMVAAL, TLB Invalidate by VA, All ASID, Last level

The TLBIMVAAL characteristics are:

## Purpose

Invalidate all cached copies of translation table entries from TLBs that meet the following requirements:

- The entry is a stage 1 translation table entry, from the final level of the translation table walk.
- The entry would be used to translate the specified address.
- If EL2 is implemented and enabled in the current Security state, the entry would be used with the current VMID.

From the entries that match these requirements, the entries that are invalidated are required for the following translation regime:

- If executed at Secure EL1 when EL3 is using AArch64, the Secure EL1&amp;0 translation regime.
- If executed in Secure state when EL3 is using AArch32, the Secure PL1&amp;0 translation regime.
- If executed in Non-secure state, the Non-secure PL1&amp;0 translation regime.

The invalidation only applies to the PE that executes this System instruction.

## Configuration

Note

This System instruction is not implemented in architecture versions before Armv8.

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TLBIMVAAL are UNDEFINED.

## Attributes

TLBIMVAAL is a 32-bit System instruction.

## Field descriptions

<!-- image -->

| 31   | 12 11   |
|------|---------|
| VA   | RES0    |

## VA, bits [31:12]

Virtual address to match. Any unlocked TLB entries that match the V A will be affected by this System instruction, regardless of the ASID.

## Bits [11:0]

Reserved, RES0.

## Executing TLBIMVAAL

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1000 | 0b0111 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T8 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T8 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TTLB == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TTLB == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.FB == ↪ → '1' then if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then AArch32.TLBI_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, R[t]); else AArch32.TLBI_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBILevel_Last, TLBI_AllAttr, R[t]); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.FB == '1' then AArch32.TLBI_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBILevel_Last, TLBI_AllAttr, R[t]); else if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) ↪ → && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && HCRX_EL2.FnXS == '1' then AArch32.TLBI_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, R[t]); else AArch32.TLBI_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_AllAttr, R[t]); elsif PSTATE.EL == EL2 then AArch32.TLBI_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_AllAttr, R[t]); elsif PSTATE.EL == EL3 then AArch32.TLBI_VAA(SecurityStateAtEL(EL3), Regime_EL30, VMID_NONE, Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_AllAttr, R[t]);
```