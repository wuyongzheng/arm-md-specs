## D24.2.83 ID\_AA64FPFR0\_EL1, AArch64 Floating-point Feature Register 0

The ID\_AA64FPFR0\_EL1 characteristics are:

## Purpose

Provides information about floating-point formats and instructions implemented in AArch64 state.

The fields in this register do not follow the standard ID scheme. See Alternative ID scheme used for ID\_AA64SMFR0\_EL1 and ID\_AA64FPFR0\_EL1.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64FPFR0\_EL1 are UNDEFINED.

## Attributes

ID\_AA64FPFR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## F8CVT, bit [31]

Indicates support for the following instructions:

- The Advanced SIMD floating-point scaling instruction FSCALE .
- The Advanced SIMD FP8 convert instructions BF1CVTL , BF1CVTL2 , BF2CVTL , BF2CVTL2 , F1CVTL , F1CVTL2 , F2CVTL , F2CVTL2 , FCVTN , and FCVTN2 .
- When FEAT\_SVE2 or FEAT\_SME2 is implemented, the SVE2 FP8 convert instructions BF1CVT , BF1CVTLT , BF2CVT , BF2CVTLT , F1CVT , F1CVTLT , F2CVT , F2CVTLT , BFCVTN , FCVTN , FCVTNB , and FCVTNT .
- When FEAT\_SME2 is implemented, the SME2 multi-vector floating-point scaling instruction FSCALE and the SME2 FP8 convert instructions BF1CVT , BF1CVTL , BF2CVT , BF2CVTL , F1CVT , F1CVTL , F2CVT , F2CVTL , BFCVT , FCVT , and FCVTN .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8CVT   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | The specified instructions are not implemented. |
| 0b1     | The specified instructions are implemented.     |

FEAT\_FP8 implements the functionality identified by the value 1.

Access to this field is RO.

## F8FMA, bit [30]

Indicates support for the following instructions:

- The Advanced SIMD FP8 to single-precision and half-precision multiply-accumulate instructions FMLALB , FMLALT , FMLALLBB , FMLALLBT , FMLALLTB , and FMLALLTT .
- When FEAT\_SVE2 is implemented and the PE is not in Streaming SVE mode, the SVE2 FP8 to single-precision and half-precision multiply-accumulate instructions FMLALB , FMLALT , FMLALLBB , FMLALLBT , FMLALLTB , and FMLALLTT .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8FMA   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | The specified instructions are not implemented. |
| 0b1     | The specified instructions are implemented.     |

FEAT\_FP8FMA implements the functionality identified by the value 1.

Access to this field is RO.

## F8DP4, bit [29]

Indicates support for the following instructions:

- Advanced SIMD FP8 to single-precision 4-way dot product FDOT (4-way) instructions.
- When FEAT\_SVE2 is implemented and the PE is not in Streaming SVE mode, SVE FP8 to single-precision 4-way dot product FDOT (4-way) instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8DP4   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this feature. |
| 0b1     | The specified instructions are implemented.                     |

Note

Other features may implement some of the specified instructions.

All other values are reserved.

FEAT\_FP8DOT4 implements the functionality identified by the value 1.

Access to this field is RO.

## F8DP2, bit [28]

Indicates support for the following instructions:

- Advanced SIMD FP8 to half-precision 2-way dot product FDOT (2-way) instructions.
- When FEAT\_SVE2 is implemented and the PE is not in Streaming SVE mode, SVE FP8 to half-precision 2-way dot product FDOT (2-way) instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8DP2   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this feature. |
| 0b1     | The specified instructions are implemented.                     |

Note

Other features may implement some of the specified instructions.

FEAT\_FP8DOT2 implements the functionality identified by the value 1.

Access to this field is RO.

## F8MM8, bit [27]

Indicates support for the following instructions:

- Advanced SIMD FP8 to single-precision matrix multiply FMMLA (8-way, FP8 to FP32) instruction.
- If FEAT\_SVE2 is implemented, SVE FP8 to single-precision matrix multiply FMMLA (widening, FP8 to FP32) instruction is implemented when the PE is not in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8MM8   | Meaning                                                                                                         |
|---------|-----------------------------------------------------------------------------------------------------------------|
| 0b0     | Advanced SIMD and SVE FP8 to single-precision matrix multiply instructions are not implemented by this feature. |
| 0b1     | The specified Advanced SIMD and SVE FP8 to single-precision matrix multiply instructions are implemented.       |

FEAT\_F8F32MM implements the functionality identified by the value 0b0001

Access to this field is RO.

## F8MM4, bit [26]

Indicates support for the following instructions:

- Advanced SIMD FP8 to half-precision matrix multiply FMMLA (4-way, FP8 to FP16) instruction.
- If FEAT\_SVE2 is implemented, SVE FP8 to half-precision matrix multiply FMMLA (widening, FP8 to FP16) instruction is implemented when the PE is not in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8MM4   | Meaning                                                                                                       |
|---------|---------------------------------------------------------------------------------------------------------------|
| 0b0     | Advanced SIMD and SVE FP8 to half-precision matrix multiply instructions are not implemented by this feature. |
| 0b1     | The specified Advanced SIMD and SVE FP8 to half-precision matrix multiply instructions are implemented.       |

FEAT\_F8F16MM implements the functionality identified by the value 0b0001

Access to this field is RO.

## Bits [25:8]

Reserved, RES0.

## Bits [7:2]

Reserved for data formats 2 to 7.

Reserved, RAZ.

## F8E4M3, bit [1]

Indicates support for OFP8 E4M3 format and behavior for FP8 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8E4M3   | Meaning                            |
|----------|------------------------------------|
| 0b0      | OFP8 E4M3 format is not supported. |
| 0b1      | OFP8 E4M3 format is supported.     |

If FEAT\_FP8 is implemented, the only permitted value is 1.

Otherwise, the only permitted value is 0.

For more information on OFP8 formats, see the Open Compute Project, OCP 8-bit Floating Point Specification (OFP8).

Access to this field is RO.

## F8E5M2, bit [0]

Indicates support for OFP8 E5M2 format and behavior for FP8 instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8E5M2   | Meaning                            |
|----------|------------------------------------|
| 0b0      | OFP8 E5M2 format is not supported. |
| 0b1      | OFP8 E5M2 format is supported.     |

If FEAT\_FP8 is implemented, the only permitted value is 1.

Otherwise, the only permitted value is 0.

For more information on OFP8 formats, see the Open Compute Project, OCP 8-bit Floating Point Specification (OFP8).

Access to this field is RO.

## Accessing ID\_AA64FPFR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_AA64FPFR0_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0100 | 0b111 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64FPFR0_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64FPFR0_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64FPFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64FPFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64FPFR0_EL1;
```