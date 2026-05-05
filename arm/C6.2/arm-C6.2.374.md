## C6.2.374 SMNEGL

Signed multiply-negate long

This instruction multiplies two 32-bit register values, negates the product, and writes the result to the 64-bit destination register.

This is an alias of SMSUBL. This means:

- The encodings in this description are named to match the encodings of SMSUBL.
- The description of SMSUBL gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

```
SMNEGL <Xd>, <Wn>, <Wm>
```

## is equivalent to

```
SMSUBL <Xd>, <Wn>, <Wm>, XZR
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## Operation

The description of SMSUBL gives the operational pseudocode for this instruction.

## Operational Information

The description of SMSUBL gives the operational information for this instruction.
