## G8.2.118 MVFR2, Media and VFP Feature Register 2

The MVFR2 characteristics are:

## Purpose

Describes the features provided by the AArch32 Advanced SIMD and floating-point implementation.

Must be interpreted with MVFR0 and MVFR1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Implemented only if the implementation includes Advanced SIMD and floating-point instructions.

AArch32 System register MVFR2 bits [31:0] are architecturally mapped to AArch64 System register MVFR2\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to MVFR2 are UNDEFINED.

## Attributes

MVFR2is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    | 4 3      |
|------|--------|----------|
| RES0 | FPMisc | SIMDMisc |

## Bits [31:8]

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

## Accessing MVFR2

Accesses to this register use the following encodings in the System register encoding space:

```
VMRS{<c>}{<q>} <Rt>, <spec_reg>
```

| reg    |
|--------|
| 0b0101 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || CPACR.cp10 == '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) ↪ → && CPTR_EL2.TFP == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.FPEN ↪ → IN {'x0'} then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x08);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = MVFR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif EL2Enabled() && ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' ↪ → && NSACR.cp10 == '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x00); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = MVFR2; elsif PSTATE.EL == EL3 then if CPACR.cp10 == '00' then UNDEFINED; else R[t] = MVFR2;
```