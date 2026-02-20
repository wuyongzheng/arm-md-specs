## A1.5 Floating-point support

The architecture includes the following types of floating-point instructions:

- Scalar floating-point instructions that operate on the lowest numbered element of the SIMD&amp;FP registers.
- Advanced SIMD floating-point instructions that operate on multiple elements of the SIMD&amp;FP registers.
- If FEAT\_SVE is implemented, AArch64 SVE instructions that operate on multiple elements of the SVE scalable vector registers, in which the SIMD&amp;FP registers occupy the least significant 128 bits.
- If FEAT\_SME is implemented, AArch64 SME instructions that operate on multiple elements of the SVE scalable vector registers and the ZA storage.

The architecture can provide the following levels of floating-point support:

- No floating-point support. This option is licensed only for implementations targeting specialized markets.
- Advanced SIMD and floating-point support.
- SVE, plus Advanced SIMD and floating-point support.
- SMEand SVE, plus Advanced SIMD and floating-point support.

Note

All Armv8-A systems that support standard operating systems with rich application environments provide hardware support for Advanced SIMD and floating-point instructions. All Armv9-A systems that support standard operating systems with rich application environments also provide hardware support for SVE2 instructions. It is a requirement of the ARM Procedure Call Standard for AArch64, see Procedure Call Standard for the Arm 64-bit Architecture .

The architecture supports the following floating-point formats:

## Table A1-4 Floating-point formats

|                                | AArch32 state                                                                                            | AArch64 state                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| IEEE 754 half-precision        | Conversion instructions to and from IEEE 754 half-precision.                                             | Conversion instructions to and from IEEE 754 half-precision.                     |
| IEEE 754 half-precision        | Supported for data processing if FEAT_FP16 is implemented.                                               | Supported for data processing if FEAT_FP16 is implemented.                       |
| Arm alternative half-precision | Conversion instructions to and from non-IEEE 754 Arm alternative half-precision.                         | Conversion instructions to and from non-IEEE 754 Arm alternative half-precision. |
| IEEE 754 single-precision      | Supported for scalar data processing.                                                                    | Supported for scalar and vector data processing.                                 |
| IEEE 754 single-precision      | Supported for Advanced SIMD, with restrictions. See Arm standard floating-point input and output values. | Supported for scalar and vector data processing.                                 |
| IEEE 754 double-precision      | Supported for scalar data processing.                                                                    | Supported for scalar and vector data processing.                                 |
| IEEE 754 double-precision      | Not supported for Advanced SIMD.                                                                         | Supported for scalar and vector data processing.                                 |
| BFloat16                       | Supported if FEAT_AA32BF16 is implemented.                                                               | Supported if FEAT_BF16 is implemented.                                           |
| OFP8 E4M3                      | Not supported.                                                                                           | Supported if FEAT_FP8 is implemented.                                            |
| OFP8 E5M2                      | Not supported.                                                                                           | Supported if FEAT_FP8 is implemented.                                            |

For many floating-point instructions, there are configurable behaviors, such as:

- Configurable rounding modes. See Rounding.
- Configurable trapping of floating-point exceptions. See Floating-point exceptions and exception traps.
- Configurable non-IEEE 754 Default NaN behavior. See NaN handling and the Default NaN.

- Configurable non-IEEE 754 flushing to zero of denormalized numbers. See Flushing denormalized numbers to zero.

Floating-point computation using AArch32 Advanced SIMD instructions remains unchanged from Armv7. T32 and A32 Advanced SIMD floating-point instructions always use Arm standard floating-point arithmetic and performs IEEE 754 floating-point arithmetic with the following restrictions:

- Denormalized numbers are flushed to zero, see Flushing denormalized numbers to zero.
- Only default NaNs are supported, see Default NaN.
- The Round to Nearest rounding mode is used.
- Untrapped floating-point exception handling is used for all floating-point exceptions.

If floating-point exception trapping is supported, then unless stated otherwise, when a floating-point exception is not trapped, that exception causes a cumulative status register bit to be set to 1 and the operation produces a default result. For more information, see Floating-point exceptions and exception traps.

In:

- AArch64 state, the Floating-point Control Register, FPCR, controls floating-point operation, and the Floating-point Status Register, FPSR, returns floating-point status information.
- AArch32 state, there is a single Floating-Point Status and Control Register, FPSCR, combining the FPCR and FPSR fields.

In AArch64 state, the PSTATE.{N,Z,C,V} condition flags are updated by floating-point comparison operations.

In AArch32 state, the FPSCR.{N,Z,C,V} condition flags are updated by floating-point comparison operations.

If FEAT\_FlagM2 is implemented, the AArch64 instructions AXFLAG and XAFLAG convert between the Arm floating-point condition flags in PSTATE and an alternative format shown in Table C6-1.

Note

For additional details of AArch32 state floating-point support, see Advanced SIMD and floating-point support.

The remainder of this section contains:

- Instruction support.
- Floating-point standards, and terminology.
- Arm standard floating-point input and output values.
- Summary of BFloat16 instruction behaviors.
- Summary of FP8 instruction behaviors.
- Flushing denormalized numbers to zero.
- NaN handling and the Default NaN
- Rounding
- Floating-point exceptions and exception traps
- Alternate BFloat16 behaviors
- BFloat16 behaviors for instructions that compute sum-of-products

## A1.5.1 Instruction support

The floating-point instructions support:

- Load and store for single elements and vectors of multiple elements.

Note

Single elements are also referred to as scalar elements.

- Data processing on single and multiple elements.
- Complex number arithmetic.
- Floating-point conversion between different levels of precision.
- Conversion between floating-point and integer types.
- Floating-point rounding.
- Atomic floating-point in-memory operations.

For more information on floating-point instructions in AArch64 state, see A64 Instruction Set Overview.

For more information on floating-point instructions in AArch32 state, see The AArch32 Instruction Sets Overview.

## A1.5.2 Floating-point standards, and terminology

The Arm architecture includes support for all the required features of ANSI/IEEE Std 754-2008, IEEE Standard for Binary Floating-Point Arithmetic , referred to as IEEE 754-2008. However, some terms in this Manual are based on the 1985 version of this standard, referred to as IEEE 754-1985:

- Arm floating-point terminology generally uses the IEEE 754-1985 terms. This section summarizes how IEEE 754-2008 changes these terms.
- References to IEEE 754 that do not include the issue year apply to either issue of the standard.

