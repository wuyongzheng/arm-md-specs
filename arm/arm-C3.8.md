## C3.8 Data processing - SIMD and floating-point

This section describes the instruction groups for data processing with SIMD and floating-point register operands.

Common features of SIMD instructions gives general information about SIMD instructions.

The following subsections describe the scalar floating-point data processing instructions:

- Floating-point move (register).
- Floating-point move (immediate).
- Floating-point conversion.
- Floating-point round to integral value.
- Floating-point multiply-add.
- Floating-point arithmetic (one source).
- Floating-point arithmetic (two sources).
- Floating-point minimum and maximum.
- Floating-point comparison.
- Floating-point conditional select.

The following subsections describe the SIMD data processing instructions:

- SIMD move.
- SIMD arithmetic.
- SIMD compare.
- SIMD widening and narrowing arithmetic.
- SIMD unary arithmetic.
- SIMD by element arithmetic.
- SIMD permute.
- SIMD immediate.
- SIMD shift (immediate).
- SIMD conversions.
- SIMD reduce (across vector lanes).
- SIMD pairwise arithmetic.
- SIMD matrix multiply-accumulate.
- SIMD dot product.
- SIMD table lookup.
- SIMD complex number arithmetic instructions.
- SIMD BFloat16.
- SIMD multiply-accumulate.
- The Cryptographic Extension in AArch64 state.

For information about the floating-point exceptions, see Floating-point exceptions and exception traps.

## C3.8.1 Common features of SIMD instructions

Anumber of SIMD instructions come in three forms:

| Wide   | Indicated by the suffix W . The element width of the destination register and the first source operand is double that of the second source operand.   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Long   | Indicated by the suffix L . The element width of the destination register is double that of both source operands.                                     |

## Narrow

Indicated by the suffix N . The element width of the destination register is half that of both source operands.

In addition, each vector form of the instruction is part of a pair, with a second and upper part suffix of 2 , to identify the variant of the instruction:

- Where a SIMD operation widens or lengthens a 64-bit vector to a 128-bit vector, the instruction provides a second part operation that can extract the source from the upper 64 bits of the source registers.
- Where a SIMD operation narrows a 128-bit vector to a 64-bit vector, the instruction provides a second-part operation that can pack the result of a second operation into the upper part of the same destination register.

Note

This is referred to as a lane set specifier .

## C3.8.2 Floating-point move (register)

The Floating-point move (register) instructions copy a scalar floating-point value from one register to another register without performing any conversion.

Some of the Floating-point move (register) instructions overlap with the functionality provided by the Advanced SIMD instructions DUP , INS , and UMOV . However, Arm recommends using the FMOV instructions when operating on scalar floating-point data to avoid the creation of scalar floating-point code that depends on the availability of the Advanced SIMD instruction set.

Table C3-110 shows the Floating-point move (register) instructions.

## Table C3-110 Floating-point move (register) instructions

| Mnemonic   | Instruction                                                                | See            |
|------------|----------------------------------------------------------------------------|----------------|
| FMOV       | Floating-point move register without conversion                            | FMOV(register) |
|            | Floating-point move to or from general-purpose register without conversion | FMOV(general)  |

## C3.8.3 Floating-point move (immediate)

The Floating-point move (immediate) instructions convert a small constant immediate floating-point value into a half-precision, single-precision, or double-precision scalar floating-point value in a SIMD and floating-point register.

The floating-point constant can be specified either in decimal notation, such as 12.0 or -1.2e1, or as a string beginning with 0x followed by a hexadecimal representation of the IEEE 754 half-precision, single-precision, or double-precision encoding. Arm recommends that a disassembler uses the decimal notation, provided that this displays the value precisely.

Note

When FEAT\_FP16 is not implemented, the only half-precision instructions that are supported are floating-point conversions between half-precision, single-precision, and double-precision.

The floating-point value must be expressible as (± n /16 × 2 r ), where n is an integer in the range 16 ≤ n ≤ 31 and r is an integer in the range of -3 ≤ r ≤ 4, that is a normalized binary floating-point encoding with one sign bit, four bits of fraction, and a 3-bit exponent.

Table C3-111 shows the Floating-point move (immediate) instruction:

## Table C3-111 Floating-point move (immediate) instruction

| Mnemonic   | Instruction                   | See                     |
|------------|-------------------------------|-------------------------|
| FMOV       | Floating-point move immediate | FMOV(scalar, immediate) |

## C3.8.4 Floating-point conversion

The following subsections describe the conversion of floating-point values:

- Convert floating-point precision.
- Convert from floating-point single-precision to BFloat16.
- Convert from floating-point to integer or fixed-point.
- Convert from integer or fixed-point to floating-point.

## C3.8.4.1 Convert floating-point precision

These instructions convert a floating-point scalar with one precision to a floating-point scalar with a different precision, using the current rounding mode as specified by FPCR.RMode.

Table C3-112 shows the Floating-point precision conversion instruction.

## Table C3-112 Floating-point precision conversion instruction

| Mnemonic   | Instruction                               | See   |
|------------|-------------------------------------------|-------|
| FCVT       | Floating-point convert precision (scalar) | FCVT  |

## C3.8.4.2 Convert from floating-point single-precision to BFloat16

The BFCVT instruction is provided by FEAT\_BF16. This instruction converts a single-precision floating-point input to BFloat16 format, honoring the FPCR rounding mode controls to give a more accurate conversion than simply removing the bottom 16 bits of the input.

Table C3-113 shows this instruction.

## Table C3-113 Floating-point single-precision to BFloat16 conversion instruction

| Mnemonic   | Instruction                                                                       | See   |
|------------|-----------------------------------------------------------------------------------|-------|
| BFCVT      | BFloat16 floating-point convert from single-precision to BFloat16 format (scalar) | BFCVT |

## C3.8.4.3 Convert from floating-point to integer or fixed-point

Floating-point to integer or fixed-point conversion is supported by the following instruction variants:

- Scalar instruction variant, which converts a floating-point value in a SIMD and floating-point source register to an integer or fixed-point value in a general-purpose destination register.
- Scalar SIMD&amp;FP instruction variant, which converts a floating-point value in a SIMD and floating-point source register to an integer value in a SIMD and floating-point destination register.

For a fixed-point value, a final immediate operand indicates that the general-purpose register holds a fixed-point number and fbits indicates the number of bits after the binary point. fbits is in the range 1- 32 inclusive for a 32-bit general-purpose register name, and 1-64 inclusive for a 64-bit general-purpose register name.

Table C3-114 shows the floating-point to integer or fixed-point conversion instructions.

Table C3-114 Floating-point to integer or fixed-point conversion instructions

| Mnemonic   | Instruction                                                                                                    | See                          |
|------------|----------------------------------------------------------------------------------------------------------------|------------------------------|
| FCVTAS     | Floating-point scalar convert to signed integer, rounding to nearest with ties to away (scalar form)           | FCVTAS (scalar)              |
| FCVTAS     | Floating-point scalar convert to signed integer, rounding to nearest with ties to away (scalar SIMD&FP form)   | FCVTAS (scalar SIMD&FP)      |
| FCVTAU     | Floating-point scalar convert to unsigned integer, rounding to nearest with ties to away (scalar form)         | FCVTAU (scalar)              |
| FCVTAU     | Floating-point scalar convert to unsigned integer, rounding to nearest with ties to away (scalar SIMD&FP form) | FCVTAU (scalar SIMD&FP)      |
| FCVTMS     | Floating-point scalar convert to signed integer, rounding toward minus infinity (scalar form)                  | FCVTMS(scalar)               |
| FCVTMS     | Floating-point scalar convert to signed integer, rounding toward minus infinity (scalar SIMD&FP form)          | FCVTMS(scalar SIMD&FP)       |
| FCVTMU     | Floating-point scalar convert to unsigned integer, rounding toward minus infinity (scalar form)                | FCVTMU(scalar)               |
| FCVTMU     | Floating-point scalar convert to unsigned integer, rounding toward minus infinity (scalar SIMD&FP form)        | FCVTMU(scalar SIMD&FP)       |
| FCVTNS     | Floating-point scalar convert to signed integer, rounding to nearest with ties to even (scalar form)           | FCVTNS (scalar)              |
| FCVTNS     | Floating-point scalar convert to signed integer, rounding to nearest with ties to even (scalar SIMD&FP form)   | FCVTNS (scalar SIMD&FP)      |
| FCVTNU     | Floating-point scalar convert to unsigned integer, rounding to nearest with ties to even (scalar form)         | FCVTNU(scalar)               |
| FCVTNU     | Floating-point scalar convert to unsigned integer, rounding to nearest with ties to even (scalar SIMD&FP form) | FCVTNU(scalar SIMD&FP)       |
| FCVTPS     | Floating-point scalar convert to signed integer, rounding toward positive infinity (scalar form)               | FCVTPS (scalar)              |
| FCVTPS     | Floating-point scalar convert to signed integer, rounding toward positive infinity (scalar SIMD&FP form)       | FCVTPS (scalar SIMD&FP)      |
| FCVTPU     | Floating-point scalar convert to unsigned integer, rounding toward positive infinity (scalar form)             | FCVTPU (scalar)              |
| FCVTPU     | Floating-point scalar convert to unsigned integer, rounding toward positive infinity (scalar SIMD&FP form)     | FCVTPU (scalar SIMD&FP)      |
| FCVTZS     | Floating-point scalar convert to signed integer, rounding toward zero (scalar form)                            | FCVTZS (scalar, integer)     |
| FCVTZS     | Floating-point scalar convert to signed fixed-point, rounding toward zero (scalar form)                        | FCVTZS (scalar, fixed-point) |
| FCVTZS     | Floating-point scalar convert to signed integer, rounding toward zero (scalar SIMD&FP form)                    | FCVTZS (scalar SIMD&FP)      |
| FCVTZU     | Floating-point scalar convert to unsigned integer, rounding toward zero (scalar form)                          | FCVTZU (scalar, integer)     |
| FCVTZU     | Floating-point scalar convert to unsigned fixed-point, rounding toward zero (scalar form)                      | FCVTZU (scalar, fixed-point) |

