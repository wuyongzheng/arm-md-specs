## F5.1.33 CMN (immediate)

Compare Negative (immediate) adds a register value and an immediate value. It updates the condition flags based on the result, and discards the result.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
CMN{<c>}{<q>} <Rn>, #<const>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(32) imm32 = A32ExpandImm(imm12);
```

T1

<!-- image -->

## Encoding

```
CMN{<c>}{<q>} <Rn>, #<const>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(32) imm32 = T32ExpandImm(i:imm3:imm8); if n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Rn&gt;

For the 'A1' variant: is the general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1' variant: is the general-purpose source register, encoded in the 'Rn' field.

## &lt;const&gt;

For the 'A1' variant: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T1' variant: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], imm32, PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
'0');
```