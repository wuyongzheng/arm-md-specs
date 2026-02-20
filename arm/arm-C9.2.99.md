## C9.2.99 FMLALL (multiple and single vector)

Multi-vector 8-bit floating-point multiply-add by vector to single-precision

This instruction widens all 8-bit floating-point elements in the one, two, or four first source vectors and the second source vector to single-precision format and multiplies the corresponding elements. The intermediate products are scaled by 2 -UInt(FPMR.LSCALE) before being destructively added without intermediate rounding to the overlapping 32-bit single-precision elements of the ZA quad-vector groups.

The quad-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA quad-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

It has encodings from 3 classes: One ZA quad-vector, Two ZA quad-vectors, and Four ZA quad-vectors

```
One ZA quad-vector (FEAT_SME_F8F32)
```

<!-- image -->

## Encoding

```
FMLALL ZA.S[<Wv>, <offs1>:<offs4>], <Zn>.B, <Zm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F32) then constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'00'); constant integer nreg = 1;
```

## Two ZA quad-vectors

```
(FEAT_SME_F8F32)
```

<!-- image -->

## Encoding

```
FMLALL ZA.S[<Wv>, <offs1>:<offs4>{, VGx2}], { <Zn1>.B-<Zn2>.B }, <Zm>.B
```

```
EndOfDecode(Decode_UNDEF);
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F32) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer nreg = 2;
```

## Four ZA quad-vectors

(FEAT\_SME\_F8F32)

<!-- image -->

## Encoding

FMLALL ZA.S[&lt;Wv&gt;, &lt;offs1&gt;:&lt;offs4&gt;{, VGx4}], { &lt;Zn1&gt;.B-&lt;Zn4&gt;.B }, &lt;Zm&gt;.B

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F32) then constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer nreg = 4;
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

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn'.

## &lt;Zn&gt;

```
EndOfDecode(Decode_UNDEF);
```

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 1 modulo 32.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 3 modulo 32.

## Operation

```
CheckFPMREnabled(); CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 4); for r = 0 to nreg-1 constant bits(VL) operand1 = Z[(n+r) MOD 32, VL]; constant bits(VL) operand2 = Z[m, VL]; for i = 0 to 3 constant bits(VL) operand3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant bits(8) element1 = Elem[operand1, 4 * e + i, 8]; constant bits(8) element2 = Elem[operand2, 4 * e + i, 8]; constant bits(32) element3 = Elem[operand3, e, 32]; Elem[result, e, 32] = FP8MulAddFP(element3, element1, element2, FPCR, FPMR); ZAvector[vec + i, VL] = result; vec = vec + vstride;
```