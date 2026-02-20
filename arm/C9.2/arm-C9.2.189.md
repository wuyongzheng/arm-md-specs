## C9.2.189 MOVAZ (array to vector, four registers)

Move and zero four ZA single-vector groups to Z four-vector operand

This instruction operates on four ZA single-vector groups. The ZA single-vector groups are zeroed after moving their contents to the destination vectors.

The single-vector group within each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo quarter the number of ZA array vectors.

The vector group symbol VGx4 indicates that the instruction operates on four ZA single-vector groups.

The preferred disassembly syntax uses a 64-bit element size, but an assembler should accept any element size if it is used consistently for all operands. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

## SME2

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
MOVAZ { <Zd1>.D-<Zd4>.D }, ZA.D[<Wv>, <offs>{, VGx4}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off3); constant integer d = UInt(Zd:'00'); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

```
EndOfDecode(Decode_UNDEF);
```

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) for r = 0 to nreg-1 constant bits(VL) result = ZAvector[vec, ZAvector[vec, VL] = Zeros(VL); Z[d + r, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
MOD vstride; VL];
```