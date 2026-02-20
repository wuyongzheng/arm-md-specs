## D24.2.54 GMID\_EL1, Multiple tag transfer ID Register

The GMID\_EL1 characteristics are:

## Purpose

Indicates the block size that is accessed by the LDGM and STGM System instructions.

## Configuration

This register is present only when FEAT\_MTE2 is implemented. Otherwise, direct accesses to GMID\_EL1 are UNDEFINED.

## Attributes

GMID\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:4]

Reserved, RES0.

## BS, bits [3:0]

Log2 of the block size in words. The minimum supported size is 16B (value == 2) and the maximum is 256B (value == 6).

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing GMID\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b001 | 0b0000 | 0b0000 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MTE2) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else
```

```
UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID5 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID5 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID5 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GMID_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID5 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID5 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GMID_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GMID_EL1;
```