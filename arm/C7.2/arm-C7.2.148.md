## C7.2.148 FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (vector)

8-bit floating-point multiply-add to single-precision (vector)

This instruction widens the first (bottom bottom), second (bottom top), third (top bottom), or fourth (top top) 8-bit element of each 32-bit container in the first and second source vectors to single-precision format and multiplies the corresponding elements. The intermediate products are scaled by 2 -UInt(FPMR.LSCALE) , before being destructively added without intermediate rounding to the single-precision elements of the destination vector that overlap with the corresponding 8-bit floating-point elements in the source vectors.

The 8-bit floating-point encoding format for the elements of the first source vector is selected by FPMR.F8S1. The 8-bit floating-point encoding format for the elements of the second source vector is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_FP8FMA)

<!-- image -->

## Encoding for the FMLALLBB variant

```
Applies when (Q == 0 && size == 00) FMLALLBB <Vd>.4S, <Vn>.16B, <Vm>.16B
```

## Encoding for the FMLALLBT variant

```
Applies when (Q == 0 && size == 01) FMLALLBT <Vd>.4S, <Vn>.16B, <Vm>.16B
```

## Encoding for the FMLALLTB variant

```
== 00)
```

```
Applies when (Q == 1 && size FMLALLTB <Vd>.4S, <Vn>.16B, <Vm>.16B
```

## Encoding for the FMLALLTT variant

```
== 01)
```

```
Applies when (Q == 1 && size FMLALLTT <Vd>.4S, <Vn>.16B, <Vm>.16B
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP8FMA) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q:size<0>);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[n, 128]; constant bits(128) operand2 = V[m, 128]; constant bits(128) operand3 = V[d, 128]; bits(128) result; for e = 0 to elements-1 constant bits(8) element1 = Elem[operand1, 4 * e + sel, 8]; constant bits(8) element2 = Elem[operand2, 4 * e + sel, 8]; constant bits(32) element3 = Elem[operand3, e, 32]; Elem[result, e, 32] = FP8MulAddFP(element3, element1, element2, FPCR, FPMR); V[d, 128] = result;
```
