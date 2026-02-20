## D24.2.96 ID\_AA64SMFR0\_EL1, SME Feature ID Register 0

The ID\_AA64SMFR0\_EL1 characteristics are:

## Purpose

Provides information about the implemented features of the AArch64 Scalable Matrix Extension.

The fields in this register do not follow the standard ID scheme. See Alternative ID scheme used for ID\_AA64SMFR0\_EL1 and ID\_AA64FPFR0\_EL1.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

## Attributes

ID\_AA64SMFR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## FA64, bit [63]

Indicates support at each Exception Level for execution of the full AArch64 Advanced SIMD and SVE instruction sets when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FA64   | Meaning                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Only those AArch64 instructions defined as being legal can be executed in streaming SVE mode.                                                        |
| 0b1    | All implemented AArch64 instructions are legal for execution in Streaming SVE mode, when enabled by SMCR_EL1.FA64, SMCR_EL2.FA64, and SMCR_EL3.FA64. |

FEAT\_SME\_FA64 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## Bits [62:61]

Reserved, RES0.

## LUTv2, bit [60]

Indicates support for the following additional variants of SME2 lookup table LUTI4 and MOVT instructions:

- A LUTI4 instruction with 8-bit result elements, two consecutively numbered source vectors, and four consecutively numbered destination vectors.
- If FEAT\_SME2p1 is implemented, a LUTI4 instruction with 8-bit result elements, two consecutively numbered source vectors, and four destination vectors with strided register numbering.
- A MOVT instruction that copies a single Z source vector to ZT0.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LUTv2   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this control. |
| 0b1     | The specified instructions are implemented.                     |

All other values are reserved.

FEAT\_SME\_LUTv2 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## SMEver, bits [59:56]

Indicates support for SME instructions when FEAT\_SME is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SMEver   | Meaning                                                 |
|----------|---------------------------------------------------------|
| 0b0000   | The mandatory SMEinstructions are implemented.          |
| 0b0001   | As 0b0000 , and adds the mandatory SME2 instructions.   |
| 0b0010   | As 0b0001 , and adds the mandatory SME2.1 instructions. |
| 0b0011   | As 0b0010 , and adds the mandatory SME2.2 instructions. |

All other values are reserved.

FEAT\_SME implements the functionality identified by the value 0b0000 .

FEAT\_SME2 implements the functionality identified by the value 0b0001 .

FEAT\_SME2p1 implements the functionality identified by the value 0b0010 .

From Armv9.4, the value 0b0001 is not permitted.

FEAT\_SME2p2 implements the functionality identified by 0b0011 .

From Armv9.6, the values 0b0000 and 0b0010 are not permitted.

Access to this field is RO.

## I16I64, bits [55:52]

Indicates support for the following SME instructions that accumulate into 64-bit integer elements in the ZA array:

- The variants of the ADDHA , ADDVA , SMOPA , SMOPS , SUMOPA , SUMOPS , UMOPA , UMOPS , USMOPA , and USMOPS instructions that accumulate into 64-bit integer tiles.

- When FEAT\_SME2 is implemented, the variants of the ADD , ADDA , SDOT , SMLALL , SMLSLL , SUB , SUBA , SVDOT , UDOT , UMLALL , UMLSLL , and UVDOT instructions that accumulate into 64-bit integer elements in ZA array vectors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I16I64   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0000   | The specified instructions are not implemented by this control. |
| 0b1111   | The specified instructions are implemented.                     |

All other values are reserved.

FEAT\_SME\_I16I64 implements the functionality identified by the value 0b1111 .

Access to this field is RO.

## Bits [51:49]

Reserved, RES0.

## F64F64, bit [48]

Indicates support for the following SME instructions that accumulate into double-precision floating-point elements in the ZA array:

