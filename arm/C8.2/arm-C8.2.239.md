## C8.2.239 FMMLA (widening, FP8 to FP16)

8-bit floating-point matrix multiply-accumulate to half-precision

This instruction performs the fused sum-of-products within each four adjacent 8-bit elements while multiplying the 2 × 4 matrix of 8-bit floating-point values held in each 64-bit segment of the first source vector with the 4 × 2 matrix of 8-bit floating-point values in the corresponding segment of the second source vector. The half-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) , before being destructively added without intermediate rounding to the 2 × 2 half-precision matrix in the corresponding segment of the destination vector. This is equivalent to accumulating 4-way dot product per destination element.

The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE2 &amp;&amp; FEAT\_F8F16MM)

<!-- image -->

## Encoding

```
FMMLA <Zda>.H, <Zn>.B, <Zm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) || !IsFeatureImplemented(FEAT_F8F16MM) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

&lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckFPMREnabled(); CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 64; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL];
```

```
bits(VL) result; for s = 0 to segments-1 constant bits(64) op1 = Elem[operand1, s, 64]; constant bits(64) op2 = Elem[operand2, s, 64]; constant bits(64) addend = Elem[operand3, s, 64]; constant integer way = 4; Elem[result, s, 64] = FP8MatMulAddFP(addend, op1, op2, way, FPCR, Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
FPMR);
```