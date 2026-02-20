## C8.2.471 MOV (predicate, merging)

Move predicates (merging)

This instruction reads Active elements from the source predicate and places those elements in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register remain unmodified. This instruction does not set the condition flags.

This is an alias of SEL (predicates). This means:

- The encodings in this description are named to match the encodings of SEL (predicates).
- The description of SEL (predicates) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

## (FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MOV <Pd>.B, <Pg>/M, <Pn>.B
```

## is equivalent to

```
SEL <Pd>.B, <Pg>, <Pn>.B, <Pd>.B
```

and is the preferred disassembly when Pd == Pm .

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of SEL (predicates) gives the operational pseudocode for this instruction.