## F5.1.201 SMLSLD, SMLSLDX

Signed Multiply Subtract Long Dual

Signed Multiply Subtract Long Dual performs two signed 16 x 16-bit multiplications. It adds the difference of the products to a 64-bit accumulate operand.

Optionally, the instruction can exchange the halfwords of the second operand before performing the arithmetic. This produces top x bottom and bottom x top multiplication.

Overflow is possible during this instruction, but only as a result of the 64-bit addition. This overflow is not detected if it occurs. Instead, the result wraps around modulo 2 64 .

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMLSLD variant

```
Applies when (M == 0) SMLSLD{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the SMLSLDX variant

```
Applies when (M == 1) SMLSLDX{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer dLo = UInt(RdLo); constant integer dHi = UInt(RdHi); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_swap = (M == '1'); if dLo == 15 || dHi == 15 || n == 15 || m == 15 then if dHi == dLo then UNPREDICTABLE;
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

## Encoding for the SMLSLD variant

```
Applies when (M == 0)
```

```
SMLSLD{<c>}{<q>} <RdLo>, <RdHi>, <Rn>,
```

## Encoding for the SMLSLDX variant

Applies when

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

```
(M == 1) SMLSLDX{<c>}{<q>}
```

## Decode for all variants of this encoding

```
constant integer dLo = UInt(RdLo); constant integer dHi = UInt(RdHi); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_swap = (M == '1'); if dLo == 15 || dHi == 15 || n == 15 || m == 15 then // Armv8-A removes UPREDICTABLE for R13 if dHi == dLo then UNPREDICTABLE;
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

<!-- image -->

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;RdLo&gt;

Is the general-purpose source register holding the lower 32 bits of the addend, and the destination register for the lower 32 bits of the result, encoded in the 'RdLo' field.

## &lt;RdHi&gt;

Is the general-purpose source register holding the upper 32 bits of the addend, and the destination register for the upper 32 bits of the result, encoded in the 'RdHi' field.

```
<Rm>
```

## &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) operand2 = if m_swap then ROR(R[m],16) else R[m]; constant integer product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>); constant integer product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>); constant integer result = (product1 - product2) + SInt(R[dHi]:R[dLo]); R[dHi] = result<63:32>; R[dLo] = result<31:0>;
```