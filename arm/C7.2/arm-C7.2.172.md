## C7.2.172 FRECPX

Floating-point reciprocal exponent (scalar)

This instruction finds an approximate reciprocal exponent for the source SIMD&amp;FP register and writes the result to the destination SIMD&amp;FP register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Half-precision and Single-precision and double-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FRECPX <Hd>, <Hn>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16;
```

Single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FRECPX <V><d>, <V><n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz);
```

## Assembler Symbols

&lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is a width specifier, encoded in 'sz':

## &lt;Hn&gt;

&lt;V&gt;

&lt;d&gt;

&lt;n&gt;

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) operand = V[n, esize]; constant boolean merge = IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); Elem[result, 0, esize] = FPRecpX(operand, FPCR); V[d, 128] = result;
```

|   sz | <V>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
