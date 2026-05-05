## C6.2.346 ROR (immediate)

Rotate right (immediate)

This instruction provides the value of the contents of a register rotated by a variable number of bits. The bits that are rotated off the right end are inserted into the vacated bit positions on the left.

This is an alias of EXTR. This means:

- The encodings in this description are named to match the encodings of EXTR.
- The description of EXTR gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0 &amp;&amp; imms == 0xxxxx)

```
ROR <Wd>, <Ws>, #<shift>
```

## is equivalent to

```
EXTR <Wd>, <Ws>, <Ws>, #<shift>
```

and is the preferred disassembly when Rn == Rm .

## Encoding for the 64-bit variant

Applies when (sf == 1 &amp;&amp; N == 1) ROR &lt;Xd&gt;, &lt;Xs&gt;, #&lt;shift&gt;

## is equivalent to

```
EXTR <Xd>, <Xs>, <Xs>, #<shift>
```

and is the preferred disassembly when Rn == Rm .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Ws&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' and 'Rm' fields.

## &lt;shift&gt;

For the '32-bit' variant: is the amount by which to rotate, in the range 0 to 31, encoded in the 'imms' field.

For the '64-bit' variant: is the amount by which to rotate, in the range 0 to 63, encoded in the 'imms' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' and 'Rm' fields.

## &lt;Xd&gt;

<!-- image -->

## Operation

The description of EXTR gives the operational pseudocode for this instruction.

## Operational Information

The description of EXTR gives the operational information for this instruction.
