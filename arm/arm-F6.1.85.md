## F6.1.85 VEXT (multibyte elements)

Vector Extract extracts elements from the bottom end of the second operand vector and the top end of the first, concatenates them and places the result in the destination vector.

This is a pseudo-instruction of VEXT (byte elements). This means:

- The encodings in this description are named to match the encodings of VEXT (byte elements).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of VEXT (byte elements) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0) VEXT{&lt;c&gt;}{&lt;q&gt;}.&lt;size&gt; {&lt;Dd&gt;, }&lt;Dn&gt;, &lt;Dm&gt;, #&lt;imm&gt; is equivalent to VEXT{&lt;c&gt;}{&lt;q&gt;}.8 {&lt;Dd&gt;, }&lt;Dn&gt;, &lt;Dm&gt;, #&lt;imm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VEXT{<c>}{<q>}.<size> {<Qd>, }<Qn>, <Qm>, #<imm> is equivalent to VEXT{<c>}{<q>}.8 {<Qd>, }<Qn>, <Qm>, #<imm>
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

```
VEXT{<c>}{<q>}.<size> {<Dd>, }<Dn>, <Dm>, #<imm>
```

is equivalent to

VEXT{&lt;c&gt;}{&lt;q&gt;}.8

{&lt;Dd&gt;, }&lt;Dn&gt;, &lt;Dm&gt;, #&lt;imm&gt;

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VEXT{<c>}{<q>}.<size> {<Qd>, }<Qn>,
```

```
(Q == 1) <Qm>, #<imm>
```

## is equivalent to

```
VEXT{<c>}{<q>}.8 {<Qd>, }<Qn>, <Qm>, #<imm>
```

## Assembler Symbols

## &lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

For the 'A1 64-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: is the size of the operation, and can be one of 16 or 32.

For the 'A1 128-bit SIMD vector' and 'T1 128-bit SIMD vector' variants: is the size of the operation, and can be one of 16, 32 or 64.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;q&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;imm&gt;

For the 'A1 64-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: is the location of the extracted result in the concatenation of the operands, as a number of bytes from the least significant end, in the range 0 to (128/ &lt;size&gt; )-1.

For the 'A1 128-bit SIMD vector' and 'T1 128-bit SIMD vector' variants: is the location of the extracted result in the concatenation of the operands, as a number of bytes from the least significant end, in the range 0 to (64/ &lt;size&gt; )-1.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

The description of VEXT (byte elements) gives the operational pseudocode for this instruction.

## Operational Information

The description of VEXT (byte elements) gives the operational information for this instruction.