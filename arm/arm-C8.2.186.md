## C8.2.186 FDOT (2-way, vectors, FP8 to FP16)

8-bit floating-point dot product to half-precision

This instruction computes the fused sum-of-products of a pair of 8-bit floating-point values held in each 16-bit element of the first source and second source vectors. The half-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) , before being destructively added without intermediate rounding to the corresponding half-precision elements of the destination vector.

The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

## SVE2

((FEAT\_SVE2 &amp;&amp; FEAT\_FP8DOT2) || FEAT\_SSVE\_FP8DOT2)

<!-- image -->

## Encoding

```
FDOT <Zda>.H, <Zn>.B,
```

```
<Zm>.B
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !HaveSVE2FP8DOT2() then constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SSVE_FP8DOT2) && IsFeatureImplemented(FEAT_FP8DOT2) then CheckSVEEnabled(); elsif IsFeatureImplemented(FEAT_FP8DOT2) then CheckNonStreamingSVEEnabled(); else CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL];
```

```
bits(VL) result; for e = 0 to elements-1 constant bits(16) op1 = Elem[operand1, e, 16]; constant bits(16) op2 = Elem[operand2, e, 16]; bits(16) sum = Elem[operand3, e, 16]; sum = FP8DotAddFP(sum, op1, op2, FPCR, FPMR); Elem[result, e, 16] = sum; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.