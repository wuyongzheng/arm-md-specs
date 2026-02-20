## C9.2.67 FCVTL

Multi-vector half-precision convert to deinterleaved single-precision

This instruction converts each element of the source vector from half-precision to single-precision floating-point, and places the two-way deinterleaved results in the double-width destination elements of the destination vectors.

This instruction follows SME2 floating-point numerical behaviors corresponding to instructions that place their results in one or more SVE Z vectors.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.F16F16 indicates whether this instruction is implemented.

## SME2

(FEAT\_SME\_F16F16)

<!-- image -->

## Encoding

```
FCVTL { <Zd1>.S-<Zd2>.S }, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Zd:'0');
```

## Assembler Symbols

&lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer pairs = VL DIV 32; constant bits(VL) operand = Z[n, VL]; bits(VL) result0; bits(VL) result1; for p = 0 to pairs-1 constant bits(16) element1 = Elem[operand, 2*p+0, 16]; constant bits(16) element2 = Elem[operand, 2*p+1, 16]; constant bits(32) res1 = FPConvertSVE(element1, FPCR, 32); constant bits(32) res2 = FPConvertSVE(element2, FPCR, 32); Elem[result0, p, 32] = res1;
```

L

```
Elem[result1, p, 32] = res2; Z[d+0, VL] = result0; Z[d+1, VL] = result1;
```