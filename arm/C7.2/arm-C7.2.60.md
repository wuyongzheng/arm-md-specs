## C7.2.60 FCMEQ (register)

Floating-point compare equal (vector)

This instruction compares each floating-point value from the first source SIMD&amp;FP register, with the corresponding floating-point value from the second source SIMD&amp;FP register, and if the comparison is equal sets every bit of the corresponding vector element in the destination SIMD&amp;FP register to one, otherwise sets every bit of the corresponding vector element in the destination SIMD&amp;FP register to zero.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 4 classes: Scalar half-precision, Scalar single-precision and double-precision, Vector half-precision, and Vector single-precision and double-precision

## Scalar half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FCMEQ <Hd>, <Hn>, <Hm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 16; constant integer datasize = esize; constant integer elements = 1;
```

Scalar single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCMEQ <V><d>, <V><n>, <V><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 32 << UInt(sz); constant integer datasize = esize; constant integer elements = 1;
```

## Vector half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FCMEQ <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Vector single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCMEQ <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Hn&gt;

Is the 16-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hm&gt;

Is the 16-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

&lt;V&gt;

- &lt;d&gt;
- &lt;n&gt;

&lt;m&gt;

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

- &lt;T&gt; For the 'Vector half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |

Is a width specifier, encoded in 'sz':

|   sz | <V>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;Vn&gt;

|   Q | <T>   |
|-----|-------|
|   1 | 8H    |

For the 'Vector single-precision and double-precision' variant: is an arrangement specifier, encoded in 'sz:Q':

|   sz |   Q | <T>      |
|------|-----|----------|
|    0 |   0 | 2S       |
|    0 |   1 | 4S       |
|    1 |   0 | RESERVED |
|    1 |   1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(esize) element1; bits(esize) element2; boolean test_passed; constant boolean merge = elements == 1 && IsMerging(FPCR); bits(128) result = if merge then V[m, 128] else Zeros(128); for e = 0 to elements-1 element1 = Elem[operand1, e, esize]; element2 = Elem[operand2, e, esize]; test_passed = FPCompareEQ(element1, element2, FPCR); Elem[result, e, esize] = if test_passed then Ones(esize) else Zeros(esize); V[d, 128] = result;
```
