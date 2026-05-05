## C6.2.485 UBFIZ

Unsigned bitfield insert in zeros

This instruction copies a bitfield of &lt;width&gt; bits from the least significant bits of the source register to bit position &lt;lsb&gt; of the destination register, setting the destination bits above and below the bitfield to zero.

This is an alias of UBFM. This means:

- The encodings in this description are named to match the encodings of UBFM.
- The description of UBFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N ==

```
0) UBFIZ <Wd>, <Wn>, #<lsb>, #<width>
```

## is equivalent to

```
UBFM <Wd>, <Wn>, #(-<lsb> MOD 32), #(<width>-1)
```

and is the preferred disassembly when UInt(imms) &lt; UInt(immr) .

## Encoding for the 64-bit variant

```
Applies when (sf == 1 && N == 1) UBFIZ <Xd>, <Xn>, #<lsb>, #<width>
```

## is equivalent to

```
UBFM <Xd>, <Xn>, #(-<lsb> MOD 64), #(<width>-1)
```

and is the preferred disassembly when UInt(imms) &lt; UInt(immr) .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;lsb&gt;

For the '32-bit' variant: is the bit number of the lsb of the destination bitfield, in the range 0 to 31.

For the '64-bit' variant: is the bit number of the lsb of the destination bitfield, in the range 0 to 63.

## &lt;width&gt;

For the '32-bit' variant: is the width of the bitfield, in the range 1 to 32-&lt;lsb&gt;.

For the '64-bit' variant: is the width of the bitfield, in the range 1 to 64-&lt;lsb&gt;.

<!-- image -->

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

The description of UBFM gives the operational pseudocode for this instruction.

## Operational Information

The description of UBFM gives the operational information for this instruction.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
