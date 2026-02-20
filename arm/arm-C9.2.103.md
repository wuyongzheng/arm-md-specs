## C9.2.103 FMLS (multiple vectors)

Multi-vector floating-point fused multiply-subtract

This instruction multiplies the corresponding floating-point elements of the two or four first and second source vectors and destructively subtracts these values without intermediate rounding from the corresponding elements of the ZA single-vector groups.

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
FMLS ZA.<T>[<Wv>, <offs>{, VGx2}], { <Zn1>.<T>-<Zn2>.<T> }, { <Zm1>.<T>-<Zm2>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if sz == '1' && !IsFeatureImplemented(FEAT_SME_F64F64) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off3); constant integer nreg = 2;
```

Two ZA single-vectors of half-precision elements

(FEAT\_SME\_F16F16)

<!-- image -->

## Encoding

```
FMLS ZA.H[<Wv>, <offs>{, VGx2}], { <Zn1>.H-<Zn2>.H }, { <Zm1>.H-<Zm2>.H }
```

```
}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then EndOfDecode(Decode_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 16; constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer offset = UInt(off3); constant integer nreg = 2;
```

<!-- image -->

<!-- image -->

## Four ZA single-vectors (FEAT\_SME2) 1 31 1 0 30 29 0 0 0 0 28 25 1 1 24 23 sz 22 1 21 Zm 20 18 0 17 1 0 16 15 Rv 14 13 1 1 0 12 10 Zn 9 7 0 0 6 5 0 4 1 3 off3 2 0 S Encoding FMLS ZA.&lt;T&gt;[&lt;Wv&gt;, &lt;offs&gt;{, VGx4}], { &lt;Zn1&gt;.&lt;T&gt;-&lt;Zn4&gt;.&lt;T&gt; }, { &lt;Zm1&gt;.&lt;T&gt;-&lt;Zm4&gt;.&lt;T&gt; } Decode for this encoding if !IsFeatureImplemented(FEAT\_SME2) then EndOfDecode(Decode\_UNDEF); if sz == '1' &amp;&amp; !IsFeatureImplemented(FEAT\_SME\_F64F64) then EndOfDecode(Decode\_UNDEF); constant integer v = UInt('010':Rv); constant integer esize = 32 &lt;&lt; UInt(sz); constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off3); constant integer nreg = 4; Four ZA single-vectors of half-precision elements (FEAT\_SME\_F16F16) 1 31 1 0 30 29 0 0 0 0 28 25 1 1 24 23 0 22 1 21 Zm 20 18 0 17 1 0 16 15 Rv 14 13 1 0 0 12 10 Zn 9 7 0 0 6 5 1 4 1 3 off3 2 0 sz S Encoding FMLS ZA.H[&lt;Wv&gt;, &lt;offs&gt;{, VGx4}], { &lt;Zn1&gt;.H-&lt;Zn4&gt;.H }, { &lt;Zm1&gt;.H-&lt;Zm4&gt;.H } Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then constant integer v = UInt('010':Rv); constant integer esize = 16; constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer offset = UInt(off3); constant integer nreg = 4;
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;T&gt;

Is the size specifier, encoded in 'sz':

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W8-W11, encoded in the 'Rv' field.

## &lt;offs&gt;

Is the vector select offset, in the range 0 to 7, encoded in the 'off3' field.

## &lt;Zn1&gt;

For the 'Two ZA single-vectors' and 'Two ZA single-vectors of half-precision elements' variants: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four ZA single-vectors' and 'Four ZA single-vectors of half-precision elements' variants: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two ZA single-vectors' and 'Two ZA single-vectors of half-precision elements' variants: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four ZA single-vectors' and 'Four ZA single-vectors of half-precision elements' variants: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer vectors = VL DIV 8; constant integer vstride = vectors DIV nreg; constant bits(32) vbase = X[v, 32];
```

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

```
integer vec = (UInt(vbase) + offset) MOD vstride; bits(VL) result; for r = 0 to nreg-1 constant bits(VL) op1 = Z[n+r, VL]; constant bits(VL) op2 = Z[m+r, VL]; constant bits(VL) op3 = ZAvector[vec, VL]; for e = 0 to elements-1 constant bits(esize) elem1 = FPNeg(Elem[op1, e, esize], FPCR); constant bits(esize) elem2 = Elem[op2, e, esize]; constant bits(esize) elem3 = Elem[op3, e, esize]; Elem[result, e, esize] = FPMulAdd_ZA(elem3, elem1, elem2, FPCR); ZAvector[vec, VL] = result; vec = vec + vstride;
```