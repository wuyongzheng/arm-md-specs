## F1.7 General information about the T32 and A32 instruction descriptions

T32 Instruction Set Encoding describes the T32 instruction encodings, and A32 Instruction Set Encoding describes the A32 instruction encodings. The following subsections give more information about the descriptions of these instructions and their encodings:

- Execution of instructions in debug state.
- Fixed values in AArch32 instruction and System register descriptions.
- UNDEFINED, UNPREDICTABLE, and CONSTRAINED UNPREDICTABLE instruction set space.
- T32 and A32 Advanced SIMD and floating-point instruction encodings.
- The PC and the use of 0b1111 as a register specifier in T32 and A32 instructions.
- The SP and the use of 0b1101 as a register specifier in T32 and A32 instructions.
- Modified immediate constants in T32 and A32 instructions.

## F1.7.1 Execution of instructions in debug state

In general, except for the instructions described in Debug state, the T32 instruction descriptions do not indicate any differences in the behavior of the instruction if it is executed in Debug state. For this information, see Executing instructions in Debug state.

Note

- A32 instructions cannot be executed in Debug state.
- For many T32 instructions, execution is unchanged in Debug state. Executing instructions in Debug state identifies these instructions.

## F1.7.2 Fixed values in AArch32 instruction and System register descriptions

This section summarizes the terms used to describe fixed values in AArch64 register and instruction descriptions. The Glossary gives full descriptions of these terms, and each entry in this section includes a link to the corresponding Glossary entry.

Note

In register descriptions, the meaning of some bits depends on the PE state. This affects the definitions of RES0 and RES1, as shown in the Glossary.

The following terms are used to describe bits or fields with fixed values:

RAZ

Read-As-Zero. See Read-As-Zero (RAZ).

In diagrams, a RAZ bit can be shown as 0.

- (0), RES0

Reserved, Should-Be-Zero (SBZ) or RES0.

In instruction encoding diagrams, and sometimes in other descriptions, (0) indicates an SBZ bit. If the bit is set to 1, behavior is CONSTRAINED UNPREDICTABLE, and must be one of the following:

- The instruction is UNDEFINED.
- The instruction is treated as a NOP .
- The instruction executes as if the value of the bit was 0.
- Any destination registers of the instruction become UNKNOWN.

This notation can be expanded for fields, so a three-bit field can be shown as either (0)(0)(0) or as (000) .

In register diagrams, but not in the A64 encoding and instruction descriptions, bits or fields can be shown as RES0. For more information, see the Glossary definition of RES0.

Note

Some of the System instruction descriptions in this chapter are based on the field description of the input value for the instruction. These are register descriptions and therefore can include RES0 fields,

The (0) and RES0 descriptions can be applied to bits or bit fields that are read-only, or are write-only. The Glossary definitions cover these cases.

RAO Read-As-One. See Read-As-One (RAO).

In diagrams, a RAO bit can be shown as 1.

(1), RES1 Reserved, Should-Be-One (SBO) or RES1.

In instruction encoding diagrams, and sometimes in other descriptions, (1) indicates an SBO bit. If the bit is set to 0, behavior is CONSTRAINED UNPREDICTABLE, and must be one of the following:

- The instruction is UNDEFINED.

- The instruction is treated as a NOP .

- The instruction executes as if the value of the bit was 1.

- Any destination registers of the instruction become UNKNOWN.

This notation can be expanded for fields, so a three-bit field can be shown as either (1)(1)(1) or as (111) .

In register diagrams, but not in the A64 encoding and instruction descriptions, bits or fields can be shown as RES1. For more information, see the Glossary definition of RES1 .

Note

Some of the System instruction descriptions in this chapter are based on the field description of the input value for the instruction. These are register descriptions and therefore can include RES1 fields.

The (1) and RES1 descriptions can be applied to bits or bit fields that are read-only, or are write-only. The Glossary definitions cover these cases.

Note

In register diagrams, (0) is a synonym for RES0, and (1) is a synonym for RES1, where RES0 and RES1 are defined in the Glossary. However, when used in an instruction encoding diagram, (0) and (1) have the narrower definition that behavior is UNPREDICTABLE or CONSTRAINED UNPREDICTABLE if either:

- Abit marked as (0) has the value 1.
- Abit marked as (1) has the value 0.

## F1.7.3 UNDEFINED, UNPREDICTABLE, and CONSTRAINED UNPREDICTABLE instruction set space

An attempt to execute an unallocated instruction results in either:

- Unpredictable behavior. The instruction is described as UNPREDICTABLE or CONSTRAINED UNPREDICTABLE. From the introduction of Armv8-A, the architecturally UNPREDICTABLE behavior in AArch32 state is greatly reduced. Most cases that earlier versions of the architecture describe as UNPREDICTABLE become either:

-

CONSTRAINED UNPREDICTABLE, meaning the architecture defines a limited range of permitted behaviors.

- -Fully predictable.

For more information, see Architectural Constraints on UNPREDICTABLE Behaviors.

- An Undefined Instruction exception. The instruction is described as UNDEFINED.

An instruction is UNDEFINED if it is declared as UNDEFINED in an instruction description, or in T32 Instruction Set Encoding or A32 Instruction Set Encoding.

An instruction is UNPREDICTABLE only if:

- It is declared as UNPREDICTABLE in an instruction description or in T32 Instruction Set Encoding or A32 Instruction Set Encoding, and Architectural Constraints on UNPREDICTABLE Behaviors does not redefine the behavior as CONSTRAINED UNPREDICTABLE.
- The pseudocode for that encoding does not indicate that a different special case applies, and a bit marked (0) or (1) in the encoding diagram of an instruction is not 0 or 1 respectively. In most cases, Armv8 makes these cases CONSTRAINED UNPREDICTABLE, as described in SBZ or SBO fields T32 and A32 in instructions.

Unless otherwise specified, T32 and A32 instructions provided as part of an architectural extension, or by an optional feature of the architecture, are UNDEFINED in an implementation that does not include that extension or feature.

Note

Examples of where this rule applies are:

- The instructions provided by the Cryptographic Extension.
- The System instructions that provide access to the System registers of the OPTIONAL Performance Monitors Extension.
- The Advanced SIMD and floating-point instructions.

For more information about UNDEFINED, UNPREDICTABLE, and CONSTRAINED UNPREDICTABLE instruction behavior, see Undefined Instruction exception.

## F1.7.4 T32 and A32 Advanced SIMD and floating-point instruction encodings

The T32 and A32 encodings of Advanced SIMD and floating-point instructions that are described in T32 Instruction Set Encoding and in A32 Instruction Set Encoding are common to the T32 and A32 instruction sets. This means:

- The instruction groups, and the set of instructions in each group, are identical for T32 and A32.
- For each instruction:
- -Each T32 encoding is exactly equivalent to an A32 encoding.
- -There is no T32 encoding without an equivalent A32 encoding, and no A32 encoding without an equivalent T32 encoding.

Note

- In the T32 instruction sets, the Advanced SIMD and floating-point instructions have 32-bit encodings.
- In the base instruction sets, some instructions are common to the T32 and A32 instruction sets, whereas other instructions have equivalent but not identical functionality in the two instruction sets.

32-bit T32 encodings are described as two contiguous halfwords, { hw1 : hw2 }, as described in Instruction encodings. In general:

- hw1 of a T32 encoding maps onto bits[31:16] of an equivalent A32 encoding.
- hw2 of a T32 encoding maps onto bits[15:0] of an equivalent A32 encoding.

However, the different structures of the T32 instruction encoding space and the A32 instruction encoding space mean that:

- For a given Advanced SIMD and floating-point instruction group:
- -The positions of the fields that identify the instruction, or instruction encoding, within the instruction group might differ between the T32 encodings and the A32 encodings.
- -However, the field values that identify the instruction of instruction encoding are identical for the T32 encoding and the A32 encoding.

The remainder of this section describes the equivalence of the T32 and A32 encodings for each of the Advanced SIMD and floating-point instruction groups.

## F1.7.4.1 Advanced SIMD data-processing

The T32 encoding of the Advanced SIMD data-processing group is:

<!-- image -->

The A32 encoding of the Advanced SIMD data-processing group is:

