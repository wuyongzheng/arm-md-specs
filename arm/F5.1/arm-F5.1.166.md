## F5.1.166 RRXS

Rotate Right with Extend, setting flags provides the value of the contents of a register shifted right by one place, with the Carry flag shifted into bit[31].

If the destination register is not the PC, this instruction updates the condition flags based on the result, and bit[0] is shifted into the Carry flag.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. Arm deprecates any use of these encodings. However, when the destination register is the PC:

- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

This is an alias of MOV , MOVS (register). This means:

- The encodings in this description are named to match the encodings of MOV , MOVS (register).
- The description of MOV, MOVS (register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T3).

A1

<!-- image -->

<!-- image -->

and is always the preferred disassembly.

T3

<!-- image -->

S

## Encoding for the MOVS, rotate right with extend variant

<!-- image -->

and is always the preferred disassembly.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 MOVS, rotate right with extend' variant: is the general-purpose destination register, encoded in the 'Rd' field. Arm deprecates using the PC as the destination register, but if the PC is used, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T3 MOVS, rotate right with extend' variant: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1 MOVS, rotate right with extend' variant: is the general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T3 MOVS, rotate right with extend' variant: is the general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of MOV, MOVS (register) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOV, MOVS (register) gives the operational information for this instruction.

&lt;q&gt;

## &lt;Rd&gt;