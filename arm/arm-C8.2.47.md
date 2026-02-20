## C8.2.47 BFCVTN

BFloat16 convert to interleaved 8-bit floating-point

This instruction converts each BFloat16 element of the pair of source vectors to 8-bit floating-point while scaling the value by 2 SInt(FPMR.NSCALE) , and places the two-way interleaved results in the corresponding 8-bit elements of the destination vector. The 8-bit floating-point encoding format is selected by FPMR.F8D .

This instruction is unpredicated.

## SVE2

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BFCVTN <Zd>.B, { <Zn1>.H-<Zn2>.H
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_FP8)) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## Operation

```
CheckFPMREnabled(); if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; bits(VL) result; constant bits(VL) operand1 = Z[n+0, VL]; constant bits(VL) operand2 = Z[n+1, VL]; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, e, 16]; constant bits(16) element2 = Elem[operand2, e, 16]; Elem[result, 2*e + 0, 8] = BFConvertFP8(element1, FPCR, FPMR); Elem[result, 2*e + 1, 8] = BFConvertFP8(element2, FPCR, FPMR); Z[d, VL] = result;
```

```
}
```