## C7.2.21 BIC (vector, immediate)

Bitwise bit clear (vector, immediate)

This instruction reads each vector element from the destination SIMD&amp;FP register, performs a bitwise AND between each result and the complement of an immediate constant, places the result into a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Shifted immediate

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 16-bit variant

Applies when (cmode == 10x1) BIC &lt;Vd&gt;.&lt;T&gt;, #&lt;imm8&gt;{, LSL #&lt;amount&gt;}

## Encoding for the 32-bit variant

Applies when (cmode ==

```
0xx1) BIC <Vd>.<T>, #<imm8>{, LSL #<amount>}
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer rd = UInt(Rd); constant integer datasize = 64 << UInt(Q); constant bits(64) imm64 = AdvSIMDExpandImm(op, cmode, a:b:c:d:e:f:g:h); constant bits(datasize) imm = Replicate(imm64, datasize DIV 64);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP register, encoded in the 'Rd' field.

For the '16-bit' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |

<!-- image -->

&lt;T&gt;

## &lt;imm8&gt;

Is an 8-bit immediate encoded in 'a:b:c:d:e:f:g:h'.

## &lt;amount&gt;

For the '16-bit' variant: is the shift amount encoded in 'cmode&lt;1&gt;':

|   cmode<1> |   <amount> |
|------------|------------|
|          0 |          0 |
|          1 |          8 |

defaulting to 0 if LSL is omitted.

For the '32-bit' variant: is the shift amount encoded in 'cmode&lt;2:1&gt;':

|   cmode<2:1> |   <amount> |
|--------------|------------|
|           00 |          0 |
|           01 |          8 |
|           10 |         16 |
|           11 |         24 |

defaulting to 0 if LSL is omitted.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[rd, datasize]; V[rd, datasize] = operand AND NOT(imm);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| 1   | 8H   |
|-----|------|

For the '32-bit' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 2S    |
|   1 | 4S    |
