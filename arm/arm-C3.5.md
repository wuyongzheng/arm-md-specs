## C3.5 Data processing - immediate

This section describes the instruction groups for data processing with immediate operands. It contains the following subsections:

- Arithmetic (immediate).
- Integer minimum and maximum (immediate)
- Logical (immediate).
- Move (wide immediate).
- Move (immediate).
- PC-relative address calculation.
- Bitfield move.
- Bitfield insert and extract
- Extract register.
- Shift (immediate).
- Sign-extend and Zero-extend.

## C3.5.1 Arithmetic (immediate)

The Arithmetic (immediate) instructions accept a 12-bit unsigned immediate value, optionally shifted left by 12 bits.

The Arithmetic (immediate) instructions that do not set Condition flags can read from and write to the current stack pointer. The flag setting instructions can read from the stack pointer, but they cannot write to it.

Table C3-81 shows the Arithmetic instructions with an immediate offset.

Table C3-81 Arithmetic instructions with an immediate

| Mnemonic   | Instruction            | See              |
|------------|------------------------|------------------|
| ADD        | Add                    | ADD(immediate)   |
| ADDS       | Add and set flags      | ADDS(immediate)  |
| SUB        | Subtract               | SUB (immediate)  |
| SUBS       | Subtract and set flags | SUBS (immediate) |
| CMP        | Compare                | CMP(immediate)   |
| CMN        | Compare negative       | CMN(immediate)   |

## C3.5.2 Integer minimum and maximum (immediate)

The Integer maximum and minimum (immediate) instructions determine the maximum/minimum of the source register value and immediate.

These instructions are only present when FEAT\_CSSC is implemented.

Table C3-82 shows the Integer maximum and minimum (immediate) instructions.

## Table C3-82 Integer maximum and minimum (immediate) instructions

| Mnemonic   | Instruction                  | See              |
|------------|------------------------------|------------------|
| SMAX       | Signed Maximum (immediate)   | SMAX(immediate)  |
| SMIN       | Signed Minimum (immediate)   | SMIN (immediate) |
| UMAX       | Unsigned Maximum (immediate) | UMAX(immediate)  |
| UMIN       | Unsigned Minimum (immediate) | UMIN(immediate)  |

## C3.5.3 Logical (immediate)

The Logical (immediate) instructions accept a bitmask immediate value that is a 32-bit pattern or a 64-bit pattern viewed as a vector of identical elements of size e = 2, 4, 8, 16, 32 or, 64 bits. Each element contains the same sub-pattern, that is a single run of 1 to (e - 1) nonzero bits from bit 0 followed by zero bits, then rotated by 0 to (e - 1) bits. This mechanism can generate 5334 unique 64-bit patterns as 2667 pairs of pattern and their bitwise inverse.

Note

Values that consist of only zeros or only ones cannot be described in this way.

The Logical (immediate) instructions that do not set the Condition flags can write to the current stack pointer, for example to align the stack pointer in a function prologue.

Note

Apart from ANDS and its TST alias, Logical (immediate) instructions do not set the Condition flags. However, the final results of a bitwise operation can be tested by a CBZ , CBNZ , TBZ , or TBNZ conditional branch.

Table C3-83 shows the Logical immediate instructions.

## Table C3-83 Logical immediate instructions

| Mnemonic   | Instruction               | See             |
|------------|---------------------------|-----------------|
| AND        | Bitwise AND               | AND(immediate)  |
| ANDS       | Bitwise AND and set flags | ANDS(immediate) |
| EOR        | Bitwise exclusive OR      | EOR(immediate)  |
| ORR        | Bitwise inclusive OR      | ORR(immediate)  |
| TST        | Test bits                 | TST (immediate) |

## C3.5.4 Move (wide immediate)

The Move (wide immediate) instructions insert a 16-bit immediate, or inverted immediate, into a 16-bit aligned position in the destination register. The value of the other bits in the destination register depends on the variant used. The optional shift amount can be any multiple of 16 that is smaller than the register size.

Table C3-84 shows the Move (wide immediate) instructions.

## Table C3-84 Move (wide immediate) instructions

| Mnemonic   | Instruction         | See   |
|------------|---------------------|-------|
| MOVZ       | Move wide with zero | MOVZ  |
| MOVN       | Move wide withNOT   | MOVN  |
| MOVK       | Move wide with keep | MOVK  |

## C3.5.5 Move (immediate)

The Move (immediate) instructions are aliases for a single MOVZ , MOVN , or ORR (immediate with zero register), instruction to load an immediate value into the destination register. An assembler must permit a signed or unsigned immediate, as long as its binary representation can be generated using one of these instructions, and an assembler error results if the immediate cannot be generated in this way. On disassembly, it is unspecified whether the immediate is output as a signed or an unsigned value.

If there is a choice between the MOVZ , MOVN , and ORR instruction to encode the immediate, then an assembler must prefer MOVZ to MOVN , and MOVZ or MOVN to ORR , to ensure reversability. A disassembler must output ORR (immediate with zero register) MOVZ, and MOVN , as a MOV mnemonic except that the underlying instruction must be used when:

- ORR has an immediate that can be generated by a MOVZ or MOVN instruction.
- A MOVN instruction has an immediate that can be encoded by MOVZ .
- MOVZ #0 or MOVN #0 have a shift amount other than LSL #0 .

