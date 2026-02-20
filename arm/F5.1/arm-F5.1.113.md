## F5.1.113 MOV, MOVS (register)

Move (register) copies a value from a register to the destination register.

If the destination register is not the PC, the MOVS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. If the destination register is the PC:

- The MOV variant of the instruction is a branch. In the T32 instruction set (encoding T1) this is a simple branch, and in the A32 instruction set it is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The MOVS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

This instruction is used by the aliases ASRS (immediate), ASR (immediate), LSLS (immediate), LSL (immediate), LSRS (immediate), LSR (immediate), RORS (immediate), ROR (immediate), RRXS, and RRX.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the MOV, rotate right with extend variant

```
Applies when (S == 0 && imm5 == 00000 && stype == 11)
```

```
MOV{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MOV, shift or rotate by value variant

```
Applies when 11))
```

```
MOV{<c>}{<q>} <Rd>, <Rm> {, <shift>
```

```
(S == 0 && !(imm5 == 00000 && stype == #<amount>}
```

## Encoding for the MOVS, rotate right with extend variant

```
Applies when (S == 1 && imm5 == 00000 && stype ==
```

```
MOVS{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MOVS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm5 == 00000 && stype ==
```

```
MOVS{<c>}{<q>} <Rd>, <Rm> {, <shift>
```

```
11)) #<amount>}
```

```
11)
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype,
```

T1

## Encoding

```
MOV{<c>}{<q>} <Rd>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(D:Rd); constant integer m = UInt(Rm); constant boolean setflags = FALSE; constant SRType shift_t = SRType_LSL; constant integer shift_n = 0; if d == 15 &&
```

T2

## Encoding

```
MOV<c>{<q>} <Rd>, <Rm> {, <shift> #<amount>} // (InITBlock()) MOVS{<q>} <Rd>, <Rm> {, <shift> #<amount>} // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = !InITBlock(); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(op, imm5); if op == '00' && imm5 == '00000' && InITBlock() then UNPREDICTABLE;
```

```
InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

<!-- image -->

```
imm5);
```

<!-- image -->

## CONSTRAINED UNPREDICTABLE behavior

If op == '00' &amp;&amp; imm5 == '00000' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passed its condition code check.
- The instruction executes as NOP , as if it failed its condition code check.
- The instruction executes as MOV Rd, Rm.

<!-- image -->

## Encoding for the MOV, rotate right with extend variant

```
Applies when (S == 0 && imm3 == 000 && imm2 == 00 && stype == 11)
```

```
MOV{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MOV, shift or rotate by value variant

```
Applies when (S == 0 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
MOV{<c>}{<q>} <Rd>, <Rm> {, <shift> #<amount>}
```

```
MOV{<c>}.W <Rd>, <Rm> {, LSL #0} // (<Rd>, <Rm> can be represented in T1)
```

```
MOV<c>.W <Rd>, <Rm> {, <shift> #<amount>} // (Inside IT block, and <Rd>, <Rm>, <shift>, <amount> can be ↪ → represented in T2)
```

## Encoding for the MOVS, rotate right with extend variant

```
Applies when (S == 1 && imm3 == 000 && imm2 == 00 && stype ==
```

```
MOVS{<c>}{<q>} <Rd>, <Rm>, RRX
```

## Encoding for the MOVS, shift or rotate by value variant

```
Applies when (S == 1 && !(imm3 == 000 && imm2 == 00 && stype == 11))
```

```
MOVS{<c>}{<q>} <Rd>, <Rm> {, <shift> #<amount>}
```

```
MOVS.W <Rd>, <Rm> {, <shift> #<amount>} // (Outside IT block, and <Rd>, <Rm>, <shift>, <amount> can be ↪ → represented in T1 or T2)
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant boolean setflags = (S == '1'); SRType shift_t; integer shift_n; (shift_t, shift_n) = DecodeImmShift(stype, // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || m == 15 then UNPREDICTABLE;
```

```
imm3:imm2);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
11)
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 MOV, rotate right with extend', 'A1 MOV, shift or rotate by value', 'A1 MOVS, rotate right with extend', and 'A1 MOVS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field. If the PC is used:

- For the MOV variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC. Arm deprecates use of the instruction if &lt;Rn&gt; is the PC.
- For the MOVS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;. Arm deprecates use of the instruction if &lt;Rn&gt; is not the LR, or if the optional shift or RRX argument is specified.

For the 'T1' variant: is the general-purpose destination register, encoded in the 'D:Rd' field. If the PC is used:

- The instruction causes a branch to the address moved to the PC. This is a simple branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The instruction must either be outside an IT block or the last instruction of an IT block.

For the 'T2', 'T3 MOV, rotate right with extend', 'T3 MOV, shift or rotate by value', 'T3 MOVS, rotate right with extend', and 'T3 MOVS, shift or rotate by value' variants: is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1 MOV, rotate right with extend', 'A1 MOV, shift or rotate by value', 'A1 MOVS, rotate right with extend', 'A1 MOVS, shift or rotate by value', and 'T1' variants: is the general-purpose source register, encoded in the 'Rm' field. The PC can be used. Arm deprecates use of the instruction if &lt;Rd&gt; is the PC.

For the 'T2', 'T3 MOV, rotate right with extend', 'T3 MOV, shift or rotate by value', 'T3 MOVS, rotate right with extend', and 'T3 MOVS, shift or rotate by value' variants: is the general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

For the 'A1 MOV, shift or rotate by value', 'A1 MOVS, shift or rotate by value', 'T3 MOV , shift or rotate by value', and 'T3 MOVS, shift or rotate by value' variants: is the type of shift to be applied to the source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

For the 'T2' variant: is the type of shift to be applied to the source register, encoded in 'op':

&lt;q&gt;

## &lt;Rd&gt;

## &lt;amount&gt;

For the 'A1 MOV, shift or rotate by value' and 'A1 MOVS, shift or rotate by value' variants: is the shift amount, in the range 0 to 31 (when &lt;shift&gt; = LSL), or 1 to 31 (when &lt;shift&gt; = ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T2' variant: is the shift amount, in the range 1 to 31 (when &lt;shift&gt; = LSL or ROR) or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm5' field as &lt;amount&gt; modulo 32.

For the 'T3 MOV, shift or rotate by value' and 'T3 MOVS, shift or rotate by value' variants: is the shift amount, in the range 0 to 31 (when &lt;shift&gt; = LSL) or 1 to 31 (when &lt;shift&gt; = ROR), or 1 to 32 (when &lt;shift&gt; = LSR or ASR), encoded in the 'imm3:imm2' field as &lt;amount&gt; modulo 32.

## Alias Conditions

| Alias   |             | Of variant                                                           | Is preferred when                                                                                           |
|---------|-------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ASRS    | (immediate) | T3 MOVS, shift or rotate by value, A1 MOVS, shift or rotate by value | S == '1' && stype == '10'                                                                                   |
| ASRS    | (immediate) | T2                                                                   | op == '10' && !InITBlock()                                                                                  |
| ASRS    | (immediate) | T3 MOVS, shift or rotate by value                                    | Unconditionally                                                                                             |
| ASR     | (immediate) | T3 MOV, shift or rotate by value, A1 MOV, shift or rotate by value   | S == '0' && stype == '10'                                                                                   |
| ASR     | (immediate) | T2                                                                   | op == '10' && InITBlock()                                                                                   |
| ASR     | (immediate) | T3 MOV, shift or rotate by value                                     | Unconditionally                                                                                             |
| LSLS    | (immediate) | A1 MOVS, shift or rotate by value                                    | S == '1' && imm5 != '00000' && stype == '00'                                                                |
| LSLS    | (immediate) | T2                                                                   | op == '00' && imm5 != '00000' && !InITBlock()                                                               |
| LSLS    | (immediate) | T3 MOVS, shift or rotate by value                                    | (S == '1' && stype == '00' && !(imm3 == '000')) &#124;&#124; (S == '1' && stype == '00' && !(imm2 == '00')) |
| LSLS    | (immediate) | T3 MOVS, shift or rotate by value                                    | Unconditionally                                                                                             |
| LSL     | (immediate) | A1 MOV, shift or rotate by value                                     | S == '0' && imm5 != '00000' && stype == '00'                                                                |
| LSL     | (immediate) | T2                                                                   | op == '00' && imm5 != '00000' && InITBlock()                                                                |
| LSL     | (immediate) | T3 MOV, shift or rotate by value                                     | (S == '0' && stype == '00' && !(imm3 == '000')) &#124;&#124; (S == '0' && stype == '00' && !(imm2 == '00')) |

|   op | <shift>   |
|------|-----------|
|   00 | LSL       |
|   01 | LSR       |
|   10 | ASR       |

| Alias   |             | Of variant Is                                                        | preferred when                                                                                              |
|---------|-------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| LSL     | (immediate) | T3 MOV, shift or rotate by value                                     | Unconditionally                                                                                             |
| LSRS    | (immediate) | T3 MOVS, shift or rotate by value, A1 MOVS, shift or rotate by value | S == '1' && stype == '01'                                                                                   |
| LSRS    | (immediate) | T2                                                                   | op == '01' && !InITBlock()                                                                                  |
| LSRS    | (immediate) | T3 MOVS, shift or rotate by value                                    | Unconditionally                                                                                             |
| LSR     | (immediate) | T3 MOV, shift or rotate by value, A1 MOV, shift or rotate by value   | S == '0' && stype == '01'                                                                                   |
| LSR     | (immediate) | T2                                                                   | op == '01' && InITBlock()                                                                                   |
| LSR     | (immediate) | T3 MOV, shift or rotate by value                                     | Unconditionally                                                                                             |
| RORS    | (immediate) | A1 MOVS, shift or rotate by value                                    | S == '1' && imm5 != '00000' && stype == '11'                                                                |
| RORS    | (immediate) | T3 MOVS, shift or rotate by value                                    | (S == '1' && stype == '11' && !(imm3 == '000')) &#124;&#124; (S == '1' && stype == '11' && !(imm2 == '00')) |
| ROR     | (immediate) | A1 MOV, shift or rotate by value                                     | S == '0' && imm5 != '00000' && stype == '11'                                                                |
| ROR     | (immediate) | T3 MOV, shift or rotate by value                                     | (S == '0' && stype == '11' && !(imm3 == '000')) &#124;&#124; (S == '0' && stype == '11' && !(imm2 == '00')) |
| RRXS    |             | A1 MOVS, rotate right with extend                                    | S == '1' && imm5 == '00000' && stype == '11'                                                                |
| RRXS    |             | T3 MOVS, rotate right with extend                                    | S == '1' && imm3 == '000' && imm2 == '00' && stype == '11'                                                  |
| RRX     |             | A1 MOV, rotate right with extend                                     | S == '0' && imm5 == '00000' && stype == '11'                                                                |
| RRX     |             | T3 MOV, rotate right with extend                                     | S == '0' && imm3 == '000' && imm2 == '00' && stype == '11'                                                  |

## Operation

```
if ConditionPassed() then PSTATE.C);
```

```
EncodingSpecificOperations(); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, constant bits(32) result = shifted; if d == 15 then if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry;
```

// PSTATE.V unchanged

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.