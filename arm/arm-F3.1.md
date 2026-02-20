## F3.1 T32 instruction set encoding

The T32 instruction stream is a sequence of halfword-aligned halfwords. Each T32 instruction is either a single 16-bit halfword in that stream, or a 32-bit instruction consisting of two consecutive halfwords in that stream.

If the value of bits[15:11] of the halfword being decoded is one of the following, the halfword is the first halfword of a 32-bit instruction:

- 0b11101 .
- 0b11110 .
- 0b11111 .

Otherwise, the halfword is a 16-bit instruction.

The T32 instruction encoding is:

<!-- image -->

Table F3-1 Main encoding table for the T32 instruction set

| Decode fields   | Decode group or instruction page   |
|-----------------|------------------------------------|
| != 111          | 16-bit                             |
| 111             | B- T2 variant                      |
| 111             | 32-bit                             |

## F3.1.1 16-bit

This section describes the encoding of the 16-bit group. The encodings in this section are decoded from T32 instruction set encoding.

<!-- image -->

This decode also imposes the constraint:

- op0&lt;5:3&gt; != 111 .

| Decode fields   | Decode group or instruction page                    |
|-----------------|-----------------------------------------------------|
| op0             |                                                     |
| 00xxxx          | Shift (immediate), add, subtract, move, and compare |
| 010000          | Data-processing (two low registers)                 |
| 010001          | Special data instructions and branch and exchange   |
| 01001x          | LDR(literal) - T1 variant                           |
| 0101xx          | Load/store (register offset)                        |
| 011xxx          | Load/store word/byte (immediate offset)             |
| 1000xx          | Load/store halfword (immediate offset)              |
| 1001xx          | Load/store (SP-relative)                            |
| 1010xx          | Add PC/SP (immediate)                               |
| 1011xx          | Miscellaneous 16-bit instructions                   |
| 1100xx          | Load/store multiple                                 |
| 1101xx          | Conditional branch, and Supervisor Call             |

## F3.1.1.1 Data-processing (two low registers)

This section describes the encoding of the Data-processing (two low registers) instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

| 15 14 13 12 11 10 9   | 15 14 13 12 11 10 9   | 6 5 3   | 2 0   |
|-----------------------|-----------------------|---------|-------|
| 0 1 0 0 0 0           | op                    | Rs      | Rd    |

## Table F3-3

|   Decode fields | Instruction page                                                      |
|-----------------|-----------------------------------------------------------------------|
|            0000 | AND, ANDS(register)                                                   |
|            0001 | EOR, EORS (register)                                                  |
|            0010 | MOV, MOVS(register-shifted register) - Logical shift left variant     |
|            0011 | MOV, MOVS(register-shifted register) - Logical shift right variant    |
|            0100 | MOV, MOVS(register-shifted register) - Arithmetic shift right variant |
|            0101 | ADC, ADCS(register)                                                   |
|            0110 | SBC, SBCS (register)                                                  |
|            0111 | MOV, MOVS(register-shifted register) - Rotate right variant           |
|            1000 | TST (register)                                                        |
|            1001 | RSB, RSBS (immediate)                                                 |

|   Decode fields | Instruction page     |
|-----------------|----------------------|
|            1010 | CMP(register)        |
|            1011 | CMN(register)        |
|            1100 | ORR, ORRS (register) |
|            1101 | MUL,MULS             |
|            1110 | BIC, BICS (register) |
|            1111 | MVN, MVNS(register)  |

## F3.1.1.2 Load/store (register offset)

This section describes the encoding of the Load/store (register offset) instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

## Table F3-4

| Decode fields   | Instruction page   |     |                  |
|-----------------|--------------------|-----|------------------|
| L 0             | B 0                | H 0 | STR (register)   |
| 0               | 0                  | 1   | STRH (register)  |
| 0               | 1                  | 0   | STRB (register)  |
| 0               | 1                  | 1   | LDRSB (register) |
| 1               | 0                  | 0   | LDR(register)    |
| 1               | 0                  | 1   | LDRH(register)   |
| 1               | 1                  | 0   | LDRB(register)   |
| 1               | 1                  | 1   | LDRSH (register) |

## F3.1.1.3 Load/store word/byte (immediate offset)

This section describes the encoding of the Load/store word/byte (immediate offset) instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

## Table F3-5

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| B               | L                  |
| 0               | 0 STR (immediate)  |
| 0               | 1 LDR(immediate)   |
| 1               | 0 STRB (immediate) |
| 1               | 1 LDRB(immediate)  |

## F3.1.1.4 Load/store halfword (immediate offset)

This section describes the encoding of the Load/store halfword (immediate offset) instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

| 15 14 13 12 11 10   | 15 14 13 12 11 10   | 6 5 3 2 0   | 6 5 3 2 0   |
|---------------------|---------------------|-------------|-------------|
| 1 0 0 0             | imm5                | Rn          | Rt          |

## Table F3-6

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STRH (immediate)   |
| 1               | LDRH(immediate)    |

## F3.1.1.5 Load/store (SP-relative)

This section describes the encoding of the Load/store (SP-relative) instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

## Table F3-7

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STR (immediate)    |
| 1               | LDR(immediate)     |

## F3.1.1.6 Add PC/SP (immediate)

This section describes the encoding of the Add PC/SP (immediate) instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

## Table F3-8

| Decode fields   | Instruction page             |
|-----------------|------------------------------|
| SP              |                              |
| 0               | ADR                          |
| 1               | ADD, ADDS(SP plus immediate) |

## F3.1.1.7 Load/store multiple

This section describes the encoding of the Load/store multiple instruction class. The encodings in this section are decoded from 16-bit.

<!-- image -->

## Table F3-9

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STM, STMIA,STMEA   |
| 1               | LDM, LDMIA,LDMFD   |

## F3.1.2 Shift (immediate), add, subtract, move, and compare

This section describes the encoding of the Shift (immediate), add, subtract, move, and compare group. The encodings in this section are decoded from 16-bit.

<!-- image -->

Table F3-10 Encoding table for the Shift (immediate), add, subtract, move, and compare group

| Decode fields   | Decode fields   | Decode group   | or instruction page                                           |
|-----------------|-----------------|----------------|---------------------------------------------------------------|
| op0             | op1             | op2            | or instruction page                                           |
| 0               | 11              | 0              | Add, subtract (three low registers)                           |
| 0               | 11              | 1              | Add, subtract (two low registers and immediate)               |
| 0               | != 11           | x              | MOV, MOVS(register) - T2 variant                              |
| 1               | xx              | x              | Add, subtract, compare, move (one low register and immediate) |

## F3.1.2.1 Add, subtract (three low registers)

This section describes the encoding of the Add, subtract (three low registers) instruction class. The encodings in this section are decoded from Shift (immediate), add, subtract, move, and compare.

<!-- image -->

## Table F3-11

| Decode fields   | Instruction page     |
|-----------------|----------------------|
| S               |                      |
| 0               | ADD, ADDS(register)  |
| 1               | SUB, SUBS (register) |

## F3.1.2.2 Add, subtract (two low registers and immediate)

This section describes the encoding of the Add, subtract (two low registers and immediate) instruction class. The encodings in this section are decoded from Shift (immediate), add, subtract, move, and compare.

<!-- image -->

| 15 14 13 12 11 10 9   | 8    | 6 5 3 2   |
|-----------------------|------|-----------|
| 0 0 0 1 1 1 S         | imm3 | Rn Rd     |

## Table F3-12

| Decode fields   | Instruction page      |
|-----------------|-----------------------|
| S               |                       |
| 0               | ADD, ADDS(immediate)  |
| 1               | SUB, SUBS (immediate) |

## F3.1.2.3 Add, subtract, compare, move (one low register and immediate)

This section describes the encoding of the Add, subtract, compare, move (one low register and immediate) instruction class. The encodings in this section are decoded from Shift (immediate), add, subtract, move, and compare.

<!-- image -->

| 15 14 13 12 11 10 8   | 15 14 13 12 11 10 8   | 15 14 13 12 11 10 8   | 7    |
|-----------------------|-----------------------|-----------------------|------|
| 0 0 1                 | op                    | Rd                    | imm8 |

## Table F3-13

| Decode fields   | Instruction page      |
|-----------------|-----------------------|
| op              |                       |
| 00              | MOV, MOVS(immediate)  |
| 01              | CMP(immediate)        |
| 10              | ADD, ADDS(immediate)  |
| 11              | SUB, SUBS (immediate) |

## F3.1.3 Special data instructions and branch and exchange

This section describes the encoding of the Special data instructions and branch and exchange group. The encodings in this section are decoded from 16-bit.

<!-- image -->

|     15 | 10 9 8   |
|--------|----------|
| 010001 | op0      |

Table F3-14 Encoding table for the Special data instructions and branch and exchange group

| Decode fields   | Decode group or instruction page                  |
|-----------------|---------------------------------------------------|
| op0             |                                                   |
| 11              | Branch and exchange                               |
| != 11           | Add, subtract, compare, move (two high registers) |

## F3.1.3.1 Branch and exchange

This section describes the encoding of the Branch and exchange instruction class. The encodings in this section are decoded from Special data instructions and branch and exchange.

<!-- image -->

## Table F3-15

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | BX                 |
| 1               | BLX(register)      |

## F3.1.3.2 Add, subtract, compare, move (two high registers)

This section describes the encoding of the Add, subtract, compare, move (two high registers) instruction class. The encodings in this section are decoded from Special data instructions and branch and exchange.

<!-- image -->

## Table F3-16

| Decode fields   | Decode fields   | Instruction page                         |
|-----------------|-----------------|------------------------------------------|
| op              | D:Rd            | Rs                                       |
| 00              | != 1101         | != 1101 ADD, ADDS(register)              |
| 00              | xxxx            | 1101 ADD, ADDS(SP plus register) - T1    |
| 00              | 1101            | != 1101 ADD, ADDS(SP plus register) - T2 |
| 01              | xxxx            | xxxx CMP(register)                       |
| 10              | xxxx            | xxxx MOV, MOVS(register)                 |

## F3.1.4 Miscellaneous 16-bit instructions

This section describes the encoding of the Miscellaneous 16-bit instructions group. The encodings in this section are decoded from 16-bit.

<!-- image -->

Table F3-17 Encoding table for the Miscellaneous 16-bit instructions group

| Decode fields   | Decode fields   |     |         | Decode group or instruction page   | Feature   |
|-----------------|-----------------|-----|---------|------------------------------------|-----------|
| op0             | op1             | op2 | op3     |                                    | Feature   |
| 0000            | xx              | x   | xxxx    | Adjust SP (immediate)              | -         |
| 0010            | xx              | x   | xxxx    | Extend                             | -         |
| 0110            | 00              | 0   | xxxx    | SETPAN                             | FEAT_PAN  |
| 0110            | 00              | 1   | xxxx    | Unallocated.                       | -         |
| 0110            | 01              | x   | xxxx    | Change Processor State             | -         |
| 0110            | 1x              | x   | xxxx    | Unallocated.                       | -         |
| 0111            | xx              | x   | xxxx    | Unallocated.                       | -         |
| 1000            | xx              | x   | xxxx    | Unallocated.                       | -         |
| 1010            | 10              | x   | xxxx    | HLT                                | -         |
| 1010            | != 10           | x   | xxxx    | Reverse bytes                      | -         |
| 1110            | xx              | x   | xxxx    | BKPT                               | -         |
| 1111            | xx              | x   | 0000    | Hints                              | -         |
| 1111            | xx              | x   | != 0000 | IT                                 | -         |

| Decode fields   | Decode fields   |     |      | Decode group or instruction page   | Feature   |
|-----------------|-----------------|-----|------|------------------------------------|-----------|
| op0             | op1             | op2 | op3  |                                    |           |
| x0x1            | xx              | x   | xxxx | CBNZ, CBZ                          | -         |
| x10x            | xx              | x   | xxxx | Push and Pop                       | -         |

## F3.1.4.1 Adjust SP (immediate)

This section describes the encoding of the Adjust SP (immediate) instruction class. The encodings in this section are decoded from Miscellaneous 16-bit instructions.

<!-- image -->

## Table F3-18

| Decode fields   | Instruction page               |
|-----------------|--------------------------------|
| S               |                                |
| 0               | ADD, ADDS(SP plus immediate)   |
| 1               | SUB, SUBS (SP minus immediate) |

## F3.1.4.2 Extend

This section describes the encoding of the Extend instruction class. The encodings in this section are decoded from Miscellaneous 16-bit instructions.

<!-- image -->

## Table F3-19

|   Decode fields U | Instruction page   |
|-------------------|--------------------|
|                 0 | SXTH               |
|                 0 | SXTB               |
|                 1 | UXTH               |
|                 1 | UXTB               |

## F3.1.4.3 Change Processor State

This section describes the encoding of the Change Processor State instruction class. The encodings in this section are decoded from Miscellaneous 16-bit instructions.

<!-- image -->

## Table F3-20

| Decode fields   |       | Instruction page                              |
|-----------------|-------|-----------------------------------------------|
| op              | flags |                                               |
| 0               | xxxxx | SETEND                                        |
| 1               | 0xxxx | CPS, CPSID, CPSIE - Interrupt enable variant  |
| 1               | 1xxxx | CPS, CPSID, CPSIE - Interrupt disable variant |

## F3.1.4.4 Reverse bytes

This section describes the encoding of the Reverse bytes instruction class. The encodings in this section are decoded from Miscellaneous 16-bit instructions.

<!-- image -->

## Table F3-21

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| op              |                    |
| 00              | REV                |
| 01              | REV16              |
| 11              | REVSH              |

## F3.1.4.5 Hints

This section describes the encoding of the Hints instruction class. The encodings in this section are decoded from Miscellaneous 16-bit instructions.

<!-- image -->

| 15 14 13 12 11 10 9 8   | 4 3 2 1 0    |
|-------------------------|--------------|
| 1 0 1 1 1 1 1 1         | hint 0 0 0 0 |

## Table F3-22

| Decode fields   | Instruction page               |
|-----------------|--------------------------------|
| 0000            | NOP                            |
| 0001            | YIELD                          |
| 0010            | WFE                            |
| 0011            | WFI                            |
| 0100            | SEV                            |
| 0101            | SEVL                           |
| 011x            | Reserved hint, behaves as NOP. |
| 1xxx            | Reserved hint, behaves as NOP. |

## F3.1.4.6 Push and Pop

This section describes the encoding of the Push and Pop instruction class. The encodings in this section are decoded from Miscellaneous 16-bit instructions.

<!-- image -->

|   L |      |
|-----|------|
|   0 | PUSH |
|   1 | POP  |

## F3.1.5 Conditional branch, and Supervisor Call

This section describes the encoding of the Conditional branch, and Supervisor Call group. The encodings in this section are decoded from 16-bit.

<!-- image -->

|   15 | 12 11   |
|------|---------|
| 1101 | op0     |

Table F3-24 Encoding table for the Conditional branch, and Supervisor Call group