| Mnemonic   | Instruction                                                                                   | See                     |
|------------|-----------------------------------------------------------------------------------------------|-------------------------|
|            | Floating-point scalar convert to unsigned integer, rounding toward zero (scalar SIMD&FP form) | FCVTZU (scalar SIMD&FP) |
| FJCVTZS    | Floating-point Javascript convert to signed fixed-point, rounding toward zero (scalar form)   | FJCVTZS                 |

## C3.8.4.4 Convert from integer or fixed-point to floating-point

The integer or fixed-point to floating-point conversion is supported by the following instruction variants:

- Scalar instruction variant, which converts an integer or fixed-point value in a general-purpose register to a floating-point value in a SIMD and floating-point destination register.
- Scalar SIMD&amp;FP variant, which converts an integer value in a SIMD and floating-point source register to a floating-point value in a SIMD and floating-point destination register.

For a fixed-point value, a final immediate operand indicates that the general-purpose register holds a fixed-point number and fbits indicates the number of bits after the binary point. fbits is in the range 1- 32 inclusive for a 32-bit general-purpose register name, and 1-64 inclusive for a 64-bit general-purpose register name.

Table C3-115 shows the integer or fixed-point to floating-point conversion instructions.

## Table C3-115 Integer or fixed-point to floating-point conversion instructions

| Mnemonic   | Instruction                                                                                              | See                         |
|------------|----------------------------------------------------------------------------------------------------------|-----------------------------|
| SCVTF      | Signed integer scalar convert to floating-point, using the current rounding mode (scalar form)           | SCVTF (scalar, integer)     |
| SCVTF      | Signed fixed-point convert to floating-point, using the current rounding mode (scalar form)              | SCVTF (scalar, fixed-point) |
| SCVTF      | Signed integer scalar convert to floating-point, using the current rounding mode (scalar SIMD&FP form)   | SCVTF (scalar SIMD&FP)      |
| UCVTF      | Unsigned integer scalar convert to floating-point, using the current rounding mode (scalar form)         | UCVTF (scalar, integer)     |
| UCVTF      | Unsigned fixed-point convert to floating-point, using the current rounding mode (scalar form)            | UCVTF (scalar, fixed-point) |
| UCVTF      | Unsigned integer scalar convert to floating-point, using the current rounding mode (scalar SIMD&FP form) | UCVTF (scalar SIMD&FP)      |

## C3.8.5 Floating-point round to integral value

The following subsections describe instructions which round a floating-point number to an integral valued floating-point number in the same format:

- Floating-point round to an integer of the same size as the register
- Floating-point round to 32-bit or 64-bit integer

## C3.8.5.1 Floating-point round to an integer of the same size as the register

The following instructions round a floating-point value to an integer floating-point value of the same size.

For these instructions:

- Azero input gives a zero result with the same sign.

- An infinite input gives an infinite result with the same sign.
- ANaNis propagated as in normal floating-point arithmetic.

These instructions can cause floating-point exceptions, for more information see Floating-point exceptions and exception traps.

Table C3-116 shows the Floating-point round to integer instructions.

## Table C3-116 Floating-point round to integer instructions

| Mnemonic   | Instruction                                                        | See             |
|------------|--------------------------------------------------------------------|-----------------|
| FRINTA     | Floating-point round to integer, to nearest with ties to away      | FRINTA (scalar) |
| FRINTI     | Floating-point round to integer, using current rounding mode       | FRINTI (scalar) |
| FRINTM     | Floating-point round to integer, toward minus infinity             | FRINTM (scalar) |
| FRINTN     | Floating-point round to integer, to nearest with ties to even      | FRINTN (scalar) |
| FRINTP     | Floating-point round to integer, toward positive infinity          | FRINTP (scalar) |
| FRINTX     | Floating-point round to integer exact, using current rounding mode | FRINTX (scalar) |
| FRINTZ     | Floating-point round to integer, toward zero                       | FRINTZ (scalar) |

## C3.8.5.2 Floating-point round to 32-bit or 64-bit integer

The following instructions are present if FEAT\_FRINTTS is implemented, The instructions round to a value that fits in a 32-bit integer or a 64-bit integer size, and use either round towards zero or the ambient rounding model.

These instructions can cause floating-point exceptions, for more information see Floating-point exceptions and exception traps.

Table C3-117 shows the Floating-point round to 32-bit or 64-bit integer instructions.

## Table C3-117 Floating-point round to integer instructions

| Mnemonic   | Instruction                                                          | See               |
|------------|----------------------------------------------------------------------|-------------------|
| FRINT32X   | Floating-point round to 32-bit integer, using current rounding model | FRINT32X (scalar) |
| FRINT32Z   | Floating-point round to 32-bit integer, toward zero                  | FRINT32Z (scalar) |
| FRINT64X   | Floating point round to 64-bit integer, using current rounding model | FRINT64X (scalar) |
| FRINT64Z   | Floating point round to 64-bit integer, toward zero                  | FRINT64Z (scalar) |

## C3.8.6 Floating-point multiply-add

Table C3-118 shows the Floating-point multiply-add instructions that require three source register operands.

## Table C3-118 Floating-point multiply-add instructions

| Mnemonic   | Instruction                                           | See    |
|------------|-------------------------------------------------------|--------|
| FMADD      | Floating-point scalar fused multiply-add              | FMADD  |
| FMSUB      | Floating-point scalar fused multiply-subtract         | FMSUB  |
| FNMADD     | Floating-point scalar negated fused multiply-add      | FNMADD |
| FNMSUB     | Floating-point scalar negated fused multiply-subtract | FNMSUB |

## C3.8.7 Floating-point arithmetic (one source)

Table C3-119 shows the Floating-point arithmetic instructions that require a single source register operand.

Table C3-119 Floating-point arithmetic instructions with one source register

| Mnemonic   | Instructions                         | See            |
|------------|--------------------------------------|----------------|
| FABS       | Floating-point scalar absolute value | FABS (scalar)  |
| FNEG       | Floating-point scalar negate         | FNEG (scalar)  |
| FSQRT      | Floating-point scalar square root    | FSQRT (scalar) |

## C3.8.8 Floating-point arithmetic (two sources)

Table C3-120 shows the Floating-point arithmetic instructions that require two source register operands.

Table C3-120 Floating-point arithmetic instructions with two source registers

| Mnemonic   | Instruction                           | See           |
|------------|---------------------------------------|---------------|
| FADD       | Floating-point scalar add             | FADD(scalar)  |
| FDIV       | Floating-point scalar divide          | FDIV (scalar) |
| FMUL       | Floating-point scalar multiply        | FMUL(scalar)  |
| FNMUL      | Floating-point scalar multiply-negate | FNMUL(scalar) |
| FSUB       | Floating-point scalar subtract        | FSUB (scalar) |

## C3.8.9 Floating-point minimum and maximum

The min(x,y) and max(x,y) operations return a quiet NaN when either x or y is NaN.

As described in Flushing denormalized numbers to zero, if flushing denormalized inputs to zero is enabled, denormal operands are flushed to zero before comparison, and if the result of the comparison is the flushed value, then a zero value is returned. Where both x and y are zero, or denormal values flushed to zero, with different signs, then +0.0 is returned by max() and -0.0 by min() .

The minNum(x,y) and maxNum(x,y) operations follow the IEEE 754-2008 standard and return the numerical operand when one operand is numerical and the other a quiet NaN. Apart from this additional handling of a single quiet NaN, the result is then identical to min(x,y) and max(x,y) .

Table C3-121 shows the Floating-point instructions that can perform floating-point minimum and maximum operations.

Table C3-121 Floating-point minimum and maximum instructions

| Mnemonic   | Instruction                          | See            |
|------------|--------------------------------------|----------------|
| FMAX       | Floating-point scalar maximum        | FMAX(scalar)   |
| FMAXNM     | Floating-point scalar maximum number | FMAXNM(scalar) |
| FMIN       | Floating-point scalar minimum        | FMIN (scalar)  |
| FMINNM     | Floating-point scalar minimum number | FMINNM(scalar) |

## C3.8.10 Floating-point comparison

These instructions set the NZCV Condition flags in PSTATE, based on the result of a comparison of two operands. If the floating-point comparisons are unordered , where one or both operands are a form of NaN, the C and V bits are set to 1 and the N and Z bits are cleared to 0.

Note

The NZCV flags in the FPSR are associated with AArch32 state. The A64 floating-point comparison instructions do not change the Condition flags in the FPSR.

For the conditional Floating-point comparison instructions, if the condition is TRUE, the flags are updated to the result of the comparison, otherwise the flags are updated to the immediate value that is defined in the instruction encoding.

The quiet compare instructions generate an Invalid Operation floating-point exception if either of the source operands is a signaling NaN. The signaling compare instructions generate an Invalid Operation floating-point exception if either of the source operands is any type of NaN.