Table A1-5 shows how the terminology in this Manual differs from that used in IEEE 754-2008.

Table A1-5 Floating-point terminology

| This manual                        | IEEE 754-2008                |
|------------------------------------|------------------------------|
| Normalized a                       | Normal                       |
| Denormal, or denormalized          | Subnormal                    |
| Round towards Minus Infinity (RM)  | roundTowardsNegative         |
| Round towards Plus Infinity (RP)   | roundTowardsPositive         |
| Round towards Zero (RZ)            | roundTowardZero              |
| Round to Nearest (RN)              | roundTiesToEven              |
| Round to Nearest with Ties to Away | roundTiesToAway              |
| Rounding mode                      | Rounding-direction attribute |

## A1.5.3 Arm standard floating-point input and output values

The Arm architecture provides full IEEE 754 floating-point arithmetic support. In AArch32 state, floating-point operations performed using Advanced SIMD instructions are limited to Arm standard floating-point operation , regardless of the selected rounding mode in the FPSCR.

Arm standard floating-point arithmetic supports the following input formats defined by the IEEE 754 floating-point standard:

- Zeros.
- Normalized numbers.
- Denormalized numbers are flushed to 0 before floating-point operations, see Flushing denormalized numbers to zero.
- NaNs.

- Infinities.

Arm standard floating-point arithmetic supports the Round to Nearest (roundTiesToEven) rounding mode defined by the IEEE 754 standard.

Arm standard floating-point arithmetic supports the following output result formats defined by the IEEE 754 standard:

- Zeros.
- Normalized numbers.
- Results with an absolute value less than the minimum normalized number are flushed to zero, see Flushing denormalized numbers to zero.
- NaNs produced in floating-point operations are always the default NaN, see Default NaN.
- Infinities.

## Note

AArch64 Advanced SIMD floating-point arithmetic is performed using the rounding mode selected by the FPCR.

## A1.5.4 Summary of BFloat16 instruction behaviors

BFloat16 instructions follow the floating-point behaviors shown in Table A1-6 and Table A1-7:

Table A1-6 Advanced SIMD and floating-point, and SVE, BFloat16 instruction behaviors

|                  |                                                     | Behaviors when the PE is in Streaming SVE mode                                                                                                 | Behaviors when the PE is not in Streaming SVE mode                                                                       |
|------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Advanced SIMD&FP | BFCVT                                               | Behaves as: Floating-point behaviors in Streaming SVE mode.                                                                                    | Follows single-precision behaviors.                                                                                      |
| Advanced SIMD&FP |                                                     | This instruction also supports the Alternate BFloat16 behaviors.                                                                               | This instruction also supports the Alternate BFloat16 behaviors.                                                         |
| Advanced SIMD&FP | BFCVTN , BFCVTN2 BFMLALB , BFMLALT                  | If legal when executed in Streaming SVE mode a , behave as Floating-point behaviors in Streaming SVE mode.                                     | Follows single-precision behaviors.                                                                                      |
| Advanced SIMD&FP |                                                     | These instructions also support the Alternate BFloat16 behaviors.                                                                              | These instructions also support the Alternate BFloat16 behaviors.                                                        |
| Advanced SIMD&FP | BFDOT , BFMMLA                                      | If legal when executed in Streaming SVE mode a , behave as BFloat16 behaviors for instructions that compute sum-of-products.                   | Behave as BFloat16 behaviors for instructions that compute sum-of-products.                                              |
| SVE              | BFADD , BFSUB BFMLA , BFMLS , BFMUL                 | Behave as Floating-point behaviors in Streaming SVE mode.                                                                                      | Follows single-precision behaviors.                                                                                      |
| SVE              | BFCLAMP BFMAX , BFMAXNM BFMIN , BFMINNM             | Behave as both: • Floating-point behaviors in Streaming SVE mode. • Additional behaviors described in the individual instruction descriptions. | Follows both: • Single-precision behaviors. • Additional behaviors described in the individual instruction descriptions. |
| SVE              | BFCVT , BFCVTNT BFMLALB , BFMLALT BFMLSLB , BFMLSLT | Behave as Floating-point behaviors in Streaming SVE mode.                                                                                      | Follows single-precision behaviors.                                                                                      |
| SVE              |                                                     | These instructions also support the Alternate BFloat16 behaviors.                                                                              | These instructions also support the Alternate BFloat16 behaviors.                                                        |
| SVE              | BFDOT                                               | Behave as BFloat16 behaviors for instructions that compute sum-of-products.                                                                    | Behave as BFloat16 behaviors for instructions that compute sum-of-products.                                              |
| SVE              | BFMMLA                                              | If legal when executed in Streaming SVE mode a , behaves as BFloat16 behaviors for instructions that compute sum-of-products.                  | Behaves as BFloat16 behaviors for instructions that compute sum-of-products.                                             |

a. These instructions generate an SME illegal instruction exception in Streaming SVE mode if FEAT\_SME\_FA64 is not implemented or not enabled at the current Exception level. See Streaming SVE mode and RZFGJP.

Table A1-7 SME BFloat16 instruction behaviors

| SME                                                                       | Behaviors in Streaming SVE mode                                                                                                     | ZA storage                                                                                                                          | Behaviors when the PE is not in Streaming SVE mode   |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| BFADD , BFMLA , BFMLS , BFSUB BFMOPA (non-widening) BFMOPS (non-widening) | Behave as Floating-point behaviors for instructions that target theSMEZA array.                                                     | Illegal a                                                                                                                           | Illegal a                                            |
| BFCLAMP BFMAX , BFMAXNM BFMIN , BFMINNM                                   | Behave as both: • Floating-point behaviors in Streaming SVE mode. • Additional behaviors described in the instruction descriptions. | Behave as both: • Floating-point behaviors in Streaming SVE mode. • Additional behaviors described in the instruction descriptions. | Illegal a                                            |
| BFCVT (single-precision to BFloat16), BFCVTN                              | Behave as Floating-point behaviors in Streaming SVE mode. These instructions also support the Alternate BFloat16 behaviors.         | Behave as Floating-point behaviors in Streaming SVE mode. These instructions also support the Alternate BFloat16 behaviors.         | Illegal a                                            |
| BFDOT , BFVDOT BFMOPA (widening) BFMOPS (widening)                        | Behave as BFloat16 behaviors for instructions that compute sum-of-products.                                                         | Illegal a                                                                                                                           | Illegal a                                            |
| BFMLAL BFMLSL                                                             | Behave as Floating-point behaviors for instructions that target theSMEZA array.                                                     | Illegal a                                                                                                                           | Illegal a                                            |

