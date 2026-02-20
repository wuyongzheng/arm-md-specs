## C9.2.178 MOVA (array to vector, two registers)

Move two ZA single-vector groups to Z two-vector operand

This instruction operates on two ZA single-vector groups.

The single-vector group within each half of the ZA array is selected by the sum of the vector select register and offset, modulo half the number of ZA array vectors.

The vector group symbol VGx2 indicates that the instruction operates on two ZA single-vector groups.

The preferred disassembly syntax uses a 64-bit element size, but an assembler should accept any element size if it is used consistently for all operands. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

This instruction is used by the alias MOV (array to vector, two registers).

## SME2

(FEAT\_SME2)

<!-- image -->

| 31 30   | 29 28 19 18 17                         | 25 24 23 22 21 16 15 14 13 12 10 9 8 7 5 4 1 0   |
|---------|----------------------------------------|--------------------------------------------------|
| 1 1     | 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 Rv 0 1 0 | 0 0 off3 Zd 0                                    |

## Encoding

```
MOVA { <Zd1>.D-<Zd2>.D }, ZA.D[<Wv>, <offs>{, VGx2}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off3); constant integer d = UInt(Zd:'0'); constant integer nreg = 2;
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## Alias Conditions

```
EndOfDecode(Decode_UNDEF);
```

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) for r = 0 to nreg-1 constant bits(VL) result = ZAvector[vec, Z[d + r, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

```
MOV (array to vector, two registers)
```

```
MOD vstride; VL];
```

## Is preferred when

Unconditionally