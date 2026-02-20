## C8.2.661 SQRDMULH (indexed)

Signed saturating rounding doubling multiply high by indexed element

This instruction multiplies all signed elements within each 128-bit segment of the first source vector by the specified signed element in the corresponding second source vector segment, then doubles and places the most significant rounded half of the result in the corresponding elements of the destination vector register. Each result element is saturated to the N-bit element's signed integer range -2 (N-1) to (2 (N-1) )-1.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

It has encodings from 3 classes: 16-bit, 32-bit, and 64-bit

## 16-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQRDMULH <Zd>.H, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## 32-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQRDMULH <Zd>.S, <Zn>.S, <Zm>.S[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

R

## 64-bit

## (FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQRDMULH <Zd>.D, <Zn>.D, <Zm>.D[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer index = UInt(i1); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

For the '16-bit' and '32-bit' variants: is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

For the '64-bit' variant: is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;imm&gt;

For the '16-bit' variant: is the element index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

For the '32-bit' variant: is the element index, in the range 0 to 3, encoded in the 'i2' field.

For the '64-bit' variant: is the element index, in the range 0 to 1, encoded in the 'i1' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant integer element1 = SInt(Elem[operand1, e, esize]);
```

```
constant integer element2 = SInt(Elem[operand2, s, esize]); constant integer res = 2 * element1 * element2; Elem[result, e, esize] = SignedSat((res + (1 << (esize - 1))) >> esize, esize); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.