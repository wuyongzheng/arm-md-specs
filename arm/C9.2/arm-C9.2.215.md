## C9.2.215 SMLSL (multiple and single vector)

Multi-vector signed 16-bit integer multiply-subtract by vector from 32-bit integer

This instruction multiplies each signed 16-bit element in the one, two, or four first source vectors with each signed 16-bit element in the second source vector, widens each product to 32 bits, and destructively subtracts these values from the corresponding 32-bit elements of the ZA double-vector groups.

The double-vector group within all of, each half of, or each quarter of the ZA array is selected by the sum of the vector select register and offset range, modulo all, half, or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA double-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction is unpredicated.

It has encodings from 3 classes: One ZA double-vector, Two ZA double-vectors, and Four ZA double-vectors

## One ZA double-vector

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SMLSL ZA.S[<Wv>, <offs1>:<offs2>], <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer esize = 32; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off3:'0'); constant integer nreg = 1;
```

```
EndOfDecode(Decode_UNDEF);
```

## Two ZA double-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SMLSL ZA.S[<Wv>, <offs1>:<offs2>{, VGx2}], { <Zn1>.H-<Zn2>.H }, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'0'); constant integer nreg = 2;
```

```
Four ZA double-vectors (FEAT_SME2)
```

<!-- image -->

## Encoding

```
SMLSL ZA.S[<Wv>, <offs1>:<offs2>{, VGx4}], { <Zn1>.H-<Zn4>.H }, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer esize = 32; constant integer v = UInt('010':Rv); constant integer n = UInt(Zn); constant integer m = UInt('0':Zm); constant integer offset = UInt(off2:'0'); constant integer nreg = 4;
```

```
EndOfDecode(Decode_UNDEF);
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

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn'.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 1 modulo 32.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' plus 3 modulo 32.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; vec = vec - (vec MOD 2); for r = 0 to nreg-1 constant bits(VL) operand1 = Z[(n+r) MOD 32, VL]; constant bits(VL) operand2 = Z[m, VL]; for i = 0 to 1 constant bits(VL) operand3 = ZAvector[vec + i, VL]; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, 2 * e + i, esize DIV 2]); constant integer element2 = SInt(Elem[operand2, 2 * e + i, esize DIV 2]); constant bits(esize) product = (element1 * element2)<esize-1:0>; Elem[result, e, esize] = Elem[operand3, e, esize] product; ZAvector[vec + i, VL] = result; vec = vec + vstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.