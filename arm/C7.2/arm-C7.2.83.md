## C7.2.83 FCVTMS (scalar SIMD&amp;FP)

Floating-point convert to signed integer, rounding toward minus infinity (scalar SIMD&amp;FP)

This instruction converts the floating-point value in the SIMD&amp;FP source register to a 32-bit or 64-bit signed integer using the Round toward Minus Infinity rounding mode, and writes the result to the SIMD&amp;FP destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Floating-point

(FEAT\_FPRCVT)

<!-- image -->

## Encoding for the Half-precision to 32-bit variant

Applies when

FCVTMS

(sf

&lt;Sd&gt;,

==

&lt;Hn&gt;

## Encoding for the Half-precision to 64-bit variant

```
Applies when (sf == 1 && ftype ==
```

```
11) FCVTMS <Dd>, <Hn>
```

## Encoding for the Single-precision to 64-bit variant

```
Applies when (sf == 1 && ftype ==
```

```
00) FCVTMS <Dd>, <Sn>
```

## Encoding for the Double-precision to 32-bit variant

```
Applies when (sf == 0 && ftype == 01)
```

```
FCVTMS <Sd>, <Dn>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_FPRCVT) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer intsize = 32 << UInt(sf); constant integer fltsize = 8 << UInt(ftype EOR '10');
```

0

&amp;&amp;

ftype ==

11)

## Assembler Symbols

&lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hn&gt;

&lt;Dd&gt;

&lt;Sn&gt;

## &lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); FPRounding_NEGINF, intsize);
```

```
bits(fltsize) fltval; bits(intsize) intval; constant boolean merge = IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); fltval = V[n, fltsize]; intval = FPToFixed(fltval, 0, FALSE, FPCR, Elem[result, 0, intsize] = intval; V[d, 128] = result;
```
