## E1.3 Advanced SIMD and floating-point instructions

In general, the architecture requires implementation of Advanced SIMD and floating-point instructions in the T32 and A32 instruction sets, but see Implications of not including Advanced SIMD and floating-point support.

The Advanced SIMD instructions perform packed Single Instruction Multiple Data (SIMD) operations, on either integer or single-precision floating-point operands. The floating-point instructions perform single-precision or double-precision scalar floating-point operations. When FEAT\_FP16 is implemented, half-precision floating-point can also be used for data processing.

These instructions permit floating-point exceptions , such as Overflow or Divide by Zero, to be handled without trapping. When handled in this way, a floating-point exception causes a cumulative status register bit to be set to 1 and a default result to be produced by the operation. The architecture also optionally supports the trapping of floating-point exceptions. For more information about floating-point exceptions, see Floating-point exceptions and exception traps.

The Advanced SIMD and floating-point instructions also provide the following conversion functions:

- Between half-precision floating-point and single-precision floating point, in both directions.
- From double-precision, floating-point to single-precision floating point or integer.
- When FEAT\_AA32BF16 is implemented, between single-precision floating-point and BFloat16 floating-point.

Some Advanced SIMD instructions support polynomial arithmetic over {0, 1}, as described in Polynomial arithmetic over {0, 1}.

For system level information about the Advanced SIMD and floating-point implementation, see Advanced SIMD and floating-point support.

The following sections give more information about the Advanced SIMD and floating-point instructions:

- Floating-point standards, and terminology.
- The SIMD and floating-point register file.
- Data types supported by the Advanced SIMD implementation.
- Advanced SIMD and floating-point System registers.
- Floating-point data types and arithmetic.
- Flushing denormalized numbers to zero.
- Floating-point exceptions and exception traps.
- Controls of Advanced SIMD operation that do not apply to floating-point operation.
- Implications of not including Advanced SIMD and floating-point support.
- Pseudocode description of floating-point operations.

## E1.3.1 The SIMD and floating-point register file

The Advanced SIMD and floating-point instructions use the same register file, which comprises 32 registers. This is distinct from the register file that holds the general-purpose registers and the PC.

The Advanced SIMD and floating-point views of the register file are different. The following sections describe these different views. Figure E1-1 shows the views of the register file, and the way the word, doubleword, and quadword registers overlap.

## E1.3.1.1 Advanced SIMD views of the register file

Advanced SIMD can view this register file as:

- Sixteen 128-bit quadword registers, Q0-Q15 .
- Thirty-two 64-bit doubleword registers, D0-D31 .

These views can be used simultaneously. For example, a program might hold 64-bit vectors in D0 and D1 and a 128-bit vector in Q1 .

## E1.3.1.2 Floating-point views of the register file

The Advanced SIMD and floating-point register file consists of thirty-two doubleword registers, which can be viewed as:

- Thirty-two 64-bit doubleword registers, D0-D31 . This view is also available to Advanced SIMD instructions.
- Thirty-two 32-bit single word registers, S0-S31 . Only half of the set is accessible in this view.

Note In AArch32 state, half-precision floating point values are always represented using the bottom 16 bits of a single word register, S0-S31 . When a half-precision value is written to a single word register, the top 16 bits of that register are set to 0.

The two views can be used simultaneously.

## E1.3.1.3 SIMD and Floating-point register file mapping onto registers

Figure E1-1 shows the different views of the SIMD and floating-point register file, and the relationship between them.

Figure E1-1 SIMD and floating-point register file, AArch32 operation

<!-- image -->

| S0-S31              | D0-D31                          | Q0-Q15             |
|---------------------|---------------------------------|--------------------|
| Floating-point only | Floating-point or Advanced SIMD | Advanced SIMD only |
| S0 S1 S2 S3         | D0 D1                           | Q0                 |
| S4 S5 S6            | D2                              | Q1                 |
| S7 S28 S29          | D3                              |                    |
| S30 S31             | D14 D15                         | Q7                 |
|                     | D16                             |                    |
|                     | D17                             |                    |
|                     | D30                             | Q8                 |
|                     |                                 | Q15                |
|                     | D31                             |                    |

The mapping between the registers is as follows:

- S&lt;2n&gt; maps to the least significant half of D&lt;n&gt;.
- S&lt;2n+1&gt; maps to the most significant half of D&lt;n&gt; .
- D&lt;2n&gt; maps to the least significant half of Q&lt;n&gt; .
- D&lt;2n+1&gt; maps to the most significant half of Q&lt;n&gt; .

For example, software can access the least significant half of the elements of a vector in Q6 by referring to D12 , and the most significant half of the elements by referring to D13 .

## E1.3.1.4 Pseudocode description of the SIMD and Floating-point register file

The functions \_Dclone , S[] , and D[] provide the S0 -S31 , D0 -D31 , and Q0 -Q15 views of the Advanced SIMD and floating-point registers:

The Din[] function returns a doubleword register from the \_Dclone[] copy of the SIMD and Floating-point register file, and the Qin[] function returns a quadword register from that register file.

Note

The CheckAdvSIMDEnabled() function copies the D[] register file to \_Dclone[] , see Pseudocode description of enabling SIMD and floating-point functionality.

## E1.3.2 Data types supported by the Advanced SIMD implementation

Advanced SIMD instructions can operate on integer and floating-point data, and the implementation defines a set of data types that support the required data formats. Advanced SIMD vector formats in AArch32 state describes these formats.

## E1.3.2.1 Advanced SIMD vectors

In an implementation that includes support for Advanced SIMD operation, a register can hold one or more packed elements, all of the same size and type. The combination of a register and a data type describes a vector of elements. The vector is considered to be an array of elements of the data type specified in the instruction. The number of elements in the vector is implied by the size of the data elements and the size of the register.