Note If FEAT\_FlagM2 is implemented, instructions AXFLAG and XAFLAG convert between the PSTATE condition flag format used by the FCMP instruction and an alternative format. See FEAT\_FlagM for more information.

Table C3-122 shows the Floating-point comparison instructions.

Table C3-122 Floating-point comparison instructions

| Mnemonic   | Instruction                                  | See    |
|------------|----------------------------------------------|--------|
| FCMP       | Floating-point quiet compare                 | FCMP   |
| FCMPE      | Floating-point signaling compare             | FCMPE  |
| FCCMP      | Floating-point conditional quiet compare     | FCCMP  |
| FCCMPE     | Floating-point conditional signaling compare | FCCMPE |

## C3.8.11 Floating-point conditional select

Table C3-123 shows the Floating-point conditional select instructions.

## Table C3-123 Floating-point conditional select instructions

| Mnemonic   | Instruction                              | See   |
|------------|------------------------------------------|-------|
| FCSEL      | Floating-point scalar conditional select | FCSEL |

## C3.8.12 SIMD move

The functionality of some data movement instructions overlaps with that provided by the scalar floating-point FMOV instructions described in Floating-point move (register).

Table C3-124 shows the SIMD move instructions.

## Table C3-124 SIMD move instructions

| Mnemonic   | Instruction                                              | See               |
|------------|----------------------------------------------------------|-------------------|
| DUP        | Duplicate vector element to vector or scalar             | DUP(element)      |
| DUP        | Duplicate general-purpose register to vector             | DUP(general)      |
| INS a      | Insert vector element from another vector element        | INS (element)     |
|            | Insert vector element from general-purpose register      | INS (general)     |
| MOV        | Move vector element to vector element                    | MOV(element)      |
|            | Move general-purpose register to vector element          | MOV(from general) |
|            | Move vector element to scalar                            | MOV(scalar)       |
|            | Move vector element to general-purpose register          | MOV(to general)   |
| UMOV       | Unsigned move vector element to general-purpose register | UMOV              |
| SMOV       | Signed move vector element to general-purpose register   | SMOV              |

## C3.8.13 SIMD arithmetic

Table C3-125 shows the SIMD arithmetic instructions.

## Table C3-125 SIMD arithmetic instructions

| Mnemonic   | Instruction                                | See                    |
|------------|--------------------------------------------|------------------------|
| ADD        | Add (vector and scalar form)               | ADD(vector)            |
| AND        | Bitwise AND(vector form)                   | AND(vector)            |
| BIC        | Bitwise bit clear (register) (vector form) | BIC (vector, register) |
| BIF        | Bitwise insert if false (vector form)      | BIF                    |
| BIT        | Bitwise insert if true (vector form)       | BIT                    |
| BSL        | Bitwise select (vector form)               | BSL                    |
| EOR        | Bitwise exclusive-OR (vector form)         | EOR(vector)            |

| Mnemonic   | Instruction                                                                               | See                   |
|------------|-------------------------------------------------------------------------------------------|-----------------------|
| FABD       | Floating-point absolute difference (vector and scalar form)                               | FABD                  |
| FADD       | Floating-point add (vector form)                                                          | FADD(vector)          |
| FAMAX      | Floating-point absolute maximum                                                           | FAMAX                 |
| FAMIN      | Floating-point absolute minimum                                                           | FAMIN                 |
| FDIV       | Floating-point divide (vector form)                                                       | FDIV (vector)         |
| FMAX       | Floating-point maximum (vector form)                                                      | FMAX(vector)          |
| FMAXNM     | Floating-point maximum number (vector form)                                               | FMAXNM(vector)        |
| FMIN       | Floating-point minimum (vector form)                                                      | FMIN (vector)         |
| FMINNM     | Floating-point minimum number (vector form)                                               | FMINNM(vector)        |
| FMUL       | Floating-point multiply (vector form)                                                     | FMUL(vector)          |
| FMULX      | Floating-point multiply extended (vector and scalar form)                                 | FMULX                 |
| FRECPS     | Floating-point reciprocal step (vector and scalar form)                                   | FRECPS                |
| FRSQRTS    | Floating-point reciprocal square root step (vector and scalar form)                       | FRSQRTS               |
| FSCALE     | Floating-point adjust exponent by vector                                                  | FSCALE                |
| FSUB       | Floating-point subtract (vector form)                                                     | FSUB (vector)         |
| MLA        | Multiply-add (vector form)                                                                | MLA(vector)           |
| MLS        | Multiply-subtract (vector form)                                                           | MLS(vector)           |
| MUL        | Multiply (vector form)                                                                    | MUL(vector)           |
| MOV        | Move vector register (vector form)                                                        | MOV(vector)           |
| ORN        | Bitwise inclusive ORNOT(vector form)                                                      | ORN(vector)           |
| ORR        | Bitwise inclusive OR(register) (vector form)                                              | ORR(vector, register) |
| PMUL       | Polynomial multiply (vector form)                                                         | PMUL                  |
| SABA       | Signed absolute difference and accumulate (vector form)                                   | SABA                  |
| SABD       | Signed absolute difference (vector form)                                                  | SABD                  |
| SHADD      | Signed halving add (vector form)                                                          | SHADD                 |
| SHSUB      | Signed halving subtract (vector form)                                                     | SHSUB                 |
| SMAX       | Signed maximum (vector form)                                                              | SMAX                  |
| SMIN       | Signed minimum (vector form)                                                              | SMIN                  |
| SQADD      | Signed saturating add (vector and scalar form)                                            | SQADD                 |
| SQDMULH    | Signed saturating doubling multiply returning high half (vector and scalar form)          | SQDMULH(vector)       |
| SQRSHL     | Signed saturating rounding shift left (register) (vector and scalar form)                 | SQRSHL                |
| SQRDMLAH   | Signed saturating rounding doubling multiply accumulate returning high half               | SQRDMLAH(vector)      |
| SQRDMLSH   | Signed saturating rounding doubling multiply subtract returning high half                 | SQRDMLSH(vector)      |
| SQRDMULH   | Signed saturating rounding doubling multiply returning high half (vector and scalar form) | SQRDMULH(vector)      |
| SQSHL      | Signed saturating shift left (register) (vector and scalar form)                          | SQSHL (register)      |
| SQSUB      | Signed saturating subtract (vector and scalar form)                                       | SQSUB                 |
| SRHADD     | Signed rounding halving add (vector form)                                                 | SRHADD                |
| SRSHL      | Signed rounding shift left (register) (vector and scalar form)                            | SRSHL                 |
| SSHL       | Signed shift left (register) (vector and scalar form)                                     | SSHL                  |

| Mnemonic   | Instruction                                                                 | See             |
|------------|-----------------------------------------------------------------------------|-----------------|
| SUB        | Subtract (vector and scalar form)                                           | SUB (vector)    |
| UABA       | Unsigned absolute difference and accumulate (vector form)                   | UABA            |
| UABD       | Unsigned absolute difference (vector form)                                  | UABD            |
| UHADD      | Unsigned halving add (vector form)                                          | UHADD           |
| UHSUB      | Unsigned halving subtract (vector form)                                     | UHSUB           |
| UMAX       | Unsigned maximum (vector form)                                              | UMAX            |
| UMIN       | Unsigned minimum (vector form)                                              | UMIN            |
| UQADD      | Unsigned saturating add (vector and scalar form)                            | UQADD           |
| UQRSHL     | Unsigned saturating rounding shift left (register) (vector and scalar form) | UQRSHL          |
| UQSHL      | Unsigned saturating shift left (register) (vector and scalar form)          | UQSHL(register) |
| UQSUB      | Unsigned saturating subtract (vector and scalar form)                       | UQSUB           |
| URHADD     | Unsigned rounding halving add (vector form)                                 | URHADD          |
| URSHL      | Unsigned rounding shift left (register) (vector and scalar form)            | URSHL           |
| USHL       | Unsigned shift left (register) (vector and scalar form)                     | USHL            |

## C3.8.14 SIMD compare

The SIMD compare instructions compare vector or scalar elements according to the specified condition and set the destination vector element to all ones if the condition holds, or to zero if the condition does not hold.

Note

Some of the comparisons, such as LS, LE, LO, and LT, can be made by reversing the operands and using the opposite comparison, HS, GE, HI, or GT.

Table C3-126 shows that SIMD compare instructions.

## Table C3-126 SIMD compare instructions

