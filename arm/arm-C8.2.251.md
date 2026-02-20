## C8.2.251 FMUL (indexed)

Floating-point multiply by indexed element

This instruction multiplies all floating-point elements within each 128-bit segment of the first source vector by the specified element in the corresponding second source vector segment. The results are placed in the corresponding elements of the destination vector.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment. This instruction is unpredicated.

It has encodings from 3 classes: Half-precision, Single-precision, and Double-precision

## Half-precision

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMUL <Zd>.H, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Single-precision

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMUL <Zd>.S, <Zn>.S, <Zm>.S[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Double-precision

## (FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMUL <Zd>.D, <Zn>.D, <Zm>.D[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer index = UInt(i1); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

For the 'Half-precision' and 'Single-precision' variants: is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

For the 'Double-precision' variant: is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;imm&gt;

For the 'Half-precision' variant: is the immediate index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

For the 'Single-precision' variant: is the immediate index, in the range 0 to 3, encoded in the 'i2' field.

For the 'Double-precision' variant: is the immediate index, in the range 0 to 1, encoded in the 'i1' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 DIV esize; constant bits(VL) op1 = Z[n, VL]; constant bits(VL) op2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = constant integer s = segmentbase + index; constant bits(esize) elem2 = Elem[op2, s, esize];
```

```
e - (e MOD eltspersegment);
```

```
constant bits(esize) elem1 = Elem[op1, e, esize]; Elem[result, e, esize] = FPMul(elem1, elem2, FPCR); Z[d, VL] = result;
```