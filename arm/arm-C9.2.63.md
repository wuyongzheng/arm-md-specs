## C9.2.63 FCVT (widening)

Multi-vector half-precision convert to single-precision

This instruction converts each element of the source vector from half-precision to single-precision floating-point, and places the results in the double-width destination elements of the destination vectors.

This instruction follows SME2 floating-point numerical behaviors corresponding to instructions that place their results in one or more SVE Z vectors.

This instruction is unpredicated.

ID\_AA64SMFR0\_EL1.F16F16 indicates whether this instruction is implemented.

## SME2

(FEAT\_SME\_F16F16)

<!-- image -->

## Encoding

```
FCVT { <Zd1>.S-<Zd2>.S }, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F16F16) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer d = UInt(Zd:'0');
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant bits(VL) operand = Z[n, VL]; bits(2*VL) result; for e = 0 to elements-1 constant bits(16) element = Elem[operand, e, 16]; constant bits(32) res = FPConvertSVE(element, FPCR, 32); Elem[result, e, 32] = res; Z[d+0, VL] = result<VL-1:0>; Z[d+1, VL] = result<2*VL-1:VL>;
```

L