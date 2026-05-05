## C5.5.86 TLBIP IPAS2E1, TLBIP IPAS2E1NXS, TLB Invalidate Pair by Intermediate Physical Address, Stage 2, EL1

The TLBIP IPAS2E1, TLBIP IPAS2E1NXS characteristics are:

## Purpose

If EL2 is implemented and enabled in the current Security state, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 2 only translation table entry, from any level of the translation table walk.
- A64-bit stage 2 only translation table entry, from any level of the translation table walk, if TTL[3:2] is 0b00 .
- If FEAT\_RME is implemented, one of the following applies:
- SCR\_EL3.{NSE, NS} is {0, 0} and the entry would be required to translate the specified IPA using the Secure EL1&amp;0 translation regime.
- SCR\_EL3.{NSE, NS} is {0, 1} and the entry would be required to translate the specified IPA using the Non-secure EL1&amp;0 translation regime.
- SCR\_EL3.{NSE, NS} is {1, 1} and the entry would be required to translate the specified IPA using the Realm EL1&amp;0 translation regime.
- If FEAT\_RME is not implemented, one of the following applies:
- SCR\_EL3.NS is 0 and the entry would be required to translate the specified IPA using the Secure EL1&amp;0 translation regime.
- SCR\_EL3.NS is 1 and the entry would be required to translate the specified IPA using the Non-secure EL1&amp;0 translation regime.
- The entry would be used with the current VMID.

The invalidation is not required to apply to caching structures that combine stage 1 and stage 2 translation table entries.

The invalidation applies to the PE that executes this System instruction.

For more information about the architectural requirements for this System instruction, see 'Invalidating TLB entries from stage 2 translations'.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP IPAS2E1, TLBIP IPAS2E1NXS are UNDEFINED.

## Attributes

TLBIP IPAS2E1, TLBIP IPAS2E1NXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

| 127   | 108 107   | 108 107    | 108 107    | 96   |
|-------|-----------|------------|------------|------|
|       | RES0      |            | IPA[55:12] |      |
| 95    |           |            |            | 64   |
|       |           | IPA[55:12] |            |      |
| 63 62 |           | 44         |            | 32   |
| NS    | RES0      | TTL        | RES0       |      |
| 31    |           |            |            | 0    |
| RES0  | RES0      | RES0       | RES0       | RES0 |

## Bits [127:108]

Reserved, RES0.

## IPA[55:12], bits [107:64]

Bits[55:12] of the intermediate physical address to match.

## NS, bit [63]

## When FEAT\_RME is implemented:

When the instruction is executed and SCR\_EL3.{NSE, NS} == {0, 0}, NS selects the IPA space.

| NS   | Meaning                             |
|------|-------------------------------------|
| 0b0  | IPA is in the Secure IPA space.     |
| 0b1  | IPA is in the Non-secure IPA space. |

When the instruction is executed and SCR\_EL3.{NSE, NS} == {1, 1}, this field is RES0, and the instruction applies only to the Realm IPA space.

When the instruction is executed and SCR\_EL3.{NSE, NS} == {0, 1}, this field is RES0, and the instruction applies only to the Non-secure IPA space.

## When FEAT\_SEL2 is implemented and FEAT\_RME is not implemented:

Not Secure. Specifies the IPA space.

| NS   | Meaning                             |
|------|-------------------------------------|
| 0b0  | IPA is in the Secure IPA space.     |
| 0b1  | IPA is in the Non-secure IPA space. |

When the instruction is executed in Non-secure state, this field is RES0, and the instruction applies only to the Non-secure IPA space.

When FEAT\_SEL2 is not implemented, or if EL2 is disabled in the current Security state, this field is RES0.

## Otherwise:

Reserved, RES0.

Bits [62:48]

Reserved, RES0.

## TTL, bits [47:44]

## When FEAT\_TTL is implemented:

Translation Table Level. Indicates the level of the translation table walk that holds the leaf entry for the address being invalidated.

| TTL    | Meaning                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00xx | No information supplied as to the translation table level. Hardware must assume that the entry can be from any level. In this case, TTL<1:0> is RES0.                                                     |
| 0b01xx | The entry comes from a 4KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Level 0. 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3.                                  |
| 0b10xx | The entry comes from a 16KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |
| 0b11xx | The entry comes from a 64KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

If an incorrect value of the TTL field is specified for the entry being invalidated by the instruction, then no entries are required by the architecture to be invalidated from the TLB.

## Otherwise:

Reserved, RES0.

## Bits [43:0]

Reserved, RES0.

## Executing TLBIP IPAS2E1, TLBIP IPAS2E1NXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBIP IPAS2E1{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1000 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x14); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch64.TLBIP_IPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Any, ↪ → TLBI_AllAttr, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then return; else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_IPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Any, TLBI_AllAttr, X[t, t2, 128]);
```

TLBIP IPAS2E1NXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x14); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch64.TLBIP_IPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Any, ↪ → TLBI_ExcludeXS, X[t, t2, 128]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then return; else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBIP_IPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Any, TLBI_ExcludeXS, X[t, t2, 128]);
```
