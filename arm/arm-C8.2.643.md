## C8.2.643 SQDMULLT (indexed)

Signed saturating doubling multiply by indexed element (top)

This instruction multiplies then doubles the odd-numbered signed elements within each 128-bit segment of the first source vector and the specified element in the corresponding second source vector segment, and places the results in overlapping double-width elements of the destination vector register. Each result element is saturated to the double-width N-bit element's signed integer range -2 (N-1) to (2 (N-1) )-1.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

It has encodings from 2 classes: 32-bit and 64-bit

## 32-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQDMULLT <Zd>.S, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer sel = 1;
```

## 64-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQDMULLT <Zd>.D, <Zn>.S, <Zm>.S[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2h:i2l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer sel = 1;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

For the '32-bit' variant: is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

For the '64-bit' variant: is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;imm&gt;

For the '32-bit' variant: is the element index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

For the '64-bit' variant: is the element index, in the range 0 to 3, encoded in the 'i2h:i2l' fields.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant integer eltspersegment = 128 DIV (2 * esize); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant integer s = e - (e MOD eltspersegment); constant integer element1 = SInt(Elem[operand1, 2 * e + sel, esize]); constant integer element2 = SInt(Elem[operand2, 2 * s + index, esize]); constant integer res = 2 * element1 * element2; Elem[result, e, 2*esize] = SignedSat(res, 2*esize); Z[d, VL] = result;
```