<!-- image -->

The encodings in this group are identified by:

- hw1 [15:13] of the T32 encoding is equivalent to bits[27:25] of the A32 encoding, and:
- -Has the value 0b111 in the T32 encoding.
- -Has the value 0b001 in the A32 encoding.
- hw1 [11:8] of the T32 encoding is equivalent to bits[31:28] of the A32 encoding, and has the value 0b111 .

This table shows the equivalence of the fields that identify the instructions, or instruction encodings, within this group:

| T32 encoding   | A32 encoding   | Field size   |
|----------------|----------------|--------------|
| op0 : op1      | op0            | 2 bits       |
| op2            | op1            | 15 bits      |
| op3            | op2            | 1 bit        |
| op4            | op3            | 1 bit        |

## F1.7.4.2 Advanced SIMD element or structure load/store

The T32 encoding of the Advanced SIMD element or structure load/store group is:

<!-- image -->

The A32 encoding of the Advanced SIMD element or structure load/store group is:

<!-- image -->

The encodings in this group are identified by:

- hw1 [15:12] of the T32 encoding is equivalent to bits[31:28] of the A32 encoding, and has the value 0b1111 .
- hw1 [11:8] of the T32 encoding is equivalent to bits[27:24] of the A32 encoding, and:
- -Has the value 0b1001 in the T32 encoding.
- -Has the value 0b0100 in the A32 encoding.
- hw1 [4] of the T32 encoding is equivalent to bit[20] of the A32 encoding, and has the value 0b0 .

op0 , op1 , and op2 are the fields that identify the instructions, or instruction encodings, within this group, and they are in equivalent positions in the T32 and A32 encodings.

## F1.7.4.3 Advanced SIMD and floating-point load/store and 64-bit register moves

The T32 encoding of the Advanced SIMD and floating-point load/store and 64-bit register moves group is:

<!-- image -->

The A32 encoding of the Advanced SIMD and floating-point load/store and 64-bit register moves group is:

<!-- image -->

The encodings in the group are identified by:

- hw1 [15:12] of the T32 encoding is equivalent to bits[31:28] of the A32 encoding, and:
- -Has the value 0b1110 in the T32 encoding.
- -Can have any value other than 0b1111 in the A32 encoding. This range of values is required because A32 instructions in this group can be executed conditionally, see Conditional execution.
- hw1 [11:9] of the T32 encoding is equivalent to bits[27:25] of the A32 encoding, and has the value 0b110 .
- hw2 [11:9] of the T32 encoding is equivalent to bits[11:9] of the A32 encoding, and has the value 0b101 .

op0 is the field that identifies the instructions, or instruction encodings, within this group, and is in equivalent positions in the T32 and A32 encodings.

## F1.7.4.4 Advanced SIMD and floating-point 32-bit register moves

The T32 encoding of the Advanced SIMD and floating-point 32-bit register moves group is:

<!-- image -->

The A32 encoding of the Advanced SIMD 32-bit register moves group is:

<!-- image -->

The encodings in this group are identified by:

- hw1 [15:12] of the T32 encoding is equivalent to bits[31:28] of the A32 encoding, and:
- -Has the value 0b1110 in the T32 encoding.
- -Can have any value other than 0b1111 in the A32 encoding. This range of values is required because A32 instructions in this group can be executed conditionally, see

Conditional execution.

- hw1 [11:8] of the T32 encoding is equivalent to bits[27:24] of the A32 encoding, and has the value 0b1110 .
- hw2 [11:9] of the T32 encoding is equivalent to bits[11:9] of the A32 encoding, and has the value 0b101 .
- hw2 [4] of the T32 encoding is equivalent to bit[4] of the A32 encoding, and has the value 0b1 .

op0 is the field that identifies the instructions, or instruction encodings, within this group, and is in equivalent positions in the T32 and A32 encodings.

## F1.7.4.5 Floating-point data-processing

The T32 encoding of the Floating-point data-processing group is:

<!-- image -->

The A32 encoding of the Floating-point data-processing group is:

<!-- image -->