| Mnemonic   | Instruction                                                                    | See             |
|------------|--------------------------------------------------------------------------------|-----------------|
| CMEQ       | Compare bitwise equal (vector and scalar form)                                 | CMEQ(register)  |
| CMEQ       | Compare bitwise equal to zero (vector and scalar form)                         | CMEQ(zero)      |
| CMHS       | Compare unsigned higher or same (vector and scalar form)                       | CMHS(register)  |
| CMGE       | Compare signed greater than or equal (vector and scalar form)                  | CMGE(register)  |
| CMGE       | Compare signed greater than or equal to zero (vector and scalar form)          | CMGE(zero)      |
| CMHI       | Compare unsigned higher (vector and scalar form)                               | CMHI (register) |
| CMGT       | Compare signed greater than (vector and scalar form)                           | CMGT(register)  |
| CMGT       | Compare signed greater than zero (vector and scalar form)                      | CMGT(zero)      |
| CMLE       | Compare signed less than or equal to zero (vector and scalar form)             | CMLE(zero)      |
| CMLT       | Compare signed less than zero (vector and scalar form)                         | CMLT(zero)      |
| CMTST      | Compare bitwise test bits nonzero (vector and scalar form)                     | CMTST           |
| FCMEQ      | Floating-point compare equal (vector and scalar form)                          | FCMEQ(register) |
| FCMEQ      | Floating-point compare equal to zero (vector and scalar form)                  | FCMEQ(zero)     |
| FCMGE      | Floating-point compare greater than or equal (vector and scalar form)          | FCMGE(register) |
| FCMGE      | Floating-point compare greater than or equal to zero (vector and scalar form)  | FCMGE(zero)     |
| FCMGT      | Floating-point compare greater than (vector and scalar form)                   | FCMGT(register) |
| FCMGT      | Floating-point compare greater than zero (vector and scalar form)              | FCMGT(zero)     |
| FCMLE      | Floating-point compare less than or equal to zero (vector and scalar form)     | FCMLE(zero)     |
| FCMLT      | Floating-point compare less than zero (vector and scalar form)                 | FCMLT (zero)    |
| FACGE      | Floating-point absolute compare greater than or equal (vector and scalar form) | FACGE           |
| FACGT      | Floating-point absolute compare greater than (vector and scalar form)          | FACGT           |

## C3.8.15 SIMD widening and narrowing arithmetic

For information about the variants of these instructions, see Common features of SIMD instructions.

Table C3-127 shows the SIMD widening and narrowing arithmetic instructions.

## Table C3-127 SIMD widening and narrowing arithmetic instructions

| Mnemonic          | Instruction                                                                | See                        |
|-------------------|----------------------------------------------------------------------------|----------------------------|
| ADDHN , ADDHN2    | Add returning high, narrow (vector form)                                   | ADDHN,ADDHN2               |
| PMULL , PMULL2    | Polynomial multiply long (vector form)                                     | PMULL, PMULL2              |
| RADDHN , RADDHN2  | Rounding add returning high, narrow (vector form)                          | RADDHN,RADDHN2             |
| RSUBHN , RSUBHN2  | Rounding subtract returning high, narrow (vector form)                     | RSUBHN, RSUBHN2            |
| SABAL , SABAL2    | Signed absolute difference and accumulate long (vector form)               | SABAL, SABAL2              |
| SABDL, SABDL2     | Signed absolute difference long (vector form)                              | SABDL, SABDL2              |
| SADDL, SADDL2     | Signed add long (vector form)                                              | SADDL, SADDL2              |
| SADDW, SADDW2     | Signed add wide (vector form)                                              | SADDW,SADDW2               |
| SMLAL , SMLAL2    | Signed multiply-add long (vector form)                                     | SMLAL, SMLAL2 (vector)     |
| SMLSL, SMLSL2     | Signed multiply-subtract long (vector form)                                | SMLSL, SMLSL2 (vector)     |
| SMULL, SMULL2     | Signed multiply long (vector form)                                         | SMULL, SMULL2 (vector)     |
| SQDMLAL, SQDMLAL2 | Signed saturating doubling multiply-add long (vector and scalar form)      | SQDMLAL, SQDMLAL2(vector)  |
| SQDMLSL, SQDMLSL2 | Signed saturating doubling multiply-subtract long (vector and scalar form) | SQDMLSL, SQDMLSL2 (vector) |
| SQDMULL, SQDMULL2 | Signed saturating doubling multiply long (vector and scalar form)          | SQDMULL, SQDMULL2(vector)  |
| SSUBL, SSUBL2     | Signed subtract long (vector form)                                         | SSUBL, SSUBL2              |
| SSUBW, SSUBW2     | Signed subtract wide (vector form)                                         | SSUBW, SSUBW2              |
| SUBHN, SUBHN2     | Subtract returning high, narrow (vector form)                              | SUBHN, SUBHN2              |
| UABAL, UABAL2     | Unsigned absolute difference and accumulate long (vector form)             | UABAL, UABAL2              |
| UABDL, UABDL2     | Unsigned absolute difference long (vector form)                            | UABDL, UABDL2              |
| UADDL, UADDL2     | Unsigned add long (vector form)                                            | UADDL,UADDL2               |
| UADDW, UADDW2     | Unsigned add wide (vector form)                                            | UADDW,UADDW2               |
| UMLAL, UMLAL2     | Unsigned multiply-add long (vector form)                                   | UMLAL, UMLAL2(vector)      |
| UMLSL, UMLSL2     | Unsigned multiply-subtract long (vector form)                              | UMLSL, UMLSL2 (vector)     |
| UMULL, UMULL2     | Unsigned multiply long (vector form)                                       | UMULL, UMULL2(vector)      |
| USUBL, USUBL2     | Unsigned subtract long (vector form)                                       | USUBL, USUBL2              |
| USUBW, USUBW2     | Unsigned subtract wide (vector form)                                       | USUBW,USUBW2               |

## C3.8.16 SIMD unary arithmetic

For information about the variants of these instructions, see Common features of SIMD instructions.

Table C3-128 shows the SIMD unary arithmetic instructions.

## Table C3-128 SIMD unary arithmetic instructions

| Mnemonic         | Instruction                                                                       | See               |
|------------------|-----------------------------------------------------------------------------------|-------------------|
| ABS              | Absolute value (vector and scalar form)                                           | ABS               |
| CLS              | Count leading sign bits (vector form)                                             | CLS (vector)      |
| CLZ              | Count leading zero bits (vector form)                                             | CLZ (vector)      |
| CNT              | Population count per byte (vector form)                                           | CNT               |
| FABS             | Floating-point absolute (vector form)                                             | FABS (vector)     |
| FNEG             | Floating-point negate (vector form)                                               | FNEG (vector)     |
| FRECPE           | Floating-point reciprocal estimate (vector and scalar form)                       | FRECPE            |
| FRECPX           | Floating-point reciprocal exponent (scalar form)                                  | FRECPX            |
| FRINT32X         | Floating-point round to 32-bit integer, using current rounding mode (vector form) | FRINT32X (vector) |
| FRINT32Z         | Floating-point round to 32-bit integer, toward zero (vector form)                 | FRINT32Z (vector) |
| FRINT64X         | Floating-point round to 64-bit integer, using current rounding mode (vector form) | FRINT64X (vector) |
| FRINT64Z         | Floating-point round to 64-bit integer, toward zero (vector form)                 | FRINT64Z (vector) |
| FRINTA           | Floating-point round to integer, to nearest with ties to away (vector form)       | FRINTA (vector)   |
| FRINTI           | Floating-point round to integer, using current rounding mode (vector form)        | FRINTI (vector)   |
| FRINTM           | Floating-point round to integer, toward minus infinity (vector form)              | FRINTM (vector)   |
| FRINTN           | Floating-point round to integer, to nearest with ties to even (vector form)       | FRINTN (vector)   |
| FRINTP           | Floating-point round to integer, toward positive infinity (vector form)           | FRINTP (vector)   |
| FRINTX           | Floating-point round to integer exact, using current rounding mode (vector form)  | FRINTX (vector)   |
| FRINTZ           | Floating-point round to integer, toward zero (vector form)                        | FRINTZ (vector)   |
| FRSQRTE          | Floating-point reciprocal square root estimate (vector and scalar form)           | FRSQRTE           |
| FSQRT            | Floating-point square root (vector form)                                          | FSQRT (vector)    |
| MVN              | Bitwise NOT(vector form)                                                          | MVN               |
| NEG              | Negate (vector and scalar form)                                                   | NEG(vector)       |
| NOT              | Bitwise NOT(vector form)                                                          | NOT               |
| RBIT             | Bitwise reverse (vector form)                                                     | RBIT (vector)     |
| REV16            | Reverse elements in 16-bit halfwords (vector form)                                | REV16 (vector)    |
| REV32            | Reverse elements in 32-bit words (vector form)                                    | REV32 (vector)    |
| REV64            | Reverse elements in 64-bit doublewords (vector form)                              | REV64             |
| SADALP           | Signed add and accumulate long pairwise (vector form)                             | SADALP            |
| SADDLP           | Signed add long pairwise (vector form)                                            | SADDLP            |
| SQABS            | Signed saturating absolute value (vector and scalar form)                         | SQABS             |
| SQNEG            | Signed saturating negate (vector and scalar form)                                 | SQNEG             |
| SQXTN , SQXTN2   | Signed saturating extract narrow (vector form)                                    | SQXTN, SQXTN2     |
| SQXTUN , SQXTUN2 | Signed saturating extract unsigned narrow (vector and scalar form)                | SQXTUN, SQXTUN2   |
| SUQADD           | Signed saturating accumulate of unsigned value (vector and scalar form)           | SUQADD            |

| Mnemonic       | Instruction                                                             | See          |
|----------------|-------------------------------------------------------------------------|--------------|
| SXTL , SXTL2   | Signed extend long                                                      | SXTL, SXTL2  |
| UADALP         | Unsigned add and accumulate long pairwise (vector form)                 | UADALP       |
| UADDLP         | Unsigned add long pairwise (vector form)                                | UADDLP       |
| UQXTN , UQXTN2 | Unsigned saturating extract narrow (vector form)                        | UQXTN,UQXTN2 |
| URECPE         | Unsigned reciprocal estimate (vector form)                              | URECPE       |
| URSQRTE        | Unsigned reciprocal square root estimate (vector form)                  | URSQRTE      |
| USQADD         | Unsigned saturating accumulate of signed value (vector and scalar form) | USQADD       |
| UXTL, UXTL2    | Unsigned extend long                                                    | UXTL, UXTL2  |
| XTN , XTN2     | Extract narrow (vector form)                                            | XTN, XTN2    |

