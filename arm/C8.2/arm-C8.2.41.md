## C8.2.41 BF1CVT, BF2CVT

8-bit floating-point convert to BFloat16

This instruction converts each even-numbered 8-bit floating-point element of the source vector to BFloat16 while downscaling the value, and places the results in the overlapping 16-bit elements of the destination vector. BF1CVT scales the values by 2 -UInt(FPMR.LSCALE[5:0]) . BF2CVT scales the values by 2 -UInt(FPMR.LSCALE2[5:0]) .

The 8-bit floating-point encoding format for BF1CVT is selected by FPMR.F8S1 . The 8-bit floating-point encoding format for BF2CVT is selected by FPMR.F8S2 .

This instruction is unpredicated.

It has encodings from 2 classes: BF1CVT and BF2CVT

## BF1CVT

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BF1CVT <Zd>.H, <Zn>.B
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_FP8)) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 8; constant integer d_esize = 16; constant boolean issrc2 = FALSE;
```

## BF2CVT

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BF2CVT <Zd>.H, <Zn>.B
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_FP8)) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 8; constant integer d_esize = 16; constant boolean issrc2 = TRUE;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element = Elem[operand, e, esize]; constant bits(d_esize) res = FP8ConvertBF(element<s_esize-1:0>, issrc2, FPCR, FPMR); Elem[result, e, esize] = ZeroExtend(res, esize); Z[d, VL] = result;
```