## C9.2.17 BFDOT (multiple and single vector)

Multi-vector BFloat16 dot product by vector to single-precision

This instruction computes the dot product of a pair of BF16 values held in the corresponding 32-bit elements of the two or four first source vectors and the second source vector. The single-precision dot product results are destructively added to the corresponding single-precision elements of the ZA single-vector groups.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction follows SME2 ZA-targeting BFloat16 numerical behaviors.

This instruction is unpredicated.

It has encodings from 2 classes: Two ZA single-vectors and Four ZA single-vectors

## Two ZA single-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
BFDOT ZA.S[<Wv>, <offs>{, VGx2}], { <Zn1>.H-<Zn2>.H }, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer nreg = 2;
```

## Four ZA single-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
BFDOT ZA.S[<Wv>, <offs>{, VGx4}], { <Zn1>.H-<Zn4>.H }, <Zm>.H
```

```
EndOfDecode(Decode_UNDEF);
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn'.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 1 modulo 32.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 3 modulo 32.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[(n+r) MOD 32, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = ZAvector[vec, VL]; for e = 0 to elements-1 constant bits(16) elt1_a = Elem[operand1, 2 * e + 0, 16]; constant bits(16) elt1_b = Elem[operand1, 2 * e + 1, 16]; constant bits(16) elt2_a = Elem[operand2, 2 * e + 0, 16]; constant bits(16) elt2_b = Elem[operand2, 2 * e + 1, 16]; bits(32) sum = Elem[operand3, e, 32]; sum = BFDotAdd(sum, elt1_a, elt1_b, elt2_a, elt2_b, FPCR); Elem[result, e, 32] = sum; ZAvector[vec, VL] = result; vec = vec + vstride;
```