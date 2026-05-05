## C6.2.269 LSL (immediate)

Logical shift left (immediate)

This instruction shifts a register value left by an immediate number of bits, shifting in zeros, and writes the result to the destination register.

This is an alias of UBFM. This means:

- The encodings in this description are named to match the encodings of UBFM.
- The description of UBFM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0 &amp;&amp; N == 0 &amp;&amp; imms != 011111)

```
LSL <Wd>, <Wn>, #<shift>
```

## is equivalent to

```
UBFM <Wd>, <Wn>, #(-<shift> MOD 32), #(31-<shift>)
```

and is the preferred disassembly when UInt(imms) + 1 == UInt(immr) .

## Encoding for the 64-bit variant

Applies when (sf == 1 &amp;&amp; N == 1 &amp;&amp; imms != 111111)

```
LSL <Xd>, <Xn>, #<shift>
```

## is equivalent to

```
UBFM <Xd>, <Xn>, #(-<shift> MOD 64), #(63-<shift>)
```

and is the preferred disassembly when UInt(imms) + 1 == UInt(immr) .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;shift&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31.

For the '64-bit' variant: is the shift amount, in the range 0 to 63.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

## Operation

The description of UBFM gives the operational pseudocode for this instruction.

## Operational Information

The description of UBFM gives the operational information for this instruction.
