## F5.1.8 ADD, ADDS (SP plus immediate)

Add to SP (immediate) adds an immediate value to the SP value, and writes the result to the destination register.

If the destination register is not the PC, the ADDS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. However, when the destination register is the PC:

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

```
Applies when (S == 0) ADD{<c>}{<q>}
```

```
{<Rd>, }SP, #<const>
```

## Encoding for the ADDS variant

```
Applies when (S == 1) ADDS{<c>}{<q>} {<Rd>, }SP, #<const>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = (S == '1'); constant bits(32) imm32 =
```

T1

## Encoding

```
ADD{<c>}{<q>} <Rd>, SP, #<imm8>
```

```
A32ExpandImm(imm12);
```

<!-- image -->

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = FALSE; constant bits(32) imm32 =
```

T2

## Encoding

```
ADD{<c>}{<q>} {SP, }SP, #<imm7>
```

## Decode for this encoding

```
constant integer d = 13; constant boolean setflags = FALSE; constant bits(32) imm32 =
```

T3

<!-- image -->

## Encoding for the ADD variant

```
Applies when (S == 0) ADD{<c>}{<q>} {<Rd>, }SP, #<const> ADD{<c>}.W {<Rd>, }SP, #<const> // (<Rd>, <const> can be represented in T1 or T2)
```

## Encoding for the ADDS variant

```
Applies when 1111)
```

```
ADDS{<c>}{<q>}
```

```
(S == 1 && Rd != {<Rd>, }SP, #<const>
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "CMN (immediate)"; constant integer d = UInt(Rd); constant boolean setflags = (S == '1'); constant bits(32) imm32 = T32ExpandImm(i:imm3:imm8); if d == 15 && !setflags then UNPREDICTABLE;
```

```
ZeroExtend(imm7:'00', 32);
```

```
ZeroExtend(imm8:'00', 32);
```

<!-- image -->

## T4

<!-- image -->

## Encoding

```
ADD{<c>}{<q>} {<Rd>, }SP, #<imm12> // (<imm12> cannot be represented in T1, T2, or T3) ADDW{<c>}{<q>} {<Rd>, }SP, #<imm12> // (<imm12> can be represented in T1, T2, or T3)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = FALSE; constant bits(32) imm32 = if d == 15 then UNPREDICTABLE;
```

```
ZeroExtend(i:imm3:imm8, 32);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 ADD' and 'A1 ADDS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the SP . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the ADD variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the ADDS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T1' variant: is the general-purpose destination register, encoded in the 'Rd' field.

For the 'T3 ADD', 'T3 ADDS', and 'T4' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the SP.

## &lt;const&gt;

For the 'A1 ADD' and 'A1 ADDS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T3 ADD' and 'T3 ADDS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## &lt;imm8&gt;

Is an unsigned immediate, a multiple of 4, in the range 0 to 1020, encoded in the 'imm8' field as &lt;imm8&gt;/4.

## &lt;q&gt;

## &lt;Rd&gt;

## SP

Is the stack pointer.

## &lt;imm7&gt;

Is the unsigned immediate, a multiple of 4, in the range 0 to 508, encoded in the 'imm7' field as &lt;imm7&gt;/4.

## &lt;imm12&gt;

Is a 12-bit unsigned immediate, in the range 0 to 4095, encoded in the 'i:imm3:imm8' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[13], imm32, '0'); if d == 15 then // Can only occur for if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

```
A32 encoding
```