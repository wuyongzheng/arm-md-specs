## F5.1.115 MOVT

Move Top writes an immediate value to the top halfword of the destination register. It does not affect the contents of the bottom halfword.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MOVT{<c>}{<q>} <Rd>, #<imm16>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(16) imm16 = imm4:imm12; if d == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
MOVT{<c>}{<q>} <Rd>, #<imm16>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant bits(16) imm16 = imm4:i:imm3:imm8; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;imm16&gt;

For the 'A1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm4:imm12' field.

For the 'T1' variant: is a 16-bit unsigned immediate, in the range 0 to 65535, encoded in the 'imm4:i:imm3:imm8' field.

## Operation

```
EncodingSpecificOperations();
```

```
if ConditionPassed() then R[d]<31:16> = imm16; // R[d]<15:0> unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.