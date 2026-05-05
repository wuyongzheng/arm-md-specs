## C6.2.67 CBHLO

Compare unsigned lower than halfwords and branch

This instruction compares the unsigned halfword values in two registers, and conditionally branches to a label at a PC-relative offset if the second value is lower than the first. This instruction provides a hint that this is not a subroutine call or return. This instruction does not affect the condition flags.

This is a pseudo-instruction of CBH&lt;cc&gt;. This means:

- The encodings in this description are named to match the encodings of CBH&lt;cc&gt;.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of CBH&lt;cc&gt; gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Branch

(FEAT\_CMPBR)

<!-- image -->

## Encoding

<!-- image -->

## Assembler Symbols

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be tested, encoded in the 'Rt' field.

## &lt;label&gt;

Is the program label to be conditionally branched to. Its offset from the address of this instruction, in the range -1024 to 1020, is encoded as 'imm9' times 4.

## Operation

The description of CBH&lt;cc&gt; gives the operational pseudocode for this instruction.