Vector indices are in the range 0 to (number of elements - 1). An index of 0 refers to the least significant end of the vector. In Advanced SIMD vector formats in AArch32 state, Figure A1-3 shows the Advanced SIMD vector formats.

## E1.3.2.1.1 Pseudocode description of Advanced SIMD vectors

The pseudocode function Elem[] accesses the element of a specified index and size in a vector.

## E1.3.3 Advanced SIMD and floating-point System registers

The Advanced SIMD and floating-point instructions have a shared register space for System registers. The only register in this space that is accessible at the Application level is the FPSCR.

Writes to the FPSCR can have side-effects on various aspects of PE operation. All of these side-effects are synchronous to the FPSCR write. This means they are guaranteed not to be visible to earlier instructions in the Execution stream, and they are guaranteed to be visible to later instructions in the Execution stream.

See Advanced SIMD and floating-point System registers for the system level view of the registers.

These registers can be described as the SIMD and floating-point System registers .

## E1.3.4 Floating-point data types and arithmetic

The T32 and A32 floating-point instructions support single-precision (32-bit) and double-precision (64-bit) data types and arithmetic as defined by the IEEE 754 floating-point standard. They also support the half-precision (16-bit) floating-point data type for data storage, by supporting conversions between single-precision and half-precision data types. When FEAT\_FP16 is implemented, it also supports the half-precision floating-point data type for data processing operations. When FEAT\_AA32BF16 is implemented, it also supports the BFloat16 floating-point storage format.

Arm standard floating-point arithmetic means IEEE 754 floating-point arithmetic with the restrictions described in Floating-point support, including supporting only the input and output values described in Arm standard floating-point input and output values.

The AArch32 Advanced SIMD instructions support single-precision and, when FEAT\_FP16 is implemented, half-precision Arm standard floating-point arithmetic.

The following sections describe the Advanced SIMD and floating-point formats:

- Half-precision floating-point formats.
- Single-precision floating-point format.

- Double-precision floating-point format.
- BFloat16 floating-point format.

The following sections describe features of Advanced SIMD and floating-point processing:

- Flushing denormalized numbers to zero.
- NaN handling and the Default NaN.

## E1.3.5 Flushing denormalized numbers to zero

Calculations involving denormalized numbers and Underflow exceptions can reduce the performance of floating-point processing. For many algorithms, replacing the denormalized operands and Intermediate results with zeros can recover this performance, without significantly affecting the accuracy of the final result. Arm floating-point implementations allow denormalized numbers to be flushed to zero to permit this optimization. If a number satisfies the condition 0 &lt; Abs(result) &lt; MinNorm , it is treated as a denormalized number.

MinNorm is defined as follows:

- For half-precision numbers, MinNorm is 2 -14.
- For single-precision and BFloat16 numbers, MinNorm is 2 -126 .
- For double-precision numbers, MinNorm is 2 -1022 .

Flushing denormals to zero is incompatible with the IEEE 754 standard, and must not be used when IEEE 754 compatibility is a requirement. Enabling flushing of denormals to zero must be done with care. Although it can improve performance on some algorithms, there are significant limitations on its use. These are application-dependent:

- On many algorithms, it has no noticeable effect, because the algorithm does not usually process denormalized numbers.
- On other algorithms, it can cause exceptions to occur and can seriously reduce the accuracy of the results of the algorithm.

## E1.3.5.1 Flushing denormalized inputs to zero

If flushing denormalized inputs to zero is enabled for an instruction and a data type, and an input to that instruction is a denormalized number of that data type, the input operand is flushed to zero, and its sign bit is not changed.

If a floating-point operation has an input denormalized number that is flushed to zero, for all purposes within the instruction other than calculating Input Denormal floating-point exceptions, all inputs that are denormalized numbers are treated as though they were zero with the same sign as the input.

For Advanced SIMD and floating-point instructions, other than FABS and FNEG , that process half-precision inputs, flushing denormalized inputs to zero can be controlled as follows:

- If FPSCR.FZ16 is 0, denormalized half-precision inputs are not flushed to zero.
- If FPSCR.FZ16 is 1, flushing denormalized inputs to zero occurs as follows:
- -If an instruction does not convert a half-precision input to a higher precision output, all input denormalized numbers are flushed to zero.
- -If an instruction converts a half-precision input to a higher precision output, input denormalized numbers are not flushed to zero.

For Advanced SIMD and scalar floating-point instructions, other than FABS and FNEG , that process single-precision, or double-precision inputs, flushing denormalized inputs to zero can be controlled as follows:

- If FPSCR.FZ is 0, flushing denormalized inputs to zero occurs as follows:
- -For Advanced SIMD floating-point instructions, all single-precision and double-precision inputs that are denormalized numbers are flushed to zero.
- -For scalar floating-point instructions, single-precision and double-precision inputs that are denormalized numbers are not flushed to zero.

- If FPSCR.FZ is 1, for all T32 and A32 instructions, single-precision and double-precision inputs that are denormalized numbers are flushed to zero.

If FEAT\_AA32BF16 is implemented, for Advanced SIMD and scalar floating-point instructions, other than FABS and FNEG , that process BFloat16 inputs, flushing denormalized inputs to zero is treated as follows:

- Instructions that convert from single-precision floating-point values to BFloat16 format flush denormalized inputs to zero.
- For any value of FPSCR.FZ, VDOT (vector), VDOT (by element), and VMMLA instructions flush all BFloat16 inputs that are denormalized numbers to zero.

## E1.3.5.2 Flushing to zero of denormalized numbers as Intermediate results of some BFloat16 instructions

BFloat16 arithmetic instructions VDOT (by element), VDOT (vector), and VMMLA, convert BFloat16 input values to IEEE single-precision format, and calculate N-way dot-products, accumulating the products in single-precision accumulators.

