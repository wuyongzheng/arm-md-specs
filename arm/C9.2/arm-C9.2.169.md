## C9.2.169 MOV (array to vector, four registers)

Move four ZA single-vector groups to Z four-vector operand

This instruction operates on four ZA single-vector groups.

The single-vector group within each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo quarter the number of ZA array vectors.

The vector group symbol VGx4 indicates that the instruction operates on four ZA single-vector groups.

The preferred disassembly syntax uses a 64-bit element size, but an assembler should accept any element size if it is used consistently for all operands. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

This is an alias of MOV A (array to vector, four registers). This means:

- The encodings in this description are named to match the encodings of MOV A (array to vector, four registers).
- The description of MOVA (array to vector, four registers) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SME2

(FEAT\_SME2)

<!-- image -->

|   31 | 30 29 28 21 19 18 17                   | 25 24 23 22 16 15 14 13 12 10 9 8 7 5 4 2 1 0   |
|------|----------------------------------------|-------------------------------------------------|
|    1 | 1 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 Rv 0 1 | 1 0 0 off3 Zd 0 0                               |

## Encoding

```
MOV { <Zd1>.D-<Zd4>.D }, ZA.D[<Wv>, <offs>{, VGx4}]
```

## is equivalent to

```
MOVA { <Zd1>.D-<Zd4>.D }, ZA.D[<Wv>, <offs>{, VGx4}]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## Operation

The description of MOVA (array to vector, four registers) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (array to vector, four registers) gives the operational information for this instruction.