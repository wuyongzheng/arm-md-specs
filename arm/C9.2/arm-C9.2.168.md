## C9.2.168 MOV (array to vector, two registers)

Move two ZA single-vector groups to Z two-vector operand

This instruction operates on two ZA single-vector groups.

The single-vector group within each half of the ZA array is selected by the sum of the vector select register and offset, modulo half the number of ZA array vectors.

The vector group symbol VGx2 indicates that the instruction operates on two ZA single-vector groups.

The preferred disassembly syntax uses a 64-bit element size, but an assembler should accept any element size if it is used consistently for all operands. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

This is an alias of MOV A (array to vector, two registers). This means:

- The encodings in this description are named to match the encodings of MOV A (array to vector, two registers).
- The description of MOVA (array to vector, two registers) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SME2

## (FEAT\_SME2)

<!-- image -->

| 31 30 29   | 28 21 19 18 17 16 15         | 25 24 23 22 14 13 12 10 9 8 7 5 4 1 0   |
|------------|------------------------------|-----------------------------------------|
| 1 1 0 0 0  | 0 0 0 0 0 0 0 0 1 1 0 0 off3 | Rv 0 1 0 0 0 Zd 0                       |

## Encoding

```
MOV { <Zd1>.D-<Zd2>.D }, ZA.D[<Wv>, <offs>{, VGx2}]
```

## is equivalent to

```
MOVA { <Zd1>.D-<Zd2>.D }, ZA.D[<Wv>, <offs>{, VGx2}]
```

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## Operation

The description of MOVA (array to vector, two registers) gives the operational pseudocode for this instruction.

## Operational Information

The description of MOVA (array to vector, two registers) gives the operational information for this instruction.