## C3.8.17 SIMD by element arithmetic

For information about the variants of these instructions, see Common features of SIMD instructions.

Table C3-129 shows the SIMD by element arithmetic instructions.

Table C3-129 SIMD by element arithmetic instructions

| Mnemonic           | Instruction                                                                      | See                            |
|--------------------|----------------------------------------------------------------------------------|--------------------------------|
| FMLA               | Floating-point fused multiply-add (vector and scalar form)                       | FMLA(by element)               |
| FMLAL , FMLAL2     | Floating-point fused multiply-add long (vector form)                             | FMLAL, FMLAL2 (by element)     |
| FMLS               | Floating-point fused multiply-subtract (vector and scalar form)                  | FMLS (by element).             |
| FMLSL , FMLSL2     | Floating-point fused multiply-subtract long (vector form)                        | FMLSL, FMLSL2 (by element)     |
| FMUL               | Floating-point multiply (vector and scalar form)                                 | FMUL(by element)               |
| FMULX              | Floating-point multiply extended (vector and scalar form)                        | FMULX(by element)              |
| MLA                | Multiply-add (vector form)                                                       | MLA(by element)                |
| MLS                | Multiply-subtract (vector form)                                                  | MLS(by element)                |
| MUL                | Multiply (vector form)                                                           | MUL(by element)                |
| SMLAL , SMLAL2     | Signed multiply-add long (vector form)                                           | SMLAL, SMLAL2 (by element)     |
| SMLSL , SMLSL2     | Signed multiply-subtract long (vector form)                                      | SMLSL, SMLSL2 (by element)     |
| SMULL , SMULL2     | Signed multiply long (vector form)                                               | SMULL, SMULL2 (by element)     |
| SQDMLAL , SQDMLAL2 | Signed saturating doubling multiply-add long (vector and scalar form)            | SQDMLAL, SQDMLAL2(by element)  |
| SQDMLSL , SQDMLSL2 | Signed saturating doubling multiply-subtract long (vector form)                  | SQDMLSL, SQDMLSL2 (by element) |
| SQDMULH            | Signed saturating doubling multiply returning high half (vector and scalar form) | SQDMULH(by element)            |
| SQDMULL , SQDMULL2 | Signed saturating doubling multiply long (vector and scalar form)                | SQDMULL, SQDMULL2(by element)  |
| SQRDMLAH           | Signed saturating rounding doubling multiply accumulate returning high half      | SQRDMLSH(by element)           |
| SQRDMLSH           | Signed saturating rounding doubling multiply subtract returning high half        | SQRDMLSH(vector)               |

| Mnemonic       | Instruction                                                                               | See                        |
|----------------|-------------------------------------------------------------------------------------------|----------------------------|
| SQRDMULH       | Signed saturating rounding doubling multiply returning high half (vector and scalar form) | SQRDMULH(by element)       |
| UMLAL , UMLAL2 | Unsigned multiply-add long (vector form)                                                  | UMLAL, UMLAL2(by element)  |
| UMLSL , UMLSL2 | Unsigned multiply-subtract long (vector form)                                             | UMLSL, UMLSL2 (by element) |
| UMULL , UMULL2 | Unsigned multiply long (vector form)                                                      | UMULL, UMULL2(by element)  |

## C3.8.18 SIMD permute

Table C3-130 shows the SIMD permute instructions.

## Table C3-130 SIMD permute instructions

| Mnemonic   | Instruction                           | See   |
|------------|---------------------------------------|-------|
| EXT        | Extract vector from a pair of vectors | EXT   |
| TRN1       | Transpose vectors (primary)           | TRN1  |
| TRN2       | Transpose vectors (secondary)         | TRN2  |
| UZP1       | Unzip vectors (primary)               | UZP1  |
| UZP2       | Unzip vectors (secondary)             | UZP2  |
| ZIP1       | Zip vectors (primary)                 | ZIP1  |
| ZIP2       | Zip vectors (secondary)               | ZIP2  |

## C3.8.19 SIMD immediate

Table C3-131 shows the SIMD immediate instructions.

## Table C3-131 SIMD immediate instructions

| Mnemonic   | Instruction                   | See                     |
|------------|-------------------------------|-------------------------|
| BIC        | Bitwise bit clear immediate   | BIC (vector, immediate) |
| FMOV       | Floating-point move immediate | FMOV(vector, immediate) |
| MOVI       | Move immediate                | MOVI                    |
| MVNI       | Move inverted immediate       | MVNI                    |
| ORR        | Bitwise inclusive ORimmediate | ORR(vector, immediate)  |

## C3.8.20 SIMD shift (immediate)

For information about the variants of these instructions, see Common features of SIMD instructions.

Table C3-132 shows the SIMD shift immediate instructions.

## Table C3-132 SIMD shift (immediate) instructions

| Mnemonic             | Instruction                                                                             | See                 |
|----------------------|-----------------------------------------------------------------------------------------|---------------------|
| RSHRN , RSHRN2       | Rounding shift right narrow immediate (vector form)                                     | RSHRN, RSHRN2       |
| SHL                  | Shift left immediate (vector and scalar form)                                           | SHL                 |
| SHLL , SHLL2         | Shift left long (by element size) (vector form)                                         | SHLL, SHLL2         |
| SHRN , SHRN2         | Shift right narrow immediate (vector form)                                              | SHRN, SHRN2         |
| SLI                  | Shift left and insert immediate (vector and scalar form)                                | SLI                 |
| SQRSHRN , SQRSHRN2   | Signed saturating rounded shift right narrow immediate (vector and scalar form)         | SQRSHRN, SQRSHRN2   |
| SQRSHRUN , SQRSHRUN2 | Signed saturating shift right unsigned narrow immediate (vector and scalar form)        | SQRSHRUN, SQRSHRUN2 |
| SQSHL                | Signed saturating shift left immediate (vector and scalar form)                         | SQSHL (immediate)   |
| SQSHLU               | Signed saturating shift left unsigned immediate (vector and scalar form)                | SQSHLU              |
| SQSHRN , SQSHRN2     | Signed saturating shift right narrow immediate (vector and scalar form)                 | SQSHRN, SQSHRN2     |
| SQSHRUN , SQSHRUN2   | Signed saturating shift right unsigned narrow immediate (vector and scalar form)        | SQSHRUN, SQSHRUN2   |
| SRI                  | Shift right and insert immediate (vector and scalar form)                               | SRI                 |
| SRSHR                | Signed rounding shift right immediate (vector and scalar form)                          | SRSHR               |
| SRSRA                | Signed rounding shift right and accumulate immediate (vector and scalar form)           | SRSRA.              |
| SSHLL , SSHLL2       | Signed shift left long immediate (vector form)                                          | SSHLL, SSHLL2       |
| SSHR                 | Signed shift right immediate (vector and scalar form)                                   | SSHR                |
| SSRA                 | Signed integer shift right and accumulate immediate (vector and scalar form)            | SSRA                |
| SXTL , SXTL2         | Signed integer extend (vector only)                                                     | SXTL, SXTL2         |
| UQRSHRN , UQRSHRN2   | Unsigned saturating rounded shift right narrow immediate (vector and scalar form)       | UQRSHRN,UQRSHRN2    |
| UQSHL                | Unsigned saturating shift left immediate (vector and scalar form)                       | UQSHL(immediate)    |
| UQSHRN , UQSHRN2     | Unsigned saturating shift right narrow immediate (vector and scalar form)               | UQSHRN, UQSHRN2     |
| URSHR                | Unsigned rounding shift right immediate (vector and scalar form)                        | URSHR               |
| URSRA                | Unsigned integer rounding shift right and accumulate immediate (vector and scalar form) | URSRA               |
| USHLL , USHLL2       | Unsigned shift left long immediate (vector form)                                        | USHLL, USHLL2       |
| USHR                 | Unsigned shift right immediate (vector and scalar form)                                 | USHR                |
| USRA                 | Unsigned shift right and accumulate immediate (vector and scalar form)                  | USRA                |
| UXTL , UXTL2         | Unsigned integer extend (vector only)                                                   | UXTL, UXTL2         |

## C3.8.21 SIMD conversions

## C3.8.21.1 Floating-point conversion

Table C3-133 shows the SIMD floating-point conversion instructions.

## Table C3-133 SIMD floating-point conversion instructions