| Decode fields   | Decode group or instruction page   |
|-----------------|------------------------------------|
| op0             |                                    |
| 111x            | Exception generation               |
| != 111x         | B- T1 variant                      |

## F3.1.5.1 Exception generation

This section describes the encoding of the Exception generation instruction class. The encodings in this section are decoded from Conditional branch, and Supervisor Call.

<!-- image -->

| 15 14 13 12 11 10 9 8   | 0    |
|-------------------------|------|
| 1 1 0 1 1 1 1 S         | imm8 |

## Table F3-25

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| S               |                    |
| 0               | UDF                |
| 1               | SVC                |

## F3.1.6 32-bit

This section describes the encoding of the 32-bit group. The encodings in this section are decoded from T32 instruction set encoding.

<!-- image -->

This decode also imposes the constraint:

- op0&lt;3:2&gt; != 00 .

## Table F3-26 Encoding table for the 32-bit group

| Decode fields   | Decode fields   |     | Decode group or instruction page                                                    |
|-----------------|-----------------|-----|-------------------------------------------------------------------------------------|
| op0             | op1             | op3 | Decode group or instruction page                                                    |
| x11x            | xxxxx           | x   | System register access, Advanced SIMD, and floating-point                           |
| 0100            | xx0xx           | x   | Load/store multiple                                                                 |
| 0100            | xx1xx           | x   | Load/store dual, load/store exclusive, load-acquire/store-release, and table branch |
| 0101            | xxxxx           | x   | Data-processing (shifted register)                                                  |
| 10xx            | xxxxx           | 1   | Branches and miscellaneous control                                                  |
| 10x0            | xxxxx           | 0   | Data-processing (modified immediate)                                                |
| 10x1            | xxxx0           | 0   | Data-processing (plain binary immediate)                                            |
| 10x1            | xxxx1           | 0   | Unallocated.                                                                        |
| 1100            | 1xxx0           | x   | Advanced SIMD element or structure load/store                                       |
| 1100            | != 1xxx0        | x   | Load/store single                                                                   |
| 1101            | 0xxxx           | x   | Data-processing (register)                                                          |
| 1101            | 10xxx           | x   | Multiply, multiply accumulate, and absolute difference                              |
| 1101            | 11xxx           | x   | Long multiply and divide                                                            |

## F3.1.6.1 Load/store multiple

This section describes the encoding of the Load/store multiple instruction class. The encodings in this section are decoded from 32-bit.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15 14 13   | 0             |
|---------------------------------|--------------|---------------|
| 1 1 1 0 1 0 0 opc 0 W L         | P M          | register_list |

## Table F3-27

| Decode fields   | Instruction page   |                                      |
|-----------------|--------------------|--------------------------------------|
| opc             | L                  |                                      |
| 00              | 0                  | SRS, SRSDA, SRSDB, SRSIA, SRSIB - T1 |
| 00              | 1                  | RFE, RFEDA, RFEDB, RFEIA, RFEIB - T1 |
| 01              | 0                  | STM, STMIA,STMEA                     |
| 01              | 1                  | LDM, LDMIA,LDMFD                     |

| Decode fields   |    | Instruction page                     |
|-----------------|----|--------------------------------------|
| opc             | L  |                                      |
| 10              | 0  | STMDB,STMFD                          |
| 10              | 1  | LDMDB,LDMEA                          |
| 11              | 0  | SRS, SRSDA, SRSDB, SRSIA, SRSIB - T2 |
| 11              | 1  | RFE, RFEDA, RFEDB, RFEIA, RFEIB - T2 |

## F3.1.6.2 Data-processing (shifted register)

This section describes the encoding of the Data-processing (shifted register) instruction class. The encodings in this section are decoded from 32-bit.

| 15 14 13 12 11 10 9 8   | 5 4   | 3   | 0 15 14   | 12 11   | 8   | 7 6 5 4 3   | 0   |
|-------------------------|-------|-----|-----------|---------|-----|-------------|-----|
| 1 1 1 0 1 0 1           | op1   | S   | (0)       | imm3    | Rd  | imm2 stype  | Rm  |

## Table F3-28

| Decode fields   | Decode fields   |         |                 |         | Instruction page                                              |
|-----------------|-----------------|---------|-----------------|---------|---------------------------------------------------------------|
| op1             | S               | Rn      | imm3:imm2:stype | Rd      |                                                               |
| 0000            | 0               | xxxx    | != 0000011      | xxxx    | AND, ANDS(register) - AND, shift or rotate by value variant   |
| 0000            | 0               | xxxx    | 0000011         | xxxx    | AND, ANDS(register) - AND, rotate right with extend variant   |
| 0000            | 1               | xxxx    | != 0000011      | != 1111 | AND, ANDS(register) - ANDS, shift or rotate by value variant  |
| 0000            | 1               | xxxx    | != 0000011      | 1111    | TST (register) - Shift or rotate by value variant             |
| 0000            | 1               | xxxx    | 0000011         | != 1111 | AND, ANDS(register) - ANDS, rotate right with extend variant  |
| 0000            | 1               | xxxx    | 0000011         | 1111    | TST (register) - Rotate right with extend variant             |
| 0001            | x               | xxxx    | != 0000011      | xxxx    | BIC, BICS (register) - BICS, shift or rotate by value variant |
| 0001            | x               | xxxx    | 0000011         | xxxx    | BIC, BICS (register) - BICS, rotate right with extend variant |
| 0010            | 0               | != 1111 | != 0000011      | xxxx    | ORR, ORRS (register) - ORR, shift or rotate by value variant  |
| 0010            | 0               | != 1111 | 0000011         | xxxx    | ORR, ORRS (register) - ORR, rotate right with extend variant  |
| 0010            | 0               | 1111    | != 0000011      | xxxx    | MOV, MOVS(register) - MOV, shift or rotate by value variant   |
| 0010            | 0               | 1111    | 0000011         | xxxx    | MOV, MOVS(register) - MOV, rotate right with extend variant   |
| 0010            | 1               | != 1111 | != 0000011      | xxxx    | ORR, ORRS (register) - ORRS, shift or rotate by value variant |
| 0010            | 1               | != 1111 | 0000011         | xxxx    | ORR, ORRS (register) - ORRS, rotate right with extend variant |
| 0010            | 1               | 1111    | != 0000011      | xxxx    | MOV, MOVS(register) - MOVS, shift or rotate by value variant  |
| 0010            | 1               | 1111    | 0000011         | xxxx    | MOV, MOVS(register) - MOVS, rotate right with extend variant  |
| 0011            | 0               | != 1111 | != 0000011      | xxxx    | ORN, ORNS(register) - ORN, shift or rotate by value variant   |
| 0011            | 0               | != 1111 | 0000011         | xxxx    | ORN, ORNS(register) - ORN, rotate right with extend variant   |
| 0011            | 0               | 1111    | != 0000011      | xxxx    | MVN, MVNS(register) - MVN, shift or rotate by value variant   |

| Decode fields   | Decode fields   |         |                 |         | Instruction page                                                      |
|-----------------|-----------------|---------|-----------------|---------|-----------------------------------------------------------------------|
| op1             | S               | Rn      | imm3:imm2:stype | Rd      |                                                                       |
| 0011            | 0               | 1111    | 0000011         | xxxx    | MVN, MVNS(register) - MVN, rotate right with extend variant           |
| 0011            | 1               | != 1111 | != 0000011      | xxxx    | ORN, ORNS(register) - ORNS, shift or rotate by value variant          |
| 0011            | 1               | != 1111 | 0000011         | xxxx    | ORN, ORNS(register) - ORNS, rotate right with extend variant          |
| 0011            | 1               | 1111    | != 0000011      | xxxx    | MVN, MVNS(register) - MVNS, shift or rotate by value variant          |
| 0011            | 1               | 1111    | 0000011         | xxxx    | MVN, MVNS(register) - MVNS, rotate right with extend variant          |
| 0100            | 0               | xxxx    | != 0000011      | xxxx    | EOR, EORS (register) - EOR, shift or rotate by value variant          |
| 0100            | 0               | xxxx    | 0000011         | xxxx    | EOR, EORS (register) - EOR, rotate right with extend variant          |
| 0100            | 1               | xxxx    | != 0000011      | != 1111 | EOR, EORS (register) - EORS, shift or rotate by value variant         |
| 0100            | 1               | xxxx    | != 0000011      | 1111    | TEQ (register) - Shift or rotate by value variant                     |
| 0100            | 1               | xxxx    | 0000011         | != 1111 | EOR, EORS (register) - EORS, rotate right with extend variant         |
| 0100            | 1               | xxxx    | 0000011         | 1111    | TEQ (register) - Rotate right with extend variant                     |
| 0101            | x               | xxxx    | xxxxxxx         | xxxx    | Unallocated.                                                          |
| 0110            | 0               | xxxx    | xxxxx00         | xxxx    | PKHBT, PKHTB - PKHBT variant                                          |
| 0110            | 0               | xxxx    | xxxxx01         | xxxx    | Unallocated.                                                          |
| 0110            | 0               | xxxx    | xxxxx10         | xxxx    | PKHBT, PKHTB - PKHTB variant                                          |
| 0110            | 0               | xxxx    | xxxxx11         | xxxx    | Unallocated.                                                          |
| 0111            | x               | xxxx    | xxxxxxx         | xxxx    | Unallocated.                                                          |
| 1000            | 0               | != 1101 | != 0000011      | xxxx    | ADD, ADDS(register) - ADD, shift or rotate by value variant           |
| 1000            | 0               | != 1101 | 0000011         | xxxx    | ADD, ADDS(register) - ADD, rotate right with extend variant           |
| 1000            | 0               | 1101    | != 0000011      | xxxx    | ADD, ADDS(SP plus register) - ADD, shift or rotate by value variant   |
| 1000            | 0               | 1101    | 0000011         | xxxx    | ADD, ADDS(SP plus register) - ADD, rotate right with extend variant   |
| 1000            | 1               | xxxx    | != 0000011      | 1111    | CMN(register) - Shift or rotate by value variant                      |
| 1000            | 1               | != 1101 | != 0000011      | != 1111 | ADD, ADDS(register) - ADDS, shift or rotate by value variant          |
| 1000            | 1               | != 1101 | 0000011         | != 1111 | ADD, ADDS(register) - ADDS, rotate right with extend variant          |
| 1000            | 1               | xxxx    | 0000011         | 1111    | CMN(register) - Rotate right with extend variant                      |
| 1000            | 1               | 1101    | != 0000011      | != 1111 | ADD, ADDS(SP plus register) - ADDS, shift or rotate by value variant  |
| 1000            | 1               | 1101    | 0000011         | != 1111 | ADD, ADDS(SP plus register) - ADDS, rotate right with extend variant  |
| 1001            | x               | xxxx    | xxxxxxx         | xxxx    | Unallocated.                                                          |
| 1010            | x               | xxxx    | != 0000011      | xxxx    | ADC, ADCS(register) - ADCS, shift or rotate by value variant          |
| 1010            | x               | xxxx    | 0000011         | xxxx    | ADC, ADCS(register) - ADCS, rotate right with extend variant          |
| 1011            | x               | xxxx    | != 0000011      | xxxx    | SBC, SBCS (register) - SBCS, shift or rotate by value variant         |
| 1011            | x               | xxxx    | 0000011         | xxxx    | SBC, SBCS (register) - SBCS, rotate right with extend variant         |
| 1100            | x               | xxxx    | xxxxxxx         | xxxx    | Unallocated.                                                          |
| 1101            | 0               | != 1101 | != 0000011      | xxxx    | SUB, SUBS (register) - SUB, shift or rotate by value variant          |
| 1101            | 0               | != 1101 | 0000011         | xxxx    | SUB, SUBS (register) - SUB, rotate right with extend variant          |
| 1101            | 0               | 1101    | != 0000011      | xxxx    | SUB, SUBS (SP minus register) - SUB, shift or rotate by value variant |

| Decode fields   | Decode fields   |         |                 |         | Instruction page                                                       |
|-----------------|-----------------|---------|-----------------|---------|------------------------------------------------------------------------|
| op1             | S               | Rn      | imm3:imm2:stype | Rd      |                                                                        |
| 1101            | 0               | 1101    | 0000011         | xxxx    | SUB, SUBS (SP minus register) - SUB, rotate right with extend variant  |
| 1101            | 1               | xxxx    | != 0000011      | 1111    | CMP(register) - Shift or rotate by value variant                       |
| 1101            | 1               | != 1101 | != 0000011      | != 1111 | SUB, SUBS (register) - SUBS, shift or rotate by value variant          |
| 1101            | 1               | != 1101 | 0000011         | != 1111 | SUB, SUBS (register) - SUBS, rotate right with extend variant          |
| 1101            | 1               | xxxx    | 0000011         | 1111    | CMP(register) - Rotate right with extend variant                       |
| 1101            | 1               | 1101    | != 0000011      | != 1111 | SUB, SUBS (SP minus register) - SUBS, shift or rotate by value variant |
| 1101            | 1               | 1101    | 0000011         | != 1111 | SUB, SUBS (SP minus register) - SUBS, rotate right with extend variant |
| 1110            | x               | xxxx    | != 0000011      | xxxx    | RSB, RSBS (register) - RSBS, shift or rotate by value variant          |
| 1110            | x               | xxxx    | 0000011         | xxxx    | RSB, RSBS (register) - RSBS, rotate right with extend variant          |
| 1111            | x               | xxxx    | xxxxxxx         | xxxx    | Unallocated.                                                           |

## F3.1.6.3 Data-processing (modified immediate)

This section describes the encoding of the Data-processing (modified immediate) instruction class. The encodings in this section are decoded from 32-bit.

<!-- image -->

| 15 14 13 12 11 10 9 8   | 5 4 3   | 5 4 3   | 0 15 14   |   0 15 14 | 12 11 8   | 12 11 8   | 7   | 7    | 0   |
|-------------------------|---------|---------|-----------|-----------|-----------|-----------|-----|------|-----|
| 1 1 1 1 0 i 0           | op1     | S       | Rn        |         0 | imm3      | Rd        |     | imm8 |     |

## Table F3-29

| Decode fields   | Decode fields   | Instruction page   | Instruction page   | Instruction page                                |
|-----------------|-----------------|--------------------|--------------------|-------------------------------------------------|
| op1             | S               | Rn                 | Rd                 |                                                 |
| 0000            | 0               | xxxx               | xxxx               | AND, ANDS(immediate) - ANDvariant               |
| 0000            | 1               | xxxx               | != 1111            | AND, ANDS(immediate) - ANDSvariant              |
| 0000            | 1               | xxxx               | 1111               | TST (immediate)                                 |
| 0001            | x               | xxxx               | xxxx               | BIC, BICS (immediate)                           |
| 0010            | 0               | != 1111            | xxxx               | ORR, ORRS (immediate) - ORRvariant              |
| 0010            | 0               | 1111               | xxxx               | MOV, MOVS(immediate) - MOVvariant               |
| 0010            | 1               | != 1111            | xxxx               | ORR, ORRS (immediate) - ORRS variant            |
| 0010            | 1               | 1111               | xxxx               | MOV, MOVS(immediate) - MOVSvariant              |
| 0011            | 0               | != 1111            | xxxx               | ORN, ORNS(immediate) - Not flag setting variant |
| 0011            | 0               | 1111               | xxxx               | MVN, MVNS(immediate) - MVNvariant               |
| 0011            | 1               | != 1111            | xxxx               | ORN, ORNS(immediate) - Flag setting variant     |

