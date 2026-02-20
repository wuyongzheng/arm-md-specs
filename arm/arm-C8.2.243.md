## C8.2.243 FMOV (zero, predicated)

Move floating-point +0.0 to vector elements (predicated)

This instruction moves floating-point constant +0.0 to each Active element in the destination vector. Inactive elements in the destination vector register remain unmodified.

This is a pseudo-instruction of CPY (immediate, merging). This means:

- The encodings in this description are named to match the encodings of CPY (immediate, merging).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of CPY (immediate, merging) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMOV <Zd>.<T>, <Pg>/M, #0.0
```

## is equivalent to

```
CPY <Zd>.<T>, <Pg>/M, #0
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

## &lt;Pg&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## Operation

The description of CPY (immediate, merging) gives the operational pseudocode for this instruction.

## Operational Information

The description of CPY (immediate, merging) gives the operational information for this instruction.