If FEAT\_AA32BF16 is implemented, for Advanced SIMD and floating-point instructions, if a BFloat16 arithmetic instruction processes an Intermediate result that is a single-precision denormalized number, the Intermediate result is unconditionally flushed to zero.

## E1.3.5.3 Flushing denormalized outputs to zero

If flushing denormalized outputs to zero is enabled for an instruction and a data type, and an output from that instruction is a denormalized number of that data type, the output operand is flushed to zero, and its sign bit is not changed.

If a floating-point operation has an output denormalized number that is flushed to zero, for all purposes within the instruction other than calculating floating-point exceptions, all outputs that are denormalized numbers are treated as though they were zero with the same sign as the output.

For Advanced SIMD and floating-point instructions, other than FABS and FNEG , that generate half-precision outputs, flushing denormalized outputs to zero can be controlled as follows:

- If FPSCR.FZ16 is 0, denormalized half-precision outputs are not flushed to zero.
- If FPSCR.FZ16 is 1, flushing denormalized outputs to zero occurs as follows:
- -If the instruction does not convert a half-precision input to a higher precision output, all output denormalized numbers are flushed to zero.
- -If the instruction converts a half-precision input to a higher precision output, output denormalized numbers are not flushed to zero.

For Advanced SIMD and scalar floating-point instructions, other than FABS and FNEG , that process single-precision, or double-precision inputs, flushing denormalized outputs to zero can be controlled as follows:

- If FPSCR.FZ is 0, flushing denormalized outputs to zero occurs as follows:
- -For Advanced SIMD floating-point instructions, all single-precision and double-precision outputs that are denormalized numbers are flushed to zero.
- -For scalar floating-point instructions, single-precision and double-precision outputs that are denormalized numbers are not flushed to zero.
- If FPSCR.FZ is 1, for all T32 and A32 instructions, single-precision and double-precision outputs that are denormalized numbers are flushed to zero.

If FEAT\_AA32BF16 is implemented, for Advanced SIMD and scalar floating-point instructions, other than FABS and FNEG , that generate BFloat16 outputs, flushing denormalized outputs to zero can be controlled as follows:

- BFloat16 arithmetic instructions flush denormalized outputs to zero.
- If FPSCR.FZ is 1, instructions that convert from single-precision floating-point values to BFloat16 format flush denormalized outputs to zero.
- VDOT(vector), VDOT (by element), and VMMLA instructions flush all BFloat16 outputs that are denormalized numbers to zero regardless of the value of FPSCR.FZ.

## E1.3.6 NaN handling and the Default NaN

The IEEE 754 standard defines a NaN as a number with all exponent bits set to 1 and a nonzero number in the mantissa, and specifies that the sign bit of a NaN has no significance.

The Arm architecture additionally defines:

- ABFloat16 NaN, that follows the encoding in BFloat16 floating-point format.
- A Default NaN , compliant with the IEEE 754 standard, that follows the encoding in Table E1-4.

For a Quiet NaN output derived from a signaling NaN operand, the most significant fraction bit is set to 1.

APEis forbidden to generate a NaN whose value is strongly correlated to the values of non-NaN inputs as a speculative result of a floating-point calculation not involving NaN inputs.

## E1.3.6.1 The Default NaN

The Default NaN is encoded as described in Table E1-4.

## Table E1-4 Default NaN encoding

|          | Half-precision, IEEE format   | Single-precision   | Double-precision   | BFloat16       |
|----------|-------------------------------|--------------------|--------------------|----------------|
| Sign bit | 0                             | 0                  | 0                  | 0              |
| Exponent | 0x1F                          | 0xFF               | 0x7FF              | 0xFF           |
| Fraction | Bit[9] == 1,                  | Bit[22] == 1,      | Bit[51] == 1,      | Bit[6] == 1,   |
|          | bits[8:0] == 0                | bits[21:0] == 0    | bits[50:0] == 0    | bits[5:0] == 0 |

If FPSCR.DN is 1, for Advanced SIMD and floating-point instructions other than FABS , FMAX* , FMIN* and FNEG , if any input to a floating-point operation performed by the instruction is a NaN, the output of the floating-point operation is the Default NaN.

For FABS , FNEG , FMAX* , and FMIN* , Default NaN behavior is explained in the instruction description.

If FPSCR.DN is 0, for floating-point processing the Default NaN is not used for NaN propagation.

If VDOT (vector), VDOT (by element), and VMMLA instructions generate a NaN, the NaN is the default NaN. regardless of the setting of FPSCR.DN.

If a floating-point instruction performs a floating-point operation, and that instruction generates an untrapped Invalid Operation floating-point exception for a reason other than one of the inputs being a signaling NaN, the output is the Default NaN.

## E1.3.6.2 NaN handling

The IEE 754 standard does not specify which input NaN is used as the output NaN. Therefore, where the Arm architecture specifies which input NaN to use, this is an addition to the requirements in the IEEE 754 standard.

Depending on the operation, the exact value of a derived Quiet NaN output might have both a different sign and a different number of fraction bits from its source. See instruction descriptions for details.

## E1.3.6.3 NaN propagation

If an output NaN is derived from one of the operands, how the input NaN propagates to the output depends on the instruction and the number of operands.

If an output NaN is derived from an input NaN and if the size of the output format is the same as the input format, then all of the following apply:

- If the input NaN is a Quiet NaN, the output NaN is the same as the input NaN.

- If the input NaN is a signaling NaN, the output NaN is derived as follows:
- -If the handling of a signaling NaN by the instruction generates an Invalid Operation exception, the output NaN is the quieted version of the input NaN.
- -If the handling of a signaling NaN by the instruction does not generate an Invalid Operation exception, the output NaN is the same as the input NaN. This case applies for FABS, FNEG, and FTSSEL instructions.

