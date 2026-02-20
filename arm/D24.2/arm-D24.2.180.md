## D24.2.180 SCXTNUM\_EL0, EL0 Read/Write Software Context Number

The SCXTNUM\_EL0 characteristics are:

## Purpose

Provides a number that can be used to separate out different context numbers with the EL0 exception level, for the purpose of protecting against side-channels using branch prediction and similar resources.

## Configuration

This register is present only when (FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented) and FEAT\_AA64 is implemented. Otherwise, direct accesses to SCXTNUM\_EL0 are UNDEFINED.

## Attributes

SCXTNUM\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |    |   32 |
|------|----|------|
|      | 31 |    0 |

## SCXTNUM,bits [63:0]

Software Context Number. A number to identify the context within the EL0 exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SCXTNUM\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SCXTNUM_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0000 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.TSCXT == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && HCR_EL2.EnSCXT == '0' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGRTR_EL2.SCXTNUM_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.TSCXT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCXTNUM_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.EnSCXT == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.SCXTNUM_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCXTNUM_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCXTNUM_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = SCXTNUM_EL0;
```

MSR SCXTNUM\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0000 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.TSCXT == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && HCR_EL2.EnSCXT == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGWTR_EL2.SCXTNUM_EL0 == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.TSCXT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SCXTNUM_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.EnSCXT == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.SCXTNUM_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SCXTNUM_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnSCXT == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnSCXT == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SCXTNUM_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then SCXTNUM_EL0 = X[t, 64];
```