Unless otherwise specified, BFloat16 instructions follow the behaviors defined in all of:

- Flushing denormalized numbers to zero.
- Rounding.
- Floating-point exceptions and exception traps

See also:

- Streaming SVE mode.
- ZAstorage.

## A1.5.5 Summary of FP8 instruction behaviors

All FP8 instructions:

- Use the Round to Nearest (RN) mode, ignoring FPCR.RMode.
- Do not flush denormalized inputs and outputs to zero, as if FPCR.{FZ, FIZ, FZ16} are all 0.
- Generate Default NaN outputs, as if FPCR.DN is 1, unless otherwise specified.
- Honor FPCR.AH, if FEAT\_AFP is implemented.
- Treat an unsupported FP8 input format, as defined in FPMR.F8S1 and FPMR.F8S2, as a CONSTRAINED UNPREDICTABLE choice of:
- -Asignaling NaN.
- -Any of the supported FP8 formats.

- Handle an unsupported FP8 output format, as defined in FPMR.F8D, by a CONSTRAINED UNPREDICTABLE choice of:
- -Setting the result to 0xff and causing an Invalid Operation floating-point exception.
- -Generating the expected result of any of the supported FP8 formats.
- Do not cause an Input Denormal floating-point exception or update FPSR.IDC.

FP8 convert instructions:

- Produce the expected default result and update FPSR.{IOC, IXC, UFC} when they detect Invalid Operation, Inexact, or Underflow exceptional floating-point conditions.
- When the rounded result with unbounded exponent has an absolute value that is greater than the maximum normalized number for the output precision, or when an Infinity is converted from other floating-point formats to an FP8 format:
- -Generate one of the following outputs with the sign of the result:
- -When FPMR.OSC is 1, the maximum normalized number.
- -When FPMR.OSC is 0 and the output is in the OFP8 E4M3 format, a signaling NaN .
- -Otherwise, an Infinity.
- -Regardless of the value of FPMR.OSC, cause an Overflow and Inexact floating-point exception.
- When the PE is in Streaming SVE mode, disable trapped floating-point exceptions as if FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} are all zero.

FP8 multiplication instructions:

- Produce the expected default result and do not update FPSR.{IOC, IXC, UFC} when they detect Invalid Operation, Inexact, or Underflow exceptional floating-point conditions.
- When the rounded result with unbounded exponent has an absolute value that is greater than the maximum normalized number for the output precision:
- -Generate one of the following outputs with the sign of the result:
- -When FPMR.OSM is 1, the maximum normalized number.
- -When FPMR.OSM is 0, an Infinity.
- -Do not update FPSR.OFC.
- Disable trapped floating-point exceptions, as if FPCR.{IDE,IXE,UFE,OFE,DZE,IOE} are all zero.

## A1.5.6 Flushing denormalized numbers to zero

For this section if FEAT\_AFP is not implemented, the behavior is the same as if FPCR.AH == 0, FPCR.FIZ == 0, and FPCR.NEP == 0.

Calculations involving denormalized numbers and Underflow exceptions can reduce the performance of floating-point processing. For many algorithms, replacing the denormalized operands and intermediate results with zeros can recover this performance, without significantly affecting the accuracy of the final result. Arm floating-point implementations allow denormalized numbers to be flushed to zero to permit this optimization.

If a number value satisfies the condition 0 &lt; Abs(value) &lt; MinNorm , it is treated as a denormalized number.

MinNorm is defined as follows:

- For OFP8 E4M3 numbers, MinNorm is 2 -6 .
- For half-precision and OFP8 E5M2 numbers, MinNorm is 2 -14 .
- For single-precision and BFloat16 numbers, MinNorm is 2 -126 .
- For double-precision numbers, MinNorm is 2 -1022 .

Flushing denormals to zero is incompatible with the IEEE 754 standard, and must not be used when IEEE 754 compatibility is a requirement. Enabling flushing of denormals to zero must be done with care. Although it can improve performance on some algorithms, there are significant limitations on its use. These are application-dependent:

- On many algorithms, it has no noticeable effect, because the algorithm does not usually process denormalized numbers.

- On other algorithms, it can cause exceptions to occur and can seriously reduce the accuracy of the results of the algorithm.

For information about FP8 instruction behaviors, see Summary of FP8 instruction behaviors.

## A1.5.6.1 Flushing denormalized inputs to zero

If flushing denormalized inputs to zero is enabled for an instruction and a data type, and an input to that instruction is a denormalized number of that data type, the input operand is flushed to zero, and its sign bit is not changed.

If a floating-point operation has a denormalized input that is flushed to zero, for all purposes within the instruction other than calculating Input Denormal floating-point exceptions, all inputs that are denormalized numbers are treated as though they were zero with the same sign as the input.

For floating-point instructions, if the instruction processes half-precision inputs, flushing denormalized inputs to zero can be controlled as follows:

- If FPCR.FZ16 == 0, denormalized half-precision inputs are not flushed to zero.
- If FPCR.FZ16 == 1:
- -Denormalized half-precision inputs to data processing instructions are flushed to zero.
- -Denormalized half-precision inputs to convert instructions are not flushed to zero.

If FPCR.FIZ == 1, or both FPCR.AH == 0 and FPCR.FZ == 1, then for floating-point instructions other than FABS and FNEG , for all inputs other than half-precision, denormalized inputs are flushed to zero.

If FPCR.FZ == 0, for all inputs other than half-precision, FPCR.FZ does not cause denormalized inputs to be flushed to zero, although other factors might cause denormalized inputs to be flushed to zero.

If FPCR.AH == 1, regardless of the value of FPCR.FIZ, all of the following instructions flush all input denormal numbers to zero:

- The BFloat16 instructions defined in Alternate BFloat16 behaviors.
- Single-precision and double-precision instructions: FRECPE, FRECPS, FRECPX, FRSQRTE, and FRSQRTS.

## A1.5.6.2 Flushing denormalized outputs to zero

If a denormalized output is flushed to zero, the output is returned as zero with the same sign bit as the denormalized output value.

If FPCR.AH == 0, the test for a denormalized number for the purpose of flushing the output to zero occurs before rounding.

