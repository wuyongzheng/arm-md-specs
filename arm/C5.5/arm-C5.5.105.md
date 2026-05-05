## C5.5.105 TLBIP RVAE1IS, TLBIP RVAE1ISNXS, TLB Range Invalidate by VA, EL1, Inner Shareable

The TLBIP RVAE1IS, TLBIP RVAE1ISNXS characteristics are:

## Purpose

Invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 1 translation table entry, from any level of the translation table walk up to the level indicated in the TTL hint.
- A64-bit stage 1 translation table entry, if TTL is 0b00 .
- The entry would be used to translate any of the V As in the specified address range, and one of the following applies:
- The entry is from a level of lookup above the final level and matches the specified ASID.
- The entry is a global entry from the final level of lookup.
- The entry is a non-global entry from the final level of lookup that matches the specified ASID.
- The entry is within the address range determined by the formula [BaseADDR &lt;= VA &lt; BaseADDR + ((NUM +1)*2 (5*SCALE +1) * Translation\_Granule\_Size)].
- When EL2 is implemented and enabled in the current Security state:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the entry would be used with the current VMIDand would be required to translate any of the VAs in the specified address range using the EL1&amp;0 translation regime for the Security state.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the entry would be required to translate any of the V As in the specified address range using the EL2&amp;0 translation regime for the Security state.
- When EL2 is not implemented or is disabled in the current Security state, the entry would be required to translate any of the V As in the specified address range using the EL1&amp;0 translation regime for the Security state.

The Security state is indicated by the value of SCR\_EL3.NS if FEAT\_RME is not implemented, or SCR\_EL3.{NSE, NS} if FEAT\_RME is implemented.

The invalidation applies to all PEs in the same Inner Shareable shareability domain as the PE that executes this System instruction.

Note

When a TLB maintenance instruction is generated to the Secure EL1&amp;0 translation regime and is defined to pass a VMIDargument, or would be defined to pass a VMID argument if SCR\_EL3.EEL2==1, then:

- APEwith SCR\_EL3.EEL2==1 is not architecturally required to invalidate any entries in the Secure EL1&amp;0 translation of a PE in the same required shareability domain with SCR\_EL3.EEL2==0.
- APEwith SCR\_EL3.EEL2==0 is not architecturally required to invalidate any entries in the Secure EL1&amp;0 translation of a PE in the same required shareability domain with SCR\_EL3.EEL2==1.
- APEisarchitecturally required to invalidate all relevant entries in the Secure EL1&amp;0 translation of a System MMUinthe same required shareability domain with a VMID of 0.

For 128-bit translation table entry, the range of addresses invalidated is UNPREDICTABLE when Block or Page size corresponding to TTL and TG, for the translation system is not aligned.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP RV AE1IS, TLBIP RVAE1ISNXS are UNDEFINED.

## Attributes

TLBIP RVAE1IS, TLBIP RVAE1ISNXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [127:108]

Reserved, RES0.

## BaseADDR[55:12], bits [107:64]

The starting address for the range of the maintenance instructions. This field is BaseADDR[55:12] for all translation granules.

## ASID, bits [63:48]

ASID value to match. Any TLB entries that match the ASID value and VA value will be affected by this System instruction.

Global TLB entries that match the V A value will be affected by this System instruction, regardless of the value of the ASID field.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being invalidated only uses 8 bits.

## TG, bits [47:46]

Translation granule size.

| TG   | Meaning                  |
|------|--------------------------|
| 0b00 | Reserved.                |
| 0b01 | 4K translation granule.  |
| 0b10 | 16K translation granule. |
| 0b11 | 64K translation granule. |

The instruction takes a translation granule size for the translations that are being invalidated. If the translations used a different translation granule size than the one being specified, then the architecture does not require that the instruction invalidates any entries.

## SCALE, bits [45:44]

The exponent element of the calculation that is used to produce the upper range.

## NUM,bits [43:39]

The base element of the calculation that is used to produce the upper range.

## TTL, bits [38:37]

TTL Level hint. The TTL hint is only guaranteed to invalidate:

- Non-leaf-level entries in the range up to but not including the level described by the TTL hint.
- Leaf-level entries in the range that match the level described by the TTL hint.

| TTL   | Meaning                                                                            |
|-------|------------------------------------------------------------------------------------|
| 0b00  | The entries in the range can be using any level for the translation table entries. |
| 0b01  | The TTL hint indicates level 1.                                                    |
| 0b10  | The TTL hint indicates level 2.                                                    |
| 0b11  | The TTL hint indicates level 3.                                                    |

## Bits [36:0]

Reserved, RES0.

## Executing TLBIP RVAE1IS, TLBIP RVAE1ISNXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
TLBIP RVAE1IS{, <Xt>, <Xt2>}
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b1000 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TTLB == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && HCR_EL2.TTLBIS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.TLBIRVAE1IS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); else
```

```
AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) then AArch64.TLBIP_RVA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]); else AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if ELIsInHost(EL0) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_RVA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, ↪ → TLBILevel_Any, TLBI_AllAttr, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]);
```

TLBIP RVAE1ISNXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b1001 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TTLB == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && HCR_EL2.TTLBIS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → IsFeatureImplemented(FEAT_HCX) && (!IsHCRXEL2Enabled() || HCRX_EL2.FGTnXS == '0') && ↪ → HFGITR_EL2.TLBIRVAE1IS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) then AArch64.TLBIP_RVA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if ELIsInHost(EL0) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_RVA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, ↪ → TLBILevel_Any, TLBI_ExcludeXS, X[t, t2, 128]);
```

```
else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_RVA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]);
```
