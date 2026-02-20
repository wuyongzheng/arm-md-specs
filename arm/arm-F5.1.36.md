## F5.1.36 CMP (immediate)

Compare (immediate) subtracts an immediate value from a register value. It updates the condition flags based on the result, and discards the result.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
CMP{<c>}{<q>} <Rn>, #<const>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(32) imm32 = A32ExpandImm(imm12);
```

T1

## Encoding

```
CMP{<c>}{<q>} <Rn>, #<imm8>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8, 32);
```

T2

<!-- image -->

## Encoding

```
CMP{<c>}{<q>} <Rn>, #<const> CMP{<c>}.W <Rn>, #<const> // (<Rd>, <const> can be represented in T1)
```

<!-- image -->

## Decode for this encoding

```
constant integer n = UInt(Rn); constant bits(32) imm32 = T32ExpandImm(i:imm3:imm8); if n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' variant: is the general-purpose source register, encoded in the 'Rn' field. The PC can be used, but this is deprecated.

For the 'T1' variant: is a general-purpose source register, encoded in the 'Rn' field.

For the 'T2' variant: is the general-purpose source register, encoded in the 'Rn' field.

## &lt;const&gt;

For the 'A1' variant: an immediate value. See Modified immediate constants in A32 instructions for the range of values.

For the 'T2' variant: an immediate value. See Modified immediate constants in T32 instructions for the range of values.

## &lt;imm8&gt;

Is a 8-bit unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], NOT(imm32), PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

&lt;q&gt;

## &lt;Rn&gt;

```
'1');
```