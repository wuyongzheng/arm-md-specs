## F5.1.37 CMP (register)

Compare (register) subtracts an optionally-shifted register value from a register value. It updates the condition flags based on the result, and discards the result.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

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
CMP{<c>}{<q>} <Rn>, <Rm>, RRX
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm5 == 00000 && stype == 11)) CMP{<c>}{<q>} <Rn>, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype,
```

T1

## Encoding

```
CMP{<c>}{<q>} <Rn>, <Rm> // (<Rn> and <Rm> both from R0-R7)
```

## Decode for this encoding

```
shift_t = SRType_LSL;
```

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant SRType constant integer shift_n = 0;
```

```
imm5);
```

<!-- image -->

T2

## Encoding

```
CMP{<c>}{<q>} <Rn>, <Rm> // (<Rn> and <Rm> not both from R0-R7)
```

## Decode for this encoding

```
constant integer n = UInt(N:Rn); constant integer m = UInt(Rm); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0; if n < 8 && m < 8 then UNPREDICTABLE; if n == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If n &lt; 8 &amp;&amp; m &lt; 8 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The condition flags become UNKNOWN.

T3

<!-- image -->

## Encoding for the Rotate right with extend variant

```
Applies when (imm3 == 000 && imm2 == 00 && stype == 11)
```

```
CMP{<c>}{<q>} <Rn>, <Rm>, RRX
```

## Encoding for the Shift or rotate by value variant

```
Applies when (!(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
CMP{<c>}{<q>} <Rn>, <Rm>, <shift>
```

```
CMP{<c>}.W <Rn>, <Rm> // (<Rn>, <Rm> can be represented in T1 or
```

```
#<amount> T2)
```

<!-- image -->

## Decode for all variants of this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if n == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 Rotate right with extend' and 'A1 Shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1', 'T3 Rotate right with extend', and 'T3 Shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field.

For the 'T2' variant: is the first general-purpose source register, encoded in the 'N:Rn' field.

## &lt;Rm&gt;

For the 'A1 Rotate right with extend' and 'A1 Shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2', 'T3 Rotate right with extend', and 'T3 Shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

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

For the 'T3 Shift or rotate by value' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], NOT(shifted), '1'); PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.