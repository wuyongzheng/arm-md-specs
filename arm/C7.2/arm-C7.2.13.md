## C7.2.13 BF1CVTL, BF1CVTL2, BF2CVTL, BF2CVTL2

8-bit floating-point convert to BFloat16 (vector)

This instruction converts each 8-bit floating-point element from the lower or upper half of the source vector to BFloat16 while downscaling the value, and places the results in the 16-bit elements of the destination vector. BF1CVTL and BF2CVTL convert the elements from the lower half of the source vector while scaling the values by 2 -UInt(FPMR.LSCALE[5:0]) and 2 -UInt(FPMR.LSCALE2[5:0]) , respectively. BF1CVTL2 and BF2CVTL2 convert the elements from the upper half of the source vector while scaling the values by 2 -UInt(FPMR.LSCALE[5:0]) and 2 -UInt(FPMR.LSCALE2[5:0]) , respectively.

The 8-bit floating-point encoding format for BF1CVTL and BF1CVTL2 is selected by FPMR.F8S1. The 8-bit floating-point encoding format for BF2CVTL and BF2CVTL2 is selected by FPMR.F8S2.

## Advanced SIMD

(FEAT\_FP8)

<!-- image -->

## Encoding for the BF1CVTL{2} variant

```
Applies when (size == 10) BF1CVTL{2} <Vd>.8H, <Vn>.<Ta>
```

## Encoding for the BF2CVTL{2} variant

Applies when

```
(size == 11) BF2CVTL{2} <Vd>.8H, <Vn>.<Ta>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer part = UInt(Q); constant integer elements = 64 DIV 8; constant boolean issrc2 = size == '11';
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
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(64) operand = Vpart[n, part, 64]; bits(128) result; for e = 0 to elements-1 Elem[result, e, 16] = FP8ConvertBF(Elem[operand, e, 8], V[d, 128] = result;
```

|   Q | <Ta>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |

```
issrc2, FPCR, FPMR);
```
