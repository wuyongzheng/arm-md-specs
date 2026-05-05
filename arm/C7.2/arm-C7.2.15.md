## C7.2.15 BFCVTN, BFCVTN2

Single-precision convert to BFloat16 (vector)

This instruction reads each single-precision element in the SIMD&amp;FP source vector, converts each value to BFloat16 format, and writes the results in the lower or upper half of the SIMD&amp;FP destination vector. The result elements are half the width of the source elements.

The BFCVTN instruction writes the half-width results to the lower half of the destination vector and clears the upper half to zero. The BFCVTN2 instruction writes the results to the upper half of the destination vector without affecting the other bits in the register.

## Vector single-precision to BFloat16

(FEAT\_BF16)

<!-- image -->

## Encoding

```
BFCVTN{2} <Vd>.<Ta>, <Vn>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_BF16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer part = UInt(Q); constant integer elements = 64 DIV 16;
```

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Vd&gt;

<!-- image -->

&lt;Vn&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 4H     |
|   1 | 8H     |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand = V[n, 128]; bits(64) result; for e = 0 to elements-1 Elem[result, e, 16] = FPConvertBF(Elem[operand, e, 32], FPCR); Vpart[d, part, 64] = result;
```
