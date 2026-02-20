## C8.2.244 FMOV (zero, unpredicated)

Move floating-point +0.0 to vector elements (unpredicated)

This instruction unconditionally broadcasts the floating-point constant +0.0 into each element of the destination vector. This instruction is unpredicated.

This is a pseudo-instruction of DUP (immediate). This means:

- The encodings in this description are named to match the encodings of DUP (immediate).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of DUP (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

FMOV

&lt;Zd&gt;.&lt;T&gt;, #0.0

## is equivalent to

DUP

&lt;Zd&gt;.&lt;T&gt;, #0

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

## Operation

The description of DUP (immediate) gives the operational pseudocode for this instruction.

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |