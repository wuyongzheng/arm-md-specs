## F1.9 Additional information about Advanced SIMD and floating-point instructions

The following subsections give additional information about the Advanced SIMD and floating-point instructions:

- Advanced SIMD and floating-point instruction syntax.
- The Advanced SIMD addressing mode.
- Advanced SIMD instruction modifiers.
- Advanced SIMD operand shapes.
- Data type specifiers.
- Register specifiers.
- Register lists.
- Register encoding.
- Advanced SIMD scalars.

Note

The Advanced SIMD architecture, its associated implementations, and supporting software, are commonly referred to as NEON™technology.

## F1.9.1 Advanced SIMD and floating-point instruction syntax

Advanced SIMD and floating-point instructions use the general conventions of the T32 and A32 instruction sets.

Advanced SIMD and floating-point data-processing instructions use the following general format:

```
V{<modifier>}<operation>{<shape>}{<c>}{<q>}{.<dt>}
```

```
{<dest>,} <src1>, <src2>
```

All Advanced SIMD and floating-point instructions begin with a V . This distinguishes Advanced SIMD vector and floating-point instructions from scalar instructions.

The main operation is specified in the &lt;operation&gt; field. It is usually a three letter mnemonic the same as or similar to the corresponding scalar integer instruction.

The &lt;c&gt; and &lt;q&gt; fields are standard assembler syntax fields. For details, see Standard assembler syntax fields.

## F1.9.2 The Advanced SIMD addressing mode

All the element and structure load/store instructions use this addressing mode. There is a choice of three formats:

[&lt;Rn&gt;{:&lt;align&gt;}] The address is contained in general-purpose register Rn. Rn is not updated by this instruction. Encoded as Rm = 0b1111 . If Rn is encoded as 0b1111 , the instruction is CONSTRAINED UNPREDICTABLE. [&lt;Rn&gt;{:&lt;align&gt;}]! The address is contained in general-purpose register Rn. Rn is updated by this instruction: Rn = Rn + transfer\_size Encoded as Rm = 0b1101 . transfer\_size is the number of bytes transferred by the instruction. This means that, after the instruction is executed, Rn points to the address in memory immediately following the last address loaded from or stored to. If Rn is encoded as 0b1111 , the instruction is CONSTRAINED UNPREDICTABLE. This addressing mode can also be written as: [&lt;Rn&gt;{:align}], #&lt;transfer\_size&gt;

However, disassembly produces the [&lt;Rn&gt;{:align}]! form.

[&lt;Rn&gt;{:&lt;align&gt;}], &lt;Rm&gt;

The address is contained in general-purpose register &lt;Rn&gt; .

Rn is updated by this instruction: Rn = Rn + Rm

Encoded as Rm = Rm. Rm must not be encoded as 0b1111 or 0b1101 , the PC or the SP.

If Rn is encoded as 0b1111 , the instruction is CONSTRAINED UNPREDICTABLE.

The CONSTRAINED UNPREDICTABLE behavior of encodings where Rn is 0b1111 is described in the section: Using R15 by instruction.

In all cases, &lt;align&gt; specifies an alignment, as specified by the individual instruction descriptions.

Previous versions of the manual used the @ character for alignment. So, for example, the first format in this section was shown as [&lt;Rn&gt;{@&lt;align&gt;}] . Both @ and : are supported. However, to ensure portability of code to assemblers that treat @ as a comment character, : is preferred.

## F1.9.3 Advanced SIMD instruction modifiers

The &lt;modifier&gt; field provides additional variants of some instructions. Table F1-10 provides definitions of the modifiers. Modifiers are not available for every instruction.

Table F1-10 Advanced SIMD instruction modifiers

| <modifier>   | Meaning                                                         |
|--------------|-----------------------------------------------------------------|
| Q            | The operation uses saturating arithmetic.                       |
| R            | The operation performs rounding.                                |
| D            | The operation doubles the result (before accumulation, if any). |
| H            | The operation halves the result.                                |

