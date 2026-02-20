## F5.1.208 SMULWB, SMULWT

Signed Multiply (word by halfword)

Signed Multiply (word by halfword) multiplies a signed 32-bit quantity and a signed 16-bit quantity. The signed 16-bit quantity is taken from either the bottom or the top half of its source register. The other half of the second source register is ignored. The top 32 bits of the 48-bit product are written to the destination register. The bottom 16 bits of the 48-bit product are ignored. No overflow is possible during this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMULWB variant

```
Applies when (M == 0) SMULWB{<c>}{<q>}
```

```
{<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULWT variant

```
Applies when (M == 1) SMULWT{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_high = (M == '1'); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding for the SMULWB variant

```
Applies when (M == 0) SMULWB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMULWT variant

```
Applies when (M == 1) SMULWT{<c>}{<q>}
```

```
{<Rd>, }<Rn>, <Rm>
```

```
UNPREDICTABLE;
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean m_high = (M == '1'); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
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

## &lt;Rn&gt;

Is the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register holding the multiplier in the bottom or top half (selected by &lt;y&gt; ), encoded in the 'Rm' field.

## Operation

if

```
ConditionPassed() then EncodingSpecificOperations(); constant bits(16) operand2 = if m_high then R[m]<31:16> else R[m]<15:0>; constant integer product = SInt(R[n]) * SInt(operand2); R[d] = product<47:16>; // Signed overflow cannot occur
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.