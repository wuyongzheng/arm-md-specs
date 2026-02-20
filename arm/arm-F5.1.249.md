## F5.1.249 SUB, SUBS (SP minus immediate)

Subtract from SP (immediate) subtracts an immediate value from the SP value, and writes the result to the destination register.

If the destination register is not the PC, the SUBS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. If the destination register is the PC:

- The SUB variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The SUBS variant of the instruction performs an exception return without the use of the stack. Arm deprecates use of this instruction. However, in this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the SUB variant

```
Applies when (S == 0) SUB{<c>}{<q>} {<Rd>, }SP, #<const>
```

## Encoding for the SUBS variant

```
Applies when (S == 1) SUBS{<c>}{<q>} {<Rd>, }SP, #<const>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = (S == '1'); constant bits(32) imm32 = A32ExpandImm(imm12);
```

T1

## Encoding

SUB{&lt;c&gt;}{&lt;q&gt;}

{SP, }SP, #&lt;imm7&gt;

<!-- image -->

## Decode for this encoding

```
constant integer d = 13; constant boolean setflags = FALSE; constant bits(32) imm32 =
```

T2

<!-- image -->

## Encoding for the SUB variant

```
Applies when (S == 0) SUB{<c>}{<q>} {<Rd>, }SP, #<const> SUB{<c>}.W {<Rd>, }SP, #<const> // (<Rd>, <const> can be represented in T1)
```

## Encoding for the SUBS variant

Applies when 1111)

```
SUBS{<c>}{<q>}
```

```
(S == 1 && Rd != {<Rd>, }SP, #<const>
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "CMP (immediate)"; constant integer d = UInt(Rd); constant boolean setflags = (S == '1'); constant bits(32) imm32 = T32ExpandImm(i:imm3:imm8); if d == 15 && !setflags then UNPREDICTABLE;
```

T3

<!-- image -->

## Encoding

```
SUB{<c>}{<q>} {<Rd>, }SP, #<imm12> // (<imm12> cannot be represented in T1, T2, or T3) SUBW{<c>}{<q>} {<Rd>, }SP, #<imm12> // (<imm12> can be represented in T1, T2, or T3)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = FALSE; constant bits(32) imm32 = ZeroExtend(i:imm3:imm8, 32); if d == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
ZeroExtend(imm7:'00', 32);
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 SUB' and 'A1 SUBS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the SP . If the PC is used:

- For the SUB variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the SUBS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;. Arm deprecates use of this instruction unless &lt;Rn&gt; is the LR.

For the 'T2 SUB', 'T2 SUBS', and 'T3' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the SP .

## &lt;const&gt;

For the 'A1 SUB' and 'A1 SUBS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T2 SUB' and 'T2 SUBS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

Is the stack pointer.

## &lt;imm7&gt;

Is the unsigned immediate, a multiple of 4, in the range 0 to 508, encoded in the 'imm7' field as &lt;imm7&gt;/4.

## &lt;imm12&gt;

Is a 12-bit unsigned immediate, in the range 0 to 4095, encoded in the 'i:imm3:imm8' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[13], NOT(imm32), '1'); if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

&lt;q&gt;

## &lt;Rd&gt;

## SP