## F1.9.4 Advanced SIMD operand shapes

The &lt;shape&gt; field provides additional variants of some instructions. Table F1-11 provides definitions of the shapes. Operand shapes are not available for every instruction.

Table F1-11 Advanced SIMD operand shapes

| <shape>   | Meaning                                                                             | Typical register shape   | Typical register shape   |
|-----------|-------------------------------------------------------------------------------------|--------------------------|--------------------------|
| (none)    | The operands and result are all the same width.                                     | Dd, Dn,Dm                | Qd, Qn,Qm                |
| L         | Long operation - result is twice the width of both operands                         | Qd, Dn,Dm                |                          |
| N         | Narrow operation - result is half the width of both operands                        | Dd, Qn,Qm                |                          |
| W         | Wide operation - result and first operand are twice the width of the second operand | Qd, Qn,Dm                |                          |

Note

- Some assemblers support a Q shape specifier, which requires all operands to be Q registers. An example of using this specifier is VADDQ.S32 q0, q1, q2 . This is not standard UAL, and Arm recommends that programmers do not use a Q shape specifier.
- Adisassembler must not generate any shape specifier not shown in Table F1-11.

## F1.9.5 Data type specifiers

The &lt;dt&gt; field normally contains one data type specifier. Unless the assembler syntax description for the instruction indicates otherwise, this indicates the data type contained in:

- The second operand, if any.
- The operand, if there is no second operand.
- The result, if there are no operand registers.

The data types of the other operand and result are implied by the &lt;dt&gt; field combined with the instruction shape. For information about data type formats, see Data types supported by the Advanced SIMD implementation.

In the instruction syntax descriptions in About the T32 and A32 Instruction Descriptions, the &lt;dt&gt; field is usually specified as a single field. However, where more convenient, it is sometimes specified as a concatenation of two fields, &lt;type&gt;&lt;size&gt; .

## F1.9.5.1 Syntax flexibility

There is some flexibility in the data type specifier syntax:

- Software can specify three data types, specifying the result and both operand data types. For example: VSUBW.I16.I16.S8 Q3, Q5, D0 instead of VSUBW.S8 Q3, Q5, D0
- Software can specify two data types, specifying the data types of the two operands. The data type of the result is implied by the instruction shape. For example: VSUBW.I16.S8 Q3, Q5, D0 instead of VSUBW.S8 Q3, Q5, D0
- Software can specify two data types, specifying the data types of the single operand and the result. For example: VMOVN.I16.I32 D0, Q1 instead of VMOVN.I32 D0, Q1
- Where an instruction requires a less specific data type, software can instead specify a more specific type, as shown in Table F1-12.
- Where an instruction does not require a data type, software can provide one.
- The F32 data type can be abbreviated to F .
- The F64 data type can be abbreviated to D .

In all cases, if software provides additional information, the additional information must match the instruction shape. Disassembly does not regenerate this additional information.

Table F1-12 Data type specification flexibility

| Specified data type   | Permitted more specific data types   | Permitted more specific data types   | Permitted more specific data types   | Permitted more specific data types   | Permitted more specific data types   |
|-----------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| None                  | Any                                  | Any                                  | Any                                  | Any                                  | Any                                  |
| .I<size>              | -                                    | .S<size>                             | .U<size>                             | -                                    | -                                    |
| .8                    | .I8                                  | .S8                                  | .U8                                  | .P8                                  | -                                    |
| .16                   | .I16                                 | .S16                                 | .U16                                 | .P16                                 | .F16                                 |
| .32                   | .I32                                 | .S32                                 | .U32                                 | -                                    | .F32 or .F                           |
| .64                   | .I64                                 | .S64                                 | .U64                                 | -                                    | .F64 or .D                           |

## F1.9.6 Register specifiers

The &lt;dest&gt; , &lt;src1&gt; , and &lt;src2&gt; fields contain register specifiers, or in some cases scalar specifiers or register lists. Table F1-13 shows the register and scalar specifier formats that appear in the instruction descriptions.

If &lt;dest&gt; is omitted, it is the same as &lt;src1&gt; .

Table F1-13 Advanced SIMD and floating-point register specifier formats

| <specifier>   | Usual meaning a                                                      | Used in        |
|---------------|----------------------------------------------------------------------|----------------|
| <Qd>          | Aquadword destination register for the result vector.                | Advanced SIMD  |
| <Qn>          | Aquadword source register for the first operand vector.              | Advanced SIMD  |
| <Qm>          | Aquadword source register for the second operand vector.             | Advanced SIMD  |
| <Dd>          | Adoubleword destination register for the result vector.              | Both           |
| <Dn>          | Adoubleword source register for the first operand vector.            | Both           |
| <Dm>          | Adoubleword source register for the second operand vector.           | Both           |
| <Sd>          | Asingleword destination register for the result vector.              | Floating-point |
| <Sn>          | Asingleword source register for the first operand vector.            | Floating-point |
| <Sm>          | Asingleword source register for the second operand vector.           | Floating-point |
| <Dd[x]>       | Adestination scalar for the result. Element x of vector <Dd> .       | Advanced SIMD  |
| <Dn[x]>       | Asource scalar for the first operand. Element x of vector <Dn> .     | Both b         |
| <Dm[x]>       | Asource scalar for the second operand. Element x of vector <Dm> .    | Advanced SIMD  |
| <Rt>          | Ageneral-purpose register, used for a source or destination address. | Both           |
| <Rt2>         | Ageneral-purpose register, used for a source or destination address. | Both           |
| <Rn>          | Ageneral-purpose register, used as a load or store base address.     | Both           |
| <Rm>          | Ageneral-purpose register, used as a post-indexed address source.    | Both           |

## F1.9.7 Register lists

Aregister list is a list of register specifiers separated by commas and enclosed in brackets { and }. There are restrictions on what registers can appear in a register list. These restrictions are described in the individual instruction descriptions. Table F1-14 shows some register list formats, with examples of actual register lists corresponding to those formats.

Note

Register lists must not wrap around the end of the register bank.

## F1.9.7.1 Syntax flexibility

There is some flexibility in the register list syntax:

- Where a register list contains consecutive registers, they can be specified as a range, instead of listing every register, for example {D0-D3} instead of {D0, D1, D2, D3} .
- Where a register list contains an even number of consecutive doubleword registers starting with an even-numbered register, it can be written as a list of quadword registers instead, for example {Q1, Q2} instead of {D2-D5} .
- Where a register list contains only one register, the enclosing braces can be omitted, for example VLD1.8 D0, [R0] instead of VLD1.8 {D0}, [R0] .

## Table F1-14 Example register lists

| Format                 | Example        | Alternative   |
|------------------------|----------------|---------------|
| {<Dd>}                 | {D3}           | D3            |
| {<Dd>, <Dd+1>, <Dd+2>} | {D3, D4, D5}   | {D3-D5}       |
| {<Dd[x]>, <Dd+2[x]}    | {D0[3], D2[3]} | -             |
| {<Dd[]>}               | {D7[]}         | D7[]          |

## F1.9.8 Register encoding

An Advanced SIMD register is either:

- Quadword , meaning it is 128 bits wide.
- Doubleword , meaning it is 64 bits wide.

Some instructions have options for either doubleword or quadword registers. This is normally encoded in Q, bit[6], as Q = 0 for doubleword operations, or Q = 1 for quadword operations.

Afloating-point register is either:

- Double-precision, meaning it is 64 bits wide.
- Single-precision, meaning it is 32 bits wide.

This is encoded in the sz field, bit[8], as sz = 1 for double-precision operations, or sz = 0 for single-precision operations.

The T32 instruction encoding of Advanced SIMD or floating-point registers is:

