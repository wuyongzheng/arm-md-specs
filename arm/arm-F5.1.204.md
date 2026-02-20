## F5.1.204 SMMUL, SMMULR

Signed Most Significant Word Multiply

Signed Most Significant Word Multiply multiplies two signed 32-bit values, extracts the most significant 32 bits of the result, and writes those bits to the destination register.

Optionally, the instruction can specify that the result is rounded instead of being truncated. In this case, the constant 0x80000000 is added to the product before the high word is extracted.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMMUL variant

```
Applies when (R == 0)
```

```
SMMUL{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMMULR variant

```
Applies when (R == 1) SMMULR{<c>}{<q>}
```

```
{<Rd>, }<Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean round = (R == '1'); if d == 15 || n == 15 || m == 15 then
```

T1

<!-- image -->

## Encoding for the SMMUL variant

```
Applies when (R == 0) SMMUL{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

## Encoding for the SMMULR variant

```
Applies when (R == 1) SMMULR{<c>}{<q>} {<Rd>, }<Rn>, <Rm>
```

```
UNPREDICTABLE;
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean round = (R == '1'); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
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

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); integer result = SInt(R[n]) * SInt(R[m]); if round then result = result R[d] = result<63:32>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
+ \texttt{0x80000000};
```