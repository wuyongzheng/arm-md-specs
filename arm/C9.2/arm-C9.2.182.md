## C9.2.182 MOVA (vector to tile, four registers)

Move Z four-vector operand to ZA four-slice operand

This instruction operates on a horizontal or vertical ZA four-slice operand within a ZA tile of the specified element size.

The first slice of the four-slice operand is selected by rounding down the sum of the slice index register and the immediate offset to the nearest lower multiple of 4, modulo the number of slices in the tile.

The immediate offset is a multiple of 4 in the range 0 to the number of elements in a 128-bit vector segment minus 4.

This instruction is unpredicated.

This instruction is used by the alias MOV (vector to tile, four registers).

It has encodings from 4 classes: 8-bit, 16-bit, 32-bit, and 64-bit

## 8-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA ZA0<HV>.B[<Ws>, <offs1>:<offs4>], { <Zn1>.B-<Zn4>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 4; constant integer esize = 8; constant integer n = UInt(Zn:'00'); constant integer d = 0; constant integer offset = UInt(off2:'00'); constant boolean vertical = V == '1';
```

## 16-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA <ZAd><HV>.H[<Ws>, <offs1>:<offs4>], {
```

size

```
}
```

```
<Zn1>.H-<Zn4>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer s = UInt('011':Rs); constant integer nreg = 4; constant integer esize = 16; constant integer n = UInt(Zn:'00'); constant integer d = UInt(ZAd); constant integer offset = UInt(o1:'00'); constant boolean vertical = V == '1';
```

```
EndOfDecode(Decode_UNDEF);
```

<!-- image -->

<!-- image -->

```
32-bit (FEAT_SME2) 1 31 1 0 30 29 0 0 0 0 28 25 0 24 1 0 23 22 0 0 0 21 19 1 18 0 17 0 16 V 15 Rs 14 13 0 0 1 12 10 Zn 9 7 0 0 6 5 0 4 0 3 0 2 ZAd 1 0 size Encoding MOVA <ZAd><HV>.S[<Ws>, <offs1>:<offs4>], { <Zn1>.S-<Zn4>.S } Decode for this encoding if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 4; constant integer esize = 32; constant integer n = UInt(Zn:'00'); constant integer d = UInt(ZAd); constant integer offset = 0; constant boolean vertical = V == '1'; 64-bit (FEAT_SME2) 1 31 1 0 30 29 0 0 0 0 28 25 0 24 1 1 23 22 0 0 0 21 19 1 18 0 17 0 16 V 15 Rs 14 13 0 0 1 12 10 Zn 9 7 0 0 6 5 0 4 0 3 ZAd 2 0 size Encoding MOVA <ZAd><HV>.D[<Ws>, <offs1>:<offs4>], { <Zn1>.D-<Zn4>.D } Decode for this encoding
```

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_SME2) then if MaxImplementedSVL() < 256 then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 4; constant integer esize = 64; constant integer n = UInt(Zn:'00'); constant integer d = UInt(ZAd); constant integer offset = 0; constant boolean vertical = V == '1';
```

## Assembler Symbols

## &lt;HV&gt;

Is the horizontal or vertical slice indicator, encoded in 'V':

|   V | <HV>   |
|-----|--------|
|   0 | H      |
|   1 | V      |

## &lt;Ws&gt;

Is the 32-bit name of the slice index register W12-W15, encoded in the 'Rs' field.

## &lt;offs1&gt;

For the '8-bit' variant: is the first slice index offset, encoded as 'off2' field times 4.

For the '16-bit' variant: is the first slice index offset, encoded as 'o1' field times 4.

For the '32-bit' and '64-bit' variants: is the first slice index offset, with implicit value 0.

## &lt;offs4&gt;

For the '8-bit' variant: is the fourth slice index offset, encoded as 'off2' field times 4 plus 3.

For the '16-bit' variant: is the fourth slice index offset, encoded as 'o1' field times 4 plus 3.

For the '32-bit' and '64-bit' variants: is the fourth slice index offset, with implicit value 3.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 4.

## &lt;Zn4&gt;

Is the name of the fourth scalable vector register of the source multi-vector group, encoded as 'Zn' times 4 plus 3.

## &lt;ZAd&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAd' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAd' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAd' field.

## Alias Conditions

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; if nreg == 4 && esize == 64 && VL < 256 then EndOfDecode(Decode_UNDEF); constant integer slices = VL DIV esize;
```

| Alias                                | Is preferred when   |
|--------------------------------------|---------------------|
| MOV (vector to tile, four registers) | Unconditionally     |

```
constant bits(32) index = X[s, 32]; constant integer slice = ((UInt(index) - (UInt(index) MOD nreg)) + offset) MOD for r = 0 to nreg-1 constant bits(VL) result = Z[n + r, VL]; ZAslice[d, esize, vertical, slice + r, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
slices;
```