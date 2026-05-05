## C7.2.414 UCVTF (scalar SIMD&amp;FP)

Unsigned integer convert to floating-point (scalar SIMD&amp;FP)

This instruction converts the unsigned integer value in the SIMD&amp;FP source register to a floating-point value using the rounding mode that is specified by the FPCR, and writes the result to the SIMD&amp;FP destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Integer

(FEAT\_FPRCVT)

<!-- image -->

## Encoding for the 32-bit to half-precision variant

Applies when

UCVTF

&lt;Hd&gt;,

(sf

&lt;Sn&gt;

## Encoding for the 32-bit to double-precision variant

```
Applies when (sf == 0 && ftype == 01)
```

UCVTF

&lt;Dd&gt;,

&lt;Sn&gt;

## Encoding for the 64-bit to half-precision variant

```
Applies when (sf == 1 && ftype == 11)
```

UCVTF

&lt;Hd&gt;,

&lt;Dn&gt;

## Encoding for the 64-bit to single-precision variant

```
Applies when (sf == 1 && ftype == 00)
```

```
UCVTF <Sd>, <Dn>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_FPRCVT) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer intsize = 32 << UInt(sf); constant integer fltsize = 8 << UInt(ftype EOR '10'); constant FPRounding rounding = FPRoundingMode(FPCR);
```

==

0

&amp;&amp;

ftype ==

11)

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Sn&gt;

&lt;Dd&gt;

## &lt;Dn&gt;

&lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## Operation

```
AArch64.CheckFPEnabled(); bits(fltsize) fltval; bits(intsize) intval; constant boolean merge = IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); intval = V[n, intsize]; fltval = FixedToFP(intval, 0, TRUE, FPCR, rounding, fltsize); Elem[result, 0, fltsize] = fltval; V[d, 128] = result;
```
