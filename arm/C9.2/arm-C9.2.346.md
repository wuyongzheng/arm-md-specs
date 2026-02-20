## C9.2.346 ZERO (quad-vector)

Zero ZA quad-vector groups

This instruction zeroes one, two, or four ZA quad-vector groups.

The quad-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA quad-vector groups respectively.

It has encodings from 3 classes: One ZA quad-vector, Two ZA quad-vectors, and Four ZA quad-vectors

## One ZA quad-vector

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs1>:<offs4>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off2:'00'); constant integer ngrp = 1; constant integer nvec = 4;
```

## Two ZA quad-vectors

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs1>:<offs4>, VGx2]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(o1:'00'); constant integer ngrp = 2; constant integer nvec = 4;
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_UNDEF);
```

## Four ZA quad-vectors

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs1>:<offs4>, VGx4]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(o1:'00'); constant integer ngrp = 4; constant integer nvec = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs1&gt;

For the 'One ZA quad-vector' variant: is the first vector select offset, encoded as 'off2' field times 4.

For the 'Four ZA quad-vectors' and 'Two ZA quad-vectors' variants: is the first vector select offset, encoded as 'o1' field times 4.

## &lt;offs4&gt;

For the 'One ZA quad-vector' variant: is the fourth vector select offset, encoded as 'off2' field times 4 plus 3.

For the 'Four ZA quad-vectors' and 'Two ZA quad-vectors' variants: is the fourth vector select offset, encoded as 'o1' field times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV ngrp; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; vec = vec - (vec MOD nvec); for r = 0 to ngrp-1 for i = 0 to nvec-1 ZAvector[vec + i, VL] = Zeros(VL); vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```