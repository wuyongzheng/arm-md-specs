## C9.2.26 BFMINNM (multiple vectors)

Multi-vector BFloat16 minimum number

This instruction determines the minimum number value of BFloat16 elements of the two or four second source vectors and the corresponding BFloat16 elements of the two or four first source vectors and destructively places the results in the corresponding elements of the two or four first source vectors.

Regardless of the value of FPCR.AH, the behavior is as follows:

- Negative zero compares less than positive zero.
- If one element is numeric and the other is a quiet NaN, the result is the numeric value.
- When FPCR.DN is 0, if either element is a signaling NaN or if both elements are NaNs, the result is a quiet NaN.
- When FPCR.DN is 1, if either element is a signaling NaN or if both elements are NaNs, the result is Default NaN.

This instruction follows SME2 non-widening BFloat16 numerical behaviors corresponding to instructions that place their results in two or four SVE Z vectors.

This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.B16B16 indicates whether this instruction is implemented.

It has encodings from 2 classes: Two registers and Four registers

## Two registers

(FEAT\_SME2 &amp;&amp; FEAT\_SVE\_B16B16)

<!-- image -->

## Encoding

```
BFMINNM { <Zdn1>.H-<Zdn2>.H }, { <Zdn1>.H-<Zdn2>.H }, { <Zm1>.H-<Zm2>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_SVE_B16B16) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn:'0'); constant integer m = UInt(Zm:'0'); constant integer nreg = 2;
```

## Four registers

(FEAT\_SME2 &amp;&amp; FEAT\_SVE\_B16B16)

<!-- image -->

## Encoding

```
BFMINNM { <Zdn1>.H-<Zdn4>.H }, { <Zdn1>.H-<Zdn4>.H }, { <Zm1>.H-<Zm4>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_SVE_B16B16) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn:'00'); constant integer m = UInt(Zm:'00'); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zdn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4.

## &lt;Zdn2&gt;

Is the name of the second scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2 plus 1.

## &lt;Zm1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4.

## &lt;Zm2&gt;

Is the name of the second scalable vector register of the second source multi-vector group, encoded as 'Zm' times 2 plus 1.

## &lt;Zdn4&gt;

Is the name of the fourth scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4 plus 3.

## &lt;Zm4&gt;

Is the name of the fourth scalable vector register of the second source multi-vector group, encoded as 'Zm' times 4 plus 3.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[dn+r, VL]; constant bits(VL) operand2 = Z[m+r, VL]; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, e, 16]; constant bits(16) element2 = Elem[operand2, e, 16]; Elem[results[r], e, 16] = BFMinNum(element1, element2, FPCR); for r = 0 to nreg-1 Z[dn+r, VL] = results[r];
```