## C9.2.59 FADD

Multi-vector floating-point accumulate to ZA array vectors

This instruction destructively adds all elements of the two or four source vectors to the corresponding elements of the ZA single-vector groups.

The single-vector group within each half of or each quarter of the ZA array is selected by the sum of the vector select register and offset, modulo half or quarter the number of ZA array vectors.

The vector group symbol, VGx2 or VGx4 , indicates that the ZA operand consists of two or four ZA single-vector groups respectively. The vector group symbol is preferred for disassembly, but optional in assembler source code.

This instruction follows SME ZA-targeting floating-point behaviors.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.F64F64 indicates whether the double-precision variant is implemented, and ID\_AA64SMFR0\_EL1.F16F16 indicates whether the half-precision variant is implemented.

It has encodings from 4 classes: Two ZA single-vectors, Two ZA single-vectors of half-precision elements, Four ZA single-vectors, and Four ZA single-vectors of half-precision elements

## Two ZA single-vectors

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FADD ZA.<T>[<Wv>, <offs>{, VGx2}], { <Zm1>.<T>-<Zm2>.<T> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_F64F64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off3); constant integer nreg = 2;
```

Two ZA single-vectors of half-precision elements

(FEAT\_SME\_F16F16 || FEAT\_SME\_F8F16)

<!-- image -->

## Encoding

```
FADD ZA.H[<Wv>, <offs>{, VGx2}], { <Zm1>.H-<Zm2>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) && !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 16; constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off3); constant integer nreg = 2;
```

```
Four ZA single-vectors (FEAT_SME2)
```

<!-- image -->

## Encoding

```
FADD ZA.<T>[<Wv>, <offs>{, VGx4}], { <Zm1>.<T>-<Zm4>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_F64F64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off3); constant integer nreg = 4;
```

Four ZA single-vectors of half-precision elements

(FEAT\_SME\_F16F16 || FEAT\_SME\_F8F16)

<!-- image -->

## Encoding

```
FADD ZA.H[<Wv>, <offs>{, VGx4}], { <Zm1>.H-<Zm4>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) && !IsFeatureImplemented(FEAT_SME_F8F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 16; constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off3); constant integer nreg = 4;
```

```
}
```

## Assembler Symbols

## &lt;T&gt;

Is the size specifier, encoded in 'sz':

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zm1&gt;

For the 'Two ZA single-vectors' and 'Two ZA single-vectors of half-precision elements' variants: is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zm' times 2.

For the 'Four ZA single-vectors' and 'Four ZA single-vectors of half-precision elements' variants: is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32]; integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to nreg-1 constant bits(VL) operand1 = ZAvector[vec, VL]; constant bits(VL) operand2 = Z[m+r, VL]; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = FPAdd_ZA(element1, element2, FPCR); ZAvector[vec, VL] = result; vec = vec + vstride;
```

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |