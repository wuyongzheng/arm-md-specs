## A1.4 Supported data types

The Arm architecture supports the following integer data types:

| Byte       | 8 bits.   |
|------------|-----------|
| Halfword   | 16 bits.  |
| Word       | 32 bits.  |
| Doubleword | 64 bits.  |
| Quadword   | 128 bits. |

The architecture also supports the following floating-point data types:

- Half-precision. See Half-precision floating-point formats.
- Single-precision. See Single-precision floating-point format.
- Double-precision. See Double-precision floating-point format.
- BFloat16. See BFloat16 floating-point format.
- 8-bit floating-point. See FP8 floating-point formats.

It also supports vectors, where a register holds a vector of multiple elements, each the same size and data type. See Advanced SIMD vector formats and SVE vector formats.

The architecture provides the following:

- Ageneral-purpose register file.
- ASIMD&amp;FPregister file.
- If FEAT\_SVE or FEAT\_SME is implemented, an SVE scalable vector register file and an SVE scalable predicate register file.
- If FEAT\_SME is implemented, the scalable ZA storage.
- If FEAT\_SME2 is implemented, the SME2 ZT0 register.

In each of these, the possible register widths depend on the Execution state.

In AArch64 state:

- The general-purpose register file contains 64-bit registers:
- -Many instructions can access these registers as 64-bit registers, or as 32-bit registers using only the bottom 32 bits.
- The SIMD&amp;FP register file contains 128-bit registers:
- -While the AArch64 vector registers support 128-bit vectors, the effective vector length can be 64-bits or 128-bits depending on the A64 instruction encoding used, see Instruction Mnemonics.
- The SVE scalable vector register file contains registers of an IMPLEMENTATION DEFINED width:
- -An SVE scalable vector register has an IMPLEMENTATION DEFINED width that is a power of two, from a minimum of 128 bits up to a maximum of 2048 bits.
- -All SVE scalable vector registers in an implementation are the same width.
- The SVE scalable predicate register file contains registers of an IMPLEMENTATION DEFINED width:
- -An SVE predicate register has an IMPLEMENTATION DEFINED width that is a power of two, from a minimum of 16 bits up to a maximum of 256 bits.
- The SME scalable ZA storage is a two-dimensional array of bytes. See ZA storage.
- The SME2 ZT0 register is 512 bits. See SME2 ZT0 register.

For more information on the register files in AArch64 state, see Registers in AArch64 Execution state.

In AArch32 state:

- The general-purpose register file contains 32-bit registers:

- Two 32-bit registers can support a doubleword.

- Vector formatting is supported, see Figure A1-4.

- The SIMD&amp;FP register file contains 64-bit registers:

- AArch32 state does not support quadword integer or floating-point data types.

Note

Two consecutive 64-bit registers can be used as a 128-bit register.

For more information on the register files in AArch32 state, see The general-purpose registers, and the PC, in AArch32 state.

## A1.4.1 Advanced SIMD vector formats

In an implementation that includes the Advanced SIMD instructions that operate on the SIMD&amp;FP register file, a register can hold one or more packed elements, all of the same size and type. In AArch32 state, the combination of a register and a data type describes a vector of elements, where the number of elements in the vector is implied by the size of the data type and the size of the register. In AArch64 state, the explicit combination of a register, number of elements, and element size describes a vector of elements. The vector is considered to be a one-dimensional array of elements of the data type specified in the instruction.

Vector indices are in the range 0 to (number of elements - 1). An index of 0 refers to the least significant bits of the vector.

For more information on the Advanced SIMD and floating-point registers in AArch32 state, see The SIMD and floating-point register file.

## A1.4.1.1 Advanced SIMD vector formats in AArch64 state

In AArch64 state, the SIMD&amp;FP registers can be referred to as V n , where n is a value from 0 to 31.

The SIMD&amp;FP registers support the following data formats for loads, stores, and data-processing operations:

- Asingle, scalar, element in the least significant bits of the register. See Registers in AArch64 Execution state.
- A128-bit vector of byte, halfword, word, or doubleword elements. See Figure A1-1.
- A64-bit vector of byte, halfword, word, or doubleword elements. See Figure A1-1.

For vectors, the element sizes are defined in Table A1-1, with the vector format described as:

- For a 128-bit vector: Vn.{2D, 4S, 8H, 16B}.
- For a 64-bit vector: Vn.{1D, 2S, 4H, 8B}.

