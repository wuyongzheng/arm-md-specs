## D24.2.200 TFSR\_EL2, Tag Fault Status Register (EL2)

The TFSR\_EL2 characteristics are:

## Purpose

Holds accumulated Tag Check Faults occurring in EL2 that are not taken precisely.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_MTE\_ASYNC is implemented. Otherwise, direct accesses to TFSR\_EL2 are UNDEFINED.

## Attributes

TFSR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32      |
|------|---------|
| RES0 |         |
| 31   | 2 1 0   |
| RES0 | TF1 TF0 |

## Bits [63:2]

Reserved, RES0.

## TF1, bit [1]

## When FEAT\_MTE\_ASYNC is implemented:

Tag Check Fault. Asynchronously set to 1 when a Tag Check Fault using a virtual address with bit[55] == 0b1 occurs.

When the Effective value of HCR\_EL2.E2H is not 1, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TF0, bit [0]

## When FEAT\_MTE\_ASYNC is implemented:

Tag Check Fault. Asynchronously set to 1 when a Tag Check Fault using a virtual address with bit[55] == 0b0 occurs.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TFSR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name TFSR\_EL2 or TFSR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TFSR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0101 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == ↪ → '1') then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == ↪ → '1') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TFSR_EL1; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TFSR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TFSR_EL2;
```

MSR TFSR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0101 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == ↪ → '1') then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == ↪ → '1') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TFSR_EL1 = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TFSR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TFSR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, TFSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == '1') ↪ → then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x190]; else X[t, 64] = TFSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TFSR_EL2; else X[t, 64] = TFSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TFSR_EL1;
```

MSR TFSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0110 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == '1') ↪ → then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x190] = X[t, 64]; else TFSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TFSR_EL2 = X[t, 64]; else
```

```
TFSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TFSR_EL1 = X[t, 64];
```