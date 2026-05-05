## C6.2.297 NGCS

Negate with carry, setting flags

This instruction negates the sum of a register value and the value of NOT (Carry flag), and writes the result to the destination register. It updates the condition flags based on the result.

This is an alias of SBCS. This means:

- The encodings in this description are named to match the encodings of SBCS.
- The description of SBCS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

NGCS

&lt;Wd&gt;, &lt;Wm&gt;

## is equivalent to

```
SBCS <Wd>, WZR, <Wm>
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) NGCS <Xd>, <Xm>
```

## is equivalent to

```
SBCS <Xd>, XZR, <Xm>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wm&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rm' field.

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of SBCS gives the operational pseudocode for this instruction.

## Operational Information

The description of SBCS gives the operational information for this instruction.
