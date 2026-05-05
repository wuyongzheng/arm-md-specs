## C7.2.56 FAMIN

Floating-point absolute minimum

This instruction determines the minimum absolute value from floating-point elements of the first source vector and the corresponding floating-point elements of the second source vector, and places the results in the corresponding elements of the destination vector.

Regardless of the value of FPCR.AH, the behavior is as follows:

- When FPCR.DN is 0, if either element is a NaN, the result is a quiet NaN.
- When FPCR.DN is 1, if either element is a NaN, the result is the Default NaN, with the sign bit set to 0.
- Denormalized inputs and results are never flushed to zero, as if FPCR.{FZ, FZ16, FIZ} are all 0.
- Denormalized inputs never generate an Input Denormal floating-point exception.

It has encodings from 2 classes: Half-precision and Single-precision and double-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FAMINMAX)

<!-- image -->

## Encoding

```
FAMIN <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FAMINMAX) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 16; constant integer datasize = if Q == '1' then 128 else 64; constant integer elements = datasize DIV esize;
```

Single-precision and double-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FAMINMAX)

<!-- image -->

## Encoding

```
FAMIN <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FAMINMAX) then EndOfDecode(Decode_UNDEF); if Q == '0' && size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = if Q == '1' then 128 else 64; constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

For the 'Half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Single-precision and double-precision' variant: is an arrangement specifier, encoded in 'size&lt;0&gt;:Q':

|   size<0> |   Q | <T>      |
|-----------|-----|----------|
|         0 |   0 | 2S       |
|         0 |   1 | 4S       |
|         1 |   0 | RESERVED |
|         1 |   1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; for e = 0 to elements-1 constant bits(esize) op1 = Elem[operand1, e, esize]; constant bits(esize) op2 = Elem[operand2, e, esize]; Elem[result, e, esize] = FPAbsMin(op1, op2, FPCR); V[d, datasize] = result;
```

&lt;T&gt;

&lt;Vn&gt;
