## F4.1 A32 instruction set encoding

The A32 instruction stream is a sequence of 32-bit word-aligned words. Each instruction is a single word in the stream.

Most A32 instructions can be conditional, with a condition determined by bits[31:28] of the instruction, the cond field. For more information see The Condition code field in A32 instruction encodings. This applies to all instructions except those with the cond field equal to 0b111 .

The behavior of an attempt to execute an unallocated instruction is described in UNDEFINED, UNPREDICTABLE, and CONSTRAINED UNPREDICTABLE instruction set space.

For more information on A32 instruction encodings see About the T32 and A32 Instruction Descriptions.

The A32 instruction encoding is:

<!-- image -->

Table F4-1 Main encoding table for the A32 instruction set

| Decode fields   | Decode fields   |     | Decode group or instruction page                                           |
|-----------------|-----------------|-----|----------------------------------------------------------------------------|
| cond            | op0             | op1 | Decode group or instruction page                                           |
| != 1111         | 00x             | x   | Data-processing and miscellaneous instructions                             |
| != 1111         | 010             | x   | Load/Store Word, Unsigned Byte (immediate, literal)                        |
| != 1111         | 011             | 0   | Load/Store Word, Unsigned Byte (register)                                  |
| != 1111         | 011             | 1   | Media instructions                                                         |
| xxxx            | 10x             | x   | Branch, branch with link, and block data transfer                          |
| xxxx            | 11x             | x   | System register access, Advanced SIMD, floating-point, and Supervisor call |
| 1111            | 0xx             | x   | Unconditional instructions                                                 |

## F4.1.1 Data-processing and miscellaneous instructions

This section describes the encoding of the Data-processing and miscellaneous instructions group. The encodings in this section are decoded from A32 instruction set encoding.

<!-- image -->

Table F4-2 Encoding table for the Data-processing and miscellaneous instructions group

| Decode fields   | Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page                          |
|-----------------|-----------------|------------------------------------|------------------------------------|------------------------------------|-----------------------------------------------------------|
| op0             | op1             | op2                                | op3                                | op4                                |                                                           |
| 0               | xxxxx           | 1                                  | != 00                              | 1                                  | Extra load/store                                          |
| 0               | 0xxxx           | 1                                  | 00                                 | 1                                  | Multiply and Accumulate                                   |
| 0               | 1xxxx           | 1                                  | 00                                 | 1                                  | Synchronization primitives and Load-Acquire/Store-Release |
| 0               | 10xx0           | 0                                  | xx                                 | x                                  | Miscellaneous                                             |
| 0               | 10xx0           | 1                                  | xx                                 | 0                                  | Halfword Multiply and Accumulate                          |
| 0               | != 10xx0        | x                                  | xx                                 | 0                                  | Data-processing register (immediate shift)                |
| 0               | != 10xx0        | 0                                  | xx                                 | 1                                  | Data-processing register (register shift)                 |
| 1               | xxxxx           | x                                  | xx                                 | x                                  | Data-processing immediate                                 |

## F4.1.1.1 Multiply and Accumulate

This section describes the encoding of the Multiply and Accumulate instruction class. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23   | 28 27 26 25 24 23   | 21 20 19   | 21 20 19   | 16 15 12 11   | 16 15 12 11   | 8 7 6 5 4   |   8 7 6 5 4 |   3 | 0   |
|--------|---------------------|---------------------|------------|------------|---------------|---------------|-------------|-------------|-----|-----|
| !=1111 | 0 0 0 0             | opc                 | S          | RdHi       | RdLo          | Rm            | 1 0         |           0 |   1 | Rn  |

## Table F4-3

|   Decode fields |    | Instruction page   |
|-----------------|----|--------------------|
|             000 | x  | MUL,MULS           |
|             001 | x  | MLA,MLAS           |
|             010 | 0  | UMAAL              |
|             010 | 1  | Unallocated.       |
|             011 | 0  | MLS                |
|             011 | 1  | Unallocated.       |
|             100 | x  | UMULL,UMULLS       |
|             101 | x  | UMLAL,UMLALS       |
|             110 | x  | SMULL, SMULLS      |
|             111 | x  | SMLAL, SMLALS      |

## F4.1.1.2 Halfword Multiply and Accumulate

This section describes the encoding of the Halfword Multiply and Accumulate instruction class. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

## Table F4-4

| Decode fields   |    | Instruction page   |                                    |
|-----------------|----|--------------------|------------------------------------|
| opc             | M  | N                  |                                    |
| 00              | x  | x                  | SMLABB, SMLABT, SMLATB, SMLATT     |
| 01              | 0  | 0                  | SMLAWB, SMLAWT-SMLAWBvariant       |
| 01              | 0  | 1                  | SMULWB, SMULWT-SMULWBvariant       |
| 01              | 1  | 0                  | SMLAWB, SMLAWT-SMLAWTvariant       |
| 01              | 1  | 1                  | SMULWB, SMULWT-SMULWTvariant       |
| 10              | x  | x                  | SMLALBB, SMLALBT, SMLALTB, SMLALTT |
| 11              | x  | x                  | SMULBB, SMULBT, SMULTB, SMULTT     |

## F4.1.2 Extra load/store

This section describes the encoding of the Extra load/store group. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

## Table F4-5 Encoding table for the Extra load/store group

| Decode fields   | Decode group or instruction page                        |
|-----------------|---------------------------------------------------------|
| op0             |                                                         |
| 0               | Load/Store Dual, Half, Signed Byte (register)           |
| 1               | Load/Store Dual, Half, Signed Byte (immediate, literal) |

## F4.1.2.1 Load/Store Dual, Half, Signed Byte (register)

This section describes the encoding of the Load/Store Dual, Half, Signed Byte (register) instruction class. The encodings in this section are decoded from Extra load/store.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8 7 6 5 4 3      |
|--------|---------------------------------|---------|-----------------------------|
| !=1111 | 0 0 0 P U 0 W o1                | Rt      | (0) (0) (0) (0) 1 !=00 1 Rm |
| cond   | op2                             | op2     | op2                         |

## Table F4-6

| Decode fields   | Decode fields   |    |     | Instruction page                        |
|-----------------|-----------------|----|-----|-----------------------------------------|
| P               | W               | o1 | op2 |                                         |
| 0               | 0               | 0  | 01  | STRH (register) - Post-indexed variant  |
| 0               | 0               | 0  | 10  | LDRD(register) - Post-indexed variant   |
| 0               | 0               | 0  | 11  | STRD (register) - Post-indexed variant  |
| 0               | 0               | 1  | 01  | LDRH(register) - Post-indexed variant   |
| 0               | 0               | 1  | 10  | LDRSB (register) - Post-indexed variant |
| 0               | 0               | 1  | 11  | LDRSH (register) - Post-indexed variant |
| 0               | 1               | 0  | 01  | STRHT                                   |
| 0               | 1               | 0  | 10  | Unallocated.                            |
| 0               | 1               | 0  | 11  | Unallocated.                            |
| 0               | 1               | 1  | 01  | LDRHT                                   |
| 0               | 1               | 1  | 10  | LDRSBT                                  |
| 0               | 1               | 1  | 11  | LDRSHT                                  |
| 1               | x               | 0  | 01  | STRH (register) - Pre-indexed variant   |
| 1               | x               | 0  | 10  | LDRD(register) - Pre-indexed variant    |
| 1               | x               | 0  | 11  | STRD (register) - Pre-indexed variant   |
| 1               | x               | 1  | 01  | LDRH(register) - Pre-indexed variant    |
| 1               | x               | 1  | 10  | LDRSB (register) - Pre-indexed variant  |
| 1               | x               | 1  | 11  | LDRSH (register) - Pre-indexed variant  |

## F4.1.2.2 Load/Store Dual, Half, Signed Byte (immediate, literal)

This section describes the encoding of the Load/Store Dual, Half, Signed Byte (immediate, literal) instruction class. The encodings in this section are decoded from Extra load/store.

<!-- image -->

| Decode fields   |    |         |   op2 | Instruction page                         |
|-----------------|----|---------|-------|------------------------------------------|
| xx              |  0 | 1111    |    10 | LDRD(literal)                            |
| != 01           |  1 | 1111    |    01 | LDRH(literal)                            |
| != 01           |  1 | 1111    |    10 | LDRSB (literal)                          |
| != 01           |  1 | 1111    |    11 | LDRSH (literal)                          |
| 00              |  0 | != 1111 |    10 | LDRD(immediate) - Post-indexed variant   |
| 00              |  0 | xxxx    |    01 | STRH (immediate) - Post-indexed variant  |
| 00              |  0 | xxxx    |    11 | STRD (immediate) - Post-indexed variant  |
| 00              |  1 | != 1111 |    01 | LDRH(immediate) - Post-indexed variant   |
| 00              |  1 | != 1111 |    10 | LDRSB (immediate) - Post-indexed variant |
| 00              |  1 | != 1111 |    11 | LDRSH (immediate) - Post-indexed variant |
| 01              |  0 | != 1111 |    10 | Unallocated.                             |
| 01              |  0 | xxxx    |    01 | STRHT                                    |
| 01              |  0 | xxxx    |    11 | Unallocated.                             |
| 01              |  1 | xxxx    |    01 | LDRHT                                    |
| 01              |  1 | xxxx    |    10 | LDRSBT                                   |
| 01              |  1 | xxxx    |    11 | LDRSHT                                   |
| 10              |  0 | != 1111 |    10 | LDRD(immediate) - Offset variant         |
| 10              |  0 | xxxx    |    01 | STRH (immediate) - Offset variant        |
| 10              |  0 | xxxx    |    11 | STRD (immediate) - Offset variant        |
| 10              |  1 | != 1111 |    01 | LDRH(immediate) - Offset variant         |
| 10              |  1 | != 1111 |    10 | LDRSB (immediate) - Offset variant       |
| 10              |  1 | != 1111 |    11 | LDRSH (immediate) - Offset variant       |
| 11              |  0 | != 1111 |    10 | LDRD(immediate) - Pre-indexed variant    |
| 11              |  0 | xxxx    |    01 | STRH (immediate) - Pre-indexed variant   |
| 11              |  0 | xxxx    |    11 | STRD (immediate) - Pre-indexed variant   |
| 11              |  1 | != 1111 |    01 | LDRH(immediate) - Pre-indexed variant    |
| 11              |  1 | != 1111 |    10 | LDRSB (immediate) - Pre-indexed variant  |
| 11              |  1 | != 1111 |    11 | LDRSH (immediate) - Pre-indexed variant  |

## F4.1.3 Synchronization primitives and Load-Acquire/Store-Release

This section describes the encoding of the Synchronization primitives and Load-Acquire/Store-Release group. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

## Table F4-8 Encoding table for the Synchronization primitives and Load-Acquire/Store-Release group

| Decode fields   | Decode group or instruction page                    |
|-----------------|-----------------------------------------------------|
| op0             |                                                     |
| 0               | Unallocated.                                        |
| 1               | Load/Store Exclusive and Load-Acquire/Store-Release |

## F4.1.3.1 Load/Store Exclusive and Load-Acquire/Store-Release

This section describes the encoding of the Load/Store Exclusive and Load-Acquire/Store-Release instruction class. The encodings in this section are decoded from Synchronization primitives and Load-Acquire/Store-Release.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8 7 6 5 4 3    |
|--------|---------------------------------|---------|---------------------------|
| !=1111 | 0 0 0 1 1 size L Rn             | xRd     | (1) (1) exord 1 0 0 1 xRt |

## Table F4-9

|   Decode fields |    |    |    | Instruction page   |
|-----------------|----|----|----|--------------------|
|              00 |  0 |  0 | 0  | STL                |
|              00 |  0 |  0 | 1  | Unallocated.       |
|              00 |  0 |  1 | 0  | STLEX              |
|              00 |  0 |  1 | 1  | STREX              |
|              00 |  1 |  0 | 0  | LDA                |
|              00 |  1 |  0 | 1  | Unallocated.       |
|              00 |  1 |  1 | 0  | LDAEX              |
|              00 |  1 |  1 | 1  | LDREX              |
|              01 |  0 |  0 | x  | Unallocated.       |
|              01 |  0 |  1 | 0  | STLEXD             |
|              01 |  0 |  1 | 1  | STREXD             |

cond

|   Decode fields |    |    |    | Instruction page   |
|-----------------|----|----|----|--------------------|
|              01 |  1 |  0 | x  | Unallocated.       |
|              01 |  1 |  1 | 0  | LDAEXD             |
|              01 |  1 |  1 | 1  | LDREXD             |
|              10 |  0 |  0 | 0  | STLB               |
|              10 |  0 |  0 | 1  | Unallocated.       |
|              10 |  0 |  1 | 0  | STLEXB             |
|              10 |  0 |  1 | 1  | STREXB             |
|              10 |  1 |  0 | 0  | LDAB               |
|              10 |  1 |  0 | 1  | Unallocated.       |
|              10 |  1 |  1 | 0  | LDAEXB             |
|              10 |  1 |  1 | 1  | LDREXB             |
|              11 |  0 |  0 | 0  | STLH               |
|              11 |  0 |  0 | 1  | Unallocated.       |
|              11 |  0 |  1 | 0  | STLEXH             |
|              11 |  0 |  1 | 1  | STREXH             |
|              11 |  1 |  0 | 0  | LDAH               |
|              11 |  1 |  0 | 1  | Unallocated.       |
|              11 |  1 |  1 | 0  | LDAEXH             |
|              11 |  1 |  1 | 1  | LDREXH             |

## F4.1.4 Miscellaneous

This section describes the encoding of the Miscellaneous group. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

| 31     |   28 27 | 23 22 21 20 19 8 7 6   |
|--------|---------|------------------------|
| !=1111 |   00010 | op0 0 0 op1            |

## Table F4-10 Encoding table for the Miscellaneous group

| Decode fields   | Decode group or instruction page   |
|-----------------|------------------------------------|
| 00              | Unallocated.                       |
|                 | 001                                |
| 00              | 010 Unallocated.                   |
| 00              | 011 Unallocated.                   |

| Decode fields   | Decode fields   | Decode group or instruction page   |
|-----------------|-----------------|------------------------------------|
| op0             | op1             | Decode group or instruction page   |
| 00              | 110             | Unallocated.                       |
| 01              | 001             | BX                                 |
| 01              | 010             | BXJ                                |
| 01              | 011             | BLX(register)                      |
| 01              | 110             | Unallocated.                       |
| 10              | 001             | Unallocated.                       |
| 10              | 010             | Unallocated.                       |
| 10              | 011             | Unallocated.                       |
| 10              | 110             | Unallocated.                       |
| 11              | 001             | CLZ                                |
| 11              | 010             | Unallocated.                       |
| 11              | 011             | Unallocated.                       |
| 11              | 110             | ERET                               |
| xx              | 111             | Exception Generation               |
| xx              | 000             | Move special register (register)   |
| xx              | 100             | Cyclic Redundancy Check            |
| xx              | 101             | Integer Saturating Arithmetic      |

## F4.1.4.1 Exception Generation

This section describes the encoding of the Exception Generation instruction class. The encodings in this section are decoded from Miscellaneous.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   |   28 27 26 25 24 23 22 21 20 19 | 28 27 26 25 24 23 22 21 20 19   | 8 7 6 5 4 3   |
|--------|---------------------------------|---------------------------------|---------------------------------|---------------|
| !=1111 | 0 0 0 1 0                       |                               0 | imm12                           | 0 1 1 1 imm4  |

## Table F4-11

|   Decode fields | Instruction page   |
|-----------------|--------------------|
|              00 | HLT                |
|              01 | BKPT               |
|              10 | HVC                |
|              11 | SMC                |

## F4.1.4.2 Move special register (register)

This section describes the encoding of the Move special register (register) instruction class. The encodings in this section are decoded from Miscellaneous.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19 16   | 28 27 26 25 24 23 22 21 20 19 16   |   28 27 26 25 24 23 22 21 20 19 16 | 28 27 26 25 24 23 22 21 20 19 16   | 15               | 12 11 10 9 8 7 6 5 4 3   |
|--------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------|--------------------------|
| !=1111 | 0 0 0 1 0                          | opc                                |                                  0 | mask                               | Rd (0) (0) B m 0 | 0 0 0 Rn                 |

## Table F4-12

| Decode fields   | Instruction page       |
|-----------------|------------------------|
| opc             | B                      |
| x0              | 0 MRS                  |
| x0              | 1 MRS(Banked register) |
| x1              | 0 MSR(register)        |
| x1              | 1 MSR(Banked register) |

## F4.1.4.3 Cyclic Redundancy Check

This section describes the encoding of the Cyclic Redundancy Check instruction class. The encodings in this section are decoded from Miscellaneous.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   |   28 27 26 25 24 23 22 21 20 19 | 16 15   | 12 11 10 9 8 7   | 12 11 10 9 8 7   | 6 5 4   |   6 5 4 |   3 | 0   |
|--------|---------------------------------|---------------------------------|---------------------------------|---------|------------------|------------------|---------|---------|-----|-----|
| !=1111 | 0 0 0 1                         | sz                              |                               0 | Rn      | (0) (0) C        | (0)              | 0 1     |       0 |   0 | Rm  |

## Table F4-13

| Decode fields   |    | Instruction page Feature   |            |
|-----------------|----|----------------------------|------------|
| sz              | C  |                            |            |
| 00              | 0  | CRC32 - CRC32B variant     | FEAT_CRC32 |
| 00              | 1  | CRC32C - CRC32CB variant   | FEAT_CRC32 |
| 01              | 0  | CRC32 - CRC32H variant     | FEAT_CRC32 |
| 01              | 1  | CRC32C - CRC32CH variant   | FEAT_CRC32 |
| 10              | 0  | CRC32 - CRC32W variant     | FEAT_CRC32 |
| 10              | 1  | CRC32C - CRC32CW variant   | FEAT_CRC32 |
| 11              | x  | CONSTRAINED UNPREDICTABLE  | -          |

The behavior of the CONSTRAINED UNPREDICTABLE encodings in this table is described in CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings.

cond

## F4.1.4.4 Integer Saturating Arithmetic

This section describes the encoding of the Integer Saturating Arithmetic instruction class. The encodings in this section are decoded from Miscellaneous.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   |   28 27 26 25 24 23 22 21 20 19 | 16 15   | 16 15                 | 12 11 10 9 8 7 6 5 4 3   |
|--------|---------------------------------|---------------------------------|---------------------------------|---------|-----------------------|--------------------------|
| !=1111 | 0 0 0 1 0                       | opc                             |                               0 | Rn      | (0) (0) (0) (0) 0 1 0 | 1 Rm                     |

## Table F4-14

|   Decode fields | Instruction page   |
|-----------------|--------------------|
|              00 | QADD               |
|              01 | QSUB               |
|              10 | QDADD              |
|              11 | QDSUB              |

## F4.1.5 Data-processing register (immediate shift)

