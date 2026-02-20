## C8.2.226 FMLALLTB (indexed)

8-bit floating-point multiply-add by indexed element to single-precision (top bottom)

This instruction widens the third 8-bit element of each 32-bit container in the first source vector and the indexed element from the corresponding 128-bit segment in the second source vector to single-precision format and multiplies the corresponding elements. The intermediate products are scaled by 2 -UInt(FPMR.LSCALE) before being destructively added without intermediate rounding to the single-precision elements of the destination vector that overlap with the corresponding 8-bit floating-point elements in the first source vector. The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

## SVE2

((FEAT\_SVE2 &amp;&amp; FEAT\_FP8FMA) || FEAT\_SSVE\_FP8FMA)

<!-- image -->

## Encoding

```
FMLALLTB <Zda>.S, <Zn>.B, <Zm>.B[<imm>]
```

## Decode for this encoding

```
then EndOfDecode(Decode_UNDEF);
```

```
if !HaveSVE2FP8FMA() constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer index = UInt(i4h:i4l);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the immediate index, in the range 0 to 15, encoded in the 'i4h:i4l' fields.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SSVE_FP8FMA) && IsFeatureImplemented(FEAT_FP8FMA) CheckSVEEnabled(); elsif IsFeatureImplemented(FEAT_FP8FMA) then CheckNonStreamingSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32;
```

```
then
```

```
constant integer eltspersegment = 128 DIV 32; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = 4 * segmentbase + index; constant bits(8) element1 = Elem[operand1, 4 * e + 2, 8]; constant bits(8) element2 = Elem[operand2, s, 8]; constant bits(32) element3 = Elem[operand3, e, 32]; Elem[result, e, 32] = FP8MulAddFP(element3, element1, element2, FPCR, Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
FPMR);
```