| 31     | 28 27 24 23   | 28 27 24 23   | 20 19   | 12 11 10   | 9   | 7   | 6   | 4   | 3   | 0   |
|--------|---------------|---------------|---------|------------|-----|-----|-----|-----|-----|-----|
| !=1111 | !=1111        | 1110          | op0     | 10         |     |     |     | 0   |     |     |
|        |               |               |         |            |     |     |     |     |     | op1 |

The encodings in this group are identified by:

- hw1 [15:12] of the T32 encoding is equivalent to bits[31:28] of the A32 encoding, and:
- -In the T32 encoding, hw1 [15:13] has the value 0b111 , and hw1 [12] is the op0 parameter used in identifying instruction encodings within this group.
- -In the A32 encoding, is the cond field and also implies the value of bit[28] of some A32 instruction encodings within this group, as the following table shows:

| cond      | Significance of bit[28] in A32 encodings   |
|-----------|--------------------------------------------|
| != 0b1111 | Part of the cond field.                    |
| 0b1111    | Has fixed value of 1.                      |

The range of cond values other than 0b1111 is required because A32 instructions in this group can be executed conditionally, see Conditional execution.

- hw1 [11:8] of the T32 encoding is equivalent to bits[27:24] of the A32 encoding, and has the value 0b1110 .
- hw2 [11:9] of the T32 encoding is equivalent to bits[11:9] of the A32 encoding, and has the value 0b101 .
- hw2 [4] of the T32 encoding is equivalent to bit[4] of the A32 encoding, and has the value 0b0 .

This table shows the equivalence of the fields that identify the instructions, or instruction encodings, within this group:

| T32 encoding   | A32 encoding                                                   |
|----------------|----------------------------------------------------------------|
| op0            | Bit[28] of the instruction encoding is 1 when cond is 0b1111 . |
| op1            | op0                                                            |
| op2            | op1                                                            |
| op3            | op2                                                            |

## F1.7.5 The PC and the use of 0b1111 as a register specifier in T32 and A32 instructions

Restrictions on the use of PC or 0b1111 as a register specifier differ between the T32 and the A32 instruction sets, as described in:

- T32 restrictions on the use of the PC, and use of 0b1111 as a register specifier.
- A32 restrictions on the use of PC or 0b1111 as a register specifier.

## F1.7.5.1 T32 restrictions on the use of the PC, and use of 0b1111 as a register specifier

The use of 0b1111 as a register specifier is not normally permitted in T32 instructions. When a value of 0b1111 is permitted, various meanings are possible. For register reads, these meanings include:

- Read the PC value, that is, the address of the current instruction + 4. The base register of the table branch instructions TBB and TBH can be the PC. This means branch tables can be placed in memory immediately after the instruction.

Note

Arm deprecates use of the PC as the base register in the STC instruction.

- Read the word-aligned PC value, that is, the address of the current instruction + 4, with bits[1:0] forced to zero. The base register of LDC , LDR , LDRB , LDRD (pre-indexed, no writeback), LDRH , LDRSB , and LDRSH instructions can be the word-aligned PC. This provides PC-relative data addressing. In addition, some encodings of the ADD and SUB instructions permit their source registers to be 0b1111 for the same purpose.

- Read zero. This is done in some cases when one instruction is a special case of another, more general instruction, but with one operand zero. In these cases, the instructions are listed on separate pages, with a special case in the pseudocode for the more general instruction cross-referencing the other page.

For register writes, these meanings include:

- The PC can be specified as the destination register of an LDR instruction. This is done by encoding Rt as 0b1111 . The loaded value is treated as an address, and the effect of execution is a branch to that address. Bit[0] of the loaded value selects whether to execute A32 or T32 instructions after the branch.

- Some other instructions write the PC in similar ways. An instruction can specify that the PC is written:

- Implicitly, for example, branch instructions.

- Explicitly by a register specifier of 0b1111 , for example 16-bit MOV (register) instructions.

- Explicitly by using a register mask, for example LDM instructions.

The address to branch to can be:

- Aloaded value, for example, RFE .

- Aregister value, for example, BX .

- The result of a calculation, for example, TBB or TBH .

The method of choosing the instruction set used after the branch can be:

