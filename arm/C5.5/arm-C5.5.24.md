## C5.5.24 TLBI RIPAS2LE1, TLBI RIPAS2LE1NXS, TLB Range Invalidate by Intermediate Physical Address, Stage 2,

## Last level, EL1

The TLBI RIPAS2LE1, TLBI RIPAS2LE1NXS characteristics are:

## Purpose

If EL2 is implemented and enabled in the current Security state, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A64-bit stage 2 only translation table entry, from the leaf level of the translation table walk, indicated by the TTL hint.
- If FEAT\_D128 is implemented, a 128-bit stage 2 only translation table entry, from the leaf level of the translation table walk, if TTL is 0b00 .
- If FEAT\_RME is implemented, one of the following applies:
- SCR\_EL3.{NSE, NS} is {0, 0} and the entry would be required to translate any IPA in the specified address range using the Secure EL1&amp;0 translation regime.
- SCR\_EL3.{NSE, NS} is {0, 1} and the entry would be required to translate any IPA in the specified address range using the Non-secure EL1&amp;0 translation regime.
- SCR\_EL3.{NSE, NS} is {1, 1} and the entry would be required to translate any IPA in the specified address range using the Realm EL1&amp;0 translation regime.
- If FEAT\_RME is not implemented, one of the following applies:
- SCR\_EL3.NS is 0 and the entry would be required to translate any IPA in the specified address range using the Secure EL1&amp;0 translation regime.
- SCR\_EL3.NS is 1 and the entry would be required to translate any IPA in the specified address range using the Non-secure EL1&amp;0 translation regime.
- The entry would be used with the current VMID.
- The entry is within the address range determined by the formula [BaseADDR &lt;= VA &lt; BaseADDR + ((NUM +1)*2 (5*SCALE +1) * Translation\_Granule\_Size)].

The invalidation is not required to apply to caching structures that combine stage 1 and stage 2 translation table entries.

The invalidation only applies to the PE that executes this System instruction.

For 64-bit translation table entry, the range of addresses invalidated is UNPREDICTABLE when:

- For the 4K translation granule:
- If TTL==01 and BaseADDR[29:12] is not equal to 000000000000000000.
- If TTL==10 and BaseADDR[20:12] is not equal to 000000000.
- For the 16K translation granule:
- If TTL==10 and BaseADDR[24:14] is not equal to 00000000000.
- For the 64K translation granule:
- If TTL==01 and BaseADDR[41:16] is not equal to 00000000000000000000000000.
- If TTL==10 and BaseADDR[28:16] is not equal to 0000000000000.

For more information about the architectural requirements for this System instruction, see 'Invalidating TLB entries from stage 2 translations'.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_TLBIRANGE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBI RIPAS2LE1, TLBI RIPAS2LE1NXS are UNDEFINED.

## Attributes

TLBI RIPAS2LE1, TLBI RIPAS2LE1NXS is a 64-bit System instruction.

## Field descriptions

<!-- image -->

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

## Bits [62:48]

Reserved, RES0.

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

| TTL   | Meaning                                                                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | The entries in the range can be using any level for the translation table entries.                                                                                            |
| 0b01  | The TTL hint indicates level 1. If FEAT_LPA2 is not implemented, when using a 16KB translation granule, this value is reserved and hardware should treat this field as 0b00 . |
| 0b10  | The TTL hint indicates level 2.                                                                                                                                               |
| 0b11  | The TTL hint indicates level 3.                                                                                                                                               |

## BaseADDR, bits [36:0]

When (IsFeatureImplemented(FEAT\_LPA2) &amp;&amp; (VTCR\_EL2.DS == '1')) || (IsFeatureImplemented(FEAT\_D128) &amp;&amp; (VTCR\_EL2.D128 == '1')):

The starting address for the range of the maintenance instructions. This field is BaseADDR[52:16] for all translation granules.

When using a 4KB translation granule, BaseADDR[15:12] is treated as 0b0000 .

When using a 16KB translation granule, BaseADDR[15:14] is treated as 0b00 .

## Otherwise:

The starting address for the range of the maintenance instruction.

When using a 4KB translation granule, this field is BaseADDR[48:12].

When using a 16KB translation granule, this field is BaseADDR[50:14].

When using a 64KB translation granule, this field is BaseADDR[52:16].

## Executing TLBI RIPAS2LE1, TLBI RIPAS2LE1NXS

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBI RIPAS2LE1{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1000 | 0b0100 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_TLBIRANGE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch64.TLBI_RIPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_AllAttr, X[t, 64]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then return; else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBI_RIPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_AllAttr, X[t, 64]);
```

When FEAT\_XS is implemented TLBI RIPAS2LE1NXS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1001 | 0b0100 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_TLBIRANGE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

```
AArch64.TLBI_RIPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, 64]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then return; else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBI_RIPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_NSH, ↪ → TLBILevel_Last, TLBI_ExcludeXS, X[t, 64]);
```
