## F2.13 Advanced SIMD data-processing instructions

Advanced SIMD data-processing instructions process registers containing vectors of elements of the same type packed together, enabling the same operation to be performed on multiple items in parallel.

Instructions operate on vectors held in 64-bit or 128-bit registers. Figure F2-2 shows an operation on two 64-bit operand vectors, generating a 64-bit vector result.

Note

Figure F2-2 and other similar figures show 64-bit vectors that consist of four 16-bit elements, and 128-bit vectors that consist of four 32-bit elements. Other element sizes produce similar figures, but with 1, 2, 8, or 16 operations performed in parallel instead of 4.

Figure F2-2 Advanced SIMD instruction operating on 64-bit registers

<!-- image -->

Many Advanced SIMD instructions have variants that produce vectors of elements double the size of the inputs. In this case, the number of elements in the result vector is the same as the number of elements in the operand vectors, but each element, and the whole vector, is double the size.

Figure F2-3 shows an example of an Advanced SIMD instruction operating on 64-bit registers, and generating a 128-bit result.

Figure F2-3 Advanced SIMD instruction producing wider result

<!-- image -->

There are also Advanced SIMD instructions that have variants that produce vectors containing elements half the size of the inputs. Figure F2-4 shows an example of an Advanced SIMD instruction operating on one 128-bit register, and generating a 64-bit result.

Figure F2-4 Advanced SIMD instruction producing narrower result

<!-- image -->

Some Advanced SIMD instructions do not conform to these standard patterns. Their operation patterns are described in the individual instruction descriptions.

Advanced SIMD instructions that perform floating-point arithmetic use the Arm standard floating-point arithmetic defined in Floating-point support.

The following sections summarize the Advanced SIMD data-processing instructions:

- Advanced SIMD parallel addition and subtraction.
- Bitwise Advanced SIMD data-processing instructions.
- Advanced SIMD comparison instructions.
- Advanced SIMD shift instructions.
- Advanced SIMD multiply instructions.
- Advanced SIMD dot product instructions.
- Miscellaneous Advanced SIMD data-processing instructions.
- Advanced SIMD BFloat16 instructions.
- Advanced SIMD matrix multiply instructions.
- The Cryptographic Extension in AArch32 state.

## F2.13.1 Advanced SIMD parallel addition and subtraction

Table F2-20 shows the Advanced SIMD parallel add and subtract instructions.

Table F2-20 Advanced SIMD parallel add and subtract instructions

| Instruction                                | See                                  |
|--------------------------------------------|--------------------------------------|
| Vector Add                                 | VADD(integer) VADD(floating-point)   |
| Vector Add and Narrow, returning High Half | VADDHN                               |
| Vector Add Long                            | VADDL                                |
| Vector Add Wide                            | VADDW                                |
| Vector Halving Add                         | VHADD                                |
| Vector Halving Subtract                    | VHSUB                                |
| Vector Pairwise Add and Accumulate Long    | VPADAL                               |
| Vector Pairwise Add                        | VPADD(integer) VPADD(floating-point) |

| Instruction                                              | See                                |
|----------------------------------------------------------|------------------------------------|
| Vector Pairwise Add Long                                 | VPADDL                             |
| Vector Rounding Add and Narrow, returning High Half      | VRADDHN                            |
| Vector Rounding Halving Add                              | VRHADD                             |
| Vector Rounding Subtract and Narrow, returning High Half | VRSUBHN                            |
| Vector Saturating Add                                    | VQADD                              |
| Vector Saturating Subtract                               | VQSUB                              |
| Vector Subtract                                          | VSUB(integer) VSUB(floating-point) |
| Vector Subtract and Narrow, returning High Half          | VSUBHN                             |
| Vector Subtract Long                                     | VSUBL                              |
| Vector Subtract Wide                                     | VSUBW                              |

## F2.13.2 Bitwise Advanced SIMD data-processing instructions

Table F2-21 shows bitwise Advanced SIMD data-processing instructions. These operate on the doubleword (64-bit) or quadword (128-bit) registers in the SIMD and floating-point register file, and there is no division into vector elements.

