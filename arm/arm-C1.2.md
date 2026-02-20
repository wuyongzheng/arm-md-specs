## C1.2 Structure of the A64 assembler language

The following sections describe the A64 assembler syntax:

- General requirements.
- Common syntax terms.
- Instruction Mnemonics.
- Condition code.
- Register names.

## C1.2.1 General requirements

The letter W denotes a general-purpose register holding a 32-bit word, and X denotes a general-purpose register holding a 64-bit doubleword.

An A64 assembler recognizes both uppercase and lowercase variants of the instruction mnemonics and register names, but not mixed case variants. An A64 disassembler can output either uppercase or lowercase mnemonics and register names. Program and data labels are case-sensitive.

The A64 assembly language does not require the # character to introduce constant immediate operands, but an assembler must allow immediate values introduced with or without the # character.

In Example C1-1, the sequence // is used as a comment leader and A64 assemblers are encouraged to accept this syntax.

## C1.2.2 Common syntax terms

The following syntax terms are used frequently throughout the A64 instruction set description.

| UPPER    | Text in upper-case letters is fixed. Text in lower-case letters is variable. This means that register name Xn indicates that the X is required, followed by a variable register number, for example X29 .                                                                                                                                                                               |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| < >      | Any text enclosed by angle braces, < >, is a value that the user supplies. Subsequent text might supply additional information.                                                                                                                                                                                                                                                         |
| { }      | Any item enclosed by curly brackets, { }, is optional. Adescription of the item and how its presence or absence affects the instruction is normally supplied by subsequent text. In some cases curly braces are actual symbols in the syntax, for example when they surround a register list. These cases are called out in the surrounding text.                                       |
| [ ]      | Any items enclosed by square brackets, [ ], constitute a list of alternative characters. Asingle one of the characters can be used in that position and the subsequent text describes the meaning of the alternatives. In some case the square brackets are part of the syntax itself, such as addressing modes or vector elements. These cases are called out in the surrounding text. |
| a&#124;b | Alternative words are separated by a vertical bar, &#124;, and can be surrounded by parentheses to delimit them. For example, U(ADD&#124;SUB)W represents UADDW or USUBW .                                                                                                                                                                                                              |
| ±        | This indicates an optional + or - sign. If neither is used then + is assumed.                                                                                                                                                                                                                                                                                                           |
| uimmn    | An n -bit unsigned, positive, immediate value.                                                                                                                                                                                                                                                                                                                                          |
| simmn    | An n -bit two's complement, signed immediate value, where n includes the sign bit.                                                                                                                                                                                                                                                                                                      |
| SP       | See Register names.                                                                                                                                                                                                                                                                                                                                                                     |
| Wn       | See Register names.                                                                                                                                                                                                                                                                                                                                                                     |
| WSP      | See Register names.                                                                                                                                                                                                                                                                                                                                                                     |
| WZR      | See Register names.                                                                                                                                                                                                                                                                                                                                                                     |
| Xn       | See Register names.                                                                                                                                                                                                                                                                                                                                                                     |
| XZR      | See Register names                                                                                                                                                                                                                                                                                                                                                                      |

## C1.2.3 Instruction Mnemonics

The A64 assembly language overloads instruction mnemonics and distinguishes between the different forms of an instruction based on the operand types. For example, the following ADD instructions all have different opcodes. However, the programmer must remember only one mnemonic, as the assembler automatically chooses the correct opcode based on the operands. The disassembler follows the same procedure in reverse.

```
ADD W0, W1, W2 // add 32-bit register ADD X0, X1, X2 // add 64-bit register ADD X0, X1, W2, SXTW // add 64-bit extended ADD X0, X1, #42 // add 64-bit immediate
```

## C1.2.4 Condition code

The A64 ISA has some instructions that set Condition flags or test Condition codes or both. For information about instructions that set the Condition flags or use the condition mnemonics, see Condition flags and related instructions.

Table C1-1 shows the available Condition codes.

```
Example C1-1 ADD instructions with different opcodes register
```

Table C1-1 Condition codes

|   cond | Mnemonic   | Meaning (integer)            | Meaning (floating-point) a        | Condition flags   |
|--------|------------|------------------------------|-----------------------------------|-------------------|
|   0000 | EQ         | Equal                        | Equal                             | Z == 1            |
|   0001 | NE         | Not equal                    | Not equal or unordered            | Z == 0            |
|   0010 | CS or HS   | Carry set                    | Greater than, equal, or unordered | C==1              |
|   0011 | CC or LO   | Carry clear                  | Less than                         | C==0              |
|   0100 | MI         | Minus, negative              | Less than                         | N==1              |
|   0101 | PL         | Plus, positive or zero       | Greater than, equal, or unordered | N==0              |
|   0110 | VS         | Overflow                     | Unordered                         | V==1              |
|   0111 | VC         | No overflow                  | Ordered                           | V==0              |
|   1000 | HI         | Unsigned higher              | Greater than, or unordered        | C==1&&Z==0        |
|   1001 | LS         | Unsigned lower or same       | Less than or equal                | !(C ==1 &&Z==0)   |
|   1010 | GE         | Signed greater than or equal | Greater than or equal             | N==V              |
|   1011 | LT         | Signed less than             | Less than, or unordered           | N!=V              |
|   1100 | GT         | Signed greater than          | Greater than                      | Z==0&&N==V        |
|   1101 | LE         | Signed less than or equal    | Less than, equal, or unordered    | !(Z==0&&N==V)     |
|   1110 | AL         | Always                       | Always                            | Any               |
|   1111 | NV b       | Always                       | Always                            | Any               |

