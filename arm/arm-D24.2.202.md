## D24.2.202 TFSRE0\_EL1, Tag Fault Status Register (EL0).

The TFSRE0\_EL1 characteristics are:

## Purpose

Holds accumulated Tag Check Faults occurring in EL0 that are not taken precisely.

## Configuration

This register is present only when FEAT\_MTE\_ASYNC is implemented. Otherwise, direct accesses to TFSRE0\_EL1 are UNDEFINED.

## Attributes

TFSRE0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32      |
|------|---------|
| RES0 |         |
| 31   | 1 0     |
| RES0 | TF1 TF0 |

## Bits [63:2]

Reserved, RES0.

## TF1, bit [1]

## When FEAT\_MTE\_ASYNC is implemented:

Tag Check Fault. Asynchronously set to 1 when a Tag Check Fault using a virtual address with bit[55] == 0b1 occurs.

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

## Accessing TFSRE0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TFSRE0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0110 | 0b001 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == '1') ↪ → then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TFSRE0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TFSRE0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TFSRE0_EL1;
```

MSR TFSRE0\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0101 | 0b0110 | 0b001 |

```
if !IsFeatureImplemented(FEAT_MTE_ASYNC) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && !(IsFeatureImplemented(FEAT_MTE2) && HCR_EL2.ATA == '1') ↪ → then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TFSRE0_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') ↪ → then UNDEFINED; elsif HaveEL(EL3) && !(IsFeatureImplemented(FEAT_MTE2) && SCR_EL3.ATA == '1') then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TFSRE0_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TFSRE0_EL1 = X[t, 64];
```