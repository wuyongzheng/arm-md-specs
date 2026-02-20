## C9.2.48 BFMUL (multiple vectors)

Multi-vector BFloat16 multiply

This instruction multiplies all the BFloat16 elements of the two or four first source vectors with the corresponding elements of the two or four second source vectors and places the results in the corresponding elements of the two or four destination vectors.

This instruction follows SME2 non-widening BFloat16 numerical behaviors corresponding to instructions that place their results in two or four SVE Z vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

```
Two registers (FEAT_SME2 && FEAT_SVE_BFSCALE)
```

<!-- image -->

## Encoding

```
BFMUL { <Zd1>.H-<Zd2>.H }, { <Zn1>.H-<Zn2>.H }, { <Zm1>.H-<Zm2>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_SVE_BFSCALE) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Zd:'0'); constant integer n = UInt(Zn:'0'); constant integer m = UInt(Zm:'0'); constant integer nreg = 2;
```

## Four registers

(FEAT\_SME2 &amp;&amp; FEAT\_SVE\_BFSCALE)

<!-- image -->

## Encoding

```
BFMUL { <Zd1>.H-<Zd4>.H }, { <Zn1>.H-<Zn4>.H }, { <Zm1>.H-<Zm4>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_SVE_BFSCALE) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Zd:'00'); constant integer n = UInt(Zn:'00'); constant integer m = UInt(Zm:'00'); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the first source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = constant bits(VL) operand2 =
```

```
Z[n+r, VL]; Z[m+r, VL]; for e = 0 to elements-1
```

```
constant bits(16) element1 = Elem[operand1, e, 16]; constant bits(16) element2 = Elem[operand2, e, 16]; Elem[results[r], e, 16] = BFMul(element1, element2, FPCR); for r = 0 to nreg-1 Z[d+r, VL] = results[r];
```