## C7.2.188 FRINTN (scalar)

Floating-point round to integral, to nearest with ties to even (scalar)

This instruction rounds a floating-point value in the SIMD&amp;FP source register to an integral floating-point value of the same size using the Round to Nearest rounding mode, and writes the result to the SIMD&amp;FP destination register.

Azero input gives a zero result with the same sign, an infinite input gives an infinite result with the same sign, and a NaN is propagated as for normal arithmetic.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype == 11)
```

```
FRINTN <Hd>, <Hn>
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when (ftype == 00)
```

```
FRINTN <Sd>, <Sn>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FRINTN <Dd>, <Dn>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(ftype EOR '10'); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_TIEEVEN;
```

## Assembler Symbols

&lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Hn&gt;

## &lt;Sd&gt;

&lt;Sn&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) operand = V[n, esize]; bits(128) result = if IsMerging(FPCR) then V[d, 128] else Zeros(128); Elem[result, 0, esize] = FPRoundInt(operand, FPCR, rounding, exact); V[d, 128] = result;
```

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
