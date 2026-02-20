## F2.4 Data-processing instructions

Core data-processing instructions belong to one of the following groups:

- Standard data-processing instructions.
- Shift instructions.
- Multiply instructions.
- Saturating instructions.
- Saturating addition and subtraction instructions.
- Packing and unpacking instructions.
- Parallel addition and subtraction instructions.
- Divide instructions.
- Miscellaneous data-processing instructions.

For related Advanced SIMD and floating-point instructions see Advanced SIMD data-processing instructions and Floating-point data-processing instructions.

## F2.4.1 Standard data-processing instructions

These instructions perform basic data-processing operations, and share a common format with some variations.

These instructions generally have a destination register Rd, a first operand register Rn, and a second operand. The second operand can be another register Rm, or an immediate constant.

If the second operand is an immediate constant, it can be:

- Encoded directly in the instruction.
- A modified immediate constant that uses 12 bits of the instruction to encode a range of constants. T32 and A32 instructions have slightly different ranges of modified immediate constants. For more information, see Modified immediate constants in T32 instructions and Modified immediate constants in A32 instructions.

If the second operand is another register, it can optionally be shifted in any of the following ways:

| LSL   | Logical Shift Left by 1-31 bits.                                        |
|-------|-------------------------------------------------------------------------|
| LSR   | Logical Shift Right by 1-32 bits.                                       |
| ASR   | Arithmetic Shift Right by 1-32 bits.                                    |
| ROR   | Rotate Right by 1-31 bits.                                              |
| RRX   | Rotate Right with Extend. For details, see Shift and rotate operations. |

In T32 code, the amount to shift by is always a constant encoded in the instruction. In A32 code, the amount to shift by is either a constant encoded in the instruction, or the value of a register, Rs.

For instructions other than CMN , CMP , TEQ , and TST , the result of the data-processing operation is placed in the destination register. In the A32 instruction set, the destination register can be the PC, causing the result to be treated as a branch address. In the T32 instruction set, this is only permitted for some 16-bit forms of the ADD and MOV instructions.

These instructions can optionally set the Condition flags, according to the result of the operation. If they do not set the flags, existing flag settings from a previous instruction are preserved.

Table F2-2 summarizes the main data-processing instructions in the T32 and A32 instruction sets. Generally, each of these instructions is described in three sections in About the T32 and A32 Instruction Descriptions, one section for each of the following:

- INSTRUCTION (immediate) where the second operand is a modified immediate constant.
- INSTRUCTION (register) where the second operand is a register, or a register shifted by a constant.
- INSTRUCTION (register-shifted register) where the second operand is a register shifted by a value obtained from another register. These are only available in the A32 instruction set.

## Table F2-2 Standard data-processing instructions

| Instruction                 | Mnemonic   | Notes                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add with Carry              | ADC        | -                                                                                                                                                                                                                                                                                                                                                                          |
| Add                         | ADD        | T32 instruction set permits use of a modified immediate constant or a zero-extended 12-bit immediate constant.                                                                                                                                                                                                                                                             |
| Form PC-relative Address    | ADR        | First operand is the PC. Second operand is an immediate constant. T32 instruction set uses a zero-extended 12-bit immediate constant. Operation is an addition or a subtraction.                                                                                                                                                                                           |
| BitwiseAND                  | AND        | -                                                                                                                                                                                                                                                                                                                                                                          |
| Bitwise Bit Clear           | BIC        | -                                                                                                                                                                                                                                                                                                                                                                          |
| Compare Negative            | CMN        | Sets flags. Like ADD but with no destination register.                                                                                                                                                                                                                                                                                                                     |
| Compare                     | CMP        | Sets flags. Like SUB but with no destination register.                                                                                                                                                                                                                                                                                                                     |
| Bitwise ExclusiveOR         | EOR        | -                                                                                                                                                                                                                                                                                                                                                                          |
| Copy operand to destination | MOV        | Has only one operand, with the same options as the second operand in most of these instructions. If the operand is a shifted register, the instruction is an LSL , LSR , ASR , or ROR instruction instead. For details, see Shift instructions. The T32 and A32 instruction sets permit use of a modified immediate constant or a zero-extended 16-bit immediate constant. |
| BitwiseNOT                  | MVN        | Has only one operand, with the same options as the second operand in most of these instructions.                                                                                                                                                                                                                                                                           |
| BitwiseORNOT                | ORN        | Not available in the A32 instruction set.                                                                                                                                                                                                                                                                                                                                  |
| BitwiseOR                   | ORR        | -                                                                                                                                                                                                                                                                                                                                                                          |
| Reverse Subtract            | RSB        | Subtracts first operand from second operand. This permits subtraction from constants and shifted registers.                                                                                                                                                                                                                                                                |
| Reverse Subtract with Carry | RSC        | Not available in the T32 instruction set.                                                                                                                                                                                                                                                                                                                                  |
| Subtract with Carry         | SBC        | -                                                                                                                                                                                                                                                                                                                                                                          |
| Subtract                    | SUB        | T32 instruction set permits use of a modified immediate constant or a zero-extended 12-bit immediate constant.                                                                                                                                                                                                                                                             |
| Test Equivalence            | TEQ        | Sets flags. Like EOR but with no destination register.                                                                                                                                                                                                                                                                                                                     |
| Test                        | TST        | Sets flags. Like AND but with no destination register.                                                                                                                                                                                                                                                                                                                     |

## F2.4.2 Shift instructions

Table F2-3 lists the shift instructions in the T32 and A32 instruction sets.

## Table F2-3 Shift instructions

| Instruction            | See                                                             |
|------------------------|-----------------------------------------------------------------|
| Arithmetic Shift Right | ASR (immediate) ASR (register) ASRS (immediate) ASRS (register) |

| Instruction              | See                                                             |
|--------------------------|-----------------------------------------------------------------|
| Logical Shift Left       | LSL (immediate) LSL (register) LSLS (immediate) LSLS (register) |
| Logical Shift Right      | LSR (immediate) LSR (register) LSRS (immediate) LSRS (register) |
| Rotate Right             | ROR(immediate) ROR(register) RORS (immediate) RORS (register)   |
| Rotate Right with Extend | RRX RRXS                                                        |

In the A32 instruction set only, the destination register of these instructions can be the PC, causing the result to be treated as an address to branch to.

## F2.4.3 Multiply instructions

These instructions can operate on signed or unsigned quantities. In some types of operation, the results are the same whether the operands are signed or unsigned.

- Table F2-4 summarizes the multiply instructions where there is no distinction between signed and unsigned quantities.

The least significant 32 bits of the result are used. More significant bits are discarded.

- Table F2-5 summarizes the signed multiply instructions.
- Table F2-6 summarizes the unsigned multiply instructions.

## Table F2-4 General multiply instructions

| Instruction           | See      | Operation (number of bits)   |
|-----------------------|----------|------------------------------|
| Multiply Accumulate   | MLA,MLAS | 32 = 32 + 32 × 32            |
| Multiply and Subtract | MLS      | 32 = 32 - 32 × 32            |
| Multiply              | MUL,MULS | 32 = 32 × 32                 |

## Table F2-5 Signed multiply instructions

| Instruction                            | See                            | Operation (number of bits)   |
|----------------------------------------|--------------------------------|------------------------------|
| Signed Multiply Accumulate (halfwords) | SMLABB, SMLABT, SMLATB, SMLATT | 32 = 32 + 16 × 16            |
| Signed Multiply Accumulate Dual        | SMLAD,SMLADX                   | 32 = 32 + 16 × 16 + 16 × 16  |
| Signed Multiply Accumulate Long        | SMLAL, SMLALS                  | 64 = 64 + 32 × 32            |

| Instruction                                      | See                                | Operation (number of bits)   |
|--------------------------------------------------|------------------------------------|------------------------------|
| Signed Multiply Accumulate Long (halfwords)      | SMLALBB, SMLALBT, SMLALTB, SMLALTT | 64 = 64 + 16 × 16            |
| Signed Multiply Accumulate Long Dual             | SMLALD,SMLALDX                     | 64 = 64 + 16 × 16 + 16 × 16  |
| Signed Multiply Accumulate (word by halfword)    | SMLAWB,SMLAWT                      | 32 = 32 + 32 × 16 a          |
| Signed Multiply Subtract Dual                    | SMLSD,SMLSDX                       | 32 = 32 + 16 × 16 - 16 × 16  |
| Signed Multiply Subtract Long Dual               | SMLSLD,SMLSLDX                     | 64 = 64 + 16 × 16 - 16 × 16  |
| Signed Most Significant Word Multiply Accumulate | SMMLA,SMMLAR                       | 32 = 32 + 32 × 32 b          |
| Signed Most Significant Word Multiply Subtract   | SMMLS,SMMLSR                       | 32 = 32 - 32 × 32 b          |
| Signed Most Significant Word Multiply            | SMMUL,SMMULR                       | 32 = 32 × 32 b               |
| Signed Dual Multiply Add                         | SMUAD,SMUADX                       | 32 = 16 × 16 + 16 × 16       |
| Signed Multiply (halfwords)                      | SMULBB, SMULBT, SMULTB, SMULTT     | 32 = 16 × 16                 |
| Signed Multiply Long                             | SMULL, SMULLS                      | 64 = 32 × 32                 |
| Signed Multiply (word by halfword)               | SMULWB,SMULWT                      | 32 = 32 × 16 a               |
| Signed Dual Multiply Subtract                    | SMUSD,SMUSDX                       | 32 = 16 × 16 - 16 × 16       |

