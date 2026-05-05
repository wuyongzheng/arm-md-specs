## C6.2.500 UXTH

Unsigned extend halfword

This instruction extracts a 16-bit value from a register, zero-extends it to the size of the register, and writes the result to the destination register.

This is an alias of UBFM. This means:

- The encodings in this description are named to match the encodings of UBFM.
- The description of UBFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

```
UXTH <Wd>, <Wn>
```

## is equivalent to

```
UBFM <Wd>, <Wn>, #0, #15
```

and is always the preferred disassembly.

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

The description of UBFM gives the operational pseudocode for this instruction.

## Operational Information

The description of UBFM gives the operational information for this instruction.
