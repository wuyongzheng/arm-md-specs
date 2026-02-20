## C8.2.837 UMLSLT (indexed)

Unsigned multiply-subtract long by indexed element (top)

This instruction multiplies the odd-numbered unsigned elements within each 128-bit segment of the first source vector by the specified unsigned element in the corresponding second source vector segment and destructively subtracts from the overlapping double-width elements of the addend vector.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment.

It has encodings from 2 classes: 32-bit and 64-bit

## 32-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
UMLSLT <Zda>.S, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel = 1;
```

## 64-bit

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
UMLSLT <Zda>.D, <Zn>.S, <Zm>.S[<imm>]
```

U

U

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2h:i2l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel = 1;
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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant integer eltspersegment = 128 DIV (2 * esize); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Z[da, VL]; for e = 0 to elements-1 constant integer s = e - (e MOD eltspersegment); constant integer element1 = UInt(Elem[operand1, 2 * e + sel, esize]); constant integer element2 = UInt(Elem[operand2, 2 * s + index, esize]); constant bits(2*esize) product = (element1 * element2)<2*esize-1:0>; Elem[result, e, 2*esize] = Elem[result, e, 2*esize] product; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.