## Table A1-1 SIMD elements in AArch64 state

| Mnemonic   | Size    |
|------------|---------|
| B          | 8 bits  |
| H          | 16 bits |
| S          | 32 bits |
| D          | 64 bits |

Figure A1-1 SIMD vectors in AArch64 state

<!-- image -->

## A1.4.1.2 Advanced SIMD vector formats in AArch32 state

Table A1-2 shows the available formats. Each instruction description specifies the data types that the instruction supports.

## Table A1-2 Advanced SIMD data types in AArch32 state

| Data type specifier   | Meaning                                           |
|-----------------------|---------------------------------------------------|
| .<size>               | Any element of <size> bits                        |
| .F<size>              | Floating-point number of <size> bits              |
| .I<size>              | Signed or unsigned integer of <size> bits         |
| .P<size>              | Polynomial over {0, 1} of degree less than <size> |
| .S<size>              | Signed integer of <size> bits                     |
| .U<size>              | Unsigned integer of <size> bits                   |

Polynomial arithmetic over {0, 1} describes the polynomial data type.

The .F16 data type is the half-precision data type selected by the FPSCR.AHP bit, see Half-precision floating-point formats.

The .F32 data type is the Arm standard single-precision floating-point data type, see Single-precision floating-point format.

The instruction definitions use a data type specifier to define the data types appropriate to the operation. Figure A1-2 shows the hierarchy of the Advanced SIMD data types.

<!-- image -->

|   .8 | .I8      | .S8 .U8   |
|------|----------|-----------|
| 0.8  | .P8      | .P8       |
| 0.8  | -        | -         |
| 0.16 | .I16     | .S16 .U16 |
| 0.16 | .P16 †   | .P16 †    |
| 0.16 | .F16     | .F16      |
| 0.16 | .BF16    | .BF16     |
| 0.32 | .I32     | .S32      |
| 0.32 | - .U32   | - .U32    |
| 0.32 | .F32     | .F32      |
| 0.64 | .I64     | .S64 .U64 |
| 0.64 | - .P64 ‡ | - .P64 ‡  |
| 0.64 | -        | -         |
| 0.64 |          |           |

- †  Output format only. See VMULL instruction description.
- ‡  Available only if the Cyptographic Extension is implemented. See VMULL instruction description.

Figure A1-2 Advanced SIMD data type hierarchy in AArch32 state

For example, a multiply instruction must distinguish between integer and floating-point data types.

An integer multiply instruction that generates a double-width (long) result must specify the input data types as signed or unsigned. However, some integer multiply instructions use modulo arithmetic, and therefore do not have to distinguish between signed and unsigned inputs.

Figure A1-3 shows the Advanced SIMD vectors in AArch32 state.

Note

In AArch32 state, a pair of even and following odd numbered doubleword registers can be concatenated and treated as a single quadword register.

Figure A1-3 Advanced SIMD vectors in AArch32 state

<!-- image -->

The AArch32 general-purpose registers support vectors formats for use by the SIMD instructions in the Base instruction set. Figure A1-4 shows these formats, that means that a general-purpose register can be treated as either 2 halfwords or 4 bytes.

Figure A1-4 Vector formatting in AArch32 state

<!-- image -->

## A1.4.2 SVE vector formats

In an implementation that includes the AArch64 SVE instructions, an SVE register can hold one or more packed or unpacked elements, all of the same size and type. The combination of a register and an element size describes a vector of elements. The vector is considered to be a one-dimensional array of elements of the data type specified in the instruction. The number of elements in the vector is implied by the size of the data elements and the Effective SVE vector length of the register.

Vector element indexes are in the range 0 to (number of elements - 1). An index of 0 refers to bits 0 to (element size -1) of the vector.

For the definition of Effective SVE vector length, see Configurable SVE vector lengths.

## A1.4.2.1 Scalable vector formats in AArch64 state

In AArch64 state, the SVE scalable vector registers can be referred to as Z n , where n is a value from 0 to 31.

The SVE scalable vector registers support the following data formats for loads, stores, and data-processing operations:

- Advanced SIMD data formats. Bits[127:0] of each Z n register hold the correspondingly numbered V n SIMD&amp;FP register.
- Aconfigurable-length vector of byte, halfword, word, doubleword, or quadword elements. See Figure A1-5. Also see Z0-Z31 in The AArch64 Application Level Programmers' Model.

