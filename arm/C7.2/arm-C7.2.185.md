## C7.2.185 FRINTM (vector)

Floating-point round to integral, toward minus infinity (vector)

This instruction rounds a vector of floating-point values in the SIMD&amp;FP source register to integral floating-point values of the same size using the Round towards Minus Infinity rounding mode, and writes the result to the SIMD&amp;FP destination register.

Azero input gives a zero result with the same sign, an infinite input gives an infinite result with the same sign, and a NaN is propagated as for normal arithmetic.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Half-precision and Single-precision and double-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FRINTM <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_NEGINF;
```

## Single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FRINTM <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_NEGINF;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

For the 'Half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Single-precision and double-precision' variant: is an arrangement specifier, encoded in 'sz:Q':

|   sz |   Q | <T>      |
|------|-----|----------|
|    0 |   0 | 2S       |
|    0 |   1 | 4S       |
|    1 |   0 | RESERVED |
|    1 |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; bits(esize) element; for e = 0 to elements-1 element = Elem[operand, e, esize]; Elem[result, e, esize] = FPRoundInt(element, FPCR, rounding, exact); V[d, datasize] = result;
```

&lt;T&gt;

&lt;Vn&gt;