If FPCR.AH == 1, the test for a denormalized number for the purpose of flushing the output to zero occurs after rounding using an unbounded exponent.

If FPCR.FZ == 0, then unless otherwise specified, for all outputs other than half-precision, FPCR.FZ does not cause denormalized outputs to be flushed to zero, although other factors might cause denormalized outputs to be flushed to zero.

If FPCR.FZ == 1, for all outputs other than half-precision, for floating-point instructions other than FABS , FNEG , FMAX , FMAXP , FMAXV , FMIN , FMINP , FMINV , BFMIN , and BFMAX , denormalized outputs are flushed to zero.

If FPCR.EBF == 0, BFDOT , BFMMLA , BFVDOT, BFMOPA (widening), and BFMOPS (widening) instructions unconditionally flush denormalized outputs to zero, as defined in BFloat16 behaviors for instructions that compute sum-of-products.

If FPCR.FZ16 == 0, denormalized half-precision outputs are not flushed to zero.

If FPCR.FZ16 == 1, for floating-point instructions other than FABS , FNEG , FMAX , FMAXP , FMAXV , FMIN , FMINP , FMINV , BFMIN , and BFMAX , denormalized half-precision outputs are flushed to zero.

If FPCR.AH == 1, regardless of the value of FPCR.{FZ, FZ16}, denormalized outputs of FABS , FNEG , FMAX , FMAXP , FMAXV , FMIN , FMINP , FMINV , BFMIN , and BFMAX , are not flushed to zero.

If FPCR.AH == 1, regardless of the value of FPCR.FZ, all of the following instructions flush all output denormal numbers to zero:

- The BFloat16 instructions defined in Alternate BFloat16 behaviors.
- Single-precision and double-precision instructions: FRECPE, FRECPS, FRECPX, FRSQRTE, and FRSQRTS.

If FPCR.FIZ == 1, for the atomic floating-point memory instructions defined in Atomic floating-point memory operations, denormalized BFloat16, single-precision, and double-precision outputs are flushed to zero.

## A1.5.6.3 Flushing denormalized BFloat16 intermediate results to zero

BFloat16 arithmetic instructions BFDOT , BFMMLA , BFVDOT , BFMOPA (widening) , and BFMOPS (widening) in AArch64 state, and VDOT (by element), VDOT (vector), VMMLA in AArch32 state when working with BFloat16 inputs, convert BFloat16 input values to IEEE single-precision format, and calculate N-way dot-products, accumulating the products in single-precision accumulators. If one of these instructions processes an intermediate result that is a single-precision denormalized number:

- If the instruction is one of AArch64 BFDOT , BFMMLA , BFVDOT , BFMOPA (widening) , and BFMOPS (widening) , the intermediate result is unconditionally flushed to zero if FEAT\_EBF16 is not implemented or when FPCR.EBF is 0. See BFloat16 behaviors for instructions that compute sum-of-products.
- If the instruction is one of AArch32 VDOT (by element), VDOT (vector), VMMLA, the intermediate result is unconditionally flushed to zero.

## A1.5.7 NaN handling and the Default NaN

The IEEE 754 standard defines a NaN as a number with all exponent bits set to 1 and a nonzero number in the mantissa, and specifies that the sign bit of a NaN has no significance.

The Arm architecture additionally defines the following in Table A1-8:

- A Default NaN , compliant with the IEEE 754 standard.
- ABFloat16 NaN, that follows the encoding in BFloat16 floating-point format.
- OFP8 NaN, that follow the encodings in FP8 floating-point formats.

For a quiet NaN output derived from a signaling NaN operand, the most significant fraction bit is set to 1.

APEis forbidden to generate a NaN whose value is strongly correlated to the values of non-NaN inputs as a speculative result of a floating-point calculation not involving NaN inputs.

## A1.5.7.1 Default NaN

ADefault NaN is encoded as described in Table A1-8.

Table A1-8 Default NaN encodings

|                          | Half-precision, IEEE Format   | Single- precision               | Double- precision               | BFloat16                      | OFP8 E4M3          | OFP8 E5M2                    |
|--------------------------|-------------------------------|---------------------------------|---------------------------------|-------------------------------|--------------------|------------------------------|
| Sign bit if FPCR.AH == 0 | 0                             | 0                               | 0                               | 0                             | 0                  | 0                            |
| Sign bit if FPCR.AH == 1 | 1                             | 1                               | 1                               | 1                             | 1                  | 1                            |
| Exponent                 | 0x1F                          | 0xFF                            | 0x7FF                           | 0xFF                          | 0xF                | 0x1F                         |
| Fraction                 | Bit[9] == '1', bits[8:0] == 0 | Bit[22] == '1', bits[21:0] == 0 | Bit[51] == '1', bits[50:0] == 0 | Bit[6] == '1', bits[5:0] == 0 | Bits[2:0] == '111' | Bit[1] == '1', bit[0] == '0' |

When FPCR.DN == 1, if any input to a floating-point operation is a NaN, the output is a Default NaN, unless the instruction is one of the following:

- FABS , FNEG , FMAX , FMAXP , FMAXV , FMIN , FMINP , FMINV , BFMAX , and BFMIN . For these, see the individual instruction descriptions for their Default NaN behavior.

The atomic floating-point memory instructions defined in Atomic floating-point memory operations generate only the Default NaN value, as if FPCR.DN == 1.

Floating-point instructions that detect an Invalid Operation condition for a reason other than one of its inputs being a NaN, produce a Default NaN as the result.

## A1.5.7.2 NaN handling

The IEEE 754 standard does not specify which input NaN is used as the output NaN. Therefore, where the Arm architecture specifies which input NaN to use, this is an addition to the requirements in the IEEE 754 standard.

Depending on the operation, the exact value of a derived quiet NaN output might have both a different sign and different fraction bits from its source. See individual instruction descriptions for details.

## A1.5.7.3 NaN propagation

For NaN propagation rules for:

- BFDOT and BFMMLA, see BFloat16 behaviors for instructions that compute sum-of-products.
- FP8 instructions, see Summary of FP8 instruction behaviors.

Otherwise, behavior is as described in this section.

If an output NaN is derived from one of the operands, how the input NaN propagates to the output depends on the instruction and the number of operands.

If an output NaN is derived from an input NaN and if the size of the output format is the same as the input format, then all of the following apply:

