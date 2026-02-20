## F5.1.104 LSR (immediate)

Logical Shift Right (immediate) shifts a register value right by an immediate number of bits, shifting in zeros, and writes the result to the destination register.

This is an alias of MOV , MOVS (register). This means:

- The encodings in this description are named to match the encodings of MOV , MOVS (register).
- The description of MOV, MOVS (register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T2 and T3).

A1

<!-- image -->

## Encoding for the MOV, shift or rotate by value variant

<!-- image -->

and is always the preferred disassembly.

T2

## Encoding for the T2 variant

```
LSR<c>{<q>} {<Rd>, }<Rm>, #<imm>
```

is equivalent to

```
MOV<c>{<q>} <Rd>, <Rm>, LSR #<imm>
```

and is the preferred disassembly when InITBlock() .

T3

<!-- image -->

S

<!-- image -->

## Encoding for the MOV, shift or rotate by value variant

```
LSR{<c>}{<q>} {<Rd>, }<Rm>, #<imm>
```

```
LSR<c>.W {<Rd>, }<Rm>, #<imm> // (!InITBlock() && UInt(Rd) < 8 && UInt(Rm) < 8)
```

is equivalent to

```
MOV{<c>}{<q>} <Rd>, <Rm>, LSR #<imm>
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 MOV, shift or rotate by value' variant: is the general-purpose destination register, encoded in the 'Rd' field. Arm deprecates using the PC as the destination register, but if the PC is used, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T2' and 'T3 MOV, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1 MOV, shift or rotate by value' variant: is the general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T2' and 'T3 MOV, shift or rotate by value' variants: is the general-purpose source register, encoded in the 'Rm' field.

## &lt;imm&gt;

For the 'A1 MOV, shift or rotate by value' and 'T2' variants: is the shift amount, in the range 1 to 32, encoded in the 'imm5' field as &lt;imm&gt; modulo 32.

For the 'T3 MOV, shift or rotate by value' variant: is the shift amount, in the range 1 to 32, encoded in the 'imm3:imm2' field as &lt;imm&gt; modulo 32.

## Operation

The description of MOV, MOVS (register) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOV, MOVS (register) gives the operational information for this instruction.

## &lt;q&gt;

## &lt;Rd&gt;