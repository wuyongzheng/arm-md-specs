## C8.2.475 MOVS (predicated)

Move predicates (zeroing), setting the condition flags

This instruction reads Active elements from the source predicate and places those elements in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

This is an alias of ANDS. This means:

- The encodings in this description are named to match the encodings of ANDS.
- The description of ANDS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MOVS <Pd>.B, <Pg>/Z, <Pn>.B
```

## is equivalent to

```
ANDS <Pd>.B, <Pg>/Z, <Pn>.B, <Pn>.B
```

and is the preferred disassembly when S == '1' &amp;&amp; Pn == Pm .

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## &lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of ANDS gives the operational pseudocode for this instruction.

## Operational Information

The description of ANDS gives the operational information for this instruction.