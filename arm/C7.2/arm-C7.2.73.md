## C7.2.73 FCVT

Floating-point convert precision (scalar)

This instruction converts the floating-point value in the SIMD&amp;FP source register to the precision for the destination register data type using the rounding mode that is determined by the FPCR and writes the result to the SIMD&amp;FP destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Floating-point

(FEAT\_FP)

<!-- image -->

## Encoding for the Half-precision to single-precision variant

```
Applies when (ftype == 11 && opc
```

```
== 00) FCVT <Sd>, <Hn>
```

## Encoding for the Half-precision to double-precision variant

```
Applies when (ftype == 11 && opc
```

```
== 01) FCVT <Dd>, <Hn>
```

## Encoding for the Single-precision to half-precision variant

```
Applies when (ftype == 00 && opc == 11)
```

```
FCVT <Hd>, <Sn>
```

## Encoding for the Single-precision to double-precision variant

```
Applies when (ftype == 00 && opc
```

```
== 01) FCVT <Dd>, <Sn>
```

## Encoding for the Double-precision to half-precision variant

```
Applies when (ftype == 01 && opc == 11)
```

FCVT

&lt;Hd&gt;, &lt;Dn&gt;

## Encoding for the Double-precision to single-precision variant

Applies when (ftype == 01 &amp;&amp; opc == 00)

FCVT

&lt;Sd&gt;, &lt;Dn&gt;

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == opc || ftype == '10' || opc == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer srcsize = 8 << UInt(ftype EOR '10'); constant integer dstsize = 8 << UInt(opc EOR '10');
```

## Assembler Symbols

&lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hn&gt;

## &lt;Dd&gt;

## &lt;Hd&gt;

&lt;Sn&gt;

## &lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(srcsize) operand = V[n, srcsize]; bits(128) result = if IsMerging(FPCR) then V[d, 128] else Zeros(128); Elem[result, 0, dstsize] = FPConvert(operand, FPCR, dstsize); V[d, 128] = result;
```
