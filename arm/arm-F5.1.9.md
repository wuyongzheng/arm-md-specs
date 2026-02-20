## F5.1.9 ADD, ADDS (SP plus register)

Add to SP (register) adds an optionally-shifted register value to the SP value, and writes the result to the destination register.

If the destination register is not the PC, the ADDS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. Arm deprecates any use of these encodings. However, when the destination register is the PC:

- The ADD variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The ADDS variant of the instruction performs an exception return without the use of the stack. In this case:
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
ADD{<c>}{<q>} {<Rd>, }SP, <Rm> ,
```

```
11) RRX
```

## Encoding for the ADD, shift or rotate by value variant

```
Applies when (S == 0 && !(imm5 == 00000 && stype == 11)) ADD{<c>}{<q>} {<Rd>, }SP, <Rm> {, <shift> #<amount>}
```

## Encoding for the ADDS, rotate right with extend variant

```
Applies when (S == 1 && imm5 == 00000 && stype ==
```

```
11) ADDS{<c>}{<q>} {<Rd>, }SP, <Rm> , RRX
```

## Encoding for the ADDS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm5 == 00000 && stype == 11)) ADDS{<c>}{<q>} {<Rd>, }SP, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm5);
```

T1

## Encoding

```
ADD{<c>}{<q>} {<Rdm>, }SP, <Rdm>
```

## Decode for this encoding

```
constant integer d = UInt(DM:Rdm); constant integer m = UInt(DM:Rdm); constant boolean setflags = FALSE; constant SRType shift_t = SRType_LSL; constant integer shift_n = 0; if d == 15 &&
```

T2

## Encoding

```
ADD{<c>}{<q>} {SP, }SP, <Rm>
```

## Decode for this encoding

```
if Rm == '1101' then SEE "encoding T1"; constant integer d = 13; constant integer m = UInt(Rm); constant boolean setflags = FALSE; constant SRType shift_t = SRType_LSL; constant integer shift_n = 0;
```

T3

<!-- image -->

## Encoding for the ADD, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype == 11)
```

```
ADD{<c>}{<q>} {<Rd>, }SP, <Rm>, RRX
```

```
InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

<!-- image -->

<!-- image -->

## Encoding for the ADD, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype ==
```

```
ADD{<c>}{<q>} {<Rd>, }SP, <Rm> {, <shift>
```

```
ADD{<c>}.W {<Rd>, }SP, <Rm> // (<Rd>, <Rm> can be represented in T1 or
```

```
11)) #<amount>} T2)
```

## Encoding for the ADDS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && Rd != 1111 && imm2 == 00 && stype == 11)
```

```
ADDS{<c>}{<q>} {<Rd>, }SP, <Rm>, RRX
```

## Encoding for the ADDS, shift or rotate by value variant

```
Applies when (S == 1 && Rd != 1111 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
ADDS{<c>}{<q>} {<Rd>, }SP, <Rm> {, <shift> #<amount>}
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "CMN (register)"; constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if (d == 15 && !setflags) || m == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 ADD, rotate right with extend', 'A1 ADD, shift or rotate by value', 'A1 ADDS, rotate right with extend', and 'A1 ADDS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the SP . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the ADD variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the ADDS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T3 ADD, rotate right with extend', 'T3 ADD, shift or rotate by value', 'T3 ADDS, rotate right with extend', and 'T3 ADDS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the SP .

<!-- image -->

## &lt;Rd&gt;

## &lt;Rm&gt;

For the 'A1 ADD, rotate right with extend', 'A1 ADD, shift or rotate by value', 'A1 ADDS, rotate right with extend', 'A1 ADDS, shift or rotate by value', and 'T2' variants: is the second general-purpose source register, encoded in the 'Rm' field. The PC can be used, but this is deprecated.

For the 'T3 ADD, rotate right with extend', 'T3 ADD, shift or rotate by value', 'T3 ADDS, rotate right with extend', and 'T3 ADDS, shift or rotate by value' variants: is the second general-purpose source register, encoded in the 'Rm' field.

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

## &lt;Rdm&gt;

Is the general-purpose destination and second source register, encoded in the 'Rdm' field. If omitted, this register is the SP. Arm deprecates using the PC as the destination register, but if the PC is used, the instruction is a branch to the address calculated by the operation. This is a simple branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

## SP

Is the stack pointer.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[13], shifted, '0'); if d == 15 then if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```