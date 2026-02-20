## C8.2.187 FDOT (2-way, indexed, FP8 to FP16)

8-bit floating-point dot product by indexed element to half-precision

This instruction computes the fused sum-of-products of a pair of 8-bit floating-point values held in each 16-bit element of the first source vector and a pair of 8-bit floating-point values in an indexed 16-bit element of the second source vector. The half-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) , before being destructively added without intermediate rounding to the corresponding half-precision elements of the destination vector.

The 8-bit floating-point groups within the second source vector are specified using an immediate index that selects the same group position within each 128-bit vector segment. The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

## SVE2

((FEAT\_SVE2 &amp;&amp; FEAT\_FP8DOT2) || FEAT\_SSVE\_FP8DOT2)

<!-- image -->

op

## Encoding

```
FDOT <Zda>.H, <Zn>.B, <Zm>.B[<imm>]
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !HaveSVE2FP8DOT2() then constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer index = UInt(i3h:i3l);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the immediate index of a pair of 8-bit elements within each 128-bit vector segment, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SSVE_FP8DOT2) && IsFeatureImplemented(FEAT_FP8DOT2) then CheckSVEEnabled(); elsif IsFeatureImplemented(FEAT_FP8DOT2) then CheckNonStreamingSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant integer eltspersegment = 128 DIV 16; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant bits(16) op1 = Elem[operand1, e, 16]; constant bits(16) op2 = Elem[operand2, s, 16]; bits(16) sum = Elem[operand3, e, 16]; sum = FP8DotAddFP(sum, op1, op2, FPCR, FPMR); Elem[result, e, 16] = sum; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.