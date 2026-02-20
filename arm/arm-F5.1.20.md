## F5.1.20 BFI

Bit Field Insert copies any number of low order bits from a register into the same number of adjacent bits at any position in the destination register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
BFI{<c>}{<q>} <Rd>, <Rn>, #<lsb>, #<width>
```

## Decode for this encoding

```
if Rn == '1111' then SEE "BFC"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer msbit = UInt(msb); constant integer lsbit = UInt(lsb); if d == 15 then UNPREDICTABLE; if msbit < lsbit then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If msbit &lt; lsbit , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

T1

<!-- image -->

## Encoding

```
BFI{<c>}{<q>} <Rd>, <Rn>, #<lsb>, #<width>
```

## Decode for this encoding

```
if Rn == '1111' then SEE "BFC"; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer msbit = UInt(msb); constant integer lsbit = UInt(imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE; if msbit < lsbit then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If msbit &lt; lsbit , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

Is the general-purpose source register, encoded in the 'Rn' field.

For the 'A1' variant: is the least significant destination bit, in the range 0 to 31, encoded in the 'lsb' field.

For the 'T1' variant: is the least significant destination bit, in the range 0 to 31, encoded in the 'imm3:imm2' field.

## &lt;width&gt;

Is the number of bits to be copied, in the range 1 to 32-&lt;lsb&gt;, encoded in the 'msb' field as &lt;lsb&gt;+&lt;width&gt;-1.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); R[d]<msbit:lsbit> = R[n]<(msbit-lsbit):0>; // Other bits of R[d] are unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

## &lt;lsb&gt;