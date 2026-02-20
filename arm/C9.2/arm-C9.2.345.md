## C9.2.345 ZERO (double-vector)

Zero ZA double-vector groups

This instruction zeroes one, two, or four ZA double-vector groups.

The double-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA double-vector groups respectively.

It has encodings from 3 classes: One ZA double-vector, Two ZA double-vectors, and Four ZA double-vectors

## One ZA double-vector

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs1>:<offs2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off3:'0'); constant integer ngrp = 1; constant integer nvec = 2;
```

## Two ZA double-vectors

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs1>:<offs2>, VGx2]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off2:'0'); constant integer ngrp = 2; constant integer nvec = 2;
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_UNDEF);
```

## Four ZA double-vectors

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
ZERO ZA.D[<Wv>, <offs1>:<offs2>, VGx4]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then constant integer v = UInt('010':Rv); constant integer offset = UInt(off2:'0'); constant integer ngrp = 4; constant integer nvec = 2;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs1&gt;

For the 'One ZA double-vector' variant: is the first vector select offset, encoded as 'off3' field times 2.

For the 'Four ZA double-vectors' and 'Two ZA double-vectors' variants: is the first vector select offset, encoded as 'off2' field times 2.

## &lt;offs2&gt;

For the 'One ZA double-vector' variant: is the second vector select offset, encoded as 'off3' field times 2 plus 1.

For the 'Four ZA double-vectors' and 'Two ZA double-vectors' variants: is the second vector select offset, encoded as 'off2' field times 2 plus 1.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV ngrp; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; vec = vec - (vec MOD nvec); for r = 0 to ngrp-1 for i = 0 to nvec-1 ZAvector[vec + i, VL] = Zeros(VL); vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```