| Decode fields   | Decode fields   |         |         |                                               |
|-----------------|-----------------|---------|---------|-----------------------------------------------|
| op1             | S               | Rn      | Rd      |                                               |
| 0011            | 1               | 1111    | xxxx    | MVN, MVNS(immediate) - MVNSvariant            |
| 0100            | 0               | xxxx    | xxxx    | EOR, EORS (immediate) - EORvariant            |
| 0100            | 1               | xxxx    | != 1111 | EOR, EORS (immediate) - EORS variant          |
| 0100            | 1               | xxxx    | 1111    | TEQ (immediate)                               |
| 0101            | x               | xxxx    | xxxx    | Unallocated.                                  |
| 011x            | x               | xxxx    | xxxx    | Unallocated.                                  |
| 1000            | 0               | != 1101 | xxxx    | ADD, ADDS(immediate) - ADDvariant             |
| 1000            | 0               | 1101    | xxxx    | ADD, ADDS(SP plus immediate) - ADDvariant     |
| 1000            | 1               | != 1101 | != 1111 | ADD, ADDS(immediate) - ADDSvariant            |
| 1000            | 1               | 1101    | != 1111 | ADD, ADDS(SP plus immediate) - ADDSvariant    |
| 1000            | 1               | xxxx    | 1111    | CMN(immediate)                                |
| 1001            | x               | xxxx    | xxxx    | Unallocated.                                  |
| 1010            | x               | xxxx    | xxxx    | ADC, ADCS(immediate)                          |
| 1011            | x               | xxxx    | xxxx    | SBC, SBCS (immediate)                         |
| 1100            | x               | xxxx    | xxxx    | Unallocated.                                  |
| 1101            | 0               | != 1101 | xxxx    | SUB, SUBS (immediate) - SUB variant           |
| 1101            | 0               | 1101    | xxxx    | SUB, SUBS (SP minus immediate) - SUB variant  |
| 1101            | 1               | != 1101 | != 1111 | SUB, SUBS (immediate) - SUBS variant          |
| 1101            | 1               | 1101    | != 1111 | SUB, SUBS (SP minus immediate) - SUBS variant |
| 1101            | 1               | xxxx    | 1111    | CMP(immediate)                                |
| 1110            | x               | xxxx    | xxxx    | RSB, RSBS (immediate)                         |
| 1111            | x               | xxxx    | xxxx    | Unallocated.                                  |

## F3.1.6.4 Long multiply and divide

This section describes the encoding of the Long multiply and divide instruction class. The encodings in this section are decoded from 32-bit.

| 15 14 13 12 11 10 9 8 7   | 6 4   | 0   | 12 11   | 8 7   | 4 3   | 0   |
|---------------------------|-------|-----|---------|-------|-------|-----|
| 1 1 1 1 1 0 1 1 1         | op1   | Rn  | RdLo    | RdHi  | op2   | Rm  |

## Table F3-30

| Decode fields   | Decode fields   | Instruction page   |
|-----------------|-----------------|--------------------|
| op1             | op2             |                    |
| 000             | != 0000         | Unallocated.       |

| Decode fields   | Decode fields   | Instruction page                                     |
|-----------------|-----------------|------------------------------------------------------|
| op1             | op2             | Instruction page                                     |
| 000             | 0000            | SMULL, SMULLS                                        |
| 001             | != 1111         | Unallocated.                                         |
| 001             | 1111            | SDIV                                                 |
| 010             | != 0000         | Unallocated.                                         |
| 010             | 0000            | UMULL,UMULLS                                         |
| 011             | != 1111         | Unallocated.                                         |
| 011             | 1111            | UDIV                                                 |
| 100             | 0000            | SMLAL, SMLALS                                        |
| 100             | 0001            | Unallocated.                                         |
| 100             | 001x            | Unallocated.                                         |
| 100             | 01xx            | Unallocated.                                         |
| 100             | 1000            | SMLALBB, SMLALBT, SMLALTB, SMLALTT - SMLALBBvariant  |
| 100             | 1001            | SMLALBB, SMLALBT, SMLALTB, SMLALTT - SMLALBTvariant  |
| 100             | 1010            | SMLALBB, SMLALBT, SMLALTB, SMLALTT - SMLALTB variant |
| 100             | 1011            | SMLALBB, SMLALBT, SMLALTB, SMLALTT - SMLALTT variant |
| 100             | 1100            | SMLALD, SMLALDX-SMLALDvariant                        |
| 100             | 1101            | SMLALD, SMLALDX-SMLALDXvariant                       |
| 100             | 111x            | Unallocated.                                         |
| 101             | 0xxx            | Unallocated.                                         |
| 101             | 10xx            | Unallocated.                                         |
| 101             | 1100            | SMLSLD,SMLSLDX - SMLSLD variant                      |
| 101             | 1101            | SMLSLD,SMLSLDX - SMLSLDXvariant                      |
| 101             | 111x            | Unallocated.                                         |
| 110             | 0000            | UMLAL,UMLALS                                         |
| 110             | 0001            | Unallocated.                                         |
| 110             | 001x            | Unallocated.                                         |
| 110             | 010x            | Unallocated.                                         |
| 110             | 0110            | UMAAL                                                |
| 110             | 0111            | Unallocated.                                         |
| 110             | 1xxx            | Unallocated.                                         |
| 111             | xxxx            | Unallocated.                                         |

## F3.1.7 System register access, Advanced SIMD, and floating-point

This section describes the encoding of the System register access, Advanced SIMD, and floating-point group. The encodings in this section are decoded from 32-bit.

<!-- image -->

Table F3-31 Encoding table for the System register access, Advanced SIMD, and floating-point group

| Decode fields   | Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page                             |
|-----------------|-----------------|------------------------------------|------------------------------------|--------------------------------------------------------------|
| op0             | op1             | op2                                | op3                                |                                                              |
| x               | 0x              | 0x                                 | x                                  | Unallocated.                                                 |
| x               | 10              | 0x                                 | x                                  | Unallocated.                                                 |
| x               | 11              | xx                                 | x                                  | Advanced SIMD data-processing                                |
| 0               | 0x              | 1x                                 | x                                  | Advanced SIMD and System register load/store and 64-bit move |
| 0               | 10              | 1x                                 | 1                                  | Advanced SIMD and System register 32-bit move                |
| 0               | 10              | 10                                 | 0                                  | Floating-point data-processing                               |
| 0               | 10              | 11                                 | 0                                  | Unallocated.                                                 |
| 1               | != 11           | 1x                                 | x                                  | Additional Advanced SIMD and floating-point instructions     |

## F3.1.8 Advanced SIMD data-processing

This section describes the encoding of the Advanced SIMD data-processing group. The encodings in this section are decoded from System register access, Advanced SIMD, and floating-point.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the T32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

Table F3-32 Encoding table for the Advanced SIMD data-processing group

| Decode fields   | Decode fields   | Decode group or instruction page                 |
|-----------------|-----------------|--------------------------------------------------|
| op0             | op1             |                                                  |
| 0               | x               | Advanced SIMD three registers of the same length |

| Decode fields   | Decode fields   | Decode group or instruction page                                     |
|-----------------|-----------------|----------------------------------------------------------------------|
| op0             | op1             |                                                                      |
| 1               | 0               | Advanced SIMD two registers, or three registers of different lengths |
| 1               | 1               | Advanced SIMD shifts and immediate generation                        |

## F3.1.8.1 Advanced SIMD three registers of the same length

This section describes the encoding of the Advanced SIMD three registers of the same length instruction class. The encodings in this section are decoded from Advanced SIMD data-processing.

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15   | 12 11   | 8 7 6 5 4 3   |
|---------------------------------|--------|---------|---------------|
| 1 1 1 U 1 1 1 1 0 D size        | Vn     | Vd      | N Q M o1 Vm   |

## Table F3-33

| Decode fields   | Decode fields   |      |    |    | Instruction page     | Feature   |
|-----------------|-----------------|------|----|----|----------------------|-----------|
| U               | size            | opc  | Q  | o1 | Instruction page     | Feature   |
| 0               | 0x              | 1100 | x  | 1  | VFMA                 | -         |
| 0               | 0x              | 1101 | x  | 0  | VADD(floating-point) | -         |
| 0               | 0x              | 1101 | x  | 1  | VMLA(floating-point) | -         |
| 0               | 0x              | 1110 | x  | 0  | VCEQ(register) - T2  | -         |
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
| x               | xx              | 0011 | x  | 0  | VCGT(register) - T1  | -         |
| x               | xx              | 0011 | x  | 1  | VCGE(register) - T1  | -         |
| 0               | 01              | 1100 | x  | 0  | SHA1P                | FEAT_SHA1 |
| 0               | 1x              | 1100 | x  | 1  | VFMS                 | -         |
| 0               | 1x              | 1101 | x  | 0  | VSUB(floating-point) | -         |
| 0               | 1x              | 1101 | x  | 1  | VMLS(floating-point) | -         |
| 0               | 1x              | 1110 | x  | 0  | Unallocated.         | -         |

| Decode fields   | Decode fields   |      |    |    | Instruction page             | Feature     |
|-----------------|-----------------|------|----|----|------------------------------|-------------|
| U               | size            | opc  | Q  | o1 |                              | Feature     |
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
| 1               | 0x              | 1110 | x  | 0  | VCGE(register) - T2          | -           |
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
| 1               | 1x              | 1110 | x  | 0  | VCGT(register) - T2          | -           |
| 1               | 1x              | 1110 | x  | 1  | VACGT                        | -           |
| 1               | 1x              | 1111 | 0  | 0  | VPMIN (floating-point)       | -           |
| 1               | 1x              | 1111 | x  | 1  | VMINNM                       | -           |
| 1               | xx              | 1000 | x  | 0  | VSUB(integer)                | -           |

| Decode fields   | Decode fields   |      |    |    | Instruction page    | Feature     |
|-----------------|-----------------|------|----|----|---------------------|-------------|
| U               | size            | opc  | Q  | o1 |                     |             |
| 1               | 10              | 0001 | x  | 1  | VBIT                | -           |
| 1               | xx              | 1000 | x  | 1  | VCEQ(register) - T1 | -           |
| 1               | xx              | 1001 | x  | 0  | VMLS(integer)       | -           |
| 1               | xx              | 1011 | x  | 0  | VQRDMULH            | -           |
| 1               | 10              | 1100 | x  | 0  | SHA256SU1           | FEAT_SHA256 |
| 1               | xx              | 1011 | x  | 1  | VQRDMLAH            | FEAT_RDM    |
| 1               | 11              | 0001 | x  | 1  | VBIF                | -           |
| 1               | xx              | 1100 | x  | 1  | VQRDMLSH            | FEAT_RDM    |
| 1               | xx              | 1111 | 1  | 0  | Unallocated.        | -           |

## F3.1.9 Advanced SIMD two registers, or three registers of different lengths

This section describes the encoding of the Advanced SIMD two registers, or three registers of different lengths group. The encodings in this section are decoded from Advanced SIMD data-processing.

<!-- image -->

Table F3-34 Encoding table for the Advanced SIMD two registers, or three registers of different lengths group

| Decode fields   | Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page                   |
|-----------------|-----------------|------------------------------------|------------------------------------|----------------------------------------------------|
| op0             | op1             | op2                                | op3                                |                                                    |
| 0               | 11              | xx                                 | x                                  | VEXT(byte elements)                                |
| 1               | 11              | 0x                                 | x                                  | Advanced SIMD two registers misc                   |
| 1               | 11              | 10                                 | x                                  | VTBL,VTBX                                          |
| 1               | 11              | 11                                 | x                                  | Advanced SIMD duplicate (scalar)                   |
| x               | != 11           | xx                                 | 0                                  | Advanced SIMD three registers of different lengths |
| x               | != 11           | xx                                 | 1                                  | Advanced SIMD two registers and a scalar           |

## F3.1.9.1 Advanced SIMD two registers misc

This section describes the encoding of the Advanced SIMD two registers misc instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1   | 0 15 12 11 10 7 6 5 4 3   |
|---------------------------------------|---------------------------|
| 1 1 1 1 1 1 1 1 1 D 1 1 size opc1     | Vd 0 opc2 Q M 0 Vm        |

## Table F3-35

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

## F3.1.9.2 Advanced SIMD duplicate (scalar)

This section describes the encoding of the Advanced SIMD duplicate (scalar) instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5   | 4 3 0 15   | 12 11 10 9 7 6 5 4 3   |
|-------------------------------|------------|------------------------|
| 1 1 1 1 1 1 1 1 1 D 1         | 1 imm4 Vd  | 1 1 opc Q M 0 Vm       |

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| 000             | VDUP(scalar)       |
| 001             | Unallocated.       |
| 01x             | Unallocated.       |
| 1xx             | Unallocated.       |

## F3.1.9.3 Advanced SIMD three registers of different lengths

This section describes the encoding of the Advanced SIMD three registers of different lengths instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

<!-- image -->

## Table F3-37

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

## F3.1.9.4 Advanced SIMD two registers and a scalar

This section describes the encoding of the Advanced SIMD two registers and a scalar instruction class. The encodings in this section are decoded from Advanced SIMD two registers, or three registers of different lengths.

| 15 14 13 12 11 10 9 8 7 6 5   | 4 3 0 15              | 12 11   | 8      | 7 6 5   | 4   |   3 | 0   |
|-------------------------------|-----------------------|---------|--------|---------|-----|-----|-----|
| 1 1 1                         | Q 1 1 1 1 1 D !=11 Vn |         | Vd opc | N 1     | M   |   0 | Vm  |

size

## Table F3-38

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

## F3.1.10 Advanced SIMD shifts and immediate generation

This section describes the encoding of the Advanced SIMD shifts and immediate generation group. The encodings in this section are decoded from Advanced SIMD data-processing.

<!-- image -->

|   15 | 13 12 11   |   13 12 11 | 7 6 5 0 15   |   7 6 5 4 3 |
|------|------------|------------|--------------|-------------|
|  111 |            |      11111 | op0          |           1 |

Table F3-39 Encoding table for the Advanced SIMD shifts and immediate generation group

| Decode fields      | Decode group or instruction page                  |
|--------------------|---------------------------------------------------|
| op0                |                                                   |
| 000xxxxxxxxxxx0    | Advanced SIMD one register and modified immediate |
| != 000xxxxxxxxxxx0 | Advanced SIMD two registers and shift amount      |

