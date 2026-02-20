## C9.2.133 FVDOT (FP16 to FP32)

Multi-vector half-precision vertical dot product by indexed element to single-precision

This instruction computes the fused sum-of-products of each vertical pair of half-precision values in the corresponding elements of the two first source vectors with the pair of half-precision values in the indexed 32-bit group of the corresponding 128-bit segment of the second source vector, without intermediate rounding. The single-precision sum-of-products are destructively added to the corresponding single-precision elements of the two ZA single-vector groups.

The half-precision pairs within the second source vector are specified using an immediate index that selects the same pair position within each 128-bit vector segment. The element index range is from 0 to 3.

The single-vector group within each half of the ZA array is selected by the sum of the vector select register and offset, modulo half the number of ZA array vectors.

The vector group symbol VGx2 indicates that the ZA operand consists of two ZA single-vector groups. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction follows SME ZA-targeting floating-point behaviors.

This instruction is unpredicated.

```
SME2
```

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FVDOT ZA.S[<Wv>, <offs>{, VGx2}], { <Zn1>.H-<Zn2>.H }, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i2);
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

```
EndOfDecode(Decode_UNDEF);
```

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;index&gt;

Is the immediate index of a pair of 16-bit elements within each 128-bit vector segment, in the range 0 to 3, encoded in the 'i2' field.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV 2; constant integer eltspersegment = 128 DIV 32; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to 1 constant bits(VL) operand1a = Z[n, VL]; constant bits(VL) operand1b = Z[n+1, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = ZAvector[vec, VL]; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant bits(16) elt1_a = Elem[operand1a, 2 * e + r, 16]; constant bits(16) elt1_b = Elem[operand1b, 2 * e + r, 16]; constant bits(16) elt2_a = Elem[operand2, 2 * s + 0, 16]; constant bits(16) elt2_b = Elem[operand2, 2 * s + 1, 16]; bits(32) sum = Elem[operand3, e, 32]; sum = FPDotAdd_ZA(sum, elt1_a, elt1_b, elt2_a, elt2_b, FPCR); Elem[result, e, 32] = sum; ZAvector[vec, VL] = result; vec = vec + vstride;
```