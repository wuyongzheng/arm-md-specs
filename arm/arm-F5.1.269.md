## F5.1.269 UBFX

Unsigned Bit Field Extract extracts any number of adjacent bits at any position from a register, zero-extends them to 32 bits, and writes the result to the destination register.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
UBFX{<c>}{<q>} <Rd>, <Rn>, #<lsb>, #<width>
```

## Decode for this encoding

```
UInt(widthm1); widthminus1;
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer lsbit = UInt(lsb); constant integer widthminus1 = constant integer msbit = lsbit + if d == 15 || n == 15 then UNPREDICTABLE; if msbit > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If msbit &gt; 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

T1

<!-- image -->

## Encoding

```
UBFX{<c>}{<q>} <Rd>, <Rn>, #<lsb>, #<width>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer lsbit = UInt(imm3:imm2); constant integer widthminus1 = UInt(widthm1); constant integer msbit = lsbit + widthminus1; // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 then UNPREDICTABLE; if msbit > 31 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If msbit &gt; 31 , then one of the following behaviors must occur:

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

For the 'A1' variant: is the bit number of the least significant bit in the field, in the range 0 to 31, encoded in the 'lsb' field.

For the 'T1' variant: is the bit number of the least significant bit in the field, in the range 0 to 31, encoded in the 'imm3:imm2' field.

## &lt;width&gt;

Is the width of the field, in the range 1 to 32-&lt;lsb&gt;, encoded in the 'widthm1' field as &lt;width&gt;-1.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); R[d] = ZeroExtend(R[n]<msbit:lsbit>, 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

&lt;q&gt;

## &lt;Rd&gt;

## &lt;Rn&gt;

## &lt;lsb&gt;