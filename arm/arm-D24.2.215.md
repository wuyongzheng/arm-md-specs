## D24.2.215 VBAR\_EL2, Vector Base Address Register (EL2)

The VBAR\_EL2 characteristics are:

## Purpose

Holds the vector base address for any exception that is taken to EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register VBAR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HVBAR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to VBAR\_EL2 are UNDEFINED.

## Attributes

VBAR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## VBA, bits [63:11]

Vector Base Address. Base address of the exception vectors for exceptions taken to EL2.

## Note

## If FEAT\_LVA3 is implemented:

- If the Effective value of HCR\_EL2.E2H is 1:
- If tagged addresses are not being used, bits [63:56] of VBAR\_EL2 must be the same or else the use of the vector address will result in a recursive exception.
- If the Effective value of HCR\_EL2.E2H is not 1:
- If tagged addresses are not being used, bits [63:56] of VBAR\_EL2 must be 0 or else the use of the vector address will result in a recursive exception.

## Otherwise :

## If FEAT\_LVA is implemented:

- If the Effective value of HCR\_EL2.E2H is 1:
- If tagged addresses are being used, bits [55:52] of VBAR\_EL2 must be the same or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:52] of VBAR\_EL2 must be the same or else the use of the vector address will result in a recursive exception.
- If the Effective value of HCR\_EL2.E2H is not 1:
- If tagged addresses are being used, bits [55:52] of VBAR\_EL2 must be 0 or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:52] of VBAR\_EL2 must be 0 or else the use of the vector address will result in a recursive exception.

## If FEAT\_LVA is not implemented:

- If the Effective value of HCR\_EL2.E2H is 1:
- If tagged addresses are being used, bits [55:48] of VBAR\_EL2 must be the same or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:48] of VBAR\_EL2 must be the same or else the use of the vector address will result in a recursive exception.
- If the Effective value of HCR\_EL2.E2H is not 1:
- If tagged addresses are being used, bits [55:48] of VBAR\_EL2 must be 0 or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:48] of VBAR\_EL2 must be 0 or else the use of the vector address will result in a recursive exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [10:0]

Reserved, RES0.

## Accessing VBAR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name VBAR\_EL2 or VBAR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, VBAR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1100 | 0b0000 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = VBAR\_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = VBAR\_EL2;

MSR VBAR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VBAR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then VBAR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, VBAR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_FGT) &amp;&amp; (!HaveEL(EL3) || SCR\_EL3.FGTEn == '1') ↪ → &amp;&amp; HFGRTR\_EL2.VBAR\_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);

```
elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x250]; else X[t, 64] = VBAR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = VBAR_EL2; else X[t, 64] = VBAR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = VBAR_EL1;
```

When FEAT\_VHE is implemented MSR VBAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.VBAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x250] = X[t, 64]; else VBAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then VBAR_EL2 = X[t, 64]; else VBAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then VBAR_EL1 = X[t, 64];
```