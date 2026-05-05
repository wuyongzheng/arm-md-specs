## C6.2.483 TST (immediate)

Test bits (immediate)

This instruction performs a bitwise AND of a register value and an immediate value, and discards the results. It updates the condition flags based on the result.

This is an alias of ANDS (immediate). This means:

- The encodings in this description are named to match the encodings of ANDS (immediate).
- The description of ANDS (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

<!-- image -->

and is always the preferred disassembly.

## Encoding for the 64-bit variant

```
Applies when (sf == 1) TST <Xn>, #<imm> is equivalent to ANDS XZR, <Xn>, #<imm>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;imm&gt;

For the '32-bit' variant: is the bitmask immediate, encoded in 'imms:immr'.

For the '64-bit' variant: is the bitmask immediate, encoded in 'N:imms:immr'.

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

The description of ANDS (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of ANDS (immediate) gives the operational information for this instruction.
