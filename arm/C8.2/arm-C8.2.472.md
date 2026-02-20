## C8.2.472 MOV (vector, predicated)

Move vector elements (predicated)

This instruction moves elements from the source vector to the corresponding elements of the destination vector. Inactive elements in the destination vector register remain unmodified.

This is an alias of SEL (vectors). This means:

- The encodings in this description are named to match the encodings of SEL (vectors).
- The description of SEL (vectors) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MOV <Zd>.<T>, <Pv>/M, <Zn>.<T>
```

## is equivalent to

```
SEL <Zd>.<T>, <Pv>, <Zn>.<T>, <Zd>.<T>
```

and is the preferred disassembly when Zd == Zm .

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the vector select predicate register, encoded in the 'Pv' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

The description of SEL (vectors) gives the operational pseudocode for this instruction.

## Operational Information

The description of SEL (vectors) gives the operational information for this instruction.