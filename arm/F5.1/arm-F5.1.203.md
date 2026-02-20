## F5.1.203 SMMLS, SMMLSR

Signed Most Significant Word Multiply Subtract

Signed Most Significant Word Multiply Subtract multiplies two signed 32-bit values, subtracts the result from a 32-bit accumulate value that is shifted left by 32 bits, and extracts the most significant 32 bits of the result of that subtraction.

Optionally, the instruction can specify that the result of the instruction is rounded instead of being truncated. In this case, the constant 0x80000000 is added to the result of the subtraction before the high word is extracted.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the SMMLS variant

```
Applies when (R == 0) SMMLS{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Encoding for the SMMLSR variant

```
Applies when (R == 1) SMMLSR{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); constant boolean round = (R == '1'); if d == 15 || n == 15 || m == 15 || a == 15 then
```

T1

<!-- image -->

## Encoding for the SMMLS variant

```
Applies when (R == 0) SMMLS{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Encoding for the SMMLSR variant

```
Applies when (R == 1) SMMLSR{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

```
UNPREDICTABLE;
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); constant boolean round = (R == '1'); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 || a == 15 then
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

&lt;Rn&gt;

Is the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

&lt;Rm&gt;

Is the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

&lt;Ra&gt;

Is the third general-purpose source register holding the addend, encoded in the 'Ra' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); integer result = (SInt(R[a]) << 32) -SInt(R[n]) * SInt(R[m]); if round then result = result + \texttt{0x80000000}; R[d] = result<63:32>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.