This section describes the encoding of the Data-processing register (immediate shift) group. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

This decode also imposes the constraint:

- op0:op1 != 100 .

Table F4-15 Encoding table for the Data-processing register (immediate shift) group

| Decode fields   | Decode group or instruction page                            |
|-----------------|-------------------------------------------------------------|
| op0             | op1                                                         |
| 0x              | x Integer Data Processing (three register, immediate shift) |
| 10              | 1 Integer Test and Compare (two register, immediate shift)  |

| Decode fields   | Decode group or instruction page                       |
|-----------------|--------------------------------------------------------|
| op0             | op1                                                    |
| 11              | x Logical Arithmetic (three register, immediate shift) |

## F4.1.5.1 Integer Data Processing (three register, immediate shift)

This section describes the encoding of the Integer Data Processing (three register, immediate shift) instruction class. The encodings in this section are decoded from Data-processing register (immediate shift).

| 31     | 28 27 26 25 24 23   | 21 20 19   | 21 20 19   | 16 15   | 12 11   | 7 6 5 4   |   3 | 0   |
|--------|---------------------|------------|------------|---------|---------|-----------|-----|-----|
| !=1111 | 0 0 0 0             | opc        | Rn         | Rd      | imm5    | stype     |   0 | Rm  |

cond

## Table F4-16

| Decode fields   | Decode fields   |         |            | Instruction page                                                       |
|-----------------|-----------------|---------|------------|------------------------------------------------------------------------|
| opc             | S               | Rn      | imm5:stype |                                                                        |
| 000             | x               | xxxx    | != 0000011 | AND, ANDS(register) - ANDS, shift or rotate by value variant           |
| 000             | x               | xxxx    | 0000011    | AND, ANDS(register) - ANDS, rotate right with extend variant           |
| 001             | x               | xxxx    | != 0000011 | EOR, EORS (register) - EORS, shift or rotate by value variant          |
| 001             | x               | xxxx    | 0000011    | EOR, EORS (register) - EORS, rotate right with extend variant          |
| 010             | 0               | != 1101 | != 0000011 | SUB, SUBS (register) - SUB, shift or rotate by value variant           |
| 010             | 0               | != 1101 | 0000011    | SUB, SUBS (register) - SUB, rotate right with extend variant           |
| 010             | 0               | 1101    | != 0000011 | SUB, SUBS (SP minus register) - SUB, shift or rotate by value variant  |
| 010             | 0               | 1101    | 0000011    | SUB, SUBS (SP minus register) - SUB, rotate right with extend variant  |
| 010             | 1               | != 1101 | != 0000011 | SUB, SUBS (register) - SUBS, shift or rotate by value variant          |
| 010             | 1               | != 1101 | 0000011    | SUB, SUBS (register) - SUBS, rotate right with extend variant          |
| 010             | 1               | 1101    | != 0000011 | SUB, SUBS (SP minus register) - SUBS, shift or rotate by value variant |
| 010             | 1               | 1101    | 0000011    | SUB, SUBS (SP minus register) - SUBS, rotate right with extend variant |
| 011             | x               | xxxx    | != 0000011 | RSB, RSBS (register) - RSBS, shift or rotate by value variant          |
| 011             | x               | xxxx    | 0000011    | RSB, RSBS (register) - RSBS, rotate right with extend variant          |
| 100             | 0               | != 1101 | != 0000011 | ADD, ADDS(register) - ADD, shift or rotate by value variant            |
| 100             | 0               | != 1101 | 0000011    | ADD, ADDS(register) - ADD, rotate right with extend variant            |
| 100             | 0               | 1101    | != 0000011 | ADD, ADDS(SP plus register) - ADD, shift or rotate by value variant    |
| 100             | 0               | 1101    | 0000011    | ADD, ADDS(SP plus register) - ADD, rotate right with extend variant    |
| 100             | 1               | != 1101 | != 0000011 | ADD, ADDS(register) - ADDS, shift or rotate by value variant           |
| 100             | 1               | != 1101 | 0000011    | ADD, ADDS(register) - ADDS, rotate right with extend variant           |
| 100             | 1               | 1101    | != 0000011 | ADD, ADDS(SP plus register) - ADDS, shift or rotate by value variant   |
| 100             | 1               | 1101    | 0000011    | ADD, ADDS(SP plus register) - ADDS, rotate right with extend variant   |

| Decode fields   | Decode fields   | Instruction page   | Instruction page   | Instruction page                                              |
|-----------------|-----------------|--------------------|--------------------|---------------------------------------------------------------|
| opc             | S               | Rn                 | imm5:stype         |                                                               |
| 101             | x               | xxxx               | != 0000011         | ADC, ADCS(register) - ADCS, shift or rotate by value variant  |
| 101             | x               | xxxx               | 0000011            | ADC, ADCS(register) - ADCS, rotate right with extend variant  |
| 110             | x               | xxxx               | != 0000011         | SBC, SBCS (register) - SBCS, shift or rotate by value variant |
| 110             | x               | xxxx               | 0000011            | SBC, SBCS (register) - SBCS, rotate right with extend variant |
| 111             | x               | xxxx               | != 0000011         | RSC, RSCS (register) - RSCS, shift or rotate by value variant |
| 111             | x               | xxxx               | 0000011            | RSC, RSCS (register) - RSCS, rotate right with extend variant |

## F4.1.5.2 Integer Test and Compare (two register, immediate shift)

This section describes the encoding of the Integer Test and Compare (two register, immediate shift) instruction class. The encodings in this section are decoded from Data-processing register (immediate shift).

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   |   28 27 26 25 24 23 22 21 20 19 | 16 15 14 13 12 11 7   | 16 15 14 13 12 11 7   | 6 5 4   |       |   3 | 0   |
|--------|---------------------------------|---------------------------------|---------------------------------|-----------------------|-----------------------|---------|-------|-----|-----|
| !=1111 | 0 0                             | opc                             |                               1 | Rn                    | (0) (0) (0) (0)       | imm5    | stype |   0 | Rm  |

## Table F4-17

| Decode fields   |            | Instruction page                                  |
|-----------------|------------|---------------------------------------------------|
| opc             | imm5:stype |                                                   |
| 00              | != 0000011 | TST (register) - Shift or rotate by value variant |
| 00              | 0000011    | TST (register) - Rotate right with extend variant |
| 01              | != 0000011 | TEQ (register) - Shift or rotate by value variant |
| 01              | 0000011    | TEQ (register) - Rotate right with extend variant |
| 10              | != 0000011 | CMP(register) - Shift or rotate by value variant  |
| 10              | 0000011    | CMP(register) - Rotate right with extend variant  |
| 11              | != 0000011 | CMN(register) - Shift or rotate by value variant  |
| 11              | 0000011    | CMN(register) - Rotate right with extend variant  |

## F4.1.5.3 Logical Arithmetic (three register, immediate shift)

This section describes the encoding of the Logical Arithmetic (three register, immediate shift) instruction class. The encodings in this section are decoded from Data-processing register (immediate shift).

<!-- image -->

cond

Table F4-18

| Decode fields   | Decode fields   | Instruction page                                              |
|-----------------|-----------------|---------------------------------------------------------------|
| opc             | imm5:stype      |                                                               |
| 00              | != 0000011      | ORR, ORRS (register) - ORRS, shift or rotate by value variant |
| 00              | 0000011         | ORR, ORRS (register) - ORRS, rotate right with extend variant |
| 01              | != 0000011      | MOV, MOVS(register) - MOVS, shift or rotate by value variant  |
| 01              | 0000011         | MOV, MOVS(register) - MOVS, rotate right with extend variant  |
| 10              | != 0000011      | BIC, BICS (register) - BICS, shift or rotate by value variant |
| 10              | 0000011         | BIC, BICS (register) - BICS, rotate right with extend variant |
| 11              | != 0000011      | MVN, MVNS(register) - MVNS, shift or rotate by value variant  |
| 11              | 0000011         | MVN, MVNS(register) - MVNS, rotate right with extend variant  |

## F4.1.6 Data-processing register (register shift)

This section describes the encoding of the Data-processing register (register shift) group. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

This decode also imposes the constraint:

- op0:op1 != 100 .

Table F4-19 Encoding table for the Data-processing register (register shift) group

| Decode fields   | Decode   | group or instruction page                                |
|-----------------|----------|----------------------------------------------------------|
| 0x              | x        | Integer Data Processing (three register, register shift) |
| 10              | 1        | Integer Test and Compare (two register, register shift)  |
|                 | x        | Logical Arithmetic (three register, register shift)      |
| 11              |          |                                                          |

## F4.1.6.1 Integer Data Processing (three register, register shift)

This section describes the encoding of the Integer Data Processing (three register, register shift) instruction class. The encodings in this section are decoded from Data-processing register (register shift).

<!-- image -->

| 31     | 28 27 26 25 24 23   | 21 20 19   | 21 20 19   | 16 15   | 12 11   | 8 7     | 6 5 4   |   3 | 0   |
|--------|---------------------|------------|------------|---------|---------|---------|---------|-----|-----|
| !=1111 | 0 0 0 0             | opc        | Rn         | Rd      | Rs      | 0 stype |         |   1 | Rm  |

## Table F4-20

| Decode fields   | Instruction page                      |
|-----------------|---------------------------------------|
| opc             |                                       |
| 000             | AND, ANDS(register-shifted register)  |
| 001             | EOR, EORS (register-shifted register) |
| 010             | SUB, SUBS (register-shifted register) |
| 011             | RSB, RSBS (register-shifted register) |
| 100             | ADD, ADDS(register-shifted register)  |
| 101             | ADC, ADCS(register-shifted register)  |
| 110             | SBC, SBCS (register-shifted register) |
| 111             | RSC, RSCS (register-shifted register) |

## F4.1.6.2 Integer Test and Compare (two register, register shift)

This section describes the encoding of the Integer Test and Compare (two register, register shift) instruction class. The encodings in this section are decoded from Data-processing register (register shift).

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   | 16 15 14 13 12 11 8   | 16 15 14 13 12 11 8   | 7 6 5 4 3   |
|--------|---------------------------------|---------------------------------|-----------------------|-----------------------|-------------|
| !=1111 | 0 0 0 1 0                       | opc                             | (0) (0) (0) (0)       | 0 stype 1             | Rm          |

## Table F4-21

| Decode fields   | Instruction page                |
|-----------------|---------------------------------|
| opc             |                                 |
| 00              | TST (register-shifted register) |
| 01              | TEQ (register-shifted register) |
| 10              | CMP(register-shifted register)  |
| 11              | CMN(register-shifted register)  |

## F4.1.6.3 Logical Arithmetic (three register, register shift)

This section describes the encoding of the Logical Arithmetic (three register, register shift) instruction class. The encodings in this section are decoded from Data-processing register (register shift).

cond

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19 16 15 12 11 8 7 6 5   |
|--------|-----------------------------------------------------|
| !=1111 | 0 0 0 1 1 opc S Rn Rd Rs 0 stype                    |

## Table F4-22

| Decode fields   | Instruction page                      |
|-----------------|---------------------------------------|
| opc             |                                       |
| 00              | ORR, ORRS (register-shifted register) |
| 01              | MOV, MOVS(register-shifted register)  |
| 10              | BIC, BICS (register-shifted register) |
| 11              | MVN, MVNS(register-shifted register)  |

## F4.1.7 Data-processing immediate

This section describes the encoding of the Data-processing immediate group. The encodings in this section are decoded from Data-processing and miscellaneous instructions.

<!-- image -->

| 31     |   28 27 | 25 24 23 22 21 20 19   |
|--------|---------|------------------------|
| !=1111 |     001 | op0 op1                |

## Table F4-23 Encoding table for the Data-processing immediate group

| Decode fields   | Decode fields   | Decode group or instruction page                      |
|-----------------|-----------------|-------------------------------------------------------|
| op0             | op1             | Decode group or instruction page                      |
| 0x              | xx              | Integer Data Processing (two register and immediate)  |
| 10              | 00              | Move Halfword (immediate)                             |
| 10              | 10              | Move Special Register and Hints (immediate)           |
| 10              | x1              | Integer Test and Compare (one register and immediate) |
| 11              | xx              | Logical Arithmetic (two register and immediate)       |

## F4.1.7.1 Integer Data Processing (two register and immediate)

This section describes the encoding of the Integer Data Processing (two register and immediate) instruction class. The encodings in this section are decoded from Data-processing immediate.

cond

<!-- image -->

| 31     | 28 27 26 25 24 23   | 28 27 26 25 24 23   | 21 20 19   | 21 20 19   | 16 15 12 11   | 16 15 12 11   | 0     |
|--------|---------------------|---------------------|------------|------------|---------------|---------------|-------|
| !=1111 | 0 0 1 0             | opc                 | S          | Rn         | Rd            | imm12         | imm12 |

## Table F4-24

| Decode fields   | Decode fields   |         | Instruction page                              |
|-----------------|-----------------|---------|-----------------------------------------------|
| opc             | S               | Rn      |                                               |
| 000             | x               | xxxx    | AND, ANDS(immediate)                          |
| 001             | x               | xxxx    | EOR, EORS (immediate)                         |
| 010             | 0               | != 11x1 | SUB, SUBS (immediate) - SUB variant           |
| 010             | 0               | 1101    | SUB, SUBS (SP minus immediate) - SUB variant  |
| 010             | 0               | 1111    | ADR-A2                                        |
| 010             | 1               | != 1101 | SUB, SUBS (immediate) - SUBS variant          |
| 010             | 1               | 1101    | SUB, SUBS (SP minus immediate) - SUBS variant |
| 011             | x               | xxxx    | RSB, RSBS (immediate)                         |
| 100             | 0               | != 11x1 | ADD, ADDS(immediate) - ADDvariant             |
| 100             | 0               | 1101    | ADD, ADDS(SP plus immediate) - ADDvariant     |
| 100             | 0               | 1111    | ADR-A1                                        |
| 100             | 1               | != 1101 | ADD, ADDS(immediate) - ADDSvariant            |
| 100             | 1               | 1101    | ADD, ADDS(SP plus immediate) - ADDSvariant    |
| 101             | x               | xxxx    | ADC, ADCS(immediate)                          |
| 110             | x               | xxxx    | SBC, SBCS (immediate)                         |
| 111             | x               | xxxx    | RSC, RSCS (immediate)                         |

## F4.1.7.2 Move Halfword (immediate)

This section describes the encoding of the Move Halfword (immediate) instruction class. The encodings in this section are decoded from Data-processing immediate.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11   |
|--------|---------------------------------|---------|---------|
| !=1111 | 0 0 1 1 0 H 0 0                 | Rd      | imm12   |

cond

| Decode fields   | Instruction page     |
|-----------------|----------------------|
| H               |                      |
| 0               | MOV, MOVS(immediate) |
| 1               | MOVT                 |

## F4.1.7.3 Move Special Register and Hints (immediate)

This section describes the encoding of the Move Special Register and Hints (immediate) instruction class. The encodings in this section are decoded from Data-processing immediate.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15 14 13 12 11   | 0     |
|--------|---------------------------------|---------------------|-------|
| !=1111 | 0 0 1 1 0 R 1 0                 | (1) (1) (1) (1)     | imm12 |

## Table F4-26

| Decode fields   |              | Instruction page               | Feature     |
|-----------------|--------------|--------------------------------|-------------|
| R:imm4          | imm12        |                                |             |
| != 00000        | xxxxxxxxxxxx | MSR(immediate)                 | -           |
| 00000           | xxxx00000000 | NOP                            | -           |
| 00000           | xxxx00000001 | YIELD                          | -           |
| 00000           | xxxx00000010 | WFE                            | -           |
| 00000           | xxxx00000011 | WFI                            | -           |
| 00000           | xxxx00000100 | SEV                            | -           |
| 00000           | xxxx00000101 | SEVL                           | -           |
| 00000           | xxxx0000011x | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx00001xxx | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx00010000 | ESB                            | FEAT_RAS    |
| 00000           | xxxx00010001 | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx00010010 | TSB                            | FEAT_TRF    |
| 00000           | xxxx00010011 | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx00010100 | CSDB                           | -           |
| 00000           | xxxx00010101 | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx00010110 | CLRBHB                         | FEAT_CLRBHB |
| 00000           | xxxx00010111 | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx00011xxx | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx001xxxxx | Reserved hint, behaves as NOP. | -           |
| 00000           | xxxx01xxxxxx | Reserved hint, behaves as NOP. | -           |

| Decode fields   |              | Instruction page               | Feature   |
|-----------------|--------------|--------------------------------|-----------|
| R:imm4          | imm12        |                                |           |
| 00000           | xxxx10xxxxxx | Reserved hint, behaves as NOP. | -         |
| 00000           | xxxx110xxxxx | Reserved hint, behaves as NOP. | -         |
| 00000           | xxxx1110xxxx | Reserved hint, behaves as NOP. | -         |
| 00000           | xxxx1111xxxx | DBG                            | -         |

## F4.1.7.4 Integer Test and Compare (one register and immediate)

This section describes the encoding of the Integer Test and Compare (one register and immediate) instruction class. The encodings in this section are decoded from Data-processing immediate.

<!-- image -->

## Table F4-27

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| opc             |                    |
| 00              | TST (immediate)    |
| 01              | TEQ (immediate)    |
| 10              | CMP(immediate)     |
| 11              | CMN(immediate)     |

## F4.1.7.5 Logical Arithmetic (two register and immediate)

This section describes the encoding of the Logical Arithmetic (two register and immediate) instruction class. The encodings in this section are decoded from Data-processing immediate.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   | 16 15 12   | 16 15 12   | 11   |
|--------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|------------|------------|------|
| !=1111 |                                 | opc                             | S                               | Rn                              | Rd         | imm12      |      |

cond

|   Decode fields | Instruction page      |
|-----------------|-----------------------|
|              00 | ORR, ORRS (immediate) |
|              01 | MOV, MOVS(immediate)  |
|              10 | BIC, BICS (immediate) |
|              11 | MVN, MVNS(immediate)  |

## F4.1.8 Load/Store Word, Unsigned Byte (immediate, literal)

This section describes the encoding of the Load/Store Word, Unsigned Byte (immediate, literal) instruction class. The encodings in this section are decoded from A32 instruction set encoding.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19 16 15   | 28 27 26 25 24 23 22 21 20 19 16 15   | 12 11   | 12 11   | 0   |
|--------|---------------------------------------|---------------------------------------|---------|---------|-----|
| !=1111 | 0 1 0 P U o2 W o1                     | Rn                                    | Rt      | imm12   |     |

## Table F4-29

