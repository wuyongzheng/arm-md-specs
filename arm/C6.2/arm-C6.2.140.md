## C6.2.140 CSETM

Conditional set mask

This instruction sets all bits of the destination register to 1 if the condition is TRUE, and otherwise sets all bits to 0.

This is an alias of CSINV. This means:

- The encodings in this description are named to match the encodings of CSINV.
- The description of CSINV gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

```
CSETM <Wd>, <invcond>
```

## is equivalent to

```
CSINV <Wd>, WZR, WZR, <cond>
```

and is always the preferred disassembly.

## Encoding for the 64-bit variant

Applies when 1)

```
(sf == CSETM <Xd>, <invcond>
```

## is equivalent to

```
CSINV <Xd>, XZR, XZR, <cond>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;invcond&gt;

Is one of the standard conditions, excluding AL and NV , encoded with its least significant bit inverted, and encoded in 'cond':

|   cond | <invcond>   | Description        |
|--------|-------------|--------------------|
|   0000 | NE          | Maps to <cond> EQ. |
|   0001 | EQ          | Maps to <cond> NE. |

<!-- image -->

|   cond | <invcond>   | Description        |
|--------|-------------|--------------------|
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

## Operation

The description of CSINV gives the operational pseudocode for this instruction.

## Operational Information

The description of CSINV gives the operational information for this instruction.