- If the input NaN is a quiet NaN, the output NaN is derived from the input NaN.
- If the input NaN is a signaling NaN, the output NaN is derived as follows:
- -If the handling of a signaling NaN by the instruction detects an Invalid Operation condition, the output NaN is derived from a quietened version of the input NaN.
- -If the handling of a signaling NaN by the instruction does not detect an Invalid Operation condition, the output NaN is derived from the input NaN.

If an output NaN is derived from an input NaN and if the size of the output format is larger than the input format, all of the following apply:

- If the input NaN is a quiet NaN, the output NaN is the same as the input NaN except that the mantissa is zero-extended in the low-order bit to fit the output format, and the exponent field is set to all ones.
- If the input NaN is a signaling NaN, the output NaN is the quieted version of the input NaN, except that the mantissa is zero-extended in the low-order bits and the exponent field is set to all ones.

If an output NaN is derived from an input NaN and if the size of the output format is smaller than the input format, all of the following apply:

- If the input NaN is a quiet NaN, the output NaN is the same as the input NaN except that the mantissa is truncated in the lower-order bits to fit the output format, and the exponent field is set to all ones.
- If the input NaN is a signaling NaN, the output NaN is the quieted version of the input NaN except that the mantissa is truncated in the lower-order bits to fit the output format, and the exponent field is set to all ones.

For the following descriptions, the term 'first operand' and 'second operand' relate to the left-to-right ordering of the arguments of the pseudocode function that describes the operation.

If FPCR.DN == 0, for instructions that perform a floating-point operation, other than FABS , FNEG , FMAX* , and FMIN* , NaN outputs that derive from NaN inputs are derived as follows:

- If all of the following apply, an instruction outputs a quiet NaN derived from the first signaling NaN operand:

- -FPCR.AH == 0.
- -At least one operand is a signaling NaN.
- -The instruction is not trapped.
- If all of the following apply, an instruction outputs a quiet NaN derived from the first NaN operand:
- -FPCR.AH == 0.
- -At least one operand is a NaN, but none of the operands is a signaling NaN.
- -The instruction is not trapped.
- If all of the following apply, the output is a quiet NaN derived from the NaN operand:
- -FPCR.AH == 1.
- -The operation has two floating-point inputs.
- -The operation has only one NaN operand.
- If all of the following apply, the output is a NaN derived from the &lt;Zn&gt; , &lt;Vn&gt; , &lt;Hn&gt; , &lt;Sn&gt; , or &lt;Dn&gt; register, except for SVE FSUBR (vectors) and SVE FDIVR, for which the output is a NaN derived from the &lt;Zm&gt; register:
- -FPCR.AH == 1.
- -The operation has two floating-point inputs.
- -The operation has two NaN operands.
- If all of the following apply, the output is a NaN derived from the NaN held in the &lt;Zn&gt; , &lt;Vn&gt; , &lt;Hn&gt; , &lt;Sn&gt; , or &lt;Dn&gt; registers:
- -FPCR.AH == 1
- -The instruction is one of those shown in Table A1-9.
- -One of the following applies:
- -The operation has three NaN operands.
- -The operation has two NaN operands and the &lt;Zn&gt; , &lt;Vn&gt; , &lt;Hn&gt; , &lt;Sn&gt; or &lt;Dn&gt; register holds a NaN.
- If all of the following apply, the output is a NaN derived from the NaN held in the &lt;Zm&gt; , &lt;Vm&gt; , &lt;Hm&gt; , &lt;Sm&gt; , or &lt;Dm&gt; registers:
- -FPCR.AH == 1
- -The instruction is one of those shown in Table A1-9.
- -The operation has two NaN operands and the &lt;Zn&gt; , &lt;Vn&gt; , &lt;Hn&gt; , &lt;Sn&gt; or &lt;Dn&gt; register does not hold a NaN.

## Table A1-9

| Advanced SIMD&FP   | BFMLALB , BFMLALT , FCMLA , FMADD , FMLA , FMLAL , FMLAL2 , FMLS , FMLSL , FMLSL2 , FMSUB , FNMADD , and FNMSUB .                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SVE                | BFMLA , BFMLALB , BFMLALT , BFMLS , BFMLSLB , BFMLSLT , FCMLA , FMAD , FMLA , FMLALB , FMLALT , FMLS , FMLSLB , FMLSLT , FMSB , FNMAD , FNMLA , FNMLS , FNMSB . |

- When the operation has four or more floating-point inputs:
- -If at least one argument to FPDot() is a signaling NaN, a function outputs a quiet NaN derived from the first signaling NaN argument.
- -If at least one argument to FPDot() is a NaN, but none of the arguments is a signaling NaN, a function outputs a quiet NaN derived from the first NaN argument.

If FPCR.AH == 0, and an output NaN is derived from an input NaN, the pseudocode functions FPAbs() , FPNeg() , BFNeg() , FPTrigMAdd() , and FPTrigSSel() can change the sign of the NaN.

If FPCR.AH == 1, and an output NaN is derived from an input NaN, for all cases, the sign bit of the NaN is unchanged.

For FMAX* , FMIN* , BFMAX* , BFMIN* , FCLAMP , and BFCLAMP , the NaN handling is described in the instruction description.

## A1.5.8 Rounding

The rounding mode specifies how the exact result of a floating-point operation is rounded to a value in the destination format.

The rounding mode is either determined by the rounding mode control field FPCR.RMode or by the instruction.

If FPCR.AH == 1, for any value of FPCR.RMode, the following instructions use Round to Nearest on outputs:

- The BFloat16 instructions defined in Alternate BFloat16 behaviors.
- Single-precision and double-precision instructions FRECPE, FRECPS, FRECPX, FRSQRTE, and FRSQRTS.
- Half-precision instructions FRECPE, FRECPS, FRECPX, FRSQRTE, and FRSQRTS.

For information about FP8 instruction behaviors, see Summary of FP8 instruction behaviors.

FPCR.RMode can select one of:

- Round to Nearest (RN) mode.
- Round towards Plus Infinity (RP) mode.
- Round towards Minus Infinity (RM) mode.
- Round towards Zero (RZ) mode.

The following additional rounding behaviors are not selected by FPCR.RMode, but are used by some instructions:

- Round to Odd.
- Round to Nearest with Ties to Away.

## A1.5.8.1 Round to Nearest (RN) mode

Round to Nearest rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format as follows:

