## F5.1.245 SUB (immediate, from PC)

Subtract from PC subtracts an immediate value from the Align(PC, 4) value to form a PC-relative address, and writes the result to the destination register. Arm recommends that, where possible, software avoids using this alias.

This is an alias of ADR. This means:

- The encodings in this description are named to match the encodings of ADR.
- The description of ADR gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A2) and T32 (T2).

A2

<!-- image -->

## Encoding for the A2 variant

```
SUB{<c>}{<q>} <Rd>, PC, #<const>
```

## is equivalent to

```
ADR{<c>}{<q>} <Rd>, <label>
```

and is the preferred disassembly when imm12 == '000000000000' .

T2

<!-- image -->

## Encoding for the T2 variant

```
SUB{<c>}{<q>} <Rd>, PC, #<imm12>
```

## is equivalent to

```
ADR{<c>}{<q>} <Rd>, <label>
```

and is the preferred disassembly when i :: imm3 :: imm8 == '000000000000' .

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Rd&gt;

For the 'A2' variant: is the general-purpose destination register, encoded in the 'Rd' field. If the PC is used, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T2' variant: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;const&gt;

An immediate value. See Modified immediate constants in A32 instructions for the range of values.

## &lt;imm12&gt;

Is a 12-bit unsigned immediate, in the range 0 to 4095, encoded in the 'i:imm3:imm8' field.

## Operation

The description of ADR gives the operational pseudocode for this instruction.