## C8.2.185 FDOT (4-way, indexed)

8-bit floating-point dot product by indexed element to single-precision

This instruction computes the fused sum-of-products of a group of four 8-bit floating-point values held in each 32-bit element of the first source vector and a group of four 8-bit floating-point values in an indexed 32-bit element of the second source vector. The single-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE) , before being destructively added without intermediate rounding to the corresponding single-precision elements of the destination vector.

The 8-bit floating-point groups within the second source vector are specified using an immediate index that selects the same group position within each 128-bit vector segment. The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

## SVE2

((FEAT\_SVE2 &amp;&amp; FEAT\_FP8DOT4) || FEAT\_SSVE\_FP8DOT4)

<!-- image -->

## Encoding

```
FDOT <Zda>.S, <Zn>.B, <Zm>.B[<imm>]
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !HaveSVE2FP8DOT4() then constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer index = UInt(i2);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the immediate index of a 32-bit group of four 8-bit values within each 128-bit vector segment, in the range 0 to 3, encoded in the 'i2' field.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SSVE_FP8DOT4) && IsFeatureImplemented(FEAT_FP8DOT4) then CheckSVEEnabled(); elsif IsFeatureImplemented(FEAT_FP8DOT4) then CheckNonStreamingSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant integer eltspersegment = 128 DIV 32; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant bits(32) op1 = Elem[operand1, e, 32]; constant bits(32) op2 = Elem[operand2, s, 32]; bits(32) sum = Elem[operand3, e, 32]; sum = FP8DotAddFP(sum, op1, op2, FPCR, FPMR); Elem[result, e, 32] = sum; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.