## F5.1.4 ADD (immediate, to PC)

Add to PC adds an immediate value to the Align(PC, 4) value to form a PC-relative address, and writes the result to the destination register. Arm recommends that, where possible, software avoids using this alias.

This is a pseudo-instruction of ADR. This means:

- The encodings in this description are named to match the encodings of ADR.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of ADR gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T3).

A1

<!-- image -->

## Encoding for the A1 variant

```
ADD{<c>}{<q>} <Rd>, PC, #<const>
```

## is equivalent to

```
ADR{<c>}{<q>} <Rd>, <label>
```

T1

## Encoding for the T1 variant

```
ADD{<c>}{<q>} <Rd>, PC, #<imm8>
```

## is equivalent to

```
ADR{<c>}{<q>} <Rd>, <label>
```

T3

<!-- image -->

## Encoding for the T3 variant

<!-- image -->

ADD{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, PC, #&lt;imm12&gt;

ADDW{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, PC, #&lt;imm12&gt; // (UInt(Rd) &lt; 8 &amp;&amp; UInt(i :: imm3 :: imm8) &lt; 256)

## is equivalent to

```
ADR{<c>}{<q>} <Rd>, <label>
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' variant: is the general-purpose destination register, encoded in the 'Rd' field. If the PC is used, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

For the 'T1' and 'T3' variants: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;const&gt;

An immediate value. See Modified immediate constants in A32 instructions for the range of values.

## &lt;imm8&gt;

Is an unsigned immediate, a multiple of 4, in the range 0 to 1020, encoded in the 'imm8' field as &lt;imm8&gt;/4.

## &lt;imm12&gt;

Is a 12-bit unsigned immediate, in the range 0 to 4095, encoded in the 'i:imm3:imm8' field.

## Operation

The description of ADR gives the operational pseudocode for this instruction.

&lt;q&gt;

## &lt;Rd&gt;