If an output NaN is derived from an input NaN and if the size of the output format is larger than the input format, all of the following apply:

- If the input NaN is a Quiet NaN, the output NaN is the same as the input NaN except that the mantissa is zero-extended in the low-order bit to fit the output format, and the exponent field is set to all ones.
- If the input NaN is a signaling NaN, the output NaN is the quieted version of the input NaN, except that the mantissa is zero-extended in the low-order bits and the exponent field is set to all ones.

If an output NaN is derived from an input NaN and if the size of the output format is smaller than the input format, all of the following apply:

- If the input NaN is a Quiet NaN, the output NaN is the same as the input NaN except that the mantissa is truncated in the lower-order bits to fit the output format, and the exponent field is set to all ones.
- If the input NaN is a signaling NaN, the output NaN is the quieted version of the input NaN except that the mantissa is truncated in the lower-order bits to fit the output format, and the exponent field is set to all ones.

For the following descriptions, when an operand is described as first this relates to the left-to-right ordering of the arguments of the pseudocode function that describes the operation.

If FPSCR.DN is 0, for Advanced SIMD, floating-point, or BFloat16 instructions that perform a floating-point operation, other than FABS , FNEG , FMAX* , and FMIN* , NaN outputs that derive from NaN inputs are derived as follows:

- If all of the following apply, an instruction outputs a quiet NaN derived from the first signaling NaN operand:
- -At least one operand is a signaling NaN.
- -The instruction is not trapped.
- If all of the following apply, an instruction outputs a Quiet NaN derived from the first NaN operand:
- -At least one operand is a NaN, but none of the operands is a signaling NaN.
- -The instruction is not trapped.

If an output NaN is derived from an input NaN, the pseudocode functions FPAbs() , and FPNeg() can change the sign of the NaN,

## E1.3.7 Rounding

The rounding mode specifies how the exact result of a floating-point operation is rounded to a value in the destination format.

The rounding mode is either determined by the rounding mode control field FPSCR.RMode or by the instruction.

The rounding mode control field FPSCR.RMode can select the following rounding modes:

- Round to Nearest (RN) mode.
- Round towards Plus Infinity (RP) mode.
- Round towards Minus Infinity (RM) mode.
- Round towards Zero (RZ) mode.

The following two additional rounding modes are not selected by FPSCR.RMode, but are used by some instructions:

- Round to Odd mode.
- Round to Nearest with ties to away mode.

## E1.3.7.1 Round to Nearest mode

Round to Nearest rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format as follows:

- If the value before rounding has an absolute value that is too large to represent in the output format, the rounded value is an Infinity. The sign of the rounded value is the same as the sign of the value before rounding.
- If the value before rounding has an absolute value that is not too large to represent in the output format, the result is calculated as follows:
- -If the two nearest floating-point numbers bracketing the value before rounding are equally near, the result is the number with an even least significant digit.
- -If the two nearest floating-point numbers bracketing the value before rounding are not equally near, the result is the floating-point number nearest to the value before rounding.

Advanced SIMD arithmetic always uses the Round to Nearest setting, regardless of the value of the RMode bits.

## E1.3.7.2 Round towards Plus Infinity mode

Round towards Plus Infinity rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is the floating-point number in the output format that is closest to and not less than the value before rounding. The result can be plus infinity.

## E1.3.7.3 Round towards Minus Infinity mode

Round towards Minus Infinity rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is the number in the output format that is closest to and not greater than the value before rounding. The result can be minus infinity.

## E1.3.7.4 Round towards Zero mode

Round towards Zero rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format. The result is the floating-point number in the output format that is closest to and not greater in absolute value than the value before rounding.

## E1.3.7.5 Round to Nearest with Ties to Away

Round to Nearest with Ties to Away rounding mode is used by the VCVTA (Advanced SIMD), VCVTA (floating-point), VRINTA (Advanced SIMD), and VRINTA (floating-point) instructions.

Round to Nearest with Ties to Away rounding mode rounds the exact result of a floating-point operation to a value that is representable in the destination format as follows:

- If the value before rounding has an absolute value that is too large to represent in the output format, the rounded value is an Infinity, the sign of the rounded value is the same as the sign of the value before rounding.
- If the value before rounding has an absolute value that is not too large to represent in the output format, the result is calculated as follows:
- -If the two nearest floating-point numbers bracketing the value before rounding are equally near, the result is the larger number.
- -If the two nearest floating-point numbers bracketing the value before rounding are not equally near, the result is the floating-point number nearest to the value before rounding.

## E1.3.7.6 Round to Odd mode

Round to Odd mode is not defined by IEEE 754.

For BFloat16 instructions, if an intermediate format has at least two more bits of precision than the result format, Round to Odd mode is used and operates as follows:

- If the rounded value is inexact, the least significant bit of the fraction is set to 1.
- If the value is too large to represent in the single-precision format, the rounded value is a single-precision Infinity, the sign of the rounded value is the same as the sign of the value before rounding.

## E1.3.8 Floating-point exceptions and exception traps

Execution of a floating-point instruction, or execution of an Advanced SIMD instruction that performs floating-point operations, can generate an exceptional condition, called a floating-point exception .

Note

An Advanced SIMD instruction that operates on floating-point values can perform multiple floating-point operations. Therefore, this section describes the handling of a floating-point exception on an operation , rather than on an instruction .

The architecture does not support asynchronous reporting of floating-point exceptions.

For each of the following floating-point exceptions, it is IMPLEMENTATION DEFINED whether an implementation includes synchronous exception generation:

- Input Denormal.
- Inexact.
- Underflow.
- Overflow.
- Divide by Zero.
- Invalid Operation.

