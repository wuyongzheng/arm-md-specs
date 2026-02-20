## C9.2.344 ZERO (single-vector)

Zero ZA single-vector groups

This instruction zeroes two or four ZA single-vector groups.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively.

It has encodings from 2 classes: Two ZA single-vectors and Four ZA single-vectors

## Two ZA single-vectors

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs>, VGx2]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off3); constant integer ngrp = 2;
```

## Four ZA single-vectors

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs>, VGx4]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer offset = UInt(off3); constant integer ngrp = 4;
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV ngrp; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; for r = 0 to ngrp-1 ZAvector[vec, VL] = Zeros(VL); vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.