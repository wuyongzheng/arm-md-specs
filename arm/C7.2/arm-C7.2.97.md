## C7.2.97 FCVTPS (scalar)

Floating-point convert to signed integer, rounding toward plus infinity (scalar)

This instruction converts the floating-point value in the SIMD&amp;FP source register to a 32-bit or 64-bit signed integer using the Round towards Plus Infinity rounding mode, and writes the result to the general-purpose destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision to 32-bit variant

```
(FEAT_FP16) Applies when (sf == 0 && ftype == 11)
```

```
FCVTPS <Wd>, <Hn>
```

## Encoding for the Half-precision to 64-bit variant

```
(FEAT_FP16) Applies when (sf == 1 && ftype == 11)
```

```
FCVTPS <Xd>, <Hn>
```

## Encoding for the Single-precision to 32-bit variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 00)
```

```
FCVTPS <Wd>, <Sn>
```

## Encoding for the Single-precision to 64-bit variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 00)
```

```
FCVTPS <Xd>, <Sn>
```

## Encoding for the Double-precision to 32-bit variant

```
(FEAT_FP) Applies when (sf == 0 && ftype == 01)
```

```
FCVTPS <Wd>, <Dn>
```

## Encoding for the Double-precision to 64-bit variant

```
(FEAT_FP) Applies when (sf == 1 && ftype == 01)
```

```
FCVTPS <Xd>, <Dn>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer intsize = 32 << UInt(sf); constant integer fltsize = 8 << UInt(ftype EOR '10'); constant FPRounding rounding = FPRounding_POSINF; constant boolean unsigned = FALSE;
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

&lt;Xd&gt;

&lt;Sn&gt;

## &lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(fltsize) fltval = V[n, fltsize]; constant integer fracbits = 0; X[d, intsize] =
```

```
FPToFixed(fltval, fracbits, unsigned, FPCR, rounding, intsize);
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.
