## C8.2.463 MOV (scalar, predicated)

Move general-purpose register to vector elements (predicated)

This instruction moves the general-purpose scalar source register to each Active element in the destination vector. Inactive elements in the destination vector register remain unmodified.

This is an alias of CPY (scalar). This means:

- The encodings in this description are named to match the encodings of CPY (scalar).
- The description of CPY (scalar) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MOV <Zd>.<T>, <Pg>/M, <R><n|SP>
```

## is equivalent to

```
CPY <Zd>.<T>, <Pg>/M, <R><n|SP>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;T&gt;

## &lt;Pg&gt;

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is a width specifier, encoded in 'size':

## &lt;n|SP&gt;

Is the number [0-30] of the general-purpose source register or the name SP (31), encoded in the 'Rn' field.

## Operation

The description of CPY (scalar) gives the operational pseudocode for this instruction.

## Operational Information

The description of CPY (scalar) gives the operational information for this instruction.

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |