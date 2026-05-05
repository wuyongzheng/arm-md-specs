## C7.2.90 FCVTNS (vector)

Floating-point convert to signed integer, rounding to nearest with ties to even (vector)

This instruction converts a scalar or each element in a vector from a floating-point value to a signed integer value using the Round to Nearest rounding mode, and writes the result to the SIMD&amp;FP destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 4 classes: Scalar half-precision, Scalar single-precision and double-precision, Vector half-precision, and Vector single-precision and double-precision

## Scalar half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FCVTNS <Hd>, <Hn>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = esize; constant integer elements = 1; constant FPRounding rounding = FPDecodeRounding(o1:o2); constant boolean unsigned = FALSE;
```

## Scalar single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTNS <V><d>, <V><n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = esize; constant integer elements = 1; constant FPRounding rounding = FPDecodeRounding(o1:o2); constant boolean unsigned = FALSE;
```

## Vector half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FCVTNS <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant FPRounding rounding = FPDecodeRounding(o1:o2); constant boolean unsigned = FALSE;
```

Vector single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTNS <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant FPRounding rounding = FPDecodeRounding(o1:o2); constant boolean unsigned = FALSE;
```

## Assembler Symbols

&lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is a width specifier, encoded in 'sz':

&lt;Hn&gt;

- &lt;V&gt;
- &lt;d&gt;
- &lt;n&gt;
- &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

- &lt;T&gt; For the 'Vector half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Vector single-precision and double-precision' variant: is an arrangement specifier, encoded in 'sz:Q':

|   sz | <V>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vn&gt;

|   sz |   Q | <T>      |
|------|-----|----------|
|    0 |   0 | 2S       |
|    0 |   1 | 4S       |
|    1 |   0 | RESERVED |
|    1 |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
if elements == 1 && IsFeatureImplemented(FEAT_FPRCVT) then AArch64.CheckFPEnabled(); else AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; constant boolean merge = elements == 1 && IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); constant integer fracbits = 0; bits(esize) element; for e = 0 to elements-1 element = Elem[operand, e, esize]; Elem[result, e, esize] = FPToFixed(element, fracbits, unsigned, FPCR, rounding, esize); V[d, 128] = result;
```
