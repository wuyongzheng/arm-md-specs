## C6.2.484 TST (shifted register)

Test (shifted register)

This instruction performs a bitwise AND operation on a register value and an optionally-shifted register value. It updates the condition flags based on the result, and discards the result.

This is an alias of ANDS (shifted register). This means:

- The encodings in this description are named to match the encodings of ANDS (shifted register).
- The description of ANDS (shifted register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0)
```

```
TST <Wn>, <Wm>{, <shift> #<amount>} is equivalent to ANDS WZR, <Wn>, <Wm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf ==

```
1)
```

```
TST <Xn>, <Xm>{, <shift> #<amount>} is equivalent to ANDS XZR, <Xn>, <Xm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the optional shift to be applied to the final source, defaulting to LSL and encoded in 'shift':

## &lt;amount&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm6' field. For the '64-bit' variant: is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;Xn&gt;

|   shift | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of ANDS (shifted register) gives the operational pseudocode for this instruction.

## Operational Information

The description of ANDS (shifted register) gives the operational information for this instruction.
