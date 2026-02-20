## D24.2.13 AIDR\_EL1, Auxiliary ID Register

The AIDR\_EL1 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED identification information.

The value of this register must be interpreted in conjunction with the value of MIDR\_EL1.

## Configuration

AArch64 System register AIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register AIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AIDR\_EL1 are UNDEFINED.

## Attributes

AIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED |                        |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

## Accessing AIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b001 | 0b0000 | 0b0000 | 0b111 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.AIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = AIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = AIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = AIDR_EL1;
```