## C8.2.216 FMLA (indexed)

Floating-point fused multiply-add by indexed element

This instruction multiplies all floating-point elements within each 128-bit segment of the first source vector by the specified element in the corresponding second source vector segment. The products are then destructively added without intermediate rounding to the corresponding elements of the addend and destination vector.

The elements within the second source vector are specified using an immediate index that selects the same element position within each 128-bit vector segment. The index range is from 0 to one less than the number of elements per 128-bit segment. This instruction is unpredicated.

It has encodings from 3 classes: Half-precision, Single-precision, and Double-precision

## Half-precision

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMLA <Zda>.H, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer index = UInt(i3h:i3l); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean op1_neg = FALSE; constant boolean op3_neg = FALSE;
```

## Single-precision

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMLA <Zda>.S, <Zn>.S,
```

```
<Zm>.S[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean op1_neg = FALSE; constant boolean op3_neg = FALSE;
```

## Double-precision

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMLA <Zda>.D, <Zn>.D, <Zm>.D[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer index = UInt(i1); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean op1_neg = FALSE; constant boolean op3_neg = FALSE;
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 DIV esize; constant bits(VL) op1 = Z[n, VL]; constant bits(VL) op2 = Z[m, VL]; bits(VL) result = Z[da, VL]; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant bits(esize) elem2 = Elem[op2, s, esize]; constant bits(esize) elem1 = (if op1_neg then FPNeg(Elem[op1, e, esize], FPCR) else Elem[op1, e, esize]); constant bits(esize) elem3 = (if op3_neg then FPNeg(Elem[result, e, esize], FPCR) else Elem[result, e, esize]); Elem[result, e, esize] = FPMulAdd(elem3, elem1, elem2, FPCR); Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.