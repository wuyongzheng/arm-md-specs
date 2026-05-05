## C6.2.87 CINV

## Conditional invert

This instruction returns, in the destination register, the bitwise inversion of the value of the source register if the condition is TRUE, and otherwise returns the value of the source register.

This is an alias of CSINV. This means:

- The encodings in this description are named to match the encodings of CSINV.
- The description of CSINV gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
0) CINV <Wd>, <Wn>, <invcond>
```

## is equivalent to

```
CSINV <Wd>, <Wn>, <Wm>, <cond>
```

and is the preferred disassembly when Rn == Rm .

## Encoding for the 64-bit variant

```
Applies when (sf == 1) CINV <Xd>, <Xn>, <invcond>
```

## is equivalent to

```
CSINV <Xd>, <Xn>, <Xm>, <cond>
```

and is the preferred disassembly when Rn == Rm .

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' and 'Rm' fields.

## &lt;invcond&gt;

Is one of the standard conditions, excluding AL and NV , encoded with its least significant bit inverted, and encoded in 'cond':

## &lt;Xd&gt;

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' and 'Rm' fields.

## Operation

The description of CSINV gives the operational pseudocode for this instruction.

## Operational Information

The description of CSINV gives the operational information for this instruction.

|   cond | <invcond>   | Description        |
|--------|-------------|--------------------|
|   0000 | NE          | Maps to <cond> EQ. |
|   0001 | EQ          | Maps to <cond> NE. |
|   0010 | CC          | Maps to <cond> CS. |
|   0011 | CS          | Maps to <cond> CC. |
|   0100 | PL          | Maps to <cond> MI. |
|   0101 | MI          | Maps to <cond> PL. |
|   0110 | VC          | Maps to <cond> VS. |
|   0111 | VS          | Maps to <cond> VC. |
|   1000 | LS          | Maps to <cond> HI. |
|   1001 | HI          | Maps to <cond> LS. |
|   1010 | LT          | Maps to <cond> GE. |
|   1011 | GE          | Maps to <cond> LT. |
|   1100 | LE          | Maps to <cond> GT. |
|   1101 | GT          | Maps to <cond> LE. |

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.
