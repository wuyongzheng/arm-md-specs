## C8.2.245 FMOV (immediate, predicated)

Move floating-point immediate to vector elements (predicated)

This instruction moves a floating-point immediate into each Active element in the destination vector. Inactive elements in the destination vector register remain unmodified.

This is an alias of FCPY. This means:

- The encodings in this description are named to match the encodings of FCPY.
- The description of FCPY gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMOV <Zd>.<T>, <Pg>/M, #<const>
```

## is equivalent to

```
FCPY <Zd>.<T>, <Pg>/M, #<const>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## &lt;const&gt;

Is a floating-point immediate value expressible as ±n÷16 × 2^r, where n and r are integers such that 16 ≤ n ≤ 31 and -3 ≤ r ≤ 4, i.e. a normalized binary floating-point encoding with 1 sign bit, 3-bit exponent, and 4-bit fractional part, encoded in the 'imm8' field.

## Operation

The description of FCPY gives the operational pseudocode for this instruction.

## Operational Information

The description of FCPY gives the operational information for this instruction.