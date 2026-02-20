## F5.1.6 ADD, ADDS (register)

Add (register) adds a register value and an optionally-shifted register value, and writes the result to the destination register.

If the destination register is not the PC, the ADDS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. If the destination register is the PC:

- The ADD variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The ADDS variant of the instruction performs an exception return without the use of the stack. Arm deprecates use of this instruction. However, in this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the ADD, rotate right with extend variant

```
Applies when (S == 0 && imm5 == 00000 && stype ==
```

```
ADD{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ADD, shift or rotate by value variant

```
Applies when (S == 0 && !(imm5 == 00000 && stype == ADD{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

## Encoding for the ADDS, rotate right with extend variant

```
Applies when (S == 1 && imm5 == 00000 && stype ==
```

```
11) ADDS{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ADDS, shift or rotate by value variant

```
Applies when
```

```
ADDS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift>
```

```
(S == 1 && !(imm5 == 00000 && stype == #<amount>}
```

```
11))
```

```
11))
```

## Decode for all variants of this encoding

```
if Rn == '1101' then SEE "ADD (SP plus register)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5);
```

T1

## Encoding

```
ADD<c>{<q>} <Rd>, <Rn>, <Rm> // (InITBlock()) ADDS{<q>} {<Rd>, }<Rn>, <Rm> // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = !InITBlock(); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0;
```

T2

## Encoding

```
Applies when (!(DN == '1' && Rdn == '101'))
```

```
ADD{<c>}{<q>} {<Rdn>, }<Rdn>, <Rm>
```

```
ADD<c>{<q>} <Rdn>, <Rm> // (Preferred syntax, Inside IT block)
```

<!-- image -->

<!-- image -->

## Decode for this encoding

```
if (DN:Rdn) == '1101' || Rm == '1101' then SEE "ADD (SP plus register)"; constant integer d = UInt(DN:Rdn); constant integer n = d; constant integer m = UInt(Rm); constant boolean setflags = FALSE; constant SRType shift_t = SRType_LSL; constant integer shift_n = 0; if n == 15 && m == 15 then UNPREDICTABLE; if d == 15 && InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

T3

<!-- image -->

## Encoding for the ADD, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype == 11)
```

```
ADD{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ADD, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype ==
```

```
11)) ADD{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>} ADD<c>.W {<Rd>, }<Rn>, <Rm> // (Inside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1) ADD{<c>}.W {<Rd>, }<Rn>, <Rm> // (<Rd> == <Rn>, and <Rd>, <Rn>, <Rm> can be represented in T2)
```

## Encoding for the ADDS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && Rd != 1111 && imm2 == 00 && stype == 11)
```

```
ADDS{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ADDS, shift or rotate by value variant

```
Applies when (S == 1 && Rd != 1111 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
ADDS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

```
ADDS.W {<Rd>, }<Rn>, <Rm> // (Outside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1 or T2)
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "CMN (register)"; if Rn == '1101' then SEE "ADD (SP plus register)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if (d == 15 && !setflags) || n == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;Rd&gt;

## &lt;Rn&gt;

For the 'A1 ADD, rotate right with extend', 'A1 ADD, shift or rotate by value', 'A1 ADDS, rotate right with extend', and 'A1 ADDS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . If the PC is used:

- For the ADD variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the ADDS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;. Arm deprecates use of this instruction.

For the 'T1' variant: is the general-purpose destination register, encoded in the 'Rd' field.

When used inside an IT block, &lt;Rd&gt; must be specified. When used outside an IT block, &lt;Rd&gt; is optional, and:

- If omitted, this register is the same as &lt;Rn&gt; .
- If present, encoding T1 is preferred to encoding T2.

For the 'T3 ADD, rotate right with extend', 'T3 ADD, shift or rotate by value', 'T3 ADDS, rotate right with extend', and 'T3 ADDS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 ADD, rotate right with extend', 'A1 ADD, shift or rotate by value', 'A1 ADDS, rotate right with extend', and 'A1 ADDS, shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used. If the SP is used, see ADD (SP plus register).

For the 'T1' variant: is the first general-purpose source register, encoded in the 'Rn' field.

For the 'T3 ADD, rotate right with extend', 'T3 ADD, shift or rotate by value', 'T3 ADDS, rotate right with extend', and 'T3 ADDS, shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. If the SP is used, see ADD (SP plus register).

## &lt;Rm&gt;

For the 'A1 ADD, rotate right with extend', 'A1 ADD, shift or rotate by value', 'A1 ADDS, rotate right with extend', and 'A1 ADDS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1', 'T3 ADD, rotate right with extend', 'T3 ADD, shift or rotate by value', 'T3 ADDS, rotate right with extend', and 'T3 ADDS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

For the 'T2' variant: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

For the 'A1 ADD, shift or rotate by value' and 'A1 ADDS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T3 ADD, shift or rotate by value' and 'T3 ADDS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## &lt;Rdn&gt;

Is the general-purpose source and destination register, encoded in the 'DN:Rdn' field. If the PC is used, the instruction is a branch to the address calculated by the operation. This is a simple branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

The assembler language allows &lt;Rdn&gt; to be specified once or twice in the assembler syntax. When used inside an IT block, and &lt;Rdn&gt; and &lt;Rm&gt; are in the range R0 to R7, &lt;Rdn&gt; must be specified once so that encoding T2 is preferred to encoding T1. In all other cases there is no difference in behavior when &lt;Rdn&gt; is specified once or twice.

Inside an IT block, if ADD&lt;c&gt; &lt;Rd&gt;, &lt;Rn&gt;, &lt;Rd&gt; cannot be assembled using encoding T1, it is assembled using encoding T2 as though ADD&lt;c&gt; &lt;Rd&gt;, &lt;Rn&gt; had been written. To prevent this happening, use the .W qualifier.

## Operation

```
if shift_t, shift_n, PSTATE.C);
```

```
ConditionPassed() then EncodingSpecificOperations(); constant bits(32) shifted = Shift(R[m], bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], shifted, '0'); if d == 15 then if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.