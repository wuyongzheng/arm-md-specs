## C5.5.138 TLBIP VALE1IS, TLBIP VALE1ISNXS, TLB Invalidate Pair by VA, Last level, EL1, Inner Shareable

The TLBIP VALE1IS, TLBIP VALE1ISNXS characteristics are:

## Purpose

Invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 1 translation table entry.
- A64-bit stage 1 translation table entry, if TTL[3:2] is 0b00 .
- The entry would be used to translate the specified V A, and one of the following applies:
- The entry is a global entry from the final level of lookup.
- The entry is a non-global entry from the final level of lookup that matches the specified ASID.
- When EL2 is implemented and enabled in the current Security state:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the entry would be used with the current VMIDand would be required to translate the specified V A using the EL1&amp;0 translation regime for the Security state.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the entry would be required to translate the specified V A using the EL2&amp;0 translation regime for the Security state.
- When EL2 is not implemented or is disabled in the current Security state, the entry would be required to translate the specified V A using the EL1&amp;0 translation regime for the Security state.

The Security state is indicated by the value of SCR\_EL3.NS if FEAT\_RME is not implemented, or SCR\_EL3.{NSE, NS} if FEAT\_RME is implemented.

The invalidation applies to all PEs in the same Inner Shareable shareability domain as the PE that executes this System instruction.

Note

From Armv8.4, when a TLB maintenance instruction is generated to the Secure EL1&amp;0 translation regime and is defined to pass a VMID argument, or would be defined to pass a VMID argument if SCR\_EL3.EEL2==1, then:

- APEwith SCR\_EL3.EEL2==1 is not architecturally required to invalidate any entries in the Secure EL1&amp;0 translation of a PE in the same required shareability domain with SCR\_EL3.EEL2==0.
- APEwith SCR\_EL3.EEL2==0 is not architecturally required to invalidate any entries in the Secure EL1&amp;0 translation of a PE in the same required shareability domain with SCR\_EL3.EEL2==1.
- APEisarchitecturally required to invalidate all relevant entries in the Secure EL1&amp;0 translation of a System MMUinthe same required shareability domain with a VMID of 0.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP V ALE1IS, TLBIP VALE1ISNXS are UNDEFINED.

## Attributes

TLBIP VALE1IS, TLBIP VALE1ISNXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

| 127   | 108 107   | 108 107   | 108 107   | 96   |
|-------|-----------|-----------|-----------|------|
| RES0  |           |           | VA[55:12] |      |
| 95    |           |           |           | 64   |
|       |           | VA[55:12] |           |      |
| 63    |           | 48 47 44  |           | 32   |
| ASID  |           | TTL       | RES0      |      |
| 31    |           |           |           | 0    |
|       |           | RES0      |           |      |

## Bits [127:108]

Reserved, RES0.

## VA[55:12], bits [107:64]

Bits[55:12] of the virtual address to match. Any appropriate TLB entries that match the ASID value (if appropriate) and V A will be affected by this System instruction.

The treatment of the low-order bits of this field depends on the translation granule size, as follows:

- Where a 4KB translation granule is being used, all bits are valid and used for the invalidation.
- Where a 16KB translation granule is being used, bits [1:0] of this field are RES0 and ignored when the instruction is executed, because V A[13:12] have no effect on the operation of the instruction.
- Where a 64KB translation granule is being used, bits [3:0] of this field are RES0 and ignored when the instruction is executed, because V A[15:12] have no effect on the operation of the instruction.

## ASID, bits [63:48]

ASID value to match. Any TLB entries that match the ASID value and VA value will be affected by this System instruction.

Global TLB entries that match the V A value will be affected by this System instruction, regardless of the value of the ASID field.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being invalidated only uses 8 bits.

## TTL, bits [47:44]

## When FEAT\_TTL is implemented:

Translation Table Level. Indicates the level of the translation table walk that holds the leaf entry for the address being invalidated.

| TTL    | Meaning                                                                                                                                               |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00xx | No information supplied as to the translation table level. Hardware must assume that the entry can be from any level. In this case, TTL<1:0> is RES0. |

| TTL    | Meaning                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b01xx | The entry comes from a 4KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Level 0. 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3.                                  |
| 0b10xx | The entry comes from a 16KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |
| 0b11xx | The entry comes from a 64KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

If an incorrect value of the TTL field is specified for the entry being invalidated by the instruction, then no entries are required by the architecture to be invalidated from the TLB.

## Otherwise:

Reserved, RES0.

## Bits [43:0]

Reserved, RES0.

## Executing TLBIP VALE1IS, TLBIP VALE1ISNXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
TLBIP VALE1IS{, <Xt>, <Xt2>}
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b1000 | 0b0011 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TTLB == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && HCR_EL2.TTLBIS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.TLBIVALE1IS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then
```

```
AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) then AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, t2, 128]); else AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if ELIsInHost(EL0) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, ↪ → TLBILevel_Last, TLBI_AllAttr, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, t2, 128]);
```

TLBIP VALE1ISNXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b1001 | 0b0011 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TTLB == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && HCR_EL2.TTLBIS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → IsFeatureImplemented(FEAT_HCX) && (!IsHCRXEL2Enabled() || HCRX_EL2.FGTnXS == '0') && ↪ → HFGITR_EL2.TLBIVALE1IS == '1' then AArch64.SystemAccessTrap(EL2, 0x14); else AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) then AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if ELIsInHost(EL0) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return;
```

```
else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_ISH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_VA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]);
```
