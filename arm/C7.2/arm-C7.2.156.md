## C7.2.156 FMOV (register)

Floating-point move register without conversion

This instruction copies the floating-point value in the SIMD&amp;FP source register to the SIMD&amp;FP destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype == 11)
```

```
FMOV <Hd>, <Hn>
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when (ftype == 00)
```

```
FMOV <Sd>, <Sn>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FMOV <Dd>, <Dn>
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

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hn&gt;

&lt;Sd&gt;

&lt;Sn&gt;

&lt;Dd&gt;

&lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) operand = V[n, esize]; bits(128) result = Zeros(128); Elem[result, 0, esize] = operand; V[d, 128] = result;
```

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
