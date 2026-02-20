## F5.1.19 BFC

Bit Field Clear clears any number of adjacent bits at any position in a register, without affecting the other bits in the register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
BFC{<c>}{<q>} <Rd>, #<lsb>, #<width>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer msbit = UInt(msb); constant integer lsbit = UInt(lsb); if d == 15 then UNPREDICTABLE; if msbit < lsbit then UNPREDICTABLE;
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
BFC{<c>}{<q>} <Rd>, #<lsb>, #<width>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer msbit = UInt(msb); constant integer lsbit = UInt(imm3:imm2); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE; if msbit < lsbit then UNPREDICTABLE;
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

For the 'A1' variant: is the least significant bit to be cleared, in the range 0 to 31, encoded in the 'lsb' field.

For the 'T1' variant: is the least significant bit that is to be cleared, in the range 0 to 31, encoded in the 'imm3:imm2' field.

## &lt;width&gt;

Is the number of bits to be cleared, in the range 1 to 32-&lt;lsb&gt;, encoded in the 'msb' field as &lt;lsb&gt;+&lt;width&gt;-1.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); R[d]<msbit:lsbit> = Replicate('0', (msbit-lsbit)+1); // Other bits of R[d] are unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;lsb&gt;