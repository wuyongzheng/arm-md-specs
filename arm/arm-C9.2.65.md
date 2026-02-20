## C9.2.65 FCVT (narrowing, FP32 to FP8)

Multi-vector single-precision convert to 8-bit floating-point

This instruction converts each single-precision element of the four source vectors to 8-bit floating-point while scaling the value by 2 SInt(FPMR.NSCALE) , and places the results in the quarter-width elements of the destination vector. The 8-bit floating-point encoding format is selected by FPMR.F8D .

This instruction is unpredicated.

```
SME2 (FEAT_SME2 && FEAT_FP8)
```

<!-- image -->

## Encoding

```
FCVT <Zd>.B, { <Zn1>.S-<Zn4>.S }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn:'00'); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## Operation

```
CheckFPMREnabled(); CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; bits(VL) result; constant bits(VL) operand1 = Z[n+0, VL]; constant bits(VL) operand2 = Z[n+1, VL]; constant bits(VL) operand3 = Z[n+2, VL]; constant bits(VL) operand4 = Z[n+3, VL]; for e = 0 to elements-1 constant bits(32) element1 = Elem[operand1, e, 32]; constant bits(32) element2 = Elem[operand2, e, 32]; constant bits(32) element3 = Elem[operand3, e, 32]; constant bits(32) element4 = Elem[operand4, e, 32]; Elem[result, 0*elements + e, 8] = FPConvertFP8(element1, FPCR, Elem[result, 1*elements + e, 8] = FPConvertFP8(element2, FPCR,
```

```
FPMR, 8); FPMR, 8);
```

```
Elem[result, 2*elements + e, 8] = FPConvertFP8(element3, FPCR, FPMR, 8); Elem[result, 3*elements + e, 8] = FPConvertFP8(element4, FPCR, FPMR, 8); Z[d, VL] = result;
```