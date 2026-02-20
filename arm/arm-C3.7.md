## C3.7 Data processing - register

This section describes the instruction groups for data processing with all register operands. It contains the following subsections:

- Arithmetic (shifted register).
- Arithmetic (extended register).
- Arithmetic with carry.
- Integer maximum and minimum (register)
- Flag manipulation instructions.
- Logical (shifted register).
- Move (register).
- Absolute value
- Shift (register).
- Multiply and divide.
- CRC32.
- Bit operation.
- Conditional select.
- Conditional comparison.

## C3.7.1 Arithmetic (shifted register)

The Arithmetic (shifted register) instructions apply an optional shift operator to the second source register value before performing the arithmetic operation. The register width of the instruction controls whether the new bits are fed into the intermediate result on a right shift or rotate at bit[63] or bit[31].

The shift operators LSL , ASR , and LSR accept an immediate shift amount in the range 0 to one less than the register width of the instruction, inclusive.

Omitting the shift operator implies LSL #0 , which means that there is no shift. A disassembler must not output LSL #0. However, a disassembler must output all other shifts by zero.

The current stack pointer, SP or WSP, cannot be used with this class of instructions. See Arithmetic (extended register) for arithmetic instructions that can operate on the current stack pointer.

Table C3-94 shows the Arithmetic (shifted register) instructions.

Table C3-94 Arithmetic (shifted register) instructions

| Mnemonic   | Instruction            | See                     |
|------------|------------------------|-------------------------|
| ADD        | Add                    | ADD(shifted register)   |
| ADDS       | Add and set flags      | ADDS(shifted register)  |
| SUB        | Subtract               | SUB (shifted register)  |
| SUBS       | Subtract and set flags | SUBS (shifted register) |
| CMN        | Compare negative       | CMN(shifted register)   |
| CMP        | Compare                | CMP(shifted register)   |
| NEG        | Negate                 | NEG(shifted register)   |
| NEGS       | Negate and set flags   | NEGS                    |

## C3.7.2 Arithmetic (extended register)

The extended register instructions provide an optional sign-extension or zero-extension of a portion of the second source register value, followed by an optional left shift by a constant amount of 1-4, inclusive.

The extended shift is described by the mandatory extend operator SXTB , SXTH , SXTW , UXTB , UXTH , or UXTW . This is followed by an optional left shift amount. If the shift amount is not specified, the default shift amount is zero. A disassembler must not output a shift amount of zero.

For 64-bit instruction forms, the additional operators UXTX and SXTX use all 64 bits of the second source register with an optional shift. In that case, Arm recommends UXTX as the operator. If and only if at least one register is SP , Arm recommends use of the LSL operator name, rather than UXTX , and when the shift amount is also zero then both the operator and the shift amount can be omitted. UXTW and SXTW both use all 32 bits of the second source register with an optional shift. In that case Arm recommends UXTW as the operator. If and only if at least one register is WSP, Arm recommends use of the LSL operator name, rather than UXTW , and when the shift amount is also zero then both the operator and the shift amount can be omitted.

For 32-bit instruction forms, the operators UXTW and SXTW both use all 32 bits of the second source register with an optional shift. In that case, Arm recommends UXTW as the operator. If and only if at least one register is WSP, Arm recommends use of the LSL operator name, rather than UXTW , and when the shift amount is also zero then both the operator and the shift amount can be omitted.

The non-flag setting variants of the extended register instruction permit the use of the current stack pointer as either the destination register and the first source register. The flag setting variants only permit the stack pointer to be used as the first source register.

In the 64-bit form of these instructions, the final register operand is written as Wm for all except the UXTX / LSL and SXTX extend operators. For example:

| CMP X4, W5, SXTW        |                            |
|-------------------------|----------------------------|
| ADD X1, X2, W3, UXTB #2 |                            |
| SUB SP, SP, X1          | // SUB SP, SP, X1, UXTX #0 |

Table C3-95 shows the Arithmetic (extended register) instructions.

Table C3-95 Arithmetic (extended register) instructions

| Mnemonic   | Instruction            | See                      |
|------------|------------------------|--------------------------|
| ADD        | Add                    | ADD(extended register)   |
| ADDS       | Add and set flags      | ADDS(extended register)  |
| SUB        | Subtract               | SUB (extended register)  |
| SUBS       | Subtract and set flags | SUBS (extended register) |
| CMN        | Compare negative       | CMN(extended register)   |
| CMP        | Compare                | CMP(extended register)   |

