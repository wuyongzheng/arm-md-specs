## C9.2.49 BFSCALE (multiple and single vector)

Multi-vector BFloat16 adjust exponent by vector

This instruction multiplies the BFloat16 elements of the two or four first source vectors by 2.0 to the power of the signed integer values in the corresponding elements of the second source vector and destructively places the results in the corresponding elements of the two or four first source vectors.

This instruction follows SME2 non-widening BFloat16 numerical behaviors corresponding to instructions that place their results in two or four SVE Z vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

## Two registers

(FEAT\_SME2 &amp;&amp; FEAT\_SVE\_BFSCALE)

<!-- image -->

## Encoding

```
BFSCALE { <Zdn1>.H-<Zdn2>.H }, { <Zdn1>.H-<Zdn2>.H }, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_SVE_BFSCALE) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn:'0'); constant integer m = UInt('0':Zm); constant integer nreg = 2;
```

## Four registers

(FEAT\_SME2 &amp;&amp; FEAT\_SVE\_BFSCALE)

<!-- image -->

## Encoding

```
BFSCALE { <Zdn1>.H-<Zdn4>.H }, { <Zdn1>.H-<Zdn4>.H }, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_SVE_BFSCALE) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn:'00'); constant integer m = UInt('0':Zm); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zdn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4.

## &lt;Zdn2&gt;

Is the name of the second scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2 plus 1.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;Zdn4&gt;

Is the name of the fourth scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[dn+r, VL]; constant bits(VL) operand2 = Z[m, VL]; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, e, 16]; constant integer element2 = SInt(Elem[operand2, e, 16]); Elem[results[r], e, 16] = BFScale(element1, element2, FPCR); for r = 0 to nreg-1 Z[dn+r, VL] = results[r];
```