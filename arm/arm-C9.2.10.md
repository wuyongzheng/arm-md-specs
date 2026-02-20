## C9.2.10 BF1CVTL, BF2CVTL

Multi-vector 8-bit floating-point convert to deinterleaved BFloat16

This instruction converts each 8-bit floating-point element of the source vector to BFloat16 while downscaling the value, and places the two-way deinterleaved results in the corresponding 16-bit elements of the destination vectors. BF1CVTL scales the values by 2 -UInt(FPMR.LSCALE[5:0]) . BF2CVTL scales the values by 2 -UInt(FPMR.LSCALE2[5:0]) . The 8-bit floating-point encoding format for BF1CVTL is selected by FPMR.F8S1 . The 8-bit floating-point encoding format for BF2CVTL is selected by FPMR.F8S2 .

This instruction is unpredicated.

It has encodings from 2 classes: BF1CVTL and BF2CVTL

## BF1CVTL

(FEAT\_SME2 &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BF1CVTL { <Zd1>.H-<Zd2>.H }, <Zn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Zd: '0'); constant boolean issrc2 = FALSE;
```

## BF2CVTL

(FEAT\_SME2 &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BF2CVTL { <Zd1>.H-<Zd2>.H }, <Zn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Zd: '0'); constant boolean issrc2 = TRUE;
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckFPMREnabled(); CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer pairs = VL DIV 16; constant bits(VL) operand = Z[n, VL]; bits(VL) result1; bits(VL) result2; for p = 0 to pairs-1 constant bits(8) element1 = Elem[operand, 2*p + 0, 8]; constant bits(8) element2 = Elem[operand, 2*p + 1, 8]; Elem[result1, p, 16] = FP8ConvertBF(element1, issrc2, FPCR, FPMR); Elem[result2, p, 16] = FP8ConvertBF(element2, issrc2, FPCR, FPMR); Z[d+0, VL] = result1; Z[d+1, VL] = result2;
```