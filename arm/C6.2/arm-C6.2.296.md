## C6.2.296 NGC

Negate with carry

This instruction negates the sum of a register value and the value of NOT (Carry flag), and writes the result to the destination register.

This is an alias of SBC. This means:

- The encodings in this description are named to match the encodings of SBC.
- The description of SBC gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

NGC

&lt;Wd&gt;, &lt;Wm&gt;

## is equivalent to

```
SBC <Wd>, WZR, <Wm>
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) NGC <Xd>, <Xm>
```

## is equivalent to

```
SBC <Xd>, XZR, <Xm>
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

The description of SBC gives the operational pseudocode for this instruction.

## Operational Information

The description of SBC gives the operational information for this instruction.
