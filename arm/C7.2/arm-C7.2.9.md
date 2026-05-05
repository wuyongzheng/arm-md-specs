## C7.2.9 AESIMC

AES inverse mix columns.

## Advanced SIMD

(FEAT\_AES)

<!-- image -->

## Encoding

```
AESIMC <Vd>.16B, <Vn>.16B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AES) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand = V[n, 128]; V[d, 128] = AESInvMixColumns(operand);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
