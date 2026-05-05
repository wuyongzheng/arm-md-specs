## C6.2.295 NEGS

Negate, setting flags

This instruction negates an optionally-shifted register value, and writes the result to the destination register. It updates the condition flags based on the result.

This is an alias of SUBS (shifted register). This means:

- The encodings in this description are named to match the encodings of SUBS (shifted register).
- The description of SUBS (shifted register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0) NEGS <Wd>, <Wm>{, <shift> #<amount>} is equivalent to SUBS <Wd>, WZR, <Wm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

```
Applies when (sf == 1) NEGS <Xd>, <Xm>{, <shift> #<amount>} is equivalent to SUBS <Xd>, XZR, <Xm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wm&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the optional shift type to be applied to the second source operand, defaulting to LSL and encoded in 'shift':

## &lt;amount&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm6' field. For the '64-bit' variant: is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;Xd&gt;

|   shift | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | RESERVED  |

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of SUBS (shifted register) gives the operational pseudocode for this instruction.

## Operational Information

The description of SUBS (shifted register) gives the operational information for this instruction.
