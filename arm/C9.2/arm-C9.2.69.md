## C9.2.69 FCVTN (FP32 to FP16)

Multi-vector single-precision convert to interleaved half-precision

This instruction converts each element of the two source vectors from single-precision to half-precision floating-point, and places the two-way interleaved results in the half-width destination elements.

This instruction follows SME2 floating-point numerical behaviors corresponding to instructions that place their results in one or more SVE Z vectors.

This instruction is unpredicated.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
FCVTN <Zd>.H, { <Zn1>.S-<Zn2>.S }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd);
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
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; bits(VL) result; constant bits(VL) operand1 = Z[n+0, VL]; constant bits(VL) operand2 = Z[n+1, VL]; for e = 0 to elements-1 constant bits(32) element1 = Elem[operand1, e, 32]; constant bits(32) element2 = Elem[operand2, e, 32]; constant bits(16) res1 = FPConvertSVE(element1, FPCR, 16); constant bits(16) res2 = FPConvertSVE(element2, FPCR, 16); Elem[result, 2*e + 0, 16] = res1; Elem[result, 2*e + 1, 16] = res2; Z[d, VL] = result;
```

```
EndOfDecode(Decode_UNDEF);
```