- Similar to the LDR case, for example, LDM or BX.

- Afixed instruction set other than the one currently being used, for example, the immediate form of BLX .

- Unchanged, for example, branch instructions or 16-bit MOV (register) instructions.

- Set from the SPSR.T bit, for RFE and SUBS PC, LR, #imm8 .

- Discard the result of a calculation. This is done in some cases when one instruction is a special case of another, more general instruction, but with the result discarded. In these cases, the instructions are listed on separate pages, with a special case in the pseudocode for the more general instruction cross-referencing the other page.

- If the destination register specifier of an LDRB , LDRH , LDRSB , or LDRSH instruction is 0b1111 , the instruction is a memory hint instead of a load operation.

- If the destination register specifier of an MRC instruction is 0b1111 , bits[31:28] of the value transferred from the System register are written to the N, Z, C, and V condition flags in the APSR, and bits[27:0] are discarded.

## F1.7.5.2 A32 restrictions on the use of PC or 0b1111 as a register specifier

In A32 instructions, the use of 0b1111 as a register specifier specifies the PC.

Many instructions are CONSTRAINED UNPREDICTABLE if they use 0b1111 as a register specifier. This is specified by pseudocode in the instruction description. Armv8-A constrains the resulting CONSTRAINED UNPREDICTABLE behavior, see Using R15 by instruction.

Note

Arm deprecates use of the PC as the base register in any store instruction.

## F1.7.6 The SP and the use of 0b1101 as a register specifier in T32 and A32 instructions

In the T32 and A32 instruction sets, Arm recommends that the use of 0b1101 as a register specifier specifies the SP.

Note

- The recommendation that the register specifier 0b1101 is used only to specify the SP applies to both the T32 and the A32 instruction sets.
- Despite this recommendation, T32 instructions that can access R13, or the SP, behave predictably from the introduction of Armv8.

## F1.7.7 Modified immediate constants in T32 and A32 instructions

The following sections describe the encoding of modified immediate constants:

- Modified immediate constants in T32 instructions.
- Modified immediate constants in A32 instructions.
- Modified immediate constants in T32 and A32 Advanced SIMD instructions.
- Modified immediate constants in T32 and A32 floating-point instructions.

## F1.7.7.1 Modified immediate constants in T32 instructions

The encoding of a modified immediate constant in a 32-bit T32 instruction is:

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|-----------------------------------------|-----------------------------------------|
| i                                       | imm3 a b c d e f g h                    |

Table F1-5 shows the range of modified immediate constants available in T32 data-processing instructions, and their encoding in the a, b, c, d, e, f, g, h, and i bits, and the imm3 field, in the instruction.

Table F1-5 Encoding of modified immediates in T32 data-processing instructions

| i:imm3:a   | <const> a                                     |
|------------|-----------------------------------------------|
| 0000x      | 00000000 00000000 00000000 abcdefgh           |
| 0001x      | 00000000 abcdefgh 00000000 abcdefgh b         |
| 0010x      | abcdefgh 00000000 abcdefgh 00000000 b         |
| 0011x      | abcdefgh abcdefgh abcdefgh abcdefgh b         |
| 01000      | 1bcdefgh 00000000 00000000 00000000           |
| 01001      | 01bcdefg h0000000 00000000 00000000 c         |
| 01010      | 001bcdef gh000000 00000000 00000000           |
| 01011      | 0001bcde fgh00000 00000000 00000000 c         |
| . . .      | . . . 8-bit values shifted to other positions |
| 11101      | 00000000 00000000 000001bc defgh000 c         |
| 11110      | 00000000 00000000 0000001b cdefgh00           |
| 11111      | 00000000 00000000 00000001 bcdefgh0 c         |

- a. This table shows the immediate constant value in binary form, to relate abcdefgh to the encoding diagram. In assembly syntax, the immediate value is specified in the usual way (a decimal number by default).

b. Arm deprecates using a modified immediate with abcdefgh == 00000000, and these cases are CONSTRAINED UNPREDICTABLE, see UNPREDICTABLE cases in immediate constants in T32 data-processing instructions.

- c. Not available in A32 instructions if h == 1.

Note

