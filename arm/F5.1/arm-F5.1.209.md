## F5.1.209 SMUSD, SMUSDX

Signed Multiply Subtract Dual

Signed Multiply Subtract Dual performs two signed 16 x 16-bit multiplications. It subtracts one of the products from the other, and writes the result to the destination register.

Optionally, the instruction can exchange the halfwords of the second operand before performing the arithmetic. This produces top x bottom and bottom x top multiplication.

Overflow cannot occur.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMUSD variant

```
Applies when (M == 0) SMUSD{<c>}{<q>} {<Rd>, }<Rn>,
```

```
<Rm>
```

## Encoding for the SMUSDX variant

```
Applies when (M == 1) SMUSDX{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_swap = (M == '1'); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding for the SMUSD variant

Applies when

```
(M == 0) SMUSD{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

```
UNPREDICTABLE;
```

## Encoding for the SMUSDX variant

Applies when

```
(M == 1)
```

```
SMUSDX{<c>}{<q>}
```

```
{<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_swap = (M == '1'); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
```

```
UNPREDICTABLE;
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

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) operand2 = if m_swap then ROR(R[m],16) else R[m]; constant integer product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>); constant integer product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>); constant integer result = product1 - product2; R[d] = result<31:0>; // Signed overflow cannot occur
```