## C8.2.22 AESIMC

AES inverse mix columns

This instruction reads a 16-byte state array from each 128-bit segment of the source register, and performs a single round of the InvMixColumns() transformation on each state array in accordance with the AES standard. Each updated state array is destructively placed in the corresponding segment of the first source vector. This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.AES indicates whether this instruction is implemented.

This instruction is legal when executed in Streaming SVE mode if one of the following is true:

- Both FEAT\_SSVE\_AES and FEAT\_SVE\_AES are implemented.
- FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE\_AES)

<!-- image -->

## Encoding

```
AESIMC <Zdn>.B, <Zdn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_AES) then EndOfDecode(Decode_UNDEF); constant integer dn = UInt(Zdn);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_AES) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant bits(VL) operand = Z[dn, VL]; bits(VL) result; for s = 0 to segments-1 Elem[result, s, 128] = AESInvMixColumns(Elem[operand, s, 128]); Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.