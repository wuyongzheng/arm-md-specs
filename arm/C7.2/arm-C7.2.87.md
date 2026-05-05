## C7.2.87 FCVTN, FCVTN2 (double to single-precision, single to half-precision)

Floating-point convert to lower precision narrow (vector)

This instruction reads each vector element in the SIMD&amp;FP source register, converts each result to half the precision of the source element, writes the final result to a vector, and writes the vector to the lower or upper half of the destination SIMD&amp;FP register. The destination vector elements are half as long as the source vector elements. The rounding mode is determined by the FPCR.

FCVTN writes the vector to the lower half of the destination register and clears the upper half. FCVTN2 writes the vector to the upper half of the destination register without affecting the other bits of the register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTN{2} <Vd>.<Tb>, <Vn>.<Ta>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16 << UInt(sz); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

<!-- image -->

&lt;Tb&gt;

## &lt;Vn&gt;

&lt;Ta&gt;

Is an arrangement specifier, encoded in 'sz:Q':

|   sz |   Q | <Tb>   |
|------|-----|--------|
|    0 |   0 | 4H     |
|    0 |   1 | 8H     |
|    1 |   0 | 2S     |
|    1 |   1 | 4S     |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'sz':

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(2*datasize) operand = V[n, 2*datasize]; bits(datasize) result; for e = 0 to elements-1 Elem[result, e, esize] = FPConvert(Elem[operand, e, 2*esize], FPCR, esize); Vpart[d, part, datasize] = result;
```

|   sz | <Ta>   |
|------|--------|
|    0 | 4S     |
|    1 | 2D     |