Table C3-85 shows the Move (immediate) instructions.

Table C3-85 Move (immediate) instructions

| Mnemonic   | Instruction                    | See                          |
|------------|--------------------------------|------------------------------|
| MOV        | Move (inverted wide immediate) | MOV(inverted wide immediate) |
|            | Move (wide immediate)          | MOV(wide immediate)          |
|            | Move (bitmask immediate)       | MOV(bitmask immediate)       |

## C3.5.6 PC-relative address calculation

The ADR instruction adds a signed, 21-bit immediate to the value of the program counter that fetched this instruction, and then writes the result to a general-purpose register. This permits the calculation of any byte address within ±1MB of the current PC.

The ADRP instruction shifts a signed, 21-bit immediate left by 12 bits, adds it to the value of the program counter with the bottom 12 bits cleared to zero, and then writes the result to a general-purpose register. This permits the calculation of the address at a 4KB aligned memory region. In conjunction with an ADD (immediate) instruction, or a load/store instruction with a 12-bit immediate offset, this allows for the calculation of, or access to, any address within ±4GB of the current PC.

Note

The term page used in the ADRP description is short-hand for the 4KB memory region, and is not related to the virtual memory translation granule size.

Table C3-86 shows the instructions used for PC-relative address calculations are as follows:

## Table C3-86 PC-relative address calculation instructions

| Mnemonic   | Instruction                                         | See   |
|------------|-----------------------------------------------------|-------|
| ADRP       | Compute address of 4KB page at a PC-relative offset | ADRP  |
| ADR        | Compute address of label at a PC-relative offset.   | ADR   |

## C3.5.7 Bitfield move

The Bitfield move instructions copy a field of constant width from bit 0 in the source register to a constant bit position in the destination register, or from a constant bit position in the source register to bit 0 in the destination register. The remaining bits in the destination register are set as follows:

- For BFM , the remaining bits are unchanged.
- For UBFM the lower bits, if any, and upper bits, if any, are set to zero.
- For SBFM , the lower bits, if any, are set to zero, and the upper bits, if any, are set to a copy of the most-significant bit in the copied field.

Table C3-87 shows the Bitfield move instructions.

## Table C3-87 Bitfield move instructions

| Mnemonic   | Instruction                     | See   |
|------------|---------------------------------|-------|
| BFM        | Bitfield move                   | BFM   |
| SBFM       | Signed bitfield move            | SBFM  |
| UBFM       | Unsigned bitfield move (32-bit) | UBFM  |

## C3.5.8 Bitfield insert and extract

The Bitfield insert and extract instructions are implemented as aliases of the Bitfield move instructions. Table C3-88 shows the Bitfield insert and extract aliases.

## Table C3-88 Bitfield insert and extract instructions

| Mnemonic   | Instruction                      | See   |
|------------|----------------------------------|-------|
| BFC        | Bitfield clear                   | BFC   |
| BFI        | Bitfield insert                  | BFI   |
| BFXIL      | Bitfield extract and insert low  | BFXIL |
| SBFIZ      | Signed bitfield insert in zero   | SBFIZ |
| SBFX       | Signed bitfield extract          | SBFX  |
| UBFIZ      | Unsigned bitfield insert in zero | UBFIZ |
| UBFX       | Unsigned bitfield extract        | UBFX  |

| Mnemonic   | Instruction   | See   |
|------------|---------------|-------|

## C3.5.9 Extract register

Depending on the register width of the operands, the Extract register instruction copies a 32-bit or 64-bit field from a constant bit position within a double-width value formed by the concatenation of a pair of source registers to a destination register.

Table C3-89 shows the Extract (immediate) instructions.

## Table C3-89 Extract register instructions

| Mnemonic   | Instruction                | See   |
|------------|----------------------------|-------|
| EXTR       | Extract register from pair | EXTR  |

## C3.5.10 Shift (immediate)

Shifts and rotates by a constant amount are implemented as aliases of the Bitfield move or Extract register instructions. The shift or rotate amount must be in the range 0 to one less than the register width of the instruction, inclusive.

Table C3-90 shows the aliases that can be used as immediate shift and rotate instructions.

Table C3-90 Aliases for immediate shift and rotate instructions

| Mnemonic   | Instruction            | See             |
|------------|------------------------|-----------------|
| ASR        | Arithmetic shift right | ASR (immediate) |
| LSL        | Logical shift left     | LSL (immediate) |
| LSR        | Logical shift right    | LSR (immediate) |
| ROR        | Rotate right           | ROR(immediate)  |

## C3.5.11 Sign-extend and Zero-extend

The Sign-extend and Zero-extend instructions are implemented as aliases of the Bitfield move instructions.

Table C3-91 shows the aliases that can be used as zero-extend and sign-extend instructions.

## Table C3-91 Zero-extend and sign-extend instructions

| Mnemonic   | Instruction          | See   |
|------------|----------------------|-------|
| SXTB       | Sign-extend byte     | SXTB  |
| SXTH       | Sign-extend halfword | SXTH  |
| SXTW       | Sign-extend word     | SXTW  |

| Mnemonic   | Instruction              | See   |
|------------|--------------------------|-------|
| UXTB       | Unsigned extend byte     | UXTB  |
| UXTH       | Unsigned extend halfword | UXTH  |