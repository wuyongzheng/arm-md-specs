## D24.2.214 VBAR\_EL1, Vector Base Address Register (EL1)

The VBAR\_EL1 characteristics are:

## Purpose

Holds the vector base address for any exception that is taken to EL1.

## Configuration

AArch64 System register VBAR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register VBAR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to VBAR\_EL1 are UNDEFINED.

## Attributes

VBAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## VBA, bits [63:11]

Vector Base Address. Base address of the exception vectors for exceptions taken to EL1.

Note

If the implementation supports FEAT\_LVA3, then:

- If tagged addresses are not being used, bits [63:56] of VBAR\_EL1 must be the same or else the use of the vector address will result in a recursive exception.

## Otherwise:

If the implementation supports FEAT\_LVA, then:

- If tagged addresses are being used, bits [55:52] of VBAR\_EL1 must be the same or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:52] of VBAR\_EL1 must be the same or else the use of the vector address will result in a recursive exception.

If the implementation does not support FEAT\_LVA, then:

- If tagged addresses are being used, bits [55:48] of VBAR\_EL1 must be the same or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:48] of VBAR\_EL1 must be the same or else the use of the vector address will result in a recursive exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [10:0]

Reserved, RES0.

## Accessing VBAR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name VBAR\_EL1 or VBAR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VBAR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.VBAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x250]; else X[t, 64] = VBAR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = VBAR_EL2; else X[t, 64] = VBAR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = VBAR_EL1;
```

MSR VBAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.VBAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x250] = X[t, 64]; else VBAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then
```

```
if ELIsInHost(EL2) then VBAR_EL2 = X[t, 64]; else VBAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then VBAR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, VBAR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x250]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = VBAR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = VBAR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR VBAR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x250] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then VBAR_EL1 = X[t, 64]; else
```

UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then VBAR\_EL1 = X[t, 64]; else UNDEFINED;