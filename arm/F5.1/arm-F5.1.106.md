## F5.1.106 LSRS (immediate)

Logical Shift Right, setting flags (immediate) shifts a register value right by an immediate number of bits, shifting in zeros, and writes the result to the destination register.

If the destination register is not the PC, this instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. Arm deprecates any use of these encodings. However, when the destination register is the PC:

- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

This is an alias of MOV , MOVS (register). This means:

- The encodings in this description are named to match the encodings of MOV , MOVS (register).
- The description of MOV, MOVS (register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T2 and T3).

A1

<!-- image -->

S

## Encoding for the MOVS, shift or rotate by value variant

<!-- image -->

and is always the preferred disassembly.

T2

## Encoding for the T2 variant

<!-- image -->

and is the preferred disassembly when !InITBlock() .

<!-- image -->

T3

<!-- image -->

S

## Encoding for the MOVS, shift or rotate by value variant

```
LSRS{<c>}{<q>}
```

```
LSRS.W {<Rd>, }<Rm>, #<imm> // (!InITBlock() && UInt(Rd) < 8 && UInt(Rm) <
```

```
{<Rd>, }<Rm>, #<imm> 8)
```

## is equivalent to

```
MOVS{<c>}{<q>} <Rd>, <Rm>, LSR #<imm>
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 MOVS, shift or rotate by value' variant: is the general-purpose destination register, encoded in the 'Rd' field. Arm deprecates using the PC as the destination register, but if the PC is used, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T2' and 'T3 MOVS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1 MOVS, shift or rotate by value' variant: is the general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T2' and 'T3 MOVS, shift or rotate by value' variants: is the general-purpose source register, encoded in the 'Rm' field.

## &lt;imm&gt;

For the 'A1 MOVS, shift or rotate by value' and 'T2' variants: is the shift amount, in the range 1 to 32, encoded in the 'imm5' field as &lt;imm&gt; modulo 32.

For the 'T3 MOVS, shift or rotate by value' variant: is the shift amount, in the range 1 to 32, encoded in the 'imm3:imm2' field as &lt;imm&gt; modulo 32.

## Operation

The description of MOV, MOVS (register) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOV, MOVS (register) gives the operational information for this instruction.

<!-- image -->

## &lt;Rd&gt;