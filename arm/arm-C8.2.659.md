## C8.2.659 SQRDMLSH (indexed)

Signed saturating rounding doubling multiply-subtract high by indexed element

This instruction multiplies then doubles all signed elements within each 128-bit segment of the first source vector and the specified signed element of the corresponding second source vector segment, and destructively subtracts the rounded high half of each result to the corresponding elements of the addend and destination vector. Each destination element is saturated to the N-bit element's signed integer range -2 (N-1) to (2 (N-1) )-1.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

It has encodings from 3 classes: 16-bit, 32-bit, and 64-bit

## 16-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQRDMLSH <Zda>.H, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## 32-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQRDMLSH <Zda>.S, <Zn>.S, <Zm>.S[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

S

## 64-bit

## (FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQRDMLSH <Zda>.D, <Zn>.D, <Zm>.D[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer index = UInt(i1); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = constant integer s = segmentbase + index;
```

```
e - (e MOD eltspersegment);
```

```
constant integer element1 = SInt(Elem[operand1, e, esize]); constant integer element2 = SInt(Elem[operand2, s, esize]); constant integer element3 = SInt(Elem[operand3, e, esize]); constant integer res = (element3 << esize) (2 * element1 * element2); Elem[result, e, esize] = SignedSat((res + (1 << (esize - 1))) >> esize, esize); Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.