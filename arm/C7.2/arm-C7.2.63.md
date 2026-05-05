## C7.2.63 FCMGE (zero)

Floating-point compare greater than or equal to zero (vector)

This instruction reads each floating-point value in the source SIMD&amp;FP register and if the value is greater than or equal to zero sets every bit of the corresponding vector element in the destination SIMD&amp;FP register to one, otherwise sets every bit of the corresponding vector element in the destination SIMD&amp;FP register to zero.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 4 classes: Scalar half-precision, Scalar single-precision and double-precision, Vector half-precision, and Vector single-precision and double-precision

## Scalar half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FCMGE <Hd>, <Hn>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = esize; constant integer elements = 1;
```

Scalar single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCMGE <V><d>, <V><n>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = esize; constant integer elements = 1;
```

## Vector half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FCMGE <Vd>.<T>, <Vn>.<T>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Vector single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCMGE <Vd>.<T>, <Vn>.<T>, #0.0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is a width specifier, encoded in 'sz':

&lt;Hn&gt;

&lt;V&gt;

- &lt;d&gt;

&lt;n&gt;

- &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

- &lt;T&gt; For the 'Vector half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Vector single-precision and double-precision' variant: is an arrangement specifier, encoded in 'sz:Q':

|   sz |   Q | <T>      |
|------|-----|----------|
|    0 |   0 | 2S       |
|    0 |   1 | 4S       |
|    1 |   0 | RESERVED |
|    1 |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vn&gt;

|   sz | <V>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; constant bits(esize) zero = FPZero('0', esize); bits(esize) element; boolean test_passed; for e = 0 to elements-1 element = Elem[operand, e, esize]; test_passed = FPCompareGE(element, zero, FPCR); Elem[result, e, esize] = if test_passed then Ones(esize) V[d, datasize] = result;
```

```
else Zeros(esize);
```
