## F1.3 Conditional execution

Most T32 and A32 instructions can be executed conditionally, based on the values of the APSR Condition flags. Table F1-1 lists the available conditions.

Table F1-1 Condition codes

|   cond | Mnemonic extension   | Meaning (integer)            | Meaning (floating-point) a        | Condition flags   |
|--------|----------------------|------------------------------|-----------------------------------|-------------------|
|   0000 | EQ                   | Equal                        | Equal                             | Z == 1            |
|   0001 | NE                   | Not equal                    | Not equal, or unordered           | Z == 0            |
|   0010 | CS b                 | Carry set                    | Greater than, equal, or unordered | C==1              |
|   0011 | CC c                 | Carry clear                  | Less than                         | C==0              |
|   0100 | MI                   | Minus, negative              | Less than                         | N==1              |
|   0101 | PL                   | Plus, positive or zero       | Greater than, equal, or unordered | N==0              |
|   0110 | VS                   | Overflow                     | Unordered                         | V==1              |
|   0111 | VC                   | No overflow                  | Not unordered                     | V==0              |
|   1000 | HI                   | Unsigned higher              | Greater than, or unordered        | C==1and Z == 0    |
|   1001 | LS                   | Unsigned lower or same       | Less than or equal                | C==0or Z == 1     |
|   1010 | GE                   | Signed greater than or equal | Greater than or equal             | N==V              |
|   1011 | LT                   | Signed less than             | Less than, or unordered           | N!=V              |
|   1100 | GT                   | Signed greater than          | Greater than                      | Z==0andN==V       |
|   1101 | LE                   | Signed less than or equal    | Less than, equal, or unordered    | Z == 1 orN!=V     |
|   1110 | None ( AL ) d        | Always (unconditional)       | Always (unconditional)            | Any               |

In T32 instructions, the condition, if it is not AL , is normally encoded in a preceding IT instruction. For more information, see Conditional instructions and IT. Some conditional branch instructions do not require a preceding IT instruction, because they include a Condition code in their encoding.

Implementations can provide a set of ITD control fields, SCTLR.ITD, SCTLR\_EL1.ITD, and HSCTLR.ITD, to disable use of IT for some instructions, making them UNDEFINED.

In A32 instructions, bits[31:28] of the instruction contain either:

- The Condition code, see The Condition code field in A32 instruction encodings.
- 0b1111 for some A32 instructions that can only be executed unconditionally.

## F1.3.1 The Condition code field in A32 instruction encodings

Every conditional A32 instruction contains a 4-bit Condition code field, the cond field, in bits 31-28:

| 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| cond                                                                                    |                                                                                         |

This field contains one of the values 0b0000 -0b1110 , as shown in Table F1-1. Most instruction mnemonics can be extended with the letters defined in the Mnemonic extension column of that table.

If the always ( AL ) condition is specified, the instruction is executed irrespective of the value of the Condition flags. The absence of a Condition code on an instruction mnemonic implies the AL Condition code.

## F1.3.2 Pseudocode description of conditional execution

The AArch32.CurrentCond() function returns a 4-bit condition specifier as follows:

- For A32 instructions, it returns bits[31:28] of the instruction.
- For the T1 and T3 encodings of the Branch instruction (see B), it returns the 4-bit cond field of the encoding.
- For all other T32 instructions:
- -If PSTATE.IT&lt;3:0&gt; != '0000' it returns PSTATE.IT&lt;7:4&gt; . -If PSTATE.IT&lt;7:0&gt; == '00000000' it returns '1110' .
- -Otherwise, execution of the instruction is CONSTRAINED UNPREDICTABLE.

For more information, see Process state, PSTATE.

The ConditionPassed() function uses this condition specifier and the Condition flags to determine whether the instruction must be executed, by calling the ConditionHolds() function.

A-profile Architecture Pseudocode includes the definitions of these functions.

Undefined Instruction exception describes the handling of conditional instructions that are UNDEFINED, UNPREDICTABLE, or CONSTRAINED UNPREDICTABLE. The pseudocode in the manual, as a sequential description of the instructions, has limitations in this respect. For more information, see Limitations of the instruction pseudocode.