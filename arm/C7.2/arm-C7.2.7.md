## C7.2.7 AESD

AES single round decryption.

## Advanced SIMD

(FEAT\_AES)

<!-- image -->

## Encoding

```
AESD <Vd>.16B, <Vn>.16B
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

Is the name of the SIMD&amp;FP source and destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[d, 128]; constant bits(128) operand2 = V[n, 128]; bits(128) result = operand1 EOR operand2; result = AESInvShiftRows(result); V[d, 128] = AESInvSubBytes(result);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
