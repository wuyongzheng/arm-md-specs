## C6.1 About the A64 base instructions

Alphabetical list of A64 base instructions gives full descriptions of the A64 instructions that are in the following instruction groups:

- Branch, Exception generation, and System instructions.
- Loads and stores associated with the general-purpose registers.
- Data processing (immediate).
- Data processing (register).

A64 instruction set encoding provides an overview of the instruction encodings as well as of the instruction classes within their functional groups.

The rest of this section is general description of the base instructions. It contains the following subsections:

- Register size.
- Use of the PC.
- Use of the stack pointer.
- Condition flags and related instructions.

## C6.1.1 Register size

Most data processing, comparison, and conversion instructions that use the general-purpose registers as the source or destination operand have two instruction variants that operate on either a 32-bit or a 64-bit value.

Where a 32-bit instruction form is selected, the following holds:

- The upper 32 bits of the source registers are ignored.
- The upper 32 bits of the destination register are set to zero.
- Right shifts and right rotates inject at bit[31], not at bit[63].
- The Condition flags, where set by the instruction, are computed from the lower 32 bits.

This distinction applies even when the results of a 32-bit instruction form are indistinguishable from the lower 32 bits computed by the equivalent 64-bit instruction form. For example, a 32-bit bitwise ORR could be performed using a 64-bit ORR and simply ignoring the top 32 bits of the result. However, the A64 instruction set includes separate 32-bit and 64-bit forms of the ORR instruction.

As well as distinct sign-extend or zero-extend instructions, the A64 instruction set also provides the ability to extend and shift the final source register of an ADD , SUB , ADDS , or SUBS instruction and the index register of a load/store instruction. This enables array index calculations involving a 64-bit array pointer and a 32-bit array index to be implemented efficiently.

The assembly language notation enables the distinct identification of registers holding 32-bit values and registers holding 64-bit values. See Register names and Register indexed addressing.

## C6.1.2 Use of the PC

A64 instructions have limited access to the PC. The only instructions that can read the PC are those that generate a PC relative address:

- ADRand ADRP.
- The Load register (literal) instruction class.
- Direct branches that use an immediate offset.
- The unconditional branch with link instructions, BL and BLR, that use the PC to create the return link address.

Only explicit control flow instructions can modify the PC:

- Conditional and unconditional branch and return instructions.

- Exception generation and exception return instructions.

For more details of instructions that can modify the PC, see Branches, Exception generating, and System instructions.

## C6.1.3 Use of the stack pointer

A64 instructions can use the stack pointer only in a limited number of cases:

- Load/store instructions use the current stack pointer as the base address:
- -When stack alignment checking is enabled by system software and the base register is SP, the current stack pointer must be initially quadword aligned, That is, it must be aligned to 16 bytes. Misalignment generates an SP alignment fault. See SP alignment checking for more information.
- Add and subtract data processing instructions in their immediate and extended register forms, use the current stack pointer as a source register or the destination register or both.
- Logical data processing instructions in their immediate form use the current stack pointer as the destination register.

## C6.1.4 Condition flags and related instructions

The A64 base instructions that use the Condition flags as an input are:

- Conditional branch. The conditional branch instruction is B.cond .
- Add or subtract with carry. These instruction types include instructions to perform multi-precision arithmetic and calculate checksums. The add or subtract with carry instructions are ADC , ADCS , SBC , and SBCS , or an architectural alias for these instructions.
- Conditional select with increment, negate, or invert. This instruction type conditionally selects between one source register and a second, incremented, negated, inverted, or unmodified source register. The conditional select with increment, negate, or invert instructions are CSINC , CSINV , and CSNEG .

These instructions also implement:

- -Conditional select or move. The Condition flags select one of two source registers as the destination register. Short conditional sequences can be replaced by unconditional instructions followed by a conditional select, CSEL .
- -Conditional set. Conditionally selects between 0 and 1, or 0 and -1. This can be used to convert the Condition flags to a Boolean value or mask in a general-purpose register, for example. These instructions include CSET and CSETM .
- Conditional compare. This instruction type sets the Condition flags to the result of a comparison if the original condition is true, otherwise it sets the Condition flags to an immediate value. It permits the flattening of nested conditional expressions without using conditional branches or performing Boolean arithmetic within the general-purpose registers. The conditional compare instructions are CCMP and CCMN .

The A64 base instructions that update the Condition flags as an output are:

- Flag-setting data processing instructions, such as ADCS , ADDS , ANDS , BICS , RMIF , SBCS , SETF8 , SETF16 , and SUBS , and the aliases CMN , CMP , and TST .
- Conditional compare instructions such as CCMN , CCMP .
- The random number generation instructions MRS RNDR and MRS RNDRRS , see Effect of random number generation instructions on Condition flags.

The A64 base instructions that manipulate the Condition flags are:

- The flag manipulation instruction CFINV , which inverts the value of the Carry flag.
- If FEAT\_FlagM2 is implemented, the base instructions AXFLAG and XAFLAG . These instructions convert between the Arm floating point comparison PSTATE condition flag format and an alternative format shown in Table C6-1.

Table C6-1 Relationship between ARM format and alternative format PSTATE condition flags

|              | ARM format   | ARM format   | Alternative format   | Alternative format   | Alternative format   | Alternative format   | Alternative format   | Alternative format   |
|--------------|--------------|--------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
| Result       | N            | Z            | C                    | V                    | N                    | Z                    | C                    | V                    |
| Greater than | 0            | 0            | 1                    | 0                    | 0                    | 0                    | 1                    | 0                    |
| Less than    | 1            | 0            | 0                    | 0                    | 0                    | 0                    | 0                    | 0                    |
| Equal        | 0            | 1            | 1                    | 0                    | 0                    | 1                    | 1                    | 0                    |
| Unordered    | 0            | 0            | 1                    | 1                    | 0                    | 1                    | 0                    | 0                    |

The flags can be directly accessed for a read/write using the NZCV.

The A64 base instructions also include conditional branch instructions that do not manipulate the Condition flags:

- Compare and branch if a register is zero or nonzero, CBZ and CBNZ .
- Test a single bit in a register and branch if the bit is zero or nonzero, TBZ and TBNZ .
- Compare and branch instructions, CB &lt; cc &gt; (immediate), CB &lt; cc &gt; (register), CBB &lt; cc &gt;, and CBH &lt; cc &gt;.

## C6.1.4.1 Effect of random number generation instructions on Condition flags

If FEAT\_RNG is implemented, then:

- When a valid random number is returned, the PSTATE.NZCV flags are set to 0b0000 .
- If the random number hardware is not capable of returning a random number in a reasonable period of time, the PSTATE.NZCV flags are set to 0b0100 , and the random number generation instructions return the value 0.

Note

The definition of 'reasonable period of time' is IMPLEMENTATION DEFINED. The expectation is that software might use this as an opportunity to reschedule or run a different routine, perhaps after a small number of retries have failed to return a valid value.