- The variants of the FMOPA and FMOPS instructions that accumulate into double-precision tiles.
- When FEAT\_SME2 is implemented, the variants of the FADD , FMLA , FMLS , and FSUB instructions that accumulate into double-precision elements in ZA array vectors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F64F64   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | The specified instructions are not implemented by this control. |
| 0b1      | The specified instructions are implemented .                    |

FEAT\_SME\_F64F64 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## I16I32, bits [47:44]

## When FEAT\_SME2 is implemented:

Indicates support for SME2 SMOPA (2-way), SMOPS (2-way), UMOPA (2-way), and UMOPS (2-way) instructions that accumulate 16-bit outer products into 32-bit integer tiles.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I16I32   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0000   | The specified instructions are not implemented by this control. |
| 0b0101   | The specified instructions are implemented.                     |

| I16I32   | Meaning   |
|----------|-----------|

All other values are reserved.

If FEAT\_SME2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## B16B16, bit [43]

Indicates support for the SME ZA-targeting non-widening BFloat16 BFADD , BFMLA , BFMLS , BFMOPA , BFMOPS , and BFSUB instructions with BFloat16 operands and results.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| B16B16   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | The specified instructions are not implemented by this control. |
| 0b1      | The specified instructions are implemented.                     |

FEAT\_SME\_B16B16 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## F16F16, bit [42]

Indicates support for the following SME2 half-precision floating-point instructions:

- FMOPA and FMOPS instructions that accumulate half-precision outer-products into half-precision tiles.
- Multi-vector FADD , FMLA , FMLS , and FSUB instructions with half-precision operands and results.
- Multi-vector FCVT and FCVTL instructions that convert half-precision inputs to single-precision results.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F16F16   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | The specified instructions are not implemented by this control. |
| 0b1      | The specified instructions are implemented.                     |

FEAT\_SME\_F16F16 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## F8F16, bit [41]

Indicates support for the following SME2 instructions:

- The ZA-targeting FP8 instructions FDOT (2-way), FMLAL , FMOPA (2-way), and FVDOT that accumulate into half-precision floating-point elements.
- ZA-targeting non-widening half-precision FADD and FSUB instructions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8F16   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this control. |
| 0b1     | The specified instructions are implemented.                     |

FEAT\_SME\_F8F16 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## F8F32, bit [40]

Indicates support for the SME2 ZA-targeting FP8 FDOT (4-way), FMLALL , FMOPA (4-way), FVDOTB , and FVDOTT instructions that accumulate into single-precision floating-point elements.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F8F32   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this control. |
| 0b1     | The specified instructions are implemented.                     |

FEAT\_SME\_F8F32 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## I8I32, bits [39:36]

## When FEAT\_SME is implemented:

Indicates support for SME SMOPA , SMOPS , SUMOPA , SUMOPS , UMOPA , UMOPS , USMOPA , and USMOPS instructions that accumulate 8-bit outer products into 32-bit tiles

The value of this field is an IMPLEMENTATION DEFINED choice of:

| I8I32   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0000  | The specified instructions are not implemented by this control. |
| 0b1111  | The specified instructions are implemented.                     |

All other values are reserved.

If FEAT\_SME is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## F16F32, bit [35]

## When FEAT\_SME is implemented:

Indicates support for SME FMOPA and FMOPS instructions that accumulate half-precision floating-point outer products into single-precision floating-point tiles.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F16F32   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | The specified instructions are not implemented by this control. |
| 0b1      | The specified instructions are implemented.                     |

If FEAT\_SME is implemented, the value 0b0 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## B16F32, bit [34]

## When FEAT\_SME is implemented:

Indicates support for SME BFMOPA and BFMOPS instructions that accumulate BFloat16 outer products into single-precision floating-point tiles.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| B16F32   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | The specified instructions are not implemented by this control. |
| 0b1      | The specified instructions are implemented.                     |

If FEAT\_SME is implemented, the value 0b0 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## BI32I32, bit [33]

## When FEAT\_SME2 is implemented:

