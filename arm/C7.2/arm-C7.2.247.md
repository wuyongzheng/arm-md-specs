## C7.2.247 MOVI

Move immediate (vector)

This instruction places an immediate constant into every vector element of the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 8-bit variant

```
Applies when (op == 0 && cmode == MOVI <Vd>.<T>, #<imm8>{, LSL #0}
```

1110)

## Encoding for the 16-bit shifted immediate variant

```
Applies when (op == 0 && cmode == 10x0)
```

```
MOVI <Vd>.<T>, #<imm8>{, LSL #<amount>}
```

## Encoding for the 32-bit shifted immediate variant

Applies when (op == 0 &amp;&amp; cmode ==

```
MOVI <Vd>.<T>, #<imm8>{, LSL
```

```
0xx0) #<amount>}
```

## Encoding for the 32-bit shifting ones variant

Applies when (op == 0 &amp;&amp; cmode ==

```
110x) MOVI <Vd>.<T>, #<imm8>, MSL #<amount>
```

## Encoding for the 64-bit scalar variant

```
Applies when (Q == 0 && op == 1 && cmode == 1110)
```

```
MOVI <Dd>, #<imm>
```

## Encoding for the 64-bit vector variant

```
Applies when (Q == 1 && op == 1 && cmode == 1110)
```

```
MOVI <Vd>.2D, #<imm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer rd = UInt(Rd); constant integer datasize = 64 << UInt(Q); constant bits(64) imm64 = AdvSIMDExpandImm(op, cmode, a:b:c:d:e:f:g:h); constant bits(datasize) imm = Replicate(imm64, datasize DIV 64);
```

o2

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

For the '8-bit' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

For the '16-bit shifted immediate' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the '32-bit shifted immediate' and '32-bit shifting ones' variants: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 2S    |
|   1 | 4S    |

&lt;T&gt;

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

## &lt;Dd&gt;

defaulting to 0 if LSL is omitted.

For the '32-bit shifting ones' variant: is the shift amount encoded in 'cmode&lt;0&gt;':

|   cmode<0> |   <amount> |
|------------|------------|
|          0 |          8 |
|          1 |         16 |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;imm&gt;

Is a 64-bit immediate 'aaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffffgggggggghhhhhhhh', encoded in 'a:b:c:d:e:f:g:h'.

## Operation

| AArch64.CheckFPAdvSIMDEnabled();   |
|------------------------------------|
| V[rd, datasize] = imm;             |

|   cmode<2:1> |   <amount> |
|--------------|------------|
|           00 |          0 |
|           01 |          8 |
|           10 |         16 |
|           11 |         24 |