The element sizes are defined in Table A1-3 with the vector format described as:

- Zn.{Q, D, S, H, B}.

Table A1-3 SVE elements in AArch64 state

| Mnemonic   | Element size   |
|------------|----------------|
| B          | 8 bits         |
| H          | 16 bits        |
| S          | 32 bits        |
| D          | 64 bits        |
| Q          | 128 bits       |

Figure A1-5 shows the vector formats of an SVE scalable vector register containing:

- Aconfigurable-length vector, where the Effective SVE vector length is 256 bits.
- Afixed-length 128-bit Advanced SIMD vector.

Figure A1-5 SVE vectors, and Advanced SIMD vectors, in an SVE scalable vector register

<!-- image -->

## A1.4.3 Half-precision floating-point formats

The Arm architecture supports two half-precision floating-point formats:

- IEEE half-precision, as described in the IEEE 754-2008 standard.
- Arm alternative half-precision format.

Note

BFloat16 is not a half-precision floating-point format, see BFloat16 floating-point format.

Both formats can be used for conversions to and from other floating-point formats. FPCR.AHP controls the format in AArch64 state and FPSCR.AHP controls the format in AArch32 state. FEAT\_FP16 adds half-precision data-processing instructions, which always use the IEEE format. These instructions ignore the value of the relevant AHP field, and behave as if it has an Effective value of 0. All SVE half-precision data-processing instructions, including conversions, ignore the value of FPCR.AHP, and behave as if it has an Effective value of 0.

The description of IEEE half-precision includes Arm-specific details that are left open by the standard, and is only an introduction to the formats and to the values they can contain. For more information, especially on the handling of infinities, NaNs, and signed zeros, see the IEEE 754 standard.

For both half-precision floating-point formats, the layout of the 16-bit format is the same. The format is:

<!-- image -->

| 15 14   | 15 14    | 10 9     | 10 9     | 0        |
|---------|----------|----------|----------|----------|
| S       | exponent | exponent | fraction | fraction |

The interpretation of the format depends on the value of the exponent field, bits[14:10] and on which half-precision format is being used.

## 0 &lt; exponent &lt; 0x1F

The value is a normalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive normalized number is 2 -14 , or approximately 6.104 × 10 -5 .

The maximum positive normalized number is (2 - 2 -10 ) × 2 15 , or 65504.

Larger normalized numbers can be expressed using the alternative format when the exponent == 0x1F .

The value is either a zero or a denormalized number, depending on the fraction bits:

fraction == 0

fraction != 0

exponent == 0

The value is a zero. There are two distinct zeros:

+0 when S==0.

-0

when S==1.

The value is a denormalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive denormalized number is 2 -24 , or approximately 5.960 × 10 -8 .

Half-precision denormalized numbers are not flushed to zero by default. When FEAT\_FP16 is implemented, the FPCR.FZ16 bit controls whether flushing denormalized numbers to zero is enabled for half-precision data-processing instructions. For details, see Flushing denormalized numbers to zero.

exponent == 0x1F

The value depends on which half-precision format is being used:

## IEEE half-precision

The value is either an infinity or a Not a Number (NaN), depending on the fraction bits:

fraction == 0

The value is an infinity. There are two distinct infinities:

+infinity

When S==0. This represents all positive numbers that are too big to be represented accurately as a normalized number.

-infinity

When S==1. This represents all negative numbers with an absolute value that is too big to be represented accurately as a normalized number.

exponent == 0

## fraction != 0

## Alternative half-precision

The value is a normalized number and is equal to:

-1 S × 2 16 × (1.fraction)

The maximum positive normalized number is (2-2 -10 ) × 2 16 or 131008.

## A1.4.4 Single-precision floating-point format

The single-precision floating-point format is as defined by the IEEE 754 standard.

This description includes Arm-specific details that are left open by the standard. It is only intended as an introduction to the formats and to the values they can contain. For full details, especially of the handling of infinities, NaNs, and signed zeros, see the IEEE 754 standard.

Asingle-precision value is a 32-bit word with the format:

fraction

S

31 30

23 22

0

exponent

<!-- image -->

The interpretation of the format depends on the value of the exponent field, bits[30:23]:

0 &lt; exponent &lt; 0xFF

The value is a normalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive normalized number is 2 -126 , or approximately 1.175 × 10 -38 .

