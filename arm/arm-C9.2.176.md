## C9.2.176 MOVA (tile to vector, two registers)

Move ZA two-slice operand to Z two-vector operand

This instruction operates on a horizontal or vertical ZA two-slice operand within a ZA tile of the specified element size.

The first slice of the two-slice operand is selected by rounding down the sum of the slice index register and the immediate offset to the nearest lower multiple of 2, modulo the number of slices in the tile.

The immediate offset is a multiple of 2 in the range 0 to the number of elements in a 128-bit vector segment minus 2.

This instruction is unpredicated.

This instruction is used by the alias MOV (tile to vector, two registers).

It has encodings from 4 classes: 8-bit, 16-bit, 32-bit, and 64-bit

## 8-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA { <Zd1>.B-<Zd2>.B }, ZA0<HV>.B[<Ws>, <offs1>:<offs2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 8; constant integer d = UInt(Zd:'0'); constant integer n = 0; constant integer offset = UInt(off3:'0'); constant boolean vertical = V == '1';
```

## 16-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA { <Zd1>.H-<Zd2>.H }, <ZAn><HV>.H[<Ws>, <offs1>:<offs2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 16; constant integer d = UInt(Zd:'0'); constant integer n = UInt(ZAn); constant integer offset = UInt(off2:'0'); constant boolean vertical = V == '1';
```

## 32-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA { <Zd1>.S-<Zd2>.S }, <ZAn><HV>.S[<Ws>, <offs1>:<offs2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 32; constant integer d = UInt(Zd:'0'); constant integer n = UInt(ZAn); constant integer offset = UInt(o1:'0'); constant boolean vertical = V == '1';
```

## 64-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA { <Zd1>.D-<Zd2>.D }, <ZAn><HV>.D[<Ws>, <offs1>:<offs2>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 64; constant integer d = UInt(Zd:'0'); constant integer n = UInt(ZAn); constant integer offset = 0; constant boolean vertical = V == '1';
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Zd1&gt;

Is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;HV&gt;

Is the horizontal or vertical slice indicator, encoded in 'V':

|   V | <HV>   |
|-----|--------|
|   0 | H      |
|   1 | V      |

## &lt;Ws&gt;

Is the 32-bit name of the slice index register W12-W15, encoded in the 'Rs' field.

## &lt;offs1&gt;

For the '8-bit' variant: is the first slice index offset, encoded as 'off3' field times 2.

For the '16-bit' variant: is the first slice index offset, encoded as 'off2' field times 2.

For the '32-bit' variant: is the first slice index offset, encoded as 'o1' field times 2.

For the '64-bit' variant: is the first slice index offset, with implicit value 0.

## &lt;offs2&gt;

For the '8-bit' variant: is the second slice index offset, encoded as 'off3' field times 2 plus 1.

For the '16-bit' variant: is the second slice index offset, encoded as 'off2' field times 2 plus 1.

For the '32-bit' variant: is the second slice index offset, encoded as 'o1' field times 2 plus 1.

For the '64-bit' variant: is the second slice index offset, with implicit value 1.

## &lt;ZAn&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAn' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAn' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAn' field.

## Alias Conditions

| Alias                               | Is preferred when   |
|-------------------------------------|---------------------|
| MOV (tile to vector, two registers) | Unconditionally     |

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; if nreg == 4 && esize == 64 && VL < 256 then EndOfDecode(Decode_UNDEF); constant integer slices = VL DIV esize; constant bits(32) index = X[s, 32]; constant integer slice = ((UInt(index) - (UInt(index) MOD nreg)) + offset) MOD slices; for r = 0 to nreg-1 constant bits(VL) result = ZAslice[n, esize, vertical, slice + r, VL]; Z[d + r, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.