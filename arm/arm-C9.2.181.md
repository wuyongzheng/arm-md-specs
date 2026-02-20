## C9.2.181 MOVA (vector to tile, two registers)

Move Z two-vector operand to ZA two-slice operand

This instruction operates on a horizontal or vertical ZA two-slice operand within a ZA tile of the specified element size.

The first slice of the two-slice operand is selected by rounding down the sum of the slice index register and the immediate offset to the nearest lower multiple of 2, modulo the number of slices in the tile.

The immediate offset is a multiple of 2 in the range 0 to the number of elements in a 128-bit vector segment minus 2.

This instruction is unpredicated.

This instruction is used by the alias MOV (vector to tile, two registers).

It has encodings from 4 classes: 8-bit, 16-bit, 32-bit, and 64-bit

## 8-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA ZA0<HV>.B[<Ws>, <offs1>:<offs2>], { <Zn1>.B-<Zn2>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 8; constant integer n = UInt(Zn:'0'); constant integer d = 0; constant integer offset = UInt(off3:'0'); constant boolean vertical = V == '1';
```

## 16-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA <ZAd><HV>.H[<Ws>, <offs1>:<offs2>], {
```

size

```
}
```

```
<Zn1>.H-<Zn2>.H }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 16; constant integer n = UInt(Zn:'0'); constant integer d = UInt(ZAd); constant integer offset = UInt(off2:'0'); constant boolean vertical = V == '1';
```

## 32-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA <ZAd><HV>.S[<Ws>, <offs1>:<offs2>], { <Zn1>.S-<Zn2>.S }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 32; constant integer n = UInt(Zn:'0'); constant integer d = UInt(ZAd); constant integer offset = UInt(o1:'0'); constant boolean vertical = V == '1';
```

## 64-bit

(FEAT\_SME2)

<!-- image -->

## Encoding

```
MOVA <ZAd><HV>.D[<Ws>, <offs1>:<offs2>], { <Zn1>.D-<Zn2>.D }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then constant integer s = UInt('011':Rs); constant integer nreg = 2; constant integer esize = 64; constant integer n = UInt(Zn:'0'); constant integer d = UInt(ZAd); constant integer offset = 0; constant boolean vertical = V == '1';
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_UNDEF);
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

For the '8-bit' variant: is the first slice index offset, encoded as 'off3' field times 2.

For the '16-bit' variant: is the first slice index offset, encoded as 'off2' field times 2.

For the '32-bit' variant: is the first slice index offset, encoded as 'o1' field times 2.

For the '64-bit' variant: is the first slice index offset, with implicit value 0.

## &lt;offs2&gt;

For the '8-bit' variant: is the second slice index offset, encoded as 'off3' field times 2 plus 1.

For the '16-bit' variant: is the second slice index offset, encoded as 'off2' field times 2 plus 1.

For the '32-bit' variant: is the second slice index offset, encoded as 'o1' field times 2 plus 1.

For the '64-bit' variant: is the second slice index offset, with implicit value 1.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;ZAd&gt;

For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAd' field.

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAd' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAd' field.

## Alias Conditions

| Alias                               | Is preferred when   |
|-------------------------------------|---------------------|
| MOV (vector to tile, two registers) | Unconditionally     |

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; if nreg == 4 && esize == 64 && VL < 256 then EndOfDecode(Decode_UNDEF); constant integer slices = VL DIV esize; constant bits(32) index = X[s, 32]; constant integer slice = ((UInt(index) - (UInt(index) MOD nreg)) + offset) MOD slices; for r = 0 to nreg-1 constant bits(VL) result = Z[n + r, VL]; ZAslice[d, esize, vertical, slice + r, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.