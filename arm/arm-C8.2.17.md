## C8.2.17 AESD (vectors)

AES single round decryption

This instruction reads a 16-byte state array from each 128-bit segment of the first source vector, together with a round key from the corresponding 128-bit segment of the second source vector. Each state array undergoes a single round of the AddRoundKey(), InvShiftRows(), and InvSubBytes() transformations in accordance with the AES standard. Each updated state array is destructively placed in the corresponding segment of the first source vector. This instruction is unpredicated.

## ID\_AA64ZFR0\_EL1.AES indicates whether this instruction is implemented.

This instruction is legal when executed in Streaming SVE mode if one of the following is true:

- Both FEAT\_SSVE\_AES and FEAT\_SVE\_AES are implemented.
- FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE\_AES)

<!-- image -->

## Encoding

```
AESD <Zdn>.B, <Zdn>.B, <Zm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_AES) then EndOfDecode(Decode_UNDEF);
```

```
constant integer m = UInt(Zm); constant integer dn = UInt(Zdn);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_AES) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; result = operand1 EOR operand2; for s = 0 to segments-1 Elem[result, s, 128] = AESInvSubBytes(AESInvShiftRows(Elem[result, s, 128])); Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.