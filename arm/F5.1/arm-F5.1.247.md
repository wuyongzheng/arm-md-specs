## F5.1.247 SUB, SUBS (register)

Subtract (register) subtracts an optionally-shifted register value from a register value, and writes the result to the destination register.

If the destination register is not the PC, the SUBS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. However, when the destination register is the PC:

- The SUB variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The SUBS variant of the instruction performs an exception return without the use of the stack. Arm deprecates use of this instruction. However, in this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the SUB, rotate right with extend variant

```
Applies when (S == 0 && imm5 == 00000 && stype == 11) SUB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the SUB, shift or rotate by value variant

```
Applies when (S == 0 && !(imm5 == 00000 && stype == SUB{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

## Encoding for the SUBS, rotate right with extend variant

```
Applies when
```

```
(S == 1 && imm5 == 00000 && stype == 11) SUBS{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the SUBS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm5 == 00000 && stype == SUBS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

```
11))
```

```
11))
```

## Decode for all variants of this encoding

```
if Rn == '1101' then SEE "SUB (SP minus register)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5);
```

T1

## Encoding

```
SUB<c>{<q>} <Rd>, <Rn>, <Rm> // (InITBlock()) SUBS{<q>} {<Rd>, }<Rn>, <Rm> // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = !InITBlock(); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0;
```

T2

<!-- image -->

## Encoding for the SUB, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype == 11) SUB{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the SUB, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype ==
```

```
SUB{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift>
```

```
11)) #<amount>}
```

```
SUB<c>.W {<Rd>, }<Rn>, <Rm> // (Inside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1)
```

<!-- image -->

## Encoding for the SUBS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && Rd != 1111 && imm2 == 00 && stype ==
```

```
SUBS{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the SUBS, shift or rotate by value variant

```
Applies when (S == 1 && Rd != 1111 && !(imm3 == 000 && imm2 == 00 && stype == 11)) SUBS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>} SUBS.W {<Rd>, }<Rn>, <Rm> // (Outside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1)
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "CMP (register)"; if Rn == '1101' then SEE "SUB (SP minus register)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if (d == 15 && !setflags) || n == 15 || m == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;Rd&gt;

<!-- image -->

## &lt;Rn&gt;

For the 'A1 SUB, rotate right with extend', 'A1 SUB, shift or rotate by value', 'A1 SUBS, rotate right with extend', and 'A1 SUBS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the SUB variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the SUBS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T1', 'T2 SUB, rotate right with extend', 'T2 SUB, shift or rotate by value', 'T2 SUBS, rotate right with extend', and 'T2 SUBS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 SUB, rotate right with extend', 'A1 SUB, shift or rotate by value', 'A1 SUBS, rotate right with extend', and 'A1 SUBS, shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated. If the SP is used, see SUB (SP minus register).

For the 'T1' variant: is the first general-purpose source register, encoded in the 'Rn' field.

For the 'T2 SUB, rotate right with extend', 'T2 SUB, shift or rotate by value', 'T2 SUBS, rotate right with extend', and 'T2 SUBS, shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. If the SP is used, see SUB (SP minus register).

## &lt;Rm&gt;

For the 'A1 SUB, rotate right with extend', 'A1 SUB, shift or rotate by value', 'A1 SUBS, rotate right with extend', and 'A1 SUBS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2 SUB, rotate right with extend', 'T2 SUB, shift or rotate by value', 'T2 SUBS, rotate right with extend', and 'T2 SUBS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

For the 'A1 SUB, shift or rotate by value' and 'A1 SUBS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR) encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T2 SUB, shift or rotate by value' and 'T2 SUBS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], NOT(shifted), '1'); if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.