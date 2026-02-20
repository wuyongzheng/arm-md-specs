## C9.2.95 FMLAL (multiple and indexed vector, FP16 to FP32)

Multi-vector half-precision multiply-add by indexed element to single-precision

This instruction widens all 16-bit half-precision elements in the one, two, or four first source vectors and the indexed element of the second source vector to single-precision format, then multiplies the corresponding elements and destructively adds these values without intermediate rounding to the overlapping 32-bit single-precision elements of the ZAdouble-vector groups.

The half-precision elements within the second source vector are specified using a 3-bit immediate index that selects the same element position within each 128-bit vector segment.

The double-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA double-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction follows SME ZA-targeting floating-point behaviors.

This instruction is unpredicated.

It has encodings from 3 classes: One ZA double-vector, Two ZA double-vectors, and Four ZA double-vectors

## One ZA double-vector

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FMLAL ZA.S[<Wv>, <offs1>:<offs2>], <Zn>.H, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3:'0'); constant integer index = UInt(i3h:i3l); constant integer nreg = 1;
```

## Two ZA double-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FMLAL ZA.S[<Wv>, <offs1>:<offs2>{, VGx2}], { <Zn1>.H-<Zn2>.H }, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'0'); constant integer index = UInt(i3h:i3l); constant integer nreg = 2;
```

Four ZA double-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FMLAL ZA.S[<Wv>, <offs1>:<offs2>{, VGx4}], { <Zn1>.H-<Zn4>.H }, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'0'); constant integer index = UInt(i3h:i3l); constant integer nreg = 4;
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

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zn&gt;

## &lt;index&gt;

Is the element index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

## &lt;Zn1&gt;

For the 'Two ZA double-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA double-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant integer eltspersegment = 128 DIV 32; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 2); for r = 0 to nreg-1 constant bits(VL) op1 = Z[n+r, VL]; constant bits(VL) op2 = Z[m, VL]; for i = 0 to 1 constant bits(VL) op3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = 2 * segmentbase + index; constant bits(16) elem1 = Elem[op1, 2 * e + i, 16]; constant bits(16) elem2 = Elem[op2, s, 16]; constant bits(32) elem3 = Elem[op3, e, 32]; Elem[result, e, 32] = FPMulAddH_ZA(elem3, elem1, elem2, FPCR); ZAvector[vec + i, VL] = result; vec = vec + vstride;
```