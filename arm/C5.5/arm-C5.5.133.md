## C5.5.133 TLBIP VAE2OS, TLBIP VAE2OSNXS, TLB Invalidate Pair by VA, EL2, Outer Shareable

The TLBIP VAE2OS, TLBIP VAE2OSNXS characteristics are:

## Purpose

When EL2 is implemented and enabled in the current Security state, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 1 translation table entry.
- A64-bit stage 1 translation table entry, if TTL[3:2] is 0b00 .
- The entry would be required to translate the specified V A using the EL2 or EL2&amp;0 translation regime, as determined by the Effective value of HCR\_EL2.E2H, for the Security state.
- If the Effective value of HCR\_EL2.E2H is not 1, the entry is from any level of the translation table walk.
- If the Effective value of HCR\_EL2.E2H is 1, one of the following applies:
- The entry is from a level of the translation table walk above the final level and matches the specified ASID.
- The entry is a global entry from the final level of the translation table walk.
- The entry is a non-global entry from the final level of the translation table walk that matches the specified ASID.

The Security state is indicated by the value of SCR\_EL3.NS if FEAT\_RME is not implemented, or SCR\_EL3.{NSE, NS} if FEAT\_RME is implemented.

The invalidation applies to all PEs in the same Outer Shareable shareability domain as the PE that executes this System instruction.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP V AE2OS, TLBIP VAE2OSNXS are UNDEFINED.

## Attributes

TLBIP VAE2OS, TLBIP VAE2OSNXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [127:108]

Reserved, RES0.

## VA[55:12], bits [107:64]

Bits[55:12] of the virtual address to match. Any appropriate TLB entries that match the ASID value (if appropriate) and V A will be affected by this System instruction.

The treatment of the low-order bits of this field depends on the translation granule size, as follows:

- Where a 4KB translation granule is being used, all bits are valid and used for the invalidation.
- Where a 16KB translation granule is being used, bits [1:0] of this field are RES0 and ignored when the instruction is executed, because V A[13:12] have no effect on the operation of the instruction.
- Where a 64KB translation granule is being used, bits [3:0] of this field are RES0 and ignored when the instruction is executed, because V A[15:12] have no effect on the operation of the instruction.

## ASID, bits [63:48]

## When ELIsInHost(EL2):

ASID value to match. Any TLB entries that match the ASID value and VA value will be affected by this System instruction.

Global TLB entries that match the V A value will be affected by this System instruction, regardless of the value of the ASID field.

If the implementation supports 16 bits of ASID, then the upper 8 bits of the ASID must be written to 0 by software when the context being invalidated only uses 8 bits.

## Otherwise:

Reserved, RES0.

## TTL, bits [47:44]

## When FEAT\_TTL is implemented:

Translation Table Level. Indicates the level of the translation table walk that holds the leaf entry for the address being invalidated.

| TTL    | Meaning                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00xx | No information supplied as to the translation table level. Hardware must assume that the entry can be from any level. In this case, TTL<1:0> is RES0.                                                     |
| 0b01xx | The entry comes from a 4KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Level 0. 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3.                                  |
| 0b10xx | The entry comes from a 16KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

| TTL    | Meaning                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b11xx | The entry comes from a 64KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

If an incorrect value of the TTL field is specified for the entry being invalidated by the instruction, then no entries are required by the architecture to be invalidated from the TLB.

## Otherwise:

Reserved, RES0.

## Bits [43:0]

Reserved, RES0.

## Executing TLBIP VAE2OS, TLBIP VAE2OSNXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
TLBIP VAE2OS{, <Xt>, <Xt2>}
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x14); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_OSH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]); else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL2, VMID_NONE, Broadcast_OSH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then UNDEFINED; elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_OSH, ↪ → TLBILevel_Any, TLBI_AllAttr, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else
```

AArch64.TLBIP\_VA(SecurityStateAtEL(EL2), Regime\_EL2, VMID\_NONE, Broadcast\_OSH, ↪ → TLBILevel\_Any, TLBI\_AllAttr, X[t, t2, 128]);

TLBIP VAE2OSNXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x14); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_OSH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL2, VMID_NONE, Broadcast_OSH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then UNDEFINED; elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL20, VMID_NONE, Broadcast_OSH, ↪ → TLBILevel_Any, TLBI_ExcludeXS, X[t, t2, 128]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBIP_VA(SecurityStateAtEL(EL2), Regime_EL2, VMID_NONE, Broadcast_OSH, ↪ → TLBILevel_Any, TLBI_ExcludeXS, X[t, t2, 128]);
```
