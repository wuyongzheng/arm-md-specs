## D24.4.48 TRCITECR\_EL1, Instrumentation Trace Control Register (EL1)

The TRCITECR\_EL1 characteristics are:

## Purpose

Provides EL1 controls for Trace Instrumentation.

## Configuration

This register is present only when FEAT\_ITE is implemented, System register access to the trace unit registers is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRCITECR\_EL1 are UNDEFINED.

## Attributes

TRCITECR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32      |
|------|---------|
| RES0 |         |
| RES0 | E1E E0E |

## Bits [63:2]

Reserved, RES0.

## E1E, bit [1]

EL1 Instrumentation Trace Enable.

| E1E   | Meaning                                      |
|-------|----------------------------------------------|
| 0b0   | Instrumentation trace prohibited at EL1.     |
| 0b1   | Instrumentation trace not prohibited at EL1. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0E, bit [0]

EL0 Instrumentation Trace Enable.

| E0E   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Instrumentation trace prohibited at EL0. |

0b1

Instrumentation trace not prohibited at EL0.

This field is ignored by the PE when EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRCITECR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TRCITECR\_EL1 or TRCITECR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCITECR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x888]; else X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRCITECR_EL2; else X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TRCITECR_EL1;
```

MSR TRCITECR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x888] = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TRCITECR_EL2 = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRCITECR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TRCITECR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x888]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRCITECR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TRCITECR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TRCITECR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x888] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRCITECR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TRCITECR_EL1 = X[t, 64]; else UNDEFINED;
```
