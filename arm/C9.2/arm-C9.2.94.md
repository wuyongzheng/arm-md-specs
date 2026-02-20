## C9.2.94 FMLAL (multiple vectors, FP8 to FP16)

Multi-vector 8-bit floating-point multiply-add to half-precision

This instruction widens all 8-bit floating-point elements in the two or four first and second source vectors to half-precision format and multiplies the corresponding elements. The intermediate products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) before being destructively added without intermediate rounding to the overlapping 16-bit half-precision elements of the ZA double-vector groups.

The double-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA double-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

It has encodings from 2 classes: Two ZA double-vectors and Four ZA double-vectors

```
Two ZA double-vectors (FEAT_SME_F8F16)
```

<!-- image -->

## Encoding

```
FMLAL ZA.H[<Wv>, <offs1>:<offs2>{, VGx2}], { <Zn1>.B-<Zn2>.B }, { <Zm1>.B-<Zm2>.B }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off2:'0'); constant integer nreg = 2;
```

## Four ZA double-vectors

(FEAT\_SME\_F8F16)

<!-- image -->

## Encoding

```
FMLAL ZA.H[<Wv>, <offs1>:<offs2>{, VGx4}], { <Zn1>.B-<Zn4>.B }, { <Zm1>.B-<Zm4>.B }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off2:'0'); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs1&gt;

Is the first vector select offset, encoded as 'off2' field times 2.

## &lt;offs2&gt;

Is the second vector select offset, encoded as 'off2' field times 2 plus 1.

## &lt;Zn1&gt;

For the 'Two ZA double-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA double-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two ZA double-vectors' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four ZA double-vectors' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckFPMREnabled(); CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg;
```

```
constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 2); for r = 0 to nreg-1 constant bits(VL) op1 = Z[n+r, VL]; constant bits(VL) op2 = Z[m+r, VL]; for i = 0 to 1 constant bits(VL) op3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant bits(8) elem1 = Elem[op1, 2 * e + i, 8]; constant bits(8) elem2 = Elem[op2, 2 * e + i, 8]; constant bits(16) elem3 = Elem[op3, e, 16]; Elem[result, e, 16] = FP8MulAddFP(elem3, elem1, elem2, FPCR, FPMR); ZAvector[vec + i, VL] = result; vec = vec + vstride;
```