If an implementation does not support synchronous exception generation from a floating-point exception, then that synchronous exception is never generated, and all statements about synchronous exception generation from that floating-point exception do not apply to the implementation.

If an implementation supports synchronous exception generation for a floating-point exception, then the registers that are presented to the exception handler are consistent with the state of the PE immediately before the instruction that caused the exception.

On return from a synchronous floating-point exception, software might not restore the cumulative exception flags.

Trapped floating-point exceptions are taken to the following levels:

- If a trapped floating-point exception occurs at EL0, the exception level it is taken to is as follows:
- -If EL2 is using AArch32 and HCR.TGE is 1, the exception is taken to EL2.
- -If EL2 is using AArch64 and HCR\_EL2.TGE is 1, the exception is taken to EL2
- -Otherwise, the exception is taken to EL1
- If a trapped floating-point exception occurs at EL1, it is taken to EL1.
- If a trapped floating-point exception occurs at EL2, it is taken to EL2.
- If a trapped floating-point exception occurs at EL3, it is taken to EL3.

If a trapped floating-point exception is taken to an Exception level that is using AArch64, then it is reported in the ELR\_ELx for the target Exception level, as described in Exception entry.

If the exception is taken to an Exception level that is using AArch32, then it is taken as an Undefined Instruction exception, see Undefined Instruction exception. The FPEXC identifies the floating-point exceptions that occurred since the corresponding status bits in that register were last set to 0.

## E1.3.8.1 Input Denormal exceptions

The cumulative floating-point exception bit FPSCR.IDC, and the trap enable bit FPSCR.IDE both relate to Input Denormal exceptions.

If a single-precision or double-precision floating-point input is flushed to zero, an Input Denormal exception is generated.

If a half-precision floating-point value is flushed to zero, an Input Denormal exception is not generated.

## E1.3.8.2 Inexact exceptions

The cumulative floating-point exception bit FPSCR.IXC, and the trap enable bit FPSCR.IXE both relate to Inexact exceptions.

If a denormalized output is flushed to zero, an Inexact exception is not generated.

If a result is not flushed to zero, and the result does not equal the result computed with unbounded exponent range and unbounded precision, then an Inexact exception is generated.

## E1.3.8.3 Underflow exceptions

The cumulative floating-point exception bit FPSR.UFC, and the trap enable bit FPSCR.UFE both relate to Underflow exceptions.

For the purpose of Underflow floating-point exception generation, a denormalized number is detected before rounding is applied.

If the result of a floating-point operation is a denormalized number that is not flushed to zero, then the Underflow exception is generated as follows:

- If the result is exact, an Underflow floating-point exception is generated only if FPSCR.UFE is 1.
- If the result is inexact, an Underflow floating-point exception is always generated.

If the result of a floating-point operation is a denormalized number that is flushed to zero, then the Underflow floating-point exception is generated. The Underflow exception is not trapped regardless of the value of FPSCR.UFE.

## E1.3.8.4 Overflow exceptions

The cumulative floating-point exception bit FPSCR.OFC, and the trap enable bit FPSCR.OFE both relate to Overflow exceptions.

If the output of an instruction rounded with an unbounded exponent is greater than the maximum normalized number for the output precision, an Overflow exception is generated.

If an untrapped Overflow exception is generated, the result is determined by the rounding mode and the sign of the result before rounding as follows:

- Round to Nearest carries all overflows to infinity with the sign of the result before rounding.
- Round towards Plus Infinity carries negative overflows to the most negative finite number of the output precision, and carries positive overflows to plus infinity.
- Round towards Minus Infinity carries positive overflows to the largest finite number of the output precision, and carries negative overflows to minus infinity.
- Round towards Zero carries all overflows to the output precision's largest finite number with the sign of the result before rounding.

## E1.3.8.5 Divide by Zero exceptions

The cumulative floating-point exception bit FPSCR.DZC, and the trap enable bit FPSCR.DZE both relate to Divide by Zero exceptions.

If a floating-point operation divides a finite nonzero number by zero, a Divide by Zero exception is generated.

For the purpose of Divide by Zero exception generation, testing for zero occurs after flushing of denormalized numbers to zero.

Adenormalized dividend that is flushed to zero is treated as zero and prevents Divide by Zero from occurring.

If the dividend is a finite nonzero, normalized number, and the divisor is a denormalized number, the divisor is treated as zero and causes Divide by Zero to occur.

For the reciprocal and reciprocal square root estimate functions, the dividend is assumed to be +1.0. This means that a zero or denormalized operand to these functions causes generation of a Divide by Zero floating-point exception.

If a floating-point operation divides a finite nonzero number by zero, and the Divide by Zero exception is untrapped, the result is a correctly signed infinity.

## E1.3.8.6 Invalid Operation exceptions

The cumulative floating-point exception bit FPSCR.IOC, and the trap enable bit FPSCR.IOE both relate to Invalid Operation exceptions.

For any floating-point instruction that performs a floating-point operation, if any of the following apply, the instruction generates an Invalid Operation exception:

- At least one operand is a signaling NaN, and the instruction is not FABS or FNEG .
- Subtracting two equal-magnitude infinities that are of the same sign.
- Multiplying a zero by an infinity.
- Dividing a zero by a zero.
- Dividing an infinity by an infinity.
- Taking the square root of an operand that is less than zero.

For the purpose of Invalid Operation Exception generation, testing for zero occurs after flushing of denormalized numbers to zero. So a denormalized input that is flushed to zero is treated as zero.

If the input is one of: a Quiet NaN, an infinity, or a number that overflows the values that can be represented in the output format, and if another exception is not generated to signal the condition, then a conversion from floating-point to either integer or fixed-point format, generates an Invalid Operation exception.

For the signaling compare instructions FCMPE and FCCMPE, if either of the source operands is any type of NaN, the instruction generates an Invalid Operation floating-point exception.

