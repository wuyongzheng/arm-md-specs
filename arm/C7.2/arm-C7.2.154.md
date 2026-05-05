## C7.2.154 FMMLA (widening, 8-bit floating-point to single-precision)

8-bit floating-point matrix multiply-accumulate to single-precision

This instruction performs the fused sum-of-products within each eight adjacent 8-bit elements while multiplying the 2 × 8 matrix of 8-bit floating-point values in the first source vector by the 8 × 2 matrix of 8-bit floating-point values in the second source vector. The single-precision sum-of-products are scaled by 2 -UInt(FPMR.LSCALE) , before being destructively added without intermediate rounding to the 2x2 single-precision matrix in the destination vector. This is equivalent to accumulating 8-way dot product per destination element.

The 8-bit floating-point encoding format for the elements of the first source vector is selected by FPMR.F8S1. The 8-bit floating-point encoding format for the elements of the second source vector is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_F8F32MM)

<!-- image -->

## Encoding

```
FMMLA <Vd>.4S, <Vn>.16B, <Vm>.16B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F8F32MM) then EndOfDecode(Decode_UNDEF);
```

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Rd);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP third source and destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) op1 = V[n, 128]; constant bits(128) op2 = V[m, 128]; constant bits(128) acc = V[d, 128]; V[d, 128] = FP8MatMulAddFP(acc, op1, op2, 8, FPCR, FPMR);
```
