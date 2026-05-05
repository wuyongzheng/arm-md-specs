## C7.2.250 MVN

Bitwise NOT (vector)

This instruction reads each vector element from the source SIMD&amp;FP register, places the inverse of each value into a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of NOT. This means:

- The encodings in this description are named to match the encodings of NOT.
- The description of NOT gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

MVN

&lt;Vd&gt;.&lt;T&gt;, &lt;Vn&gt;.&lt;T&gt;

## is equivalent to

<!-- image -->

and is always the preferred disassembly.

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;T&gt;

## &lt;Vn&gt;

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

The description of NOT gives the operational pseudocode for this instruction.

## Operational Information

The description of NOT gives the operational information for this instruction.
