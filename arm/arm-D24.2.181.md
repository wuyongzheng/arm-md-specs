## D24.2.181 SCXTNUM\_EL1, EL1 Read/Write Software Context Number

The SCXTNUM\_EL1 characteristics are:

## Purpose

Provides a number that can be used to separate out different context numbers with the EL1 exception level, for the purpose of protecting against side-channels using branch prediction and similar resources.

## Configuration

This register is present only when (FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented) and FEAT\_AA64 is implemented. Otherwise, direct accesses to SCXTNUM\_EL1 are UNDEFINED.

## Attributes

SCXTNUM\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## SCXTNUM,bits [63:0]

Software Context Number. A number to identify the context within the EL1 exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SCXTNUM\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name SCXTNUM\_EL1 or SCXTNUM\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SCXTNUM_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif EffectiveHCR_EL2_NVx() == '011' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && HCR_EL2.EnSCXT == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.SCXTNUM_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x188]; else X[t, 64] = SCXTNUM_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = SCXTNUM_EL2; else X[t, 64] = SCXTNUM_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SCXTNUM_EL1;
```

MSR SCXTNUM\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif EffectiveHCR_EL2_NVx() == '011' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && HCR_EL2.EnSCXT == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.SCXTNUM_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x188] = X[t, 64]; else SCXTNUM_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then SCXTNUM_EL2 = X[t, 64]; else SCXTNUM_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SCXTNUM_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SCXTNUM\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1101 | 0b0000 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x188]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCXTNUM_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = SCXTNUM_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR SCXTNUM\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1101 | 0b0000 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x188] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SCXTNUM_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then SCXTNUM_EL1 = X[t, 64]; else UNDEFINED;
```