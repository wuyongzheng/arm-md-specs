## F5.1.197 SMLALBB, SMLALBT, SMLALTB, SMLALTT

Signed Multiply Accumulate Long (halfwords)

Signed Multiply Accumulate Long (halfwords) multiplies two signed 16-bit values to produce a 32-bit value, and accumulates this with a 64-bit value. The multiply acts on two signed 16-bit quantities, taken from either the bottom or the top half of their respective source registers. The other halves of these source registers are ignored. The 32-bit product is sign-extended and accumulated with a 64-bit accumulate value.

Overflow is possible during this instruction, but only as a result of the 64-bit addition. This overflow is not detected if it occurs. Instead, the result wraps around modulo 2 64 .

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMLALBB variant

```
Applies when (M == 0 && N == 0) SMLALBB{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLALBT variant

```
Applies when (M == 1 && N == 0) SMLALBT{<c>}{<q>}
```

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLALTB variant

```
Applies when (M == 0 && N == 1) SMLALTB{<c>}{<q>}
```

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLALTT variant

```
Applies when (M == 1 && N == 1) SMLALTT{<c>}{<q>}
```

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer dLo = UInt(RdLo); constant integer dHi = UInt(RdHi); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer n_index = UInt(N); constant integer m_index = UInt(M); if dLo == 15 || dHi == 15 || n == 15 || m == 15 then if dHi == dLo then UNPREDICTABLE;
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If dHi == dLo , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

T1

<!-- image -->

## Encoding for the SMLALBB variant

```
Applies when (N == 0 && M == 0) SMLALBB{<c>}{<q>}
```

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLALBT variant

```
Applies when (N == 0 && M == 1) SMLALBT{<c>}{<q>}
```

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLALTB variant

```
Applies when (N == 1 && M == 0) SMLALTB{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLALTT variant

```
Applies when (N == 1 && M == 1) SMLALTT{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer dLo = UInt(RdLo); constant integer dHi = UInt(RdHi); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer n_index = UInt(N); constant integer m_index = UInt(M); if dLo == 15 || dHi == 15 || n == 15 || m == 15 then // Armv8-A removes UNPREDICTABLE for R13 if dHi == dLo then UNPREDICTABLE;
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If dHi == dLo , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;RdLo&gt;

Is the general-purpose source register holding the lower 32 bits of the addend, and the destination register for the lower 32 bits of the result, encoded in the 'RdLo' field.

## &lt;RdHi&gt;

Is the general-purpose source register holding the upper 32 bits of the addend, and the destination register for the upper 32 bits of the result, encoded in the 'RdHi' field.

## &lt;Rn&gt;

For the 'A1 SMLALBB', 'A1 SMLALBT', 'A1 SMLALTB', and 'A1 SMLALTT' variants: is the first general-purpose source register holding the multiplicand in the bottom or top half (selected by &lt;x&gt; ), encoded in the 'Rn' field.

For the 'T1 SMLALBB', 'T1 SMLALBT', 'T1 SMLALTB', and 'T1 SMLALTT' variants: is the first general-purpose source register holding the multiplicand in the bottom or top half (selected by &lt;x&gt;), encoded in the 'Rn' field.

## &lt;Rm&gt;

For the 'A1 SMLALBB', 'A1 SMLALBT', 'A1 SMLALTB', and 'A1 SMLALTT' variants: is the second general-purpose source register holding the multiplier in the bottom or top half (selected by &lt;y&gt; ), encoded in the 'Rm' field.

For the 'T1 SMLALBB', 'T1 SMLALBT', 'T1 SMLALTB', and 'T1 SMLALTT' variants: is the second general-purpose source register holding the multiplier in the bottom or top half (selected by &lt;x&gt;), encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(16) operand1 = Elem[R[n], n_index, 16]; constant bits(16) operand2 = Elem[R[m], m_index, 16]; constant integer result = SInt(operand1) * SInt(operand2) + SInt(R[dHi]:R[dLo]); R[dHi] = result<63:32>; R[dLo] = result<31:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.