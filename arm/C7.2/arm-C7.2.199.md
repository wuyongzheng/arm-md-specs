## C7.2.199 FSQRT (scalar)

Floating-point square root (scalar)

This instruction calculates the square root of the value in the SIMD&amp;FP source register and writes the result to the SIMD&amp;FP destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

(FEAT\_FP16) Applies when (ftype == 11)

```
FSQRT <Hd>, <Hn>
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when
```

```
FSQRT <Sd>,
```

```
(ftype == 00) <Sn>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FSQRT <Dd>, <Dn>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(ftype EOR '10');
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

<!-- image -->

## &lt;Sn&gt;

&lt;Dd&gt;

&lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) operand = V[n, esize]; bits(128) result = if IsMerging(FPCR) then V[d, 128] else Zeros(128); Elem[result, 0, esize] = FPSqrt(operand, FPCR); V[d, 128] = result;
```

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
