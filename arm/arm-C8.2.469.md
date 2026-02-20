## C8.2.469 MOV

Move predicate (unpredicated)

This instruction reads all elements from the source predicate and places those elements in the destination predicate. This instruction is unpredicated. This instruction does not set the condition flags.

For programmer convenience, an assembler must also accept predicate-as-counter register names for the source and destination predicate registers.

This is an alias of ORR (predicates). This means:

- The encodings in this description are named to match the encodings of ORR (predicates).
- The description of ORR (predicates) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Not setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

MOV

&lt;Pd&gt;.B, &lt;Pn&gt;.B

## is equivalent to

```
ORR <Pd>.B, <Pn>/Z, <Pn>.B, <Pn>.B
```

and is the preferred disassembly when S == '0' &amp;&amp; Pn == Pm &amp;&amp; Pm == Pg .

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

&lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of ORR (predicates) gives the operational pseudocode for this instruction.