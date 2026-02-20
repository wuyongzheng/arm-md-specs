## C8.2.476 MOVS (unpredicated)

Move predicate (unpredicated), setting the condition flags

This instruction reads all elements from the source predicate and places those elements in the destination predicate. This instruction is unpredicated. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

This is an alias of ORRS. This means:

- The encodings in this description are named to match the encodings of ORRS.
- The description of ORRS gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

MOVS &lt;Pd&gt;.B, &lt;Pn&gt;.B

## is equivalent to

ORRS &lt;Pd&gt;.B, &lt;Pn&gt;/Z, &lt;Pn&gt;.B, &lt;Pn&gt;.B

and is the preferred disassembly when S == '1' &amp;&amp; Pn == Pm &amp;&amp; Pm == Pg .

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

&lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

The description of ORRS gives the operational pseudocode for this instruction.

## Operational Information

The description of ORRS gives the operational information for this instruction.