| Decode fields   | Decode fields   | Decode fields   | Decode fields   | Instruction page                        |
|-----------------|-----------------|-----------------|-----------------|-----------------------------------------|
| P:W             | o2              | o1              | Rn              |                                         |
| != 01           | 0               | 1               | 1111            | LDR(literal)                            |
| != 01           | 1               | 1               | 1111            | LDRB(literal)                           |
| 00              | 0               | 0               | xxxx            | STR (immediate) - Post-indexed variant  |
| 00              | 0               | 1               | != 1111         | LDR(immediate) - Post-indexed variant   |
| 00              | 1               | 0               | xxxx            | STRB (immediate) - Post-indexed variant |
| 00              | 1               | 1               | != 1111         | LDRB(immediate) - Post-indexed variant  |
| 01              | 0               | 0               | xxxx            | STRT                                    |
| 01              | 0               | 1               | xxxx            | LDRT                                    |
| 01              | 1               | 0               | xxxx            | STRBT                                   |
| 01              | 1               | 1               | xxxx            | LDRBT                                   |
| 10              | 0               | 0               | xxxx            | STR (immediate) - Offset variant        |
| 10              | 0               | 1               | != 1111         | LDR(immediate) - Offset variant         |
| 10              | 1               | 0               | xxxx            | STRB (immediate) - Offset variant       |
| 10              | 1               | 1               | != 1111         | LDRB(immediate) - Offset variant        |
| 11              | 0               | 0               | xxxx            | STR (immediate) - Pre-indexed variant   |
| 11              | 0               | 1               | != 1111         | LDR(immediate) - Pre-indexed variant    |

| Decode fields   | Decode fields   | Instruction page   | Instruction page   | Instruction page                       |
|-----------------|-----------------|--------------------|--------------------|----------------------------------------|
| P:W             | o2              | o1                 |                    | Rn                                     |
| 11              | 1               | 0                  | xxxx               | STRB (immediate) - Pre-indexed variant |
| 11              | 1               | 1                  | != 1111            | LDRB(immediate) - Pre-indexed variant  |

## F4.1.9 Load/Store Word, Unsigned Byte (register)

This section describes the encoding of the Load/Store Word, Unsigned Byte (register) instruction class. The encodings in this section are decoded from A32 instruction set encoding.

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11   | 7 6 5 4 3   | 0   |
|--------|---------------------------------|---------|---------|-------------|-----|
| !=1111 | 0 1 1 P U o2 W o1               | Rn      | Rt      | stype 0     | Rm  |

cond

## Table F4-30

| Decode fields   | Decode fields   |    |    | Instruction page                       |
|-----------------|-----------------|----|----|----------------------------------------|
| P               | o2              | W  | o1 |                                        |
| 0               | 0               | 0  | 0  | STR (register) - Post-indexed variant  |
| 0               | 0               | 0  | 1  | LDR(register) - Post-indexed variant   |
| 0               | 0               | 1  | 0  | STRT                                   |
| 0               | 0               | 1  | 1  | LDRT                                   |
| 0               | 1               | 0  | 0  | STRB (register) - Post-indexed variant |
| 0               | 1               | 0  | 1  | LDRB(register) - Post-indexed variant  |
| 0               | 1               | 1  | 0  | STRBT                                  |
| 0               | 1               | 1  | 1  | LDRBT                                  |
| 1               | 0               | x  | 0  | STR (register) - Pre-indexed variant   |
| 1               | 0               | x  | 1  | LDR(register) - Pre-indexed variant    |
| 1               | 1               | x  | 0  | STRB (register) - Pre-indexed variant  |
| 1               | 1               | x  | 1  | LDRB(register) - Pre-indexed variant   |

## F4.1.10 Media instructions

This section describes the encoding of the Media instructions group. The encodings in this section are decoded from A32 instruction set encoding.

| 31     |   28 27 | 25 24   | 20 19   |
|--------|---------|---------|---------|
| !=1111 |     011 | op0     |         |

## Table F4-31 Encoding table for the Media instructions group

| Decode fields op0   | op1   | Decode group or instruction page     |
|---------------------|-------|--------------------------------------|
| 00xxx               | xxx   | Parallel Arithmetic                  |
| 01000               | 101   | SEL                                  |
| 01000               | 001   | Unallocated.                         |
| 01000               | xx0   | PKHBT, PKHTB                         |
| 01001               | x01   | Unallocated.                         |
| 01001               | xx0   | Unallocated.                         |
| 0110x               | x01   | Unallocated.                         |
| 0110x               | xx0   | Unallocated.                         |
| 01x10               | 001   | Saturate 16-bit                      |
| 01x10               | 101   | Unallocated.                         |
| 01x11               | x01   | Reverse Bit/Byte                     |
| 01x1x               | xx0   | Saturate 32-bit                      |
| 01xxx               | 111   | Unallocated.                         |
| 01xxx               | 011   | Extend and Add                       |
| 10xxx               | xxx   | Signed multiply, Divide              |
| 11000               | 000   | Unsigned Sum of Absolute Differences |
| 11000               | 100   | Unallocated.                         |
| 11001               | x00   | Unallocated.                         |
| 1101x               | x00   | Unallocated.                         |
| 110xx               | 111   | Unallocated.                         |
| 1110x               | 111   | Unallocated.                         |
| 1110x               | x00   | Bitfield Insert                      |
| 11110               | 111   | Unallocated.                         |
| 11111               | 111   | Permanently UNDEFINED                |
| 1111x               | x00   | Unallocated.                         |
| 11x0x               | x10   | Unallocated.                         |
| 11x1x               | x10   | Bitfield Extract                     |
| 11xxx               | 011   | Unallocated.                         |
| 11xxx               | x01   | Unallocated.                         |

## F4.1.10.1 Parallel Arithmetic

This section describes the encoding of the Parallel Arithmetic instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 20   | 28 27 26 25 24 23 22 20   | 19 16 15   | 19 16 15   | 12 11 10 9 8    | 7 6   | 5 4   |   3 | 0   |
|--------|---------------------------|---------------------------|------------|------------|-----------------|-------|-------|-----|-----|
| !=1111 | 0 1 1 0 0                 | op1                       | Rn         | Rd         | (1) (1) (1) (1) | B     | op2   |   1 | Rm  |

## Table F4-32

|   Decode fields op1 | B   | op2   | Instruction page   |
|---------------------|-----|-------|--------------------|
|                 000 | x   | xx    | Unallocated.       |
|                 001 | 0   | 00    | SADD16             |
|                 001 | 0   | 01    | SASX               |
|                 001 | 0   | 10    | SSAX               |
|                 001 | 0   | 11    | SSUB16             |
|                 001 | 1   | 00    | SADD8              |
|                 001 | 1   | 01    | Unallocated.       |
|                 001 | 1   | 10    | Unallocated.       |
|                 001 | 1   | 11    | SSUB8              |
|                 010 | 0   | 00    | QADD16             |
|                 010 | 0   | 01    | QASX               |
|                 010 | 0   | 10    | QSAX               |
|                 010 | 0   | 11    | QSUB16             |
|                 010 | 1   | 00    | QADD8              |
|                 010 | 1   | 01    | Unallocated.       |
|                 010 | 1   | 10    | Unallocated.       |
|                 010 | 1   | 11    | QSUB8              |
|                 011 | 0   | 00    | SHADD16            |
|                 011 | 0   | 01    | SHASX              |
|                 011 | 0   | 10    | SHSAX              |
|                 011 | 0   | 11    | SHSUB16            |
|                 011 | 1   | 00    | SHADD8             |
|                 011 | 1   | 01    | Unallocated.       |
|                 011 | 1   | 10    | Unallocated.       |
|                 011 | 1   | 11    | SHSUB8             |
|                 100 | x   | xx    | Unallocated.       |
|                 101 | 0   | 00    | UADD16             |

| Decode fields   |    |     | Instruction page   |
|-----------------|----|-----|--------------------|
| op1             | B  | op2 |                    |
| 101             | 0  | 01  | UASX               |
| 101             | 0  | 10  | USAX               |
| 101             | 0  | 11  | USUB16             |
| 101             | 1  | 00  | UADD8              |
| 101             | 1  | 01  | Unallocated.       |
| 101             | 1  | 10  | Unallocated.       |
| 101             | 1  | 11  | USUB8              |
| 110             | 0  | 00  | UQADD16            |
| 110             | 0  | 01  | UQASX              |
| 110             | 0  | 10  | UQSAX              |
| 110             | 0  | 11  | UQSUB16            |
| 110             | 1  | 00  | UQADD8             |
| 110             | 1  | 01  | Unallocated.       |
| 110             | 1  | 10  | Unallocated.       |
| 110             | 1  | 11  | UQSUB8             |
| 111             | 0  | 00  | UHADD16            |
| 111             | 0  | 01  | UHASX              |
| 111             | 0  | 10  | UHSAX              |
| 111             | 0  | 11  | UHSUB16            |
| 111             | 1  | 00  | UHADD8             |
| 111             | 1  | 01  | Unallocated.       |
| 111             | 1  | 10  | Unallocated.       |
| 111             | 1  | 11  | UHSUB8             |

## F4.1.10.2 Saturate 16-bit

This section describes the encoding of the Saturate 16-bit instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8 7 6 5   | 4 3   | 0   |
|--------|---------------------------------|---------|----------------------|-------|-----|
| !=1111 | 0 1 1 0 1 U 1 0                 | sat_imm | (1) (1) (1) (1) 0    | 0 1 1 | Rn  |

cond

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| U 0             | SSAT16             |
| 1               | USAT16             |

## F4.1.10.3 Reverse Bit/Byte

This section describes the encoding of the Reverse Bit/Byte instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19 18 17 16 15   | 12 11 10 9 8 7     | 6 5 4   |   3 | 0   |
|--------|---------------------------------------------|--------------------|---------|-----|-----|
| !=1111 | 0 1 1 0 1 o1 1 1 (1) (1) (1) (1)            | (1) (1) (1) (1) o2 | 0 1     |   1 | Rm  |

## Table F4-34

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| o1              | o2                 |
| 0               | 0 REV              |
| 0               | 1 REV16            |
| 1               | 0 RBIT             |
| 1               | 1 REVSH            |

## F4.1.10.4 Saturate 32-bit

This section describes the encoding of the Saturate 32-bit instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20   | 16 15   | 12 11   | 7 6 5 4 3   |
|--------|------------------------------|---------|---------|-------------|
| !=1111 | 0 1 1 0 1 U 1                | sat_imm | Rd      | sh 0 1 Rn   |

cond

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| U 0             | SSAT               |
| 1               | USAT               |

## F4.1.10.5 Extend and Add

This section describes the encoding of the Extend and Add instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8 7   | 6 5 4 3                | 0   |
|--------|---------------------------------|---------|------------------|------------------------|-----|
| !=1111 | 0 1 1 0 1 U                     | op Rn   | Rd               | rotate (0) (0) 0 1 1 1 | Rm  |

## Table F4-36

| Decode fields   | Decode fields   |         | Instruction page   |
|-----------------|-----------------|---------|--------------------|
| U               | op              | Rn      |                    |
| 0               | 00              | != 1111 | SXTAB16            |
| 0               | 00              | 1111    | SXTB16             |
| 0               | 10              | != 1111 | SXTAB              |
| 0               | 10              | 1111    | SXTB               |
| 0               | 11              | != 1111 | SXTAH              |
| 0               | 11              | 1111    | SXTH               |
| 1               | 00              | != 1111 | UXTAB16            |
| 1               | 00              | 1111    | UXTB16             |
| 1               | 10              | != 1111 | UXTAB              |
| 1               | 10              | 1111    | UXTB               |
| 1               | 11              | != 1111 | UXTAH              |
| 1               | 11              | 1111    | UXTH               |

## F4.1.10.6 Signed multiply, Divide

This section describes the encoding of the Signed multiply, Divide instruction class. The encodings in this section are decoded from Media instructions.

| 31     | 28 27 26 25 24 23 22   | 20 19   | 16 15   | 12 11   | 8 7   | 5 4   |   3 | 0   |
|--------|------------------------|---------|---------|---------|-------|-------|-----|-----|
| !=1111 | 0 1 1 1 0              | op1     | Rd      | Ra      | Rm    | op2   |   1 | Rn  |

cond cond

## Table F4-37

| Decode fields   | Decode fields   | Decode fields   | Instruction page                |
|-----------------|-----------------|-----------------|---------------------------------|
| op1             | Ra              | op2             | Instruction page                |
| 000             | != 1111         | 000             | SMLAD, SMLADX-SMLADvariant      |
| 000             | != 1111         | 001             | SMLAD, SMLADX-SMLADXvariant     |
| 000             | != 1111         | 010             | SMLSD, SMLSDX- SMLSDvariant     |
| 000             | != 1111         | 011             | SMLSD, SMLSDX- SMLSDXvariant    |
| 000             | xxxx            | 1xx             | Unallocated.                    |
| 000             | 1111            | 000             | SMUAD, SMUADX-SMUADvariant      |
| 000             | 1111            | 001             | SMUAD, SMUADX-SMUADXvariant     |
| 000             | 1111            | 010             | SMUSD, SMUSDX-SMUSDvariant      |
| 000             | 1111            | 011             | SMUSD, SMUSDX-SMUSDXvariant     |
| 001             | xxxx            | 000             | SDIV                            |
| 001             | xxxx            | != 000          | Unallocated.                    |
| 010             | xxxx            | xxx             | Unallocated.                    |
| 011             | xxxx            | 000             | UDIV                            |
| 011             | xxxx            | != 000          | Unallocated.                    |
| 100             | xxxx            | 000             | SMLALD, SMLALDX-SMLALDvariant   |
| 100             | xxxx            | 001             | SMLALD, SMLALDX-SMLALDXvariant  |
| 100             | xxxx            | 010             | SMLSLD,SMLSLDX - SMLSLD variant |
| 100             | xxxx            | 011             | SMLSLD,SMLSLDX - SMLSLDXvariant |
| 100             | xxxx            | 1xx             | Unallocated.                    |
| 101             | != 1111         | 000             | SMMLA, SMMLAR-SMMLAvariant      |
| 101             | != 1111         | 001             | SMMLA, SMMLAR-SMMLARvariant     |
| 101             | xxxx            | 01x             | Unallocated.                    |
| 101             | xxxx            | 10x             | Unallocated.                    |
| 101             | xxxx            | 110             | SMMLS, SMMLSR-SMMLSvariant      |
| 101             | xxxx            | 111             | SMMLS, SMMLSR-SMMLSRvariant     |
| 101             | 1111            | 000             | SMMUL, SMMULR-SMMULvariant      |
| 101             | 1111            | 001             | SMMUL, SMMULR-SMMULRvariant     |
| 11x             | xxxx            | xxx             | Unallocated.                    |

## F4.1.10.7 Unsigned Sum of Absolute Differences

This section describes the encoding of the Unsigned Sum of Absolute Differences instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19 16 15   | 28 27 26 25 24 23 22 21 20 19 16 15   | 12 11   | 12 11   | 8 7 6 5 4 3   | 0   |
|--------|---------------------------------------|---------------------------------------|---------|---------|---------------|-----|
| !=1111 | 0 1 1 1 1 0 0 0                       | Rd                                    | Ra      | Rm      | 0 0 0 1       | Rn  |

## Table F4-38

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| Ra              |                    |
| != 1111         | USADA8             |
| 1111            | USAD8              |

## F4.1.10.8 Bitfield Insert

This section describes the encoding of the Bitfield Insert instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 16 15   | 28 27 26 25 24 23 22 21 20 16 15   | 12 11   | 12 11   | 7 6 5 4 3   | 0   |
|--------|------------------------------------|------------------------------------|---------|---------|-------------|-----|
| !=1111 | 0 1 1 1 1 1 0                      | msb                                | Rd      | lsb     | 0 0 1       | Rn  |

## Table F4-39

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| Rn              |                    |
| != 1111         | BFI                |
| 1111            | BFC                |

## F4.1.10.9 Permanently UNDEFINED

This section describes the encoding of the Permanently UNDEFINED instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   | 8 7 6 5 4   | 3 0   |
|--------|---------------------------------|---------------------------------|-------------|-------|
| !=1111 | 0 1 1 1 1 1 1 1                 | imm12                           | 1 1 1 1     | imm4  |

cond cond

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| 0xxx            | Unallocated.       |
| 10xx            | Unallocated.       |
| 110x            | Unallocated.       |
| 1110            | UDF                |

## F4.1.10.10 Bitfield Extract

This section describes the encoding of the Bitfield Extract instruction class. The encodings in this section are decoded from Media instructions.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20   | 16 15   | 12 11   | 7 6 5 4   | 3     | 0   |
|--------|------------------------------|---------|---------|-----------|-------|-----|
| !=1111 | 0 1 1 1 1 U 1                | widthm1 | Rd      | lsb       | 1 0 1 | Rn  |

cond

## Table F4-41

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| U               |                    |
| 0               | SBFX               |
| 1               | UBFX               |

## F4.1.11 Branch, branch with link, and block data transfer

This section describes the encoding of the Branch, branch with link, and block data transfer group. The encodings in this section are decoded from A32 instruction set encoding.

<!-- image -->

cond

10

31

28 27 26 25 24

0

op0

Table F4-42 Encoding table for the Branch, branch with link, and block data transfer group

| Decode fields   | Decode group or instruction page   |
|-----------------|------------------------------------|
| 1111            | Exception Save/Restore             |
| != 1111         | Load/Store Multiple                |
| xxxx            | Branch (immediate)                 |

## F4.1.11.1 Exception Save/Restore

This section describes the encoding of the Exception Save/Restore instruction class. The encodings in this section are decoded from Branch, branch with link, and block data transfer.

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 5 4   |
|------------------------------------------|---------|-------|
| 1 1 1 1 1 0 0 P U S W L                  | Rn      | mode  |

## Table F4-43

| Decode fields   | Decode fields   |    | Instruction   | page                                                       |
|-----------------|-----------------|----|---------------|------------------------------------------------------------|
| P               | U               | S  | L             |                                                            |
| x               | x               | 0  | 0             | Unallocated.                                               |
| 0               | 0               | 0  | 1             | RFE, RFEDA, RFEDB, RFEIA, RFEIB - Decrement After variant  |
| 0               | 0               | 1  | 0             | SRS, SRSDA, SRSDB, SRSIA, SRSIB - Decrement After variant  |
| 0               | 1               | 0  | 1             | RFE, RFEDA, RFEDB, RFEIA, RFEIB - Increment After variant  |
| 0               | 1               | 1  | 0             | SRS, SRSDA, SRSDB, SRSIA, SRSIB - Increment After variant  |
| 1               | 0               | 0  | 1             | RFE, RFEDA, RFEDB, RFEIA, RFEIB - Decrement Before variant |
| 1               | 0               | 1  | 0             | SRS, SRSDA, SRSDB, SRSIA, SRSIB - Decrement Before variant |
| x               | x               | 1  | 1             | Unallocated.                                               |
| 1               | 1               | 0  | 1             | RFE, RFEDA, RFEDB, RFEIA, RFEIB - Increment Before variant |
| 1               | 1               | 1  | 0             | SRS, SRSDA, SRSDB, SRSIA, SRSIB - Increment Before variant |

