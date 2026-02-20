## C9.2.29 BFMLA (multiple vectors)

Multi-vector BFloat16 fused multiply-add

This instruction multiplies the corresponding BFloat16 elements of the two or four first and second source vectors and destructively adds these values without intermediate rounding to the corresponding elements of the ZA single-vector groups.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction follows SME2 ZA-targeting non-widening BFloat16 numerical behaviors.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.B16B16 indicates whether this instruction is implemented.

It has encodings from 2 classes: Two ZA single-vectors and Four ZA single-vectors

## Two ZA single-vectors

(FEAT\_SME\_B16B16)

<!-- image -->

## Encoding

```
BFMLA ZA.H[<Wv>, <offs>{, VGx2}], { <Zn1>.H-<Zn2>.H }, {
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_B16B16) then constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off3); constant integer nreg = 2;
```

## Four ZA single-vectors

```
(FEAT_SME_B16B16)
```

<!-- image -->

## Encoding

```
BFMLA ZA.H[<Wv>, <offs>{, VGx4}], { <Zn1>.H-<Zn4>.H }, { <Zm1>.H-<Zm4>.H }
```

```
<Zm1>.H-<Zm2>.H }
```

```
EndOfDecode(Decode_UNDEF);
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_B16B16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off3); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

For the 'Two ZA single-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA single-vectors' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two ZA single-vectors' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four ZA single-vectors' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) bits(VL) result; for r = 0 to nreg-1
```

```
MOD vstride;
```

```
constant bits(VL) op1 = Z[n+r, VL]; constant bits(VL) op2 = Z[m+r, VL]; constant bits(VL) op3 = ZAvector[vec, VL]; for e = 0 to elements-1 constant bits(16) elem1 = Elem[op1, e, 16]; constant bits(16) elem2 = Elem[op2, e, 16]; constant bits(16) elem3 = Elem[op3, e, 16]; Elem[result, e, 16] = BFMulAdd_ZA(elem3, elem1, elem2, FPCR); ZAvector[vec, VL] = result; vec = vec + vstride;
```