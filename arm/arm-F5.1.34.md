## F5.1.34 CMN (register)

Compare Negative (register) adds a register value and an optionally-shifted register value. It updates the condition flags based on the result, and discards the result.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

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
CMN{<c>}{<q>} <Rn>, <Rm>, RRX
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm5 == 00000 && stype == 11)) CMN{<c>}{<q>} <Rn>, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5);
```

T1

## Encoding

```
CMN{<c>}{<q>} <Rn>, <Rm>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0;
```

<!-- image -->

T2

<!-- image -->

## Encoding for the Rotate right with extend variant

```
Applies when (imm3 == 000 && imm2 == 00 && stype == 11)
```

```
CMN{<c>}{<q>} <Rn>, <Rm>, RRX
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
CMN{<c>}{<q>} <Rn>, <Rm> {, <shift> #<amount>}
```

```
CMN{<c>}.W <Rn>, <Rm> // (<Rn>, <Rm> can be represented in T1)
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, // Armv8-A removes UNPREDICTABLE for R13 if n == 15 || m == 15 then UNPREDICTABLE;
```

```
imm3:imm2);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Rotate right with extend' and 'A1 Shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2 Rotate right with extend', and 'T2 Shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

For the 'A1 Rotate right with extend' and 'A1 Shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2 Rotate right with extend', and 'T2 Shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

&lt;q&gt;

## &lt;Rn&gt;

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

For the 'A1 Shift or rotate by value' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T2 Shift or rotate by value' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], shifted, '0'); PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.