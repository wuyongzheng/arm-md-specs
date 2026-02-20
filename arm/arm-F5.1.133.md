## F5.1.133 PKHBT, PKHTB

Pack Halfword combines one halfword of its first operand with the other halfword of its shifted second operand.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the PKHBT variant

```
Applies when (tb == 0) PKHBT{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, LSL #<imm>}
```

## Encoding for the PKHTB variant

```
Applies when
```

```
(tb == 1)
```

```
PKHTB{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, ASR #<imm>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean tbform = (tb == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(tb:'0', imm5); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the PKHBT variant

```
Applies when (tb == 0) PKHBT{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, LSL #<imm>} // (tbform == FALSE)
```

## Encoding for the PKHTB variant

```
Applies when (tb == 1) PKHTB{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, ASR #<imm>} // (tbform ==
```

```
TRUE)
```

## Decode for all variants of this encoding

```
imm3:imm2);
```

```
if S == '1' || T == '1' then UNDEFINED; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean tbform = (tb == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(tb:'0', // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;imm&gt;

For the 'A1 PKHBT' and 'A1 PKHTB' variants: the shift to apply to the value read from &lt;Rm&gt; , encoded in the 'imm5' field.

For PKHBT , it is one of:

omitted No shift, encoded as 0b00000 .

1-31 Left shift by specified number of bits, encoded as a binary number.

For PKHTB , it is one of:

omitted Instruction is a pseudo-instruction and is assembled as though PKHBT{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, &lt;Rm&gt;, &lt;Rn&gt; had been written.

- 1-32 Arithmetic right shift by specified number of bits. A shift by 32 bits is encoded as 0b00000 . Other shift amounts are encoded as binary numbers.

## Note

An assembler can permit &lt;imm&gt; = 0 to mean the same thing as omitting the shift, but this is not standard UAL and must not be used for disassembly.

For the 'T1 PKHBT' and 'T1 PKHTB' variants: the shift to apply to the value read from &lt;Rm&gt; , encoded in the 'imm3:imm2' field.

For PKHBT , it is one of:

omitted No shift, encoded as 0b00000 .

1-31 Left shift by specified number of bits, encoded as a binary number.

For PKHTB , it is one of:

- omitted Instruction is a pseudo-instruction and is assembled as though PKHBT{&lt;c&gt;}{&lt;q&gt;} &lt;Rd&gt;, &lt;Rm&gt;, &lt;Rn&gt; had been written.
- 1-32 Arithmetic right shift by specified number of bits. A shift by 32 bits is encoded as 0b00000 . Other shift amounts are encoded as binary numbers.

Note

An assembler can permit &lt;imm&gt; = 0 to mean the same thing as omitting the shift, but this is not standard UAL and must not be used for disassembly.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) operand2 = Shift(R[m], shift_t, shift_n, PSTATE.C); // PSTATE.C ignored R[d]<15:0> = if tbform then operand2<15:0> else R[n]<15:0>; R[d]<31:16> = if tbform then R[n]<31:16> else operand2<31:16>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.