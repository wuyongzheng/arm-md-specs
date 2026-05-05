## C6.2.97 CMP (shifted register)

Compare (shifted register)

This instruction subtracts an optionally-shifted register value from a register value. It updates the condition flags based on the result, and discards the result.

This is an alias of SUBS (shifted register). This means:

- The encodings in this description are named to match the encodings of SUBS (shifted register).
- The description of SUBS (shifted register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0)
```

```
CMP <Wn>, <Wm>{, <shift> #<amount>} is equivalent to SUBS WZR, <Wn>, <Wm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf ==

```
1) CMP <Xn>, <Xm>{, <shift> #<amount>} is equivalent to SUBS XZR, <Xn>, <Xm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the optional shift type to be applied to the second source operand, defaulting to LSL and encoded in 'shift':

## &lt;amount&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm6' field. For the '64-bit' variant: is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;Xn&gt;

|   shift | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | RESERVED  |

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of SUBS (shifted register) gives the operational pseudocode for this instruction.

## Operational Information

The description of SUBS (shifted register) gives the operational information for this instruction.
