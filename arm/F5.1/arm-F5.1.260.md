## F5.1.260 TEQ (register)

Test Equivalence (register) performs a bitwise exclusive-OR operation on a register value and an optionally-shifted register value. It updates the condition flags based on the result, and discards the result.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Rotate right with extend variant

```
Applies when (imm5 == 00000 && stype
```

```
== 11)
```

```
TEQ{<c>}{<q>} <Rn>, <Rm>, RRX
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm5 == 00000 && stype == 11)) TEQ{<c>}{<q>} <Rn>, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype,
```

T1

<!-- image -->

## Encoding for the Rotate right with extend variant

```
Applies when (imm3 == 000 && imm2 == 00 && stype ==
```

```
TEQ{<c>}{<q>} <Rn>, <Rm>, RRX
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm3 == 000 && imm2 == 00 && stype ==
```

```
TEQ{<c>}{<q>} <Rn>, <Rm> {, <shift>
```

```
#<amount>}
```

```
11))
```

```
imm5);
```

```
11)
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, // Armv8-A removes UNPREDICTABLE for R13 if n == 15 || m == 15 then UNPREDICTABLE;
```

```
imm3:imm2);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Rotate right with extend' and 'A1 Shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1 Rotate right with extend' and 'T1 Shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

For the 'A1 Rotate right with extend' and 'A1 Shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1 Rotate right with extend' and 'T1 Shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

&lt;q&gt;

## &lt;Rn&gt;

## &lt;amount&gt;

For the 'A1 Shift or rotate by value' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T1 Shift or rotate by value' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) result = R[n] EOR shifted; PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.