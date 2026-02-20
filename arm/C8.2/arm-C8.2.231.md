## C8.2.231 FMLALT (vectors, FP16 to FP32)

Half-precision multiply-add to single-precision (top)

This instruction widens the odd-numbered half-precision elements in the first source vector and the corresponding elements in the second source vector to single-precision format and then destructively multiplies and adds these values without intermediate rounding to the single-precision elements of the destination vector that overlap with the corresponding half-precision elements in the source vectors. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
FMLALT <Zda>.S, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean op1_neg = FALSE;
```

## Assembler Symbols

&lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) op1 = Z[n, VL]; constant bits(VL) op2 = Z[m, VL]; constant bits(VL) op3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize DIV 2) elem1 = (if op1_neg then FPNeg(Elem[op1, 2*e + 1, esize DIV 2], FPCR) else Elem[op1, 2*e + 1, esize DIV 2]); constant bits(esize DIV 2) elem2 = Elem[op2, 2*e + 1, esize DIV 2]; constant bits(esize) elem3 = Elem[op3, e, esize]; Elem[result, e, esize] = FPMulAddH(elem3, elem1, elem2, FPCR);
```

Z[da, VL] = result;

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.