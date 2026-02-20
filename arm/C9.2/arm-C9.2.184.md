## C9.2.184 MOVA (vector to array, four registers)

Move Z four-vector operand to four ZA single-vector groups

This instruction operates on four ZA single-vector groups.

The single-vector group within each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo quarter the number of ZA array vectors.

The vector group symbol VGx4 indicates that the instruction operates on four ZA single-vector groups.

The preferred disassembly syntax uses a 64-bit element size, but an assembler should accept any element size if it is used consistently for all operands. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

This instruction is used by the alias MOV (vector to array, four registers).

## SME2

(FEAT\_SME2)

<!-- image -->

| 31 30   | 29 28                              | 25 24 23 22 21 19 18 17 16 15 14 13 12 10 9 7 6 5 4 3 2   |
|---------|------------------------------------|-----------------------------------------------------------|
| 1 1     | 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 Rv 0 | 1 1 Zn 0 0 0 0 off3                                       |

## Encoding

```
MOVA ZA.D[<Wv>, <offs>{, VGx4}], { <Zn1>.D-<Zn4>.D }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off3); constant integer n = UInt(Zn:'00'); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Alias Conditions

```
EndOfDecode(Decode_UNDEF);
```

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) for r = 0 to nreg-1 constant bits(VL) result = Z[n + r, VL]; ZAvector[vec, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

```
MOV (vector to array, four registers)
```

```
MOD vstride;
```

## Is preferred when

Unconditionally