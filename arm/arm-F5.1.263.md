## F5.1.263 TST (immediate)

Test (immediate) performs a bitwise AND operation on a register value and an immediate value. It updates the condition flags based on the result, and discards the result.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
TST{<c>}{<q>} <Rn>, #<const>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant boolean a32 = TRUE; constant bits(12) imm = imm12;
```

T1

<!-- image -->

## Encoding

```
TST{<c>}{<q>} <Rn>, #<const>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant boolean a32 = FALSE; constant bits(12) imm = i:imm3:imm8; // Armv8-A removes UNPREDICTABLE for R13 if n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields.
```

## &lt;Rn&gt;

For the 'A1' variant: is the general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1' variant: is the general-purpose source register, encoded in the 'Rn' field.

## &lt;const&gt;

For the 'A1' variant: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T1' variant: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) imm32; bit carry; (imm32, carry) = if a32 then A32ExpandImm_C(imm, PSTATE.C) else T32ExpandImm_C(imm, PSTATE.C); constant bits(32) result = R[n] AND imm32; PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.