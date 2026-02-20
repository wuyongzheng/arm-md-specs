## D24.2.1 ACCDATA\_EL1, Accelerator Data

The ACCDATA\_EL1 characteristics are:

## Purpose

Holds the lower 32 bits of the data that is stored by an ST64BV0, Single-copy atomic 64-byte EL0 store instruction.

## Configuration

This register is present only when FEAT\_LS64\_ACCDATA is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to ACCDATA\_EL1 are UNDEFINED.

## Attributes

ACCDATA\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      | 32   |
|---------|------|
| RES0    |      |
| 31      | 0    |
| ACCDATA |      |

## Bits [63:32]

Reserved, RES0.

## ACCDATA, bits [31:0]

Accelerator Data field. Holds bits[31:0] of the data that is stored by an ST64BV0 instruction.

## Accessing ACCDATA\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ACCDATA\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_LS64_ACCDATA) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ADEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nACCDATA_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.ADEn == '0' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ACCDATA_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ADEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.ADEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ACCDATA_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ACCDATA_EL1;
```

MSR ACCDATA\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_LS64_ACCDATA) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ADEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nACCDATA_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.ADEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ACCDATA_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.ADEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.ADEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ACCDATA_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ACCDATA_EL1 = X[t, 64];
```