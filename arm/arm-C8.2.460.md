## C8.2.460 MOV (predicate, zeroing)

Move predicates (zeroing)

This instruction reads Active elements from the source predicate and places those elements in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

This is an alias of AND (predicates). This means:

- The encodings in this description are named to match the encodings of AND (predicates).
- The description of AND (predicates) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Not setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

MOV &lt;Pd&gt;.B, &lt;Pg&gt;/Z, &lt;Pn&gt;.B

## is equivalent to

```
AND <Pd>.B, <Pg>/Z, <Pn>.B, <Pn>.B
```

and is the preferred disassembly when S == '0' &amp;&amp; Pn == Pm .

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of AND (predicates) gives the operational pseudocode for this instruction.