## F5.1.206 SMULBB, SMULBT, SMULTB, SMULTT

Signed Multiply (halfwords)

Signed Multiply (halfwords) multiplies two signed 16-bit quantities, taken from either the bottom or the top half of their respective source registers. The other halves of these source registers are ignored. The 32-bit product is written to the destination register. No overflow is possible during this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMULBB variant

```
Applies when (M == 0 && N == 0) SMULBB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULBT variant

```
Applies when (M == 1 && N == 0) SMULBT{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULTB variant

```
Applies when (M == 0 && N == 1) SMULTB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULTT variant

```
Applies when
```

```
(M == 1 && N == 1) SMULTT{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer n_index = UInt(N); constant integer m_index = UInt(M); if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the SMULBB variant

Applies when (N == 0 &amp;&amp; M ==

```
0)
```

```
SMULBB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULBT variant

```
Applies when (N == 0 && M == 1) SMULBT{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULTB variant

```
Applies when (N == 1 && M ==
```

```
0)
```

```
SMULTB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULTT variant

Applies when (N == 1 &amp;&amp; M ==

```
1)
```

```
SMULTT{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer n_index = UInt(N); constant integer m_index = UInt(M); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

Is the first general-purpose source register holding the multiplicand in the bottom or top half (selected by &lt;x&gt; ), encoded in the 'Rn' field.

&lt;q&gt;

## &lt;Rd&gt;

&lt;Rn&gt;

## &lt;Rm&gt;

Is the second general-purpose source register holding the multiplier in the bottom or top half (selected by &lt;y&gt; ), encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(16) operand1 = Elem[R[n], n_index, 16]; constant bits(16) operand2 = Elem[R[m], m_index, 16]; constant integer result = SInt(operand1) * SInt(operand2); R[d] = result<31:0>; // Signed overflow cannot occur
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.