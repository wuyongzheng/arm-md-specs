## C6.2.355 SBFX

## Signed bitfield extract

This instruction copies a bitfield of &lt;width&gt; bits starting from bit position &lt;lsb&gt; in the source register to the least significant bits of the destination register, and sets destination bits above the bitfield to a copy of the most significant bit of the bitfield.

This is an alias of SBFM. This means:

- The encodings in this description are named to match the encodings of SBFM.
- The description of SBFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0)

```
SBFX <Wd>, <Wn>, #<lsb>, #<width>
```

```
is equivalent to
```

```
SBFM <Wd>, <Wn>, #<lsb>, #(<lsb>+<width>-1)
```

and is the preferred disassembly when BFXPreferred(sf, opc[1], imms, immr) .

## Encoding for the 64-bit variant

Applies when (sf == 1 &amp;&amp; N == 1)

```
SBFX <Xd>, <Xn>, #<lsb>, #<width>
```

## is equivalent to

```
SBFM <Xd>, <Xn>, #<lsb>, #(<lsb>+<width>-1)
```

and is the preferred disassembly when BFXPreferred(sf, opc[1], imms, immr) .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;lsb&gt;

For the '32-bit' variant: is the bit number of the lsb of the source bitfield, in the range 0 to 31.

For the '64-bit' variant: is the bit number of the lsb of the source bitfield, in the range 0 to 63.

## &lt;width&gt;

For the '32-bit' variant: is the width of the bitfield, in the range 1 to 32-&lt;lsb&gt;.

For the '64-bit' variant: is the width of the bitfield, in the range 1 to 64-&lt;lsb&gt;.

<!-- image -->

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

The description of SBFM gives the operational pseudocode for this instruction.

## Operational Information

The description of SBFM gives the operational information for this instruction.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
