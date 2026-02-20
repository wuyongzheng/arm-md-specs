## C9.2.118 FMOPS (non-widening)

Floating-point outer product, subtracting

The half-precision variant works with a 16-bit element ZA tile.

The single-precision variant works with a 32-bit element ZA tile.

The double-precision variant works with a 64-bit element ZA tile.

This instruction generates an outer product of the first source vector and the second source vector. In case of the half-precision variant, the first source is SVLH × 1 vector and the second source is 1 × SVLH vector. In case of the single-precision variant, the first source is SVLS × 1 vector and the second source is 1 × SVLS vector. In case of the double-precision variant, the first source is SVLD × 1 vector and the second source is 1 × SVLD vector.

Each source vector is independently predicated by a corresponding governing predicate. When either source vector element is Inactive the corresponding destination tile element remains unmodified.

The resulting outer product, SVLH × SVLH in case of half-precision variant, SVLS × SVLS in case of single-precision variant or SVLD × SVLD in case of double-precision variant, is then destructively subtracted from the destination tile. This is equivalent to performing a single multiply-subtract from each of the destination tile elements.

This instruction follows SME ZA-targeting floating-point behaviors.

ID\_AA64SMFR0\_EL1.F64F64 indicates whether the double-precision variant is implemented, and ID\_AA64SMFR0\_EL1.F16F16 indicates whether the half-precision variant is implemented.

It has encodings from 3 classes: Half-precision, Single-precision, and Double-precision

## Half-precision

(FEAT\_SME\_F16F16)

<!-- image -->

## Encoding

```
FMOPS <ZAda>.H, <Pn>/M, <Pm>/M, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda);
```

## Single-precision

(FEAT\_SME)

<!-- image -->

## Encoding

```
FMOPS <ZAda>.S, <Pn>/M, <Pm>/M, <Zn>.S, <Zm>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda);
```

## Double-precision

(FEAT\_SME\_F64F64)

<!-- image -->

## Encoding

```
FMOPS <ZAda>.D, <Pn>/M, <Pm>/M, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F64F64) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda);
```

## Assembler Symbols

## &lt;ZAda&gt;

For the 'Half-precision' variant: is the name of the ZA tile ZA0-ZA1, encoded in the 'ZAda' field.

For the 'Single-precision' variant: is the name of the ZA tile ZA0-ZA3, encoded in the 'ZAda' field.

For the 'Double-precision' variant: is the name of the ZA tile ZA0-ZA7, encoded in the 'ZAda' field.

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
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV esize; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) op1 = Z[n, VL]; constant bits(VL) op2 = Z[m, VL]; constant bits(dim*dim*esize) op3 = ZAtile[da, esize, dim*dim*esize]; bits(dim*dim*esize) result; for row = 0 to dim-1 for col = 0 to dim-1 constant bits(esize) elem2 = Elem[op2, col, esize]; constant bits(esize) elem3 = Elem[op3, row*dim+col, esize]; if (ActivePredicateElement(mask1, row, esize) && ActivePredicateElement(mask2, col, esize)) then constant bits(esize) elem1 = FPNeg(Elem[op1, row, esize], FPCR); Elem[result, row*dim+col, esize] = FPMulAdd_ZA(elem3, elem1, elem2, else Elem[result, row*dim+col, esize] = elem3; ZAtile[da, esize, dim*dim*esize] = result;
```

```
FPCR);
```