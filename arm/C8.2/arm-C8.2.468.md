## C8.2.468 MOV

Move logical bitmask immediate to vector (unpredicated)

This instruction unconditionally broadcasts the logical bitmask immediate into each element of the destination vector. This instruction is unpredicated. The immediate is a 64-bit value consisting of a single run of ones or zeros repeating every 2, 4, 8, 16, 32 or 64 bits.

This is an alias of DUPM. This means:

- The encodings in this description are named to match the encodings of DUPM.
- The description of DUPM gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

MOV

&lt;Zd&gt;.&lt;T&gt;, #&lt;const&gt;

is equivalent to

DUPM

&lt;Zd&gt;.&lt;T&gt;, #&lt;const&gt;

and is the preferred disassembly when SVEMoveMaskPreferred(imm13) .

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'imm13':

## &lt;const&gt;

Is a 64, 32, 16 or 8-bit bitmask consisting of replicated 2, 4, 8, 16, 32 or 64 bit fields, each field containing a rotated run of non-zero bits, encoded in the 'imm13' field.

<!-- image -->

| imm13         | <T>      |
|---------------|----------|
| 0xxxxxx0xxxxx | S        |
| 0xxxxxx10xxxx | H        |
| 0xxxxxx110xxx | B        |
| 0xxxxxx1110xx | B        |
| 0xxxxxx11110x | B        |
| 0xxxxxx11111x | RESERVED |
| 1xxxxxxxxxxxx | D        |

## Operation

The description of DUPM gives the operational pseudocode for this instruction.