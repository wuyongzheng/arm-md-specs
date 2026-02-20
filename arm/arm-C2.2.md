## C2.2 General information about the A64 instruction descriptions

This section provides general information about the A64 instruction descriptions. Some of this information also applies to System register descriptions, for example the terms defined in Fixed values in AArch64 instruction and System register descriptions apply to the AArch64 descriptions throughout this manual. The following subsections provide this information:

- Execution of instructions in Debug state.
- Fixed values in AArch64 instruction and System register descriptions.
- Modified immediate constants in A64 floating-point instructions.

## C2.2.1 Execution of instructions in Debug state

In general, except for the instructions described in Debug state, the A64 instruction descriptions do not indicate any differences in the behavior of the instruction if it is executed in Debug state. For this information, see Executing instructions in Debug state.

Note

For many instructions, execution is unchanged in Debug state. Executing instructions in Debug state identifies these instructions.

## C2.2.2 Fixed values in AArch64 instruction and System register descriptions

This section summarizes the terms used to describe fixed values in AArch64 register and instruction descriptions. The Glossary gives full descriptions of these terms, and each entry in this section includes a link to the corresponding Glossary entry.

Note

In register descriptions, the meaning of some bits depends on the PE state. This affects the definitions of RES0 and RES1, as shown in the Glossary.

The following terms are used to describe bits or fields with fixed values:

- RAZ Read-As-Zero. See Read-As-Zero (RAZ).

In diagrams, a RAZ bit can be shown as 0.

- (0), RES0

Reserved, Should-Be-Zero (SBZ) or RES0.

In instruction encoding diagrams, and sometimes in other descriptions, (0) indicates an SBZ bit. If the bit is set to 1, behavior is CONSTRAINED UNPREDICTABLE, and must be one of the following:

- The instruction is UNDEFINED.
- The instruction is treated as a NOP .
- The instruction executes as if the value of the bit was 0.
- Any destination registers of the instruction become UNKNOWN.

This notation can be expanded for fields, so a three-bit field can be shown as either (0)(0)(0) or as (000) .

In register diagrams, but not in the A64 encoding and instruction descriptions, bits or fields can be shown as RES0. See the Glossary definition of RES0 for more information.

Note

Some of the System instruction descriptions in this chapter are based on the field description of the input value for the instruction. These are register descriptions and therefore can include RES0 fields,

The (0) and RES0 descriptions can be applied to bits or bit fields that are read-only, or are write-only. The Glossary definitions cover these cases.

RAO

Read-As-One. See Read-As-One (RAO).

In diagrams, a RAO bit can be shown as 1.

(1), RES1

Reserved, Should-Be-One (SBO) or RES1.

In instruction encoding diagrams, and sometimes in other descriptions, (1) indicates an SBO bit. If the bit is set to 0, behavior is CONSTRAINED UNPREDICTABLE, and must be one of the following:

- The instruction is UNDEFINED.
- The instruction is treated as a NOP .
- The instruction executes as if the value of the bit was 1.
- Any destination registers of the instruction become UNKNOWN.

This notation can be expanded for fields, so a three-bit field can be shown as either (1)(1)(1) or as (111) .

In register diagrams, but not in the A64 encoding and instruction descriptions, bits or fields can be shown as RES1. See the Glossary definition of RES1 for more information.

Note

Some of the System instruction descriptions in this chapter are based on the field description of the input value for the instruction. These are register descriptions and therefore can include RES1 fields,

The (1) and RES1 descriptions can be applied to bits or bit fields that are read-only, or are write-only. The Glossary definitions cover these cases.

## C2.2.3 Modified immediate constants in A64 floating-point instructions

Table C2-1 shows the immediate constants available in FMOV (scalar, immediate) and FMOV (vector, immediate) floating-point instructions.

Table C2-1 A64 Floating-point modified immediate constants

| Data type   | immediate   | Constant a                                                              |
|-------------|-------------|-------------------------------------------------------------------------|
| F16         | abcdefgh    | aBbbcdef gh000000                                                       |
| F32         | abcdefgh    | aBbbbbbc defgh000 00000000 00000000                                     |
| F64         | abcdefgh    | aBbbbbbb bbcdefgh 00000000 00000000 00000000 00000000 00000000 00000000 |

The immediate value shown in the table is either:

- The value of the imm8 field for an FMOV (scalar, immediate) instruction, see FMOV (scalar, immediate).
- The value obtained by concatenating the a:b:c:d:e:f:g:h fields for an FMOV (vector, immediate) instruction, see FMOV (vector, immediate).

Table C2-2 shows the floating-point constant values encoded in the b:c:d:e:f:g:h fields of the FMOV (vector, immediate) instruction.

## Table C2-2 Floating-point constant values

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

## C2.2.3.1 Operation of modified immediate constants, floating-point instructions

For an A64 floating-point instruction that uses a modified immediate constant, the operation described by the VFPExpandImm() pseudocode function returns the value of the immediate constant.

## Chapter C3 A64 Instruction Set Overview

This chapter provides an overview of the A64 instruction set. It contains the following sections:

- Branches, Exception generating, and System instructions.
- Loads and stores.
- Loads and stores - SVE, SVE2.
- Loads and stores - SME, SME2, SVE2p1.
- Data processing - immediate.
- Data processing - MTE.
- Data processing - register.
- Data processing - SIMD and floating-point.
- Data processing - SVE.
- Data processing - SVE2.
- Data processing - SME, SME2.

For a structured breakdown of instruction groups by encoding, see A64 Instruction Set Encoding.