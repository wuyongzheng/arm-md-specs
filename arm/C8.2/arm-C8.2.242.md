## C8.2.242 FMMLA (non-widening)

Floating-point matrix multiply-accumulate

This instruction supports single-precision and double-precision data types in a 2x2 matrix contained in segments of 128 or 256 bits, respectively. It multiplies the 2x2 matrix in each segment of the first source vector by the 2x2 matrix in the corresponding segment of the second source vector. The intermediate products are rounded before they are summed, and the intermediate sum is rounded before accumulation into the 2x2 matrix held in the corresponding segment of the addend and destination vector. This is equivalent to performing a 2-way dot product per destination element. This instruction is unpredicated. The single-precision variant is vector length agnostic. The double-precision variant requires that the Effective SVE vector length is at least 256 bits.

ID\_AA64ZFR0\_EL1.F32MM indicates whether the single-precision variant is implemented.

ID\_AA64ZFR0\_EL1.F64MM indicates whether the double-precision variant is implemented.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

It has encodings from 2 classes: 32-bit element and 64-bit element

## 32-bit element

(FEAT\_F32MM)

<!-- image -->

## Encoding

```
FMMLA <Zda>.S, <Zn>.S, <Zm>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F32MM) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## 64-bit element

(FEAT\_F64MM)

<!-- image -->

## Encoding

```
FMMLA <Zda>.D, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_F64MM) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; if VL < esize * 4 then EndOfDecode(Decode_UNDEF); constant integer segments = VL DIV (4 * esize); constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result = Zeros(VL); bits(4*esize) op1, op2; bits(4*esize) res, addend; for s = 0 to segments-1 op1 = Elem[operand1, s, 4*esize]; op2 = Elem[operand2, s, 4*esize]; addend = Elem[operand3, s, 4*esize]; res = FPMatMulAdd(addend, op1, op2, esize, Elem[result, s, 4*esize] = res; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
FPCR);
```