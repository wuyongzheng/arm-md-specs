## C7.2.102 FCVTXN, FCVTXN2

Floating-point convert to lower precision narrow, rounding to odd (vector)

This instruction reads each double-precision element in the source SIMD&amp;FP register, converts each value to single-precision format using the Round to Odd rounding mode, and writes the results to the destination SIMD&amp;FP register.

Note

This instruction uses the Round to Odd rounding mode, which is not defined by the IEEE 754-2008 standard. This rounding mode ensures that if the result of the conversion is inexact, the least significant bit of the mantissa is forced to 1. This rounding mode enables a floating-point value to be converted to a lower precision format via an intermediate precision format while avoiding double rounding errors. For example, a 64-bit floating-point value can be converted to a correctly rounded 16-bit floating-point value by first using this instruction to produce a 32-bit value and then using another instruction with the wanted rounding mode to convert the 32-bit value to the final 16-bit floating-point value.

The Vector variant of FCVTXN writes the half-width results to the lower half of the destination register and clears the upper half to 0. FCVTXN2 writes the half-width results to the upper half of the destination register without affecting the other bits of the register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTXN S<d>, D<n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32; constant integer datasize = esize; constant integer elements = 1; constant integer part = 0;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTXN{2} <Vd>.<Tb>, <Vn>.2D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32; constant integer datasize = 64; constant integer elements = 2; constant integer part = UInt(Q);
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;n&gt;

2

&lt;Vd&gt;

&lt;Tb&gt;

&lt;Vn&gt;

|   Q | <Tb>   |
|-----|--------|
|   0 | 2S     |
|   1 | 4S     |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(2*datasize) operand = V[n, 2*datasize]; constant boolean merge = elements == 1 && IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); for e = 0 to elements-1 Elem[result, e, esize] = FPConvert(Elem[operand, e, 2*esize], FPCR, FPRounding_ODD, esize); if merge then V[d, 128] = result; else Vpart[d, part, datasize] = Elem[result, 0, datasize];
```
