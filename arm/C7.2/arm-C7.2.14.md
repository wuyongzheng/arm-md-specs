## C7.2.14 BFCVT

Single-precision convert to BFloat16 (scalar)

This instruction converts the single-precision floating-point value in the 32-bit SIMD&amp;FP source register to BFloat16 format and writes the result in the 16-bit SIMD&amp;FP destination register.

ID\_AA64ISAR1\_EL1.BF16 indicates whether this instruction is supported.

## Single-precision to BFloat16

(FEAT\_BF16)

<!-- image -->

## Encoding

```
BFCVT <Hd>, <Sn>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_BF16) then constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

<!-- image -->

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(32) operand = V[n, 32]; constant boolean merge = IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); Elem[result, 0, 16] = FPConvertBF(operand, FPCR); V[d, 128] = result;
```

```
EndOfDecode(Decode_UNDEF);
```