Table F2-21 Bitwise Advanced SIMD data-processing instructions

| Instruction                               | See                              |
|-------------------------------------------|----------------------------------|
| Vector BitwiseAND                         | VAND(register)                   |
| Vector Bitwise Bit Clear (AND complement) | VBIC (immediate) VBIC (register) |
| Vector Bitwise ExclusiveOR                | VEOR                             |
| Vector Bitwise Insert if False            | VBIF                             |
| Vector Bitwise Insert if True             | VBIT                             |
| Vector Bitwise Move                       | VMOV(immediate) VMOV(register)   |
| Vector BitwiseNOT                         | VMVN(immediate) VMVN(register)   |
| Vector BitwiseOR                          | VORR(immediate) VORR(register)   |
| Vector BitwiseORNOT                       | VORN(register)                   |
| Vector Bitwise Select                     | VBSL                             |

## F2.13.3 Advanced SIMD comparison instructions

Table F2-22 shows Advanced SIMD comparison instructions.

## Table F2-22 Advanced SIMD comparison instructions

| Instruction                                   | See                 |
|-----------------------------------------------|---------------------|
| Vector Absolute Compare Greater Than or Equal | VACGE               |
| Vector Absolute Compare Greater Than          | VACGT               |
| Vector Compare Equal                          | VCEQ(register)      |
| Vector Compare Equal to Zero                  | VCEQ(immediate #0)  |
| Vector Compare Greater Than or Equal          | VCGE(register)      |
| Vector Compare Greater Than or Equal to Zero  | VCGE(immediate #0)  |
| Vector Compare Greater Than                   | VCGT(register)      |
| Vector Compare Greater Than Zero              | VCGT(immediate #0)  |
| Vector Compare Less Than or Equal to Zero     | VCLE (immediate #0) |
| Vector Compare Less Than Zero                 | VCLT (immediate #0) |
| Vector Test Bits                              | VTST                |

## F2.13.4 Advanced SIMD shift instructions

Table F2-23 lists the shift instructions in the Advanced SIMD instruction set.

## Table F2-23 Advanced SIMD shift instructions

| Instruction                                       | See                                      |
|---------------------------------------------------|------------------------------------------|
| Vector Saturating Rounding Shift Left             | VQRSHL                                   |
| Vector Saturating Rounding Shift Right and Narrow | VQRSHRN,VQRSHRUN                         |
| Vector Saturating Shift Left                      | VQSHL(register) VQSHL, VQSHLU(immediate) |
| Vector Saturating Shift Right and Narrow          | VQSHRN,VQSHRUN                           |
| Vector Rounding Shift Left                        | VRSHL                                    |
| Vector Rounding Shift Right                       | VRSHR                                    |
| Vector Rounding Shift Right and Accumulate        | VRSRA                                    |
| Vector Rounding Shift Right and Narrow            | VRSHRN                                   |
| Vector Shift Left                                 | VSHL (immediate) VSHL (register)         |
| Vector Shift Left Long                            | VSHLL                                    |
| Vector Shift Right                                | VSHR                                     |
| Vector Shift Right and Narrow                     | VSHRN                                    |
| Vector Shift Left and Insert                      | VSLI                                     |
| Vector Shift Right and Accumulate                 | VSRA                                     |
| Vector Shift Right and Insert                     | VSRI                                     |

## F2.13.5 Advanced SIMD multiply instructions

Table F2-24 shows the Advanced SIMD multiply instructions.

## Table F2-24 Advanced SIMD multiply instructions

| Instruction                                                                 | See                                                               |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------|
| Vector Multiply Accumulate                                                  | VMLA(integer) VMLA(floating-point) VMLA(by scalar)                |
| Vector Multiply Accumulate Long                                             | VMLAL(integer) VMLAL(by scalar)                                   |
| Vector Multiply Subtract                                                    | VMLS(integer) VMLS(floating-point) VMLS(by scalar)                |
| Vector Multiply Subtract Long                                               | VMLSL(integer) VMLSL(by scalar)                                   |
| Vector Multiply                                                             | VMUL(integer and polynomial) VMUL(floating-point) VMUL(by scalar) |
| Vector Multiply Long                                                        | VMULL(integer and polynomial) VMULL(by scalar)                    |
| Vector Fused Multiply Accumulate                                            | VFMA                                                              |
| Vector Floating-Point Multiply-Add Long                                     | VFMAL(vector) VFMAL(by scalar)                                    |
| Vector Fused Multiply Subtract                                              | VFMS                                                              |
| Vector Floating-Point Multiply-Subtract Long                                | VFMSL(vector) VFMSL(by scalar)                                    |
| Vector Saturating Doubling Multiply Accumulate Long                         | VQDMLAL                                                           |
| Vector Saturating Doubling Multiply Subtract Long                           | VQDMLSL                                                           |
| Vector Saturating Doubling Multiply Returning High Half                     | VQDMULH                                                           |
| Vector Saturating Doubling Multiply Long                                    | VQDMULL                                                           |
| Vector Saturating Rounding Doubling Multiply Accumulate Returning High Half | VQRDMLAH                                                          |
| Vector Saturating Rounding Doubling Multiply Subtract Returning High Half   | VQRDMLSH                                                          |
| Vector Saturating Rounding Doubling Multiply Returning High Half            | VQRDMULH                                                          |

Advanced SIMD multiply instructions can operate on vectors of:

- 8-bit, 16-bit, or 32-bit unsigned integers.
- 8-bit, 16-bit, or 32-bit signed integers.
- 8-bit polynomials over {0, 1}. VMUL and VMULL are the only instructions that operate on polynomials. VMULL produces a 16-bit polynomial over {0, 1}.
- Single-precision (32-bit) or half-precision (16-bit) floating-point numbers.

They can also act on one vector and one scalar.

Long instructions have doubleword (64-bit) operands, and produce quadword (128-bit) results. Other Advanced SIMD multiply instructions can have either doubleword or quadword operands, and produce results of the same size.

Floating-point multiply instructions can operate on:

- Half-precision (16-bit) floating-point numbers.
- Single-precision (32-bit) floating-point numbers.
- Double-precision (64-bit) floating-point numbers.

## F2.13.6 Advanced SIMD dot product instructions

FEAT\_DotProd provides SIMD instructions that perform the dot product of the four 8-bit subelements of the 32-bit elements of one vector with the four 8-bit subelements of a second vector. It provides two forms of the instructions, each with signed and unsigned versions:

Vector form

The dot product is calculated for each element of the first vector with the corresponding element of the second vector.

Indexed form

The dot product is calculated for each element of the first vector with the element of the second vector that is indicated by the index argument to the instruction.

Note

That is, a single element from the second vector is used, and the dot product is calculated between each element of the first vector and this single element from the second vector.

Table F2-25 shows the Advanced SIMD dot product instructions.

## Table F2-25 Advanced SIMD dot product instructions

| Mnemonic   | Instruction                                            | See                |
|------------|--------------------------------------------------------|--------------------|
| VSDOT      | Signed dot product (vector form)                       | VSDOT(vector)      |
| VUDOT      | Unsigned dot product (vector form)                     | VUDOT(vector)      |
| VSDOT      | Signed dot product (indexed form)                      | VSDOT(by element)  |
| VSUDOT     | Mixed sign integer dot product by indexed quadruplet a | VSUDOT(by element) |
| VUDOT      | Unsigned dot product (indexed form)                    | VUDOT(by element)  |
| VUSDOT     | Mixed sign integer dot product (vector format) a       | VUSDOT(vector)     |
| VUSDOT     | Mixed sign integer dot product by indexed quadruplet a | VUSDOT(by element) |

## F2.13.7 AArch32 Advanced SIMD complex number arithmetic instructions

FEAT\_FCMA provides AArch32 Advanced SIMD instructions that perform arithmetic on complex numbers held in element pairs in vector registers, where the less significant element of the pair contains the real component and the more significant element contains the imaginary component.

These instructions provide single-precision versions. If FEAT\_FP16 is implemented they also provide half-precision versions, otherwise the half-precision encodings are UNDEFINED.

Table F2-26 shows the FEAT\_FCMA AArch32 Advanced SIMD instructions.

## Table F2-26 Advanced SIMD complex number arithmetic instructions

| Mnemonic   | Instruction                                               | See               |
|------------|-----------------------------------------------------------|-------------------|
| VCADD      | Floating-point complex add                                | VCADD             |
| VCMLA      | Floating-point complex multiply accumulate (vector form)  | VCMLA             |
| VCMLA      | Floating-point complex multiply accumulate (indexed form) | VCMLA(by element) |

Apair of VCMLA instructions can be used to perform a complex number multiplication. In Complex multiplication, this is demonstrated for the similar AArch64 instruction FCMLA . The usage of VCMLA in this manner is identical.

## F2.13.8 Advanced SIMD BFloat16 instructions

When FEAT\_AA32BF16 is implemented, BFloat16 instructions are available in AArch32 state.

Table F2-27 shows the Advanced SIMD BFloat16 instructions.

Table F2-27 BFloat16 Advanced SIMD instructions

| Mnemonic      | Instruction                                                                       | See                                                             |
|---------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------|
| VDOT          | BFloat16 floating-point vector dot product (vector and by scalar formats)         | VDOT(vector) VDOT(by element)                                   |
| VMMLA         | BFloat16 floating-point matrix multiply-accumulate                                | VMMLA                                                           |
| VFMAB , VFMAT | BFloat16 floating-point widening multiply-add long (vector and by scalar formats) | VFMAB, VFMAT(BFloat16, vector)VFMAB,VFMAT (BFloat16, by scalar) |
| VCVT          | BFloat16 convert from single-precision to BFloat16 format                         | VCVT(from single-precision to BFloat16, Advanced SIMD)          |

## F2.13.9 Advanced SIMD matrix multiply instructions

When FEAT\_AA32I8MM is implemented, these instructions are available in AArch32 state. They include integer and mixed sign dot product instructions.

The matrix multiply-accumulate instructions delimit source and destination vectors into segments. Within each segment:

- The first source vector matrix is organized in row-by-row order.
- The second source vector matrix elements are organized in a column-by-column order.
- The destination vector matrix is organized in row-by-row order.

One matrix multiplication is performed per segment.

Table F2-28 shows the Advanced SIMD matrix multiply instructions.

Table F2-28 Matrix multiply Advanced SIMD instructions

| Mnemonic   | Instruction                                                              | See    |
|------------|--------------------------------------------------------------------------|--------|
| VSMMLA     | Widening 8-bit signed integer matrix multiply-accumulate into 2x2 matrix | VSMMLA |

| Mnemonic   | Instruction                                                                  | See     |
|------------|------------------------------------------------------------------------------|---------|
| VUMMLA     | Widening 8-bit unsigned integer matrix multiply-accumulate into 2x2 matrix   | VUMMLA  |
| VUSMMLA    | Widening 8-bit mixed sign integer matrix multiply-accumulate into 2x2 matrix | VUSMMLA |

## F2.13.10 Miscellaneous Advanced SIMD data-processing instructions

Table F2-29 shows miscellaneous Advanced SIMD data-processing instructions.

## Table F2-29 Miscellaneous Advanced SIMD data-processing instructions

| Instruction                                                | See                                                              |
|------------------------------------------------------------|------------------------------------------------------------------|
| Vector Absolute Difference and Accumulate                  | VABA                                                             |
| Vector Absolute Difference and Accumulate Long             | VABAL                                                            |
| Vector Absolute Difference                                 | VABD(integer) VABD(floating-point)                               |
| Vector Absolute Difference Long                            | VABDL(integer)                                                   |
| Vector Absolute                                            | VABS                                                             |
| Vector Convert between floating-point and fixed-point      | VCVT(between floating-point and fixed-point, Advanced SIMD)      |
| Vector Convert between floating-point and integer          | VCVT(between floating-point and integer, Advanced SIMD)          |
| Vector Convert between half-precision and single-precision | VCVT(between half-precision and single-precision, Advanced SIMD) |
| Vector Count Leading Sign Bits                             | VCLS                                                             |
| Vector Count Leading Zeros                                 | VCLZ                                                             |
| Vector Count Set Bits                                      | VCNT                                                             |
| Vector Duplicate scalar                                    | VDUP(scalar)                                                     |
| Vector Extract                                             | VEXT(byte elements)                                              |
| Vector move Insertion                                      | VINS                                                             |
| Vector Move and Narrow                                     | VMOVN                                                            |
| Vector Move Long                                           | VMOVL                                                            |
| Vector Move extraction                                     | VMOVX                                                            |
| Vector Maximum                                             | VMAX(integer) VMAX(floating-point)                               |
| Vector Minimum                                             | VMIN(integer) VMIN(floating-point)                               |
| Vector Negate                                              | VNEG                                                             |
| Vector Pairwise Maximum                                    | VPMAX(integer) VPMAX(floating-point)                             |
| Vector Pairwise Minimum                                    | VPMIN (integer) VPMIN (floating-point)                           |
| Vector Reciprocal Estimate                                 | VRECPE                                                           |
| Vector Reciprocal Step                                     | VRECPS                                                           |
| Vector Reciprocal Square Root Estimate                     | VRSQRTE                                                          |

| Instruction                        | See            |
|------------------------------------|----------------|
| Vector Reciprocal Square Root Step | VRSQRTS        |
| Vector Reverse in halfwords        | VREV16         |
| Vector Reverse in words            | VREV32         |
| Vector Reverse in doublewords      | VREV64         |
| Vector Saturating Absolute         | VQABS          |
| Vector Saturating Move and Narrow  | VQMOVN,VQMOVUN |
| Vector Saturating Negate           | VQNEG          |
| Vector Swap                        | VSWP           |
| Vector Table Lookup                | VTBL,VTBX      |
| Vector Transpose                   | VTRN           |
| Vector Unzip                       | VUZP           |
| Vector Zip                         | VZIP           |

## F2.13.11 The Cryptographic Extension in AArch32 state

The instructions provided by the optional Cryptographic Extension use the Advanced SIMD and floating-point register file. For more information about the functions they provide see:

- Advanced Encryption Standard (AES) .
- The Galois/Counter Mode of Operation .
- Secure Hash Algorithm (SHA) .

Table F2-30 shows the AArch32 Cryptographic Extension instructions.

Table F2-30 AArch32 Cryptographic Extension instructions

| Mnemonic   | Instruction                 | See                             |
|------------|-----------------------------|---------------------------------|
| AESD       | AES single round decryption | AESD                            |
| AESE       | AES single round encryption | AESE                            |
| AESIMC     | AES inverse mix columns     | AESIMC                          |
| AESMC      | AES mix columns             | AESMC                           |
| VMULL      | Polynomial multiply long    | VMULL(integer and polynomial) a |
| SHA1C      | SHA1 hash update (choose)   | SHA1C                           |
| SHA1H      | SHA1 fixed rotate           | SHA1H                           |
| SHA1M      | SHA1 hash update (majority) | SHA1M                           |
| SHA1P      | SHA1 hash update (parity)   | SHA1P                           |
| SHA1SU0    | SHA1 schedule update 0      | SHA1SU0                         |
| SHA1SU1    | SHA1 schedule update 1      | SHA1SU1                         |
| SHA256H    | SHA256 hash update (part 1) | SHA256H                         |
| SHA256H2   | SHA256 hash update (part 2) | SHA256H2                        |
| SHA256SU0  | SHA256 schedule update 0    | SHA256SU0                       |

| Mnemonic   | Instruction              | See       |
|------------|--------------------------|-----------|
| SHA256SU1  | SHA256 schedule update 1 | SHA256SU1 |