## C3.7.3 Arithmetic with carry

The Arithmetic with carry instructions accept two source registers, with the carry flag as an additional input to the calculation. They do not support shifting of the second source register.

Table C3-96 shows the Arithmetic with carry instructions

## Table C3-96 Arithmetic with carry instructions

| Mnemonic   | Instruction                       | See   |
|------------|-----------------------------------|-------|
| ADC        | Add with carry                    | ADC   |
| ADCS       | Add with carry and set flags      | ADCS  |
| SBC        | Subtract with carry               | SBC   |
| SBCS       | Subtract with carry and set flags | SBCS  |
| NGC        | Negate with carry                 | NGC   |
| NGCS       | Negate with carry and set flags   | NGCS  |

## C3.7.4 Integer maximum and minimum (register)

The Integer maximum and minimum (register) instructions determine the maximum/minimum of the two source register values.

These instructions are only present when FEAT\_CSSC is implemented.

Table C3-97 shows the Integer maximum and minimum (register) instructions.

Table C3-97 Integer maximum and minimum (register) instructions

| Mnemonic   | Instruction                 | See             |
|------------|-----------------------------|-----------------|
| SMAX       | Signed Maximum (register)   | SMAX(register)  |
| SMIN       | Signed Minimum (register)   | SMIN (register) |
| UMAX       | Unsigned Maximum (register) | UMAX(register)  |
| UMIN       | Unsigned Minimum (register) | UMIN(register)  |

## C3.7.5 Flag manipulation instructions

The Flag manipulation instructions set the value of the NZCV condition flags directly.

The instructions SETF8 and SETF16 accept one source register and set the NZV condition flags based on the value of the input register. The instruction RMIF accepts one source register and two immediate values, rotating the first source register using the first immediate value and setting the NZCV condition flags masked by the second immediate value.

The instructions XAFLAG and AXFLAG convert PSTATE condition flags between the FCMP instruction format and an alternative format. See Table C6-1 for more information.

Table C3-98 shows the Flag manipulation instructions.

## Table C3-98 Flag manipulation instructions

| Mnemonic   | Instruction                                                  | See           |
|------------|--------------------------------------------------------------|---------------|
| AXFLAG     | Convert from FCMPcomparison format to the alternative format | AXFLAG        |
| CFINV      | Invert value of the PSTATE.C bit                             | CFINV         |
| RMIF       | Rotate, mask insert flags                                    | RMIF          |
| SETF8      | Evaluation of 8-bit flags                                    | SETF8, SETF16 |
| SETF16     | Evaluation of 16-bit flags                                   | SETF8, SETF16 |
| XAFLAG     | Convert from alternative format to FCMPcomparison format     | XAFLAG        |

## C3.7.6 Logical (shifted register)

The Logical (shifted register) instructions apply an optional shift operator to the second source register value before performing the main operation. The register width of the instruction controls whether the new bits are fed into the intermediate result on a right shift or rotate at bit[63] or bit[31].

The shift operators LSL , ASR , LSR , and ROR accept a constant immediate shift amount in the range 0 to one less than the register width of the instruction, inclusive.

Omitting the shift operator and amount implies LSL #0 , which means that there is no shift. A disassembler must not output LSL #0. However, a disassembler must output all other shifts by zero.

Note

Apart from ANDS, TST , and BICS operation can usually directly control a CBZ , CBNZ , TBZ , or TBNZ conditional branch.

, the logical instructions do not set the Condition flags, but the final result of a bit

Table C3-99 shows the Logical (shifted register) instructions.

Table C3-99 Logical (shifted register) instructions

| Mnemonic   | Instruction                     | See                     |
|------------|---------------------------------|-------------------------|
| AND        | BitwiseAND                      | AND(shifted register)   |
| ANDS       | Bitwise ANDand set flags        | ANDS(shifted register)  |
| BIC        | Bitwise bit clear               | BIC (shifted register)  |
| BICS       | Bitwise bit clear and set flags | BICS (shifted register) |
| EON        | Bitwise exclusive-ORNOT         | EON(shifted register)   |
| EOR        | Bitwise exclusive-OR            | EOR(shifted register)   |
| ORR        | Bitwise inclusiveOR             | ORR(shifted register)   |
| MVN        | BitwiseNOT                      | MVN                     |
| ORN        | Bitwise inclusiveORNOT          | ORN(shifted register)   |
| TST        | Test bits                       | TST (shifted register)  |

