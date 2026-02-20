## C8.2.148 F1CVTLT, F2CVTLT

8-bit floating-point convert to half-precision (top)

This instruction converts each odd-numbered 8-bit floating-point element of the source vector to half-precision while downscaling the value, and places the results in the overlapping 16-bit elements of the destination vector. F1CVTLT scales the values by 2 -UInt(FPMR.LSCALE[3:0]) . F2CVTLT scales the values by 2 -UInt(FPMR.LSCALE2[3:0]) .

The 8-bit floating-point encoding format for F1CVTLT is selected by FPMR.F8S1 . The 8-bit floating-point encoding format for F2CVTLT is selected by FPMR.F8S2 .

This instruction is unpredicated.

It has encodings from 2 classes: F1CVTLT and F2CVTLT

## F1CVTLT

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
F1CVTLT <Zd>.H, <Zn>.B
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_FP8)) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean issrc2 = FALSE;
```

## F2CVTLT

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
F2CVTLT <Zd>.H, <Zn>.B
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) ||
```

```
!IsFeatureImplemented(FEAT_FP8)) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean issrc2 = TRUE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize DIV 2) element = Elem[operand, 2*e + 1, esize DIV 2]; Elem[result, e, esize] = FP8ConvertFP(element, issrc2, FPCR, FPMR); Z[d, VL] = result;
```