## E1.3.8.7 Floating-point exception traps

For Advanced SIMD instructions, and for floating-point instructions when floating-point exception trapping is not supported, these are non-trapping exceptions and the data-processing instructions do not generate any trapped exceptions.

For floating-point instructions when floating-point exception trapping is supported:

- The floating-point exceptions can be trapped, by setting trap enable bits in the FPSCR, see Floating-point exceptions and exception traps, and:
- -When a trap is not enabled the corresponding floating-point exception updates the corresponding FPSCR cumulative bit, but does not generate an exception.
- -When a trap is enabled the corresponding floating-point exception does not update the FPSCR, but generates an exception. In this case, bits in the FPEXC indicate which floating-point exceptions have occurred.
- The definition of the Underflow floating-point exception is different in the trapped and cumulative exception cases. In the trapped case, the definition is:
- -The trapped Underflow floating-point exception occurs if the absolute value of the result of an operation, produced before rounding, is less than the minimum positive normalized number for the destination precision, regardless of whether the rounded result is inexact.
- As with cumulative exceptions, higher priority trapped exceptions can prevent lower priority exceptions from occurring, as described in Combinations of floating-point exceptions.
- For Invalid Operation floating-point exceptions, for details of which Quiet NaN is produced as the default result, see NaN handling and the Default NaN.
- For Overflow floating-point exceptions, the sign bit of the default result is determined normally for the overflowing operation.
- For Divide by Zero floating-point exceptions, the sign bit of the default result is determined normally for a division. This means it is the exclusive-OR of the sign bits of the two operands.

Table E1-5 shows the results of untrapped floating-point exceptions. That table uses the following abbreviations:

| MaxNorm   | The maximum normalized number of the destination precision.             |
|-----------|-------------------------------------------------------------------------|
| RM        | Round towards Minus Infinity mode, as defined in the IEEE 754 standard. |
| RN        | Round to Nearest mode, as defined in the IEEE 754 standard.             |

RP

Round towards Plus Infinity mode, as defined in the IEEE 754 standard.

RZ

Round towards Zero mode, as defined in the IEEE 754 standard.

For more information about the IEEE 754 descriptions of the rounding modes, see Floating-point standards, and terminology.

## Table E1-5 Results of untrapped floating-point exceptions

| Exception type         | Default result for positive sign   | Default result for positive sign   | Default result for negative sign   | Default result for negative sign   |
|------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| IOC, Invalid Operation | Quiet NaN                          |                                    | Quiet NaN                          |                                    |
| DZC, Divide by Zero    | +infinity                          |                                    | -infinity                          |                                    |
| OFC, Overflow          | RN, RP: RM, RZ:                    | +infinity +MaxNorm                 | RN, RM: RP, RZ:                    | -infinity -MaxNorm                 |
| UFC, Underflow         | Normal rounded result              | Normal rounded result              | Normal rounded result              | Normal rounded result              |
| IXC, Inexact           | Normal rounded result              | Normal rounded result              | Normal rounded result              | Normal rounded result              |
| IDC, Input Denormal    | Normal rounded result              | Normal rounded result              | Normal rounded result              | Normal rounded result              |

## E1.3.8.8 Combinations of floating-point exceptions

Many pseudocode functions perform floating-point operations , including FixedToFP() , FPAdd() , FPCompare() , FPCompareEQ() , FPCompareGE() , FPCompareGT() , FPDiv() , FPMax() , FPMin() , FPMul() , FPMulAdd() , FPRecipEstimate() , FPRecipStep() , FPRSqrtEstimate() , FPRSqrtStep() , FPSqrt() , FPSub() , and FPToFixed() . All of these operations can generate floating-point exceptions.

Note

FPAbs() and FPNeg() are not classified as floating-point operations because:

- They cannot generate floating-point exceptions.
- The floating-point operation behavior described in the following sections does not apply to them:
- -Flushing denormalized numbers to zero.
- -NaN handling and the Default NaN.

More than one exception might occur on the same operation. The architecture permits only the following combinations of floating-point exceptions:

- Overflow with Inexact.
- Underflow with Inexact.
- Input Denormal with one or more of the other floating-point exception types.

The priority order of these floating-point exceptions is that the Inexact exception is treated as lowest priority, and the Input Denormal exception is treated as highest priority.

When none of the floating-point exceptions caused by an operation is trapped, any floating-point exception that occurs causes the associated cumulative bit in the FPSCR to be set.

When one or more floating-point exceptions caused by an operation is trapped, the behavior of the instruction depends on the priority of the exceptions:

- If the higher priority floating-point exception is trapped, its trap handler is called. It is IMPLEMENTATION DEFINED whether any information about the lower priority floating-point exception is provided.

Note

Information about the lower priority floating-point exception might be provided in:

- -The FPEXC, if the exception generated by the trap is taken to an Exception level that is using AArch32.
- -The ESR\_ELx.ISS field, if the exception generated by the trap is taken to an Exception level that is using AArch64.

However, information might be provided in another IMPLEMENTATION DEFINED way, for example using an IMPLEMENTATION DEFINED register.

Apart from this, the lower priority floating-point exception is ignored in this case.

- If the higher priority floating-point exception is untrapped, its cumulative bit is set to 1 and its default result is evaluated. Then the lower priority floating-point exception is handled normally, using this default result.

Some floating-point instructions specify more than one floating-point operation, as indicated by the pseudocode descriptions of the instruction. In such cases, a floating-point exception on one operation is treated as higher priority than a floating-point exception on another operation if the occurrence of the second floating-point exception depends on the result of the first operation. Otherwise, it is CONSTRAINED UNPREDICTABLE which floating-point exception is treated as higher priority.

