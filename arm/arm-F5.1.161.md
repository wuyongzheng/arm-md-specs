## F5.1.161 ROR (immediate)

Rotate Right (immediate) provides the value of the contents of a register rotated by a constant value. The bits that are rotated off the right end are inserted into the vacated bit positions on the left.

This is an alias of MOV , MOVS (register). This means:

- The encodings in this description are named to match the encodings of MOV , MOVS (register).
- The description of MOV, MOVS (register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T3).

A1

<!-- image -->

## Encoding for the MOV, shift or rotate by value variant

```
ROR{<c>}{<q>} {<Rd>, }<Rm>, #<imm>
```

## is equivalent to

```
MOV{<c>}{<q>} <Rd>, <Rm>, ROR #<imm>
```

and is always the preferred disassembly.

T3

<!-- image -->

## Encoding for the MOV, shift or rotate by value variant

```
Applies when (!(imm3 == '000' && imm2 == '00')) ROR{<c>}{<q>} {<Rd>, }<Rm>, #<imm>
```

is equivalent to

```
MOV{<c>}{<q>} <Rd>, <Rm>, ROR #<imm>
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Rd&gt;

For the 'A1 MOV, shift or rotate by value' variant: is the general-purpose destination register, encoded in the 'Rd' field. Arm deprecates using the PC as the destination register, but if the PC is used, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T3 MOV, shift or rotate by value' variant: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1 MOV, shift or rotate by value' variant: is the general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T3 MOV, shift or rotate by value' variant: is the general-purpose source register, encoded in the 'Rm' field.

## &lt;imm&gt;

For the 'A1 MOV, shift or rotate by value' variant: is the shift amount, in the range 1 to 31, encoded in the 'imm5' field.

For the 'T3 MOV, shift or rotate by value' variant: is the shift amount, in the range 1 to 31, encoded in the 'imm3:imm2' field.

## Operation

The description of MOV, MOVS (register) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOV, MOVS (register) gives the operational information for this instruction.