## C1.2.5 SVE Condition code aliases

The SVE and SME assembler syntax defines an alternative set of condition code aliases for use with AArch64 conditional instructions, as follows:

Table C1-2 shows the available SVE Condition code aliases.

Table C1-2 SVE Condition codes

|   cond | Mnemonic   | SVE alias   | Meaning                                                                                                 | Condition flags         |
|--------|------------|-------------|---------------------------------------------------------------------------------------------------------|-------------------------|
|   0000 | EQ         | NONE        | All Active elements were FALSE or there were no Active elements .                                       | Z == 1                  |
|   0001 | NE         | ANY         | An Active element was TRUE.                                                                             | Z == 0                  |
|   0010 | CS or HS   | NLAST       | The Last active element was FALSE or there were no Active elements .                                    | C==1                    |
|   0011 | CC or LO   | LAST        | The Last active element was TRUE.                                                                       | C==0                    |
|   0100 | MI         | FIRST       | The First active element was TRUE.                                                                      | N==1                    |
|   0101 | PL         | NFRST       | The First active element was FALSE or there were no Active elements .                                   | N==0                    |
|   0110 | VS         | -           | CTERM comparison failed, but end of partition reached.                                                  | V==1                    |
|   0111 | VC         | -           | CTERM comparison succeeded, or end of partition not reached.                                            | V==0                    |
|   1000 | HI         |             | An Active element was TRUE, but the Last active element was FALSE.                                      | C==1&&Z==0              |
|   1001 | LS         | PLAST       | The Last active element was TRUE, or all Active elements were FALSE, or there were no Active elements . | C==0 &#124;&#124; Z ==1 |
|   1010 | GE         | TCONT       | CTERM termination condition not detected.                                                               | N==V                    |
|   1011 | LT         | TSTOP       | CTERM termination condition detected.                                                                   | N!=V                    |

## C1.2.6 Register names

## See:

- General-purpose register file and zero register and stack pointer.
- Advanced SIMD and floating-point register file.
- Advanced SIMD and floating-point scalar register names.
- SIMD vector register names.
- SIMD vector element names.
- For SVE register names, see Z0-Z31, P0-P15, and FFR, First Fault Register.
- For SME ZA storage, see ZA array vector access and ZA tile access.
- For SME2 ZT0 storage, see ZT0.

## C1.2.6.1 General-purpose register file and zero register and stack pointer

The 31 general-purpose registers in the general-purpose register file are named R0-R30 and encoded in the instruction register fields with values 0-30. In a general-purpose register field the value 31 represents either the current stack pointer or the zero register, depending on the instruction and the operand position.

When the registers are used in a specific instruction variant, they must be qualified to indicate the operand data size, 32 bits or 64 bits, and the data size of the instruction.

When the data size is 32 bits, the lower 32 bits of the register are used and the upper 32 bits are ignored on a read and cleared to zero on a write.

Table C1-3 shows the qualified names for registers, where n is a register number 0-30.

Table C1-3 Naming of general-purpose registers, the zero register, and the stack pointer

| Name   | Size    | Encoding   | Description                   |
|--------|---------|------------|-------------------------------|
| Wn     | 32 bits | 0-30       | General-purpose register 0-30 |
| Xn     | 64 bits | 0-30       | General-purpose register 0-30 |
| WZR    | 32 bits | 31         | Zero register                 |
| XZR    | 64 bits | 31         | Zero register                 |
| WSP    | 32 bits | 31         | Current stack pointer         |
| SP     | 64 bits | 31         | Current stack pointer         |

This list gives more information about the instruction arguments shown in Table C1-3:

- The names Xn and Wn both refer to the same general-purpose register, Rn.
- There is no register named W31 or X31.
- The name SP represents the stack pointer for 64-bit operands where an encoding of the value 31 in the corresponding register field is interpreted as a read or write of the current stack pointer. When instructions do not interpret this operand encoding as the stack pointer, use of the name SP is an error.
- The name WSP represents the current stack pointer in a 32-bit context.
- The name XZR represents the zero register for 64-bit operands where an encoding of the value 31 in the corresponding register field is interpreted as returning zero when read or discarding the result when written. When instructions do not interpret this operand encoding as the zero register, use of the name XZR is an error.
- The name WZR represents the zero register in a 32-bit context.
- The architecture does not define a specific name for general-purpose register R30 to reflect its role as the link register on procedure calls. However, an A64 assembler must always use W30 and X30 for this purpose, and additional software names might be defined as part of the Procedure Call Standard, see Procedure Call Standard for the Arm 64-bit Architecture .