Indicates support for SME BMOPA and BMOPS instructions that accumulate thirty-two 1-bit binary outer products into 32-bit integer tiles.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BI32I32   | Meaning                                                         |
|-----------|-----------------------------------------------------------------|
| 0b0       | The specified instructions are not implemented by this control. |

0b1

The specified instructions are implemented.

If FEAT\_SME2 is implemented, the value 0b0 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## F32F32, bit [32]

## When FEAT\_SME is implemented:

Indicates support for SME FMOPA and FMOPS instructions that accumulate single-precision floating-point outer products into single-precision floating-point tiles.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F32F32   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | The specified instructions are not implemented by this control. |
| 0b1      | The specified instructions are implemented.                     |

If FEAT\_SME is implemented, the value 0b0 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Bit [31]

Reserved, RES0.

## SF8FMA, bit [30]

Indicates support for the SVE2 FP8 to single-precision and half-precision multiply-accumulate FMLALB , FMLALT , FMLALLBB , FMLALLBT , FMLALLTB , and FMLALLTT instructions when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SF8FMA   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | This control has no effect on Streaming SVE mode behavior.      |
| 0b1      | The specified instructions are supported in Streaming SVE mode. |

Note

Other features may support some of the specified instructions in Non-streaming SVE mode.

If FEAT\_SME2 and FEAT\_FP8FMA are implemented, the value 0b0 is not permitted.

FEAT\_SSVE\_FP8FMA implements the functionality identified by the value 0b1 .

Access to this field is RO.

## SF8DP4, bit [29]

Indicates support for the SVE2 FP8 to single-precision 4-way dot product FDOT (4-way) instructions when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SF8DP4   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | This control has no effect on Streaming SVE mode behavior.      |
| 0b1      | The specified instructions are supported in Streaming SVE mode. |

Note

Other features may support some of the specified instructions in Non-streaming SVE mode.

If FEAT\_SME2 and FEAT\_FP8DOT4 are implemented, the value 0b0 is not permitted.

FEAT\_SSVE\_FP8DOT4 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## SF8DP2, bit [28]

Indicates support for the SVE2 FP8 to half-precision 2-way dot product FDOT (2-way) instructions when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SF8DP2   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0      | This control has no effect on Streaming SVE mode behavior.      |
| 0b1      | The specified instructions are supported in Streaming SVE mode. |

Note

Other features may support some of the specified instructions in Non-streaming SVE mode.

If FEAT\_SME2 and FEAT\_FP8DOT2 are implemented, the value 0b0 is not permitted.

FEAT\_SSVE\_FP8DOT2 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## Bits [27:26]

Reserved, RES0.

## SBitPerm, bit [25]

Indicates support for the SVE bit permute instructions identified as implemented by ID\_AA64ZFR0\_EL1.BitPerm, when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SBitPerm   | Meaning                                                                          |
|------------|----------------------------------------------------------------------------------|
| 0b0        | This control has no effect on Streaming SVE mode behavior.                       |
| 0b1        | The specified instructions are implemented when the PE is in Streaming SVE mode. |

Note

Other features may support some of the specified instructions in Non-streaming SVE mode.

FEAT\_SSVE\_BitPerm implements the functionality identified by the value 0b1 .

Access to this field is RO.

## AES, bit [24]

Indicates support for the SVE AES and 128-bit polynomial multiply long instructions identified as implemented by ID\_AA64ZFR0\_EL1.AES, when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AES   | Meaning                                                                        |
|-------|--------------------------------------------------------------------------------|
| 0b0   | This control has no effect on Streaming SVE mode behavior.                     |
| 0b1   | The specified instructions are supported when the PE is in Streaming SVE mode. |

Note

Other features may support some of the specified instructions in Non-streaming SVE mode.

FEAT\_SSVE\_AES implements the functionality identified by the value 0b1 .

Access to this field is RO.

