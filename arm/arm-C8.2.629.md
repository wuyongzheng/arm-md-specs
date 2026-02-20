## C8.2.629 SQDMLALB (indexed)

Signed saturating doubling multiply-add by indexed element (bottom)

This instruction multiples the even-numbered signed elements within each 128-bit segment of the first source vector and specified signed element in the corresponding second source vector segment and then doubles the result of the multiplication. Each intermediate value is saturated to the double-width N-bit value's signed integer range -2 (N-1) to (2 (N-1) )-1 and is then destructively added to the overlapping double-width elements of the addend and destination vector. Each destination element is saturated to the double-width N-bit element's signed integer range -2 (N-1) to (2 (N-1) )-1.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

It has encodings from 2 classes: 32-bit and 64-bit

## 32-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQDMLALB <Zda>.S, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel = 0;
```

## 64-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQDMLALB <Zda>.D, <Zn>.S, <Zm>.S[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2h:i2l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel = 0;
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant integer eltspersegment = 128 DIV (2 * esize); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Z[da, VL]; for e = 0 to elements-1 constant integer s = e - (e MOD eltspersegment); constant integer element1 = SInt(Elem[operand1, 2 * e + sel, esize]); constant integer element2 = SInt(Elem[operand2, 2 * s + index, esize]); constant integer element3 = SInt(Elem[result, e, 2*esize]); constant integer product = SInt(SignedSat(2 * element1 * element2, 2*esize)); constant integer res = element3 + product; Elem[result, e, 2*esize] = SignedSat(res, 2*esize); Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.