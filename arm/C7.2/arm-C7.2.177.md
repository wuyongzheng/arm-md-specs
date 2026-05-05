## C7.2.177 FRINT64X (vector)

Floating-point round to 64-bit integer, using current rounding mode (vector)

This instruction rounds a vector of floating-point values in the SIMD&amp;FP source register to integral floating-point values that fit into a 64-bit integer size using the rounding mode that is determined by the FPCR, and writes the result to the SIMD&amp;FP destination register.

Azero input returns a zero result with the same sign. When one of the result values is not numerically equal to the corresponding input value, an Inexact exception is raised. When an input is infinite, NaN or out-of-range, the instruction returns for the corresponding result value the most negative integer representable in the destination size, and an Invalid Operation floating-point exception is raised.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

Vector single-precision and double-precision

(FEAT\_FRINTTS)

<!-- image -->

## Encoding

```
FRINT64X <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FRINTTS) then EndOfDecode(Decode_UNDEF); if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer intsize = 64;
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'sz:Q':

|   sz | Q <T>   |
|------|---------|
|    0 | 0 2S    |

&lt;T&gt;

&lt;Vn&gt;

|   sz |   Q | <T>      |
|------|-----|----------|
|    0 |   1 | 4S       |
|    1 |   0 | RESERVED |
|    1 |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; constant FPRounding rounding = FPRoundingMode(FPCR); bits(esize) element; for e = 0 to elements-1 element = Elem[operand, e, esize]; Elem[result, e, esize] = FPRoundIntN(element, FPCR, rounding, intsize); V[d, datasize] = result;
```
