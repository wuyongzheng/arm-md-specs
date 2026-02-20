## C8.2.188 FDOT (2-way, vectors, FP16 to FP32)

Half-precision dot product to single-precision

This instruction computes the fused sum-of-products of a pair of half-precision values held in each 32-bit element of the first source and second source vectors, without intermediate rounding, and then destructively adds the single-precision sum-of-products to the corresponding single-precision element of the destination vector.

This instruction is unpredicated.

## SVE2

(FEAT\_SME2 || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
FDOT <Zda>.S, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(16) elt1_a = Elem[operand1, 2 * e + 0, 16]; constant bits(16) elt1_b = Elem[operand1, 2 * e + 1, 16]; constant bits(16) elt2_a = Elem[operand2, 2 * e + 0, 16]; constant bits(16) elt2_b = Elem[operand2, 2 * e + 1, 16]; bits(32) sum = Elem[operand3, e, 32]; sum = FPDotAdd(sum, elt1_a, elt1_b, elt2_a, elt2_b, FPCR);
```

```
Elem[result, e, 32] = sum; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.