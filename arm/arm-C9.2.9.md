## C9.2.9 BF1CVT, BF2CVT

Multi-vector 8-bit floating-point convert to BFloat16

This instruction converts each 8-bit floating-point element of the source vector to BFloat16 while downscaling the value, and places the results in the corresponding 16-bit elements of the destination vectors. BF1CVT scales the values by 2 -UInt(FPMR.LSCALE[5:0]) . BF2CVT scales the values by 2 -UInt(FPMR.LSCALE2[5:0]) . The 8-bit floating-point encoding format for BF1CVT is selected by FPMR.F8S1 . The 8-bit floating-point encoding format for BF2CVT is selected by FPMR.F8S2 .

This instruction is unpredicated.

It has encodings from 2 classes: BF1CVT and BF2CVT

## BF1CVT

(FEAT\_SME2 &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BF1CVT { <Zd1>.H-<Zd2>.H }, <Zn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Zd: '0'); constant boolean issrc2 = FALSE;
```

## BF2CVT

(FEAT\_SME2 &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BF2CVT { <Zd1>.H-<Zd2>.H }, <Zn>.B
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
CheckFPMREnabled(); CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 8; constant bits(VL) operand = Z[n, VL]; bits(2*VL) result; for e = 0 to elements-1 constant bits(8) element = Elem[operand, e, 8]; Elem[result, e, 16] = FP8ConvertBF(element, issrc2, FPCR, FPMR); Z[d+0, VL] = result<VL-1:0>; Z[d+1, VL] = result<2*VL-1:VL>;
```