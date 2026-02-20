## F5.1.128 ORN, ORNS (immediate)

Bitwise OR NOT (immediate) performs a bitwise (inclusive) OR of a register value and the complement of an immediate value, and writes the result to the destination register. It can optionally update the condition flags based on the result.

<!-- image -->

## Encoding for the Flag setting variant

```
Applies when
```

```
ORNS{<c>}{<q>}
```

```
(S == 1) {<Rd>, }<Rn>, #<const>
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0) ORN{<c>}{<q>} {<Rd>, }<Rn>, #<const>
```

## Decode for all variants of this encoding

```
(immediate)";
```

```
if Rn == '1111' then SEE "MVN constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean setflags = (S == '1'); constant boolean a32 = FALSE; constant bits(12) imm = i:imm3:imm8; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field. If omitted, this register is the same as &lt;Rn&gt; .

Is the general-purpose source register, encoded in the 'Rn' field.

## &lt;const&gt;

An immediate value. See Modified immediate constants in T32 instructions for the range of values.

<!-- image -->

## &lt;Rd&gt;

&lt;Rn&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) imm32; bit carry; (imm32, carry) = if a32 then A32ExpandImm_C(imm, PSTATE.C) else T32ExpandImm_C(imm, PSTATE.C); constant bits(32) result = R[n] OR NOT(imm32); R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.