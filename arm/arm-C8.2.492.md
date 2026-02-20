## C8.2.492 ORN (immediate)

Bitwise inclusive OR with inverted immediate (unpredicated)

This instruction performs a bitwise inclusive OR on an inverted immediate with each 64-bit element of the source vector, and destructively places the results in the corresponding elements of the source vector. The immediate is a 64-bit value consisting of a single run of ones or zeros repeating every 2, 4, 8, 16, 32 or 64 bits. This instruction is unpredicated.

This is a pseudo-instruction of ORR (immediate). This means:

- The encodings in this description are named to match the encodings of ORR (immediate).
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of ORR (immediate) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
ORN <Zdn>.<T>, <Zdn>.<T>, #<const>
```

## is equivalent to

```
ORR <Zdn>.<T>, <Zdn>.<T>, #(-<const> - 1)
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'imm13':

## &lt;const&gt;

Is a 64, 32, 16 or 8-bit bitmask consisting of replicated 2, 4, 8, 16, 32 or 64 bit fields, each field containing a rotated run of non-zero bits, encoded in the 'imm13' field.

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

The description of ORR (immediate) gives the operational pseudocode for this instruction.

## Operational Information

The description of ORR (immediate) gives the operational information for this instruction.