Asthe footnotes to Table F1-5 show, the range of values available in T32 modified immediate constants is slightly different from the range of values available in A32 instructions. See Modified immediate constants in A32 instructions for the A32 values.

## F1.7.7.1.1 Carry out

Alogical instruction with i:imm3:a == '00xxx' does not affect the Carry flag. Otherwise, a logical flag-setting instruction sets the Carry flag to the value of bit[31] of the modified immediate constant.

## F1.7.7.1.2 Operation of modified immediate constants, T32 instructions

For a T32 data-processing instruction, the T32ExpandImm() pseudocode function returns the value of the 32-bit immediate constant, calling T32ExpandImm\_C() to evaluate the constant.

## F1.7.7.2 Modified immediate constants in A32 instructions

The encoding of a modified immediate constant in an A32 instruction is:

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4   | 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4   | 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4   |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|                                                                                 | rotation                                                                        | a b c d e f g h                                                                 |

Table F1-6 shows the range of modified immediate constants available in A32 data-processing instructions, and their encoding in the a, b, c, d, e, f, g, and h bits and the rotation field in the instruction.

Table F1-6 Encoding of modified immediates in A32 processing instructions

| rotation   | <const> a                                                   |
|------------|-------------------------------------------------------------|
| 0000       | 00000000 00000000 00000000 abcdefgh                         |
| 0001       | gh000000 00000000 00000000 00abcdef                         |
| 0010       | efgh0000 00000000 00000000 0000abcd                         |
| 0011       | cdefgh00 00000000 00000000 000000ab                         |
| 0100       | abcdefgh 00000000 00000000 00000000                         |
| . . .      | . . . 8-bit values shifted to other even-numbered positions |
| 1001       | 00000000 00abcdef gh000000 00000000                         |
| . . .      | . . . 8-bit values shifted to other even-numbered positions |
| 1110       | 00000000 00000000 0000abcd efgh0000                         |
| 1111       | 00000000 00000000 000000ab cdefgh00                         |

Note

The range of values available in A32 modified immediate constants is slightly different from the range of values available in 32-bit T32 instructions. See Modified immediate constants in T32 instructions.

## F1.7.7.2.1 Carry out

Alogical instruction with the rotation field set to 0b0000 does not affect APSR.C. Otherwise, a logical flag-setting instruction sets APSR.C to the value of bit[31] of the modified immediate constant.

## F1.7.7.2.2 Constants with multiple encodings

Some constant values have multiple possible encodings. In this case, a UAL assembler must select the encoding with the lowest unsigned value of the rotation field. This is the encoding that appears first in Table F1-6. For example, the constant #3 must be encoded with (rotation, abcdefgh) == ( 0b0000 , 0b00000011 ), not ( 0b0001 , 0b00001100 ), ( 0b0010 , 0b00110000 ), or ( 0b0011 , 0b11000000 ).

In particular, this means that all constants in the range 0-255 are encoded with rotation == 0b0000 , and permitted constants outside that range are encoded with rotation != 0b0000 . Aflag-setting logical instruction with a modified immediate constant therefore leaves APSR.C unchanged if the constant is in the range 0-255 and sets it to the most significant bit of the constant otherwise. This matches the behavior of T32 modified immediate constants for all constants that are permitted in both the T32 and A32 instruction sets.

An alternative syntax is available for a modified immediate constant that permits the programmer to specify the encoding directly. In this syntax, #&lt;const&gt; is instead written as #&lt;byte&gt;, #&lt;rot&gt; , where:

&lt;byte&gt;

Is the numeric value of abcdefgh, in the range 0-255.

&lt;rot&gt;

Is twice the numeric value of rotation, an even number in the range 0-30.

This syntax permits all A32 data-processing instructions with modified immediate constants to be disassembled to assembler syntax that assembles to the original instruction.

This syntax also makes it possible to write variants of some flag-setting logical instructions that have different effects on APSR.C to those obtained with the normal #&lt;const&gt; syntax. For example, ANDS R1, R2, #12, #2 has the same behavior as ANDS R1, R2, #3 except that it sets APSR.C to 0 instead of leaving it unchanged. Such variants of flag-setting logical instructions do not have equivalents in the T32 instruction set, and Arm deprecates their use.

## F1.7.7.2.3 Operation of modified immediate constants, A32 instructions

For an A32 data-processing instruction, the A32ExpandImm() pseudocode function returns the value of the 32-bit immediate constant, calling A32ExpandImm\_C() to evaluate the constant.

## F1.7.7.3 Modified immediate constants in T32 and A32 Advanced SIMD instructions

Table F1-7 shows the modified immediate constants available with Advanced SIMD instructions, and how they are encoded.

Table F1-7 Modified immediate values for Advanced SIMD instructions

| op   | cmode   | Constant a        |          |          |          |          |          |          | <dt> b   | Notes   |
|------|---------|-------------------|----------|----------|----------|----------|----------|----------|----------|---------|
| -    | 000x    | 00000000 abcdefgh | 00000000 | 00000000 | abcdefgh | 00000000 | 00000000 | 00000000 | I32      | c       |
|      | 001x    | 00000000 00000000 | 00000000 | abcdefgh | 00000000 | 00000000 | 00000000 | abcdefgh | I32      | c,d     |
|      | 010x    | 00000000 00000000 | abcdefgh | 00000000 | 00000000 | 00000000 | abcdefgh | 00000000 | I32      | c,d     |
|      | 011x    | abcdefgh 00000000 | 00000000 | 00000000 | 00000000 | abcdefgh | 00000000 | 00000000 | I32      | c,d     |
|      | 100x    | 00000000 abcdefgh | abcdefgh | 00000000 | abcdefgh | 00000000 | abcdefgh | 00000000 | I16      | c       |
|      | 101x    | abcdefgh 00000000 | 00000000 | abcdefgh | 00000000 | abcdefgh | 00000000 | abcdefgh | I16      | c,d     |
|      | 1100    | 00000000 11111111 | 00000000 | abcdefgh | 11111111 | 00000000 | 00000000 | abcdefgh | I32      | d,e     |
|      | 1101    | 00000000 11111111 | abcdefgh | 11111111 | 11111111 | 00000000 | abcdefgh | 11111111 | I32      | d,e     |
| 0    | 1110    | abcdefgh abcdefgh | abcdefgh | abcdefgh | abcdefgh | abcdefgh | abcdefgh | abcdefgh | I8       | f       |
|      | 1111    | aBbbbbbc 00000000 | defgh000 | 00000000 | 00000000 | aBbbbbbc | defgh000 | 00000000 | F32      | f,g     |

<!-- image -->

| op   |   cmode | Constant a                                                              | <dt> b   | Notes   |
|------|---------|-------------------------------------------------------------------------|----------|---------|
| 1    |    1110 | aaaaaaaa bbbbbbbb cccccccc dddddddd eeeeeeee ffffffff gggggggg hhhhhhhh | I64      | f       |
|      |    1111 | UNDEFINED                                                               | -        | -       |

- a. In this table, the immediate value is shown in binary form, to relate abcdefgh to the encoding diagram. In assembler syntax, the constant is specified by a data type and a value of that type. That value is specified in the normal way (a decimal number by default) and is replicated enough times to fill the 64-bit immediate. For example, a data type of I32 and a value of 10 specify the 64-bit constant 0x0000000A0000000A .
- b. This specifies the data type used when the instruction is disassembled. On assembly, the data type must be matched in the table if possible. Other data types are permitted as pseudo-instructions when a program is assembled, provided the 64-bit constant specified by the data type and value is available for the instruction. If a constant is available in more than one way, the first entry in this table that can produce it is used. For example, VMOV.I64 D0, #0x8000000080000000 does not specify a 64-bit constant that is available from the I64 line of the table, but does specify one that is available from the fourth I32 line or the F32 line. It is assembled to the first of these, and therefore is disassembled as VMOV.I32 D0, #0x80000000 .
- c. This constant is available for the VBIC , VMOV , VMVN , and VORR instructions.
- d. CONSTRAINED UNPREDICTABLE if abcdefgh == 0b00000000 , see UNPREDICTABLE cases in immediate constants in Advanced SIMD instructions. The required behavior is that these encodings produce an immediate constant of zero.
- e. This constant is available for the VMOV and VMVN instructions only.
- f. This constant is available for the VMOV instruction only.
- g. In this entry, B = NOT( b ). The bit pattern represents the floating-point number (-1) S × 2 exp × mantissa, where S = UInt(a) , exp = UInt(NOT(b):c:d)-3 and mantissa = (16+UInt(e:f:g:h))/16 .

