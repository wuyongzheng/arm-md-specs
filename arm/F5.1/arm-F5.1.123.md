## F5.1.123 MUL, MULS

Multiply multiplies two register values. The least significant 32 bits of the result are written to the destination register. These 32 bits do not depend on whether the source register values are considered to be signed values or unsigned values.

Optionally, it can update the condition flags based on the result. In the T32 instruction set, this option is limited to only a few forms of the instruction. Use of this option adversely affects performance on many implementations.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the Flag setting variant

```
Applies when (S == 1) MULS{<c>}{<q>} <Rd>, <Rn>{,
```

```
<Rm>}
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0) MUL{<c>}{<q>} <Rd>, <Rn>{, <Rm>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); if d == 15 || n == 15 || m == 15 then
```

T1

## Encoding

```
MUL<c>{<q>} <Rdm>, <Rn>{, <Rdm>} // (InITBlock()) MULS{<q>} <Rdm>, <Rn>{, <Rdm>} // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rdm); constant integer n = UInt(Rn); constant integer m = UInt(Rdm); constant boolean setflags = !InITBlock();
```

```
UNPREDICTABLE;
```

<!-- image -->

## T2

<!-- image -->

## Encoding

```
MUL{<c>}{<q>} <Rd>, <Rn>{, <Rm>} MUL<c>.W <Rd>, <Rn>{, <Rm>} // (Inside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = FALSE; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 then
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

## &lt;Rm&gt;

Is the second general-purpose source register holding the multiplier, encoded in the 'Rm' field. If omitted, &lt;Rd&gt; is used.

## &lt;Rdm&gt;

Is the second general-purpose source register holding the multiplier and the destination register, encoded in the 'Rdm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer operand1 = SInt(R[n]); // operand1 = UInt(R[n]) produces the same final results constant integer operand2 = SInt(R[m]); // operand2 = UInt(R[m]) produces the same final results constant integer result = operand1 * operand2; R[d] = result<31:0>; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result<31:0>); // PSTATE.C, PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.