| 15 14 13 12 11 10 9 8 7   | 6 5 4 3   | 2 1 0   | 15 14 13 12 11 10 9 8 7 6 5   |
|---------------------------|-----------|---------|-------------------------------|
|                           | D         | Vn      | Vd sz N Q M                   |

The A32 instruction encoding of Advanced SIMD or floating-point registers is:

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9   |    |    |    | 8 7 6 5   |
|-----------------------------------------------------------------------|----|----|----|-----------|
|                                                                       | D  | Vn | Vd | sz N Q M  |

Some instructions use only one or two registers, and use the unused register fields as additional opcode bits.

Table F1-15 shows the encodings for the registers.

<!-- image -->

Table F1-15 Encoding of register numbers

| Register mnemonic   | Usual usage                       | Register number encoded in a   | Notes a        | Used in        |
|---------------------|-----------------------------------|--------------------------------|----------------|----------------|
| <Qd>                | Destination (quadword)            | D, Vd (bits[22, 15:13])        | bit[12] == 0 b | Advanced SIMD  |
| <Qn>                | First operand (quadword)          | N, Vn (bits[7, 19:17])         | bit[16] == 0 b | Advanced SIMD  |
| <Qm>                | Second operand (quadword)         | M, Vm(bits[5, 3:1])            | bit[0] == 0 b  | Advanced SIMD  |
| <Dd>                | Destination (doubleword)          | D, Vd (bits[22, 15:12])        | -              | Both           |
| <Dn>                | First operand (doubleword)        | N, Vn (bits[7, 19:16])         | -              | Both           |
| <Dm>                | Second operand (doubleword)       | M, Vm(bits[5, 3:0])            | -              | Both           |
| <Sd>                | Destination (single-precision)    | Vd, D(bits[15:12, 22])         | -              | Floating-point |
| <Sn>                | First operand (single-precision)  | Vn, N(bits[19:16, 7])          | -              | Floating-point |
| <Sm>                | Second operand (single-precision) | Vm, M(bits[3:0, 5])            | -              | Floating-point |

## F1.9.9 Advanced SIMD scalars

Advanced SIMD scalars can be 8-bit, 16-bit, 32-bit, or 64-bit. Instructions other than multiply instructions can access any element in the register set. The instruction syntax refers to the scalars using an index into a doubleword vector. The descriptions of the individual instructions contain details of the encodings.

Table F1-16 shows the form of encoding for scalars used in multiply instructions. These instructions cannot access scalars in some registers. The descriptions of the individual instructions contain cross references to this section where appropriate.

32-bit Advanced SIMD scalars, when used as single-precision floating-point numbers, are equivalent to Floating-point single-precision registers. That is, Dm[x] in a 32-bit context (0 &lt;= m &lt;= 15, 0 &lt;= x &lt;=1) is equivalent to S[2m + x] .

Table F1-16 Encoding of scalars in multiply instructions

| Scalar mnemonic   | Usual usage    | Scalar size   | Register specifier   | Index specifier   | Accessible registers   |
|-------------------|----------------|---------------|----------------------|-------------------|------------------------|
| <Dm[x]>           | Second operand | 16-bit        | Vm[2:0]              | M, Vm[3]          | D0-D7                  |
|                   |                | 32-bit        | Vm[3:0]              | M                 | D0-D15                 |

## Chapter F2 The AArch32 Instruction Sets Overview

This chapter describes the T32 and A32 instruction sets. It contains the following sections:

- Support for instructions in different versions of the Arm architecture.
- Unified Assembler Language.
- Branch instructions.
- Data-processing instructions.
- PSTATE and banked register access instructions.
- Load/store instructions.
- Load/store multiple instructions.
- Miscellaneous instructions.
- Exception-generating and exception-handling instructions.
- System register access instructions.
- Advanced SIMD and floating-point load/store instructions.
- Advanced SIMD and floating-point register transfer instructions.
- Advanced SIMD data-processing instructions.
- Floating-point data-processing instructions.