## F5.1.32 CLZ

Count Leading Zeros returns the number of binary zero bits before the first binary one bit in a value.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
CLZ{<c>}{<q>} <Rd>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); if d == 15 || m == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
CLZ{<c>}{<q>} <Rd>, <Rm>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer m = UInt(Rm); constant integer n = UInt(Rn); // Armv8-A removes UNPREDICTABLE for R13 if m != n || d == 15 || m == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If m != n , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The instruction executes with the additional decode: m = UInt(Rn);.
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Rm&gt;

For the 'A1' variant: is the general-purpose source register, encoded in the 'Rm' field.

For the 'T1' variant: is the general-purpose source register, encoded in the 'Rm' field. It must be encoded with an identical value in the 'Rn' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer result R[d] = result<31:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
= CountLeadingZeroBits(R[m]);
```