The maximum positive normalized number is (2 - 2 -23 ) × 2 127 , or approximately 3.403 × 10 38 .

The value is either a zero or a denormalized number, depending on the fraction bits:

fraction == 0

The value is a NaN, and is either a quiet NaN or a signaling NaN .

The two types of NaN are distinguished by their most significant fraction bit, bit[9]:

bit[9] == 0

The NaN is a signaling NaN. The sign bit can take any value, and the remaining fraction bits can take any value except all zeros.

bit[9] == 1

The NaN is a quiet NaN. The sign bit and remaining fraction bits can take any value.

The value is a zero. There are two distinct zeros:

+0 When S==0.

- -0

When S==1.

These usually behave identically. In particular, the result is equal if +0 and -0 are compared as floating-point numbers. However, they yield different results in some circumstances. For example, the sign of the infinity produced as the result of dividing

Note

NaNs with different sign or fraction bits are distinct NaNs, but this does not mean software can use floating-point comparison instructions to distinguish them. This is because the IEEE 754 standard specifies that a NaN compares as unordered with everything, including itself.

## A1.4.5 Double-precision floating-point format

The double-precision floating-point format is as defined by the IEEE 754 standard. Double-precision floating-point is supported by both SIMD and floating-point instructions in AArch64 state, and only by floating-point instructions in AArch32 state.

This description includes IMPLEMENTATION SPECIFIC details that are left open by the standard. It is only intended as an introduction to the formats and to the values they can contain. For full details, especially of the handling of infinities, nabs, and signed zeros, see the IEEE 754 standard.

Adouble-precision value is a 64-bit doubleword, with the format:

fraction != 0

by zero depends on the sign of the zero. The two zeros can be distinguished from each other by performing an integer comparison of the two words.

The value is a denormalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive denormalized number is 2 -149 , or approximately 1.401 × 10 -45 .

Denormalized numbers are always flushed to zero in Advanced SIMD processing in AArch32 state. They are optionally flushed to zero in floating-point processing and in Advanced SIMD processing in AArch64 state. For details, see Flushing denormalized numbers to zero.

exponent == 0xFF

The value is either an infinity or a Not a Number (NaN), depending on the fraction bits:

fraction == 0

fraction != 0

The value is an infinity. There are two distinct infinities:

+infinity

When S==0. This represents all positive numbers that are too big to be represented accurately as a normalized number.

-infinity

When S==1. This represents all negative numbers with an absolute value that is too big to be represented accurately as a normalized number.

The value is a NaN, and is either a quiet NaN or a signaling NaN .

The two types of NaN are distinguished by their most significant fraction bit, bit[22]:

bit[22] == 0

bit[22] == 1

The NaN is a signaling NaN. The sign bit can take any value, and the remaining fraction bits can take any value except all zeros.

The NaN is a quiet NaN. The sign bit and remaining fraction bits can take any value.

For details of the default NaN , see Default NaN.

<!-- image -->

Double-precision values represent numbers, infinities, and NaNs in a similar way to single-precision values, with the interpretation of the format depending on the value of the exponent:

## 0 &lt; exponent &lt; 0x7FF

The value is a normalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive normalized number is 2 -1022 , or approximately 2.225 × 10 -308 .

The maximum positive normalized number is (2 - 2 -52 ) × 2 1023 , or approximately 1.798 × 10 308 .

The value is either a zero or a denormalized number, depending on the fraction bits:

## fraction == 0

fraction != 0

## exponent == 0

The value is a zero. There are two distinct zeros that behave in the same way as the two single-precision zeros:

$$+0 when S==0.$$

-0

when S==1.

The value is a denormalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive denormalized number is 2 -1074 , or approximately 4.941 × 10 -324 .

Optionally, denormalized numbers are flushed to zero in floating-point calculations. For details, see Flushing denormalized numbers to zero.

exponent == 0x7FF

The value is either an infinity or a NaN, depending on the fraction bits:

## fraction == 0

## fraction != 0

The value is an infinity. As for single-precision, there are two infinities:

+infinity

When S==0.

-infinity

When S==1.

The value is a NaN, and is either a quiet NaN or a signaling NaN .

The two types of NaN are distinguished by their most significant fraction bit, bit[51] of the doubleword:

bit[51] == 0

bit[51] == 1

