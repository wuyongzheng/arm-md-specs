## F5.1.111 MLS

Multiply and Subtract multiplies two register values, and subtracts the product from a third register value. The least significant 32 bits of the result are written to the destination register. These 32 bits do not depend on whether the source register values are considered to be signed values or unsigned values.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MLS{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); if d == 15 || n == 15 || m == 15 || a == 15 then
```

T1

<!-- image -->

## Encoding

```
MLS{<c>}{<q>} <Rd>, <Rn>, <Rm>, <Ra>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); if d == 15 || n == 15 || m == 15 || a == 15 then // Armv8-A removes UNPREDICTABLE for R13
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
UNPREDICTABLE;
```

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

- &lt;Rn&gt; Is the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

&lt;Rm&gt;

Is the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

&lt;Ra&gt;

Is the third general-purpose source register holding the minuend, encoded in the 'Ra' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer operand1 = SInt(R[n]); // operand1 = UInt(R[n]) produces the same final results constant integer operand2 = SInt(R[m]); // operand2 = UInt(R[m]) produces the same final results constant integer addend = SInt(R[a]); // addend = UInt(R[a]) produces the same final results constant integer result = addend -operand1 * operand2; R[d] = result<31:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

&lt;q&gt;

&lt;Rd&gt;