- If the value before rounding has an absolute value that is too large to represent in the output format, the rounded value is an Infinity. The sign of the rounded value is the same as the sign of the value before rounding.
- If the value before rounding has an absolute value that is not too large to represent in the output format, the result is calculated as follows:
- -If the two nearest floating-point numbers bracketing the value before rounding are equally near, the result is the number with an even least significant digit.
- -If the two nearest floating-point numbers bracketing the value before rounding are not equally near, the result is the floating-point number nearest to the value before rounding.

## A1.5.8.2 Round towards Plus Infinity (RP) mode

Round towards Plus Infinity rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is the floating-point number in the output format that is closest to and not less than the value before rounding. The result can be plus infinity.

## A1.5.8.3 Round towards Minus Infinity (RM) mode

Round towards Minus Infinity rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is the number in the output format that is closest to and not greater than the value before rounding. The result can be minus infinity.

## A1.5.8.4 Round towards Zero (RZ) mode

Round towards Zero rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is the floating-point number in the output format that is closest to and not greater in absolute value than the value before rounding.

## A1.5.8.5 Round to Nearest with Ties to Away

Round to Nearest with Ties to Away rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is calculated as follows:

- If the two nearest floating-point numbers bracketing the value before rounding are equally near, the result is the number with the largest absolute value.
- If the two nearest floating-point numbers bracketing the value before rounding are not equally near, the result is the floating-point number nearest to the value before rounding.

Round to Nearest with Ties to Away rounding is used by FCVTAS (scalar), FCVTAS (vector), FCVTAU (scalar), FCVTAU (vector), FRINTA (scalar), and FRINTA (vector).

## A1.5.8.6 Round to Odd

Round to Odd is not defined by IEEE 754.

Round to Odd rounds the exact result of a floating-point operation to a value that is representable in the destination format. If the result of the rounding is inexact, the least significant bit of the mantissa is forced to 1.

The following instructions use Round to Odd:

- BFloat16 instructions defined in BFloat16 behaviors for instructions that compute sum-of-products.
- FCVTXN, FCVTXN2, FCVTX, and FCVTXNT, for which Round to Odd rounding can avoid double rounding errors when a floating-point value is converted to a lower precision destination format through an intermediate precision format.

## Example A1-1 Converting 64-bit floating-point format to 16-bit floating-point format

A64-bit floating-point value can be converted to a correctly rounded 16-bit floating-point value using the following steps:

1. Use an FCVTXN instruction to produce a 32-bit value.
2. Use another instruction with the required rounding mode to convert the 32-bit value to the final 16-bit floating-point value.

## A1.5.9 Floating-point exceptions and exception traps

Execution of a floating-point instruction, or execution of an Advanced SIMD, SVE, or SME instruction that performs floating-point operations, can generate an exceptional condition, called a floating-point exception .

Predicated SVE floating-point instructions only generate floating-point exceptions in response to floating-point operations performed on Active elements .

Note

In AArch64 state, an Advanced SIMD, SVE, or SME instruction that operates on floating-point values can perform multiple floating-point operations. Therefore, this section describes the handling of a floating-point exception on an operation , rather than on an instruction .

The architecture does not support asynchronous reporting of floating-point exceptions.

For each of the following floating-point exceptions, it is IMPLEMENTATION DEFINED whether an implementation includes synchronous exception generation:

- Input Denormal.
- Inexact.
- Underflow.

- Overflow.
- Divide by Zero.
- Invalid Operation.

If an implementation does not support synchronous exception generation from a floating-point exception, then that synchronous exception is never generated and all statements about synchronous exception generation from that floating-point exception do not apply to the implementation.

Synchronous exception generation by floating-point exceptions is enabled using the FPCR as follows:

- For each floating-point exception that supports synchronous exception generation, the relevant control bit chosen from FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} is used to enable synchronous exception generation.
- For each floating-point exception that does not support synchronous exception generation, the relevant bit chosen from FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} is RAZ/WI.

For information about FP8 instruction behaviors, see Summary of FP8 instruction behaviors.

## A1.5.9.1 Operations that do not generate floating-point exceptions

The following instructions do not generate any floating-point exceptions:

- The SVE exponential accelerator instruction, FEXPA.
- The SVE trigonometric select coefficient instruction, FTSSEL.
- The BFloat16 instructions defined in BFloat16 behaviors for instructions that compute sum-of-products.
- The SME instructions defined in Floating-point behaviors for instructions that target the SME ZA array.
- The instructions defined in Atomic floating-point memory operations.

If FPCR.AH is 1, all of the following instructions do not generate any floating-point exceptions regardless of their input values:

- The BFloat16 instructions defined in Alternate BFloat16 behaviors.
- Single-precision, double-precision and half-precision instructions FRECPE, FRECPS, FRECPX, FRSQRTE, and FRSQRTS.

All the following apply to FPAbs(), FPNeg() , and BFNeg ():

- They cannot generate floating-point exceptions.
- The floating-point behavior described in the Flushing denormalized numbers to zero does not apply to them.
- The floating-point behavior described in the section NaN handling and the Default NaN does not apply to them.
- When FPCR.AH is 1, the sign of a NaN input is not changed. When FPCR.AH is 0, the sign of a NaN input can be changed.

## A1.5.9.2 Input Denormal exceptions

The cumulative floating-point exception bit FPSR.IDC, and the trap enable bit FPCR.IDE both relate to Input Denormal exceptions.

Input Denormal exceptions are not generated for denormalized half-precision inputs. For BFloat16 denormalized inputs and FP8 denormalized inputs, see Summary of BFloat16 instruction behaviors and Summary of FP8 instruction behaviors respectively. For single-precision and double-precision inputs:

- When FPCR.{AH, FZ, FIZ} is {0, 0, x}, Input Denormal exceptions are not generated.
- When FPCR.{AH, FZ, FIZ} is {0, 1, x}, an Input Denormal exception is generated when an input is flushed to zero.
- When FPCR.{AH, FZ, FIZ} is {1, x, 1}, Input Denormal exceptions are not generated.
- When FPCR.{AH, FZ, FIZ} is {1, x, 0}, an operation with a denormalized input generates an Input Denormal exception unless any of the following are true:
- -Another operand to the operation is a NaN.

