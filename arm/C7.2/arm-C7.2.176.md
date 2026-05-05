## C7.2.176 FRINT32Z (scalar)

Floating-point round to 32-bit integer toward zero (scalar)

This instruction rounds a floating-point value in the SIMD&amp;FP source register to an integral floating-point value that fits into a 32-bit integer size using the Round towards Zero rounding mode, and writes the result to the SIMD&amp;FP destination register.

Azero input returns a zero result with the same sign. When the result value is not numerically equal to the input value, an Inexact exception is raised. When the input is infinite, NaN or out-of-range, the instruction returns the most negative integer representable in the destination size, and an Invalid Operation floating-point exception is raised.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Floating-point

(FEAT\_FRINTTS)

<!-- image -->

## Encoding for the Single-precision variant

```
Applies when (ftype == 00) FRINT32Z <Sd>, <Sn>
```

## Encoding for the Double-precision variant

```
Applies when
```

```
(ftype == FRINT32Z <Dd>, <Dn>
```

```
01)
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FRINTTS) then EndOfDecode(Decode_UNDEF);
```

```
if ftype IN {'1x'} then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(ftype<0>); constant integer intsize = 32; constant FPRounding rounding = FPRounding_ZERO;
```

## Assembler Symbols

&lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

<!-- image -->

## &lt;Dd&gt;

&lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) operand = V[n, esize]; bits(128) result = if IsMerging(FPCR) then V[d, 128] else Zeros(128); Elem[result, 0, esize] = FPRoundIntN(operand, FPCR, rounding, intsize); V[d, 128] = result;
```

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