## F4.1.11.2 Load/Store Multiple

This section describes the encoding of the Load/Store Multiple instruction class. The encodings in this section are decoded from Branch, branch with link, and block data transfer.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   |               | 0   |
|--------|---------------------------------|---------|---------------|-----|
| !=1111 | 1 0 0 P U op W L                | Rn      | register_list |     |

cond

## Table F4-44

| Decode fields   | Decode fields   |    |    |                  | Instruction page      |
|-----------------|-----------------|----|----|------------------|-----------------------|
| P               | U               | op | L  | register_list    |                       |
| 0               | 0               | 0  | 0  | xxxxxxxxxxxxxxxx | STMDA,STMED           |
| 0               | 0               | 0  | 1  | xxxxxxxxxxxxxxxx | LDMDA,LDMFA           |
| 0               | 1               | 0  | 0  | xxxxxxxxxxxxxxxx | STM, STMIA,STMEA      |
| 0               | 1               | 0  | 1  | xxxxxxxxxxxxxxxx | LDM, LDMIA,LDMFD      |
| x               | x               | 1  | 0  | xxxxxxxxxxxxxxxx | STM(User registers)   |
| 1               | 0               | 0  | 0  | xxxxxxxxxxxxxxxx | STMDB,STMFD           |
| 1               | 0               | 0  | 1  | xxxxxxxxxxxxxxxx | LDMDB,LDMEA           |
| x               | x               | 1  | 1  | 0xxxxxxxxxxxxxxx | LDM(User registers)   |
| 1               | 1               | 0  | 0  | xxxxxxxxxxxxxxxx | STMIB, STMFA          |
| 1               | 1               | 0  | 1  | xxxxxxxxxxxxxxxx | LDMIB,LDMED           |
| x               | x               | 1  | 1  | 1xxxxxxxxxxxxxxx | LDM(exception return) |

## F4.1.11.3 Branch (immediate)

This section describes the encoding of the Branch (immediate) instruction class. The encodings in this section are decoded from Branch, branch with link, and block data transfer.

<!-- image -->

| 31   | 28 27 26 25 24 23   | 0     |
|------|---------------------|-------|
| cond | 1 0 1 H             | imm24 |

## Table F4-45

| Decode fields   | Instruction   | page                    |
|-----------------|---------------|-------------------------|
| cond            | H             |                         |
| != 1111         | 0             | B                       |
| != 1111         | 1             | BL, BLX(immediate) - A1 |
| 1111            | x             | BL, BLX(immediate) - A2 |

## F4.1.12 System register access, Advanced SIMD, floating-point, and Supervisor call

This section describes the encoding of the System register access, Advanced SIMD, floating-point, and Supervisor call group. The encodings in this section are decoded from A32 instruction set encoding.

<!-- image -->

Table F4-46 Encoding table for the System register access, Advanced SIMD, floating-point, and Supervisor call group

| Decode fields   | Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page                             |
|-----------------|-----------------|------------------------------------|------------------------------------|--------------------------------------------------------------|
| cond            | op0             | op1                                | op2                                |                                                              |
| xxxx            | 0x              | 0x                                 | x                                  | Unallocated.                                                 |
| xxxx            | 10              | 0x                                 | x                                  | Unallocated.                                                 |
| xxxx            | 11              | xx                                 | x                                  | Supervisor call                                              |
| 1111            | != 11           | 1x                                 | x                                  | Unconditional Advanced SIMD and floating-point instructions  |
| != 1111         | 0x              | 1x                                 | x                                  | Advanced SIMD and System register load/store and 64-bit move |
| != 1111         | 10              | 1x                                 | 1                                  | Advanced SIMD and System register 32-bit move                |
| != 1111         | 10              | 10                                 | 0                                  | Floating-point data-processing                               |
| != 1111         | 10              | 11                                 | 0                                  | Unallocated.                                                 |

## F4.1.13 Supervisor call

This section describes the encoding of the Supervisor call group. The encodings in this section are decoded from System register access, Advanced SIMD, floating-point, and Supervisor call.

<!-- image -->

| 31   |   28 27 | 24 23   |
|------|---------|---------|
| cond |    1111 |         |

Table F4-47 Encoding table for the Supervisor call group

| Decode fields   | Decode group or instruction page   |
|-----------------|------------------------------------|
| cond            |                                    |
| 1111            | Unallocated.                       |
| != 1111         | SVC                                |

## F4.1.14 Unconditional Advanced SIMD and floating-point instructions

This section describes the encoding of the Unconditional Advanced SIMD and floating-point instructions group. The encodings in this section are decoded from System register access, Advanced SIMD, floating-point, and Supervisor call.

<!-- image -->

This decode also imposes the constraint:

- op0&lt;2:1&gt; != 11 .

Table F4-48 Encoding table for the Unconditional Advanced SIMD and floating-point instructions group

| Decode fields   | Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page                           |
|-----------------|-----------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------------------------------|
| op0             | op1             | op2                                | op3                                | op4                                | op5                                |                                                            |
| 0xx             | xxxxxx          | x                                  | 0x                                 | x                                  | x                                  | Advanced SIMD three registers of the same length extension |
| 100             | xxxxxx          | 0                                  | != 00                              | 0                                  | 0                                  | Floating-point conditional select                          |
| 101             | 00xxxx          | 0                                  | != 00                              | x                                  | 0                                  | Floating-point minNum/maxNum                               |
| 101             | 110000          | 0                                  | != 00                              | 1                                  | 0                                  | Floating-point extraction and insertion                    |
| 101             | 111xxx          | 0                                  | != 00                              | 1                                  | 0                                  | Floating-point directed convert to integer                 |
| 10x             | xxxxxx          | 0                                  | 00                                 | x                                  | x                                  | Advanced SIMD and floating-point multiply with accumulate  |
| 10x             | xxxxxx          | 1                                  | 0x                                 | x                                  | x                                  | Advanced SIMD and floating-point dot product               |

## F4.1.14.1 Advanced SIMD three registers of the same length extension

This section describes the encoding of the Advanced SIMD three registers of the same length extension instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F4-49

| Decode fields   | Decode fields   |     |     |    |    | Instruction page                             | Feature       |
|-----------------|-----------------|-----|-----|----|----|----------------------------------------------|---------------|
| op1             | op2             | op3 | op4 | Q  | U  |                                              |               |
| x1              | 0x              | 0   | 0   | 0  | 0  | VCADD-64-bit SIMD vector variant             | FEAT_FCMA     |
| x1              | 0x              | 0   | 0   | 0  | 1  | Unallocated.                                 | -             |
| x1              | 0x              | 0   | 0   | 1  | 0  | VCADD-128-bit SIMD vector variant            | FEAT_FCMA     |
| x1              | 0x              | 0   | 0   | 1  | 1  | Unallocated.                                 | -             |
| 00              | 0x              | 0   | 0   | x  | x  | Unallocated.                                 | -             |
| 00              | 0x              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 00              | 00              | 1   | 0   | 0  | 0  | Unallocated.                                 | -             |
| 00              | 00              | 1   | 0   | 0  | 1  | Unallocated.                                 | -             |
| 00              | 00              | 1   | 0   | 1  | 0  | VMMLA                                        | FEAT_AA32BF16 |
| 00              | 00              | 1   | 0   | 1  | 1  | Unallocated.                                 | -             |
| 00              | 00              | 1   | 1   | 0  | 0  | VDOT(vector) - 64-bit SIMD vector variant    | FEAT_AA32BF16 |
| 00              | 00              | 1   | 1   | 0  | 1  | Unallocated.                                 | -             |
| 00              | 00              | 1   | 1   | 1  | 0  | VDOT(vector) - 128-bit SIMD vector variant   | FEAT_AA32BF16 |
| 00              | 00              | 1   | 1   | 1  | 1  | Unallocated.                                 | -             |
| 00              | 01              | 1   | 0   | x  | x  | Unallocated.                                 | -             |
| 00              | 01              | 1   | 1   | x  | x  | Unallocated.                                 | -             |
| 00              | 10              | 0   | 0   | x  | 1  | VFMAL(vector)                                | FEAT_FHM      |
| 00              | 10              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 00              | 10              | 1   | 0   | 0  | x  | Unallocated.                                 | -             |
| 00              | 10              | 1   | 0   | 1  | 0  | VSMMLA                                       | FEAT_AA32I8MM |
| 00              | 10              | 1   | 0   | 1  | 1  | VUMMLA                                       | FEAT_AA32I8MM |
| 00              | 10              | 1   | 1   | 0  | 0  | VSDOT(vector) - 64-bit SIMD vector variant   | FEAT_DotProd  |
| 00              | 10              | 1   | 1   | 0  | 1  | VUDOT(vector) - 64-bit SIMD vector variant   | FEAT_DotProd  |
| 00              | 10              | 1   | 1   | 1  | 0  | VSDOT(vector) - 128-bit SIMD vector variant  | FEAT_DotProd  |
| 00              | 10              | 1   | 1   | 1  | 1  | VUDOT(vector) - 128-bit SIMD vector variant  | FEAT_DotProd  |
| 00              | 11              | 0   | 0   | x  | 1  | VFMAB, VFMAT(BFloat16, vector)               | FEAT_AA32BF16 |
| 00              | 11              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 00              | 11              | 1   | 0   | x  | x  | Unallocated.                                 | -             |
| 00              | 11              | 1   | 1   | x  | x  | Unallocated.                                 | -             |
| 01              | 10              | 0   | 0   | x  | 1  | VFMSL(vector)                                | FEAT_FHM      |
| 01              | 10              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 01              | 10              | 1   | 0   | 0  | x  | Unallocated.                                 | -             |
| 01              | 10              | 1   | 0   | 1  | 0  | VUSMMLA                                      | FEAT_AA32I8MM |
| 01              | 10              | 1   | 0   | 1  | 1  | Unallocated.                                 | -             |
| 01              | 10              | 1   | 1   | 0  | 0  | VUSDOT(vector) - 64-bit SIMD vector variant  | FEAT_AA32I8MM |
| 01              | 10              | 1   | 1   | x  | 1  | Unallocated.                                 | -             |
| 01              | 10              | 1   | 1   | 1  | 0  | VUSDOT(vector) - 128-bit SIMD vector variant | FEAT_AA32I8MM |

| Decode fields   | Decode fields   |     |     |    |    | Instruction page   | Feature   |
|-----------------|-----------------|-----|-----|----|----|--------------------|-----------|
| op1             | op2             | op3 | op4 | Q  | U  |                    |           |
| 01              | 11              | 0   | 1   | x  | x  | Unallocated.       | -         |
| 01              | 11              | 1   | 0   | x  | x  | Unallocated.       | -         |
| 01              | 11              | 1   | 1   | x  | x  | Unallocated.       | -         |
| xx              | 1x              | 0   | 0   | x  | 0  | VCMLA              | FEAT_FCMA |
| 10              | 11              | 0   | 1   | x  | x  | Unallocated.       | -         |
| 10              | 11              | 1   | 0   | x  | x  | Unallocated.       | -         |
| 10              | 11              | 1   | 1   | x  | x  | Unallocated.       | -         |
| 11              | 11              | 0   | 1   | x  | x  | Unallocated.       | -         |
| 11              | 11              | 1   | 0   | x  | x  | Unallocated.       | -         |
| 11              | 11              | 1   | 1   | x  | x  | Unallocated.       | -         |

## F4.1.14.2 Floating-point conditional select

This section describes the encoding of the Floating-point conditional select instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19 16   | 31 30 29 28 27 26 25 24 23 22 21 20 19 16   | 15   | 12 11 10 9 8 7 6 5 4 3   |
|---------------------------------------------|---------------------------------------------|------|--------------------------|
| 1 1 1 1                                     | Vn                                          | Vd   | 1 0 !=00 N 0 M 0 Vm      |

## Table F4-50

|   Decode fields size | Instruction page                                                               | Feature   |
|----------------------|--------------------------------------------------------------------------------|-----------|
|                   01 | VSELEQ, VSELGE, VSELGT, VSELVS - Greater than, half-precision scalar variant   | FEAT_FP16 |
|                   10 | VSELEQ, VSELGE, VSELGT, VSELVS - Greater than, single-precision scalar variant | -         |
|                   11 | VSELEQ, VSELGE, VSELGT, VSELVS - Greater than, double-precision scalar variant | -         |

## F4.1.14.3 Floating-point minNum/maxNum

This section describes the encoding of the Floating-point minNum/maxNum instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8 7 6 5 4 3   |
|------------------------------------------|---------|--------------------------|
| 1 1 1 1 1 1 1 0 1 D 0 0                  | Vn      | 1 0 !=00 N op M 0 Vm     |

size

## Table F4-51

|   Decode fields |    | Instruction page                       | Feature   |
|-----------------|----|----------------------------------------|-----------|
|              01 |  0 | VMAXNM-Half-precision scalar variant   | FEAT_FP16 |
|              01 |  1 | VMINNM-Half-precision scalar variant   | FEAT_FP16 |
|              10 |  0 | VMAXNM-Single-precision scalar variant | -         |
|              10 |  1 | VMINNM-Single-precision scalar variant | -         |
|              11 |  0 | VMAXNM-Double-precision scalar variant | -         |
|              11 |  1 | VMINNM-Double-precision scalar variant | -         |

## F4.1.14.4 Floating-point extraction and insertion

This section describes the encoding of the Floating-point extraction and insertion instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F4-52

|   Decode fields | Instruction   | page         | Feature   |
|-----------------|---------------|--------------|-----------|
|              01 | x             | Unallocated. | -         |
|              10 | 0             | VMOVX        | FEAT_FP16 |
|              10 | 1             | VINS         | FEAT_FP16 |
|              11 | x             | Unallocated. | -         |

## F4.1.14.5 Floating-point directed convert to integer

This section describes the encoding of the Floating-point directed convert to integer instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F4-53

