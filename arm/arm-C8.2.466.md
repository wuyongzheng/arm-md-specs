## C8.2.466 MOV (scalar, unpredicated)

Move general-purpose register to vector elements (unpredicated)

This instruction unconditionally broadcasts the general-purpose scalar source register into each element of the destination vector. This instruction is unpredicated.

This is an alias of DUP (scalar). This means:

- The encodings in this description are named to match the encodings of DUP (scalar).
- The description of DUP (scalar) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

MOV

&lt;Zd&gt;.&lt;T&gt;, &lt;R&gt;&lt;n|SP&gt;

is equivalent to

DUP

&lt;Zd&gt;.&lt;T&gt;, &lt;R&gt;&lt;n|SP&gt;

and is always the preferred disassembly.

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

Is a width specifier, encoded in 'size':

<!-- image -->

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;n|SP&gt;

Is the number [0-30] of the general-purpose source register or the name SP (31), encoded in the 'Rn' field.

## Operation

The description of DUP (scalar) gives the operational pseudocode for this instruction.

## Operational Information

The description of DUP (scalar) gives the operational information for this instruction.

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |