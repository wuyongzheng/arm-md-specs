## F5.1.5 ADD, ADDS (immediate)

Add (immediate) adds an immediate value to a register value, and writes the result to the destination register.

If the destination register is not the PC, the ADDS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. If the destination register is the PC:

- The ADD variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The ADDS variant of the instruction performs an exception return without the use of the stack. Arm deprecates use of this instruction. However, in this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, T3, and T4).

A1

<!-- image -->

## Encoding for the ADD variant

Applies when (S == 0 &amp;&amp; Rn != 11x1)

```
ADD{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Encoding for the ADDS variant

```
Applies when (S == 1 && Rn != 1101) ADDS{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Decode for all variants of this encoding

```
immediate)";
```

<!-- image -->

```
if Rn == '1111' && S == '0' then SEE "ADR"; if Rn == '1101' then SEE "ADD (SP plus constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 = A32ExpandImm(imm12);
```

T1

## Encoding

```
ADD<c>{<q>} <Rd>, <Rn>, #<imm3> // (InITBlock()) ADDS{<q>} <Rd>, <Rn>, #<imm3> // (Outside IT block)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = !InITBlock(); constant bits(32) imm32 =
```

T2

## Encoding

```
ADD<c>{<q>} <Rdn>, #<imm8> // (InITBlock() && UInt(imm8) < 8) ADD<c>{<q>} {<Rdn>, }<Rdn>, #<imm8> // (Inside IT block, and <Rdn>, <imm8> cannot be represented in T1) ADDS{<q>} <Rdn>, #<imm8> // (Outside IT block, and <Rdn>, <imm8> can be represented in T1) ADDS{<q>} {<Rdn>, }<Rdn>, #<imm8> // (Outside IT block, and <Rdn>, <imm8> cannot be represented in T1)
```

## Decode for this encoding

```
constant integer d = UInt(Rdn); constant integer n = UInt(Rdn); constant boolean setflags = !InITBlock(); constant bits(32) imm32 = ZeroExtend(imm8, 32);
```

T3

<!-- image -->

## Encoding for the ADD variant

```
Applies when (S == 0) ADD{<c>}{<q>} {<Rd>, }<Rn>, #<const> ADD<c>.W {<Rd>, }<Rn>, #<const> // (Inside IT block, and <Rd>, <Rn>, <const> can be represented in T1 ↪ → or T2)
```

```
ZeroExtend(imm3, 32);
```

<!-- image -->

## Encoding for the ADDS variant

Applies when (S == 1 &amp;&amp; Rd !=

```
1111) ADDS{<c>}{<q>} {<Rd>, }<Rn>, #<const> ADDS.W {<Rd>, }<Rn>, #<const> // (Outside IT block, and <Rd>, <Rn>, <const> can be represented in T1 or ↪ → T2)
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "CMN (immediate)"; if Rn == '1101' then SEE "ADD (SP plus immediate)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant bits(32) imm32 = T32ExpandImm(i:imm3:imm8); // Armv8-A removes UNPREDICTABLE for R13 if (d == 15 && !setflags) || n == 15 then UNPREDICTABLE;
```

T4

<!-- image -->

## Encoding

```
ADD{<c>}{<q>} {<Rd>, }<Rn>, #<imm12> // (<imm12> cannot be represented in T1, T2, or T3) ADDW{<c>}{<q>} {<Rd>, }<Rn>, #<imm12> // (<imm12> can be represented in T1, T2, or T3)
```

## Decode for this encoding

```
if Rn == '1111' then SEE "ADR"; if Rn == '1101' then SEE "ADD (SP plus immediate)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = FALSE; constant bits(32) imm32 = ZeroExtend(i:imm3:imm8, 32); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

&lt;Rd&gt;

For the 'A1 ADD' and 'A1 ADDS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . If the PC is used:

## &lt;Rn&gt;

- For the ADD variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the ADDS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;. Arm deprecates use of this instruction.

For the 'T1', 'T3 ADD', 'T3 ADDS', and 'T4' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 ADD', 'A1 ADDS', and 'T4' variants: is the general-purpose source register, encoded in the 'Rn' field. If the SP is used, see ADD (SP plus immediate). If the PC is used, see ADR.

For the 'T1' variant: is the general-purpose source register, encoded in the 'Rn' field.

For the 'T3 ADD' and 'T3 ADDS' variants: is the general-purpose source register, encoded in the 'Rn' field. If the SP is used, see ADD (SP plus immediate).

## &lt;const&gt;

For the 'A1 ADD' and 'A1 ADDS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T3 ADD' and 'T3 ADDS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## &lt;imm3&gt;

Is a 3-bit unsigned immediate, in the range 0 to 7, encoded in the 'imm3' field.

## &lt;Rdn&gt;

Is the general-purpose source and destination register, encoded in the 'Rdn' field.

## &lt;imm8&gt;

Is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field.

## &lt;imm12&gt;

Is a 12-bit unsigned immediate, in the range 0 to 4095, encoded in the 'i:imm3:imm8' field.

When multiple encodings of the same length are available for an instruction, encoding T3 is preferred to encoding T4 (if encoding T4 is required, use the ADDW syntax). Encoding T1 is preferred to encoding T2 if &lt;Rd&gt; is specified and encoding T2 is preferred to encoding T1 if &lt;Rd&gt; is omitted.

## Operation

```
if CurrentInstrSet() == InstrSet_A32 then if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], imm32, '0'); if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv; else if ConditionPassed() then EncodingSpecificOperations();
```

```
bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], imm32, '0'); R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.