## C3.7.7 Move (register)

The Move (register) instructions are aliases for other data processing instructions. They copy a value from a general-purpose register to another general-purpose register or the current stack pointer, or from the current stack pointer to a general-purpose register.

## Table C3-100 MOV register instructions

| Mnemonic   | Instruction                                | See             |
|------------|--------------------------------------------|-----------------|
| MOV        | Move register                              | MOV(register)   |
|            | Move register to SP or move SP to register | MOV(to/from SP) |

## C3.7.8 Absolute value

The Absolute value instruction is only present when FEAT\_CSSC is implemented.

Table C3-101 shows the Absolute value instruction.

## Table C3-101 Absolute value instruction

| Mnemonic   | Instruction    | See   |
|------------|----------------|-------|
| ABS        | Absolute value | ABS   |

## C3.7.9 Shift (register)

In the Shift (register) instructions, the shift amount is the positive value in the second source register modulo the register size. The register width of the instruction controls whether the new bits are fed into the result on a right shift or rotate at bit[63] or bit[31].

Table C3-102 shows the Shift (register) instructions.

## Table C3-102 Shift (register) instructions

| Mnemonic   | Instruction                     | See   |
|------------|---------------------------------|-------|
| ASRV       | Arithmetic shift right variable | ASRV  |
| LSLV       | Logical shift left variable     | LSLV  |
| LSRV       | Logical shift right variable    | LSRV  |
| RORV       | Rotate right variable           | RORV  |

However, the Shift (register) instructions have a preferred set of aliases that match the shift immediate aliases described in Shift (immediate).

Table C3-103 shows the aliases for Shift (register) instructions.

Table C3-103 Aliases for Variable shift instructions

| Mnemonic   | Instruction            | See            |
|------------|------------------------|----------------|
| ASR        | Arithmetic shift right | ASR (register) |
| LSL        | Logical shift left     | LSL (register) |
| LSR        | Logical shift right    | LSR (register) |
| ROR        | Rotate right           | ROR(register)  |

## C3.7.10 Multiply and divide

This section describes the instructions used for integer multiplication and division. It contains the following subsections:

- Multiply.
- Divide.

## C3.7.10.1 Multiply

The Multiply instructions write to a single 32-bit or 64-bit destination register, and are built around the fundamental four operand multiply-add and multiply-subtract operation, together with 32-bit to 64-bit widening variants. A 64-bit to 128-bit widening multiple can be constructed with two instructions, using SMULH or UMULH to generate the upper 64 bits. Table C3-104 shows the Multiply instructions.

## Table C3-104 Multiply integer instructions

| Mnemonic   | Instruction                     | See    |
|------------|---------------------------------|--------|
| MADD       | Multiply-add                    | MADD   |
| MSUB       | Multiply-subtract               | MSUB   |
| MNEG       | Multiply-negate                 | MNEG   |
| MUL        | Multiply                        | MUL    |
| SMADDL     | Signed multiply-add long        | SMADDL |
| SMSUBL     | Signed multiply-subtract long   | SMSUBL |
| SMNEGL     | Signed multiply-negate long     | SMNEGL |
| SMULL      | Signed multiply long            | SMULL  |
| SMULH      | Signed multiply high            | SMULH  |
| UMADDL     | Unsigned multiply-add long      | UMADDL |
| UMSUBL     | Unsigned multiply-subtract long | UMSUBL |
| UMNEGL     | Unsigned multiply-negate long   | UMNEGL |
| UMULL      | Unsigned multiply long          | UMULL  |
| UMULH      | Unsigned multiply high          | UMULH  |

## C3.7.10.2 Divide

The Divide instructions compute the quotient of a division, rounded towards zero. The remainder can then be computed as (numerator - (quotient × denominator)), using the MSUB instruction.

If a signed integer division ( INT\_MIN / -1) is performed where INT\_MIN is the most negative integer value representable in the selected register size, then the result overflows the signed integer range. No indication of this overflow is produced and the result that is written to the destination register is INT\_MIN .

Adivision by zero results in a zero being written to the destination register, without any indication that the division by zero occurred.

Table C3-105 shows the Divide instructions.

## Table C3-105 Divide instructions

| Mnemonic   | Instruction     | See   |
|------------|-----------------|-------|
| SDIV       | Signed divide   | SDIV  |
| UDIV       | Unsigned divide | UDIV  |

## C3.7.11 CRC32

