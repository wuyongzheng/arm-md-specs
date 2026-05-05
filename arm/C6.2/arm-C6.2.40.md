## C6.2.40 BFXIL

Bitfield extract and insert at low end

This instruction copies a bitfield of &lt;width&gt; bits starting from bit position &lt;lsb&gt; in the source register to the least significant bits of the destination register, leaving the other destination bits unchanged.

This is an alias of BFM. This means:

- The encodings in this description are named to match the encodings of BFM.
- The description of BFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N ==

```
0) BFXIL <Wd>, <Wn>, #<lsb>, #<width>
```

## is equivalent to

```
BFM <Wd>, <Wn>, #<lsb>, #(<lsb>+<width>-1)
```

and is the preferred disassembly when UInt(imms) &gt;= UInt(immr) .

## Encoding for the 64-bit variant

```
Applies when (sf == 1 && N == 1) BFXIL <Xd>, <Xn>, #<lsb>, #<width>
```

## is equivalent to

```
BFM <Xd>, <Xn>, #<lsb>, #(<lsb>+<width>-1)
```

and is the preferred disassembly when UInt(imms) &gt;= UInt(immr) .

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

The description of BFM gives the operational pseudocode for this instruction.

## Operational Information

The description of BFM gives the operational information for this instruction.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