| Mnemonic         | Instruction                                                                                                | See                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| FCVTAS           | Floating-point convert to signed integer, rounding to nearest with ties to away (vector and scalar form)   | FCVTAS (vector)                                                      |
| FCVTAU           | Floating-point convert to unsigned integer, rounding to nearest with ties to away (vector and scalar form) | FCVTAU (vector)                                                      |
| FCVTL , FCVTL2   | Floating-point convert to higher precision long (vector form)                                              | FCVTL, FCVTL2                                                        |
| FCVTMS           | Floating-point convert to signed integer, rounding toward minus infinity (vector and scalar form)          | FCVTMS(vector)                                                       |
| FCVTMU           | Floating-point convert to unsigned integer, rounding toward minus infinity (vector and scalar form)        | FCVTMU(vector)                                                       |
| FCVTN , FCVTN2   | Floating-point convert to lower precision narrow (vector form)                                             | FCVTN, FCVTN2 (double to single-precision, single to half-precision) |
| FCVTNS           | Floating-point convert to signed integer, rounding to nearest with ties to even (vector and scalar form)   | FCVTNS (vector)                                                      |
| FCVTNU           | Floating-point convert to unsigned integer, rounding to nearest with ties to even (vector and scalar form) | FCVTNU(vector)                                                       |
| FCVTPS           | Floating-point convert to signed integer, rounding toward positive infinity (vector and scalar form)       | FCVTPS (vector)                                                      |
| FCVTPU           | Floating-point convert to unsigned integer, rounding toward positive infinity (vector and scalar form)     | FCVTPU (vector)                                                      |
| FCVTXN , FCVTXN2 | Floating-point convert to lower precision narrow, rounding to odd (vector and scalar form)                 | FCVTXN, FCVTXN2                                                      |
| FCVTZS           | Floating-point convert to signed integer, rounding toward zero (vector and scalar form)                    | FCVTZS (vector, integer)                                             |
| FCVTZS           | Floating-point convert to signed fixed-point, rounding toward zero (vector and scalar form)                | FCVTZS (vector, fixed-point)                                         |
| FCVTZU           | Floating-point convert to unsigned integer, rounding toward zero (vector and scalar form)                  | FCVTZU (vector, integer)                                             |
| FCVTZU           | Floating-point convert to unsigned fixed-point, rounding toward zero, (vector and scalar form)             | FCVTZU (vector, fixed-point)                                         |

## C3.8.21.2 Integer conversion

Table C3-134 shows the SIMD integer conversion instructions.

## Table C3-134 SIMD integer conversion instructions

| Mnemonic   | Instruction                                                             | See                         |
|------------|-------------------------------------------------------------------------|-----------------------------|
| SCVTF      | Signed integer convert to floating-point (vector and scalar form)       | SCVTF (vector, integer)     |
|            | Signed fixed-point convert to floating-point (vector and scalar form)   | SCVTF (vector, fixed-point) |
| UCVTF      | Unsigned integer convert to floating-point (vector and scalar form)     | UCVTF (vector, integer)     |
|            | Unsigned fixed-point convert to floating-point (vector and scalar form) | UCVTF (vector, fixed-point) |

## C3.8.21.3 FP8 floating-point conversion

Convert each floating-point element of the source vector while scaling the value, and place the results in the corresponding elements of the destination vector.

For instructions that convert other floating-point formats to FP8 formats, each input element is scaled by adding the value specified in FPMR.NSCALE to its unbounded exponent during the conversion.

For instructions that convert FP8 formats to other floating-point formats, each input element is scaled by subtracting the value specified in FPMR.LSCALE or FPMR.LSCALE2 from its unbounded exponent during the conversion.

For more information, see the instruction descriptions.

Table C3-135 shows the SIMD FP8 floating-point conversion instructions.

## Table C3-135 SIMD FP8 floating-point conversion instructions

| Mnemonic                             | Instruction                                                          | See                                                      |
|--------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------|
| BF1CVTL, BF1CVTL2, BF2CVTL, BF2CVTL2 | 8-bit floating-point convert to BFloat16 (vector)                    | BF1CVTL, BF1CVTL2, BF2CVTL, BF2CVTL2                     |
| F1CVTL, F1CVTL2, F2CVTL, F2CVTL2     | 8-bit floating-point convert to half-precision (vector)              | F1CVTL, F1CVTL2, F2CVTL, F2CVTL2                         |
| FCVTN                                | Half-precision to 8-bit floating-point convert and narrow (vector)   | FCVTN (half-precision to 8-bit floating-point)           |
| FCVTN , FCVTN2                       | Single-precision to 8-bit floating-point convert and narrow (vector) | FCVTN, FCVTN2 (single-precision to 8-bit floating-point) |

## C3.8.22 SIMD reduce (across vector lanes)

The SIMD reduce (across vector lanes) instructions perform arithmetic operations horizontally, that is across all lanes of the input vector. They deliver a single scalar result.

Table C3-136 shows the SIMD reduce (across vector lanes) instructions.

Table C3-136 SIMD reduce (across vector lanes) instructions

| Mnemonic   | Instruction                                   | See     |
|------------|-----------------------------------------------|---------|
| ADDV       | Add (across vector)                           | ADDV    |
| FMAXNMV    | Floating-point maximum number (across vector) | FMAXNMV |
| FMAXV      | Floating-point maximum (across vector)        | FMAXV   |
| FMINNMV    | Floating-point minimum number (across vector) | FMINNMV |
| FMINV      | Floating-point minimum (across vector)        | FMINV   |
| SADDLV     | Signed add long (across vector)               | SADDLV  |
| SMAXV      | Signed maximum (across vector)                | SMAXV   |
| SMINV      | Signed minimum (across vector)                | SMINV   |

| Mnemonic   | Instruction                       | See    |
|------------|-----------------------------------|--------|
| UADDLV     | Unsigned add long (across vector) | UADDLV |
| UMAXV      | Unsigned maximum (across vector)  | UMAXV  |
| UMINV      | Unsigned minimum (across vector)  | UMINV  |

## C3.8.23 SIMD pairwise arithmetic

The SIMD pairwise arithmetic instructions perform operations on pairs of adjacent elements and deliver a vector result.

Table C3-137 shows the SIMD pairwise arithmetic instructions.

## Table C3-137 SIMD pairwise arithmetic instructions

| Mnemonic   | Instruction                                                     | See                             |
|------------|-----------------------------------------------------------------|---------------------------------|
| ADDP       | Add pairwise (vector and scalar form)                           | ADDP(vector) ADDP(scalar)       |
| FADDP      | Floating-point add pairwise (vector and scalar form)            | FADDP (vector) FADDP (scalar)   |
| FMAXNMP    | Floating-point maximum number pairwise (vector and scalar form) | FMAXNMP(vector) FMAXNMP(scalar) |
| FMAXP      | Floating-point maximum pairwise (vector and scalar form)        | FMAXP(vector) FMAXP(scalar)     |
| FMINNMP    | Floating-point minimum number pairwise (vector and scalar form) | FMINNMP(vector) FMINNMP(scalar) |
| FMINP      | Floating-point minimum pairwise (vector and scalar form)        | FMINP (vector) FMINP (scalar)   |
| SMAXP      | Signed maximum pairwise                                         | SMAXP                           |
| SMINP      | Signed minimum pairwise                                         | SMINP                           |
| UMAXP      | Unsigned maximum pairwise                                       | UMAXP                           |
| UMINP      | Unsigned minimum pairwise                                       | UMINP                           |

## C3.8.24 SIMD dot product

## C3.8.24.1 Integer dot product

FEAT\_DotProd provides SIMD instructions that perform the dot product of the four 8-bit subelements of the 32-bit elements of one vector with the four 8-bit subelements of a second vector. It provides two forms of the instructions, each with signed and unsigned versions:

| Vector form   | The dot product is calculated for each element of the first vector with the corresponding element of the second vector.                                                                                                                                                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Indexed form  | The dot product is calculated for each element of the first vector with the element of the second vector that is indicated by the index argument to the instruction. Note That is, a single element from the second vector is used, and the dot product is calculated between each element of the first vector and this single element from the second vector. |

Table C3-138 shows the SIMD integer dot product instructions.

## Table C3-138 SIMD integer dot product instructions

| Mnemonic   | Instruction                                            | See               |
|------------|--------------------------------------------------------|-------------------|
| SDOT       | Signed dot product (vector form)                       | SDOT (vector)     |
| UDOT       | Unsigned dot product (vector form)                     | UDOT(vector)      |
| SDOT       | Signed dot product (indexed form)                      | SDOT (by element) |
| UDOT       | Unsigned dot product (indexed form)                    | UDOT(by element)  |
| USDOT      | Mixed sign integer dot product (vector form) a         | USDOT(vector)     |
|            | Mixed sign integer dot product by indexed quadruplet a | USDOT(by element) |
| SUDOT      | Mixed sign integer dot product by indexed quadruplet a | SUDOT(by element) |

## C3.8.24.2 FP8 floating-point dot product

The FP8 floating-point dot product instructions accumulate the dot product of two or four adjacent FP8 source elements into half-precision or single-precision destination elements. They generate a fused, downscaled sum-of-products and accumulate into each destination element, without intermediate rounding.

For these instructions, the unbounded intermediate sum-of-products is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

Table C3-139 shows these instructions.

## Table C3-139 SIMD FP8 floating-point dot product instructions

| Mnemonic   | Instruction                                                               | See                                                         |
|------------|---------------------------------------------------------------------------|-------------------------------------------------------------|
| FDOT       | 8-bit floating-point dot product to half-precision (vector, by element)   | FDOT (8-bit floating-point to half-precision, by element)   |
| FDOT       | 8-bit floating-point dot product to half-precision (vector)               | FDOT (8-bit floating-point to half-precision, vector)       |
| FDOT       | 8-bit floating-point dot product to single-precision (vector, by element) | FDOT (8-bit floating-point to single-precision, by element) |
| FDOT       | 8-bit floating-point dot product to single-precision (vector)             | FDOT (8-bit floating-point to single-precision, vector)     |

## C3.8.25 SIMD matrix multiply-accumulate

## C3.8.25.1 Integer matrix multiply-accumulate

The integer matrix multiply-accumulate instructions are implemented by FEAT\_I8MM.

The source and destination vectors of this instruction are organized as follows:

- In the first source vector, a 2x8 matrix of 8-bit integers in row-by-row order.

- In the second source vector, an 8x2 matrix of 8-bit integers in column-by-column order.
- In the destination vector, a 2x2 matrix of 32-bit integers in row-by-row order.