## Table F2-6 Unsigned multiply instructions

| Instruction                                  | See          | Operation (number of bits)   |
|----------------------------------------------|--------------|------------------------------|
| Unsigned Multiply Accumulate Accumulate Long | UMAAL        | 64 = 32 + 32 + 32 × 32       |
| Unsigned Multiply Accumulate Long            | UMLAL,UMLALS | 64 = 64 + 32 × 32            |
| Unsigned Multiply Long                       | UMULL,UMULLS | 64 = 32 × 32                 |

## F2.4.4 Saturating instructions

Table F2-7 lists the saturating instructions in the T32 and A32 instruction sets. For more information, see Pseudocode description of saturation.

## Table F2-7 Saturating instructions

| Instruction          | See    | Operation                                                   |
|----------------------|--------|-------------------------------------------------------------|
| Signed Saturate      | SSAT   | Saturates optionally shifted 32-bit value to selected range |
| Signed Saturate 16   | SSAT16 | Saturates two 16-bit values to selected range               |
| Unsigned Saturate    | USAT   | Saturates optionally shifted 32-bit value to selected range |
| Unsigned Saturate 16 | USAT16 | Saturates two 16-bit values to selected range               |

## F2.4.5 Saturating addition and subtraction instructions

Table F2-8 lists the saturating addition and subtraction instructions in the T32 and A32 instruction sets. For more information, see Pseudocode description of saturation.

Table F2-8 Saturating addition and subtraction instructions

| Instruction                    | See   | Operation                                                                                                                                      |
|--------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Saturating Add                 | QADD  | Add, saturating result to the 32-bit signed integer range                                                                                      |
| Saturating Subtract            | QSUB  | Subtract, saturating result to the 32-bit signed integer range                                                                                 |
| Saturating Double and Add      | QADD  | Doubles one value and adds a second value, saturating the doubling and the addition to the 32-bit signed integer range                         |
| Saturating Double and Subtract | QDSUB | Doubles one value and subtracts the result from a second value, saturating the doubling and the subtraction to the 32-bit signed integer range |

## F2.4.6 Packing and unpacking instructions

Table F2-9 lists the packing and unpacking instructions in the T32 and A32 instruction sets.

## Table F2-9 Packing and unpacking instructions

| Instruction                    | See          | Operation                        |
|--------------------------------|--------------|----------------------------------|
| Pack Halfword                  | PKHBT, PKHTB | Combine halfwords                |
| Signed Extend and Add Byte     | SXTAB        | Extend 8 bits to 32 and add      |
| Signed Extend and Add Byte 16  | SXTAB16      | Dual extend 8 bits to 16 and add |
| Signed Extend and Add Halfword | SXTAH        | Extend 16 bits to 32 and add     |
| Signed Extend Byte             | SXTB         | Extend 8 bits to 32              |

| Instruction                      | See     | Operation                        |
|----------------------------------|---------|----------------------------------|
| Signed Extend Byte 16            | SXTB16  | Dual extend 8 bits to 16         |
| Signed Extend Halfword           | SXTH    | Extend 16 bits to 32             |
| Unsigned Extend and Add Byte     | UXTAB   | Extend 8 bits to 32 and add      |
| Unsigned Extend and Add Byte 16  | UXTAB16 | Dual extend 8 bits to 16 and add |
| Unsigned Extend and Add Halfword | UXTAH   | Extend 16 bits to 32 and add     |
| Unsigned Extend Byte             | UXTB    | Extend 8 bits to 32              |
| Unsigned Extend Byte 16          | UXTB16  | Dual extend 8 bits to 16         |
| Unsigned Extend Halfword         | UXTH    | Extend 16 bits to 32             |

## F2.4.7 Parallel addition and subtraction instructions

These instructions perform additions and subtractions on the values of two registers and write the result to a destination register, treating the register values as sets of two halfwords or four bytes. That is, they perform SIMD additions or subtractions on the general-purpose registers.

These instructions consist of a prefix followed by a main instruction mnemonic. The prefixes are as follows:

| S   | Signed arithmetic modulo 2 8 or 2 16 .    |
|-----|-------------------------------------------|
| Q   | Signed saturating arithmetic.             |
| SH  | Signed arithmetic, halving the results.   |
| U   | Unsigned arithmetic modulo 2 8 or 2 16 .  |
| UQ  | Unsigned saturating arithmetic.           |
| UH  | Unsigned arithmetic, halving the results. |

The main instruction mnemonics are as follows:

| ADD16   | Adds the top halfwords of two operands to form the top halfword of the result, and the bottom halfwords of the same two operands to form the bottom halfword of the result.   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASX     | Exchanges halfwords of the second operand, and then adds top halfwords and subtracts bottom halfwords.                                                                        |
| SAX     | Exchanges halfwords of the second operand, and then subtracts top halfwords and adds bottom halfwords.                                                                        |
| SUB16   | Subtracts each halfword of the second operand from the corresponding halfword of the first operand to form the corresponding halfword of the result.                          |
| ADD8    | Adds each byte of the second operand to the corresponding byte of the first operand to form the corresponding byte of the result.                                             |
| SUB8    | Subtracts each byte of the second operand from the corresponding byte of the first operand to form the corresponding byte of the result.                                      |

The instruction set permits all 36 combinations of prefix and main instruction operand, as Table F2-10 shows.

See also Advanced SIMD parallel addition and subtraction.

## Table F2-10 Parallel addition and subtraction instructions

| Main instruction                     | Signed   | Saturating   | Signed halving   | Unsigned   | Unsigned saturating   | Unsigned halving   |
|--------------------------------------|----------|--------------|------------------|------------|-----------------------|--------------------|
| ADD16 , add, two halfwords           | SADD16   | QADD16       | SHADD16          | UADD16     | UQADD16               | UHADD16            |
| ASX , add and subtract with exchange | SASX     | QASX         | SHASX            | UASX       | UQASX                 | UHASX              |
| SAX , subtract and add with exchange | SSAX     | QSAX         | SHSAX            | USAX       | UQSAX                 | UHSAX              |
| SUB16 , subtract, two halfwords      | SSUB16   | QSUB16       | SHSUB16          | USUB16     | UQSUB16               | UHSUB16            |
| ADD8 , add, four bytes               | SADD8    | QADD8        | SHADD8           | UADD8      | UQADD8                | UHADD8             |
| SUB8 , subtract, four bytes          | SSUB8    | QSUB8        | SHSUB8           | USUB8      | UQSUB8                | UHSUB8             |

## F2.4.8 Divide instructions

Signed and unsigned integer divide instructions are included in both the T32 instruction set and the A32 instruction set.

For descriptions of the instructions see:

- SDIV.
- UDIV.

For the SDIV and UDIV

instructions, division by zero always returns a zero result.

The ID\_ISAR0.Divide\_instrs field indicates the level of support for these instructions. The field value of 0b0010 indicates they are implemented in both the T32 and A32 instruction sets.

## F2.4.9 Miscellaneous data-processing instructions

Table F2-11 lists the miscellaneous data-processing instructions in the T32 and A32 instruction sets. Immediate values in these instructions are simple binary numbers.

Table F2-11 Miscellaneous data-processing instructions

| Instruction                                         | See    | Notes                                                                    |
|-----------------------------------------------------|--------|--------------------------------------------------------------------------|
| BitField Clear                                      | BFC    | -                                                                        |
| BitField Insert                                     | BFI    | -                                                                        |
| Count Leading Zeros                                 | CLZ    | -                                                                        |
| Move Top                                            | MOVT   | Moves 16-bit immediate value to top halfword. Bottom halfword unchanged. |
| Reverse Bits                                        | RBIT   | -                                                                        |
| Byte-Reverse Word                                   | REV    | -                                                                        |
| Byte-Reverse Packed Halfword                        | REV16  | -                                                                        |
| Byte-Reverse Signed Halfword                        | REVSH  | -                                                                        |
| Signed BitField Extract                             | SBFX   | -                                                                        |
| Select Bytes using GEflags                          | SEL    | -                                                                        |
| Unsigned BitField Extract                           | UBFX   | -                                                                        |
| Unsigned Sum of Absolute Differences                | USAD8  | -                                                                        |
| Unsigned Sum of Absolute Differences and Accumulate | USADA8 | -                                                                        |