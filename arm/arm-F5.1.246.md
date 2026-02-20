## F5.1.246 SUB, SUBS (immediate)

Subtract (immediate) subtracts an immediate value from a register value, and writes the result to the destination register.

If the destination register is not the PC, the SUBS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. If the destination register is the PC:

- The SUB variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The SUBS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode, except for encoding T5 with &lt;imm8&gt; set to zero, which is the encoding for the ERET instruction, see ERET.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, T3, T4, and T5).

A1

<!-- image -->

## Encoding for the SUB variant

```
Applies when (S == 0 && Rn != SUB{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

11x1)

## Encoding for the SUBS variant

```
Applies when (S == 1 && Rn != 1101) SUBS{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Decode for all variants of this encoding

```
immediate)";
```

<!-- image -->

```
if Rn == '1111' && S == '0' then SEE "ADR"; if Rn == '1101' then SEE "SUB (SP minus constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 = A32ExpandImm(imm12);
```

T1

## Encoding

```
SUB<c>{<q>} <Rd>, <Rn>, #<imm3> // (InITBlock()) SUBS{<q>} <Rd>, <Rn>, #<imm3> // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = !InITBlock(); constant bits(32) imm32 =
```

T2

## Encoding

```
SUB<c>{<q>} <Rdn>, #<imm8> // (InITBlock() && UInt(Rdn) < 8 && UInt(imm8) < 8) SUB<c>{<q>} {<Rdn>, }<Rdn>, #<imm8> // (Inside IT block, and <Rdn>, <imm8> cannot be represented in T1) SUBS{<q>} <Rdn>, #<imm8> // (Outside IT block, and <Rdn>, <imm8> can be represented in T1) SUBS{<q>} {<Rdn>, }<Rdn>, #<imm8> // (Outside IT block, and <Rdn>, <imm8> cannot be represented in T1)
```

## Decode for this encoding

```
constant integer d = UInt(Rdn); constant integer n = UInt(Rdn); constant boolean setflags = !InITBlock(); constant bits(32) imm32 = ZeroExtend(imm8, 32);
```

T3

<!-- image -->

## Encoding for the SUB variant

<!-- image -->

```
ZeroExtend(imm3, 32);
```

<!-- image -->

## Encoding for the SUBS variant

<!-- image -->

<!-- image -->

## Applies when (S == 1 &amp;&amp; Rd != 1111) SUBS{&lt;c&gt;}{&lt;q&gt;} {&lt;Rd&gt;, }&lt;Rn&gt;, #&lt;const&gt; SUBS.W {&lt;Rd&gt;, }&lt;Rn&gt;, #&lt;const&gt; // (Outside IT block, and &lt;Rd&gt;, &lt;Rn&gt;, &lt;const&gt; can be represented in T1 or ↪ → T2) Decode for all variants of this encoding if Rd == '1111' &amp;&amp; S == '1' then SEE "CMP (immediate)"; if Rn == '1101' then SEE "SUB (SP minus immediate)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 = T32ExpandImm(i:imm3:imm8); // Armv8-A removes UNPREDICTABLE for R13 if (d == 15 &amp;&amp; !setflags) || n == 15 then UNPREDICTABLE; T4 1 1 1 1 0 15 11 i 10 1 0 9 8 1 7 0 6 1 5 0 4 !=11x1 3 0 0 15 imm3 14 12 Rd 11 8 imm8 7 0 o1 o2 Rn Encoding SUB{&lt;c&gt;}{&lt;q&gt;} {&lt;Rd&gt;, }&lt;Rn&gt;, #&lt;imm12&gt; // (&lt;imm12&gt; cannot be represented in T1, T2, or T3) SUBW{&lt;c&gt;}{&lt;q&gt;} {&lt;Rd&gt;, }&lt;Rn&gt;, #&lt;imm12&gt; // (&lt;imm12&gt; can be represented in T1, T2, or T3) Decode for this encoding if Rn == '1111' then SEE "ADR"; if Rn == '1101' then SEE "SUB (SP minus immediate)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = FALSE; constant bits(32) imm32 = ZeroExtend(i:imm3:imm8, 32); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE; T5 1 1 1 15 13 1 0 12 11 0 10 1 1 1 1 9 6 0 1 5 4 Rn 3 0 1 15 0(0)0 14 12 (1) 11 (1)(1)(1) 10 8 imm8 7 0 Encoding Applies when (!(Rn == 1110 &amp;&amp; imm8 == 00000000)) SUBS{&lt;c&gt;}{&lt;q&gt;} PC, LR, #&lt;imm8&gt;

## Decode for this encoding

```
if Rn == '1110' && IsZero(imm8) then SEE "ERET"; constant integer d = 15; constant integer n = UInt(Rn); constant boolean setflags = TRUE; constant bits(32) imm32 = ZeroExtend(imm8, 32); if n != 14 then UNPREDICTABLE; if InITBlock() && !LastInITBlock() then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly SUBS PC. LR and related instructions (A32) and SUBS PC, LR and related instructions (T32).

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 SUB' and 'A1 SUBS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . If the PC is used:

- For the SUB variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the SUBS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;. Arm deprecates use of this instruction unless &lt;Rn&gt; is the LR.

For the 'T1', 'T3 SUB', 'T3 SUBS', and 'T4' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 SUB', 'A1 SUBS', and 'T4' variants: is the general-purpose source register, encoded in the 'Rn' field. If the SP is used, see SUB (SP minus immediate). If the PC is used, see ADR.

For the 'T1' variant: is the general-purpose source register, encoded in the 'Rn' field.

For the 'T3 SUB' and 'T3 SUBS' variants: is the general-purpose source register, encoded in the 'Rn' field. If the SP is used, see SUB (SP minus immediate).

## &lt;const&gt;

For the 'A1 SUB' and 'A1 SUBS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T3 SUB' and 'T3 SUBS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## &lt;imm3&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'imm3' field.

## &lt;Rdn&gt;

Is the general-purpose source and destination register, encoded in the 'Rdn' field.

## &lt;imm8&gt;

For the 'T2' variant: is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

For the 'T5' variant: is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field. If &lt;Rn&gt; is the LR, and zero is used, see ERET.

## &lt;imm12&gt;

Is a 12-bit unsigned immediate, in the range 0 to 4095, encoded in the 'i:imm3:imm8' field.

In the T32 instruction set, MOVS{&lt;c&gt;}{&lt;q&gt;} PC, LR is a pseudo-instruction for SUBS{&lt;c&gt;}{&lt;q&gt;} PC, LR, #0 .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], NOT(imm32), '1'); if d == 15 then if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.