| Decode fields   | Decode fields   |       |    | Instruction page                                          | Feature   |
|-----------------|-----------------|-------|----|-----------------------------------------------------------|-----------|
| o1              | RM              | size  | op |                                                           | Feature   |
| 0               | xx              | != 00 | 1  | Unallocated.                                              | -         |
| 0               | 00              | 01    | 0  | VRINTA (floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 0               | 00              | 10    | 0  | VRINTA (floating-point) - Single-precision scalar variant | -         |
| 0               | 00              | 11    | 0  | VRINTA (floating-point) - Double-precision scalar variant | -         |
| 0               | 01              | 01    | 0  | VRINTN (floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 0               | 01              | 10    | 0  | VRINTN (floating-point) - Single-precision scalar variant | -         |
| 0               | 01              | 11    | 0  | VRINTN (floating-point) - Double-precision scalar variant | -         |
| 0               | 10              | 01    | 0  | VRINTP (floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 0               | 10              | 10    | 0  | VRINTP (floating-point) - Single-precision scalar variant | -         |
| 0               | 10              | 11    | 0  | VRINTP (floating-point) - Double-precision scalar variant | -         |
| 0               | 11              | 01    | 0  | VRINTM (floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 0               | 11              | 10    | 0  | VRINTM (floating-point) - Single-precision scalar variant | -         |
| 0               | 11              | 11    | 0  | VRINTM (floating-point) - Double-precision scalar variant | -         |
| 1               | 00              | 01    | x  | VCVTA(floating-point) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | 00              | 10    | x  | VCVTA(floating-point) - Single-precision scalar variant   | -         |
| 1               | 00              | 11    | x  | VCVTA(floating-point) - Double-precision scalar variant   | -         |
| 1               | 01              | 01    | x  | VCVTN(floating-point) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | 01              | 10    | x  | VCVTN(floating-point) - Single-precision scalar variant   | -         |
| 1               | 01              | 11    | x  | VCVTN(floating-point) - Double-precision scalar variant   | -         |
| 1               | 10              | 01    | x  | VCVTP (floating-point) - Half-precision scalar variant    | FEAT_FP16 |
| 1               | 10              | 10    | x  | VCVTP (floating-point) - Single-precision scalar variant  | -         |
| 1               | 10              | 11    | x  | VCVTP (floating-point) - Double-precision scalar variant  | -         |
| 1               | 11              | 01    | x  | VCVTM(floating-point) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | 11              | 10    | x  | VCVTM(floating-point) - Single-precision scalar variant   | -         |
| 1               | 11              | 11    | x  | VCVTM(floating-point) - Double-precision scalar variant   | -         |

## F4.1.14.6 Advanced SIMD and floating-point multiply with accumulate

This section describes the encoding of the Advanced SIMD and floating-point multiply with accumulate instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F4-54

| Decode fields   | Decode fields   |    |    | Instruction page                                                                   | Feature       |
|-----------------|-----------------|----|----|------------------------------------------------------------------------------------|---------------|
| op1             | op2             | Q  | U  |                                                                                    |               |
| 0               | xx              | x  | 0  | VCMLA(by element) - 128-bit SIMD vector of half-precision floating-point variant   | FEAT_FCMA     |
| 0               | 00              | x  | 1  | VFMAL(by scalar)                                                                   | FEAT_FHM      |
| 0               | 01              | x  | 1  | VFMSL(by scalar)                                                                   | FEAT_FHM      |
| 0               | 10              | x  | 1  | Unallocated.                                                                       | -             |
| 0               | 11              | x  | 1  | VFMAB, VFMAT(BFloat16, by scalar)                                                  | FEAT_AA32BF16 |
| 1               | xx              | 0  | 0  | VCMLA(by element) - 64-bit SIMD vector of single-precision floating-point variant  | FEAT_FCMA     |
| 1               | xx              | x  | 1  | Unallocated.                                                                       | -             |
| 1               | xx              | 1  | 0  | VCMLA(by element) - 128-bit SIMD vector of single-precision floating-point variant | FEAT_FCMA     |

## F4.1.14.7 Advanced SIMD and floating-point dot product

This section describes the encoding of the Advanced SIMD and floating-point dot product instruction class. The encodings in this section are decoded from Unconditional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F4-55

| Decode fields   | Decode fields   |     |    |    | Instruction page                                | Feature       |
|-----------------|-----------------|-----|----|----|-------------------------------------------------|---------------|
| op1             | op2             | op4 | Q  | U  |                                                 | Feature       |
| 0               | 00              | 0   | x  | x  | Unallocated.                                    | -             |
| 0               | 00              | 1   | 0  | 0  | VDOT(by element) - 64-bit SIMD vector variant   | FEAT_AA32BF16 |
| 0               | 00              | 1   | x  | 1  | Unallocated.                                    | -             |
| 0               | 00              | 1   | 1  | 0  | VDOT(by element) - 128-bit SIMD vector variant  | FEAT_AA32BF16 |
| 0               | 01              | 0   | x  | x  | Unallocated.                                    | -             |
| 0               | 10              | 0   | x  | x  | Unallocated.                                    | -             |
| 0               | 10              | 1   | 0  | 0  | VSDOT(by element) - 64-bit SIMD vector variant  | FEAT_DotProd  |
| 0               | 10              | 1   | 0  | 1  | VUDOT(by element) - 64-bit SIMD vector variant  | FEAT_DotProd  |
| 0               | 10              | 1   | 1  | 0  | VSDOT(by element) - 128-bit SIMD vector variant | FEAT_DotProd  |
| 0               | 10              | 1   | 1  | 1  | VUDOT(by element) - 128-bit SIMD vector variant | FEAT_DotProd  |
| 0               | 11              | x   | x  | x  | Unallocated.                                    | -             |

| Decode fields   | Decode fields   |     |    |    | Instruction page                                 | Feature       |
|-----------------|-----------------|-----|----|----|--------------------------------------------------|---------------|
| op1             | op2             | op4 | Q  | U  |                                                  |               |
| 1               | xx              | 0   | x  | x  | Unallocated.                                     | -             |
| 1               | 00              | 1   | 0  | 0  | VUSDOT(by element) - 64-bit SIMD vector variant  | FEAT_AA32I8MM |
| 1               | 00              | 1   | 0  | 1  | VSUDOT(by element) - 64-bit SIMD vector variant  | FEAT_AA32I8MM |
| 1               | 00              | 1   | 1  | 0  | VUSDOT(by element) - 128-bit SIMD vector variant | FEAT_AA32I8MM |
| 1               | 00              | 1   | 1  | 1  | VSUDOT(by element) - 128-bit SIMD vector variant | FEAT_AA32I8MM |
| 1               | 01              | 1   | x  | x  | Unallocated.                                     | -             |
| 1               | 1x              | 1   | x  | x  | Unallocated.                                     | -             |

## F4.1.15 Advanced SIMD and System register load/store and 64-bit move

This section describes the encoding of the Advanced SIMD and System register load/store and 64-bit move group. The encodings in this section are decoded from System register access, Advanced SIMD, floating-point, and Supervisor call.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the A32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

| 31     | 28 27 25 24   | 28 27 25 24   | 21 20   |   21 20 | 12 11 10 9 8   | 0   |
|--------|---------------|---------------|---------|---------|----------------|-----|
| !=1111 |               | op0           |         |       1 | op1            |     |

Table F4-56 Encoding table for the Advanced SIMD and System register load/store and 64-bit move group

| Decode fields   |    | Decode group or instruction page             |
|-----------------|----|----------------------------------------------|
| 00x0            | 0x | Advanced SIMD and floating-point 64-bit move |
| 00x0            | 11 | System register 64-bit move                  |
| != 00x0         | 0x | Advanced SIMD and floating-point load/store  |
| != 00x0         | 11 | System register load/store                   |
| xxxx            | 10 | Unallocated.                                 |

## F4.1.15.1 Advanced SIMD and floating-point 64-bit move

This section describes the encoding of the Advanced SIMD and floating-point 64-bit move instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9   | 8 7 6 5       | 4 3   | 0   |
|--------|---------------------------------|---------|--------------|---------------|-------|-----|
| !=1111 | 1 1 0 0 0 D 0 op                | Rt2     | Rt           | 1 0 size opc2 | M o3  | Vm  |

cond

## Table F4-57

| Decode fields   | Decode fields   | Decode fields   | Decode fields   | Decode fields   | Instruction page                                                                                                              |
|-----------------|-----------------|-----------------|-----------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| D               | op              | size            | opc2            | o3              | Instruction page                                                                                                              |
| 0               | x               | xx              | xx              | x               | Unallocated.                                                                                                                  |
| 1               | x               | xx              | xx              | 0               | Unallocated.                                                                                                                  |
| 1               | x               | 0x              | 00              | 1               | Unallocated.                                                                                                                  |
| 1               | x               | xx              | 01              | x               | Unallocated.                                                                                                                  |
| 1               | 0               | 10              | 00              | 1               | VMOV(between two general-purpose registers and two single-precision registers) - From general-purpose registers variant       |
| 1               | 0               | 11              | 00              | 1               | VMOV(between two general-purpose registers and a doubleword floating-point register) - From general-purpose registers variant |
| 1               | x               | xx              | 1x              | x               | Unallocated.                                                                                                                  |
| 1               | 1               | 10              | 00              | 1               | VMOV(between two general-purpose registers and two single-precision registers) - To general-purpose registers variant         |
| 1               | 1               | 11              | 00              | 1               | VMOV(between two general-purpose registers and a doubleword floating-point register) - To general-purpose registers variant   |

## F4.1.15.2 System register 64-bit move

This section describes the encoding of the System register 64-bit move instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 28 27 26 25 24 23 22 21 20 19   | 16 15 12 11 10   | 16 15 12 11 10   | 9 8 7 4   | 9 8 7 4   | 3   |
|--------|---------------------------------|---------------------------------|------------------|------------------|-----------|-----------|-----|
| !=1111 | 1 1 0 0 0 D                     | L                               | Rt2              | Rt 1             | opc1      | CRm       |     |
| cond   |                                 |                                 |                  |                  |           |           |     |

## Table F4-58

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| D               | L                  |
| 0               | x Unallocated.     |
| 1               | 0 MCRR             |
| 1               | 1 MRRC             |

## F4.1.15.3 Advanced SIMD and floating-point load/store

This section describes the encoding of the Advanced SIMD and floating-point load/store instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8   | 0    |
|--------|---------------------------------|---------|----------------|------|
| !=1111 | 1 1 0 P U D W L                 | Rn      | 1 0 size       | imm8 |

## Table F4-59

| Decode fields   | Decode fields   | Decode fields   |    |         |      |          | Instruction page                                    | Feature   |
|-----------------|-----------------|-----------------|----|---------|------|----------|-----------------------------------------------------|-----------|
| P               | U               | W               | L  | Rn      | size | imm8     |                                                     | Feature   |
| 0               | 0               | 1               | x  | xxxx    | xx   | xxxxxxxx | Unallocated.                                        | -         |
| 0               | 1               | x               | x  | xxxx    | 0x   | xxxxxxxx | Unallocated.                                        | -         |
| 0               | 1               | x               | 0  | xxxx    | 10   | xxxxxxxx | VSTM, VSTMDB, VSTMIA - Increment After variant      | -         |
| 0               | 1               | x               | 0  | xxxx    | 11   | xxxxxxx0 | VSTM, VSTMDB, VSTMIA - Increment After variant      | -         |
| 0               | 1               | x               | 0  | xxxx    | 11   | xxxxxxx1 | FSTMDBX, FSTMIAX - Increment After variant          | -         |
| 0               | 1               | x               | 1  | xxxx    | 10   | xxxxxxxx | VLDM,VLDMDB,VLDMIA-Increment After variant          | -         |
| 0               | 1               | x               | 1  | xxxx    | 11   | xxxxxxx0 | VLDM,VLDMDB,VLDMIA-Increment After variant          | -         |
| 0               | 1               | x               | 1  | xxxx    | 11   | xxxxxxx1 | FLDM*X(FLDMDBX, FLDMIAX) - Increment After variant  | -         |
| 1               | x               | 0               | 0  | xxxx    | 01   | xxxxxxxx | VSTR - Half-precision scalar variant                | FEAT_FP16 |
| 1               | x               | 0               | 0  | xxxx    | 10   | xxxxxxxx | VSTR - Single-precision scalar variant              | -         |
| 1               | x               | 0               | 0  | xxxx    | 11   | xxxxxxxx | VSTR - Double-precision scalar variant              | -         |
| 1               | x               | 0               | 1  | != 1111 | 01   | xxxxxxxx | VLDR(immediate) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | x               | 0               | 1  | != 1111 | 10   | xxxxxxxx | VLDR(immediate) - Single-precision scalar variant   | -         |
| 1               | x               | 0               | 1  | != 1111 | 11   | xxxxxxxx | VLDR(immediate) - Double-precision scalar variant   | -         |
| 1               | 0               | 1               | x  | xxxx    | 0x   | xxxxxxxx | Unallocated.                                        | -         |
| 1               | 0               | 1               | 0  | xxxx    | 10   | xxxxxxxx | VSTM, VSTMDB, VSTMIA - Decrement Before variant     | -         |
| 1               | 0               | 1               | 0  | xxxx    | 11   | xxxxxxx0 | VSTM, VSTMDB, VSTMIA - Decrement Before variant     | -         |
| 1               | 0               | 1               | 0  | xxxx    | 11   | xxxxxxx1 | FSTMDBX, FSTMIAX - Decrement Before variant         | -         |
| 1               | 0               | 1               | 1  | xxxx    | 10   | xxxxxxxx | VLDM,VLDMDB,VLDMIA-Decrement Before variant         | -         |
| 1               | 0               | 1               | 1  | xxxx    | 11   | xxxxxxx0 | VLDM,VLDMDB,VLDMIA-Decrement Before variant         | -         |
| 1               | 0               | 1               | 1  | xxxx    | 11   | xxxxxxx1 | FLDM*X(FLDMDBX, FLDMIAX) - Decrement Before variant | -         |
| 1               | x               | 0               | 1  | 1111    | 01   | xxxxxxxx | VLDR(literal) - Half-precision scalar variant       | FEAT_FP16 |
| 1               | x               | 0               | 1  | 1111    | 10   | xxxxxxxx | VLDR(literal) - Single-precision scalar variant     | -         |
| 1               | x               | 0               | 1  | 1111    | 11   | xxxxxxxx | VLDR(literal) - Double-precision scalar variant     | -         |

cond

| Decode fields   | Decode fields   | Decode fields   | Instruction page   |      |      |          |              | Feature   |
|-----------------|-----------------|-----------------|--------------------|------|------|----------|--------------|-----------|
| P               | U               | W               | L                  | Rn   | size | imm8     |              |           |
| 1               | 1               | 1               | x                  | xxxx | xx   | xxxxxxxx | Unallocated. | -         |

## F4.1.15.4 System register load/store

This section describes the encoding of the System register load/store instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

<!-- image -->

## Table F4-60

| Decode fields   | Decode fields   |    |         |         |      | Instruction page                      |
|-----------------|-----------------|----|---------|---------|------|---------------------------------------|
| P:U:W           | D               | L  | Rn      | CRd     | cp15 |                                       |
| != 000          | 0               | x  | xxxx    | != 0101 | 0    | Unallocated.                          |
| != 000          | 0               | 1  | 1111    | 0101    | 0    | LDC(literal)                          |
| != 000          | x               | x  | xxxx    | xxxx    | 1    | Unallocated.                          |
| != 000          | 1               | x  | xxxx    | 0101    | 0    | Unallocated.                          |
| 0x1             | 0               | 0  | xxxx    | 0101    | 0    | STC - Post-indexed variant            |
| 0x1             | 0               | 1  | != 1111 | 0101    | 0    | LDC(immediate) - Post-indexed variant |
| 010             | 0               | 0  | xxxx    | 0101    | 0    | STC - Unindexed variant               |
| 010             | 0               | 1  | != 1111 | 0101    | 0    | LDC(immediate) - Unindexed variant    |
| 1x0             | 0               | 0  | xxxx    | 0101    | 0    | STC - Offset variant                  |
| 1x0             | 0               | 1  | != 1111 | 0101    | 0    | LDC(immediate) - Offset variant       |
| 1x1             | 0               | 0  | xxxx    | 0101    | 0    | STC - Pre-indexed variant             |
| 1x1             | 0               | 1  | != 1111 | 0101    | 0    | LDC(immediate) - Pre-indexed variant  |

## F4.1.16 Advanced SIMD and System register 32-bit move

This section describes the encoding of the Advanced SIMD and System register 32-bit move group. The encodings in this section are decoded from System register access, Advanced SIMD, floating-point, and Supervisor call.

<!-- image -->

| 31     |   28 27 | 24 23   | 21 20   |   12 11 10 | 8 7   |   5 4 | 0   |
|--------|---------|---------|---------|------------|-------|-------|-----|
| !=1111 |    1110 | op0     |         |          1 | op1   |     1 |     |

Table F4-61 Encoding table for the Advanced SIMD and System register 32-bit move group

| Decode fields   | Decode fields   | Decode group or instruction page                            | Feature   |
|-----------------|-----------------|-------------------------------------------------------------|-----------|
| op0             | op1             |                                                             |           |
| 000             | 000             | Unallocated.                                                | -         |
| 000             | 001             | VMOV(between general-purpose register and half-precision)   | FEAT_FP16 |
| 000             | 010             | VMOV(between general-purpose register and single-precision) | -         |
| 001             | 010             | Unallocated.                                                | -         |
| 01x             | 010             | Unallocated.                                                | -         |
| 10x             | 010             | Unallocated.                                                | -         |
| 110             | 010             | Unallocated.                                                | -         |
| 111             | 010             | Floating-point move special register                        | -         |
| xxx             | 011             | Advanced SIMD 8/16/32-bit element move/duplicate            | -         |
| xxx             | 10x             | Unallocated.                                                | -         |
| xxx             | 11x             | System register 32-bit move                                 | -         |

## F4.1.16.1 Floating-point move special register

This section describes the encoding of the Floating-point move special register instruction class. The encodings in this section are decoded from Advanced SIMD and System register 32-bit move.

| 31     | 28 27 26 25 24 23 22 21 20 19 16   | 28 27 26 25 24 23 22 21 20 19 16   | 15   | 12 11 10 9 8 7 6 5 4 3 2 1 0          |
|--------|------------------------------------|------------------------------------|------|---------------------------------------|
| !=1111 | 1 1 1 0 1 1 1 L                    | reg                                | Rt   | 1 0 1 0 (0) (0) (0) 1 (0) (0) (0) (0) |

## Table F4-62

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | VMSR               |
| 1               | VMRS               |

## F4.1.16.2 Advanced SIMD 8/16/32-bit element move/duplicate

This section describes the encoding of the Advanced SIMD 8/16/32-bit element move/duplicate instruction class. The encodings in this section are decoded from Advanced SIMD and System register 32-bit move.

<!-- image -->

| 31     | 28 27 26 25 24 23 21 20 19 16 15 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|--------|-----------------------------------------------------------------|
| !=1111 | 1 1 1 0 opc1 L Vn Rt 1 0 1 1 N opc2 1 (0) (0) (0) (0)           |

## Table F4-63

| Decode fields   |   Instruction page | opc2   |                                          |
|-----------------|--------------------|--------|------------------------------------------|
| 0xx             |                  0 | xx     | VMOV(general-purpose register to scalar) |
| xxx             |                  1 | xx     | VMOV(scalar to general-purpose register) |
| 1xx             |                  0 | 0x     | VDUP(general-purpose register)           |
| 1xx             |                  0 | 1x     | Unallocated.                             |

## F4.1.16.3 System register 32-bit move

This section describes the encoding of the System register 32-bit move instruction class. The encodings in this section are decoded from Advanced SIMD and System register 32-bit move.

<!-- image -->

## Table F4-64

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | MCR                |
| 1               | MRC                |

## F4.1.17 Floating-point data-processing

This section describes the encoding of the Floating-point data-processing group. The encodings in this section are decoded from System register access, Advanced SIMD, floating-point, and Supervisor call.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the A32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

## Table F4-65 Encoding table for the Floating-point data-processing group

| Decode fields   |    | Decode group or instruction page                 |
|-----------------|----|--------------------------------------------------|
| 1x11            | 1  | Floating-point data-processing (two registers)   |
| 1x11            | 0  | Floating-point move immediate                    |
| != 1x11         | x  | Floating-point data-processing (three registers) |

## F4.1.17.1 Floating-point data-processing (two registers)

This section describes the encoding of the Floating-point data-processing (two registers) instruction class. The encodings in this section are decoded from Floating-point data-processing.

<!-- image -->

## Table F4-66

| Decode fields   | Decode fields   |      |    | Instruction page                                 | Feature   |
|-----------------|-----------------|------|----|--------------------------------------------------|-----------|
| o1              | opc2            | size | o3 |                                                  |           |
| x               | xxx             | 00   | x  | Unallocated.                                     | -         |
| 0               | 000             | 01   | 0  | Unallocated.                                     | -         |
| 0               | 000             | 01   | 1  | VABS - Half-precision scalar variant             | FEAT_FP16 |
| 0               | 000             | 10   | 0  | VMOV(register) - Single-precision scalar variant | -         |
| 0               | 000             | 10   | 1  | VABS - Single-precision scalar variant           | -         |
| 0               | 000             | 11   | 0  | VMOV(register) - Double-precision scalar variant | -         |
| 0               | 000             | 11   | 1  | VABS - Double-precision scalar variant           | -         |
| 0               | 001             | 01   | 0  | VNEG-Half-precision scalar variant               | FEAT_FP16 |
| 0               | 001             | 01   | 1  | VSQRT - Half-precision scalar variant            | FEAT_FP16 |
| 0               | 001             | 10   | 0  | VNEG-Single-precision scalar variant             | -         |

| Decode fields   | Decode fields   |      |    | Instruction page                                                                                   | Feature       |
|-----------------|-----------------|------|----|----------------------------------------------------------------------------------------------------|---------------|
| o1              | opc2            | size | o3 |                                                                                                    |               |
| 0               | 001             | 10   | 1  | VSQRT - Single-precision scalar variant                                                            | -             |
| 0               | 001             | 11   | 0  | VNEG-Double-precision scalar variant                                                               | -             |
| 0               | 001             | 11   | 1  | VSQRT - Double-precision scalar variant                                                            | -             |
| 0               | 010             | 01   | x  | Unallocated.                                                                                       | -             |
| 0               | 010             | 10   | 0  | VCVTB- Half-precision to single-precision variant                                                  | -             |
| 0               | 010             | 10   | 1  | VCVTT- Half-precision to single-precision variant                                                  | -             |
| 0               | 010             | 11   | 0  | VCVTB- Half-precision to double-precision variant                                                  | -             |
| 0               | 010             | 11   | 1  | VCVTT- Half-precision to double-precision variant                                                  | -             |
| 0               | 011             | 01   | 0  | VCVTB(BFloat16)                                                                                    | FEAT_AA32BF16 |
| 0               | 011             | 01   | 1  | VCVTT(BFloat16)                                                                                    | FEAT_AA32BF16 |
| 0               | 011             | 10   | 0  | VCVTB- Single-precision to half-precision variant                                                  | -             |
| 0               | 011             | 10   | 1  | VCVTT- Single-precision to half-precision variant                                                  | -             |
| 0               | 011             | 11   | 0  | VCVTB- Double-precision to half-precision variant                                                  | -             |
| 0               | 011             | 11   | 1  | VCVTT- Double-precision to half-precision variant                                                  | -             |
| 0               | 100             | 01   | 0  | VCMP                                                                                               | FEAT_FP16     |
| 0               | 100             | 01   | 1  | VCMPE                                                                                              | FEAT_FP16     |
| 0               | 100             | 10   | 0  | VCMP                                                                                               | -             |
| 0               | 100             | 10   | 1  | VCMPE                                                                                              | -             |
| 0               | 100             | 11   | 0  | VCMP                                                                                               | -             |
| 0               | 100             | 11   | 1  | VCMPE                                                                                              | -             |
| 0               | 101             | 01   | 0  | VCMP                                                                                               | FEAT_FP16     |
| 0               | 101             | 01   | 1  | VCMPE                                                                                              | FEAT_FP16     |
| 0               | 101             | 10   | 0  | VCMP                                                                                               | -             |
| 0               | 101             | 10   | 1  | VCMPE                                                                                              | -             |
| 0               | 101             | 11   | 0  | VCMP                                                                                               | -             |
| 0               | 101             | 11   | 1  | VCMPE                                                                                              | -             |
| 0               | 110             | 01   | 0  | VRINTR - Half-precision scalar variant                                                             | FEAT_FP16     |
| 0               | 110             | 01   | 1  | VRINTZ (floating-point) - Half-precision scalar variant                                            | FEAT_FP16     |
| 0               | 110             | 10   | 0  | VRINTR - Single-precision scalar variant                                                           | -             |
| 0               | 110             | 10   | 1  | VRINTZ (floating-point) - Single-precision scalar variant                                          | -             |
| 0               | 110             | 11   | 0  | VRINTR - Double-precision scalar variant                                                           | -             |
| 0               | 110             | 11   | 1  | VRINTZ (floating-point) - Double-precision scalar variant                                          | -             |
| 0               | 111             | 01   | 0  | VRINTX (floating-point) - Half-precision scalar variant                                            | FEAT_FP16     |
| 0               | 111             | 01   | 1  | Unallocated.                                                                                       | -             |
| 0               | 111             | 10   | 0  | VRINTX (floating-point) - Single-precision scalar variant                                          | -             |
| 0               | 111             | 10   | 1  | VCVT(between double-precision and single-precision) - Single-precision to double-precision variant | -             |
| 0               | 111             | 11   | 0  | VRINTX (floating-point) - Double-precision scalar variant                                          | -             |
| 0               | 111             | 11   | 1  | VCVT(between double-precision and single-precision) - Double-precision to single-precision variant | -             |

| Decode fields   | Decode fields   |      |    | Instruction page                                                                  | Feature    |
|-----------------|-----------------|------|----|-----------------------------------------------------------------------------------|------------|
| o1              | opc2            | size | o3 |                                                                                   | Feature    |
| 1               | 000             | 01   | x  | VCVT(integer to floating-point, floating-point) - Half-precision scalar variant   | FEAT_FP16  |
| 1               | 000             | 10   | x  | VCVT(integer to floating-point, floating-point) - Single-precision scalar variant | -          |
| 1               | 000             | 11   | x  | VCVT(integer to floating-point, floating-point) - Double-precision scalar variant | -          |
| 1               | 001             | 01   | x  | Unallocated.                                                                      | -          |
| 1               | 001             | 10   | x  | Unallocated.                                                                      | -          |
| 1               | 001             | 11   | 0  | Unallocated.                                                                      | -          |
| 1               | 001             | 11   | 1  | VJCVT                                                                             | FEAT_JSCVT |
| 1               | 01x             | 01   | x  | VCVT(between floating-point and fixed-point, floating-point)                      | FEAT_FP16  |
| 1               | 01x             | 10   | x  | VCVT(between floating-point and fixed-point, floating-point)                      | -          |
| 1               | 01x             | 11   | x  | VCVT(between floating-point and fixed-point, floating-point)                      | -          |
| 1               | 100             | 01   | 0  | VCVTR                                                                             | FEAT_FP16  |
| 1               | 100             | 01   | 1  | VCVT(floating-point to integer, floating-point)                                   | FEAT_FP16  |
| 1               | 100             | 10   | 0  | VCVTR                                                                             | -          |
| 1               | 100             | 10   | 1  | VCVT(floating-point to integer, floating-point)                                   | -          |
| 1               | 100             | 11   | 0  | VCVTR                                                                             | -          |
| 1               | 100             | 11   | 1  | VCVT(floating-point to integer, floating-point)                                   | -          |
| 1               | 101             | 01   | 0  | VCVTR                                                                             | FEAT_FP16  |
| 1               | 101             | 01   | 1  | VCVT(floating-point to integer, floating-point)                                   | FEAT_FP16  |
| 1               | 101             | 10   | 0  | VCVTR                                                                             | -          |
| 1               | 101             | 10   | 1  | VCVT(floating-point to integer, floating-point)                                   | -          |
| 1               | 101             | 11   | 0  | VCVTR                                                                             | -          |
| 1               | 101             | 11   | 1  | VCVT(floating-point to integer, floating-point)                                   | -          |
| 1               | 11x             | 01   | x  | VCVT(between floating-point and fixed-point, floating-point)                      | FEAT_FP16  |
| 1               | 11x             | 10   | x  | VCVT(between floating-point and fixed-point, floating-point)                      | -          |
| 1               | 11x             | 11   | x  | VCVT(between floating-point and fixed-point, floating-point)                      | -          |

## F4.1.17.2 Floating-point move immediate

This section describes the encoding of the Floating-point move immediate instruction class. The encodings in this section are decoded from Floating-point data-processing.

<!-- image -->

| 31     | 28 27 26 25 24 23 22 21 20 19 16 15 12 11 10 9 8 7 6 5 4 3   |
|--------|--------------------------------------------------------------|
| !=1111 | 1 1 1 0 1 D 1 1 imm4H Vd 1 0 size (0) 0 (0) 0 imm4L          |

## Table F4-67

|   Decode fields size | Instruction page                                  | Feature   |
|----------------------|---------------------------------------------------|-----------|
|                   00 | Unallocated.                                      | -         |
|                   01 | VMOV(immediate) - Half-precision scalar variant   | FEAT_FP16 |
|                   10 | VMOV(immediate) - Single-precision scalar variant | -         |
|                   11 | VMOV(immediate) - Double-precision scalar variant | -         |

## F4.1.17.3 Floating-point data-processing (three registers)

This section describes the encoding of the Floating-point data-processing (three registers) instruction class. The encodings in this section are decoded from Floating-point data-processing.

<!-- image -->

## Table F4-68

| Decode fields   | Decode fields   |    | Instruction page                                       | Feature   |
|-----------------|-----------------|----|--------------------------------------------------------|-----------|
| o0:o1           | size            | o2 |                                                        |           |
| != 111          | 00              | x  | Unallocated.                                           | -         |
| 000             | 01              | 0  | VMLA(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 000             | 01              | 1  | VMLS(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 000             | 10              | 0  | VMLA(floating-point) - Single-precision scalar variant | -         |
| 000             | 10              | 1  | VMLS(floating-point) - Single-precision scalar variant | -         |
| 000             | 11              | 0  | VMLA(floating-point) - Double-precision scalar variant | -         |
| 000             | 11              | 1  | VMLS(floating-point) - Double-precision scalar variant | -         |
| 001             | 01              | 0  | VNMLS-Half-precision scalar variant                    | FEAT_FP16 |
| 001             | 01              | 1  | VNMLA-Half-precision scalar variant                    | FEAT_FP16 |
| 001             | 10              | 0  | VNMLS-Single-precision scalar variant                  | -         |
| 001             | 10              | 1  | VNMLA-Single-precision scalar variant                  | -         |
| 001             | 11              | 0  | VNMLS-Double-precision scalar variant                  | -         |
| 001             | 11              | 1  | VNMLA-Double-precision scalar variant                  | -         |
| 010             | 01              | 0  | VMUL(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 010             | 01              | 1  | VNMUL-Half-precision scalar variant                    | FEAT_FP16 |
| 010             | 10              | 0  | VMUL(floating-point) - Single-precision scalar variant | -         |
| 010             | 10              | 1  | VNMUL-Single-precision scalar variant                  | -         |
| 010             | 11              | 0  | VMUL(floating-point) - Double-precision scalar variant | -         |

cond

| Decode fields   | Decode fields   |    | Instruction page                                       | Feature   |
|-----------------|-----------------|----|--------------------------------------------------------|-----------|
| o0:o1           | size            | o2 |                                                        | Feature   |
| 010             | 11              | 1  | VNMUL-Double-precision scalar variant                  | -         |
| 011             | 01              | 0  | VADD(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 011             | 01              | 1  | VSUB(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 011             | 10              | 0  | VADD(floating-point) - Single-precision scalar variant | -         |
| 011             | 10              | 1  | VSUB(floating-point) - Single-precision scalar variant | -         |
| 011             | 11              | 0  | VADD(floating-point) - Double-precision scalar variant | -         |
| 011             | 11              | 1  | VSUB(floating-point) - Double-precision scalar variant | -         |
| 100             | 01              | 0  | VDIV - Half-precision scalar variant                   | FEAT_FP16 |
| 100             | 10              | 0  | VDIV - Single-precision scalar variant                 | -         |
| 100             | 11              | 0  | VDIV - Double-precision scalar variant                 | -         |
| 101             | 01              | 0  | VFNMS-Half-precision scalar variant                    | FEAT_FP16 |
| 101             | 01              | 1  | VFNMA-Half-precision scalar variant                    | FEAT_FP16 |
| 101             | 10              | 0  | VFNMS-Single-precision scalar variant                  | -         |
| 101             | 10              | 1  | VFNMA-Single-precision scalar variant                  | -         |
| 101             | 11              | 0  | VFNMS-Double-precision scalar variant                  | -         |
| 101             | 11              | 1  | VFNMA-Double-precision scalar variant                  | -         |
| 110             | 01              | 0  | VFMA-Half-precision scalar variant                     | FEAT_FP16 |
| 110             | 01              | 1  | VFMS- Half-precision scalar variant                    | FEAT_FP16 |
| 110             | 10              | 0  | VFMA-Single-precision scalar variant                   | -         |
| 110             | 10              | 1  | VFMS- Single-precision scalar variant                  | -         |
| 110             | 11              | 0  | VFMA-Double-precision scalar variant                   | -         |
| 110             | 11              | 1  | VFMS- Double-precision scalar variant                  | -         |

## F4.1.18 Unconditional instructions

This section describes the encoding of the Unconditional instructions group. The encodings in this section are decoded from A32 instruction set encoding.

<!-- image -->

| Decode fields   | Decode fields   | Decode group or instruction page              |
|-----------------|-----------------|-----------------------------------------------|
| op0             | op1             | Decode group or instruction page              |
| 00x             | x               | Miscellaneous                                 |
| 01x             | x               | Advanced SIMD data-processing                 |
| 1xx             | 1               | Memory hints and barriers                     |
| 100             | 0               | Advanced SIMD element or structure load/store |
| 101             | 0               | Unallocated.                                  |
| 11x             | 0               | Unallocated.                                  |

## F4.1.19 Miscellaneous

This section describes the encoding of the Miscellaneous group. The encodings in this section are decoded from Unconditional instructions.

<!-- image -->

|      31 | 25 24   | 20 19   | 8 7 4 3   |
|---------|---------|---------|-----------|
| 1111000 | op0     |         | op1       |

## Table F4-70 Encoding table for the Miscellaneous group

| Decode fields   |      | Decode group or instruction page   | Feature   |
|-----------------|------|------------------------------------|-----------|
| op0             | op1  |                                    |           |
| 0xxxx           | xxxx | Unallocated.                       | -         |
| 10000           | xx0x | Change Process State               | -         |
| 10001           | 1000 | Unallocated.                       | -         |
| 10001           | x100 | Unallocated.                       | -         |
| 10001           | xx01 | Unallocated.                       | -         |
| 10001           | 0000 | SETPAN                             | FEAT_PAN  |
| 1000x           | 0111 | Unallocated.                       | -         |
| 10010           | 0111 | CONSTRAINED UNPREDICTABLE          | -         |
| 10011           | 0111 | Unallocated.                       | -         |
| 1001x           | xx0x | Unallocated.                       | -         |
| 100xx           | 0011 | Unallocated.                       | -         |
| 100xx           | 0x10 | Unallocated.                       | -         |
| 100xx           | 1x1x | Unallocated.                       | -         |
| 101xx           | xxxx | Unallocated.                       | -         |

| 11xxx   | xxxx   | Unallocated.   | -   |
|---------|--------|----------------|-----|

The behavior of the CONSTRAINED UNPREDICTABLE encodings in this table is described in CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings.

## F4.1.19.1 Change Process State

This section describes the encoding of the Change Process State instruction class. The encodings in this section are decoded from Miscellaneous.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5   | 0    |
|-------------------------------------------------------------------------------|------|
| 1 1 1 1 0 0 0 1 0 0 0 0 imod M op (0) (0) (0) (0) (0) (0) E A I F 0           | mode |

## Table F4-71

| Decode fields   | Decode fields   | Instruction page   | Instruction page   | Instruction page   | Instruction page   | Instruction page                                              |
|-----------------|-----------------|--------------------|--------------------|--------------------|--------------------|---------------------------------------------------------------|
| imod            | M               | op                 | I                  | F                  | mode               |                                                               |
| xx              | x               | 1                  | 0                  | 0                  | 0xxxx              | SETEND                                                        |
| 00              | 1               | 0                  | x                  | x                  | xxxxx              | CPS, CPSID, CPSIE - Change mode variant                       |
| 10              | x               | 0                  | x                  | x                  | xxxxx              | CPS, CPSID, CPSIE - Interrupt enable and change mode variant  |
| xx              | x               | 1                  | 0                  | 0                  | 1xxxx              | Unallocated.                                                  |
| xx              | x               | 1                  | 0                  | 1                  | xxxxx              | Unallocated.                                                  |
| xx              | x               | 1                  | 1                  | x                  | xxxxx              | Unallocated.                                                  |
| 11              | x               | 0                  | x                  | x                  | xxxxx              | CPS, CPSID, CPSIE - Interrupt disable and change mode variant |

## F4.1.20 Advanced SIMD data-processing

This section describes the encoding of the Advanced SIMD data-processing group. The encodings in this section are decoded from Unconditional instructions.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the A32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

## Table F4-72 Encoding table for the Advanced SIMD data-processing group

| Decode fields   | Decode fields   | Decode group or instruction page                                     |
|-----------------|-----------------|----------------------------------------------------------------------|
| op0             | op1             | Decode group or instruction page                                     |
| 0               | x               | Advanced SIMD three registers of the same length                     |
| 1               | 0               | Advanced SIMD two registers, or three registers of different lengths |
| 1               | 1               | Advanced SIMD shifts and immediate generation                        |

## F4.1.20.1 Advanced SIMD three registers of the same length

This section describes the encoding of the Advanced SIMD three registers of the same length instruction class. The encodings in this section are decoded from Advanced SIMD data-processing.

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15                       | 12 11   | 7 6 5 4 3   |    | 0   |
|------------------------------------------|-----------------------------|---------|-------------|----|-----|
|                                          | 1 1 1 1 0 0 1 U 0 D size Vn | Vd      | N Q M       | o1 | Vm  |

## Table F4-73

| Decode fields   | Decode fields   |      |    |    | Instruction page     | Feature   |
|-----------------|-----------------|------|----|----|----------------------|-----------|
| U               | size            | opc  | Q  | o1 |                      |           |
| 0               | 0x              | 1100 | x  | 1  | VFMA                 | -         |
| 0               | 0x              | 1101 | x  | 0  | VADD(floating-point) | -         |
| 0               | 0x              | 1101 | x  | 1  | VMLA(floating-point) | -         |
| 0               | 0x              | 1110 | x  | 0  | VCEQ(register) - A2  | -         |
| 0               | 0x              | 1111 | x  | 0  | VMAX(floating-point) | -         |
| 0               | 0x              | 1111 | x  | 1  | VRECPS               | -         |
| x               | xx              | 0000 | x  | 0  | VHADD                | -         |
| 0               | 00              | 0001 | x  | 1  | VAND(register)       | -         |
| x               | xx              | 0000 | x  | 1  | VQADD                | -         |
| x               | xx              | 0001 | x  | 0  | VRHADD               | -         |
| 0               | 00              | 1100 | x  | 0  | SHA1C                | FEAT_SHA1 |
| x               | xx              | 0010 | x  | 0  | VHSUB                | -         |
| 0               | 01              | 0001 | x  | 1  | VBIC (register)      | -         |
| x               | xx              | 0010 | x  | 1  | VQSUB                | -         |
| x               | xx              | 0011 | x  | 0  | VCGT(register) - A1  | -         |
| x               | xx              | 0011 | x  | 1  | VCGE(register) - A1  | -         |
| 0               | 01              | 1100 | x  | 0  | SHA1P                | FEAT_SHA1 |
| 0               | 1x              | 1100 | x  | 1  | VFMS                 | -         |
| 0               | 1x              | 1101 | x  | 0  | VSUB(floating-point) | -         |

| Decode fields   | Decode fields   |      |    |    | Instruction page             | Feature     |
|-----------------|-----------------|------|----|----|------------------------------|-------------|
| U               | size            | opc  | Q  | o1 |                              |             |
| 0               | 1x              | 1101 | x  | 1  | VMLS(floating-point)         | -           |
| 0               | 1x              | 1110 | x  | 0  | Unallocated.                 | -           |
| 0               | 1x              | 1111 | x  | 0  | VMIN(floating-point)         | -           |
| 0               | 1x              | 1111 | x  | 1  | VRSQRTS                      | -           |
| x               | xx              | 0100 | x  | 0  | VSHL (register)              | -           |
| 0               | xx              | 1000 | x  | 0  | VADD(integer)                | -           |
| 0               | 10              | 0001 | x  | 1  | VORR(register)               | -           |
| 0               | xx              | 1000 | x  | 1  | VTST                         | -           |
| x               | xx              | 0100 | x  | 1  | VQSHL(register)              | -           |
| 0               | xx              | 1001 | x  | 0  | VMLA(integer)                | -           |
| x               | xx              | 0101 | x  | 0  | VRSHL                        | -           |
| x               | xx              | 0101 | x  | 1  | VQRSHL                       | -           |
| 0               | xx              | 1011 | x  | 0  | VQDMULH                      | -           |
| 0               | 10              | 1100 | x  | 0  | SHA1M                        | FEAT_SHA1   |
| 0               | xx              | 1011 | x  | 1  | VPADD(integer)               | -           |
| x               | xx              | 0110 | x  | 0  | VMAX(integer)                | -           |
| 0               | 11              | 0001 | x  | 1  | VORN(register)               | -           |
| x               | xx              | 0110 | x  | 1  | VMIN(integer)                | -           |
| x               | xx              | 0111 | x  | 0  | VABD(integer)                | -           |
| x               | xx              | 0111 | x  | 1  | VABA                         | -           |
| 0               | 11              | 1100 | x  | 0  | SHA1SU0                      | FEAT_SHA1   |
| 1               | 0x              | 1101 | x  | 0  | VPADD(floating-point)        | -           |
| 1               | 0x              | 1101 | x  | 1  | VMUL(floating-point)         | -           |
| 1               | 0x              | 1110 | x  | 0  | VCGE(register) - A2          | -           |
| 1               | 0x              | 1110 | x  | 1  | VACGE                        | -           |
| 1               | 0x              | 1111 | 0  | 0  | VPMAX(floating-point)        | -           |
| 1               | 0x              | 1111 | x  | 1  | VMAXNM                       | -           |
| 1               | 00              | 0001 | x  | 1  | VEOR                         | -           |
| x               | xx              | 1001 | x  | 1  | VMUL(integer and polynomial) | -           |
| 1               | 00              | 1100 | x  | 0  | SHA256H                      | FEAT_SHA256 |
| x               | xx              | 1010 | 0  | 0  | VPMAX(integer)               | -           |
| 1               | 01              | 0001 | x  | 1  | VBSL                         | -           |
| x               | xx              | 1010 | 0  | 1  | VPMIN (integer)              | -           |
| x               | xx              | 1010 | 1  | x  | Unallocated.                 | -           |
| 1               | 01              | 1100 | x  | 0  | SHA256H2                     | FEAT_SHA256 |
| 1               | 1x              | 1101 | x  | 0  | VABD(floating-point)         | -           |
| 1               | 1x              | 1110 | x  | 0  | VCGT(register) - A2          | -           |
| 1               | 1x              | 1110 | x  | 1  | VACGT                        | -           |
| 1               | 1x              | 1111 | 0  | 0  | VPMIN (floating-point)       | -           |

| Decode fields   | Decode fields   |      |    |    | Instruction page    | Feature     |
|-----------------|-----------------|------|----|----|---------------------|-------------|
| U               | size            | opc  | Q  | o1 |                     |             |
| 1               | 1x              | 1111 | x  | 1  | VMINNM              | -           |
| 1               | xx              | 1000 | x  | 0  | VSUB(integer)       | -           |
| 1               | 10              | 0001 | x  | 1  | VBIT                | -           |
| 1               | xx              | 1000 | x  | 1  | VCEQ(register) - A1 | -           |
| 1               | xx              | 1001 | x  | 0  | VMLS(integer)       | -           |
| 1               | xx              | 1011 | x  | 0  | VQRDMULH            | -           |
| 1               | 10              | 1100 | x  | 0  | SHA256SU1           | FEAT_SHA256 |
| 1               | xx              | 1011 | x  | 1  | VQRDMLAH            | FEAT_RDM    |
| 1               | 11              | 0001 | x  | 1  | VBIF                | -           |
| 1               | xx              | 1100 | x  | 1  | VQRDMLSH            | FEAT_RDM    |
| 1               | xx              | 1111 | 1  | 0  | Unallocated.        | -           |

## F4.1.21 Advanced SIMD two registers, or three registers of different lengths

This section describes the encoding of the Advanced SIMD two registers, or three registers of different lengths group. The encodings in this section are decoded from Advanced SIMD data-processing.

<!-- image -->

Table F4-74 Encoding table for the Advanced SIMD two registers, or three registers of different lengths group

| Decode fields   | Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page                   |
|-----------------|-----------------|------------------------------------|------------------------------------|----------------------------------------------------|
| op0             | op1             | op2                                | op3                                |                                                    |
| 0               | 11              | xx                                 | x                                  | VEXT(byte elements)                                |
| 1               | 11              | 0x                                 | x                                  | Advanced SIMD two registers misc                   |
| 1               | 11              | 10                                 | x                                  | VTBL,VTBX                                          |
| 1               | 11              | 11                                 | x                                  | Advanced SIMD duplicate (scalar)                   |
| x               | != 11           | xx                                 | 0                                  | Advanced SIMD three registers of different lengths |
| x               | != 11           | xx                                 | 1                                  | Advanced SIMD two registers and a scalar           |

## F4.1.21.1 Advanced SIMD two registers misc

This section describes the encoding of the Advanced SIMD two registers misc instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15   | 12 11 10 7 6 5 4 3   |
|------------------------------------------------------|----------------------|
| 1 1 1 1 0 0 1 1 1 D 1 1 size opc1                    | Vd 0 opc2 Q M 0 Vm   |

## Table F4-75

| Decode fields   | Decode fields   |      |    | Instruction page                                       | Feature       |
|-----------------|-----------------|------|----|--------------------------------------------------------|---------------|
| size            | opc1            | opc2 | Q  | Instruction page                                       | Feature       |
| xx              | 00              | 0000 | x  | VREV64                                                 | -             |
| xx              | 00              | 0001 | x  | VREV32                                                 | -             |
| xx              | 00              | 0010 | x  | VREV16                                                 | -             |
| xx              | 00              | 0011 | x  | Unallocated.                                           | -             |
| xx              | 00              | 010x | x  | VPADDL                                                 | -             |
| xx              | 00              | 0110 | 0  | AESE                                                   | FEAT_AES      |
| xx              | 00              | 0110 | 1  | AESD                                                   | FEAT_AES      |
| xx              | 00              | 0111 | 0  | AESMC                                                  | FEAT_AES      |
| xx              | 00              | 0111 | 1  | AESIMC                                                 | FEAT_AES      |
| xx              | 00              | 1000 | x  | VCLS                                                   | -             |
| 00              | 10              | 0000 | x  | VSWP                                                   | -             |
| xx              | 00              | 1001 | x  | VCLZ                                                   | -             |
| xx              | 00              | 1010 | x  | VCNT                                                   | -             |
| xx              | 00              | 1011 | x  | VMVN(register)                                         | -             |
| 00              | 10              | 1100 | 1  | Unallocated.                                           | -             |
| xx              | 00              | 110x | x  | VPADAL                                                 | -             |
| xx              | 00              | 1110 | x  | VQABS                                                  | -             |
| xx              | 00              | 1111 | x  | VQNEG                                                  | -             |
| xx              | 01              | x000 | x  | VCGT(immediate #0)                                     | -             |
| xx              | 01              | x001 | x  | VCGE(immediate #0)                                     | -             |
| xx              | 01              | x010 | x  | VCEQ(immediate #0)                                     | -             |
| xx              | 01              | x011 | x  | VCLE (immediate #0)                                    | -             |
| xx              | 01              | x100 | x  | VCLT (immediate #0)                                    | -             |
| xx              | 01              | x110 | x  | VABS                                                   | -             |
| xx              | 01              | x111 | x  | VNEG                                                   | -             |
| xx              | 01              | 0101 | 1  | SHA1H                                                  | FEAT_SHA1     |
| 01              | 10              | 1100 | 1  | VCVT(from single-precision to BFloat16, Advanced SIMD) | FEAT_AA32BF16 |
| xx              | 10              | 0001 | x  | VTRN                                                   | -             |
| xx              | 10              | 0010 | x  | VUZP                                                   | -             |
| xx              | 10              | 0011 | x  | VZIP                                                   | -             |

| Decode fields   | Decode fields   |      |    | Instruction page                                                                                              | Feature     |
|-----------------|-----------------|------|----|---------------------------------------------------------------------------------------------------------------|-------------|
| size            | opc1            | opc2 | Q  | Instruction page                                                                                              | Feature     |
| xx              | 10              | 0100 | 0  | VMOVN                                                                                                         | -           |
| xx              | 10              | 0100 | 1  | VQMOVN,VQMOVUN-Unsigned result variant                                                                        | -           |
| xx              | 10              | 0101 | x  | VQMOVN,VQMOVUN-Signed result variant                                                                          | -           |
| xx              | 10              | 0110 | 0  | VSHLL                                                                                                         | -           |
| xx              | 10              | 0111 | 0  | SHA1SU1                                                                                                       | FEAT_SHA1   |
| xx              | 10              | 0111 | 1  | SHA256SU0                                                                                                     | FEAT_SHA256 |
| xx              | 10              | 1000 | x  | VRINTN (Advanced SIMD)                                                                                        | -           |
| xx              | 10              | 1001 | x  | VRINTX (Advanced SIMD)                                                                                        | -           |
| xx              | 10              | 1010 | x  | VRINTA (Advanced SIMD)                                                                                        | -           |
| xx              | 10              | 1011 | x  | VRINTZ (Advanced SIMD)                                                                                        | -           |
| 10              | 10              | 1100 | 1  | Unallocated.                                                                                                  | -           |
| xx              | 10              | 1100 | 0  | VCVT(between half-precision and single-precision, Advanced SIMD) - Single-precision to half-precision variant | -           |
| xx              | 10              | 1101 | x  | VRINTM (Advanced SIMD)                                                                                        | -           |
| xx              | 10              | 1110 | 0  | VCVT(between half-precision and single-precision, Advanced SIMD) - Half-precision to single-precision variant | -           |
| xx              | 10              | 1110 | 1  | Unallocated.                                                                                                  | -           |
| xx              | 10              | 1111 | x  | VRINTP (Advanced SIMD)                                                                                        | -           |
| xx              | 11              | 000x | x  | VCVTA(Advanced SIMD)                                                                                          | -           |
| xx              | 11              | 001x | x  | VCVTN(Advanced SIMD)                                                                                          | -           |
| xx              | 11              | 010x | x  | VCVTP (Advanced SIMD)                                                                                         | -           |
| xx              | 11              | 011x | x  | VCVTM(Advanced SIMD)                                                                                          | -           |
| xx              | 11              | 10x0 | x  | VRECPE                                                                                                        | -           |
| xx              | 11              | 10x1 | x  | VRSQRTE                                                                                                       | -           |
| 11              | 10              | 1100 | 1  | Unallocated.                                                                                                  | -           |
| xx              | 11              | 11xx | x  | VCVT(between floating-point and integer, Advanced SIMD)                                                       | -           |

## F4.1.21.2 Advanced SIMD duplicate (scalar)

This section describes the encoding of the Advanced SIMD duplicate (scalar) instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 7 6 5 4 3   |
|------------------------------------------|---------|------------------------|
| 1 1 1 1 0 0 1 1 1 D 1 1 imm4             |         | 1 1 opc Q M 0 Vm       |

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| 000             | VDUP(scalar)       |
| 001             | Unallocated.       |
| 01x             | Unallocated.       |
| 1xx             | Unallocated.       |

## F4.1.21.3 Advanced SIMD three registers of different lengths

This section describes the encoding of the Advanced SIMD three registers of different lengths instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11   | 7 6 5 4   |
|------------------------------------------|---------|---------|-----------|
| 1 1 1 1 0 0 1 U 1 D !=11                 | Vn      | opc     | N 0 M 0   |

## Table F4-77

| Decode fields   |          | Instruction page              |
|-----------------|----------|-------------------------------|
| U x             | opc 0000 | VADDL                         |
| x               | 0001     | VADDW                         |
| x               | 0010     | VSUBL                         |
| 0               | 0100     | VADDHN                        |
| x               | 0011     | VSUBW                         |
| 0               | 0110     | VSUBHN                        |
| 0               | 1001     | VQDMLAL                       |
| x               | 0101     | VABAL                         |
| 0               | 1011     | VQDMLSL                       |
| 0               | 1101     | VQDMULL                       |
| x               | 0111     | VABDL(integer)                |
| x               | 1000     | VMLAL(integer)                |
| x               | 1010     | VMLSL(integer)                |
| 1               | 0100     | VRADDHN                       |
| 1               | 0110     | VRSUBHN                       |
| x               | 11x0     | VMULL(integer and polynomial) |
| 1               | 1001     | Unallocated.                  |
| 1               | 1011     | Unallocated.                  |

| Decode fields   | Instruction   | page         |
|-----------------|---------------|--------------|
| U               | opc           |              |
| 1               | 1101          | Unallocated. |
| x               | 1111          | Unallocated. |

## F4.1.21.4 Advanced SIMD two registers and a scalar

This section describes the encoding of the Advanced SIMD two registers and a scalar instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11   | 8 7 6 5 4 3   |
|------------------------------------------|---------|---------|---------------|
| 1 1 1 1 0 0 1 Q 1 D !=11                 | Vn      |         | N 1 M 0 Vm    |

size

## Table F4-78

| Decode fields   | Decode fields   | Instruction page   | Feature   |
|-----------------|-----------------|--------------------|-----------|
| Q               | opc             | Instruction page   | Feature   |
| x               | 000x            | VMLA(by scalar)    | -         |
| 0               | 0011            | VQDMLAL            | -         |
| x               | 0010            | VMLAL(by scalar)   | -         |
| 0               | 0111            | VQDMLSL            | -         |
| x               | 010x            | VMLS(by scalar)    | -         |
| 0               | 1011            | VQDMULL            | -         |
| x               | 0110            | VMLSL(by scalar)   | -         |
| x               | 100x            | VMUL(by scalar)    | -         |
| 1               | 0011            | Unallocated.       | -         |
| x               | 1010            | VMULL(by scalar)   | -         |
| 1               | 0111            | Unallocated.       | -         |
| x               | 1100            | VQDMULH            | -         |
| x               | 1101            | VQRDMULH           | -         |
| 1               | 1011            | Unallocated.       | -         |
| x               | 1110            | VQRDMLAH           | FEAT_RDM  |
| x               | 1111            | VQRDMLSH           | FEAT_RDM  |

## F4.1.22 Advanced SIMD shifts and immediate generation

This section describes the encoding of the Advanced SIMD shifts and immediate generation group. The encodings in this section are decoded from Advanced SIMD data-processing.

<!-- image -->

|      31 | 25 24 23 22 21   | 25 24 23 22 21   |   7 6 5 4 3 |
|---------|------------------|------------------|-------------|
| 1111001 |                  | op0              |           1 |

Table F4-79 Encoding table for the Advanced SIMD shifts and immediate generation group

| Decode fields      | Decode group or instruction page                  |
|--------------------|---------------------------------------------------|
| op0                |                                                   |
| 000xxxxxxxxxxx0    | Advanced SIMD one register and modified immediate |
| != 000xxxxxxxxxxx0 | Advanced SIMD two registers and shift amount      |

## F4.1.22.1 Advanced SIMD one register and modified immediate

This section describes the encoding of the Advanced SIMD one register and modified immediate instruction class. The encodings in this section are decoded from Advanced SIMD shifts and immediate generation.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18   | 16 15   | 12 11 8 7 6 5 4 3   |
|---------------------------------------------|---------|---------------------|
| 1 1 1 1 0 0 1 i 1 D 0 0 0 imm3              |         | cmode 0 Q op 1 imm4 |

## Table F4-80

| Decode fields   |    | Instruction page      |
|-----------------|----|-----------------------|
| cmode           | op |                       |
| 0xx0            | 0  | VMOV(immediate) - A1  |
| 0xx0            | 1  | VMVN(immediate) - A1  |
| 0xx1            | 0  | VORR(immediate) - A1  |
| 0xx1            | 1  | VBIC (immediate) - A1 |
| 10x0            | 0  | VMOV(immediate) - A3  |
| 10x0            | 1  | VMVN(immediate) - A2  |
| 10x1            | 0  | VORR(immediate) - A2  |
| 10x1            | 1  | VBIC (immediate) - A2 |
| 11xx            | 0  | VMOV(immediate) - A4  |
| 110x            | 1  | VMVN(immediate) - A3  |
| 1110            | 1  | VMOV(immediate) - A5  |
| 1111            | 1  | Unallocated.          |

## F4.1.22.2 Advanced SIMD two registers and shift amount

This section describes the encoding of the Advanced SIMD two registers and shift amount instruction class. The encodings in this section are decoded from Advanced SIMD shifts and immediate generation.

| 31 30 29 28 27 26 25 24 23 22 21   | 19 18   | 16 15   | 12 11   | 8 7 6 5 4 3   |
|------------------------------------|---------|---------|---------|---------------|
| 1 1 1 1 0 0 1 U 1 D imm3H          | imm3L   | Vd      | opc     | L Q M 1 Vm    |

## Table F4-81

| Decode fields   | Decode fields   |       |      |    |    | Instruction page                                                        |
|-----------------|-----------------|-------|------|----|----|-------------------------------------------------------------------------|
| U               | imm3H:L         | imm3L | opc  | L  | Q  |                                                                         |
| x               | != 0000         | xxx   | 0000 | x  | x  | VSHR                                                                    |
| x               | != 0000         | xxx   | 0001 | x  | x  | VSRA                                                                    |
| x               | != 0000         | 000   | 1010 | x  | 0  | VMOVL                                                                   |
| x               | != 0000         | xxx   | 0010 | x  | x  | VRSHR                                                                   |
| x               | != 0000         | xxx   | 0011 | x  | x  | VRSRA                                                                   |
| x               | != 0000         | xxx   | 0111 | x  | x  | VQSHL, VQSHLU(immediate) - 128-bit SIMD vector, signed result variant   |
| x               | != 0000         | xxx   | 1001 | 0  | 0  | VQSHRN, VQSHRUN-Signed result variant                                   |
| x               | != 0000         | xxx   | 1001 | 0  | 1  | VQRSHRN, VQRSHRUN-Signed result variant                                 |
| x               | != 0000         | xxx   | 1010 | 0  | 0  | VSHLL                                                                   |
| x               | != 0000         | xxx   | 11xx | 0  | x  | VCVT(between floating-point and fixed-point, Advanced SIMD)             |
| 0               | != 0000         | xxx   | 0101 | x  | x  | VSHL (immediate)                                                        |
| 0               | != 0000         | xxx   | 1000 | 0  | 0  | VSHRN                                                                   |
| 0               | != 0000         | xxx   | 1000 | 0  | 1  | VRSHRN                                                                  |
| 1               | != 0000         | xxx   | 0100 | x  | x  | VSRI                                                                    |
| 1               | != 0000         | xxx   | 0101 | x  | x  | VSLI                                                                    |
| 1               | != 0000         | xxx   | 0110 | x  | x  | VQSHL, VQSHLU(immediate) - 128-bit SIMD vector, unsigned result variant |
| 1               | != 0000         | xxx   | 1000 | 0  | 0  | VQSHRN, VQSHRUN-Unsigned result variant                                 |
| 1               | != 0000         | xxx   | 1000 | 0  | 1  | VQRSHRN, VQRSHRUN-Unsigned result variant                               |

## F4.1.23 Memory hints and barriers

This section describes the encoding of the Memory hints and barriers group. The encodings in this section are decoded from Unconditional instructions.

<!-- image -->

## Table F4-82 Encoding table for the Memory hints and barriers group

| Decode fields   |       | Decode group or instruction page   |
|-----------------|-------|------------------------------------|
| op0 00xx1       | op1 x | CONSTRAINED UNPREDICTABLE          |
| 01001           | x     | CONSTRAINED UNPREDICTABLE          |
| 01011           | x     | Barriers                           |
| 011x1           | x     | CONSTRAINED UNPREDICTABLE          |
| 0xxx0           | x     | Preload (immediate)                |
| 1xxx0           | 0     | Preload (register)                 |
| 1xxx1           | 0     | CONSTRAINED UNPREDICTABLE          |
| 1xxxx           | 1     | Unallocated.                       |

The behavior of the CONSTRAINED UNPREDICTABLE encodings in this table is described in CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings.

## F4.1.23.1 Barriers

This section describes the encoding of the Barriers instruction class. The encodings in this section are decoded from Memory hints and barriers.

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7   | 4 3    | 0      |
|---------------------------------------------------------------------------|--------|--------|
| 1 1 1 1 0 1 0 1 0 1 1 1 (1) (1) (1) (1) (1) (1) (1) (1) (0) (0) (0) (0)   | opcode | option |

## Table F4-83

| Decode fields   | Instruction   | page                      | Feature   |
|-----------------|---------------|---------------------------|-----------|
| opcode          | option        |                           |           |
| 0000            | xxxx          | CONSTRAINED UNPREDICTABLE | -         |
| 0001            | xxxx          | CLREX                     | -         |
| 001x            | xxxx          | CONSTRAINED UNPREDICTABLE | -         |

| Decode fields   |         | Instruction page          | Feature   |
|-----------------|---------|---------------------------|-----------|
| 0100            | != 0x00 | DSB                       | -         |
| 0100            | 0000    | SSBB                      | -         |
| 0100            | 0100    | PSSBB                     | -         |
| 0101            | xxxx    | DMB                       | -         |
| 0110            | xxxx    | ISB                       | -         |
| 0111            | xxxx    | SB                        | FEAT_SB   |
| 1xxx            | xxxx    | CONSTRAINED UNPREDICTABLE | -         |

The behavior of the CONSTRAINED UNPREDICTABLE encodings in this table is described in CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings.

## F4.1.23.2 Preload (immediate)

This section describes the encoding of the Preload (immediate) instruction class. The encodings in this section are decoded from Memory hints and barriers.

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15 14 13 12 11   | 0     |
|------------------------------------------|---------------------|-------|
| 1 1 1 1 0 1 0 D U R 0 1                  | (1) (1) (1) (1)     | imm12 |

## Table F4-84

| Decode fields   | Decode fields   | Instruction page                                     |
|-----------------|-----------------|------------------------------------------------------|
| D               | R               | Rn                                                   |
| 0               | 0               | xxxx Reserved hint, behaves as NOP.                  |
| 0               | 1               | xxxx PLI (immediate, literal)                        |
| 1               | x               | 1111 PLD (literal)                                   |
| 1               | 0               | != 1111 PLD, PLDW(immediate) - Preload write variant |
| 1               | 1               | != 1111 PLD, PLDW(immediate) - Preload read variant  |

## F4.1.23.3 Preload (register)

This section describes the encoding of the Preload (register) instruction class. The encodings in this section are decoded from Memory hints and barriers.

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15 14 13 12 11   | 7 6 5 4 3   |
|------------------------------------------|---------------------|-------------|
| 1 1 1 1 0 1 1 D U o2 0 1                 | (1) (1) (1) (1)     | stype 0 Rm  |

## Table F4-85

| Decode fields   | Decode fields   |            | Instruction page                                                      |
|-----------------|-----------------|------------|-----------------------------------------------------------------------|
| D               | o2              | imm5:stype |                                                                       |
| 0               | 0               | xxxxxxx    | Reserved hint, behaves as NOP.                                        |
| 0               | 1               | != 0000011 | PLI (register) - Shift or rotate by value variant                     |
| 0               | 1               | 0000011    | PLI (register) - Rotate right with extend variant                     |
| 1               | 0               | != 0000011 | PLD, PLDW(register) - Preload write, optional shift or rotate variant |
| 1               | 0               | 0000011    | PLD, PLDW(register) - Preload write, rotate right with extend variant |
| 1               | 1               | != 0000011 | PLD, PLDW(register) - Preload read, optional shift or rotate variant  |
| 1               | 1               | 0000011    | PLD, PLDW(register) - Preload read, rotate right with extend variant  |

## F4.1.24 Advanced SIMD element or structure load/store

This section describes the encoding of the Advanced SIMD element or structure load/store group. The encodings in this section are decoded from Unconditional instructions.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the A32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

## Table F4-86 Encoding table for the Advanced SIMD element or structure load/store group

| Decode fields   | Decode fields   | Decode group or instruction page                      |
|-----------------|-----------------|-------------------------------------------------------|
| op0             | op1             | Decode group or instruction page                      |
| 0               | xx              | Advanced SIMD load/store multiple structures          |
| 1               | 11              | Advanced SIMD load single structure to all lanes      |
| 1               | != 11           | Advanced SIMD load/store single structure to one lane |

## F4.1.24.1 Advanced SIMD load/store multiple structures

This section describes the encoding of the Advanced SIMD load/store multiple structures instruction class. The encodings in this section are decoded from Advanced SIMD element or structure load/store.

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11   | 8 7 6 5 4 3   |
|------------------------------------------|---------|---------|---------------|
| 1 1 1 1 0 1 0 0 0 D L 0                  | Rn      | itype   | size align Rm |

## Table F4-87

| Decode fields   | Decode fields   |         | Instruction page                     |
|-----------------|-----------------|---------|--------------------------------------|
| L               | itype           | Rm      | Instruction page                     |
| 0               | 000x            | != 11x1 | VST4 (multiple 4-element structures) |
| 0               | 000x            | 1101    | VST4 (multiple 4-element structures) |
| 0               | 000x            | 1111    | VST4 (multiple 4-element structures) |
| 0               | 0010            | != 11x1 | VST1 (multiple single elements)      |
| 0               | 0010            | 1101    | VST1 (multiple single elements)      |
| 0               | 0010            | 1111    | VST1 (multiple single elements)      |
| 0               | 0011            | != 11x1 | VST2 (multiple 2-element structures) |
| 0               | 0011            | 1101    | VST2 (multiple 2-element structures) |
| 0               | 0011            | 1111    | VST2 (multiple 2-element structures) |
| 0               | 010x            | != 11x1 | VST3 (multiple 3-element structures) |
| 0               | 010x            | 1101    | VST3 (multiple 3-element structures) |
| 0               | 010x            | 1111    | VST3 (multiple 3-element structures) |
| 0               | 0110            | != 11x1 | VST1 (multiple single elements)      |
| 0               | 0110            | 1101    | VST1 (multiple single elements)      |
| 0               | 0110            | 1111    | VST1 (multiple single elements)      |
| 0               | 0111            | != 11x1 | VST1 (multiple single elements)      |
| 0               | 0111            | 1101    | VST1 (multiple single elements)      |
| 0               | 0111            | 1111    | VST1 (multiple single elements)      |
| 0               | 100x            | != 11x1 | VST2 (multiple 2-element structures) |
| 0               | 100x            | 1101    | VST2 (multiple 2-element structures) |
| 0               | 100x            | 1111    | VST2 (multiple 2-element structures) |
| 0               | 1010            | != 11x1 | VST1 (multiple single elements)      |
| 0               | 1010            | 1101    | VST1 (multiple single elements)      |
| 0               | 1010            | 1111    | VST1 (multiple single elements)      |
| 1               | 000x            | != 11x1 | VLD4 (multiple 4-element structures) |
| 1               | 000x            | 1101    | VLD4 (multiple 4-element structures) |
| 1               | 000x            | 1111    | VLD4 (multiple 4-element structures) |
| 1               | 0010            | != 11x1 | VLD1 (multiple single elements)      |
| 1               | 0010            | 1101    | VLD1 (multiple single elements)      |
| 1               | 0010            | 1111    | VLD1 (multiple single elements)      |

| Decode fields   | Decode fields   |         | Instruction page                     |
|-----------------|-----------------|---------|--------------------------------------|
| L               | itype           | Rm      |                                      |
| 1               | 0011            | != 11x1 | VLD2 (multiple 2-element structures) |
| 1               | 0011            | 1101    | VLD2 (multiple 2-element structures) |
| 1               | 0011            | 1111    | VLD2 (multiple 2-element structures) |
| 1               | 010x            | != 11x1 | VLD3 (multiple 3-element structures) |
| 1               | 010x            | 1101    | VLD3 (multiple 3-element structures) |
| 1               | 010x            | 1111    | VLD3 (multiple 3-element structures) |
| x               | 1011            | xxxx    | Unallocated.                         |
| 1               | 0110            | != 11x1 | VLD1 (multiple single elements)      |
| 1               | 0110            | 1101    | VLD1 (multiple single elements)      |
| 1               | 0110            | 1111    | VLD1 (multiple single elements)      |
| 1               | 0111            | != 11x1 | VLD1 (multiple single elements)      |
| 1               | 0111            | 1101    | VLD1 (multiple single elements)      |
| 1               | 0111            | 1111    | VLD1 (multiple single elements)      |
| x               | 11xx            | xxxx    | Unallocated.                         |
| 1               | 100x            | != 11x1 | VLD2 (multiple 2-element structures) |
| 1               | 100x            | 1101    | VLD2 (multiple 2-element structures) |
| 1               | 100x            | 1111    | VLD2 (multiple 2-element structures) |
| 1               | 1010            | != 11x1 | VLD1 (multiple single elements)      |
| 1               | 1010            | 1101    | VLD1 (multiple single elements)      |
| 1               | 1010            | 1111    | VLD1 (multiple single elements)      |

## F4.1.24.2 Advanced SIMD load single structure to all lanes

This section describes the encoding of the Advanced SIMD load single structure to all lanes instruction class. The encodings in this section are decoded from Advanced SIMD element or structure load/store.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15   | 12 11 10 9 8 7 6 5 4 3   |
|------------------------------------------|---------|--------------------------|
| 1 1 1 1 0 1 0 0 1 D L 0                  | Rn      | 1 1 N size T a Rm        |

## Table F4-88

| Decode fields   | Decode fields   | Instruction page   | Instruction page   | Instruction page                   |
|-----------------|-----------------|--------------------|--------------------|------------------------------------|
| L               | N               | a                  | Rm                 |                                    |
| 0               | xx              | x                  | xxxx               | Unallocated.                       |
| 1               | 00              | x                  | != 11x1            | VLD1 (single element to all lanes) |
| 1               | 00              | x                  | 1101               | VLD1 (single element to all lanes) |

| Decode fields   | Decode fields   |    |         | Instruction page                               |
|-----------------|-----------------|----|---------|------------------------------------------------|
| L               | N               | a  | Rm      |                                                |
| 1               | 00              | x  | 1111    | VLD1 (single element to all lanes)             |
| 1               | 01              | x  | != 11x1 | VLD2 (single 2-element structure to all lanes) |
| 1               | 01              | x  | 1101    | VLD2 (single 2-element structure to all lanes) |
| 1               | 01              | x  | 1111    | VLD2 (single 2-element structure to all lanes) |
| 1               | 10              | 0  | != 11x1 | VLD3 (single 3-element structure to all lanes) |
| 1               | 10              | 0  | 1101    | VLD3 (single 3-element structure to all lanes) |
| 1               | 10              | 0  | 1111    | VLD3 (single 3-element structure to all lanes) |
| 1               | 10              | 1  | xxxx    | Unallocated.                                   |
| 1               | 11              | x  | != 11x1 | VLD4 (single 4-element structure to all lanes) |
| 1               | 11              | x  | 1101    | VLD4 (single 4-element structure to all lanes) |
| 1               | 11              | x  | 1111    | VLD4 (single 4-element structure to all lanes) |

## F4.1.24.3 Advanced SIMD load/store single structure to one lane

This section describes the encoding of the Advanced SIMD load/store single structure to one lane instruction class. The encodings in this section are decoded from Advanced SIMD element or structure load/store.

<!-- image -->

| 31 30 29 28 27 26 25 24 23 22 21 20 19   | 16 15                | 12 11 10 9   | 8   | 7 4         | 0   |
|------------------------------------------|----------------------|--------------|-----|-------------|-----|
| 1 1 1                                    | 1 0 1 0 0 1 D L 0 Rn | !=11         | N   | index_align | Rm  |

## Table F4-89

| Decode fields   | Decode fields   |    |         |                                                 |
|-----------------|-----------------|----|---------|-------------------------------------------------|
| L               | size            | N  | Rm      |                                                 |
| 0               | 00              | 00 | != 11x1 | VST1 (single element from one lane)             |
| 0               | 00              | 00 | 1101    | VST1 (single element from one lane)             |
| 0               | 00              | 00 | 1111    | VST1 (single element from one lane)             |
| 0               | 00              | 01 | != 11x1 | VST2 (single 2-element structure from one lane) |
| 0               | 00              | 01 | 1101    | VST2 (single 2-element structure from one lane) |
| 0               | 00              | 01 | 1111    | VST2 (single 2-element structure from one lane) |
| 0               | 00              | 10 | != 11x1 | VST3 (single 3-element structure from one lane) |
| 0               | 00              | 10 | 1101    | VST3 (single 3-element structure from one lane) |
| 0               | 00              | 10 | 1111    | VST3 (single 3-element structure from one lane) |
| 0               | 00              | 11 | != 11x1 | VST4 (single 4-element structure from one lane) |
| 0               | 00              | 11 | 1101    | VST4 (single 4-element structure from one lane) |
| 0               | 00              | 11 | 1111    | VST4 (single 4-element structure from one lane) |

size

| Decode fields   | Decode fields   |    |         | Instruction page                                |
|-----------------|-----------------|----|---------|-------------------------------------------------|
| L               | size            | N  | Rm      |                                                 |
| 0               | 01              | 00 | != 11x1 | VST1 (single element from one lane)             |
| 0               | 01              | 00 | 1101    | VST1 (single element from one lane)             |
| 0               | 01              | 00 | 1111    | VST1 (single element from one lane)             |
| 0               | 01              | 01 | != 11x1 | VST2 (single 2-element structure from one lane) |
| 0               | 01              | 01 | 1101    | VST2 (single 2-element structure from one lane) |
| 0               | 01              | 01 | 1111    | VST2 (single 2-element structure from one lane) |
| 0               | 01              | 10 | != 11x1 | VST3 (single 3-element structure from one lane) |
| 0               | 01              | 10 | 1101    | VST3 (single 3-element structure from one lane) |
| 0               | 01              | 10 | 1111    | VST3 (single 3-element structure from one lane) |
| 0               | 01              | 11 | != 11x1 | VST4 (single 4-element structure from one lane) |
| 0               | 01              | 11 | 1101    | VST4 (single 4-element structure from one lane) |
| 0               | 01              | 11 | 1111    | VST4 (single 4-element structure from one lane) |
| 0               | 10              | 00 | != 11x1 | VST1 (single element from one lane)             |
| 0               | 10              | 00 | 1101    | VST1 (single element from one lane)             |
| 0               | 10              | 00 | 1111    | VST1 (single element from one lane)             |
| 0               | 10              | 01 | != 11x1 | VST2 (single 2-element structure from one lane) |
| 0               | 10              | 01 | 1101    | VST2 (single 2-element structure from one lane) |
| 0               | 10              | 01 | 1111    | VST2 (single 2-element structure from one lane) |
| 0               | 10              | 10 | != 11x1 | VST3 (single 3-element structure from one lane) |
| 0               | 10              | 10 | 1101    | VST3 (single 3-element structure from one lane) |
| 0               | 10              | 10 | 1111    | VST3 (single 3-element structure from one lane) |
| 0               | 10              | 11 | != 11x1 | VST4 (single 4-element structure from one lane) |
| 0               | 10              | 11 | 1101    | VST4 (single 4-element structure from one lane) |
| 0               | 10              | 11 | 1111    | VST4 (single 4-element structure from one lane) |
| 1               | 00              | 00 | != 11x1 | VLD1 (single element to one lane)               |
| 1               | 00              | 00 | 1101    | VLD1 (single element to one lane)               |
| 1               | 00              | 00 | 1111    | VLD1 (single element to one lane)               |
| 1               | 00              | 01 | != 11x1 | VLD2 (single 2-element structure to one lane)   |
| 1               | 00              | 01 | 1101    | VLD2 (single 2-element structure to one lane)   |
| 1               | 00              | 01 | 1111    | VLD2 (single 2-element structure to one lane)   |
| 1               | 00              | 10 | != 11x1 | VLD3 (single 3-element structure to one lane)   |
| 1               | 00              | 10 | 1101    | VLD3 (single 3-element structure to one lane)   |
| 1               | 00              | 10 | 1111    | VLD3 (single 3-element structure to one lane)   |
| 1               | 00              | 11 | != 11x1 | VLD4 (single 4-element structure to one lane)   |
| 1               | 00              | 11 | 1101    | VLD4 (single 4-element structure to one lane)   |
| 1               | 00              | 11 | 1111    | VLD4 (single 4-element structure to one lane)   |
| 1               | 01              | 00 | != 11x1 | VLD1 (single element to one lane)               |
| 1               | 01              | 00 | 1101    | VLD1 (single element to one lane)               |
| 1               | 01              | 00 | 1111    | VLD1 (single element to one lane)               |

| Decode fields   | Decode fields   |    |         | Instruction page                              |
|-----------------|-----------------|----|---------|-----------------------------------------------|
| L               | size            | N  | Rm      |                                               |
| 1               | 01              | 01 | != 11x1 | VLD2 (single 2-element structure to one lane) |
| 1               | 01              | 01 | 1101    | VLD2 (single 2-element structure to one lane) |
| 1               | 01              | 01 | 1111    | VLD2 (single 2-element structure to one lane) |
| 1               | 01              | 10 | != 11x1 | VLD3 (single 3-element structure to one lane) |
| 1               | 01              | 10 | 1101    | VLD3 (single 3-element structure to one lane) |
| 1               | 01              | 10 | 1111    | VLD3 (single 3-element structure to one lane) |
| 1               | 01              | 11 | != 11x1 | VLD4 (single 4-element structure to one lane) |
| 1               | 01              | 11 | 1101    | VLD4 (single 4-element structure to one lane) |
| 1               | 01              | 11 | 1111    | VLD4 (single 4-element structure to one lane) |
| 1               | 10              | 00 | != 11x1 | VLD1 (single element to one lane)             |
| 1               | 10              | 00 | 1101    | VLD1 (single element to one lane)             |
| 1               | 10              | 00 | 1111    | VLD1 (single element to one lane)             |
| 1               | 10              | 01 | != 11x1 | VLD2 (single 2-element structure to one lane) |
| 1               | 10              | 01 | 1101    | VLD2 (single 2-element structure to one lane) |
| 1               | 10              | 01 | 1111    | VLD2 (single 2-element structure to one lane) |
| 1               | 10              | 10 | != 11x1 | VLD3 (single 3-element structure to one lane) |
| 1               | 10              | 10 | 1101    | VLD3 (single 3-element structure to one lane) |
| 1               | 10              | 10 | 1111    | VLD3 (single 3-element structure to one lane) |
| 1               | 10              | 11 | != 11x1 | VLD4 (single 4-element structure to one lane) |
| 1               | 10              | 11 | 1101    | VLD4 (single 4-element structure to one lane) |
| 1               | 10              | 11 | 1111    | VLD4 (single 4-element structure to one lane) |