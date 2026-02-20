## C9.2.13 BFCVT (BFloat16 to 8-bit floating-point)

Multi-vector BFloat16 convert to 8-bit floating-point

This instruction converts each BFloat16 element of the two source vectors to 8-bit floating-point while scaling the value by 2 SInt(FPMR.NSCALE) , and places the results in the half-width elements of the destination vector. The 8-bit floating-point encoding format is selected by FPMR.F8D .

This instruction is unpredicated.

## SME2

(FEAT\_SME2 &amp;&amp; FEAT\_FP8)

<!-- image -->

## Encoding

```
BFCVT <Zd>.B, { <Zn1>.H-<Zn2>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) || !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd);
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
CheckFPMREnabled(); CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; bits(VL) result; constant bits(VL) operand1 = Z[n+0, VL]; constant bits(VL) operand2 = Z[n+1, VL]; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, e, 16]; constant bits(16) element2 = Elem[operand2, e, 16]; Elem[result, 0*elements + e, 8] = BFConvertFP8(element1, FPCR, FPMR); Elem[result, 1*elements + e, 8] = BFConvertFP8(element2, FPCR, FPMR); Z[d, VL] = result;
```