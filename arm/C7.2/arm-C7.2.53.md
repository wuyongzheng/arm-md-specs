## C7.2.53 FADDP (scalar)

Floating-point add pair of elements (scalar)

This instruction adds two floating-point vector elements in the source SIMD&amp;FP register and writes the scalar result into the destination SIMD&amp;FP register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Half-precision and Single-precision and double-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FADDP H<d>, <Vn>.2H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); if sz == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 16; constant integer datasize = 32;
```

## Single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FADDP <V><d>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 32 << UInt(sz); constant integer datasize = esize * 2;
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the destination width specifier, encoded in 'sz':

|   sz | <V>   |
|------|-------|
|    0 | S     |
|    1 | D     |

&lt;Vn&gt;

&lt;V&gt;

&lt;T&gt;

Is the source arrangement specifier, encoded in 'sz':

|   sz | <T>   |
|------|-------|
|    0 | 2S    |
|    1 | 2D    |

```
esize]; esize];
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; constant bits(esize) element1 = Elem[operand, 0, constant bits(esize) element2 = Elem[operand, 1, V[d, esize] = FPAdd(element1, element2, FPCR);
```
