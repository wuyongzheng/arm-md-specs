## C8.2.69 BFMUL (vectors, unpredicated)

BFloat16 multiply (unpredicated)

This instruction multiplies all BFloat16 elements of the second source vector to corresponding elements of the first source vector and places the results in the corresponding elements of the destination vector.

This instruction follows SVE2 non-widening BFloat16 numerical behaviors.

This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.B16B16 indicates whether this instruction is implemented.

## SVE2

(FEAT\_SVE\_B16B16)

<!-- image -->

## Encoding

```
BFMUL <Zd>.H, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_B16B16) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 16; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, e, 16]; constant bits(16) element2 = Elem[operand2, e, 16]; Elem[result, e, 16] = BFMul(element1, element2, FPCR); Z[d, VL] = result;
```