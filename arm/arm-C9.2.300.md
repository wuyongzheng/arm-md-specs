## C9.2.300 UMLALL (multiple and indexed vector)

Multi-vector unsigned integer multiply-add long long by indexed element

This instruction multiplies each unsigned 8-bit or 16-bit element in the one, two, or four first source vectors with each unsigned 8-bit or 16-bit indexed element of the second source vector, widens each product to 32 bits or 64 bits, and destructively adds these values to the corresponding 32-bit or 64-bit elements of the ZA quad-vector groups.

The elements within the second source vector are specified using an immediate element index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

The quad-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA quad-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.I16I64 indicates whether the 16-bit integer variant is implemented.

It has encodings from 6 classes: One ZA quad-vector of 32-bit elements, One ZA quad-vector of 64-bit elements, Two ZAquad-vectors of 32-bit elements, Two ZA quad-vectors of 64-bit elements, Four ZA quad-vectors of 32-bit elements, and Four ZA quad-vectors of 64-bit elements

```
One ZA quad-vector of 32-bit elements (FEAT_SME2)
```

<!-- image -->

## Encoding

```
UMLALL ZA.S[<Wv>, <offs1>:<offs4>], <Zn>.B, <Zm>.B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'00'); constant integer index = UInt(i4h:i4l); constant integer nreg = 1;
```

## One ZA quad-vector of 64-bit elements

(FEAT\_SME2 &amp;&amp; FEAT\_SME\_I16I64)

<!-- image -->

## Encoding

```
UMLALL ZA.D[<Wv>, <offs1>:<offs4>], <Zn>.H, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !(IsFeatureImplemented(FEAT_SME2) && IsFeatureImplemented(FEAT_SME_I16I64)) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'00'); constant integer index = UInt(i3h:i3l); constant integer nreg = 1;
```

## Two ZA quad-vectors of 32-bit elements (FEAT\_SME2)

<!-- image -->

## Encoding

```
UMLALL ZA.S[<Wv>, <offs1>:<offs4>{, VGx2}], { <Zn1>.B-<Zn2>.B }, <Zm>.B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer index = UInt(i4h:i4l); constant integer nreg = 2;
```

Two ZA quad-vectors of 64-bit elements

(FEAT\_SME2 &amp;&amp; FEAT\_SME\_I16I64)

<!-- image -->

## Encoding

```
UMLALL ZA.D[<Wv>, <offs1>:<offs4>{, VGx2}], { <Zn1>.H-<Zn2>.H }, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !(IsFeatureImplemented(FEAT_SME2) && IsFeatureImplemented(FEAT_SME_I16I64)) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer index = UInt(i3h:i3l); constant integer nreg = 2;
```

## Four ZA quad-vectors of 32-bit elements

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UMLALL ZA.S[<Wv>, <offs1>:<offs4>{, VGx4}], { <Zn1>.B-<Zn4>.B },
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer index = UInt(i4h:i4l); constant integer nreg = 4;
```

## Four ZA quad-vectors of 64-bit elements

(FEAT\_SME2 &amp;&amp; FEAT\_SME\_I16I64)

<!-- image -->

## Encoding

```
UMLALL ZA.D[<Wv>, <offs1>:<offs4>{, VGx4}], { <Zn1>.H-<Zn4>.H }, <Zm>.H[<index>]
```

```
<Zm>.B[<index>]
```

## Decode for this encoding

```
if !(IsFeatureImplemented(FEAT_SME2) && IsFeatureImplemented(FEAT_SME_I16I64)) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(o1:'00'); constant integer index = UInt(i3h:i3l); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs1&gt;

For the 'One ZA quad-vector of 32-bit elements' and 'One ZA quad-vector of 64-bit elements' variants: is the first vector select offset, encoded as 'off2' field times 4.

For the 'Four ZA quad-vectors of 32-bit elements', 'Four ZA quad-vectors of 64-bit elements', 'Two ZA quad-vectors of 32-bit elements', and 'Two ZA quad-vectors of 64-bit elements' variants: is the first vector select offset, encoded as 'o1' field times 4.

## &lt;offs4&gt;

For the 'One ZA quad-vector of 32-bit elements' and 'One ZA quad-vector of 64-bit elements' variants: is the fourth vector select offset, encoded as 'off2' field times 4 plus 3.

For the 'Four ZA quad-vectors of 32-bit elements', 'Four ZA quad-vectors of 64-bit elements', 'Two ZA quad-vectors of 32-bit elements', and 'Two ZA quad-vectors of 64-bit elements' variants: is the fourth vector select offset, encoded as 'o1' field times 4 plus 3.

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;index&gt;

For the 'Four ZA quad-vectors of 32-bit elements', 'One ZA quad-vector of 32-bit elements', and 'Two ZA quad-vectors of 32-bit elements' variants: is the element index, in the range 0 to 15, encoded in the 'i4h:i4l' fields.

For the 'Four ZA quad-vectors of 64-bit elements', 'One ZA quad-vector of 64-bit elements', and 'Two ZA quad-vectors of 64-bit elements' variants: is the element index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

## &lt;Zn1&gt;

For the 'Two ZA quad-vectors of 32-bit elements' and 'Two ZA quad-vectors of 64-bit elements' variants: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA quad-vectors of 32-bit elements' and 'Four ZA quad-vectors of 64-bit elements' variants: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zn&gt;

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant integer eltspersegment = 128 DIV esize; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 4); for r = 0 to nreg-1 constant bits(VL) operand1 = Z[n+r, VL]; constant bits(VL) operand2 = Z[m, VL]; for i = 0 to 3 constant bits(VL) operand3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = 4 * segmentbase + index; constant integer element1 = UInt(Elem[operand1, 4 * e + i, esize DIV 4]); constant integer element2 = UInt(Elem[operand2, s, esize DIV 4]); constant bits(esize) product = (element1 * element2)<esize-1:0>; Elem[result, e, esize] = Elem[operand3, e, esize] + product; ZAvector[vec + i, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.