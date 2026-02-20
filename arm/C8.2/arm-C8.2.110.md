## C8.2.110 CMPLO (vectors)

Compare unsigned lower than vector, setting the condition flags

This instruction compares active unsigned integer elements in the first source vector being lower than the corresponding unsigned elements in the second source vector, and places the boolean results of the comparison in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

This is a pseudo-instruction of CMP&lt;cc&gt; (vectors). This means:

- The encodings in this description are named to match the encodings of CMP&lt;cc&gt; (vectors).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of CMP&lt;cc&gt; (vectors) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Higher

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CMPLO <Pd>.<T>, <Pg>/Z, <Zm>.<T>, <Zn>.<T>
```

## is equivalent to

```
CMPHI <Pd>.<T>, <Pg>/Z, <Zn>.<T>, <Zm>.<T>
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

## &lt;T&gt;

## &lt;Pg&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## Operation

The description of CMP&lt;cc&gt; (vectors) gives the operational pseudocode for this instruction.

## Operational Information

The description of CMP&lt;cc&gt; (vectors) gives the operational information for this instruction.