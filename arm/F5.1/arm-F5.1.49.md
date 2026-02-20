## F5.1.49 EOR, EORS (immediate)

Bitwise Exclusive-OR (immediate) performs a bitwise exclusive-OR of a register value and an immediate value, and writes the result to the destination register.

If the destination register is not the PC, the EORS variant of the instruction updates the condition flags based on the result.

The field descriptions for &lt;Rd&gt; identify the encodings where the PC is permitted as the destination register. Arm deprecates any use of these encodings. However, when the destination register is the PC:

- The EOR variant of the instruction is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- The EORS variant of the instruction performs an exception return without the use of the stack. In this case:
- The PE branches to the address written to the PC, and restores PSTATE from SPSR\_&lt;current\_mode&gt;.
- The PE checks SPSR\_&lt;current\_mode&gt; for an illegal return event. See Illegal return events from AArch32 state.
- The instruction is UNDEFINED in Hyp mode.
- The instruction is CONSTRAINED UNPREDICTABLE in User mode and System mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the EOR variant

```
Applies when (S == 0) EOR{<c>}{<q>}
```

```
{<Rd>, }<Rn>, #<const>
```

## Encoding for the EORS variant

```
Applies when (S == 1) EORS{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == constant boolean a32 = TRUE; constant bits(12) imm = imm12;
```

T1

<!-- image -->

```
'1');
```

## Encoding for the EOR variant

Applies when

```
{<Rd>, }<Rn>, #<const>
```

```
(S == 0) EOR{<c>}{<q>}
```

## Encoding for the EORS variant

```
Applies when (S == 1 && Rd != 1111) EORS{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Decode for all variants of this encoding

```
if Rd == '1111' && S == '1' then SEE "TEQ (immediate)"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant boolean a32 = FALSE; constant bits(12) imm = i:imm3:imm8; // Armv8-A removes UNPREDICTABLE for R13 if (d == 15 && !setflags) || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 EOR' and 'A1 EORS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; . Arm deprecates using the PC as the destination register, but if the PC is used:

- For the EOR variant, the instruction is a branch to the address calculated by the operation. This is an interworking branch, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.
- For the EORS variant, the instruction performs an exception return, that restores PSTATE from SPSR\_&lt;current\_mode&gt;.

For the 'T1 EOR' and 'T1 EORS' variants: is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

For the 'A1 EOR' and 'A1 EORS' variants: is the general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1 EOR' and 'T1 EORS' variants: is the general-purpose source register, encoded in the 'Rn' field.

## &lt;const&gt;

For the 'A1 EOR' and 'A1 EORS' variants: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T1 EOR' and 'T1 EORS' variants: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

<!-- image -->

## &lt;Rd&gt;

## &lt;Rn&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) imm32; bit carry; (imm32, carry) = if a32 then A32ExpandImm_C(imm, PSTATE.C) else T32ExpandImm_C(imm, PSTATE.C); constant bits(32) result = R[n] EOR imm32; if d == 15 then // Can only occur for A32 encoding if setflags then ALUExceptionReturn(result); else ALUWritePC(result); else R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.