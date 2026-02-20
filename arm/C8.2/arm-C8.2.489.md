## C8.2.489 NOT (predicate)

Bitwise invert predicate

This instruction performs a bitwise invert on each active element of the source predicate, and places the results in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

This is an alias of EOR (predicates). This means:

- The encodings in this description are named to match the encodings of EOR (predicates).
- The description of EOR (predicates) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Not setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
NOT <Pd>.B, <Pg>/Z, <Pn>.B
```

## is equivalent to

```
EOR <Pd>.B, <Pg>/Z, <Pn>.B, <Pg>.B
```

and is the preferred disassembly when Pm == Pg .

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of EOR (predicates) gives the operational pseudocode for this instruction.