For example, a VMLA.F32 instruction specifies a floating-point multiplication followed by a floating-point addition. The addition can generate Overflow, Underflow and Inexact floating-point exceptions, all of which depend on both operands to the addition and so are treated as lower priority than any floating-point exception on the multiplication. The same applies to Invalid Operation floating-point exceptions on the addition caused by adding opposite-signed infinities. The addition can also generate an Input Denormal floating-point exception, caused by the addend being a denormalized number while in Flush-to-zero mode. It is CONSTRAINED UNPREDICTABLE which of an Input Denormal floating-point exception on the addition and a floating-point exception on the multiplication is treated as higher priority, because the occurrence of the Input Denormal floating-point exception does not depend on the result of the multiplication. The same applies to an Invalid Operation floating-point exception on the addition caused by the addend being a signaling NaN.

Note

The VFMA instruction performs a vector addition and a vector multiplication as a single operation. The VFMS instruction performs a vector subtraction and a vector multiplication as a single operation.

## E1.3.9 Controls of Advanced SIMD operation that do not apply to floating-point operation

Earlier architectures permitted implementation of either, both, or neither of the Advanced SIMD and floating-point additions to the base instruction set, and provided some controls that applied to the Advanced SIMD functionality but not to the floating-point functionality. From the introduction of Armv8, Advanced SIMD functionality cannot be separated from floating-point functionality, but in AArch32 state these controls function as they did in earlier architectures. This means they apply only to the following instructions and instruction encodings:

- All instructions with encodings defined in:
- -Advanced SIMD data-processing, for the T32 instruction set.
- -Advanced SIMD data-processing, for the A32 instruction set.
- All instructions with encodings defined in:
- -Advanced SIMD element or structure load/store, for the T32 instruction set.
- -Advanced SIMD element or structure load/store, for the A32 instruction set.
- The form of the VDUP instruction described in VDUP (general-purpose register).
- The byte and halfword forms of the VMOV instructions described in each of:
- -VMOV(general-purpose register to scalar).
- -VMOV(scalar to general-purpose register).

The controls of this functionality are:

- The CPACR.ASEDIS field.
- The HCPTR.TASE field.

In an implementation that supports Advanced SIMD functionality, support for each of these controls is optional:

- If the CPACR.ASEDIS control is not supported then the CPACR.ASEDIS field is RAZ/WI. This is equivalent to the control permitting the execution of Advanced SIMD instructions at EL1 and EL0.
- If the HCPTR.TASE control is not supported then the HCPTR.TASE field is RAZ/WI. This means the HCPTR does not provide a control that can trap Non-secure execution of Advanced SIMD instructions to Hyp mode.

## E1.3.10 Implications of not including Advanced SIMD and floating-point support

In general, the architecture requires the inclusion of the Advanced SIMD and floating-point instructions in all instruction sets. Exceptionally, for implementation targeting specialized markets, Arm might produce or license an Armv8-A implementation that does not provide any support for Advanced SIMD and floating-point instructions. In such an implementation, in AArch32 state:

- Each of the CPACR.{cp10, cp11} fields is RES0.
- The CPACR.ASEDIS bit is RES0.
- Each of the HCPTR.{TASE, TCP10, TCP11} fields is RES1.
- Each of the NSACR.{NSASEDIS, cp10, cp11} fields is RES0.
- The FPEXC register is UNDEFINED.

## E1.3.11 Pseudocode description of floating-point operations

The following subsections contain pseudocode definitions of the floating-point functionality supported by the architecture:

- Generation of specific floating-point values.
- Floating-point negation and absolute value.
- Floating-point value unpacking.
- Floating-point exception and NaN handling.
- Floating-point rounding.
- Selection of Arm standard floating-point arithmetic.
- Floating-point comparisons.
- Floating-point maximum and minimum.
- Floating-point addition and subtraction.
- Floating-point multiplication and division.
- Floating-point fused multiply-add.
- Floating-point reciprocal estimate and step.
- Floating-point square root.
- Floating-point reciprocal square root estimate and step.
- Floating-point conversions.

## E1.3.11.1 Generation of specific floating-point values

The following pseudocode functions generate specific floating-point values. The sign argument is '0' for the positive version and '1' for the negative version:

- FPInfinity() . · FPMaxNormal() . · FPZero() . · FPTwo() . · FPThree() .
- FPDefaultNaN() .

## E1.3.11.2 Floating-point negation and absolute value

The floating-point negation and absolute value operations affect only the sign bit. They do not treat NaN operands specially, nor denormalized number operands when flush-to-zero is selected.

The floating-point negation operation is described by the pseudocode function FPNeg() . The floating-point absolute value operation is described by the pseudocode function FPAbs() .

## E1.3.11.3 Floating-point value unpacking

The FPUnpack() function determines the type of a floating-point number, defined by FPType {} , and its numerical value. It also does flush-to-zero processing on input operands.

## E1.3.11.4 Floating-point exception and NaN handling

The FPProcessException() procedure checks whether a floating-point exception is trapped, and handles it accordingly. The floating-point exception types are defined by FPExc {} .

The FPProcessNaN() function processes a NaN operand, producing the correct result value and generating an Invalid Operation floating-point exception if necessary. The FPProcessNaNs() function performs the standard NaN processing for a two-operand operation. The FPProcessNaNs3() function performs the standard NaN processing for a three-operand operation.

## E1.3.11.5 Floating-point rounding

The FPRound() function rounds and encodes a floating-point result to a specified destination format. This includes processing Overflow, Underflow and Inexact floating-point exceptions and performing flush-to-zero processing on result values.

## E1.3.11.6 Selection of Arm standard floating-point arithmetic

The StandardFPCR() function returns the FPSCR value that selects Arm standard floating-point arithmetic. Most of the arithmetic functions have a Boolean fpscr\_controlled argument that is TRUE for Floating-point operations and FALSE for Advanced SIMD operations, and that selects between using the real FPSCR value and this value.