## F3.1.10.1 Advanced SIMD one register and modified immediate

This section describes the encoding of the Advanced SIMD one register and modified immediate instruction class. The encodings in this section are decoded from Advanced SIMD shifts and immediate generation.

<!-- image -->

| 15 14 13 12 11 10 9 8   | 7 6 5 4 3 2 0 15 12 11 8 7 6 5 4 3    |
|-------------------------|---------------------------------------|
| 1 1 1 i 1 1 1 1         | 1 D 0 0 0 imm3 Vd cmode 0 Q op 1 imm4 |

## Table F3-40

| Decode fields   |    | Instruction page      |
|-----------------|----|-----------------------|
| cmode           | op |                       |
| 0xx0            | 0  | VMOV(immediate) - T1  |
| 0xx0            | 1  | VMVN(immediate) - T1  |
| 0xx1            | 0  | VORR(immediate) - T1  |
| 0xx1            | 1  | VBIC (immediate) - T1 |
| 10x0            | 0  | VMOV(immediate) - T3  |
| 10x0            | 1  | VMVN(immediate) - T2  |
| 10x1            | 0  | VORR(immediate) - T2  |
| 10x1            | 1  | VBIC (immediate) - T2 |
| 11xx            | 0  | VMOV(immediate) - T4  |
| 110x            | 1  | VMVN(immediate) - T3  |
| 1110            | 1  | VMOV(immediate) - T5  |
| 1111            | 1  | Unallocated.          |

## F3.1.10.2 Advanced SIMD two registers and shift amount

This section describes the encoding of the Advanced SIMD two registers and shift amount instruction class. The encodings in this section are decoded from Advanced SIMD shifts and immediate generation.

| 15 14 13 12 11 10 9 8 7 6 5   | 3 2         | 0 15   | 12 11 8 7 6 5 4 3   |
|-------------------------------|-------------|--------|---------------------|
| 1 1 1 U 1 1 1 1 1 D           | imm3H imm3L | Vd     | opc L Q M 1 Vm      |

## Table F3-41

| Decode fields   | Decode fields   |       |      |    |    | Instruction page                                                        |
|-----------------|-----------------|-------|------|----|----|-------------------------------------------------------------------------|
| U               | imm3H:L         | imm3L | opc  | L  | Q  |                                                                         |
| x               | != 0000         | xxx   | 0000 | x  | x  | VSHR                                                                    |
| x               | != 0000         | xxx   | 0001 | x  | x  | VSRA                                                                    |
| x               | != 0000         | 000   | 1010 | 0  | 0  | VMOVL                                                                   |
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

## F3.1.11 Advanced SIMD and System register load/store and 64-bit move

This section describes the encoding of the Advanced SIMD and System register load/store and 64-bit move group. The encodings in this section are decoded from System register access, Advanced SIMD, and floating-point.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the T32 Advanced SIMD and floating-point instructions and their encoding

|      15 | 9 8   | 5 4   |   0 15 | 12 11 10 9 8   |
|---------|-------|-------|--------|----------------|
| 1110110 | op0   |       |      1 | op1            |

Table F3-42 Encoding table for the Advanced SIMD and System register load/store and 64-bit move group

| Decode fields   |    | Decode group or instruction page             |
|-----------------|----|----------------------------------------------|
| 00x0            | 0x | Advanced SIMD and floating-point 64-bit move |
| 00x0            | 11 | System register 64-bit move                  |
| != 00x0         | 0x | Advanced SIMD and floating-point load/store  |
| != 00x0         | 11 | System register Load/Store                   |
| xxxx            | 10 | Unallocated.                                 |

## F3.1.11.1 Advanced SIMD and floating-point 64-bit move

This section describes the encoding of the Advanced SIMD and floating-point 64-bit move instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15   | 12 11 10 9 8 7 6 5 4   |
|-----------------------------------|--------|------------------------|
| 1 1 1 0 1 1 0 0 0 D 0 op          | Rt2    | 1 0 size opc2 M o3     |

## Table F3-43

| Decode fields   | Decode fields   | Decode fields   |      |    | Instruction page                                                                                                              |
|-----------------|-----------------|-----------------|------|----|-------------------------------------------------------------------------------------------------------------------------------|
| D               | op              | size            | opc2 | o3 | Instruction page                                                                                                              |
| 0               | x               | xx              | xx   | x  | Unallocated.                                                                                                                  |
| 1               | x               | xx              | xx   | 0  | Unallocated.                                                                                                                  |
| 1               | x               | 0x              | 00   | 1  | Unallocated.                                                                                                                  |
| 1               | x               | xx              | 01   | x  | Unallocated.                                                                                                                  |
| 1               | 0               | 10              | 00   | 1  | VMOV(between two general-purpose registers and two single-precision registers) - From general-purpose registers variant       |
| 1               | 0               | 11              | 00   | 1  | VMOV(between two general-purpose registers and a doubleword floating-point register) - From general-purpose registers variant |
| 1               | x               | xx              | 1x   | x  | Unallocated.                                                                                                                  |

| Decode fields   | Decode fields   | Decode fields   |      |    |                                                                                                                             |
|-----------------|-----------------|-----------------|------|----|-----------------------------------------------------------------------------------------------------------------------------|
| D               | op              | size            | opc2 | o3 |                                                                                                                             |
| 1               | 1               | 10              | 00   | 1  | VMOV(between two general-purpose registers and two single-precision registers) - To general-purpose registers variant       |
| 1               | 1               | 11              | 00   | 1  | VMOV(between two general-purpose registers and a doubleword floating-point register) - To general-purpose registers variant |

## F3.1.11.2 System register 64-bit move

This section describes the encoding of the System register 64-bit move instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15   | 12 11 10 9 8   | 4 3   |     |
|-----------------------------------|--------|----------------|-------|-----|
| 1 1 1 0 1 1 0 0 0 D 0 L           | Rt2    | 1 1 1          | opc1  | CRm |

<!-- image -->

## Table F3-44

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| D               | L                  |
| 0               | x Unallocated.     |
| 1               | 0 MCRR             |
| 1               | 1 MRRC             |

## F3.1.11.3 Advanced SIMD and floating-point load/store

This section describes the encoding of the Advanced SIMD and floating-point load/store instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15   | 12 11 10 9 8   |
|---------------------------------|--------|----------------|
| 1 1 1 0 1 1 0 P U D W L         | Rn     | 1 0 size       |

## Table F3-45

| Decode fields   | Decode fields   | Decode fields   |    |         |      |          | Instruction page                                    | Feature   |
|-----------------|-----------------|-----------------|----|---------|------|----------|-----------------------------------------------------|-----------|
| P               | U               | W               | L  | Rn      | size | imm8     |                                                     |           |
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
| 1               | 1               | 1               | x  | xxxx    | xx   | xxxxxxxx | Unallocated.                                        | -         |

## F3.1.11.4 System register Load/Store

This section describes the encoding of the System register Load/Store instruction class. The encodings in this section are decoded from Advanced SIMD and System register load/store and 64-bit move.

<!-- image -->

## Table F3-46

| Decode fields   | Decode fields   |    |         |         |      | Instruction page                      |
|-----------------|-----------------|----|---------|---------|------|---------------------------------------|
| P:U:W           | D               | L  | Rn      | CRd     | cp15 |                                       |
| != 000          | x               | x  | xxxx    | != 0101 | 0    | Unallocated.                          |
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

## F3.1.12 Advanced SIMD and System register 32-bit move

This section describes the encoding of the Advanced SIMD and System register 32-bit move group. The encodings in this section are decoded from System register access, Advanced SIMD, and floating-point.

<!-- image -->

|       15 | 8 7   | 5 4   |   12 11 10 | 8   | 7   |   5 4 3 | 0   |
|----------|-------|-------|------------|-----|-----|---------|-----|
| 11101110 | op0   |       |          1 | op1 |     |       1 |     |

## Table F3-47 Encoding table for the Advanced SIMD and System register 32-bit move group

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

## F3.1.12.1 Floating-point move special register

This section describes the encoding of the Floating-point move special register instruction class. The encodings in this section are decoded from Advanced SIMD and System register 32-bit move.

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15   | 12 11 10 9 8 7 6 5 4 3 2 1 0          |
|-----------------------------------|--------|---------------------------------------|
| 1 1 1 0 1 1 1 0 1 1 1 L           | reg    | 1 0 1 0 (0) (0) (0) 1 (0) (0) (0) (0) |

## Table F3-48

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | VMSR               |
| 1               | VMRS               |

## F3.1.12.2 Advanced SIMD 8/16/32-bit element move/duplicate

This section describes the encoding of the Advanced SIMD 8/16/32-bit element move/duplicate instruction class. The encodings in this section are decoded from Advanced SIMD and System register 32-bit move.

| 15 14 13 12 11 10 9 8   | 5 4 3   | 0 15   | 12 11 10 9 8 7 6 5 4 3 2 1 0     |
|-------------------------|---------|--------|----------------------------------|
| 1 1 1 0 1 1 1 0         | L       | Vn     | 1 0 1 1 N opc2 1 (0) (0) (0) (0) |

## Table F3-49

| Decode fields   | Instruction page   |      |                                          |
|-----------------|--------------------|------|------------------------------------------|
| opc1            | L                  | opc2 |                                          |
| 0xx             | 0                  | xx   | VMOV(general-purpose register to scalar) |
| xxx             | 1                  | xx   | VMOV(scalar to general-purpose register) |
| 1xx             | 0                  | 0x   | VDUP(general-purpose register)           |
| 1xx             | 0                  | 1x   | Unallocated.                             |

## F3.1.12.3 System register 32-bit move

This section describes the encoding of the System register 32-bit move instruction class. The encodings in this section are decoded from Advanced SIMD and System register 32-bit move.

<!-- image -->

## Table F3-50

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | MCR                |
| 1               | MRC                |

## F3.1.13 Floating-point data-processing

This section describes the encoding of the Floating-point data-processing group. The encodings in this section are decoded from System register access, Advanced SIMD, and floating-point.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the T32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

## Table F3-51 Encoding table for the Floating-point data-processing group

| Decode fields   |    | Decode group or instruction page                 |
|-----------------|----|--------------------------------------------------|
| 1x11            | 1  | Floating-point data-processing (two registers)   |
| 1x11            | 0  | Floating-point move immediate                    |
| != 1x11         | x  | Floating-point data-processing (three registers) |

## F3.1.13.1 Floating-point data-processing (two registers)

This section describes the encoding of the Floating-point data-processing (two registers) instruction class. The encodings in this section are decoded from Floating-point data-processing.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6       | 5 4 3 2 0 15 12 11 10 9 8 7 6 5 4 3   |
|---------------------------------|---------------------------------------|
| 1 1 1 0 1 1 1 0 1 D 1 1 o1 opc2 | Vd 1 0 size o3 1 M 0 Vm               |

## Table F3-52

| Decode fields   | Decode fields   |      |    | Instruction page                                  | Feature   |
|-----------------|-----------------|------|----|---------------------------------------------------|-----------|
| o1              | opc2            | size | o3 |                                                   | Feature   |
| x               | xxx             | 00   | x  | Unallocated.                                      | -         |
| 0               | 000             | 01   | 0  | Unallocated.                                      | -         |
| 0               | 000             | 01   | 1  | VABS - Half-precision scalar variant              | FEAT_FP16 |
| 0               | 000             | 10   | 0  | VMOV(register) - Single-precision scalar variant  | -         |
| 0               | 000             | 10   | 1  | VABS - Single-precision scalar variant            | -         |
| 0               | 000             | 11   | 0  | VMOV(register) - Double-precision scalar variant  | -         |
| 0               | 000             | 11   | 1  | VABS - Double-precision scalar variant            | -         |
| 0               | 001             | 01   | 0  | VNEG-Half-precision scalar variant                | FEAT_FP16 |
| 0               | 001             | 01   | 1  | VSQRT - Half-precision scalar variant             | FEAT_FP16 |
| 0               | 001             | 10   | 0  | VNEG-Single-precision scalar variant              | -         |
| 0               | 001             | 10   | 1  | VSQRT - Single-precision scalar variant           | -         |
| 0               | 001             | 11   | 0  | VNEG-Double-precision scalar variant              | -         |
| 0               | 001             | 11   | 1  | VSQRT - Double-precision scalar variant           | -         |
| 0               | 010             | 01   | x  | Unallocated.                                      | -         |
| 0               | 010             | 10   | 0  | VCVTB- Half-precision to single-precision variant | -         |
| 0               | 010             | 10   | 1  | VCVTT- Half-precision to single-precision variant | -         |
| 0               | 010             | 11   | 0  | VCVTB- Half-precision to double-precision variant | -         |

| Decode fields   | Decode fields   |      |    | Instruction page                                                                                   | Feature       |
|-----------------|-----------------|------|----|----------------------------------------------------------------------------------------------------|---------------|
| o1              | opc2            | size | o3 |                                                                                                    |               |
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
| 1               | 000             | 01   | x  | VCVT(integer to floating-point, floating-point) - Half-precision scalar variant                    | FEAT_FP16     |
| 1               | 000             | 10   | x  | VCVT(integer to floating-point, floating-point) - Single-precision scalar variant                  | -             |
| 1               | 000             | 11   | x  | VCVT(integer to floating-point, floating-point) - Double-precision scalar variant                  | -             |
| 1               | 001             | 01   | x  | Unallocated.                                                                                       | -             |

| Decode fields   | Decode fields   |      |    | Instruction page                                             | Feature    |
|-----------------|-----------------|------|----|--------------------------------------------------------------|------------|
| o1              | opc2            | size | o3 |                                                              |            |
| 1               | 001             | 11   | 0  | Unallocated.                                                 | -          |
| 1               | 001             | 11   | 1  | VJCVT                                                        | FEAT_JSCVT |
| 1               | 01x             | 01   | x  | VCVT(between floating-point and fixed-point, floating-point) | FEAT_FP16  |
| 1               | 01x             | 10   | x  | VCVT(between floating-point and fixed-point, floating-point) | -          |
| 1               | 01x             | 11   | x  | VCVT(between floating-point and fixed-point, floating-point) | -          |
| 1               | 100             | 01   | 0  | VCVTR                                                        | FEAT_FP16  |
| 1               | 100             | 01   | 1  | VCVT(floating-point to integer, floating-point)              | FEAT_FP16  |
| 1               | 100             | 10   | 0  | VCVTR                                                        | -          |
| 1               | 100             | 10   | 1  | VCVT(floating-point to integer, floating-point)              | -          |
| 1               | 100             | 11   | 0  | VCVTR                                                        | -          |
| 1               | 100             | 11   | 1  | VCVT(floating-point to integer, floating-point)              | -          |
| 1               | 101             | 01   | 0  | VCVTR                                                        | FEAT_FP16  |
| 1               | 101             | 01   | 1  | VCVT(floating-point to integer, floating-point)              | FEAT_FP16  |
| 1               | 101             | 10   | 0  | VCVTR                                                        | -          |
| 1               | 101             | 10   | 1  | VCVT(floating-point to integer, floating-point)              | -          |
| 1               | 101             | 11   | 0  | VCVTR                                                        | -          |
| 1               | 101             | 11   | 1  | VCVT(floating-point to integer, floating-point)              | -          |
| 1               | 11x             | 01   | x  | VCVT(between floating-point and fixed-point, floating-point) | FEAT_FP16  |
| 1               | 11x             | 10   | x  | VCVT(between floating-point and fixed-point, floating-point) | -          |
| 1               | 11x             | 11   | x  | VCVT(between floating-point and fixed-point, floating-point) | -          |

