## C5.5.125 TLBIP VAALE1, TLBIP VAALE1NXS, TLB Invalidate Pair by VA, All ASID, Last level, EL1

The TLBIP VAALE1, TLBIP VAALE1NXS characteristics are:

## Purpose

Invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 1 translation table entry, from the final level of the translation table walk.
- A64-bit stage 1 translation table entry, from the final level of the translation table walk, if TTL[3:2] is 0b00 .
- When EL2 is implemented and enabled in the current Security state:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the entry would be used with the current VMIDand would be required to translate the specified V A using the EL1&amp;0 translation regime for the Security state.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the entry would be required to translate the specified V A using the EL2&amp;0 translation regime for the Security state.
- When EL2 is not implemented or is disabled in the current Security state, the entry would be required to translate the specified V A using the EL1&amp;0 translation regime for the Security state.

The Security state is indicated by the value of SCR\_EL3.NS if FEAT\_RME is not implemented, or SCR\_EL3.{NSE, NS} if FEAT\_RME is implemented.

The invalidation applies to the PE that executes this System instruction.

Note

For the EL1&amp;0 and EL2&amp;0 translation regimes, the invalidation applies to both global entries and non-global entries with any ASID.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP V AALE1, TLBIP VAALE1NXS are UNDEFINED.

## Attributes

TLBIP VAALE1, TLBIP VAALE1NXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

| 127   | 108 107   | 108 107     | 108 107   | 96   |
|-------|-----------|-------------|-----------|------|
| RES0  |           |             | VA[55:12] |      |
| 95    |           |             |           | 64   |
| 63    |           | 48 47 44 43 | 32        |      |
| RES0  |           | TTL         | RES0      |      |
| 31    |           |             |           | 0    |
|       |           | RES0        |           |      |

## Bits [127:108]

Reserved, RES0.

## VA[55:12], bits [107:64]

Bits[55:12] of the virtual address to match. Any appropriate TLB entries that match the V A will be affected by this System instruction, regardless of the ASID.

If the TLB maintenance instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then the software must treat bits[55:32] as RES0.

The treatment of the low-order bits of this field depends on the translation granule size, as follows:

- Where a 4KB translation granule is being used, all bits are valid and used for the invalidation.
- Where a 16KB translation granule is being used, bits [1:0] of this field are RES0 and ignored when the instruction is executed, because V A[13:12] have no effect on the operation of the instruction.
- Where a 64KB translation granule is being used, bits [3:0] of this field are RES0 and ignored when the instruction is executed, because V A[15:12] have no effect on the operation of the instruction.

## Bits [63:48]

Reserved, RES0.

## TTL, bits [47:44]

## When FEAT\_TTL is implemented:

Translation Table Level. Indicates the level of the translation table walk that holds the leaf entry for the address being invalidated.

| TTL    | Meaning                                                                                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00xx | No information supplied as to the translation table level. Hardware must assume that the entry can be from any level. In this case, TTL<1:0> is RES0.                    |
| 0b01xx | The entry comes from a 4KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Level 0. 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

| TTL    | Meaning                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b10xx | The entry comes from a 16KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |
| 0b11xx | The entry comes from a 64KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

If an incorrect value of the TTL field is specified for the entry being invalidated by the instruction, then no entries are required by the architecture to be invalidated from the TLB.

## Otherwise:

Reserved, RES0.

## Bits [43:0]

Reserved, RES0.

## Executing TLBIP VAALE1, TLBIP VAALE1NXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
TLBIP VAALE1{, <Xt>, <Xt2>}
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b1000 | 0b0111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TTLB == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.TLBIVAALE1 == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && HCR_EL2.FB == '1' then if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBILevel_Last, TLBI_AllAttr, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_XS) && IsFeatureImplemented(FEAT_HCX) && IsHCRXEL2Enabled() && ↪ → HCRX_EL2.FnXS == '1' then
```

```
AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) then AArch64.TLBIP_VAA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, t2, 128]); else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if ELIsInHost(EL0) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_VAA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_AllAttr, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_AllAttr, X[t, t2, 128]);
```

TLBIP VAALE1NXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b1001 | 0b0111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TTLB == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → IsFeatureImplemented(FEAT_HCX) && (!IsHCRXEL2Enabled() || HCRX_EL2.FGTnXS == '0') && ↪ → HFGITR_EL2.TLBIVAALE1 == '1' then AArch64.SystemAccessTrap(EL2, 0x14); elsif EL2Enabled() && HCR_EL2.FB == '1' then AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ForcedISH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) then AArch64.TLBIP_VAA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if ELIsInHost(EL0) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then
```

```
return; else AArch64.TLBIP_VAA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_VAA(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, t2, 128]);
```
