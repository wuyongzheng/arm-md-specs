## C8.2.241 FMMLA (widening, FP16 to FP32)

Half-precision matrix multiply-accumulate to single-precision

This instruction performs two fused sums-of-products within each two pairs of adjacent half-precision elements while multiplying the 2 × 4 matrix of half-precision values held in each 128-bit segment of the first source vector by the 4 × 2 matrix of half-precision values in the corresponding segment of the second source vector. The intermediate sums-of-products are rounded before they are summed, and their intermediate sum is rounded before accumulation into the 2 × 2 single-precision matrix in the corresponding segment of the destination vector. This is equivalent to performing a 4-way dot product per destination element.

This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE\_F16F32MM)

<!-- image -->

## Encoding

```
FMMLA <Zda>.S, <Zn>.H,
```

```
<Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_F16F32MM) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
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
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for s = 0 to segments-1 constant bits(128) op1 = Elem[operand1, constant bits(128) op2 = Elem[operand2,
```

```
s, 128]; s, 128];
```

```
constant bits(128) addend = Elem[operand3, s, 128]; Elem[result, s, 128] = FPMatMulAddH(addend, op1, op2, FPCR); Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.