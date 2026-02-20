## C8.2.246 FMOV (immediate, unpredicated)

Move floating-point immediate to vector elements (unpredicated)

This instruction unconditionally broadcasts the floating-point immediate into each element of the destination vector. This instruction is unpredicated.

This is an alias of FDUP. This means:

- The encodings in this description are named to match the encodings of FDUP.
- The description of FDUP gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

FMOV

&lt;Zd&gt;.&lt;T&gt;, #&lt;const&gt;

## is equivalent to

```
FDUP <Zd>.<T>, #<const>
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

## &lt;const&gt;

Is a floating-point immediate value expressible as ±n÷16 × 2^r, where n and r are integers such that 16 ≤ n ≤ 31 and -3 ≤ r ≤ 4, i.e. a normalized binary floating-point encoding with 1 sign bit, 3-bit exponent, and 4-bit fractional part, encoded in the 'imm8' field.

## Operation

The description of FDUP gives the operational pseudocode for this instruction.

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |