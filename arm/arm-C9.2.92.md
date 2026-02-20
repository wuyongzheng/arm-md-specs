## C9.2.92 FMLAL (multiple and indexed vector, FP8 to FP16)

Multi-vector 8-bit floating-point multiply-add by indexed element to half-precision

This instruction widens all 8-bit floating-point elements in the one, two, or four first source vectors and the indexed element of the second source vector to half-precision format and multiplies the corresponding elements. The intermediate products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) before being destructively added without intermediate rounding to the overlapping 16-bit half-precision elements of the ZA double-vector groups.

The 8-bit floating-point elements within the second source vector are specified using a 4-bit immediate index that selects the same element position within each 128-bit vector segment.

The double-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA double-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

It has encodings from 3 classes: One ZA double-vector, Two ZA double-vectors, and Four ZA double-vectors

```
One ZA double-vector (FEAT_SME_F8F16)
```

<!-- image -->

## Encoding

```
FMLAL ZA.H[<Wv>, <offs1>:<offs2>], <Zn>.B, <Zm>.B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3:'0'); constant integer index = UInt(i4A:i4B:i4C); constant integer nreg = 1;
```

```
Two ZA double-vectors (FEAT_SME_F8F16)
```

<!-- image -->

## Encoding

```
FMLAL ZA.H[<Wv>, <offs1>:<offs2>{, VGx2}], { <Zn1>.B-<Zn2>.B }, <Zm>.B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'0'); constant integer index = UInt(i4h:i4l); constant integer nreg = 2;
```

## Four ZA double-vectors

(FEAT\_SME\_F8F16)

<!-- image -->

## Encoding

```
FMLAL ZA.H[<Wv>, <offs1>:<offs2>{, VGx4}], { <Zn1>.B-<Zn4>.B }, <Zm>.B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'0'); constant integer index = UInt(i4h:i4l); constant integer nreg = 4;
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

For the 'One ZA double-vector' variant: is the element index, in the range 0 to 15, encoded in the 'i4A:i4B:i4C' fields.

For the 'Four ZA double-vectors' and 'Two ZA double-vectors' variants: is the element index, in the range 0 to 15, encoded in the 'i4h:i4l' fields.

## &lt;Zn1&gt;

For the 'Two ZA double-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA double-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckFPMREnabled(); CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant integer eltspersegment = 128 DIV 16; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 2); for r = 0 to nreg-1 constant bits(VL) op1 = Z[n+r, VL]; constant bits(VL) op2 = Z[m, VL]; for i = 0 to 1 constant bits(VL) op3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = 2 * segmentbase + index; constant bits(8) elem1 = Elem[op1, 2 * e + i, 8]; constant bits(8) elem2 = Elem[op2, s, 8]; constant bits(16) elem3 = Elem[op3, e, 16]; Elem[result, e, 16] = FP8MulAddFP(elem3, elem1, elem2, FPCR, FPMR); ZAvector[vec + i, VL] = result; vec = vec + vstride;
```