- -The operation generates a Divide-by-Zero exception.
- -The operation generates an Invalid Operation exception.
- -The instruction that generated the operation was one of:
- -Advanced SIMD&amp;FP convert from single-precision to BFloat16: BFCVT, BFCVTN, BFCVTN2.
- -Advanced SIMD&amp;FP convert to integer: FCVTAS , FCVTAU , FCVTMS , FCVTMU , FCVTNS , FCVTNU , FCVTPS , FCVTPU , FCVTZS , FCVTZU .
- -Advanced SIMD&amp;FP round to integral: FRINT32X , FRINT32Z , FRINT64X , FRINT64Z , FRINTA , FRINTI , FRINTM , FRINTN , FRINTP , FRINTX , FRINTZ .
- -Advanced SIMD&amp;FP JavaScript convert to signed fixed-point: FJCVTZS.
- -SVE convert from single-precision to BFloat16: BFCVT, BFCVTNT.
- -SVE convert to integer: FCVTZS, FCVTZU.
- -SVE round to integral: FRINT&lt;r&gt;.
- -SMEconvert from single-precision to BFloat16: BFCVT, BFCVTN.
- -SMEconvert to integer: FCVTZS, FCVTZU.
- -SMEround to integral: FRINTA, FRINTM, FRINTN, FRINTP.

When a denormalized input is flushed to zero, the occurrence of floating-point exceptions other than Input Denormal is determined by treating the input value that is flushed to zero as zero.

## A1.5.9.3 Inexact exceptions

The cumulative floating-point exception bit FPSR.IXC and the trap enable bit FPCR.IXE both relate to Inexact exceptions.

If a denormalized output is flushed to zero, all of the following apply:

- If FPCR.AH is 1, an Inexact exception is generated.
- If FPCR.AH is 0, an Inexact exception is not generated.

If a result is not flushed to zero, and the result does not equal the result computed with unbounded exponent range and unbounded precision, then an Inexact exception is generated.

## A1.5.9.4 Underflow exceptions

The cumulative floating-point exception bit FPSR.UFC, and the trap enable bit FPCR.UFE both relate to Underflow exceptions.

If FPCR.AH is 0, for the purpose of Underflow floating-point exception generation, a denormalized number is detected before rounding is applied.

If FPCR.AH is 1, for the purpose of Underflow floating-point exception generation, a denormalized number is detected after rounding with an unbounded exponent.

If the result of a floating-point operation is a denormalized number that is not flushed to zero, then:

- If the result is exact, an Underflow floating-point exception is generated only if FPCR.UFE is 1.
- If the result is inexact, an Underflow floating-point exception is always generated.

If the result of a floating-point operation is a denormalized number that is flushed to zero, then the Underflow floating-point exception is generated, however this floating-point exception is not trapped regardless of the value of FPCR.UFE.

## A1.5.9.5 Overflow exceptions

The cumulative floating-point exception bit FPSR.OFC, and the trap enable bit FPCR.OFE both relate to Overflow exceptions.

If the output of an instruction rounded with an unbounded exponent is greater than the maximum normalized number for the output precision, an Overflow exception is generated.

If an untrapped Overflow exception is generated, the result is determined by the selected rounding behavior and the sign of the result before rounding, as follows:

- Round to Nearest carries all overflows to infinity with the sign of the result before rounding, except for FP8 instructions, for which, see Summary of FP8 instruction behaviors.
- Round towards Plus Infinity carries negative overflows to the most negative finite number of the output precision, and carries positive overflows to plus infinity.
- Round towards Minus Infinity carries positive overflows to the largest finite number of the output precision, and carries negative overflows to minus infinity.
- Round towards Zero carries all overflows to the output precision's largest finite number with the sign of the result before rounding.
- Round to Nearest Ties to Away carries all overflows to infinity with the sign of the result before rounding.
- Round to Odd, when used by convert instructions, carries all overflows to the output precision's largest finite number with the sign of the result before rounding.
- Round to Odd, when used by some BFloat16 instructions, carries all overflows to infinity with the sign of the result before rounding.

## A1.5.9.6 Divide by Zero exceptions

The cumulative floating-point exception bit FPSR.DZC, and the trap enable bit FPCR.DZE both relate to Divide by Zero exceptions.

If a floating-point operation divides a finite nonzero number by zero, a Divide by Zero exception is generated.

If a floating-point operation divides a finite nonzero number by zero, and the Divide by Zero exception is untrapped, the result is a correctly signed infinity.

## A1.5.9.7 Invalid Operation exceptions

The cumulative floating-point exception bit FPSR.IOC, and the trap enable bit FPCR.IOE both relate to Invalid Operation exceptions.

For any floating-point instruction that performs a floating-point operation, if any of the following apply, the instruction generates an Invalid Operation exception:

- At least one operand is a signaling NaN.
- Subtracting two equal-magnitude infinities that are of the same sign.
- When FPCR.AH is 0, multiplying a zero by an infinity.
- Dividing a zero by a zero.
- Dividing an infinity by an infinity.
- Taking the square root of an operand that is less than zero.

When FPCR.AH is 1, a floating-point instruction multiplying a zero by an infinity:

- Generates an Invalid Operation exception if the instruction is one of the following fused multiply-add instructions and the addend is not a quiet NaN:
- -Advanced SIMD FMLA , FMLAL , FMLAL2 , FMLS , FMLSL , FMLSL2 .
- -SVE FMLA , FMLALB , FMLALT , FMLS , FMLSLB , FMLSLT , BFMLA , BFMLS .
- Generates an Invalid Operation exception otherwise.

If the input is one of: a quiet NaN, an infinity, or a number that overflows the values that can be represented in the output format, and if another exception is not generated to signal the condition, then a conversion from floating-point to either integer or fixed-point format, generates an Invalid Operation exception.

For the signaling compare instructions FCMPE and FCCMPE, if either of the source operands is any type of NaN, the instruction generates an Invalid Operation floating-point exception.

If FPCR.AH is 1, for FMAX (vector), FMAX (scalar), FMAXP (scalar), FMAXP (vector), FMAXV, FMIN (vector), FMIN (scalar), FMINP (scalar), FMINP (vector), FMINV, BFMAX, and BFMIN, if either input is any type of NaN, then an Invalid Operation floating-point exception is generated.

## A1.5.9.8 Handling floating-point exceptions

If an implementation supports synchronous exception generation for floating-point exceptions, the synchronous exceptions generated by the floating-point exception traps are taken to the lowest Exception level that can handle such an exception and that is not at a lower Exception level than where the exception was generated.

If an implementation supports synchronous exception generation for floating-point exceptions in AArch64 state, all of the following apply:

