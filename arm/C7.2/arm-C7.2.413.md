## C7.2.413 UCVTF (scalar, integer)

Unsigned integer convert to floating-point (scalar)

This instruction converts the unsigned integer value in the general-purpose source register to a floating-point value using the rounding mode that is specified by the FPCR, and writes the result to the SIMD&amp;FP destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the 32-bit to half-precision variant

```
(FEAT_FP16) Applies when (sf == 0 && ftype == 11)
```

```
UCVTF <Hd>, <Wn>
```

## Encoding for the 32-bit to single-precision variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 00)
```

```
UCVTF <Sd>, <Wn>
```

## Encoding for the 32-bit to double-precision variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 01)
```

UCVTF

&lt;Dd&gt;,

&lt;Wn&gt;

## Encoding for the 64-bit to half-precision variant

```
(FEAT_FP16) Applies when (sf == 1 && ftype == 11)
```

```
UCVTF <Hd>, <Xn>
```

## Encoding for the 64-bit to single-precision variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 00)
```

```
UCVTF <Sd>, <Xn>
```

## Encoding for the 64-bit to double-precision variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 01)
```

```
UCVTF <Dd>, <Xn>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer intsize = 32 << UInt(sf); constant integer decode_fltsize = 8 << UInt(ftype EOR '10'); constant boolean unsigned = TRUE;
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

&lt;Sd&gt;

&lt;Dd&gt;

&lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant integer fltsize = if IsMerging(FPCR) then 128 else decode_fltsize; constant bits(intsize) intval = X[n, intsize]; constant FPRounding rounding = FPRoundingMode(FPCR); constant integer fracbits = 0; bits(fltsize) fltval = if IsMerging(FPCR) then V[d, fltsize] else Elem[fltval, 0, decode_fltsize] = FixedToFP(intval, fracbits, unsigned, FPCR, rounding, decode_fltsize); V[d, fltsize] = fltval;
```

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

```
Zeros(fltsize);
```
