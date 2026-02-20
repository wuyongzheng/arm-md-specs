## C9.2.101 FMLS (multiple and indexed vector)

Multi-vector floating-point fused multiply-subtract by indexed element

This instruction multiplies the indexed element of the second source vector by the corresponding floating-point elements of the two or four first source vectors and destructively subtracts these values without intermediate rounding from the corresponding elements of the ZA single-vector groups.

The elements within the second source vector are specified using an immediate element index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction follows SME ZA-targeting floating-point behaviors.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.F64F64 indicates whether the double-precision variant is implemented, and ID\_AA64SMFR0\_EL1.F16F16 indicates whether the half-precision variant is implemented.

It has encodings from 6 classes: Two ZA single-vectors of half-precision elements, Two ZA single-vectors of single-precision elements, Two ZA single-vectors of double-precision elements, Four ZA single-vectors of half-precision elements, Four ZA single-vectors of single-precision elements, and Four ZA single-vectors of double-precision elements

Two ZA single-vectors of half-precision elements

(FEAT\_SME\_F16F16)

<!-- image -->

## Encoding

```
FMLS ZA.H[<Wv>, <offs>{, VGx2}], { <Zn1>.H-<Zn2>.H }, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 16; constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i3h:i3l); constant integer nreg = 2;
```

## Two ZA single-vectors of single-precision elements

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FMLS ZA.S[<Wv>, <offs>{, VGx2}], { <Zn1>.S-<Zn2>.S }, <Zm>.S[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32; constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i2); constant integer nreg = 2;
```

Two ZA single-vectors of double-precision elements

(FEAT\_SME2 &amp;&amp; FEAT\_SME\_F64F64)

<!-- image -->

## Encoding

```
FMLS ZA.D[<Wv>, <offs>{, VGx2}], { <Zn1>.D-<Zn2>.D }, <Zm>.D[<index>]
```

## Decode for this encoding

```
if !(IsFeatureImplemented(FEAT_SME2) && IsFeatureImplemented(FEAT_SME_F64F64)) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 64; constant integer n = UInt(Zn:'0'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i1); constant integer nreg = 2;
```

## Four ZA single-vectors of half-precision elements

(FEAT\_SME\_F16F16)

<!-- image -->

## Encoding

```
FMLS ZA.H[<Wv>, <offs>{, VGx4}], { <Zn1>.H-<Zn4>.H }, <Zm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 16; constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i3h:i3l); constant integer nreg = 4;
```

## Four ZA single-vectors of single-precision elements

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FMLS ZA.S[<Wv>, <offs>{, VGx4}], { <Zn1>.S-<Zn4>.S }, <Zm>.S[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32; constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i2); constant integer nreg = 4;
```

## Four ZA single-vectors of double-precision elements

(FEAT\_SME2 &amp;&amp; FEAT\_SME\_F64F64)

<!-- image -->

## Encoding

```
FMLS ZA.D[<Wv>, <offs>{, VGx4}], { <Zn1>.D-<Zn4>.D }, <Zm>.D[<index>]
```

## Decode for this encoding

```
if !(IsFeatureImplemented(FEAT_SME2) && IsFeatureImplemented(FEAT_SME_F64F64)) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 64; constant integer n = UInt(Zn:'00'); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3); constant integer index = UInt(i1); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

For the 'Two ZA single-vectors of double-precision elements', 'Two ZA single-vectors of half-precision elements', and 'Two ZA single-vectors of single-precision elements' variants: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA single-vectors of double-precision elements', 'Four ZA single-vectors of half-precision elements', and 'Four ZA single-vectors of single-precision elements' variants: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;index&gt;

For the 'Four ZA single-vectors of half-precision elements' and 'Two ZA single-vectors of half-precision elements' variants: is the element index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

For the 'Four ZA single-vectors of single-precision elements' and 'Two ZA single-vectors of single-precision elements' variants: is the element index, in the range 0 to 3, encoded in the 'i2' field.

For the 'Four ZA single-vectors of double-precision elements' and 'Two ZA single-vectors of double-precision elements' variants: is the element index, in the range 0 to 1, encoded in the 'i1' field.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant integer eltspersegment = 128 DIV esize; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to nreg-1 constant bits(VL) op1 = Z[n+r, VL]; constant bits(VL) op2 = Z[m, VL]; constant bits(VL) op3 = ZAvector[vec, VL]; for e = 0 to elements-1 constant bits(esize) elem1 = FPNeg(Elem[op1, e, esize], FPCR); constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant bits(esize) elem2 = Elem[op2, s, esize]; constant bits(esize) elem3 = Elem[op3, e, esize]; Elem[result, e, esize] = FPMulAdd_ZA(elem3, elem1, elem2, FPCR); ZAvector[vec, VL] = result; vec = vec + vstride;
```