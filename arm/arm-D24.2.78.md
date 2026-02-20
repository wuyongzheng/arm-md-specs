## D24.2.78 ID\_AA64AFR0\_EL1, AArch64 Auxiliary Feature Register 0

The ID\_AA64AFR0\_EL1 characteristics are:

## Purpose

Provides information about the IMPLEMENTATION DEFINED features of the PE in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64AFR0\_EL1 are UNDEFINED.

## Attributes

ID\_AA64AFR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

IMPLEMENTATIONDEFINED, bits [31:28]

IMPLEMENTATION DEFINED.

IMPLEMENTATIONDEFINED, bits [27:24]

IMPLEMENTATION DEFINED.

IMPLEMENTATIONDEFINED, bits [23:20]

IMPLEMENTATION DEFINED.

IMPLEMENTATIONDEFINED, bits [19:16]

IMPLEMENTATION DEFINED.

IMPLEMENTATIONDEFINED, bits [15:12]

IMPLEMENTATION DEFINED.

IMPLEMENTATIONDEFINED, bits [11:8]

IMPLEMENTATION DEFINED.

## IMPLEMENTATIONDEFINED, bits [7:4]

IMPLEMENTATION DEFINED.

## IMPLEMENTATIONDEFINED, bits [3:0]

IMPLEMENTATION DEFINED.

## Accessing ID\_AA64AFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64AFR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64AFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64AFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64AFR0_EL1;
```