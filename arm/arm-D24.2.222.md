## D24.2.222 VSTCR\_EL2, Virtualization Secure Translation Control Register

The VSTCR\_EL2 characteristics are:

## Purpose

The control register for stage 2 of the Secure EL1&amp;0 translation regime.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SEL2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to VSTCR\_EL2 are UNDEFINED.

## Attributes

VSTCR\_EL2 is a 64-bit register.

## Field descriptions

IsProfile(PROFILE\_A)

<!-- image -->

Any of the bits in VSTCR\_EL2 are permitted to be cached in a TLB.

## Bits [63:34]

Reserved, RES0.

## SL2, bit [33]

## When FEAT\_LPA2 is implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

Starting level of the Secure stage 2 translation lookup controlled by VSTCR\_EL2.

If VTCR\_EL2.DS == 1, then VSTCR\_EL2.SL2, in combination with VSTCR\_EL2.SL0, gives encodings for the Secure stage 2 translation table walk initial lookup level.

If VTCR\_EL2.DS == 0, then VSTCR\_EL2.SL2 is RES0.

If the translation granule size is not 4KB, then this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [32]

Reserved, RES0.

## Bit [31]

Reserved, RES1.

## SA, bit [30]

Secure stage 2 translation output address space.

| SA   | Meaning                                                                           |
|------|-----------------------------------------------------------------------------------|
| 0b0  | All stage 2 translations for the Secure IPA space access the Secure PA space.     |
| 0b1  | All stage 2 translations for the Secure IPA space access the Non-secure PA space. |

When the value of VSTCR\_EL2.SW is 1, this bit behaves as 1 for all purposes other than reading back the value of the bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SW, bit [29]

Secure stage 2 translation address space.

| SW   | Meaning                                                                                      |
|------|----------------------------------------------------------------------------------------------|
| 0b0  | All stage 2 translation table walks for the Secure IPA space are to the Secure PA space.     |
| 0b1  | All stage 2 translation table walks for the Secure IPA space are to the Non-secure PA space. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [28:16]

Reserved, RES0.

## TG0, bits [15:14]

Secure stage 2 granule size for VSTTBR\_EL2.

Other values are reserved.

If FEAT\_GTG is implemented, ID\_AA64MMFR0\_EL1.{TGran4\_2, TGran16\_2, TGran64\_2} indicate which granule sizes are supported for stage 2 translation.

| TG0   | Meaning   |
|-------|-----------|
| 0b00  | 4KB.      |
| 0b01  | 64KB.     |
| 0b10  | 16KB.     |

If FEAT\_GTG is not implemented, ID\_AA64MMFR0\_EL1.{TGran4, TGran16, TGran64} indicate which granule sizes are supported.

If the value is programmed to either a reserved value, or a size that has not been implemented, then for all purposes other than read back from this register, the hardware will treat the field as if it has been programmed to an IMPLEMENTATION DEFINED choice of the sizes that has been implemented.

It is IMPLEMENTATION DEFINED whether the value read back is the value programmed or the value that corresponds to the size chosen.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [13:8]

Reserved, RES0.

## SL0, bits [7:6]

## When FEAT\_TTST is implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

Starting level of the Secure stage 2 translation lookup, controlled by VSTCR\_EL2. The meaning of this field depends on the value of VSTCR\_EL2.TG0.

| SL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | If VSTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 2. • If FEAT_LPA2 is implemented and VSTCR_EL2.SL2 is 0b0 , start at level 2. • If FEAT_LPA2 is implemented and VSTCR_EL2.SL2 is 0b1 , start at level -1. If VSTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 3.                                     |
| 0b01  | If VSTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 1. • If FEAT_LPA2 is implemented and VSTCR_EL2.SL2 is 0b0 , start at level 1. • If FEAT_LPA2 is implemented, the combination of VSTCR_EL2.SL0 == 01 and VSTCR_EL2.SL2 == 1 is reserved. If VSTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 2.       |
| 0b10  | If VSTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 0. • If FEAT_LPA2 is implemented and VSTCR_EL2.SL2 is 0b0 , start at level 0. • If FEAT_LPA2 is implemented, the combination of VSTCR_EL2.SL0 == 10 and VSTCR_EL2.SL2 == 1 is reserved. If VSTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 1.       |
| 0b11  | If VSTCR_EL2.TG0 is 0b00 (4KB granule): • If FEAT_LPA2 is not implemented, start at level 3. • If FEAT_LPA2 is implemented and VSTCR_EL2.SL2 is 0b0 , start at level 3. • If FEAT_LPA2 is implemented, the combination of VSTCR_EL2.SL0 == 11 and VSTCR_EL2.SL2 == 1 is reserved. If VSTCR_EL2.TG0 is 0b10 (16KB granule) and FEAT_LPA2 is implemented, start at level 0. |

If this field is programmed to a value that is not consistent with the programming of VSTCR\_EL2.T0SZ, then a stage 2 level 0 Translation fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_TTST is not implemented and (FEAT\_D128 is not implemented or VTCR\_EL2.D128 == '0'):

Starting level of the Secure stage 2 translation lookup, controlled by VSTCR\_EL2. The meaning of this field depends on the value of VSTCR\_EL2.TG0.

| SL0   | Meaning                                                                                                                                     |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | If VSTCR_EL2.TG0 is 0b00 (4KB granule), start at level 2. If VSTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 3. |
| 0b01  | If VSTCR_EL2.TG0 is 0b00 (4KB granule), start at level 1. If VSTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 2. |
| 0b10  | If VSTCR_EL2.TG0 is 0b00 (4KB granule), start at level 0. If VSTCR_EL2.TG0 is 0b10 (16KB granule) or 0b01 (64KB granule), start at level 1. |

All other values are reserved. If this field is programmed to a reserved value, or to a value that is not consistent with the programming of VSTCR\_EL2.T0SZ, then a stage 2 level 0 Translation fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## T0SZ, bits [5:0]

The size offset of the memory region addressed by VSTTBR\_EL2. The region size is 2 (64-T0SZ) bytes.

The maximum and minimum possible values for this field depend on the level of translation table and the memory translation granule size, as described in the AArch64 Virtual Memory System Architecture chapter.

If this field is programmed to a value that is not consistent with the programming of SL0, then a stage 2 level 0 Translation fault is generated.

Note

For the 4KB translation granule, if FEAT\_LPA2 is implemented and this field is less than 16, the translation table walk begins with a level -1 initial lookup.

For the 16KB translation granule, if FEAT\_LPA2 is implemented and this field is less than 17, the translation table walk begins with a level 0 initial lookup.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VSTCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VSTCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0110 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x048]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else X[t, 64] = VSTCR_EL2; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = VSTCR_EL2;
```

MSR VSTCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0110 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x048] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; else VSTCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else VSTCR_EL2 = X[t, 64];
```

```
then
```