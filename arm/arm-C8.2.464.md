## C8.2.464 MOV (SIMD&amp;FP scalar, predicated)

Move SIMD&amp;FP scalar register to vector elements (predicated)

This instruction moves the SIMD &amp; floating-point scalar source register to each Active element in the destination vector. Inactive elements in the destination vector register remain unmodified.

This is an alias of CPY (SIMD&amp;FP scalar). This means:

- The encodings in this description are named to match the encodings of CPY (SIMD&amp;FP scalar).
- The description of CPY (SIMD&amp;FP scalar) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MOV <Zd>.<T>, <Pg>/M, <V><n>
```

## is equivalent to

```
CPY <Zd>.<T>, <Pg>/M, <V><n>
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

&lt;n&gt;

|   size | <V>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the number [0-31] of the source SIMD&amp;FP register, encoded in the 'Vn' field.

## Operation

The description of CPY (SIMD&amp;FP scalar) gives the operational pseudocode for this instruction.

## Operational Information

The description of CPY (SIMD&amp;FP scalar) gives the operational information for this instruction.