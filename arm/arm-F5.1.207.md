## F5.1.207 SMULL, SMULLS

Signed Multiply Long multiplies two 32-bit signed values to produce a 64-bit result.

In A32 instructions, the condition flags can optionally be updated based on the result. Use of this option adversely affects performance on many implementations.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Flag setting variant

```
Applies when (S == 1) SMULLS{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0) SMULL{<c>}{<q>}
```

```
<RdLo>, <RdHi>, <Rn>, <Rm>
```

## Decode for all variants of this encoding

```
constant integer dLo = UInt(RdLo); constant integer dHi = UInt(RdHi); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); if dLo == 15 || dHi == 15 || n == 15 || m == 15 then if dHi == dLo then UNPREDICTABLE;
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

## Encoding

```
SMULL{<c>}{<q>} <RdLo>, <RdHi>, <Rn>, <Rm>
```

## Decode for this encoding

```
constant integer dLo = UInt(RdLo); constant integer dHi = UInt(RdHi); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = FALSE; if dLo == 15 || dHi == 15 || n == 15 || m == 15 then // Armv8-A removes UNPREDICTABLE for R13 if dHi == dLo then UNPREDICTABLE;
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

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;RdLo&gt;

Is the general-purpose destination register for the lower 32 bits of the result, encoded in the 'RdLo' field.

## &lt;RdHi&gt;

Is the general-purpose destination register for the upper 32 bits of the result, encoded in the 'RdHi' field.

## &lt;Rn&gt;

Is the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer result = SInt(R[n]) * R[dHi] = result<63:32>; R[dLo] = result<31:0>; if setflags then PSTATE.N = result<63>; PSTATE.Z = IsZeroBit(result<63:0>); // PSTATE.C, PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
SInt(R[m]);
```