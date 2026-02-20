## C8.2.491 NOTS

Bitwise invert predicate, setting the condition flags

This instruction performs a bitwise invert on each active element of the source predicate, and places the results in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the Vflag to zero.

This is an alias of EORS. This means:

- The encodings in this description are named to match the encodings of EORS.
- The description of EORS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
NOTS <Pd>.B, <Pg>/Z, <Pn>.B
```

## is equivalent to

```
EORS <Pd>.B, <Pg>/Z, <Pn>.B, <Pg>.B
```

and is the preferred disassembly when Pm == Pg .

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## &lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of EORS gives the operational pseudocode for this instruction.

## Operational Information

The description of EORS gives the operational information for this instruction.