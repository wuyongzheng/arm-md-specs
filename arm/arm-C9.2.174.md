## C9.2.174 MOV (vector to array, four registers)

Move Z four-vector operand to four ZA single-vector groups

This instruction operates on four ZA single-vector groups.

The single-vector group within each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo quarter the number of ZA array vectors.

The vector group symbol VGx4 indicates that the instruction operates on four ZA single-vector groups.

The preferred disassembly syntax uses a 64-bit element size, but an assembler should accept any element size if it is used consistently for all operands. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

This is an alias of MOV A (vector to array, four registers). This means:

- The encodings in this description are named to match the encodings of MOV A (vector to array, four registers).
- The description of MOVA (vector to array, four registers) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SME2

## (FEAT\_SME2)

<!-- image -->

| 31 30   | 29 28                            | 25 24 23 22 21 19 18 17 16 15 14 13 12 10   |      |
|---------|----------------------------------|---------------------------------------------|------|
| 1 1     | 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 Rv | 0 1 1                                       | off3 |

## Encoding

```
MOV ZA.D[<Wv>, <offs>{, VGx4}], { <Zn1>.D-<Zn4>.D } is equivalent to MOVA ZA.D[<Wv>, <offs>{, VGx4}], { <Zn1>.D-<Zn4>.D }
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

The description of MOVA (vector to array, four registers) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (vector to array, four registers) gives the operational information for this instruction.