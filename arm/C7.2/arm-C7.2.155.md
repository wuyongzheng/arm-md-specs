## C7.2.155 FMOV (vector, immediate)

Floating-point move immediate (vector)

This instruction copies an immediate floating-point constant into every element of the SIMD&amp;FP destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Half-precision and Single-precision and double-precision

## Half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FMOV <Vd>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer rd = UInt(Rd); constant integer datasize = 64 << UInt(Q); constant bits(8) imm8 = a:b:c:d:e:f:g:h; constant bits(16) imm16 = imm8<7>:NOT(imm8<6>):Replicate(imm8<6>, 2):imm8<5:0>:Zeros(6); constant bits(datasize) imm = Replicate(imm16, datasize DIV 16);
```

## Single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the Single-precision variant

```
Applies when (op == 0) FMOV <Vd>.<T>, #<imm>
```

## Encoding for the Double-precision variant

```
Applies when
```

```
(Q == 1 && op == 1) FMOV <Vd>.2D, #<imm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if cmode:op == '11111' then // FMOV Dn,#imm is in main FP instruction set if Q == '0' then EndOfDecode(Decode_UNDEF); constant integer rd = UInt(Rd); constant integer datasize = 64 << UInt(Q); constant bits(64) imm64 = AdvSIMDExpandImm(op, cmode, a:b:c:d:e:f:g:h); constant bits(datasize) imm = Replicate(imm64, datasize DIV 64);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

For the 'Half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Single-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 2S    |
|   1 | 4S    |

<!-- image -->

## &lt;imm&gt;

Is a signed floating-point constant with 3-bit exponent and normalized 4 bits of precision, encoded in 'a:b:c:d:e:f:g:h'. For details of the range of constants available and the encoding of &lt;imm&gt; , see Modified immediate constants in A64 floating-point instructions.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); V[rd, datasize] = imm;
```