- The registers that are presented to the exception handler are consistent with the state of the PE immediately before the instruction that caused the exception, except that an implementation is permitted to not restore the cumulative floating-point exception bits in the event of such an exception.
- When the execution of separate operations in separate SIMD elements causes multiple floating-point exceptions, the ESR\_ELx reports one exception associated with one element that the instruction uses. The architecture does not specify which element is reported.

The AArch64.FPTrappedException() and FPProcessException() pseudocode functions describe the handling of trapped floating-point exceptions generated in AArch64 state.

## A1.5.9.9 Combinations of floating-point exceptions

More than one floating-point exception might occur on the same operation. The architecture permits only the following combinations of floating-point exceptions:

- Overflow with Inexact.
- Underflow with Inexact.
- If FPCR.AH is 0, Input Denormal with one or more of the other floating-point exception types.
- If FPCR.AH is 1, Input Denormal with Inexact, Underflow, or Overflow.

If two floating-point exceptions occur on the same operation, the Input Denormal exception is treated as highest priority and the Inexact exception is treated as lowest priority.

Some floating-point instructions specify more than one floating-point operation, this is indicated by the pseudocode descriptions of the instruction. In these cases, it is possible for one instruction to generate multiple exceptions. Multiple exceptions from one instruction are prioritized as follows:

- If an exception generating operation outputs a result that is used by a second exception generating operation, the exception generated by the operation that outputs the result is treated as higher priority than the exception generated by the second operation that uses the result.
- If exception generating operations do not use the outputs of other exception generating operations, it is CONSTRAINED UNPREDICTABLE which floating-point exception is treated as higher priority. The exception prioritized might differ between different instances of the same two floating-point exceptions being generated on the same operation during execution of the instruction.
- Atrapped Underflow exception has priority over a trapped Inexact exception.

If none of the floating-point exceptions caused by an operation is trapped, any floating-point exception that occurs causes the associated cumulative exception flag bit in the FPSR to be set to 1.

When FPCR.AH is 1, if the result of a floating-point operation is a denormalized number that is flushed to zero, both an untrapped Underflow floating-point exception and an Inexact floating-point exception are generated, which always sets the cumulative Underflow exception flag FPSR.UFC to 1 regardless of whether the Inexact floating-point exception is trapped. Otherwise, when a trapped floating-point exception is taken, it is IMPLEMENTATION DEFINED whether the FPSR is restored to the value it had immediately before the instruction that generated the trapped floating-point exception. If the IMPLEMENTATION DEFINED choice is that the FPSR is not restored, it is CONSTRAINED UNPREDICTABLE which trapped floating-point exceptions, if any, are indicated by the corresponding FPSR cumulative exception flag bits being set to 1.

When a trapped floating-point exception is taken, then in the ESR\_ELx, all of the following apply:

- The highest priority trapped floating-point exception has a floating-point exception trapped bit set to 1.
- If any other untrapped floating-point exceptions are generated by the same operation, each untrapped exception has a floating-point exception trapped bit set to 0. This applies to both higher priority and lower priority untrapped floating-point exceptions.

- If any lower priority trapped floating-point exceptions are generated by the same operation, for each exception, it is CONSTRAINED UNPREDICTABLE whether the floating-point exception trapped bit is set to 1.

The architectural requirements for floating-point exception prioritization apply only to multiple floating-point exceptions generated on the same element of an Advanced SIMD, SVE or SME operation. For trapped floating-point exceptions from Advanced SIMD, SVE or SME instructions, the architecture does not define the floating-point exception prioritization between different elements of the instruction.

## A1.5.10 Alternate BFloat16 behaviors

The behaviors in this section apply to the following instructions:

- Advanced SIMD&amp;FP: BFCVT , BFCVTN , BFCVTN2 , BFMLALB , BFMLALT .
- SVE: BFCVT , BFCVTNT , BFMLALB , BFMLALT , BFMLSLB , BFMLSLT .
- SME: BFCVT (single-precision to BFloat16), BFCVTN .

Table A1-6 and Table A1-7 describe when these instructions are legal.

When FPCR.AH is 1, the instructions:

- Produce the expected IEEE 754 default result but do not update the FPSR cumulative exception flag bits.
- Disable trapped floating-point exceptions, as if FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} are all 0.
- Use Round to Nearest Even, ignoring FPCR.RMode.
- Flush denormalized inputs and outputs to zero, as if FPCR.{FZ, FIZ} is {1, 1}.

## A1.5.11 BFloat16 behaviors for instructions that compute sum-of-products

The behaviors in this section apply to the following instructions:

- Advanced SIMD: BFDOT and BFMMLA .
- SVE: BFDOT and BFMMLA .
- SME: BFMOPA (widening) and BFMOPS (widening), and SME2 BFDOT and BFVDOT .

Table A1-6 and Table A1-7 describe when these instructions are legal.

## When FPCR.EBF is 0, the instructions:

- Perform unfused two-way sum-of-products for each pair of adjacent BFloat16 elements in the source vectors, with rounding of all intermediate products and sums.
- Ignore FPCR.RMode and use non-IEEE 754 Round to Odd behavior. See Round to Odd.
- Flush denormalized inputs and outputs to zero, as if FPCR.{FZ, FIZ} is {1, 1}.
- Disable alternative floating-point behaviors, as if FPCR.AH is 0.

## When FPCR.EBF is 1, the instructions:

- Perform a fused two-way sum-of-products for each pair of adjacent BFloat16 elements in the source vectors, without rounding of the intermediate products, but rounding the single-precision sum before addition to the single-precision accumulator element.
- Honor FPCR.RMode, supporting all four IEEE 754 rounding modes.
- Honor FPCR.{FZ, FIZ}.
- Honor FPCR.AH.

## Regardless of the value of FPCR.EBF, the instructions:

- Produce the expected IEEE 754 single-precision default result but do not update the FPSR cumulative exception flag bits.
- Disable trapped floating-point exceptions, as if FPCR.{IDE, IXE, UFE, OFE, DZE, IOE} are all 0.

- Generate an intermediate sum-of-products of the same infinity when there are infinite products all with the same sign.
- Generate an intermediate sum-of-products that is a Default NaN when any of the following are true:
- -Any multiplier input is a NaN.
- -Any product is infinity x 0.0.
- -Both products are infinity of differing signs.
- Generate a Default NaN, as if FPCR.DN is 1.