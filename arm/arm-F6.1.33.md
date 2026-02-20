## F6.1.33 VAND (immediate)

Vector Bitwise AND (immediate) performs a bitwise AND between a register value and an immediate value, and returns the result into the destination vector.

This is a pseudo-instruction of VBIC (immediate). This means:

- The encodings in this description are named to match the encodings of VBIC (immediate).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of VBIC (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

<!-- image -->

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VAND{<c>}{<q>}.I32 {<Qd>, }<Qd>, #<imm> is equivalent to VBIC{<c>}{<q>}.I32 <Qd>, #~<imm>
```

A2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

<!-- image -->

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

VAND{&lt;c&gt;}{&lt;q&gt;}.I16

{&lt;Qd&gt;, }&lt;Qd&gt;, #&lt;imm&gt;

is equivalent to

VBIC{&lt;c&gt;}{&lt;q&gt;}.I16

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

VAND{&lt;c&gt;}{&lt;q&gt;}.I32

{&lt;Dd&gt;, }&lt;Dd&gt;, #&lt;imm&gt;

is equivalent to

VBIC{&lt;c&gt;}{&lt;q&gt;}.I32

&lt;Dd&gt;, #~&lt;imm&gt;

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

VAND{&lt;c&gt;}{&lt;q&gt;}.I32

{&lt;Qd&gt;, }&lt;Qd&gt;, #&lt;imm&gt;

is equivalent to

VBIC{&lt;c&gt;}{&lt;q&gt;}.I32 &lt;Qd&gt;, #~&lt;imm&gt;

T2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

VAND{&lt;c&gt;}{&lt;q&gt;}.I16

{&lt;Dd&gt;, }&lt;Dd&gt;, #&lt;imm&gt;

is equivalent to

VBIC{&lt;c&gt;}{&lt;q&gt;}.I16

&lt;Qd&gt;, #~&lt;imm&gt;

&lt;Dd&gt;, #~&lt;imm&gt;

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

VAND{&lt;c&gt;}{&lt;q&gt;}.I16 {&lt;Qd&gt;, }&lt;Qd&gt;, #&lt;imm&gt;

is equivalent to

VBIC{&lt;c&gt;}{&lt;q&gt;}.I16

&lt;Qd&gt;, #~&lt;imm&gt;

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A2 128-bit SIMD vector', and 'A2 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 128-bit SIMD vector', and 'T2 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;imm&gt;

Is a constant of the specified type that is replicated to fill the destination register. For details of the range of constants available and the encoding of &lt;imm&gt; , see Modified immediate constants in T32 and A32 Advanced SIMD instructions.

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## Operation

The description of VBIC (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of VBIC (immediate) gives the operational information for this instruction.