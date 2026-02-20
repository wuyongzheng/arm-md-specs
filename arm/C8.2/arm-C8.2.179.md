## C8.2.179 FCVTXNT

Double-precision convert to single-precision, rounding to odd (top, predicated)

This instruction converts active double-precision elements from the source vector to single-precision, rounding to Odd, and places the results in the odd-numbered 32-bit elements of the destination vector, leaving the even-numbered elements unchanged. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

Rounding to Odd (aka Von Neumann rounding) permits a two-step conversion from double-precision to half-precision without incurring intermediate rounding errors.

It has encodings from 2 classes: Double-precision to single-precision, merging and Double-precision to single-precision, zeroing

Double-precision to single-precision, merging

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVTXNT <Zd>.S, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = TRUE;
```

Double-precision to single-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVTXNT <Zd>.S, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = FALSE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant integer halfesize = esize DIV 2; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = Z[d, VL]; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; Elem[result, 2*e + 1, halfesize] = FPConvertSVE(element, FPCR, FPRounding_ODD, halfesize); elsif !merging then Elem[result, 2*e + 1, halfesize] = Zeros(halfesize); Z[d, VL] = result;
```