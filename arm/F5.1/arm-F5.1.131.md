## F5.1.131 ORR, ORRS (register)

Bitwise OR (register) performs a bitwise (inclusive) OR of a register value and an optionally-shifted register value, and writes the result to the destination register.

If the destination register is not the PC, the ORRS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. ARM deprecates any use of these encodings. However, when the destination register is the PC:

- The ORR variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The ORRS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the ORR, rotate right with extend variant

```
Applies when (S == 0 && imm5 == 00000 && stype == 11)
```

```
ORR{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ORR, shift or rotate by value variant

Applies when

```
ORR{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift>
```

```
(S == 0 && !(imm5 == 00000 && stype == 11)) #<amount>}
```

## Encoding for the ORRS, rotate right with extend variant

```
(S == 1 && imm5 == 00000 && stype ==
```

```
Applies when ORRS{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, RRX
```

```
11)
```

## Encoding for the ORRS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm5 == 00000 && stype == 11)) ORRS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5);
```

T1

## Encoding

ORR&lt;c&gt;{&lt;q&gt;}

{&lt;Rdn&gt;, }&lt;Rdn&gt;, &lt;Rm&gt;

<!-- image -->

// (InITBlock())

```
ORRS{<q>} {<Rdn>, }<Rdn>, <Rm> // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rdn); constant integer n = UInt(Rdn); constant integer m = UInt(Rm); constant boolean setflags = !InITBlock(); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0;
```

T2

<!-- image -->

## Encoding for the ORR, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype ==
```

```
ORR{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ORR, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
ORR{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

```
ORR<c>.W {<Rd>, }<Rn>, <Rm> // (Inside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1)
```

## Encoding for the ORRS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && imm2 == 00 && stype ==
```

```
ORRS{<c>}{<q>}
```

```
11) {<Rd>, }<Rn>, <Rm>, RRX
```

## Encoding for the ORRS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
ORRS{<c>}{<q>} {<Rd>, }<Rn>, <Rm> {, <shift> #<amount>}
```

```
ORRS.W {<Rd>, }<Rn>, <Rm> // (Outside IT block, and <Rd>, <Rn>, <Rm> can be represented in T1)
```

## Decode for all variants of this encoding

```
imm3:imm2);
```

```
if Rn == '1111' then SEE "Related encodings"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

Related encodings: Data-processing (shifted register)

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;Rd&gt;

## &lt;Rn&gt;

For the 'A1 ORR, rotate right with extend', 'A1 ORR, shift or rotate by value', 'A1 ORRS, rotate right with extend', and 'A1 ORRS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the ORR variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the ORRS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T2 ORR, rotate right with extend', 'T2 ORR, shift or rotate by value', 'T2 ORRS, rotate right with extend', and 'T2 ORRS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 ORR, rotate right with extend', 'A1 ORR, shift or rotate by value', 'A1 ORRS, rotate right with extend', and 'A1 ORRS, shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T2 ORR, rotate right with extend', 'T2 ORR, shift or rotate by value', 'T2 ORRS, rotate right with extend', and 'T2 ORRS, shift or rotate by value' variants: is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

For the 'A1 ORR, rotate right with extend', 'A1 ORR, shift or rotate by value', 'A1 ORRS, rotate right with extend', and 'A1 ORRS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2 ORR, rotate right with extend', 'T2 ORR, shift or rotate by value', 'T2 ORRS, rotate right with extend', and 'T2 ORRS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

&lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

## &lt;amount&gt;

For the 'A1 ORR, shift or rotate by value' and 'A1 ORRS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T2 ORR, shift or rotate by value' and 'T2 ORRS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## &lt;Rdn&gt;

Is the first general-purpose source register and the destination register, encoded in the 'Rdn' field.

In T32 assembly:

- Outside an IT block, if ORRS &lt;Rd&gt;, &lt;Rn&gt;, &lt;Rd&gt; is written with &lt;Rd&gt; and &lt;Rn&gt; both in the range R0-R7, it is assembled using encoding T1 as though ORRS &lt;Rd&gt;, &lt;Rn&gt; had been written.
- Inside an IT block, if ORR&lt;c&gt; &lt;Rd&gt;, &lt;Rn&gt;, &lt;Rd&gt; is written with &lt;Rd&gt; and &lt;Rn&gt; both in the range R0-R7, it is assembled using encoding T1 as though ORR&lt;c&gt; &lt;Rd&gt;, &lt;Rn&gt; had been written.

To prevent either of these happening, use the .W qualifier.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) result = R[n] OR shifted; if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.