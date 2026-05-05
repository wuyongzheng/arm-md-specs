## C6.2.272 LSR (immediate)

Logical shift right (immediate)

This instruction shifts a register value right by an immediate number of bits, shifting in zeros, and writes the result to the destination register.

This is an alias of UBFM. This means:

- The encodings in this description are named to match the encodings of UBFM.
- The description of UBFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0 &amp;&amp; imms == 011111)

```
LSR <Wd>, <Wn>, #<shift>
```

## is equivalent to

```
UBFM <Wd>, <Wn>, #<shift>, #31
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

```
Applies when (sf == 1 && N == 1 && imms == 111111) LSR <Xd>, <Xn>, #<shift>
```

## is equivalent to

```
UBFM <Xd>, <Xn>, #<shift>, #63
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;shift&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, encoded in the 'immr' field.

For the '64-bit' variant: is the shift amount, in the range 0 to 63, encoded in the 'immr' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

## Operation

The description of UBFM gives the operational pseudocode for this instruction.

## Operational Information

The description of UBFM gives the operational information for this instruction.
