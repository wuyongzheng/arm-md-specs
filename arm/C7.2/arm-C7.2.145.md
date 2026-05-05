## C7.2.145 FMLALB, FMLALT (by element)

8-bit floating-point multiply-add to half-precision (vector, by element)

This instruction widens the even-numbered (bottom) or odd-numbered (top) 8-bit elements in the first source vector and the indexed element from the second source vector to half-precision format and multiplies the corresponding elements. The intermediate products are scaled by 2 -UInt(FPMR.LSCALE[3:0]) , before being destructively added without intermediate rounding to the half-precision elements of the destination vector that overlap with the corresponding 8-bit floating-point elements in the first source vector.

The 8-bit floating-point encoding format for the elements of the first source vector is selected by FPMR.F8S1. The 8-bit floating-point encoding format for the elements of the second source vector is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_FP8FMA)

<!-- image -->

## Encoding for the FMLALB variant

```
Applies when (Q == 0) FMLALB <Vd>.8H, <Vn>.16B, <Vm>.B[<index>]
```

## Encoding for the FMLALT variant

```
Applies when (Q == 1) FMLALT <Vd>.8H,
```

```
<Vn>.16B, <Vm>.B[<index>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP8FMA) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt('00':Rm<2:0>); constant integer d = UInt(Rd); constant integer index = UInt(H:L:M:Rm<3>); constant integer elements = 128 DIV 16; constant integer sel = UInt(Q);
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, in the range V0 to V7, encoded in the 'Rm&lt;2:0&gt;' field.

## &lt;index&gt;

Is the element index, in the range 0 to 15, encoded in the 'H:L:M:Rm&lt;3&gt;' fields.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[n, 128]; constant bits(128) operand2 = V[m, 128]; constant bits(128) operand3 = V[d, 128]; bits(128) result; for e = 0 to elements-1 constant bits(8) element1 = Elem[operand1, 2 * e + sel, 8]; constant bits(8) element2 = Elem[operand2, index, 8]; constant bits(16) element3 = Elem[operand3, e, 16]; Elem[result, e, 16] = FP8MulAddFP(element3, element1, element2, FPCR, V[d, 128] = result;
```

```
FPMR);
```
