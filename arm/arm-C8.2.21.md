## C8.2.21 AESEMC

Multi-vector AES single round encryption and mix columns

This instruction reads a 16-byte state array from each 128-bit segment of the two or four first source vectors, together with a round key from the indexed 128-bit segment of the corresponding 512-bit portion of the second source vector. Each state array undergoes a single round of the AddRoundKey(), ShiftRows(), SubBytes(), and MixColumns() transformations in accordance with the AES standard. Each updated state array is destructively placed in the corresponding segment of the two or four first source vectors.

When the vector length is less than 512 bits, the most significant bits of the index are ignored to select the indexed 128-bit segment of the second source vector. This instruction is unpredicated.

This instruction is legal when executed in Streaming SVE mode if both FEAT\_SSVE\_AES and FEAT\_SVE\_AES2 are implemented.

It has encodings from 2 classes: Two registers and Four registers

## Two registers

(FEAT\_SVE\_AES2)

<!-- image -->

## Encoding

```
AESEMC { <Zdn1>.B-<Zdn2>.B }, { <Zdn1>.B-<Zdn2>.B }, <Zm>.Q[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_AES2) then EndOfDecode(Decode_UNDEF);
```

```
constant integer m = UInt(Zm); constant integer dn = UInt(Zdn:'0'); integer index = UInt(i2); constant integer nreg = 2;
```

## Four registers

(FEAT\_SVE\_AES2)

<!-- image -->

## Encoding

```
AESEMC { <Zdn1>.B-<Zdn4>.B }, { <Zdn1>.B-<Zdn4>.B },
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_AES2) then EndOfDecode(Decode_UNDEF);
```

```
constant integer m = UInt(Zm); constant integer dn = UInt(Zdn:'00'); integer index = UInt(i2); constant integer nreg = 4;
```

```
<Zm>.Q[<index>]
```

## Assembler Symbols

## &lt;Zdn1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4.

## &lt;Zdn2&gt;

Is the name of the second scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 2 plus 1.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;index&gt;

Is the round key index, in the range 0 to 3, encoded in the 'i2' field.

## &lt;Zdn4&gt;

Is the name of the fourth scalable vector register of the destination and first source multi-vector group, encoded as 'Zdn' times 4 plus 3.

## Operation

```
if IsFeatureImplemented(FEAT_SSVE_AES) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; if VL == 128 then index = 0; if VL == 256 then index = index MOD 2; constant integer segments = VL DIV 128; constant bits(VL) operand2 = Z[m, VL]; array [0..3] of bits(VL) results; for r = 0 to nreg-1 constant bits(VL) operand1 = Z[dn + r, VL]; for s = 0 to segments-1 constant integer keyindex = (s - (s MOD 4)) + index; constant bits(128) res = Elem[operand1, s, 128] EOR Elem[operand2, keyindex, 128]; Elem[results[r], s, 128] = AESMixColumns(AESSubBytes(AESShiftRows(res))); for r = 0 to nreg-1 Z[dn + r, VL] = results[r];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.