## C7.2.251 MVNI

Move inverted immediate (vector)

This instruction places the inverse of an immediate constant into every vector element of the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 16-bit shifted immediate variant

Applies when (cmode ==

```
10x0) MVNI <Vd>.<T>, #<imm8>{, LSL
```

```
#<amount>}
```

## Encoding for the 32-bit shifted immediate variant

```
Applies when (cmode == 0xx0) MVNI <Vd>.<T>, #<imm8>{, LSL
```

```
#<amount>}
```

## Encoding for the 32-bit shifting ones variant

```
Applies when (cmode == 110x) MVNI
```

```
<Vd>.<T>, #<imm8>, MSL #<amount>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer rd = UInt(Rd); constant integer datasize = 64 << UInt(Q); constant bits(64) imm64 = AdvSIMDExpandImm(op, cmode, a:b:c:d:e:f:g:h); constant bits(datasize) imm = Replicate(imm64, datasize DIV 64);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

For the '16-bit shifted immediate' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |

<!-- image -->

## &lt;imm8&gt;

Is an 8-bit immediate encoded in 'a:b:c:d:e:f:g:h'.

## &lt;amount&gt;

For the '16-bit shifted immediate' variant: is the shift amount encoded in 'cmode&lt;1&gt;':

|   cmode<1> |   <amount> |
|------------|------------|
|          0 |          0 |
|          1 |          8 |

defaulting to 0 if LSL is omitted.

For the '32-bit shifted immediate' variant: is the shift amount encoded in 'cmode&lt;2:1&gt;':

|   cmode<2:1> |   <amount> |
|--------------|------------|
|           00 |          0 |
|           01 |          8 |
|           10 |         16 |
|           11 |         24 |

defaulting to 0 if LSL is omitted.

For the '32-bit shifting ones' variant: is the shift amount encoded in 'cmode&lt;0&gt;':

|   cmode<0> |   <amount> |
|------------|------------|
|          0 |          8 |
|          1 |         16 |

|   Q | <T>   |
|-----|-------|
|   1 | 8H    |

For the '32-bit shifted immediate' and '32-bit shifting ones' variants: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 2S    |
|   1 | 4S    |

## Operation

AArch64.CheckFPAdvSIMDEnabled();

V[rd, datasize] = NOT(imm);
