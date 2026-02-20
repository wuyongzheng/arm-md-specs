## F5.1.129 ORN, ORNS (register)

Bitwise OR NOT (register) performs a bitwise (inclusive) OR of a register value and the complement of an optionally-shifted register value, and writes the result to the destination register. It can optionally update the condition flags based on the result.

<!-- image -->

## Encoding for the ORN, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype == 11)
```

```
ORN{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ORN, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype == 11)) ORN{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

## Encoding for the ORNS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && imm2 == 00 && stype ==
```

```
ORNS{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ORNS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm3 == 000 && imm2 == 00 && stype ==
```

```
11)) ORNS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
if Rn == '1111' then SEE "MVN (register)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

```
imm3:imm2);
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

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

Is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) result = R[n] OR NOT(shifted); R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.