The NaN is a signaling NaN. The sign bit can take any value, and the remaining fraction bits can take any value except all zeros.

Note

NaNs with different sign or fraction bits are distinct NaNs, but this does not mean software can use floating-point comparison instructions to distinguish them. This is because the IEEE 754 standard specifies that a NaN compares as unordered with everything, including itself.

## A1.4.6 BFloat16 floating-point format

BFloat16 is a 16-bit floating-point storage format that inherits many of its properties and behaviors from the IEEE 754 single-precision format described in Single-precision floating-point format.

The BFloat16 format is:

## 0 &lt; exponent &lt; 0xFF

The value is a normalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive normalized number is 2 -126 , or approximately 1.175 × 10 -38 .

The maximum positive normalized number is (2 - 2 -7 ) × 2 127 , or approximately 3.390 × 10 38 .

The value is either a zero or a denormalized number, depending on the fraction bits:

fraction == 0

fraction != 0

exponent == 0

The NaN is a quiet NaN. The sign bit and the remaining fraction bits can take any value.

For details of the default NaN , see Default NaN.

<!-- image -->

The value is a zero. There are two distinct zeros:

<!-- formula-not-decoded -->

-0 when S==1.

These usually behave identically. However, they yield different results in some circumstances. For example, the sign of the result produced as the result of multiplying by zero depends on the sign of the zero. The two zeros can be distinguished from each other by performing an integer bitwise comparison of the two halfwords.

The value is a denormalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive denormalized number is 2 -133 , or approximately 9.184 × 10 -41 .

Denormalized numbers are always flushed to zero in Advanced SIMD processing in AArch32 state. They are optionally flushed to zero in floating-point processing and in Advanced SIMD processing in AArch64 state. For details, see Flushing denormalized numbers to zero.

exponent == 0xFF

The value is either an infinity or a Not a Number (NaN), depending on the fraction bits:

## fraction == 0

The value is an infinity. There are two distinct infinities:

+infinity

When S==0. This represents all positive numbers that are too big to be represented accurately as a normalized number.

-infinity

When S==1. This represents all negative numbers with an absolute value that is too big to be represented accurately as a normalized number.

## fraction != 0

The value is a NaN, and is either a quiet NaN or a signaling NaN .

The two types of NaN are distinguished by their most significant fraction bit, bit[6]:

bit[6] == 0

The NaN is a signaling NaN. The sign bit can take any value, and the remaining fraction bits can take any value except all zeros.

bit[6] == 1

The NaN is a quiet NaN. The sign bit and remaining fraction bits can take any value.

BFloat16 values are 16-bit halfwords that software can convert to single-precision format, by appending 16 zero bits, so that single-precision arithmetic instructions can be used. A single-precision value can be converted to a BFloat16 value, either by:

- Truncating, by removing the least significant 16 bits.
- Using the BFloat16 conversion instructions, see Table C3-113.

## See also:

- Summary of BFloat16 instruction behaviors.

## A1.4.7 FP8 floating-point formats

The Arm architecture supports two 8-bit floating-point (FP8) formats:

- OFP8 E4M3 format.
- OFP8 E5M2 format.

These formats are used by FP8 instructions, which are instructions, where the input or output elements are in FP8 floating-point format. FPMR.F8S1 controls the format for inputs named First FP8 input data stream and FPMR.F8S2 controls the format for inputs named Second FP8 input data stream . The format of an FP8 output from an FP8 instruction is determined by FPMR.F8D field.

For more information, see OCP8-bit Floating Point Specification (OFP8) .

## A1.4.7.1 OFP8 E4M3 format

The OFP8 E4M3 format is:

<!-- image -->

(0 &lt; exponent &lt; 0xF ) || (exponent == 0xF &amp;&amp;fraction &lt; 0x7 )

The value is a normalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive normalized number is 2 -6 .

The maximum positive normalized number is (2 - 2 -2 ) × 2 8 .

The value is either a zero or a denormalized number, depending on the fraction bits:

## fraction == 0

fraction != 0

exponent == 0

exponent == 0

The value is a zero. There are two distinct zeros that behave in the same way as the two single-precision zeros:

+0 when S==0.

-0 when S==1.

The value is a denormalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive denormalized number is 2 -9 .

FP8 denormalized numbers are never flushed to zero.

exponent == 0xF &amp;&amp;fraction == 0x7

The value is a signaling NaN .

