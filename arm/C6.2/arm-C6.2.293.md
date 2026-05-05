## C6.2.293 MVN

Bitwise NOT

This instruction writes the bitwise inverse of a register value to the destination register.

This is an alias of ORN (shifted register). This means:

- The encodings in this description are named to match the encodings of ORN (shifted register).
- The description of ORN (shifted register) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0)
```

```
MVN <Wd>, <Wm>{, <shift> #<amount>} is equivalent to ORN <Wd>, WZR, <Wm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when (sf ==

```
MVN <Xd>, <Xm>{, <shift>
```

```
1) #<amount>}
```

## is equivalent to

```
ORN <Xd>, XZR, <Xm>{, <shift> #<amount>}
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wm&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the optional shift to be applied to the final source, defaulting to LSL and encoded in 'shift':

|   shift | <shift>   |
|---------|-----------|
|      00 | LSL       |

## &lt;amount&gt;

For the '32-bit' variant: is the shift amount, in the range 0 to 31, defaulting to 0 and encoded in the 'imm6' field. For the '64-bit' variant: is the shift amount, in the range 0 to 63, defaulting to 0 and encoded in the 'imm6' field.

## &lt;Xd&gt;

|   shift | <shift>   |
|---------|-----------|
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rm' field.

## Operation

The description of ORN (shifted register) gives the operational pseudocode for this instruction.

## Operational Information

The description of ORN (shifted register) gives the operational information for this instruction.