## F1.7.7.3.1 Operation of modified immediate constants, Advanced SIMD instructions

For a T32 or A32 Advanced SIMD instruction that uses a modified immediate constant, the operation described by the AdvSIMDExpandImm() pseudocode function returns the value of the 64-bit immediate constant.

## F1.7.7.4 Modified immediate constants in T32 and A32 floating-point instructions

Table F1-8 shows the immediate constants available in the VMOV (immediate) floating-point instruction, and Table F1-9 shows the resulting floating-point values.

Table F1-8 Floating-point modified immediate constants

| Data type   | imm4H   | imm4L   | Constant a                                                              |
|-------------|---------|---------|-------------------------------------------------------------------------|
| F16         | abcd    | efgh    | aBbbcdef gh000000                                                       |
| F32         | abcd    | efgh    | aBbbbbbc defgh000 00000000 00000000                                     |
| F64         | abcd    | efgh    | aBbbbbbb bbcdefgh 00000000 00000000 00000000 00000000 00000000 00000000 |

Table F1-9 Floating-point constant values

| efgh   |   bcd |      |      |    |            |            |           |          |
|--------|-------|------|------|----|------------|------------|-----------|----------|
|        | 0     | 1    | 10   | 11 | 100        | 101        | 110       | 111      |
| 0000   | 2     | 4    |  8   | 16 |   0.125    |   0.25     |   0.5     |   1      |
| 0001   | 2.125 | 4.25 |  8.5 | 17 |   0.132812 |   0.265625 |   0.53125 |   1.0625 |
| 0010   | 2.25  | 4.5  |  9   | 18 |   0.140625 |   0.28125  |   0.5625  |   1.125  |
| 0011   | 2.375 | 4.75 |  9.5 | 19 |   0.148438 |   0.296875 |   0.59375 |   1.1875 |
| 0100   | 2.5   | 5    | 10   | 20 |   0.15625  |   0.3125   |   0.625   |   1.25   |
| 0101   | 2.625 | 5.25 | 10.5 | 21 |   0.164062 |   0.328125 |   0.65625 |   1.3125 |
| 0110   | 2.75  | 5.5  | 11   | 22 |   0.171875 |   0.34375  |   0.6875  |   1.375  |
| 0111   | 2.875 | 5.75 | 11.5 | 23 |   0.179688 |   0.359375 |   0.71875 |   1.4375 |
| 1000   | 3     | 6    | 12   | 24 |   0.1875   |   0.375    |   0.75    |   1.5    |
| 1001   | 3.125 | 6.25 | 12.5 | 25 |   0.195312 |   0.390625 |   0.78125 |   1.5625 |
| 1010   | 3.25  | 6.5  | 13   | 26 |   0.203125 |   0.40625  |   0.8125  |   1.625  |
| 1011   | 3.375 | 6.75 | 13.5 | 27 |   0.210938 |   0.421875 |   0.84375 |   1.6875 |
| 1100   | 3.5   | 7    | 14   | 28 |   0.21875  |   0.4375   |   0.875   |   1.75   |
| 1101   | 3.625 | 7.25 | 14.5 | 29 |   0.226562 |   0.453125 |   0.90625 |   1.8125 |
| 1110   | 3.75  | 7.5  | 15   | 30 |   0.234375 |   0.46875  |   0.9375  |   1.875  |
| 1111   | 3.875 | 7.75 | 15.5 | 31 |   0.242188 |   0.484375 |   0.96875 |   1.9375 |

## F1.7.7.4.1 Operation of modified immediate constants, floating-point instructions

For a T32 or A32 floating-point instruction that uses a modified immediate constant, the operation described by the VFPExpandImm() pseudocode function returns the value of the immediate constant.