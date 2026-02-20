## D24.2.156 REVIDR\_EL1, Revision ID Register

The REVIDR\_EL1 characteristics are:

## Purpose

Provides implementation-specific minor revision information.

## Configuration

If REVIDR\_EL1 has the same value as MIDR\_EL1, then its contents have no significance.

AArch64 System register REVIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register REVIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to REVIDR\_EL1 are UNDEFINED.

## Attributes

REVIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED |                        |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

## Accessing REVIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, REVIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0000 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.REVIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = REVIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = REVIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = REVIDR_EL1;
```