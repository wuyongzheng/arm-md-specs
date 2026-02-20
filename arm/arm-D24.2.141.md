## D24.2.141 MVFR2\_EL1, AArch32 Media and VFP Feature Register 2

The MVFR2\_EL1 characteristics are:

## Purpose

Describes the features provided by the AArch32 Advanced SIMD and floating-point implementation.

Must be interpreted with MVFR0\_EL1 and MVFR1\_EL1.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

In an implementation where at least one Exception level supports execution in AArch32 state, but there is no support for Advanced SIMD and floating-point operation, this register is RAZ.

AArch64 System register MVFR2\_EL1 bits [31:0] are architecturally mapped to AArch32 System register MVFR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MVFR2\_EL1 are UNDEFINED.

## Attributes

MVFR2\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## FPMisc, bits [7:4]

Indicates whether the floating-point implementation provides support for miscellaneous VFP features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FPMisc   | Meaning                                                                            |
|----------|------------------------------------------------------------------------------------|
| 0b0000   | Not implemented, or no support for miscellaneous features.                         |
| 0b0001   | Support for Floating-point selection.                                              |
| 0b0010   | As 0b0001 , and Floating-point Conversion to Integer with Directed Rounding modes. |
| 0b0011   | As 0b0010 , and Floating-point Round to Integer Floating-point.                    |
| 0b0100   | As 0b0011 , and Floating-point MaxNum and MinNum.                                  |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0100 .

Access to this field is RO.

## SIMDMisc, bits [3:0]

Indicates whether the Advanced SIMD implementation provides support for miscellaneous Advanced SIMD features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIMDMisc   | Meaning                                                            |
|------------|--------------------------------------------------------------------|
| 0b0000     | Not implemented, or no support for miscellaneous features.         |
| 0b0001     | Floating-point Conversion to Integer with Directed Rounding modes. |
| 0b0010     | As 0b0001 , and Floating-point Round to Integer Floating-point.    |
| 0b0011     | As 0b0010 , and Floating-point MaxNum and MinNum.                  |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b0011 .

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing MVFR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MVFR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MVFR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MVFR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MVFR2_EL1;
```