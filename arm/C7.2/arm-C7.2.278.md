## C7.2.278 SCVTF (scalar, fixed-point)

Signed fixed-point convert to floating-point (scalar)

This instruction converts the signed value in the 32-bit or 64-bit general-purpose source register to a floating-point value using the rounding mode that is specified by the FPCR, and writes the result to the SIMD&amp;FP destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the 32-bit to half-precision variant

```
(FEAT_FP16) Applies when (sf == 0 && ftype == 11)
```

```
SCVTF <Hd>, <Wn>, #<fbits>
```

## Encoding for the 64-bit to half-precision variant

```
(FEAT_FP16) Applies when (sf == 1 && ftype == 11)
```

```
SCVTF <Hd>, <Xn>, #<fbits>
```

## Encoding for the 32-bit to single-precision variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 00)
```

```
SCVTF <Sd>, <Wn>, #<fbits>
```

## Encoding for the 64-bit to single-precision variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 00)
```

```
SCVTF <Sd>, <Xn>, #<fbits>
```

## Encoding for the 32-bit to double-precision variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 01)
```

```
SCVTF <Dd>, <Wn>, #<fbits>
```

## Encoding for the 64-bit to double-precision variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 01)
```

```
SCVTF <Dd>, <Xn>, #<fbits>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); if sf == '0' && scale<5> == '0' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer intsize = 32 << UInt(sf); constant integer decode_fltsize = 8 << UInt(ftype EOR '10'); constant integer fracbits = 64 -UInt(scale); constant boolean unsigned = FALSE;
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;fbits&gt;

For the '32-bit to double-precision', '32-bit to half-precision', and '32-bit to single-precision' variants: is the number of bits after the binary point in the fixed-point source, in the range 1 to 32, encoded as 64 minus 'scale'.

For the '64-bit to double-precision', '64-bit to half-precision', and '64-bit to single-precision' variants: is the number of bits after the binary point in the fixed-point source, in the range 1 to 64, encoded as 64 minus 'scale'.

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Xn&gt;

## &lt;Sd&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## Operation

```
AArch64.CheckFPEnabled(); constant boolean merge = IsMerging(FPCR); constant integer fltsize = if merge then 128 else decode_fltsize; bits(fltsize) fltval = if merge then V[d, fltsize] else Zeros(fltsize); constant bits(intsize) intval = X[n, intsize]; constant FPRounding rounding = FPRoundingMode(FPCR); Elem[fltval, 0, decode_fltsize] = FixedToFP(intval, fracbits, unsigned, FPCR, rounding, decode_fltsize); V[d, fltsize] = fltval;
```
