## F5.1.112 MOV, MOVS (immediate)

Move (immediate) writes an immediate value to the destination register.

If the destination register is not the PC, the MOVS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. Arm deprecates any use of these encodings. However, when the destination register is the PC:

- The MOV variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The MOVS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1, T2, and T3).

A1

<!-- image -->

## Encoding for the MOV variant

```
Applies when (S == 0) MOV{<c>}{<q>}
```

```
<Rd>, #<const>
```

## Encoding for the MOVS variant

```
Applies when (S == 1) MOVS{<c>}{<q>}
```

```
<Rd>, #<const>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = (S == '1'); bits(32) imm32; bit carry; (imm32, carry) = A32ExpandImm_C(imm12,
```

A2

<!-- image -->

## Encoding

```
PSTATE.C);
```

```
MOV{<c>}{<q>} <Rd>, #<imm16> // (<imm16> can not be represented in A1) MOVW{<c>}{<q>} <Rd>, #<imm16> // (<imm16> can be represented in A1)
```

<!-- image -->

<!-- image -->

```
Decode for this encoding constant integer d = UInt(Rd); constant boolean setflags = FALSE; constant bits(32) imm32 = ZeroExtend(imm4:imm12, 32); constant bit carry = bit UNKNOWN; if d == 15 then UNPREDICTABLE; T1 0 0 1 15 13 0 0 12 11 Rd 10 8 imm8 7 0 op Encoding MOV<c>{<q>} <Rd>, #<imm8> // (InITBlock()) MOVS{<q>} <Rd>, #<imm8> // (Outside IT block) Decode for this encoding constant integer d = UInt(Rd); constant boolean setflags = !InITBlock(); constant bits(32) imm32 = ZeroExtend(imm8, 32); constant bit carry = PSTATE.C; T2 1 1 1 0 11 i 10 0 9 0 0 1 0 8 5 S 4 1 1 1 1 3 0 0 15 imm3 14 12 Rd 11 8 imm8 7 0 op1 Rn Encoding for the MOV variant Applies when (S == 0) MOV{<c>}{<q>} <Rd>, #<const> MOV<c>.W <Rd>, #<const> // (Inside IT block, and <Rd>, <const> can be represented in T1) Encoding for the MOVS variant
```

```
Applies when (S == 1) MOVS{<c>}{<q>} <Rd>, #<const> MOVS.W <Rd>, #<const> // (Outside IT block, and <Rd>, <const> can be represented in T1)
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = (S == '1'); bits(32) imm32; bit carry; (imm32, carry) = T32ExpandImm_C(i:imm3:imm8, PSTATE.C); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE;
```

T3

<!-- image -->

## Encoding

```
MOV{<c>}{<q>} <Rd>, #<imm16> // (<imm16> cannot be represented in T1 or T2) MOVW{<c>}{<q>} <Rd>, #<imm16> // (<imm16> can be represented in T1 or T2)
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean setflags = FALSE; constant bits(32) imm32 = constant bit carry = bit UNKNOWN; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE;
```

```
ZeroExtend(imm4:i:imm3:imm8, 32);
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 MOV' and 'A1 MOVS' variants: is the general-purpose destination register, encoded in the 'Rd' field. Arm deprecates using the PC as the destination register, but if the PC is used:

- For the MOV variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the MOVS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'A2', 'T1', 'T2 MOV', 'T2 MOVS', and 'T3' variants: is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;const&gt;

For the 'A1 MOV' and 'A1 MOVS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T2 MOV' and 'T2 MOVS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## &lt;imm16&gt;

For the 'A2' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm4:imm12' field.

For the 'T3' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm4:i:imm3:imm8' field.

## &lt;imm8&gt;

Is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) result = imm32; if d == 15 then // Can only occur for encoding A1 if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.