One matrix multiplication is performed per vector and accumulated into the destination vector.

Table C3-140 shows these instructions.

## Table C3-140 SIMD integer matrix multiply-accumulate instructions

| Mnemonic   | Instruction                                                            | See            |
|------------|------------------------------------------------------------------------|----------------|
| SMMLA      | Widening signed 8-bit to 32-bit integer matrix multiply-accumulate     | SMMLA(vector)  |
| UMMLA      | Widening unsigned 8-bit to 32-bit integer matrix multiply-accumulate   | UMMLA(vector)  |
| USMMLA     | Widening mixed sign 8-bit to 32-bit integer matrix multiply-accumulate | USMMLA(vector) |

## C3.8.25.2 FP8 matrix multiply-accumulate

The FP8 FMMLA (widening, 8-bit floating-point to single-precision) instruction is implemented by FEAT\_F8F32MM. The source and destination vectors of this instruction are organized as follows:

- In the first source vector, a 2x8 matrix of 8-bit floating-point values in row-by-row order.
- In the second source vector, an 8x2 matrix of 8-bit floating-point values in column-by-column order.
- In the destination vector, a 2x2 matrix of single-precision values in row-by-row order.

One matrix multiplication is performed per vector and accumulated into the destination vector.

The FP8 FMMLA (widening, 8-bit floating-point to half-precision) instruction is implemented by FEAT\_F8F16MM. This instruction delimits each source and destination vector into 64-bit segments. The 64-bit segments are organized as follows:

- In the first source vector, a 2x4 matrix of 8-bit floating-point values in row-by-row order.
- In the second source vector, a 4x2 matrix of 8-bit floating-point values in column-by-column order.
- In the destination vector, a 2x2 matrix of half-precision values in row-by-row order.

One matrix multiplication is performed per vector segment and accumulated into the destination vector segment.

These instructions generate a fused, downscaled sum-of-products and accumulate into each destination element, without intermediate rounding.

For these instructions, the intermediate sum of products is downscaled by subtracting the value in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

## Table C3-141 SIMD FP8 matrix multiply-accumulate instructions

| Mnemonic   | Instruction                                                                      | See                                                       |
|------------|----------------------------------------------------------------------------------|-----------------------------------------------------------|
| FMMLA      | 8-bit floating-point matrix multiply-accumulate into 2x2 single-precision matrix | FMMLA(widening, 8-bit floating-point to single-precision) |
| FMMLA      | 8-bit floating-point matrix multiply-accumulate into 2x2 half-precision matrix   | FMMLA(widening, 8-bit floating-point to half-precision)   |

## C3.8.26 SIMD table lookup

## C3.8.26.1 Table vector lookup

Table C3-142 shows the SIMD table vector lookup instructions.

## Table C3-142 SIMD table vector lookup instructions

| Mnemonic   | Instruction                   | See   |
|------------|-------------------------------|-------|
| TBL        | Table vector lookup           | TBL   |
| TBX        | Table vector lookup extension | TBX   |

## C3.8.26.2 Lookup table using 2-bit or 4-bit indices

Copy indexed elements from the first source vector(s) to the destination vector, using packed indices from a portion of the second source vector.

Table C3-143 shows the SIMD lookup table instructions.

## Table C3-143 SIMD lookup table using 2-bit or 4-bit indices instructions

| Mnemonic   | Instruction                      | See   |
|------------|----------------------------------|-------|
| LUTI2      | Lookup table using 2-bit indices | LUTI2 |
| LUTI4      | Lookup table using 4-bit indices | LUTI4 |

## C3.8.27 SIMD complex number arithmetic instructions

FEAT\_FCMA provides SIMD instructions that perform arithmetic on complex numbers held in element pairs in vector registers, where the less significant element of the pair contains the real component and the more significant element contains the imaginary component.

These instructions provide double-precision and single-precision versions. If FEAT\_FP16 is implemented they also provide half-precision versions, otherwise the half-precision encodings are UNDEFINED.

Table C3-144 shows the FEAT\_FCMA SIMD instructions.

Table C3-144 SIMD complex number arithmetic instructions

| Mnemonic   | Instruction                                               | See               |
|------------|-----------------------------------------------------------|-------------------|
| FCADD      | Floating-point complex add                                | FCADD             |
| FCMLA      | Floating-point complex multiply accumulate (vector form)  | FCMLA             |
| FCMLA      | Floating-point complex multiply accumulate (indexed form) | FCMLA(by element) |

Apair of FCMLA instructions can be used to perform a complex number multiplication. This is demonstrated in Complex multiplication.

## C3.8.28 SIMD multiply-accumulate

## C3.8.28.1 Floating-point fused multiply-accumulate

The SIMD floating-point fused multiply-accumulate instructions multiply the vector elements in the first source SIMD&amp;FP register by the corresponding value in the second source SIMD&amp;FP register, and accumulate or subtract the product in the vector elements of the destination SIMD&amp;FP register.

Table C3-145 shows these instructions.

## Table C3-145 SIMD floating-point fused multiply-accumulate instructions

| Mnemonic       | Instruction                                               | See                    |
|----------------|-----------------------------------------------------------|------------------------|
| FMLA           | Floating-point fused multiply-add (vector form)           | FMLA(vector)           |
| FMLAL , FMLAL2 | Floating-point fused multiply-add long (vector form)      | FMLAL, FMLAL2 (vector) |
| FMLS           | Floating-point fused multiply-subtract (vector form)      | FMLS (vector)          |
| FMLSL , FMLSL2 | Floating-point fused multiply-subtract long (vector form) | FMLSL, FMLSL2 (vector) |

## C3.8.28.2 FP8 floating-point widening multiply-accumulate

The FP8 floating-point multiply-accumulate instructions widen the 8-bit floating-point elements in the source vectors to half-precision or single-precision format and multiply the corresponding elements.

They generate a fused, downscaled product and accumulate into the corresponding elements of the destination vector, without intermediate rounding.

For these instructions, the unbounded intermediate product is scaled by subtracting the value specified in FPMR.LSCALE from its unbounded exponent. For more information, see the instruction descriptions.

Table C3-146 shows these instructions.

## Table C3-146 SIMD FP8 floating-point widening multiply-accumulate instructions

| Mnemonic                               | Instruction                                                                          | See                                                 |
|----------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------|
| FMLALB, FMLALT                         | 8-bit floating-point multiply-add long to half-precision (vector, by element)        | FMLALB, FMLALT (by element)                         |
| FMLALB, FMLALT                         | 8-bit floating-point multiply-add long to half-precision (vector)                    | FMLALB, FMLALT (vector)                             |
| FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT | 8-bit floating-point multiply-add long-long to single-precision (vector, by element) | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (by element) |
| FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT | 8-bit floating-point multiply-add long-long to single-precision (vector)             | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (vector)     |

## C3.8.29 SIMD BFloat16

If FEAT\_BF16 is implemented, the instructions in this section are available.

## C3.8.29.1 SIMD BFloat16 floating-point multiply-add

The BFloat16 floating-point multiply-add instructions perform an implicit conversion of the bottom (even-numbered) or top (odd-numbered) BFloat16 source elements to IEEE 754 single-precision floating-point format before performing a fused multiply-add without intermediate rounding to the overlapping single-precision destination element. These instructions follow the normal floating-point behaviors that apply to single-precision arithmetic, controlled by the Effective value of the FPCR, and captured in the FPSR cumulative exception bits.

## Table C3-147 SIMD BFloat16 floating-point multiply-add instructions

| Mnemonic   | Instruction                                                                          | See                                                     |
|------------|--------------------------------------------------------------------------------------|---------------------------------------------------------|
| BFMLALB    | BFloat16 floating-point widening multiply-add long bottom (vector and indexed forms) | BFMLALB, BFMLALT (vector) BFMLALB, BFMLALT (by element) |
| BFMLALT    | BFloat16 floating-point widening multiply-add long top (vector and index forms)      | BFMLALB, BFMLALT (vector) BFMLALB, BFMLALT (by element) |

## C3.8.29.2 SIMD BFloat16 floating-point dot product

The BFloat16 floating-point dot product instruction, BFDOT , performs an implicit conversion of vectors of BFloat16 input values to IEEE 754 single-precision floating-point format.

The BFloat16 dot product instructions delimit their source vectors into pairs of BFloat16 elements.

## Table C3-148 SIMD BFloat16 floating-point dot product instructions

| Mnemonic   | Instruction                                                    | See                               |
|------------|----------------------------------------------------------------|-----------------------------------|
| BFDOT      | BFloat16 floating-point dot product (vector and indexed forms) | BFDOT (vector) BFDOT (by element) |

## C3.8.29.3 SIMD BFloat16 floating-point matrix multiply-accumulate

The BFloat16 floating-point matrix multiply-accumulate instruction, BFMMLA is implemented by FEAT\_BF16.

The source and destination vectors of this instruction are organized as follows:

- In the first source vector, a 2x4 matrix of BFloat16 values in row-by-row order.
- In the second source vector, a 4x2 matrix of BFloat16 values in column-by-column order.
- In the destination vector, a 2x2 matrix of single-precision values in row-by-row order.

One matrix multiplication is performed per source vector and accumulated into the corresponding destination vector. This corresponds to accumulating two 2-way BFloat16 widening dot products into each single-precision destination element, following the numeric behaviors described for BFDOT instruction in SIMD BFloat16 floating-point dot product.

## Table C3-149 SIMD BFloat16 floating-point matrix multiply instructions

