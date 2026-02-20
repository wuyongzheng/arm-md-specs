## F6.1.25 VACLE

Vector Absolute Compare Less Than or Equal takes the absolute value of each element in a vector, and compares it with the absolute value of the corresponding element of a second vector. If the first is less than or equal to the second, the corresponding element in the destination vector is set to all ones. Otherwise, it is set to all zeros.

This is a pseudo-instruction of V ACGE. This means:

- The encodings in this description are named to match the encodings of V ACGE.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of V ACGE gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VACLE{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

{&lt;Dd&gt;, }&lt;Dn&gt;, is equivalent to

VACGE{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

&lt;Dd&gt;,

&lt;Dm&gt;,

&lt;Dm&gt;

&lt;Dn&gt;

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

VACLE{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

is equivalent to

VACGE{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

<!-- image -->

{&lt;Qd&gt;, }&lt;Qn&gt;,

&lt;Qm&gt;

&lt;Qd&gt;,

&lt;Qm&gt;,

&lt;Qn&gt;

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

VACLE{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt; {&lt;Qd&gt;, }&lt;Qn&gt;, &lt;Qm&gt;

is equivalent to

VACGE{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt; &lt;Qd&gt;, &lt;Qm&gt;, &lt;Qn&gt;

## Assembler Symbols

## &lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'sz':

|   sz | <dt>   |
|------|--------|
|    0 | F32    |
|    1 | F16    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

<!-- image -->

## &lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

The description of V ACGE gives the operational pseudocode for this instruction.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.