## C7.2.80 FCVTL, FCVTL2

Floating-point convert to higher precision long (vector)

This instruction reads each element in a vector in the SIMD&amp;FP source register, converts each value to double the precision of the source element using the rounding mode that is determined by the FPCR, and writes each result to the equivalent element of the vector in the SIMD&amp;FP destination register.

Where the operation lengthens a 64-bit vector to a 128-bit vector, the FCVTL2 variant operates on the elements in the top 64 bits of the source register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTL{2} <Vd>.<Ta>, <Vn>.<Tb>
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

&lt;Vd&gt;

## &lt;Ta&gt;

## &lt;Vn&gt;

## &lt;Tb&gt;

Is an arrangement specifier, encoded in 'sz':

|   sz | <Ta>   |
|------|--------|
|    0 | 4S     |
|    1 | 2D     |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'sz:Q':

|   sz |   Q | <Tb>   |
|------|-----|--------|
|    0 |   0 | 4H     |
|    0 |   1 | 8H     |
|    1 |   0 | 2S     |
|    1 |   1 | 4S     |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = Vpart[n, part, datasize]; bits(2*datasize) result; for e = 0 to elements-1 Elem[result, e, 2*esize] = FPConvert(Elem[operand, e, esize], FPCR, 2 * esize); V[d, 2*datasize] = result;
```
