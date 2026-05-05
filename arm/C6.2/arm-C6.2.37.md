## C6.2.37 BFC

## Bitfield clear

This instruction sets a bitfield of &lt;width&gt; bits at bit position &lt;lsb&gt; of the destination register to zero, leaving the other destination bits unchanged.

This is an alias of BFM. This means:

- The encodings in this description are named to match the encodings of BFM.
- The description of BFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Leaving other bits unchanged

(FEAT\_ASMv8p2)

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0)

```
BFC <Wd>, #<lsb>, #<width>
```

## is equivalent to

```
BFM <Wd>, WZR, #(-<lsb> MOD 32), #(<width>-1)
```

and is the preferred disassembly when UInt(imms) &lt; UInt(immr) .

## Encoding for the 64-bit variant

Applies when (sf == 1 &amp;&amp; N == 1)

```
BFC <Xd>, #<lsb>, #<width>
```

## is equivalent to

```
BFM <Xd>, XZR, #(-<lsb> MOD 64), #(<width>-1)
```

and is the preferred disassembly when UInt(imms) &lt; UInt(immr) .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;lsb&gt;

For the '32-bit' variant: is the bit number of the lsb of the destination bitfield, in the range 0 to 31.

For the '64-bit' variant: is the bit number of the lsb of the destination bitfield, in the range 0 to 63.

## &lt;width&gt;

For the '32-bit' variant: is the width of the bitfield, in the range 1 to 32-&lt;lsb&gt;.

For the '64-bit' variant: is the width of the bitfield, in the range 1 to 64-&lt;lsb&gt;.

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

The description of BFM gives the operational pseudocode for this instruction.

## Operational Information

The description of BFM gives the operational information for this instruction.