## E1.3.11.7 Floating-point comparisons

The FPCompare() function compares two floating-point numbers, producing a {N, Z, C, V} Condition flags result as shown in Table E1-6:

## Table E1-6 Effect of a Floating-point comparison on the Condition flags

| Comparison result   |   N |   Z |   C |   V |
|---------------------|-----|-----|-----|-----|
| Equal               |   0 |   1 |   1 |   0 |
| Less than           |   1 |   0 |   0 |   0 |
| Greater than        |   0 |   0 |   1 |   0 |
| Unordered           |   0 |   0 |   1 |   1 |

This result defines the operation of the VCMP floating-point instruction. The VCMP instruction writes these flag values in the FPSCR. After using a VMRS instruction to transfer them to the APSR, they can control conditional execution as shown in Table F1-1.

The FPCompareEQ() , FPCompareGE() , and FPCompareGT() functions describe the operation of Advanced SIMD instructions that perform floating-point comparisons.

## E1.3.11.8 Floating-point maximum and minimum

The FPMax() function returns the maximum of two floating-point numbers. The FPMin() function returns the minimum of two floating-point numbers.

## E1.3.11.9 Floating-point addition and subtraction

The FPAdd() function adds two floating-point numbers. The FPSub() function subtracts one floating-point number from another floating-point number.

## E1.3.11.10 Floating-point multiplication and division

The FPMul() function multiplies two floating-point numbers. The FPDiv() function divides one floating-point number by another floating-point number.

## E1.3.11.11 Floating-point fused multiply-add

The FPMulAdd() function performs a floating-point fused multiply-add.

## E1.3.11.12 Floating-point reciprocal estimate and step

The Advanced SIMD implementation includes instructions that support Newton-Raphson calculation of the reciprocal of a number.

The VRECPE instruction produces the initial estimate of the reciprocal. It uses the pseudocode functions:

- FPRecipEstimate() .
- UnsignedRecipEstimate() .

Table E1-7 shows the results where input values are out of range.

Table E1-7 VRECPE results for out of range inputs

| Number type    | Input Vm[i]               | Result Vd[i]   |
|----------------|---------------------------|----------------|
| Integer        | <= 0x7FFF_FFFF            | 0xFFFF_FFFF    |
| Floating-point | NaN                       | Default NaN    |
| Floating-point | ±0 or denormalized number | ±infinity a    |
| Floating-point | ±infinity                 | ±0             |
| Floating-point | Absolute value >= 2 126   | ±0             |

- a. FPSCR.DZC is set to 1

The Newton-Raphson iteration:

<!-- formula-not-decoded -->

converges to ( 1/d ) if x0 is the result of VRECPE applied to d .

The VRECPS instruction performs a (2 - op1 × op2) calculation and can be used with a multiplication to perform a step of this iteration. The functionality of this instruction is defined by the FPRecipStep() pseudocode function.

Table E1-8 shows the results where input values are out of range.

Table E1-8 VRECPS results for out of range inputs

| Input Vn[i]   | Input Vm[i]   | Result Vd[i]   |
|---------------|---------------|----------------|
| Any NaN       | -             | Default NaN    |
| -             | Any NaN       | Default NaN    |

| Input Vn[i]                 | Input Vm[i]                 |   Result Vd[i] |
|-----------------------------|-----------------------------|----------------|
| ±0.0 or denormalized number | ±infinity                   |              2 |
| ±infinity                   | ±0.0 or denormalized number |              2 |

## E1.3.11.13 Floating-point square root

The FPSqrt() function returns the square root of a floating-point number.

## E1.3.11.14 Floating-point reciprocal square root estimate and step

The Advanced SIMD implementation includes instructions that support Newton-Raphson calculation of the reciprocal of the square root of a number.

The VRSQRTE instruction produces the initial estimate of the reciprocal of the square root. It uses the pseudocode functions:

- FPRSqrtEstimate() .
- UnsignedRSqrtEstimate() .

Table E1-9 shows the results where input values are out of range.

## Table E1-9 VRSQRTE results for out of range inputs

| Number type    | Input Vm[i]                          | Result Vd[i]   |
|----------------|--------------------------------------|----------------|
| Integer        | <= 0x3FFF_FFFF                       | 0xFFFF_FFFF    |
| Floating-point | NaN, -(normalized number), -infinity | Default NaN    |
| Floating-point | -0 or -(denormalized number)         | - infinity a   |
| Floating-point | +0 or +(denormalized number)         | +infinity a    |
| Floating-point | +infinity                            | +0             |

The Newton-Raphson iteration:

<!-- formula-not-decoded -->

converges to ( 1/ √ d ) if x0 is the result of VRSQRTE applied to d .

The VRSQRTS instruction performs a (3 - op1 × op2)/2 calculation and can be used with two multiplications to perform a step of this iteration. The functionality of this instruction is defined by the FPRSqrtStep() pseudocode function.

Table E1-10 shows the results where input values are out of range.

## Table E1-10 VRSQRTS results for out of range inputs

| Input Vn[i]                 | Input Vm[i]                 | Result Vd[i]   |
|-----------------------------|-----------------------------|----------------|
| Any NaN                     | -                           | Default NaN    |
| -                           | Any NaN                     | Default NaN    |
| ±0.0 or denormalized number | ±infinity                   | 1.5            |
| ±infinity                   | ±0.0 or denormalized number | 1.5            |

FPRSqrtStep() calls the FPHalvedSub() pseudocode function.

## E1.3.11.15 Floating-point conversions

The FPConvert() pseudocode function performs conversions between half-precision, single-precision, and double-precision floating-point numbers.

The FPToFixed() and FixedToFP() functions perform conversions between floating-point numbers and integers or fixed-point numbers.