An infinity is not supported.

## A1.4.7.2 OFP8 E5M2 format

The OFP8 E5M2 format is:

## 0 &lt; exponent &lt; 0x1F

The value is a normalized number and is equal to:

<!-- formula-not-decoded -->

The minimum positive normalized number is 2 -14 .

The maximum positive normalized number is (2 - 2 -2 ) × 2 15 .

The value is either a zero or a denormalized number, depending on the fraction bits:

fraction == 0

<!-- image -->

The value is a zero. There are two distinct zeros that behave in the same way as the two single-precision zeros:

+0

when S==0.

-0

when S==1.

fraction != 0

The value is a denormalized number and is equal to:

$$(-1) S × 2 -14 × (0.fraction)$$

The minimum positive denormalized number is 2 -16 .

FP8 denormalized numbers are never flushed to zero.

exponent == 0x1F

The value is either an infinity or a NaN, depending on the fraction bits:

## fraction == 0

The value is an infinity. There are two distinct infinities:

+infinity

When S==0. This represents all positive numbers that are too big to be represented accurately as a normalized number.

- -infinity

When S==1. This represents all negative numbers with an absolute that is too big to be represented accurately as a normalized number.

## fraction != 0

The value is a NaN, and is either a quiet NaN or a signaling NaN .

The two types of NaN are distinguished by their most significant fraction bit, bit[1]:

bit[1] == 0

The NaN is a signaling NaN. The sign bit can take any value, and bit[0] is 1.

bit[1] == 1

The NaN is a quiet NaN. The sign bit and bit[0] can take any value.

## A1.4.8 Conversion between floating-point and fixed-point values

The Arm architecture supports the conversion of a scalar floating-point value to or from a signed or unsigned fixed-point value in a general-purpose register. Conversion instructions take an argument, #fbits, that specifies the number of fraction bits in the fixed-point number. That is, #fbits indicates that the general-purpose register holds a fixed-point number with fbits bits after the binary point, where fbits is in the range 1 to 64 for a 64-bit general-purpose register, or 1 to 32 for a 32-bit general-purpose register:

- For a 64-bit register Xd:
- -The integer part is Xd[63:#fbits].
- -The fractional part is Xd[(#fbits-1):0].
- For a 32-bit register Wd or Rd:
- -The integer part is Wd[31:#fbits] or Rd[31:#fbits].
- -The fractional part is Wd[(#fbits-1):0] or Rd[(#fbits-1):0].

These instructions can cause the following floating-point exceptions:

Invalid Operation When the floating-point input is NaN or Infinity or when a numerical value cannot be represented within the destination register.

Inexact

When the numeric result differs from the input value.

Input Denormal When flushing denormalized numbers to zero is enabled and the denormal input is replaced by a zero, see Flushing denormalized numbers to zero and Input Denormal exceptions.

Note

An out of range fixed-point result is saturated to the destination size.

For more information, see Floating-point exceptions and exception traps.

## A1.4.9 Polynomial arithmetic over {0, 1}

Some SIMD instructions that operate on SIMD&amp;FP registers can operate on polynomials over {0, 1}, see Supported data types. The polynomial data type represents a polynomial in x of the form bn-1x n-1 + . . . + b1x + b0 where bk is bit[k] of the value.

The coefficients 0 and 1 are manipulated using the rules of Boolean arithmetic:

- 0 + 0 = 1 + 1 = 0.
- 0 + 1 = 1 + 0 = 1.
- 0 × 0 = 0 × 1 = 1 × 0 = 0.
- 1 × 1 = 1.

That is:

- Adding two polynomials over {0, 1} is the same as a bitwise exclusive-OR.
- Multiplying two polynomials over {0, 1} is the same as integer multiplication except that partial products are exclusive-ORed instead of being added.

A64, A32, and T32 provide instructions for performing polynomial multiplication of 8-bit values.

- For AArch32, see VMUL (integer and polynomial) and VMULL (integer and polynomial).
- For AArch64, see PMUL and PMULL, PMULL2.

The Cryptographic Extension adds the ability to perform long polynomial multiplies of 64-bit values. See PMULL, PMULL2.

## A1.4.9.1 Pseudocode description of polynomial multiplication

In pseudocode, polynomial addition is described by the EOR operation on bitstrings.

Polynomial multiplication is described by the PolynomialMult() function defined in A-profile Architecture Pseudocode.