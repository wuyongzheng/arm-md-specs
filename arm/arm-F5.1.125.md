## F5.1.125 MVN, MVNS (register)

Bitwise NOT (register) writes the bitwise inverse of a register value to the destination register.

If the destination register is not the PC, the MVNS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. ARM deprecates any use of these encodings. However, when the destination register is the PC:

- The MVN variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The MVNS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the MVN, rotate right with extend variant

```
Applies when (S == 0 && imm5 == 00000 && stype == 11)
```

```
MVN{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MVN, shift or rotate by value variant

```
Applies when (S == 0 && !(imm5 == 00000 && stype == 11)) MVN{<c>}{<q>} <Rd>, <Rm> {, <shift> #<amount>}
```

## Encoding for the MVNS, rotate right with extend variant

```
Applies when (S == 1 && imm5 == 00000 && stype ==
```

```
MVNS{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MVNS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm5 == 00000 && stype ==
```

```
MVNS{<c>}{<q>} <Rd>, <Rm> {, <shift>
```

```
11)) #<amount>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5);
```

```
11)
```

T1

## Encoding

```
MVN<c>{<q>} <Rd>, <Rm> // (InITBlock())
```

```
MVNS{<q>} <Rd>, <Rm> // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = !InITBlock(); constant SRType shift_t = SRType_LSL; constant integer shift_n = 0;
```

T2

<!-- image -->

## Encoding for the MVN, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype == 11)
```

```
MVN{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MVN, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
MVN{<c>}{<q>} <Rd>, <Rm> {, <shift> #<amount>}
```

```
MVN<c>.W <Rd>, <Rm> // (Inside IT block, and <Rd>, <Rm> can be represented in T1)
```

## Encoding for the MVNS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && imm2 == 00 && stype == 11)
```

```
MVNS{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MVNS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
MVNS{<c>}{<q>} <Rd>, <Rm> {, <shift> #<amount>}
```

```
MVNS.W <Rd>, <Rm> // (Outside IT block, and <Rd>, <Rm> can be represented in T1)
```

<!-- image -->

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

```
imm3:imm2);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 MVN, rotate right with extend', 'A1 MVN, shift or rotate by value', 'A1 MVNS, rotate right with extend', and 'A1 MVNS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. Arm deprecates using the PC as the destination register, but if the PC is used:

- For the MVN variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the MVNS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T1', 'T2 MVN, rotate right with extend', 'T2 MVN, shift or rotate by value', 'T2 MVNS, rotate right with extend', and 'T2 MVNS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1 MVN, rotate right with extend', 'A1 MVN, shift or rotate by value', 'A1 MVNS, rotate right with extend', and 'A1 MVNS, shift or rotate by value' variants: is the general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T1', 'T2 MVN, rotate right with extend', 'T2 MVN, shift or rotate by value', 'T2 MVNS, rotate right with extend', and 'T2 MVNS, shift or rotate by value' variants: is the general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

<!-- image -->

## &lt;Rd&gt;

## &lt;amount&gt;

For the 'A1 MVN, shift or rotate by value' and 'A1 MVNS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T2 MVN, shift or rotate by value' and 'T2 MVNS, shift or rotate by value' variants: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, constant bits(32) result = NOT(shifted); if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

```
PSTATE.C);
```