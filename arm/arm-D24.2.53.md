## D24.2.53 GCR\_EL1, Tag Control Register.

The GCR\_EL1 characteristics are:

## Purpose

Tag Control Register.

## Configuration

This register is present only when FEAT\_MTE2 is implemented. Otherwise, direct accesses to GCR\_EL1 are UNDEFINED.

## Attributes

GCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:17]

Reserved, RES0.

## RRND, bit [16]

Controls generation of tag values by the IRG instruction.

| RRND   | Meaning                                                                                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | IRG generates a tag value as defined by RandomTag() and ChooseNonExcludedTag(). This mode does not provide strong guarantees for randomness and should only be used for debugging purposes. |
| 0b1    | IRG generates an implementation-specific tag value with a distribution of tag values no worse than generated with GCR_EL1.RRND == 0.                                                        |

Note

Arm recommends that IMPLEMENTATION DEFINED algorithms minimize the risk of a bias by selecting tags from a uniform distribution.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Exclude, bits [15:0]

Allocation Tag values excluded from selection by ChooseNonExcludedTag().

If all bits of GCR\_EL1.Exclude are 1, then the Allocation Tag value 0 will be used.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing GCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b110 |

```
if !IsFeatureImplemented(FEAT_MTE2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == '1') ↪ → then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GCR_EL1;
```

MSR GCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b110 |

```
if !IsFeatureImplemented(FEAT_MTE2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED;
```

```
elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == '1') ↪ → then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then GCR_EL1 = X[t, 64];
```