## C7.2.89 FCVTN, FCVTN2 (single-precision to 8-bit floating-point)

Single-precision convert to 8-bit floating-point (vector)

This instruction converts each single-precision element of the two source vectors to 8-bit floating-point while scaling the value by 2 SInt(FPMR.NSCALE) , and places the in-order results in the 8-bit elements of the lower or upper half of the destination vector. FCVTN writes the results to the lower half of the destination vector and clears the upper half. FCVTN2 writes the results to the upper half of the destination vector without affecting the other bits of the vector.

The 8-bit floating-point encoding format is selected by FPMR.F8D.

## Advanced SIMD

(FEAT\_FP8)

<!-- image -->

## Encoding

```
FCVTN{2} <Vd>.<Ta>, <Vn>.4S, <Vm>.4S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FP8) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer part = UInt(Q); constant integer elements = 128 DIV 32;
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

&lt;Ta&gt;

&lt;Vn&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
CheckFPMREnabled(); AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[n, 128]; constant bits(128) operand2 = V[m, 128]; bits(64) result; for e = 0 to elements-1 Elem[result, 0*elements + e, 8] = FPConvertFP8(Elem[operand1, e, 32], FPCR, FPMR, 8); Elem[result, 1*elements + e, 8] = FPConvertFP8(Elem[operand2, e, 32], FPCR, FPMR, 8); Vpart[d, part, 64] = result;
```