## SFEXPA, bit [23]

Indicates support for the SVE FEXPA instruction when the PE is in Streaming SVE mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SFEXPA   | Meaning                                                                      |
|----------|------------------------------------------------------------------------------|
| 0b0      | This control has no effect on Streaming SVE mode behavior.                   |
| 0b1      | The specified instruction is supported when the PE is in Streaming SVE mode. |

Note

Other features may support some of the specified instructions in Non-streaming SVE mode.

FEAT\_SSVE\_FEXPA implements the functionality identified by the value 0b1 .

Access to this field is RO.

## Bits [22:17]

Reserved, RES0.

## STMOP, bit [16]

Indicates support for the following SME Structured sparsity outer product instructions:

- BFTMOPA (non-widening), if FEAT\_SME\_B16B16 is implemented.
- BFTMOPA (widening, BF16 to FP32).
- FTMOPA (non-widening, FP16), if FEAT\_SME\_F16F16 is implemented.
- FTMOPA (non-widening, FP32).
- FTMOPA (widening, 2-way, FP16 to FP32).
- FTMOPA (widening, 2-way, FP8 to FP16), if FEAT\_SME\_F8F16 is implemented.
- FTMOPA (widening, 4-way, FP8 to FP32) if FEAT\_SME\_F8F32 is implemented.
- STMOPA , SUTMOPA , USTMOPA , UTMOPA (4-way, Int8 to Int32). STMOPA , UTMOPA (2-way, Int16 to Int32).

The value of this field is an IMPLEMENTATION DEFINED choice of:

| STMOP   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this control. |
| 0b1     | The specified instructions are implemented.                     |

FEAT\_SME\_TMOP implements the functionality identified by the value 0b1 .

Access to this field is RO.

## Bits [15:1]

Reserved, RES0.

## SMOP4, bit [0]

Indicates support for the following SME Quarter-tile outer product instructions:

- BFMOP4A , BFMOP4S (non-widening, BF16), if FEAT\_SME\_B16B16 is implemented.
- BFMOP4A , BFMOP4S (widening, 2-way, BF16 to FP32).
- FMOP4A , FMOP4S (non-widening, FP16), if FEAT\_SME\_F16F16 is implemented.
- FMOP4A , FMOP4S (non-widening, FP32).
- FMOP4A , FMOP4S (non-widening, FP64), if FEAT\_SME\_F64F64 is implemented.
- FMOP4A , FMOP4S (widening, 2-way, FP16 to FP32).
- FMOP4A (widening, 2-way, FP8 to FP16), if FEAT\_SME\_F8F16 is implemented.
- FMOP4A (widening, 4-way, FP8 to FP32) instruction, if FEAT\_SME\_F8F32 is implemented.
- SMOP4A , SMOP4S , SUMOP4A , SUMOP4S , UMOP4A , UMOP4S , USMOP4A , USMOP4S (4-way, Int8 to Int32).
- SMOP4A , SMOP4S , SUMOP4A , SUMOP4S , UMOP4A , UMOP4S , USMOP4A , USMOP4S (4-way, Int16 to Int64), if FEAT\_SME\_I16I64 is implemented.
- SMOP4A , SMOP4S , UMOP4A , UMOP4S (2-way, Int16 to Int32).

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SMOP4   | Meaning                                                         |
|---------|-----------------------------------------------------------------|
| 0b0     | The specified instructions are not implemented by this control. |
| 0b1     | The specified instructions are implemented.                     |

FEAT\_SME\_MOP4 implements the functionality identified by the value 0b1 .

Access to this field is RO.

## Accessing ID\_AA64SMFR0\_EL1

This register is read-only and can be accessed from EL1 and higher.

This register is only accessible from the AArch64 state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64SMFR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0100 | 0b101 |

```
if PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64SMFR0_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64SMFR0_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64SMFR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64SMFR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64SMFR0_EL1;
```