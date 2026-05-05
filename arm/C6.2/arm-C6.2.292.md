## C6.2.292 MUL

## Multiply

This instruction multiplies two register values and writes the result to the destination register.

This is an alias of MADD. This means:

- The encodings in this description are named to match the encodings of MADD.
- The description of MADD gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

```
MUL <Wd>, <Wn>, <Wm>
```

## is equivalent to

```
MADD <Wd>, <Wn>, <Wm>, WZR
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf == 1)

```
MUL <Xd>, <Xn>, <Xm>
```

## is equivalent to

```
MADD <Xd>, <Xn>, <Xm>, XZR
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

Is the 64-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## Operation

The description of MADD gives the operational pseudocode for this instruction.

## Operational Information

The description of MADD gives the operational information for this instruction.
