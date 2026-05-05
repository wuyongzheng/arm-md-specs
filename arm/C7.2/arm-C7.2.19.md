## C7.2.19 BFMLALB, BFMLALT (vector)

BFloat16 multiply-add to single-precision (vector)

This instruction widens the even-numbered (bottom) or odd-numbered (top) 16-bit elements in the first and second source vectors from Bfloat16 to single-precision format. The instruction then multiplies and adds these values without intermediate rounding to the single-precision elements of the destination vector that overlap with the corresponding BFloat16 elements in the source vectors.

ID\_AA64ISAR1\_EL1.BF16 indicates whether this instruction is supported.

## Vector

(FEAT\_BF16)

<!-- image -->

## Encoding

```
BFMLAL<bt> <Vd>.4S, <Vn>.8H, <Vm>.8H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_BF16) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q);
```

## Assembler Symbols

&lt;bt&gt;

Is the bottom or top element specifier, encoded in 'Q':

|   Q | <bt>   |
|-----|--------|
|   0 | B      |
|   1 | T      |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vd&gt;

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

```
EndOfDecode(Decode_UNDEF);
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[n, 128]; constant bits(128) operand2 = V[m, 128]; constant bits(128) operand3 = V[d, 128]; bits(128) result; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, 2 * e + sel, 16]; constant bits(16) element2 = Elem[operand2, 2 * e + sel, 16]; constant bits(32) addend = Elem[operand3, e, 32]; Elem[result, e, 32] = BFMulAddH(addend, element1, element2, FPCR); V[d, 128] = result;
```
