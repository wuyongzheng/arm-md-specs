## F5.1.205 SMUAD, SMUADX

Signed Dual Multiply Add

Signed Dual Multiply Add performs two signed 16 x 16-bit multiplications. It adds the products together, and writes the result to the destination register.

Optionally, the instruction can exchange the halfwords of the second operand before performing the arithmetic. This produces top x bottom and bottom x top multiplication.

This instruction sets PSTATE.Q to 1 if the addition overflows. The multiplications cannot overflow.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMUAD variant

```
Applies when (M == 0) SMUAD{<c>}{<q>} {<Rd>, }<Rn>,
```

```
<Rm>
```

## Encoding for the SMUADX variant

```
Applies when (M == 1) SMUADX{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_swap = (M == '1'); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding for the SMUAD variant

Applies when

```
(M == 0) SMUAD{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

```
UNPREDICTABLE;
```

## Encoding for the SMUADX variant

Applies when

```
(M == 1)
```

```
SMUADX{<c>}{<q>}
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

&lt;Rd&gt;

- &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) operand2 = if m_swap then ROR(R[m],16) else R[m]; constant integer product1 = SInt(R[n]<15:0>) * SInt(operand2<15:0>); constant integer product2 = SInt(R[n]<31:16>) * SInt(operand2<31:16>); constant integer result = product1 + product2; R[d] = result<31:0>; if result != SInt(result<31:0>) then // Signed overflow PSTATE.Q = '1';
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.