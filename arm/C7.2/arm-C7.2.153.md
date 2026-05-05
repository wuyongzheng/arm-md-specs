## C7.2.153 FMMLA (widening, 8-bit floating-point to half-precision)

8-bit floating-point matrix multiply-accumulate to half-precision

This instruction performs the fused sum-of-products within each four adjacent 8-bit elements while multiplying the 2 × 4 matrix of 8-bit floating-point values held in each 64-bit segment of the first source vector by the 4 × 2 matrix of 8-bit floating-point values in the corresponding segment of the second source vector. The half-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) , before being destructively added without intermediate rounding to the 2x2 half-precision matrix in the destination vector. This is equivalent to accumulating 4-way dot product per destination element.

The 8-bit floating-point encoding format for the elements of the first source vector is selected by FPMR.F8S1. The 8-bit floating-point encoding format for the elements of the second source vector is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_F8F16MM)

<!-- image -->

## Encoding

```
FMMLA <Vd>.8H, <Vn>.16B, <Vm>.16B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F8F16MM) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Rd);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP third source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = constant bits(128) operand2 = constant bits(128) operand3 = bits(128) result; bits(64) op1, op2, acc; for s = 0 to 1 op1 = Elem[operand1, s, 64]; op2 = Elem[operand2, s, 64];
```

```
V[n, 128]; V[m, 128]; V[d, 128];
```

```
acc = Elem[operand3, s, 64]; Elem[result, s, 64] = FP8MatMulAddFP(acc, op1, op2, 4, FPCR, FPMR); V[d, 128] = result;
```
