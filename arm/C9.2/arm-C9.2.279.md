## C9.2.279 SUMOPS

Signed by unsigned integer sum of outer products, subtracting

The 8-bit integer variant works with a 32-bit element ZA tile.

The 16-bit integer variant works with a 64-bit element ZA tile.

This instruction multiplies the sub-matrix in the first source vector by the sub-matrix in the second source vector. In case of the 8-bit integer variant, the first source holds SVLS × 4 sub-matrix of signed 8-bit integer values, and the second source holds 4 × SVLS sub-matrix of unsigned 8-bit integer values. In case of the 16-bit integer variant, the first source holds SVLD × 4 sub-matrix of signed 16-bit integer values, and the second source holds 4 × SVLD sub-matrix of unsigned 16-bit integer values.

Each source vector is independently predicated by a corresponding governing predicate. When an 8-bit source element in case of 8-bit integer variant or a 16-bit source element in case of 16-bit integer variant is Inactive, it is treated as having the value 0.

The resulting SVLS × SVLS widened 32-bit integer or SVLD × SVLD widened 64-bit integer sum of outer products is then destructively subtracted from the 32-bit integer or 64-bit integer destination tile, respectively for 8-bit integer and 16-bit integer instruction variants. This is equivalent to performing a 4-way dot product and subtract from each of the destination tile elements.

In case of the 8-bit integer variant, each 32-bit container of the first source vector holds 4 consecutive column elements of each row of a SVLS × 4 sub-matrix, and each 32-bit container of the second source vector holds 4 consecutive row elements of each column of a 4 × SVLS sub-matrix. In case of the 16-bit integer variant, each 64-bit container of the first source vector holds 4 consecutive column elements of each row of a SVLD × 4 sub-matrix, and each 64-bit container of the second source vector holds 4 consecutive row elements of each column of a 4 × SVLD sub-matrix.

ID\_AA64SMFR0\_EL1.I16I64 indicates whether the 16-bit integer variant is implemented.

It has encodings from 2 classes: 32-bit and 64-bit

```
32-bit
```

(FEAT\_SME)

<!-- image -->

## Encoding

```
SUMOPS <ZAda>.S, <Pn>/M, <Pm>/M, <Zn>.B,
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda); constant boolean op1_unsigned = FALSE; constant boolean op2_unsigned = TRUE;
```

```
<Zm>.B
```

## 64-bit

(FEAT\_SME\_I16I64)

<!-- image -->

## Encoding

```
SUMOPS <ZAda>.D, <Pn>/M, <Pm>/M, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_I16I64) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda); constant boolean op1_unsigned = FALSE; constant boolean op2_unsigned = TRUE;
```

## Assembler Symbols

## &lt;ZAda&gt;

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3, encoded in the 'ZAda' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7, encoded in the 'ZAda' field.

## &lt;Pn&gt;

Is the name of the first governing scalable predicate register P0-P7, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second governing scalable predicate register P0-P7, encoded in the 'Pm' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV esize; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(dim*dim*esize) operand3 = ZAtile[da, esize, dim*dim*esize]; bits(dim*dim*esize) result; integer prod;
```

```
for row = 0 to dim-1 for col = 0 to dim-1 bits(esize) sum = Elem[operand3, row*dim+col, esize]; for k = 0 to 3 if (ActivePredicateElement(mask1, 4*row + k, esize DIV 4) && ActivePredicateElement(mask2, 4*col + k, esize DIV 4)) then constant bits(esize DIV 4) op1elt = Elem[operand1, 4*row + k, esize DIV 4]; constant bits(esize DIV 4) op2elt = Elem[operand2, 4*col + k, esize DIV 4]; constant integer element1 = if op1_unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if op2_unsigned then UInt(op2elt) else SInt(op2elt); prod = element1 * element2; sum = sum prod; Elem[result, row*dim+col, esize] = sum; ZAtile[da, esize, dim*dim*esize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.