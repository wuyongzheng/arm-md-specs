## F5.1.194 SMLABB, SMLABT, SMLATB, SMLATT

Signed Multiply Accumulate (halfwords) performs a signed multiply accumulate operation. The multiply acts on two signed 16-bit quantities, taken from either the bottom or the top half of their respective source registers. The other halves of these source registers are ignored. The 32-bit product is added to a 32-bit accumulate value and the result is written to the destination register.

If overflow occurs during the addition of the accumulate value, the instruction sets PSTATE.Q to 1. It is not possible for overflow to occur during the multiplication.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMLABB variant

```
Applies when (M == 0 && N == 0) SMLABB{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Encoding for the SMLABT variant

```
Applies when (M == 1 && N == 0) SMLABT{<c>}{<q>} <Rd>,
```

```
<Rn>, <Rm>, <Ra>
```

## Encoding for the SMLATB variant

```
Applies when (M == 0 && N == 1) SMLATB{<c>}{<q>} <Rd>,
```

```
<Rn>, <Rm>, <Ra>
```

## Encoding for the SMLATT variant

```
Applies when (M == 1 && N == 1) SMLATT{<c>}{<q>} <Rd>,
```

```
<Rn>, <Rm>, <Ra>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); constant integer n_index = UInt(N); constant integer m_index = UInt(M); if d == 15 || n == 15 || m == 15 || a == 15 then
```

```
UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the SMLABB variant

Applies when (N == 0 &amp;&amp; M ==

```
SMLABB{<c>}{<q>} <Rd>,
```

```
0) <Rn>, <Rm>, <Ra>
```

## Encoding for the SMLABT variant

Applies when (N == 0 &amp;&amp; M ==

```
1) SMLABT{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Encoding for the SMLATB variant

Applies when (N == 1 &amp;&amp; M ==

```
SMLATB{<c>}{<q>} <Rd>,
```

```
0) <Rn>, <Rm>, <Ra>
```

## Encoding for the SMLATT variant

```
Applies when (N == 1 && M == 1)
```

```
SMLATT{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Decode for all variants of this encoding

```
SMULTT";
```

```
if Ra == '1111' then SEE "SMULBB, SMULBT, SMULTB, constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); constant integer n_index = UInt(N); constant integer m_index = UInt(M); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

<!-- image -->

&lt;Rd&gt;

## &lt;Rn&gt;

Is the first general-purpose source register holding the multiplicand in the bottom or top half (selected by &lt;x&gt; ), encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register holding the multiplier in the bottom or top half (selected by &lt;y&gt; ), encoded in the 'Rm' field.

## &lt;Ra&gt;

Is the third general-purpose source register holding the addend, encoded in the 'Ra' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(16) operand1 = Elem[R[n], n_index, 16]; constant bits(16) operand2 = Elem[R[m], m_index, 16]; constant integer result = SInt(operand1) * SInt(operand2) + SInt(R[a]); R[d] = result<31:0>; if result != SInt(result<31:0>) then // Signed overflow PSTATE.Q = '1';
```