## C1.2.6.2 Advanced SIMD and floating-point register file

The 32 registers in the Advanced SIMD and floating-point register file, V0-V31, hold floating-point operands for the scalar floating-point instructions, and both scalar and vector operands for the Advanced SIMD instructions. When they are used in a specific instruction form, the names must be further qualified to indicate the data shape, that is the data element size and the number of elements or lanes within the register. A similar requirement is placed on the general-purpose registers. See General-purpose register file and zero register and stack pointer.

Note

The data type is described by the instruction mnemonics that operate on the data. The data type is not described by the register name. The data type is the interpretation of bits within each register or vector element, whether these are integers, floating-point values, polynomials, or cryptographic hashes.

## C1.2.6.3 Advanced SIMD and floating-point scalar register names

Advanced SIMD and floating-point instructions that operate on scalar data only access the lower bits of an Advanced SIMD and floating-point register. The unused high bits are ignored on a read and cleared to 0 on a write.

Table C1-4 shows the qualified names for accessing scalar Advanced SIMD and floating-point registers. The letter n denotes a register number between 0 and 31.

Table C1-4 Advanced SIMD and floating-point scalar register names

| Size     | Name   |
|----------|--------|
| 8 bits   | Bn     |
| 16 bits  | Hn     |
| 32 bits  | Sn     |
| 64 bits  | Dn     |
| 128 bits | Qn     |

## C1.2.6.4 SIMD vector register names

If a register holds multiple data elements on which arithmetic is performed in a parallel, SIMD manner, then a qualifier describes the vector shape. The vector shape is the element size and the number of elements or lanes. If the element size in bits multiplied by the number of lanes does not equal 128, then the upper 64 bits of the register are ignored on a read and cleared to zero on a write.

Table C1-5 shows the SIMD vector register names. The letter n denotes a register number between 0 and 31.

Table C1-5 SIMD vector register names

| Shape             | Name   |
|-------------------|--------|
| 8 bits × 8 lanes  | Vn.8B  |
| 8 bits × 16 lanes | Vn.16B |
| 16 bits × 4 lanes | Vn.4H  |
| 16 bits × 8 lanes | Vn.8H  |
| 32 bits × 2 lanes | Vn.2S  |
| 32 bits × 4 lanes | Vn.4S  |
| 64 bits × 1 lane  | Vn.1D  |
| 64 bits × 2 lanes | Vn.2D  |

## C1.2.6.5 SIMD vector element names

Appending a constant, zero-based element index to the register name inside square brackets indicates that a single element from a SIMD and floating-point register is used as a scalar operand. The number of lanes is not represented, as it is not encoded in the instruction and can only be inferred from the index value.

Table C1-6 shows the vector register names and the element index. The letter i denotes the element index.

Table C1-6 Vector register names with element index

| Size    | Name    |
|---------|---------|
| 8 bits  | Vn.B[i] |
| 16 bits | Vn.H[i] |
| 32 bits | Vn.S[i] |
| 64 bits | Vn.D[i] |

An assembler must accept a fully qualified SIMD register name if the number of lanes is greater than the index value. See SIMD vector register names. For example, an assembler must accept all of the following forms as the name for the 32-bit element in bits [63:32] of the SIMD and floating-point register V9:

```
V9.S[1] //standard disassembly V9.2S[1] //optional number V9.4S[1] //optional number
```

## Note

The SIMD and floating-point register element name Vn.S[0] is not equivalent to the scalar SIMD and floating-point register name Sn . Although they represent the same bits in the register, they select different instruction encoding forms, either the vector element or the scalar form.

## C1.2.6.5.1 SIMD vector register list

Where an instruction operates on multiple SIMD&amp;FP or SVE registers, for example vector load/store structure and table lookup operations, the registers are specified as a list enclosed by curly braces. This list consists of either a sequence of registers separated by commas, or a register range separated by a hyphen. The registers must be numbered in increasing order, modulo 32, in increments of one. The hyphenated form is preferred for disassembly if there are more than two registers in the list and the register numbers are increasing by 1. The following examples are equivalent representations of a set of four registers V4 to V7 , each holding four lanes of 32-bit elements:

```
{ V4.4S - V7.4S } //standard disassembly { V4.4S, V5.4S, V6.4S, V7.4S } //alternative
```

## C1.2.6.5.2 SIMD vector element list

Registers in a list can also have a vector element form. For example, the LD4 instruction can load one element into each of four registers, and in this case the index is appended to the list as follows:

```
{ V4.S - V7.S }[3] //standard disassembly { V4.4S, V5.4S, V6.4S, V7.4S }[3] //alternative with optional number of lanes
```

```
representation
```

```
of lanes of lanes
```