The CRC32 instructions operate on the general-purpose register file to update a 32-bit CRC value from an input value comprising 1, 2, 4, or 8 bytes. There are two different classes of CRC instructions, CRC32 , and CRC32C , that support two commonly used 32-bit polynomials, known as CRC-32 and CRC-32C.

To fit with common usage, the bit order of the values is reversed as part of the operation.

When bits[19:16] of ID\_AA64ISAR0\_EL1 are set to 0b0001 , the CRC instructions are implemented.

These instructions are optional in an Armv8.0 implementation.

All implementations of Armv8.1 architecture and later are required to implement the CRC32 instructions.

Table C3-106 shows the CRC instructions.

## Table C3-106 CRC32 instructions

| Mnemonic   | Instruction                 | See                                |
|------------|-----------------------------|------------------------------------|
| CRC32B     | CRC-32 sum from byte        | CRC32B, CRC32H, CRC32W, CRC32X     |
| CRC32H     | CRC-32 sum from halfword    | CRC32B, CRC32H, CRC32W, CRC32X     |
| CRC32W     | CRC-32 sum from word        | CRC32B, CRC32H, CRC32W, CRC32X     |
| CRC32X     | CRC-32 sum from doubleword  | CRC32B, CRC32H, CRC32W, CRC32X     |
| CRC32CB    | CRC-32C sum from byte       | CRC32CB, CRC32CH, CRC32CW, CRC32CX |
| CRC32CH    | CRC-32C sum from halfword   | CRC32CB, CRC32CH, CRC32CW, CRC32CX |
| CRC32CW    | CRC-32C sum from word       | CRC32CB, CRC32CH, CRC32CW, CRC32CX |
| CRC32CX    | CRC-32C sum from doubleword | CRC32CB, CRC32CH, CRC32CW, CRC32CX |

## C3.7.12 Bit operation

The CNT and CTZ instructions are only present when FEAT\_CSSC is implemented.

Table C3-107 shows the Bit operation instructions.

## Table C3-107 Bit operation instructions

| Mnemonic   | Instruction                | See   |
|------------|----------------------------|-------|
| CLS        | Count leading sign bits    | CLS   |
| CLZ        | Count leading zero bits    | CLZ   |
| CNT        | Count bits                 | CNT   |
| CTZ        | Count trailing zero bits   | CTZ   |
| RBIT       | Reverse bit order          | RBIT  |
| REV        | Reverse bytes in register  | REV   |
| REV16      | Reverse bytes in halfwords | REV16 |
| REV32      | Reverse bytes in words     | REV32 |
| REV64      | Reverse bytes in register  | REV64 |

## C3.7.13 Conditional select

The Conditional select instructions select between the first or second source register, depending on the current state of the Condition flags. When the named condition is true, the first source register is selected and its value is copied without modification to the destination register. When the condition is false the second source register is selected and its value might be optionally inverted, negated, or incremented by one, before writing to the destination register.

Other useful conditional set and conditional unary operations are implemented as aliases of the four Conditional select instructions.

Table C3-108 shows the Conditional select instructions.

## Table C3-108 Conditional select instructions

| Mnemonic   | Instruction                  | See   |
|------------|------------------------------|-------|
| CSEL       | Conditional select           | CSEL  |
| CSINC      | Conditional select increment | CSINC |
| CSINV      | Conditional select inversion | CSINV |
| CSNEG      | Conditional select negation  | CSNEG |
| CSET       | Conditional set              | CSET  |
| CSETM      | Conditional set mask         | CSETM |
| CINC       | Conditional increment        | CINC  |
| CINV       | Conditional invert           | CINV  |
| CNEG       | Conditional negate           | CNEG  |

## C3.7.14 Conditional comparison

The Conditional comparison instructions provide a conditional select for the NZCV Condition flags, setting the flags to the result of an arithmetic comparison of its two source register values if the named input condition is true, or to an immediate value if the input condition is false. There are register and immediate forms. The immediate form compares the source register to a small 5-bit unsigned value.

Table C3-109 shows the Conditional comparison instructions.

Table C3-109 Conditional comparison instructions

| Mnemonic   | Instruction                              | See             |
|------------|------------------------------------------|-----------------|
| CCMN       | Conditional compare negative (register)  | CCMN(register)  |
| CCMN       | Conditional compare negative (immediate) | CCMN(immediate) |
| CCMP       | Conditional compare (register)           | CCMP(register)  |
| CCMP       | Conditional compare (immediate)          | CCMP(immediate) |