## F3.1.13.2 Floating-point move immediate

This section describes the encoding of the Floating-point move immediate instruction class. The encodings in this section are decoded from Floating-point data-processing.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5   | 0 15   | 12 11 10 9 8 7 6 5 4 3     |
|-------------------------------|--------|----------------------------|
| 1 1 1 0 1 1 1 0 1 D 1         | imm4H  | 1 0 size (0) 0 (0) 0 imm4L |

## Table F3-53

|   Decode fields | Instruction page                                  | Feature   |
|-----------------|---------------------------------------------------|-----------|
|              00 | Unallocated.                                      | -         |
|              01 | VMOV(immediate) - Half-precision scalar variant   | FEAT_FP16 |
|              10 | VMOV(immediate) - Single-precision scalar variant | -         |

|   Decode fields | Instruction page                                  | Feature   |
|-----------------|---------------------------------------------------|-----------|
|              11 | VMOV(immediate) - Double-precision scalar variant | -         |

## F3.1.13.3 Floating-point data-processing (three registers)

This section describes the encoding of the Floating-point data-processing (three registers) instruction class. The encodings in this section are decoded from Floating-point data-processing.

| 15 14 13 12 11 10 9 8 7 6   | 4 3   | 12 11 10 9 8 7 6 5 4 3   |
|-----------------------------|-------|--------------------------|
| 1 1 1 0 1 1 1 0 o0 D        | o1 Vn | 1 0 size N o2 M 0 Vm     |

## Table F3-54

