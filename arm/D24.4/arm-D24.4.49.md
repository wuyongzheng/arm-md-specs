## D24.4.49 TRCITECR\_EL2, Instrumentation Trace Control Register (EL2)

The TRCITECR\_EL2 characteristics are:

## Purpose

Provides EL2 controls for Trace Instrumentation.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_ITE is implemented, System register access to the trace unit registers is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to TRCITECR\_EL2 are UNDEFINED.

## Attributes

TRCITECR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## E2E, bit [1]

EL2 Instrumentation Trace Enable.

| E2E   | Meaning                                      |
|-------|----------------------------------------------|
| 0b0   | Instrumentation trace prohibited at EL2.     |
| 0b1   | Instrumentation trace not prohibited at EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0HE, bit [0]

EL0 Instrumentation Trace Enable.

| E0HE   | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0    | Instrumentation trace prohibited at EL0 when HCR_EL2.TGE == 1. |

| E0HE   | Meaning                                                            |
|--------|--------------------------------------------------------------------|
| 0b1    | Instrumentation trace not prohibited at EL0 when HCR_EL2.TGE == 1. |

This field is ignored by the PE when any of the following are true:

- HCR\_EL2.TGE == 0.
- EL2 is disabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRCITECR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name TRCITECR\_EL2 or TRCITECR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCITECR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TRCITECR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TRCITECR_EL2; MSR TRCITECR_EL2, <Xt>
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TRCITECR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TRCITECR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, TRCITECR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x888]; else X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TRCITECR_EL2; else
```

```
X[t, 64] = TRCITECR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TRCITECR_EL1;
```

MSR TRCITECR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_ITE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nTRCITECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x888] = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnITE == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnITE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then TRCITECR_EL2 = X[t, 64]; else TRCITECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TRCITECR_EL1 = X[t, 64];
```
