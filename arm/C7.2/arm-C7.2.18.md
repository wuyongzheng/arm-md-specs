## C7.2.18 BFMLALB, BFMLALT (by element)

BFloat16 multiply-add to single-precision (by element)

This instruction widens the even-numbered (bottom) or odd-numbered (top) 16-bit elements in the first source vector, and the indexed element in the second source vector from Bfloat16 to single-precision format. The instruction then multiplies and adds these values without intermediate rounding to single-precision elements of the destination vector that overlap with the corresponding BFloat16 elements in the first source vector.

ID\_AA64ISAR1\_EL1.BF16 indicates whether this instruction is supported.

## Vector

(FEAT\_BF16)

<!-- image -->

## Encoding

```
BFMLAL<bt> <Vd>.4S, <Vn>.8H, <Vm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_BF16) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt('0':Rm); constant integer d = UInt(Rd); constant integer index = UInt(H:L:M); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q);
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

Is the name of the second SIMD&amp;FP source register, in the range V0 to V15, encoded in the 'Rm' field.

## &lt;index&gt;

Is the element index, in the range 0 to 7, encoded in the 'H:L:M' fields.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(128) result; constant bits(128) operand1 = V[n, 128]; constant bits(128) operand2 = V[m, 128]; constant bits(128) operand3 = V[d, 128]; constant bits(16) element2 = Elem[operand2, index, 16]; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, 2 * e + sel, 16]; constant bits(32) addend = Elem[operand3, e, 32]; Elem[result, e, 32] = BFMulAddH(addend, element1, element2, FPCR); V[d, 128] = result;
```
