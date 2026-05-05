## C7.2.45 F1CVTL, F1CVTL2, F2CVTL, F2CVTL2

8-bit floating-point convert to half-precision (vector)

This instruction converts each 8-bit floating-point element from the lower or upper half of the source vector to half-precision while downscaling the value, and places the results in the 16-bit elements of the destination vector. F1CVTL and F2CVTL convert the elements from the lower half of the source vector while scaling the values by 2 -UInt(FPMR.LSCALE[3:0]) and 2 -UInt(FPMR.LSCALE2[3:0]) , respectively. F1CVTL2 and F2CVTL2 convert the elements from the upper half of the source vector while scaling the values by 2 -UInt(FPMR.LSCALE[3:0]) and 2 -UInt(FPMR.LSCALE2[3:0]) , respectively.

The 8-bit floating-point encoding format for F1CVTL and F1CVTL2 is selected by FPMR.F8S1. The 8-bit floating-point encoding format for F2CVTL and F2CVTL2 is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_FP8)

<!-- image -->

## Encoding for the F1CVTL{2} variant

```
Applies when (size == 00) F1CVTL{2} <Vd>.8H,
```

```
<Vn>.<Ta>
```

## Encoding for the F2CVTL{2} variant

```
Applies when (size == 01) F2CVTL{2} <Vd>.8H,
```

```
<Vn>.<Ta>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF);
```

```
constant integer n = UInt(Rn); constant integer d = UInt(Rd); constant integer part = UInt(Q); constant integer elements = 64 DIV 8; constant boolean issrc2 = size == '01';
```

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vd&gt;

&lt;Vn&gt;

&lt;Ta&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(64) operand = Vpart[n, part, 64]; bits(128) result; for e = 0 to elements-1 Elem[result, e, 16] = FP8ConvertFP(Elem[operand, e, 8], V[d, 128] = result;
```

|   Q | <Ta>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |

```
issrc2, FPCR, FPMR);
```
