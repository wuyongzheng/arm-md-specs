## C7.2.132 FMIN (scalar)

Floating-point minimum (scalar)

This instruction compares the first and second source SIMD&amp;FP register values, and writes the smaller of the two floating-point values to the destination SIMD&amp;FP register.

When FPCR.AH is 0, the behavior is as follows:

- Negative zero compares less than positive zero.
- When FPCR.DN is 0, if either value is a NaN, the result is a quiet NaN.
- When FPCR.DN is 1, if either value is a NaN, the result is Default NaN.

When FPCR.AH is 1, the behavior is as follows:

- If both values are zeros, regardless of the sign of either zero, the result is the second value.
- If either value is a NaN, regardless of the value of FPCR.DN, the result is the second value.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype == 11)
```

```
FMIN <Hd>, <Hn>, <Hm>
```

## Encoding for the Single-precision variant

(FEAT\_FP) Applies when (ftype == 00)

```
FMIN <Sd>, <Sn>, <Sm>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FMIN
```

```
<Dd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(ftype EOR '10');
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

Is the 16-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hm&gt;

Is the 16-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;Sd&gt;

&lt;Sn&gt;

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

&lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) operand1 = V[n, esize]; constant bits(esize) operand2 = V[m, esize]; bits(128) result = if IsMerging(FPCR) then V[n, 128] Elem[result, 0, esize] = FPMin(operand1, operand2, FPCR); V[d, 128] = result;
```

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

```
else Zeros(128);
```