| Decode fields   | Decode fields   |    | Instruction page                                       | Feature   |
|-----------------|-----------------|----|--------------------------------------------------------|-----------|
| o0:o1           | size            | o2 |                                                        | Feature   |
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
| 010             | 11              | 1  | VNMUL-Double-precision scalar variant                  | -         |
| 011             | 01              | 0  | VADD(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 011             | 01              | 1  | VSUB(floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 011             | 10              | 0  | VADD(floating-point) - Single-precision scalar variant | -         |

| Decode fields   | Decode fields   |    | Instruction page                                       | Feature   |
|-----------------|-----------------|----|--------------------------------------------------------|-----------|
| o0:o1           | size            | o2 | Instruction page                                       | Feature   |
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

## F3.1.14 Additional Advanced SIMD and floating-point instructions

This section describes the encoding of the Additional Advanced SIMD and floating-point instructions group. The encodings in this section are decoded from System register access, Advanced SIMD, and floating-point.

<!-- image -->

This decode also imposes the constraint:

- op0&lt;2:1&gt; != 11 .

Table F3-55 Encoding table for the Additional Advanced SIMD and floating-point instructions group

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

## F3.1.14.1 Advanced SIMD three registers of the same length extension

This section describes the encoding of the Advanced SIMD three registers of the same length extension instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F3-56

| Decode fields   | Decode fields   |     |     |    |    | Instruction page                           | Feature       |
|-----------------|-----------------|-----|-----|----|----|--------------------------------------------|---------------|
| op1             | op2             | op3 | op4 | Q  | U  |                                            | Feature       |
| x1              | 0x              | 0   | 0   | 0  | 0  | VCADD-64-bit SIMD vector variant           | FEAT_FCMA     |
| x1              | 0x              | 0   | 0   | 0  | 1  | Unallocated.                               | -             |
| x1              | 0x              | 0   | 0   | 1  | 0  | VCADD-128-bit SIMD vector variant          | FEAT_FCMA     |
| x1              | 0x              | 0   | 0   | 1  | 1  | Unallocated.                               | -             |
| 00              | 0x              | 0   | 0   | x  | x  | Unallocated.                               | -             |
| 00              | 0x              | 0   | 1   | x  | x  | Unallocated.                               | -             |
| 00              | 00              | 1   | 0   | 0  | 0  | Unallocated.                               | -             |
| 00              | 00              | 1   | 0   | 0  | 1  | Unallocated.                               | -             |
| 00              | 00              | 1   | 0   | 1  | 0  | VMMLA                                      | FEAT_AA32BF16 |
| 00              | 00              | 1   | 0   | 1  | 1  | Unallocated.                               | -             |
| 00              | 00              | 1   | 1   | 0  | 0  | VDOT(vector) - 64-bit SIMD vector variant  | FEAT_AA32BF16 |
| 00              | 00              | 1   | 1   | 0  | 1  | Unallocated.                               | -             |
| 00              | 00              | 1   | 1   | 1  | 0  | VDOT(vector) - 128-bit SIMD vector variant | FEAT_AA32BF16 |

| Decode fields   | Decode fields   |     |     |    |    | Instruction page                             | Feature       |
|-----------------|-----------------|-----|-----|----|----|----------------------------------------------|---------------|
| op1             | op2             | op3 | op4 | Q  | U  |                                              |               |
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
| 01              | 11              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 01              | 11              | 1   | 0   | x  | x  | Unallocated.                                 | -             |
| 01              | 11              | 1   | 1   | x  | x  | Unallocated.                                 | -             |
| xx              | 1x              | 0   | 0   | x  | 0  | VCMLA                                        | FEAT_FCMA     |
| 10              | 11              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 10              | 11              | 1   | 0   | x  | x  | Unallocated.                                 | -             |
| 10              | 11              | 1   | 1   | x  | x  | Unallocated.                                 | -             |
| 11              | 11              | 0   | 1   | x  | x  | Unallocated.                                 | -             |
| 11              | 11              | 1   | 0   | x  | x  | Unallocated.                                 | -             |
| 11              | 11              | 1   | 1   | x  | x  | Unallocated.                                 | -             |

## F3.1.14.2 Floating-point conditional select

This section describes the encoding of the Floating-point conditional select instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F3-57

|   Decode fields size | Instruction page                                                               | Feature   |
|----------------------|--------------------------------------------------------------------------------|-----------|
|                   01 | VSELEQ, VSELGE, VSELGT, VSELVS - Greater than, half-precision scalar variant   | FEAT_FP16 |
|                   10 | VSELEQ, VSELGE, VSELGT, VSELVS - Greater than, single-precision scalar variant | -         |
|                   11 | VSELEQ, VSELGE, VSELGT, VSELVS - Greater than, double-precision scalar variant | -         |

## F3.1.14.3 Floating-point minNum/maxNum

This section describes the encoding of the Floating-point minNum/maxNum instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F3-58

|   Decode fields |    | Instruction page                       | Feature   |
|-----------------|----|----------------------------------------|-----------|
|              01 |  0 | VMAXNM-Half-precision scalar variant   | FEAT_FP16 |
|              01 |  1 | VMINNM-Half-precision scalar variant   | FEAT_FP16 |
|              10 |  0 | VMAXNM-Single-precision scalar variant | -         |
|              10 |  1 | VMINNM-Single-precision scalar variant | -         |
|              11 |  0 | VMAXNM-Double-precision scalar variant | -         |
|              11 |  1 | VMINNM-Double-precision scalar variant | -         |

## F3.1.14.4 Floating-point extraction and insertion

This section describes the encoding of the Floating-point extraction and insertion instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F3-59

|   Decode fields | Instruction   | page         | Feature   |
|-----------------|---------------|--------------|-----------|
|              01 | x             | Unallocated. | -         |
|              10 | 0             | VMOVX        | FEAT_FP16 |
|              10 | 1             | VINS         | FEAT_FP16 |
|              11 | x             | Unallocated. | -         |

## F3.1.14.5 Floating-point directed convert to integer

This section describes the encoding of the Floating-point directed convert to integer instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | 15 12 11 10 9 8 7 6 5 4   |
|-----------------------------------------|---------------------------|
| 1 1 1 1 1 1 1 0 1 D 1 1 1 o1 RM         | Vd 1 0 !=00 op 1 M 0      |

## Table F3-60

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

size

| Decode fields   | Decode fields   |      |    | Instruction page                                          | Feature   |
|-----------------|-----------------|------|----|-----------------------------------------------------------|-----------|
| o1              | RM              | size | op |                                                           | Feature   |
| 0               | 11              | 01   | 0  | VRINTM (floating-point) - Half-precision scalar variant   | FEAT_FP16 |
| 0               | 11              | 10   | 0  | VRINTM (floating-point) - Single-precision scalar variant | -         |
| 0               | 11              | 11   | 0  | VRINTM (floating-point) - Double-precision scalar variant | -         |
| 1               | 00              | 01   | x  | VCVTA(floating-point) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | 00              | 10   | x  | VCVTA(floating-point) - Single-precision scalar variant   | -         |
| 1               | 00              | 11   | x  | VCVTA(floating-point) - Double-precision scalar variant   | -         |
| 1               | 01              | 01   | x  | VCVTN(floating-point) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | 01              | 10   | x  | VCVTN(floating-point) - Single-precision scalar variant   | -         |
| 1               | 01              | 11   | x  | VCVTN(floating-point) - Double-precision scalar variant   | -         |
| 1               | 10              | 01   | x  | VCVTP (floating-point) - Half-precision scalar variant    | FEAT_FP16 |
| 1               | 10              | 10   | x  | VCVTP (floating-point) - Single-precision scalar variant  | -         |
| 1               | 10              | 11   | x  | VCVTP (floating-point) - Double-precision scalar variant  | -         |
| 1               | 11              | 01   | x  | VCVTM(floating-point) - Half-precision scalar variant     | FEAT_FP16 |
| 1               | 11              | 10   | x  | VCVTM(floating-point) - Single-precision scalar variant   | -         |
| 1               | 11              | 11   | x  | VCVTM(floating-point) - Double-precision scalar variant   | -         |

## F3.1.14.6 Advanced SIMD and floating-point multiply with accumulate

This section describes the encoding of the Advanced SIMD and floating-point multiply with accumulate instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F3-61

| Decode fields   | Decode fields   |    |    | Instruction page                                                                  | Feature       |
|-----------------|-----------------|----|----|-----------------------------------------------------------------------------------|---------------|
| op1             | op2             | Q  | U  |                                                                                   |               |
| 0               | xx              | x  | 0  | VCMLA(by element) - 128-bit SIMD vector of half-precision floating-point variant  | FEAT_FCMA     |
| 0               | 00              | x  | 1  | VFMAL(by scalar)                                                                  | FEAT_FHM      |
| 0               | 01              | x  | 1  | VFMSL(by scalar)                                                                  | FEAT_FHM      |
| 0               | 10              | x  | 1  | Unallocated.                                                                      | -             |
| 0               | 11              | x  | 1  | VFMAB, VFMAT(BFloat16, by scalar)                                                 | FEAT_AA32BF16 |
| 1               | xx              | 0  | 0  | VCMLA(by element) - 64-bit SIMD vector of single-precision floating-point variant | FEAT_FCMA     |

| Decode fields   | Decode fields   | Instruction page   | Instruction page                                                                   | Feature   |
|-----------------|-----------------|--------------------|------------------------------------------------------------------------------------|-----------|
| op1             | op2             | Q                  |                                                                                    | Feature   |
| 1               | xx              | x                  | Unallocated.                                                                       | -         |
| 1               | xx              | 1                  | VCMLA(by element) - 128-bit SIMD vector of single-precision floating-point variant | FEAT_FCMA |

## F3.1.14.7 Advanced SIMD and floating-point dot product

This section describes the encoding of the Advanced SIMD and floating-point dot product instruction class. The encodings in this section are decoded from Additional Advanced SIMD and floating-point instructions.

<!-- image -->

## Table F3-62

| Decode fields   | Decode fields   |     |    |    | Instruction page                                 | Feature       |
|-----------------|-----------------|-----|----|----|--------------------------------------------------|---------------|
| op1             | op2             | op4 | Q  | U  |                                                  | Feature       |
| 0               | 00              | 0   | x  | x  | Unallocated.                                     | -             |
| 0               | 00              | 1   | 0  | 0  | VDOT(by element) - 64-bit SIMD vector variant    | FEAT_AA32BF16 |
| 0               | 00              | 1   | x  | 1  | Unallocated.                                     | -             |
| 0               | 00              | 1   | 1  | 0  | VDOT(by element) - 128-bit SIMD vector variant   | FEAT_AA32BF16 |
| 0               | 01              | 0   | x  | x  | Unallocated.                                     | -             |
| 0               | 10              | 0   | x  | x  | Unallocated.                                     | -             |
| 0               | 10              | 1   | 0  | 0  | VSDOT(by element) - 64-bit SIMD vector variant   | FEAT_DotProd  |
| 0               | 10              | 1   | 0  | 1  | VUDOT(by element) - 64-bit SIMD vector variant   | FEAT_DotProd  |
| 0               | 10              | 1   | 1  | 0  | VSDOT(by element) - 128-bit SIMD vector variant  | FEAT_DotProd  |
| 0               | 10              | 1   | 1  | 1  | VUDOT(by element) - 128-bit SIMD vector variant  | FEAT_DotProd  |
| 0               | 11              | x   | x  | x  | Unallocated.                                     | -             |
| 1               | xx              | 0   | x  | x  | Unallocated.                                     | -             |
| 1               | 00              | 1   | 0  | 0  | VUSDOT(by element) - 64-bit SIMD vector variant  | FEAT_AA32I8MM |
| 1               | 00              | 1   | 0  | 1  | VSUDOT(by element) - 64-bit SIMD vector variant  | FEAT_AA32I8MM |
| 1               | 00              | 1   | 1  | 0  | VUSDOT(by element) - 128-bit SIMD vector variant | FEAT_AA32I8MM |
| 1               | 00              | 1   | 1  | 1  | VSUDOT(by element) - 128-bit SIMD vector variant | FEAT_AA32I8MM |
| 1               | 01              | 1   | x  | x  | Unallocated.                                     | -             |
| 1               | 1x              | 1   | x  | x  | Unallocated.                                     | -             |

## F3.1.15 Load/store dual, load/store exclusive, load-acquire/store-release, and table branch

This section describes the encoding of the Load/store dual, load/store exclusive, load-acquire/store-release, and table branch group. The encodings in this section are decoded from 32-bit.

<!-- image -->

This decode also imposes the constraint:

- op0&lt;1&gt; == 1 .

Table F3-63 Encoding table for the Load/store dual, load/store exclusive, load-acquire/store-release, and table branch group

| Decode fields   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page   | Decode group or instruction page          |
|-----------------|------------------------------------|------------------------------------|------------------------------------|-------------------------------------------|
| op0             | op1                                | op2                                | op3                                |                                           |
| 0010            | x                                  | xxxx                               | xxx                                | Load/store exclusive                      |
| 0110            | 0                                  | xxxx                               | 000                                | Unallocated.                              |
| 0110            | 1                                  | xxxx                               | 000                                | TBB,TBH                                   |
| 0110            | x                                  | xxxx                               | 01x                                | Load/store exclusive byte/half/dual       |
| 0110            | x                                  | xxxx                               | 1xx                                | Load-acquire / Store-release              |
| 0x11            | x                                  | != 1111                            | xxx                                | Load/store dual (immediate, post-indexed) |
| 1x10            | x                                  | != 1111                            | xxx                                | Load/store dual (immediate)               |
| 1x11            | x                                  | != 1111                            | xxx                                | Load/store dual (immediate, pre-indexed)  |
| != 0xx0         | x                                  | 1111                               | xxx                                | LDRD(literal)                             |

## F3.1.15.1 Load/store exclusive

This section describes the encoding of the Load/store exclusive instruction class. The encodings in this section are decoded from Load/store dual, load/store exclusive, load-acquire/store-release, and table branch.

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15   | 12 11   | 8 7   | 0    |
|-----------------------------------|--------|---------|-------|------|
| 1 1 1 0 1 0 0 0 0 1 0 L           | Rn     | Rt      | Rd    | imm8 |

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STREX              |
| 1               | LDREX              |

## F3.1.15.2 Load/store exclusive byte/half/dual

This section describes the encoding of the Load/store exclusive byte/half/dual instruction class. The encodings in this section are decoded from Load/store dual, load/store exclusive, load-acquire/store-release, and table branch.

| 15 14 13 12 11 10 9 8 7 6 5 4   | 3         | 0 15   | 12 11   | 8 7   | 6 5 4   | 3   | 0   |
|---------------------------------|-----------|--------|---------|-------|---------|-----|-----|
| 1 1 1 0 1 0 0                   | 0 1 1 0 L | Rn     | Rt      | 0 1   |         | sz  | Rd  |

## Table F3-65

| Decode fields   | Instruction page   |              |
|-----------------|--------------------|--------------|
| L               | sz                 |              |
| 0               | 00                 | STREXB       |
| 0               | 01                 | STREXH       |
| 0               | 10                 | Unallocated. |
| 0               | 11                 | STREXD       |
| 1               | 00                 | LDREXB       |
| 1               | 01                 | LDREXH       |
| 1               | 10                 | Unallocated. |
| 1               | 11                 | LDREXD       |

## F3.1.15.3 Load-acquire / Store-release

This section describes the encoding of the Load-acquire / Store-release instruction class. The encodings in this section are decoded from Load/store dual, load/store exclusive, load-acquire/store-release, and table branch.

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15   | 12 11 8 7 6 5 4 3   |
|-----------------------------------|--------|---------------------|
| 1 1 1 0 1 0 0 0 1 1 0 L           | Rn     | Rt2 1 op sz Rd      |

| Decode fields   | Decode fields   |    | Instruction page   |
|-----------------|-----------------|----|--------------------|
| L               | op              | sz |                    |
| 0               | 0               | 00 | STLB               |
| 0               | 0               | 01 | STLH               |
| 0               | 0               | 10 | STL                |
| 0               | 0               | 11 | Unallocated.       |
| 0               | 1               | 00 | STLEXB             |
| 0               | 1               | 01 | STLEXH             |
| 0               | 1               | 10 | STLEX              |
| 0               | 1               | 11 | STLEXD             |
| 1               | 0               | 00 | LDAB               |
| 1               | 0               | 01 | LDAH               |
| 1               | 0               | 10 | LDA                |
| 1               | 0               | 11 | Unallocated.       |
| 1               | 1               | 00 | LDAEXB             |
| 1               | 1               | 01 | LDAEXH             |
| 1               | 1               | 10 | LDAEX              |
| 1               | 1               | 11 | LDAEXD             |

## F3.1.15.4 Load/store dual (immediate, post-indexed)

This section describes the encoding of the Load/store dual (immediate, post-indexed) instruction class. The encodings in this section are decoded from Load/store dual, load/store exclusive, load-acquire/store-release, and table branch.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15   | 12 11   | 8 7   | 0    |
|---------------------------------|--------|---------|-------|------|
| 1 1 1 0 1 0 0 0 U 1 1 L         | !=1111 | Rt      | Rt2   | imm8 |

## Table F3-67

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STRD (immediate)   |
| 1               | LDRD(immediate)    |

## F3.1.15.5 Load/store dual (immediate)

This section describes the encoding of the Load/store dual (immediate) instruction class. The encodings in this section are decoded from Load/store dual, load/store exclusive, load-acquire/store-release, and table branch.

Rn

<!-- image -->

## Table F3-68

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STRD (immediate)   |
| 1               | LDRD(immediate)    |

## F3.1.15.6 Load/store dual (immediate, pre-indexed)

This section describes the encoding of the Load/store dual (immediate, pre-indexed) instruction class. The encodings in this section are decoded from Load/store dual, load/store exclusive, load-acquire/store-release, and table branch.

<!-- image -->

## Table F3-69

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| L               |                    |
| 0               | STRD (immediate)   |
| 1               | LDRD(immediate)    |

## F3.1.16 Branches and miscellaneous control

This section describes the encoding of the Branches and miscellaneous control group. The encodings in this section are decoded from 32-bit.

<!-- image -->

Table F3-70 Encoding table for the Branches and miscellaneous control group

| Decode fields   | Decode fields   |     |     |        |     | Decode group or instruction page   |
|-----------------|-----------------|-----|-----|--------|-----|------------------------------------|
| op0             | op1             | op2 | op3 | op4    | op5 | Decode group or instruction page   |
| 0               | 1110            | 0x  | 0x0 | xxx    | 0   | MSR(register)                      |
| 0               | 1110            | 0x  | 0x0 | xxx    | 1   | MSR(Banked register)               |
| 0               | 1110            | 10  | 0x0 | 000    | x   | Hints                              |
| 0               | 1110            | 10  | 0x0 | != 000 | x   | Change processor state             |
| 0               | 1110            | 11  | 0x0 | xxx    | x   | Miscellaneous system               |
| 0               | 1111            | 00  | 0x0 | xxx    | x   | BXJ                                |
| 0               | 1111            | 01  | 0x0 | xxx    | x   | Exception return                   |
| 0               | 1111            | 1x  | 0x0 | xxx    | 0   | MRS                                |
| 0               | 1111            | 1x  | 0x0 | xxx    | 1   | MRS(Banked register)               |
| 1               | 1110            | 00  | 000 | xxx    | x   | DCPS                               |
| 1               | 1110            | 00  | 010 | xxx    | x   | Unallocated.                       |
| 1               | 1110            | 01  | 0x0 | xxx    | x   | Unallocated.                       |
| 1               | 1110            | 1x  | 0x0 | xxx    | x   | Unallocated.                       |
| 1               | 1111            | 0x  | 0x0 | xxx    | x   | Unallocated.                       |
| 1               | 1111            | 1x  | 0x0 | xxx    | x   | Exception generation               |
| x               | != 111x         | x   | 0x0 | xxx    | x   | B- T3 variant                      |
| x               | xxxx            | x   | 0x1 | xxx    | x   | B- T4 variant                      |
| x               | xxxx            | x   | 1x0 | xxx    | x   | BL, BLX(immediate) - T2 variant    |
| x               | xxxx            | x   | 1x1 | xxx    | x   | BL, BLX(immediate) - T1 variant    |

## F3.1.16.1 Hints

This section describes the encoding of the Hints instruction class. The encodings in this section are decoded from Branches and miscellaneous control.

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 15 14 13 12 11 10 9 8 7   | 4 3   | 0      |
|-----------------------------------------------------------------|-------|--------|
| 1 1 1 1 0 0 1 1 1 0 1 0 (1) (1) (1) (1) 1 0 (0) 0 (0) 0 0 0     | hint  | option |

| Decode fields   |        | Instruction page               | Feature     |
|-----------------|--------|--------------------------------|-------------|
| hint            | option |                                |             |
| 0000            | 0000   | NOP                            | -           |
| 0000            | 0001   | YIELD                          | -           |
| 0000            | 0010   | WFE                            | -           |
| 0000            | 0011   | WFI                            | -           |
| 0000            | 0100   | SEV                            | -           |
| 0000            | 0101   | SEVL                           | -           |
| 0000            | 011x   | Reserved hint, behaves as NOP. | -           |
| 0000            | 1xxx   | Reserved hint, behaves as NOP. | -           |
| 0001            | 0000   | ESB                            | FEAT_RAS    |
| 0001            | 0001   | Reserved hint, behaves as NOP. | -           |
| 0001            | 0010   | TSB                            | FEAT_TRF    |
| 0001            | 0011   | Reserved hint, behaves as NOP. | -           |
| 0001            | 0100   | CSDB                           | -           |
| 0001            | 0101   | Reserved hint, behaves as NOP. | -           |
| 0001            | 0110   | CLRBHB                         | FEAT_CLRBHB |
| 0001            | 0111   | Reserved hint, behaves as NOP. | -           |
| 0001            | 1xxx   | Reserved hint, behaves as NOP. | -           |
| 001x            | xxxx   | Reserved hint, behaves as NOP. | -           |
| 01xx            | xxxx   | Reserved hint, behaves as NOP. | -           |
| 10xx            | xxxx   | Reserved hint, behaves as NOP. | -           |
| 110x            | xxxx   | Reserved hint, behaves as NOP. | -           |
| 1110            | xxxx   | Reserved hint, behaves as NOP. | -           |
| 1111            | xxxx   | DBG                            | -           |

## F3.1.16.2 Change processor state

This section describes the encoding of the Change processor state instruction class. The encodings in this section are decoded from Branches and miscellaneous control.

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 15 14 13 12 11 10 9 8 7 6 5   | 0    |
|---------------------------------------------------------------------|------|
| 1 1 1 1 0 0 1 1 1 0 1 0 (1) (1) (1) (1) 1 0 (0) 0 (0) imod M A I F  | mode |

|   Decode fields |    | Instruction page                                              |
|-----------------|----|---------------------------------------------------------------|
|              00 | 1  | CPS, CPSID, CPSIE - Change mode variant                       |
|              01 | x  | Unallocated.                                                  |
|              10 | x  | CPS, CPSID, CPSIE - Interrupt enable and change mode variant  |
|              11 | x  | CPS, CPSID, CPSIE - Interrupt disable and change mode variant |

## F3.1.16.3 Miscellaneous system

This section describes the encoding of the Miscellaneous system instruction class. The encodings in this section are decoded from Branches and miscellaneous control.

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 15 14 13 12 11 10 9 8 7     | 4 3   | 0      |
|-------------------------------------------------------------------|-------|--------|
| 1 1 1 1 0 0 1 1 1 0 1 1 (1) (1) (1) (1) 1 0 (0) 0 (1) (1) (1) (1) | opc   | option |

## Table F3-73

| Decode fields   |         | Instruction page   | Feature   |
|-----------------|---------|--------------------|-----------|
| opc             | option  |                    |           |
| 000x            | xxxx    | Unallocated.       | -         |
| 0010            | xxxx    | CLREX              | -         |
| 0011            | xxxx    | Unallocated.       | -         |
| 0100            | != 0x00 | DSB                | -         |
| 0100            | 0000    | SSBB               | -         |
| 0100            | 0100    | PSSBB              | -         |
| 0101            | xxxx    | DMB                | -         |
| 0110            | xxxx    | ISB                | -         |
| 0111            | xxxx    | SB                 | FEAT_SB   |
| 1xxx            | xxxx    | Unallocated.       | -         |

## F3.1.16.4 Exception return

This section describes the encoding of the Exception return instruction class. The encodings in this section are decoded from Branches and miscellaneous control.

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15 14 13 12 11 10 9 8 7    |      |
|-----------------------------------|------------------------------|------|
| 1 1 1 1 0 0 1 1 1 1 0 1           | Rn 1 0 (0) 0 (1) (1) (1) (1) | imm8 |

Table F3-74

| Decode fields   | Instruction page      |
|-----------------|-----------------------|
| Rn:imm8         |                       |
| != 111000000000 | SUB, SUBS (immediate) |
| 111000000000    | ERET                  |

## F3.1.16.5 DCPS

This section describes the encoding of the DCPS instruction class. The encodings in this section are decoded from Branches and miscellaneous control.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4 3   | 0 15 14 13 12 11   | 2 1 0   |
|-----------------------------------|--------------------|---------|
| 1 1 1 1 0 1 1 1 1 0 0 0           | 1 0 0 0            | opt     |

## Table F3-75

| Decode fields   | imm10         |    | Instruction page   |
|-----------------|---------------|----|--------------------|
| != 1111         | xxxxxxxxxx    | xx | Unallocated.       |
| 1111            | != 0000000000 | xx | Unallocated.       |
| 1111            | 0000000000    | 00 | Unallocated.       |
| 1111            | 0000000000    | 01 | DCPS1              |
| 1111            | 0000000000    | 10 | DCPS2              |
| 1111            | 0000000000    | 11 | DCPS3              |

## F3.1.16.6 Exception generation

This section describes the encoding of the Exception generation instruction class. The encodings in this section are decoded from Branches and miscellaneous control.

| 15 14 13 12 11 10 9 8 7 6 5 4 3 0   | 15 14 13 12 11   |       |
|-------------------------------------|------------------|-------|
| 1 1 1 1 0 1 1 1 1 1 1 o1 imm4       | 1 0 o2 0         | imm12 |

|   Decode fields |   Instruction page |              |
|-----------------|--------------------|--------------|
|               0 |                  0 | HVC          |
|               0 |                  1 | Unallocated. |
|               1 |                  0 | SMC          |
|               1 |                  1 | UDF          |

## F3.1.17 Data-processing (plain binary immediate)

This section describes the encoding of the Data-processing (plain binary immediate) group. The encodings in this section are decoded from 32-bit.

<!-- image -->

Table F3-77 Encoding table for the Data-processing (plain binary immediate) group

|   Decode fields |    | Decode group or instruction page   |
|-----------------|----|------------------------------------|
|               0 | 0x | Data-processing (simple immediate) |
|               0 | 10 | Move Wide (16-bit immediate)       |
|               0 | 11 | Unallocated.                       |
|               1 | xx | Saturate, Bitfield                 |

## F3.1.17.1 Data-processing (simple immediate)

This section describes the encoding of the Data-processing (simple immediate) instruction class. The encodings in this section are decoded from Data-processing (plain binary immediate).

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5   | 0 15 14   | 12 11 8 7   |
|-------------------------------|-----------|-------------|
| 1 1 1 1 0 i 1 0 o1 0 o2       | 0 imm3    | Rd imm8     |

| Decode fields   | Decode fields   | Instruction page                    |
|-----------------|-----------------|-------------------------------------|
| o1              | o2              | Rn                                  |
| 0               | 0               | != 11x1 ADD, ADDS(immediate)        |
| 0               | 0               | 1101 ADD, ADDS(SP plus immediate)   |
| 0               | 0               | 1111 ADR-T3                         |
| 0               | 1               | xxxx Unallocated.                   |
| 1               | 0               | xxxx Unallocated.                   |
| 1               | 1               | != 11x1 SUB, SUBS (immediate)       |
| 1               | 1               | 1101 SUB, SUBS (SP minus immediate) |
| 1               | 1               | 1111 ADR-T2                         |

## F3.1.17.2 Move Wide (16-bit immediate)

This section describes the encoding of the Move Wide (16-bit immediate) instruction class. The encodings in this section are decoded from Data-processing (plain binary immediate).

| 15 14 13 12 11 10 9   | 4 3 0            | 15 14 12 11 8 7   |
|-----------------------|------------------|-------------------|
| 1 1 1 1 0 i 1         | 0 imm4 0 imm3 Rd | imm8              |

## Table F3-79

| Decode fields   | Instruction page     |
|-----------------|----------------------|
| o1              |                      |
| 0               | MOV, MOVS(immediate) |
| 1               | MOVT                 |

## F3.1.17.3 Saturate, Bitfield

This section describes the encoding of the Saturate, Bitfield instruction class. The encodings in this section are decoded from Data-processing (plain binary immediate).

| 15 14 13 12 11 10 9 8   | 5 4   |   3 | 0   |   15 14 | 12 11   | 8 7   | 6 5 4    | 0       |
|-------------------------|-------|-----|-----|---------|---------|-------|----------|---------|
| 1 1 1 1 0 (0) 1 1       | op1   |   0 | Rn  |       0 | imm3    | Rd    | imm2 (0) | widthm1 |

| Decode fields   | Decode fields   | Instruction page   |                                       |
|-----------------|-----------------|--------------------|---------------------------------------|
| op1             | Rn              | imm3:imm2          |                                       |
| 000             | xxxx            | xxxxx              | SSAT - Logical shift left variant     |
| 001             | xxxx            | != 00000           | SSAT - Arithmetic shift right variant |
| 001             | xxxx            | 00000              | SSAT16                                |
| 010             | xxxx            | xxxxx              | SBFX                                  |
| 011             | != 1111         | xxxxx              | BFI                                   |
| 011             | 1111            | xxxxx              | BFC                                   |
| 100             | xxxx            | xxxxx              | USAT - Logical shift left variant     |
| 101             | xxxx            | != 00000           | USAT - Arithmetic shift right variant |
| 101             | xxxx            | 00000              | USAT16                                |
| 110             | xxxx            | xxxxx              | UBFX                                  |
| 111             | xxxx            | xxxxx              | Unallocated.                          |

## F3.1.18 Advanced SIMD element or structure load/store

This section describes the encoding of the Advanced SIMD element or structure load/store group. The encodings in this section are decoded from 32-bit.

This group has encodings in both the T32 and A32 instruction sets. For information about mappings between the encodings of this group, see About the T32 Advanced SIMD and floating-point instructions and their encoding

<!-- image -->

Table F3-81 Encoding table for the Advanced SIMD element or structure load/store group

| Decode fields   | Decode fields   | Decode group or instruction page                      |
|-----------------|-----------------|-------------------------------------------------------|
| op0             | op1             | Decode group or instruction page                      |
| 0               | xx              | Advanced SIMD load/store multiple structures          |
| 1               | 11              | Advanced SIMD load single structure to all lanes      |
| 1               | != 11           | Advanced SIMD load/store single structure to one lane |

## F3.1.18.1 Advanced SIMD load/store multiple structures

This section describes the encoding of the Advanced SIMD load/store multiple structures instruction class. The encodings in this section are decoded from Advanced SIMD element or structure load/store.

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15   | 12 11 8 7 6 5 4 3   |
|---------------------------------|--------|---------------------|
| 1 1 1 1 1 0 0 1 0 D L 0         | Rn     | itype size align Rm |

## Table F3-82

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

## F3.1.18.2 Advanced SIMD load single structure to all lanes

This section describes the encoding of the Advanced SIMD load single structure to all lanes instruction class. The encodings in this section are decoded from Advanced SIMD element or structure load/store.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5   | 0 15   | 12 11 10 9 8 7 6 5 4 3   |
|-------------------------------|--------|--------------------------|
| 1 1 1 1 1 0 0 1 1 D L         | Rn     | 1 1 N size T a Rm        |

## Table F3-83

| Decode fields   | Decode fields   | Instruction page   | Instruction page   | Instruction page                   |
|-----------------|-----------------|--------------------|--------------------|------------------------------------|
| L               | N               | a                  | Rm                 |                                    |
| 0               | x               | x                  | xxxx               | Unallocated.                       |
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

## F3.1.18.3 Advanced SIMD load/store single structure to one lane

This section describes the encoding of the Advanced SIMD load/store single structure to one lane instruction class. The encodings in this section are decoded from Advanced SIMD element or structure load/store.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15   | 12 11 10 9 8 7 4 3    |
|---------------------------------|--------|-----------------------|
| 1 1 1 1 1 0 0 1 1 D L 0         | Rn     | !=11 N index_align Rm |

## Table F3-84

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

## F3.1.19 Load/store single

This section describes the encoding of the Load/store single group. The encodings in this section are decoded from 32-bit.

<!-- image -->

This decode also imposes the constraint:

- op0&lt;1&gt;:op1 != 10 .

## Table F3-85 Encoding table for the Load/store single group

| Decode fields   | Decode fields   |         |        | Decode group or instruction page               |
|-----------------|-----------------|---------|--------|------------------------------------------------|
| op0             | op1             | op2     | op3    |                                                |
| 00              | x               | != 1111 | 000000 | Load/store, unsigned (register offset)         |
| 00              | x               | != 1111 | 000001 | Unallocated.                                   |
| 00              | x               | != 1111 | 00001x | Unallocated.                                   |
| 00              | x               | != 1111 | 0001xx | Unallocated.                                   |
| 00              | x               | != 1111 | 001xxx | Unallocated.                                   |
| 00              | x               | != 1111 | 01xxxx | Unallocated.                                   |
| 00              | x               | != 1111 | 10x0xx | Unallocated.                                   |
| 00              | x               | != 1111 | 10x1xx | Load/store, unsigned (immediate, post-indexed) |
| 00              | x               | != 1111 | 1100xx | Load/store, unsigned (negative immediate)      |
| 00              | x               | != 1111 | 1110xx | Load/store, unsigned (unprivileged)            |
| 00              | x               | != 1111 | 11x1xx | Load/store, unsigned (immediate, pre-indexed)  |
| 01              | x               | != 1111 | xxxxxx | Load/store, unsigned (positive immediate)      |
| 0x              | x               | 1111    | xxxxxx | Load, unsigned (literal)                       |
| 10              | 1               | != 1111 | 000000 | Load/store, signed (register offset)           |
| 10              | 1               | != 1111 | 000001 | Unallocated.                                   |
| 10              | 1               | != 1111 | 00001x | Unallocated.                                   |
| 10              | 1               | != 1111 | 0001xx | Unallocated.                                   |
| 10              | 1               | != 1111 | 001xxx | Unallocated.                                   |
| 10              | 1               | != 1111 | 01xxxx | Unallocated.                                   |
| 10              | 1               | != 1111 | 10x0xx | Unallocated.                                   |
| 10              | 1               | != 1111 | 10x1xx | Load/store, signed (immediate, post-indexed)   |
| 10              | 1               | != 1111 | 1100xx | Load/store, signed (negative immediate)        |
| 10              | 1               | != 1111 | 1110xx | Load/store, signed (unprivileged)              |
| 10              | 1               | != 1111 | 11x1xx | Load/store, signed (immediate, pre-indexed)    |
| 11              | 1               | != 1111 | xxxxxx | Load/store, signed (positive immediate)        |
| 1x              | 1               | 1111    | xxxxxx | Load, signed (literal)                         |

## F3.1.19.1 Load/store, unsigned (register offset)

This section describes the encoding of the Load/store, unsigned (register offset) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| Decode fields   | Decode fields   | Instruction page                            |
|-----------------|-----------------|---------------------------------------------|
| size            | L Rt            |                                             |
| 00              | 0 xxxx          | STRB (register)                             |
| 00              | 1 !=            | LDRB(register)                              |
| 00              | 1 1111          | PLD, PLDW(register) - Preload read variant  |
| 01              | 0 xxxx          | STRH (register)                             |
| 01              | 1 !=            | LDRH(register)                              |
| 01              | 1 1111          | PLD, PLDW(register) - Preload write variant |
| 10              | 0 xxxx          | STR (register)                              |
| 10              | 1 xxxx          | LDR(register)                               |
| 11              | x xxxx          | Unallocated.                                |

## F3.1.19.2 Load/store, unsigned (immediate, post-indexed)

This section describes the encoding of the Load/store, unsigned (immediate, post-indexed) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

## Table F3-87

|   Decode fields | Instruction page   |
|-----------------|--------------------|
|              00 | STRB (immediate)   |
|              00 | LDRB(immediate)    |
|              01 | STRH (immediate)   |
|              01 | LDRH(immediate)    |
|              10 | STR (immediate)    |
|              10 | LDR(immediate)     |
|              11 | Unallocated.       |

## F3.1.19.3 Load/store, unsigned (negative immediate)

This section describes the encoding of the Load/store, unsigned (negative immediate) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

Table F3-88

| Decode fields   | Decode fields   |         | Instruction page                             |
|-----------------|-----------------|---------|----------------------------------------------|
| size            | L               | Rt      |                                              |
| 00              | 0               | xxxx    | STRB (immediate)                             |
| 00              | 1               | != 1111 | LDRB(immediate)                              |
| 00              | 1               | 1111    | PLD, PLDW(immediate) - Preload read variant  |
| 01              | 0               | xxxx    | STRH (immediate)                             |
| 01              | 1               | != 1111 | LDRH(immediate)                              |
| 01              | 1               | 1111    | PLD, PLDW(immediate) - Preload write variant |
| 10              | 0               | xxxx    | STR (immediate)                              |
| 10              | 1               | xxxx    | LDR(immediate)                               |
| 11              | x               | xxxx    | Unallocated.                                 |

## F3.1.19.4 Load/store, unsigned (unprivileged)

This section describes the encoding of the Load/store, unsigned (unprivileged) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

## Table F3-89

|   Decode fields | Instruction page   |
|-----------------|--------------------|
|              00 | STRBT              |
|              00 | LDRBT              |
|              01 | STRHT              |
|              01 | LDRHT              |
|              10 | STRT               |

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| 10              |                    |
|                 | LDRT               |
| 11              | Unallocated.       |

## F3.1.19.5 Load/store, unsigned (immediate, pre-indexed)

This section describes the encoding of the Load/store, unsigned (immediate, pre-indexed) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

## Table F3-90

|   Decode fields | Instruction page   |
|-----------------|--------------------|
|              00 | STRB (immediate)   |
|              00 | LDRB(immediate)    |
|              01 | STRH (immediate)   |
|              01 | LDRH(immediate)    |
|              10 | STR (immediate)    |
|              10 | LDR(immediate)     |
|              11 | Unallocated.       |

## F3.1.19.6 Load/store, unsigned (positive immediate)

This section describes the encoding of the Load/store, unsigned (positive immediate) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| Decode fields   | Decode fields   |         | Instruction page                             |
|-----------------|-----------------|---------|----------------------------------------------|
| size            | L               | Rt      | Instruction page                             |
| 00              | 0               | xxxx    | STRB (immediate)                             |
| 00              | 1               | != 1111 | LDRB(immediate)                              |
| 00              | 1               | 1111    | PLD, PLDW(immediate) - Preload read variant  |
| 01              | 0               | xxxx    | STRH (immediate)                             |
| 01              | 1               | != 1111 | LDRH(immediate)                              |
| 01              | 1               | 1111    | PLD, PLDW(immediate) - Preload write variant |
| 10              | 0               | xxxx    | STR (immediate)                              |
| 10              | 1               | xxxx    | LDR(immediate)                               |

## F3.1.19.7 Load, unsigned (literal)

This section describes the encoding of the Load, unsigned (literal) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 15   | 0     |
|--------------------------------------------|-------|
| 1 1 1 1 1 0 0 0 U size L 1 1 1 1           | imm12 |

## Table F3-92

| Decode fields   | Instruction page   | Rt      |               |
|-----------------|--------------------|---------|---------------|
| 0x              | 1                  | 1111    | PLD (literal) |
| 00              | 1                  | != 1111 | LDRB(literal) |
| 01              | 1                  | != 1111 | LDRH(literal) |
| 10              | 1                  | xxxx    | LDR(literal)  |
| 11              | x                  | xxxx    | Unallocated.  |

## F3.1.19.8 Load/store, signed (register offset)

This section describes the encoding of the Load/store, signed (register offset) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| 15 14 13 12 11 10 9 8 7   |   6 5 4 | 0      | 15   | 12 11 10 9 8 7 6 5 4 3   |
|---------------------------|---------|--------|------|--------------------------|
| 1 1 1 1 1 0 0 1 0 size    |       1 | !=1111 | Rt   | 0 0 0 0 0 0 imm2 Rm      |

Rn

## Table F3-93

| Decode fields   | Instruction   | page                           |
|-----------------|---------------|--------------------------------|
| size 00         | Rt != 1111    | LDRSB (register)               |
| 00              | 1111          | PLI (register)                 |
| 01              | != 1111       | LDRSH (register)               |
| 01              | 1111          | Reserved hint, behaves as NOP. |
| 1x              | xxxx          | Unallocated.                   |

## F3.1.19.9 Load/store, signed (immediate, post-indexed)

This section describes the encoding of the Load/store, signed (immediate, post-indexed) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

## Table F3-94

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| 00              | LDRSB (immediate)  |
| 01              | LDRSH (immediate)  |
| 1x              | Unallocated.       |

## F3.1.19.10 Load/store, signed (negative immediate)

This section describes the encoding of the Load/store, signed (negative immediate) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| Decode fields   | Instruction   | page                           |
|-----------------|---------------|--------------------------------|
| 00              | != 1111       | LDRSB (immediate)              |
| 00              | 1111          | PLI (immediate, literal)       |
| 01              | != 1111       | LDRSH (immediate)              |
| 01              | 1111          | Reserved hint, behaves as NOP. |
| 1x              | xxxx          | Unallocated.                   |

## F3.1.19.11 Load/store, signed (unprivileged)

This section describes the encoding of the Load/store, signed (unprivileged) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

## Table F3-96

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| size 00         | LDRSBT             |
| 01              | LDRSHT             |
| 1x              | Unallocated.       |

## F3.1.19.12 Load/store, signed (immediate, pre-indexed)

This section describes the encoding of the Load/store, signed (immediate, pre-indexed) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| Decode fields   | Instruction page   |
|-----------------|--------------------|
| 00              | LDRSB (immediate)  |
| 01              | LDRSH (immediate)  |
| 1x              | Unallocated.       |

## F3.1.19.13 Load/store, signed (positive immediate)

This section describes the encoding of the Load/store, signed (positive immediate) instruction class. The encodings in this section are decoded from Load/store single.

<!-- image -->

| 15 14 13 12 11 10 9 8 7   | 5 4    | 0 15   | 12 11   |
|---------------------------|--------|--------|---------|
| 1 1 1 1 1 0 0 1 1         | size 1 | Rt     | imm12   |

## Table F3-98

|   Decode fields | Instruction   | page                           |
|-----------------|---------------|--------------------------------|
|              00 | != 1111       | LDRSB (immediate)              |
|              00 | 1111          | PLI (immediate, literal)       |
|              01 | != 1111       | LDRSH (immediate)              |
|              01 | 1111          | Reserved hint, behaves as NOP. |

## F3.1.19.14 Load, signed (literal)

This section describes the encoding of the Load, signed (literal) instruction class. The encodings in this section are decoded from Load/store single.

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1   | 0              | 12 11   | 0     |
|---------------------------------------|----------------|---------|-------|
| 1 1 1 1 1 0 0 1 U                     | size 1 1 1 1 1 | Rt      | imm12 |

| Decode fields   | Instruction   | page                           |
|-----------------|---------------|--------------------------------|
| 00              | != 1111       | LDRSB (literal)                |
| 00              | 1111          | PLI (immediate, literal)       |
| 01              | != 1111       | LDRSH (literal)                |
| 01              | 1111          | Reserved hint, behaves as NOP. |
| 1x              | xxxx          | Unallocated.                   |

## F3.1.20 Data-processing (register)

This section describes the encoding of the Data-processing (register) group. The encodings in this section are decoded from 32-bit.

<!-- image -->

Table F3-100 Encoding table for the Data-processing (register) group

| Decode fields   | Decode fields   |      | Decode group or instruction page                            |
|-----------------|-----------------|------|-------------------------------------------------------------|
| op0             | op1             | op2  | Decode group or instruction page                            |
| 0               | 1111            | 0000 | MOV, MOVS(register-shifted register) - Flag setting variant |
| 0               | 1111            | 0001 | Unallocated.                                                |
| 0               | 1111            | 001x | Unallocated.                                                |
| 0               | 1111            | 01xx | Unallocated.                                                |
| 0               | 1111            | 1xxx | Register extends                                            |
| 1               | 1111            | 0xxx | Parallel add-subtract                                       |
| 1               | 1111            | 10xx | Data-processing (two source registers)                      |
| 1               | 1111            | 11xx | Unallocated.                                                |
| x               | != 1111         | xxxx | Unallocated.                                                |

## F3.1.20.1 Register extends

This section describes the encoding of the Register extends instruction class. The encodings in this section are decoded from Data-processing (register).

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4   | 0 15 14 13 12 11   | 8 7 6 5 4 3     |
|---------------------------------|--------------------|-----------------|
| 1 1 1 1 1 0 1 0 0 op1 U         | 1 1 1 1 Rd         | 1 (0) rotate Rm |

## Table F3-101

| Decode fields   |    |         | Instruction page   |
|-----------------|----|---------|--------------------|
| op1             | U  | Rn      |                    |
| 00              | 0  | != 1111 | SXTAH              |
| 00              | 0  | 1111    | SXTH               |
| 00              | 1  | != 1111 | UXTAH              |
| 00              | 1  | 1111    | UXTH               |
| 01              | 0  | != 1111 | SXTAB16            |
| 01              | 0  | 1111    | SXTB16             |
| 01              | 1  | != 1111 | UXTAB16            |
| 01              | 1  | 1111    | UXTB16             |
| 10              | 0  | != 1111 | SXTAB              |
| 10              | 0  | 1111    | SXTB               |
| 10              | 1  | != 1111 | UXTAB              |
| 10              | 1  | 1111    | UXTB               |
| 11              | x  | xxxx    | Unallocated.       |

## F3.1.20.2 Parallel add-subtract

This section describes the encoding of the Parallel add-subtract instruction class. The encodings in this section are decoded from Data-processing (register).

| 15 14 13 12 11 10 9 8 7   | 6 4   | 0 15 14 13 12   | 11 8 7 6 5 4 3   |
|---------------------------|-------|-----------------|------------------|
| 1 1 1 1 1 0 1 0 1         | op1   | 1 1 1 1         | Rd 0 U H S Rm    |

| Decode fields   |     |     |     | Instruction page   |
|-----------------|-----|-----|-----|--------------------|
| op1 000         | U 0 | H 0 | S 0 | SADD8              |
| 000             | 0   | 0   | 1   | QADD8              |
| 000             | 0   | 1   | 0   | SHADD8             |
| 000             | 0   | 1   | 1   | Unallocated.       |
| 000             | 1   | 0   | 0   | UADD8              |
| 000             | 1   | 0   | 1   | UQADD8             |
| 000             | 1   | 1   | 0   | UHADD8             |
| 000             | 1   | 1   | 1   | Unallocated.       |
| 001             | 0   | 0   | 0   | SADD16             |
| 001             | 0   | 0   | 1   | QADD16             |
| 001             | 0   | 1   | 0   | SHADD16            |
| 001             | 0   | 1   | 1   | Unallocated.       |
| 001             | 1   | 0   | 0   | UADD16             |
| 001             | 1   | 0   | 1   | UQADD16            |
| 001             | 1   | 1   | 0   | UHADD16            |
| 001             | 1   | 1   | 1   | Unallocated.       |
| 010             | 0   | 0   | 0   | SASX               |
| 010             | 0   | 0   | 1   | QASX               |
| 010             | 0   | 1   | 0   | SHASX              |
| 010             | 0   | 1   | 1   | Unallocated.       |
| 010             | 1   | 0   | 0   | UASX               |
| 010             | 1   | 0   | 1   | UQASX              |
| 010             | 1   | 1   | 0   | UHASX              |
| 010             | 1   | 1   | 1   | Unallocated.       |
| 100             | 0   | 0   | 0   | SSUB8              |
| 100             | 0   | 0   | 1   | QSUB8              |
| 100             | 0   | 1   | 0   | SHSUB8             |
| 100             | 0   | 1   | 1   | Unallocated.       |
| 100             | 1   | 0   | 0   | USUB8              |
| 100             | 1   | 0   | 1   | UQSUB8             |
| 100             | 1   | 1   | 0   | UHSUB8             |
| 100             | 1   | 1   | 1   | Unallocated.       |
| 101             | 0   | 0   | 0   | SSUB16             |
| 101             | 0   | 0   | 1   | QSUB16             |
| 101             | 0   | 1   | 0   | SHSUB16            |
| 101             | 0   | 1   | 1   | Unallocated.       |

|   Decode fields | Instruction page   |    | S   |              |
|-----------------|--------------------|----|-----|--------------|
|             101 | 1                  | 0  | 1   | UQSUB16      |
|             101 | 1                  | 1  | 0   | UHSUB16      |
|             101 | 1                  | 1  | 1   | Unallocated. |
|             110 | 0                  | 0  | 0   | SSAX         |
|             110 | 0                  | 0  | 1   | QSAX         |
|             110 | 0                  | 1  | 0   | SHSAX        |
|             110 | 0                  | 1  | 1   | Unallocated. |
|             110 | 1                  | 0  | 0   | USAX         |
|             110 | 1                  | 0  | 1   | UQSAX        |
|             110 | 1                  | 1  | 0   | UHSAX        |
|             110 | 1                  | 1  | 1   | Unallocated. |
|             111 | x                  | x  | x   | Unallocated. |

## F3.1.20.3 Data-processing (two source registers)

This section describes the encoding of the Data-processing (two source registers) instruction class. The encodings in this section are decoded from Data-processing (register).

| 15 14 13 12 11 10 9 8 7   | 6 4   | 3 0        | 15 14 13 12 11   | 8 7 6 5 4 3   |
|---------------------------|-------|------------|------------------|---------------|
| 1 1 1 1 1 0 1 0 1         | op1   | Rn 1 1 1 1 | Rd               | 1 0 op2 Rm    |

## Table F3-103

| Decode fields   |     | Instruction page   | Feature   |
|-----------------|-----|--------------------|-----------|
| op1             | op2 |                    |           |
| 000             | 00  | QADD               | -         |
| 000             | 01  | QDADD              | -         |
| 000             | 10  | QSUB               | -         |
| 000             | 11  | QDSUB              | -         |
| 001             | 00  | REV                | -         |
| 001             | 01  | REV16              | -         |
| 001             | 10  | RBIT               | -         |
| 001             | 11  | REVSH              | -         |
| 010             | 00  | SEL                | -         |
| 010             | 01  | Unallocated.       | -         |
| 010             | 1x  | Unallocated.       | -         |

| Decode fields   |     | Instruction page          | Feature    |
|-----------------|-----|---------------------------|------------|
| op1             | op2 |                           |            |
| 011             | 00  | CLZ                       | -          |
| 011             | 01  | Unallocated.              | -          |
| 011             | 1x  | Unallocated.              | -          |
| 100             | 00  | CRC32 - CRC32B variant    | FEAT_CRC32 |
| 100             | 01  | CRC32 - CRC32H variant    | FEAT_CRC32 |
| 100             | 10  | CRC32 - CRC32W variant    | FEAT_CRC32 |
| 100             | 11  | CONSTRAINED UNPREDICTABLE | -          |
| 101             | 00  | CRC32C - CRC32CB variant  | FEAT_CRC32 |
| 101             | 01  | CRC32C - CRC32CH variant  | FEAT_CRC32 |
| 101             | 10  | CRC32C - CRC32CW variant  | FEAT_CRC32 |
| 101             | 11  | CONSTRAINED UNPREDICTABLE | -          |
| 11x             | xx  | Unallocated.              | -          |

The behavior of the CONSTRAINED UNPREDICTABLE encodings in this table is described in CONSTRAINED UNPREDICTABLE behavior for T32 and A32 instruction encodings.

## F3.1.21 Multiply, multiply accumulate, and absolute difference

This section describes the encoding of the Multiply, multiply accumulate, and absolute difference group. The encodings in this section are decoded from 32-bit.

<!-- image -->

Table F3-104 Encoding table for the Multiply, multiply accumulate, and absolute difference group

| Decode fields   | Decode group or instruction page   |
|-----------------|------------------------------------|
| op0             |                                    |
| 00              | Multiply and absolute difference   |
| 01              | Unallocated.                       |
| 1x              | Unallocated.                       |

## F3.1.21.1 Multiply and absolute difference

This section describes the encoding of the Multiply and absolute difference instruction class. The encodings in this section are decoded from Multiply, multiply accumulate, and absolute difference.

<!-- image -->

| 15 14 13 12 11 10 9 8 7   | 6 4   | 0 15   | 12 11   | 8 7 6   | 5 4 3   | 0   |
|---------------------------|-------|--------|---------|---------|---------|-----|
| 1 1 1 1 1 0 1 1 0         | op1   | Rn     | Ra      | 0 0     | op2     | Rm  |

## Table F3-105

| Decode fields   | Decode fields   |     | Instruction page                                |
|-----------------|-----------------|-----|-------------------------------------------------|
| op1             | Ra              | op2 | Instruction page                                |
| 000             | != 1111         | 00  | MLA,MLAS                                        |
| 000             | xxxx            | 01  | MLS                                             |
| 000             | xxxx            | 1x  | Unallocated.                                    |
| 000             | 1111            | 00  | MUL,MULS                                        |
| 001             | != 1111         | 00  | SMLABB, SMLABT, SMLATB, SMLATT - SMLABBvariant  |
| 001             | != 1111         | 01  | SMLABB, SMLABT, SMLATB, SMLATT - SMLABTvariant  |
| 001             | != 1111         | 10  | SMLABB, SMLABT, SMLATB, SMLATT - SMLATB variant |
| 001             | != 1111         | 11  | SMLABB, SMLABT, SMLATB, SMLATT - SMLATT variant |
| 001             | 1111            | 00  | SMULBB, SMULBT, SMULTB, SMULTT - SMULBBvariant  |
| 001             | 1111            | 01  | SMULBB, SMULBT, SMULTB, SMULTT - SMULBTvariant  |
| 001             | 1111            | 10  | SMULBB, SMULBT, SMULTB, SMULTT - SMULTB variant |
| 001             | 1111            | 11  | SMULBB, SMULBT, SMULTB, SMULTT - SMULTT variant |
| 010             | != 1111         | 00  | SMLAD, SMLADX-SMLADvariant                      |
| 010             | != 1111         | 01  | SMLAD, SMLADX-SMLADXvariant                     |
| 010             | xxxx            | 1x  | Unallocated.                                    |
| 010             | 1111            | 00  | SMUAD, SMUADX-SMUADvariant                      |
| 010             | 1111            | 01  | SMUAD, SMUADX-SMUADXvariant                     |
| 011             | != 1111         | 00  | SMLAWB, SMLAWT-SMLAWBvariant                    |
| 011             | != 1111         | 01  | SMLAWB, SMLAWT-SMLAWTvariant                    |
| 011             | xxxx            | 1x  | Unallocated.                                    |
| 011             | 1111            | 00  | SMULWB, SMULWT-SMULWBvariant                    |
| 011             | 1111            | 01  | SMULWB, SMULWT-SMULWTvariant                    |
| 100             | != 1111         | 00  | SMLSD,SMLSDX- SMLSDvariant                      |
| 100             | != 1111         | 01  | SMLSD,SMLSDX- SMLSDXvariant                     |
| 100             | xxxx            | 1x  | Unallocated.                                    |
| 100             | 1111            | 00  | SMUSD, SMUSDX-SMUSDvariant                      |
| 100             | 1111            | 01  | SMUSD, SMUSDX-SMUSDXvariant                     |
| 101             | != 1111         | 00  | SMMLA, SMMLAR-SMMLAvariant                      |
| 101             | != 1111         | 01  | SMMLA, SMMLAR-SMMLARvariant                     |
| 101             | xxxx            | 1x  | Unallocated.                                    |

| Decode fields   | Decode fields   |     | Instruction page            |
|-----------------|-----------------|-----|-----------------------------|
| op1             | Ra              | op2 | Instruction page            |
| 101             | 1111            | 00  | SMMUL, SMMULR-SMMULvariant  |
| 101             | 1111            | 01  | SMMUL, SMMULR-SMMULRvariant |
| 110             | xxxx            | 00  | SMMLS, SMMLSR-SMMLSvariant  |
| 110             | xxxx            | 01  | SMMLS, SMMLSR-SMMLSRvariant |
| 110             | xxxx            | 1x  | Unallocated.                |
| 111             | != 1111         | 00  | USADA8                      |
| 111             | xxxx            | 01  | Unallocated.                |
| 111             | xxxx            | 1x  | Unallocated.                |
| 111             | 1111            | 00  | USAD8                       |