| Mnemonic   | Instruction                                                        | See    |
|------------|--------------------------------------------------------------------|--------|
| BFMMLA     | BFloat16 floating-point matrix multiply-accumulate into 2x2 matrix | BFMMLA |

## C3.8.29.4 SIMD BFloat16 floating-point convert

The BFloat16 floating-point convert instructions perform accurately rounded down-conversion of single-precision source vector elements to BFloat16 format.

Table C3-150 SIMD BFloat16 floating-point convert instructions

| Mnemonic         | Instruction                                                                   | See             |
|------------------|-------------------------------------------------------------------------------|-----------------|
| BFCVTN , BFCVTN2 | Floating-point convert from single-precision to BFloat16 format (vector form) | BFCVTN, BFCVTN2 |

## C3.8.30 The Cryptographic Extension in AArch64 state

## C3.8.30.1 The Armv8.0 Cryptographic Extension

The instructions provided by the OPTIONAL Armv8.0 Cryptographic Extension use the SIMD and floating-point register file. For more information about the functions they provide, see:

- Advanced Encryption Standard (AES) .
- Secure Hash Algorithm (SHA) .
- The Galois/Counter Mode of Operation .

Table C3-151 shows the Armv8.0 Cryptographic Extension instructions.

Table C3-151 Cryptographic Extension instructions

| Mnemonic   | Instruction                 | See             |
|------------|-----------------------------|-----------------|
| AESD       | AES single round decryption | AESD            |
| AESE       | AES single round encryption | AESE            |
| AESIMC     | AES inverse mix columns     | AESIMC          |
| AESMC      | AES mix columns             | AESMC           |
| PMULL      | Polynomial multiply long    | PMULL, PMULL2 a |
| SHA1C      | SHA1 hash update (choose)   | SHA1C           |
| SHA1H      | SHA1 fixed rotate           | SHA1H           |
| SHA1M      | SHA1 hash update (majority) | SHA1M           |
| SHA1P      | SHA1 hash update (parity)   | SHA1P           |
| SHA1SU0    | SHA1 schedule update 0      | SHA1SU0         |
| SHA1SU1    | SHA1 schedule update 1      | SHA1SU1         |
| SHA256H    | SHA256 hash update, part 1  | SHA256H         |
| SHA256H2   | SHA256 hash update, part 2  | SHA256H2        |
| SHA256SU0  | SHA256 schedule update 0    | SHA256SU0       |
| SHA256SU1  | SHA256 schedule update 1    | SHA256SU1       |

## C3.8.30.2 Armv8.2 extensions to the Cryptographic Extension

Armv8.2 supports the following OPTIONAL extensions to the Cryptographic Extension:

- FEAT\_SHA512, SHA2-512 functionality.
- FEAT\_SHA3, SHA3 functionality.
- FEAT\_SM3, SM3 functionality.
- FEAT\_SM4, SM4 functionality.

## C3.8.30.2.1 FEAT\_SHA512, SHA2-512 functionality

FEAT\_SHA512 provides instructions to accelerate the SHA-2 hash algorithm using a digest that is larger than 256 bits. The relevant standards are SHA-384, SHA-512, SHA-512|224 and SHA-512|256. These are all based on the SHA-512 computation, and therefore this set of instructions is described as the SHA512 instructions .

Implementation of FEAT\_SHA512 requires the implementation of the SHA1 and SHA2-256 instructions from the Armv8.0 Cryptographic Extension.

Note

Implementation of FEAT\_SHA512 does not require the implementation of the AES instructions, and the 64-bit polynomial variants of the PMULL instructions, from the Armv8.0 Cryptographic Extension.

When FEAT\_SHA512 is implemented, the value of ID\_AA64ISAR0\_EL1.SHA2 is 0b0010 , indicating support for the SHA512 instructions.

Table C3-152 shows the FEAT\_SHA512 instructions:

## Table C3-152 FEAT\_SHA512 instructions

| Mnemonic   | Instruction               | See       |
|------------|---------------------------|-----------|
| SHA512H    | SHA512 Hash update part 1 | SHA512H   |
| SHA512H2   | SHA512 Hash update part 2 | SHA512H2  |
| SHA512SU0  | SHA512 Schedule Update 0  | SHA512SU0 |
| SHA512SU1  | SHA512 Schedule Update 1  | SHA512SU1 |

Use of the SHA512 instructions shows an example of the use of these instructions to calculate a SHA512 hash iteration. This example code is not part of the architectural definition of these instructions.

## C3.8.30.2.2 FEAT\_SHA3, SHA3 functionality

FEAT\_SHA3 provides instructions to accelerate the SHA-3 hash algorithm. This set of instructions is described as the SHA3 instructions.

Note

Implementation of FEAT\_SHA3 does not require the implementation of the AES instructions, and the 64-bit polynomial variants of the PMULL instructions, from the Armv8.0 Cryptographic Extension.

When FEAT\_SHA3 is implemented, the value of ID\_AA64ISAR0\_EL1.SHA3 is 0b0001 , indicating support for the SHA3 instructions.

Table C3-153 shows the FEAT\_SHA3 instructions. The SHA-3 hash algorithm is based on a running digest of 1600 bytes, arranged as a five by five array of 64-bit registers. The Arm acceleration of these instructions is based on mapping the 25 64-bit values into 25 vector registers, with each 64-bit value occupying the same 64-bit element in each vector. A series of transformations is performed on these registers as part of a round of the SHA-3 hash calculation.

The SIMD nature of the vector registers means the acceleration can compute two parallel SHA3 hash calculations, where one calculation is performed using the zeroth 64-bit element of each vector, and the other calculation is performed using the first 64-bit element of each vector.

To provide acceleration where the SIMD calculation is not required, the instructions provide variants that operate only on the zeroth 64-bit elements. These are provided as a power optimization.

## Table C3-153 FEAT\_SHA3 instructions

| Mnemonic   | Instruction               | See   |
|------------|---------------------------|-------|
| BCAX       | Bit Clear and ExclusiveOR | BCAX  |
| EOR3       | Three-way ExclusiveOR     | EOR3  |
| RAX1       | Rotate and ExclusiveOR    | RAX1  |
| XAR        | Exclusive ORand Rotate    | XAR   |

Use of the SHA3 instructions shows an example of the use of these instructions to calculate the combined theta, phi, rho and chi operations of a SHA3 iteration. This example code is not part of the architectural definition of these instructions.

## C3.8.30.2.3 FEAT\_SM3, SM3 functionality

FEAT\_SM3 provides instructions to accelerate the SM3 hash algorithm, the standard Chinese hash algorithm. These are described as the SM3 instructions.

FEAT\_SM3 can be implemented independently of any part of the Armv8.0 Cryptographic Extension, and independently of FEAT\_SHA512.

Note

This means that Armv8.2 permits an implementation of the Cryptographic Extension that provides only the FEAT\_SM3 functionality.

When FEAT\_SM3 is implemented, the value of ID\_AA64ISAR0\_EL1.SM3 is 0b0001 , indicating support for the SM3 instructions.

Table C3-154 shows the FEAT\_SM3 instructions. The SM3 algorithm computes a digest of 256 bits, which can be held in two vector registers. The SM3 instructions include instructions to accelerate the computation of the hash and the schedule update.

Note

The SM3 instruction names refer to intermediate variables defined as part of the SM3 Cryptographic Hash Algorithm specification.

## Table C3-154 FEAT\_SM3 instructions

| Mnemonic   | Instruction                  | See       |
|------------|------------------------------|-----------|
| SM3SS1     | SM3 SS1 calculation          | SM3SS1    |
| SM3TT1A    | SM3 TT1 calculation, partA   | SM3TT1A   |
| SM3TT1B    | SM3 TT1 calculation, partB   | SM3TT1B   |
| SM3TT2A    | SM3 TT2 calculation, partA   | SM3TT2A   |
| SM3TT2B    | SM3 TT2 calculation, partB   | SM3TT2B   |
| SM3PARTW1  | SM3 PARTWcalculation, part 1 | SM3PARTW1 |
| SM3PARTW2  | SM3 PARTWcalculation, part 1 | SM3PARTW2 |

Use of the SM3 instructions shows an example of the use of these instructions to generate an SM3 hash. This example code is not part of the architectural definition of these instructions.

## C3.8.30.2.4 FEAT\_SM4, SM4 functionality

FEAT\_SM4 provides instruction to accelerate the SM4 encryption algorithm, the standard Chinese encryption algorithm. This set of instructions is described as the SM4 instructions.

FEAT\_SM4 can be implemented independently of any part of the Armv8.0 Cryptographic Extension, and independently of FEAT\_SHA3.

Note

This means that Armv8.2 permits an implementation of the Cryptographic Extension that provides only the FEAT\_SM4 functionality.

When FEAT\_SM4 is implemented, the value of ID\_AA64ISAR0\_EL1.SM4 is 0b0001 , indicating support for the SM4 instructions.

Table C3-155 shows the FEAT\_SM4 instructions. The SM4 algorithm is 128-bit wide block cipher. The SM4E instruction accelerates a single round of encryption or decryption, and the SM4EKEY instruction accelerates a single round of key generation:

## Table C3-155 FEAT\_SM4 instructions

| Mnemonic   | Instruction   | See     |
|------------|---------------|---------|
| SM4E       | SM4 Encrypt   | SM4E    |
| SM4EKEY    | SM4 Key       | SM4EKEY |

Use of the SM4 instructions shows an example of the use of these instructions to perform SM4 encryption and decryption. This example code is not part of the architectural definition of these instructions.