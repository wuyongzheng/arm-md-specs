## C9.2.180 MOVA (tile to vector, single)

Move ZA tile slice to Z vector

This instruction operates on individual horizontal or vertical slices within a named ZA tile of the specified element size. The slice number within the tile is selected by the sum of the slice index register and immediate offset, modulo the number of such elements in a vector. The immediate offset is in the range 0 to the number of elements in a 128-bit vector segment minus 1.

Inactive elements in the destination vector remain unmodified.

This instruction is used by the alias MOV (tile to vector, single).

It has encodings from 5 classes: 8-bit, 16-bit, 32-bit, 64-bit, and 128-bit

8-bit

(FEAT\_SME)

<!-- image -->

## Encoding

```
MOVA <Zd>.B, <Pg>/M, ZA0<HV>.B[<Ws>, <offs>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer s = UInt('011':Rs); constant integer n = 0; constant integer offset = UInt(off4); constant integer esize = 8; constant integer d = UInt(Zd); constant boolean vertical = V == '1';
```

## 16-bit

(FEAT\_SME)

<!-- image -->

## Encoding

```
MOVA <Zd>.H, <Pg>/M, <ZAn><HV>.H[<Ws>, <offs>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer s = UInt('011':Rs); constant integer n = UInt(ZAn); constant integer offset = UInt(off3); constant integer esize = 16; constant integer d = UInt(Zd); constant boolean vertical = V == '1';
```

## 32-bit

(FEAT\_SME)

<!-- image -->

## Encoding

```
MOVA <Zd>.S, <Pg>/M, <ZAn><HV>.S[<Ws>, <offs>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF);
```

```
constant integer g = UInt(Pg); constant integer s = UInt('011':Rs); constant integer n = UInt(ZAn); constant integer offset = UInt(off2); constant integer esize = 32; constant integer d = UInt(Zd); constant boolean vertical = V == '1';
```

## 64-bit

(FEAT\_SME)

<!-- image -->

## Encoding

```
MOVA <Zd>.D, <Pg>/M, <ZAn><HV>.D[<Ws>, <offs>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer s = UInt('011':Rs); constant integer n = UInt(ZAn); constant integer offset = UInt(o1); constant integer esize = 64; constant integer d = UInt(Zd); constant boolean vertical = V == '1';
```

## 128-bit

(FEAT\_SME)

<!-- image -->

## Encoding

```
MOVA <Zd>.Q, <Pg>/M, <ZAn><HV>.Q[<Ws>, <offs>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer s = UInt('011':Rs); constant integer n = UInt(ZAn); constant integer offset = 0; constant integer esize = 128; constant integer d = UInt(Zd); constant boolean vertical = V == '1';
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

&lt;Pg&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;HV&gt;

Is the horizontal or vertical slice indicator, encoded in 'V':

|   V | <HV>   |
|-----|--------|
|   0 | H      |
|   1 | V      |

## &lt;Ws&gt;

Is the 32-bit name of the slice index register W12-W15, encoded in the 'Rs' field.

## &lt;offs&gt;

For the '8-bit' variant: is the slice index offset, in the range 0 to 15, encoded in the 'off4' field.

For the '16-bit' variant: is the slice index offset, in the range 0 to 7, encoded in the 'off3' field.

For the '32-bit' variant: is the slice index offset, in the range 0 to 3, encoded in the 'off2' field.

For the '64-bit' variant: is the slice index offset, in the range 0 to 1, encoded in the 'o1' field.

For the '128-bit' variant: is the slice index offset, with implicit value 0.

## &lt;ZAn&gt;

```
For the '16-bit' variant: is the name of the ZA tile ZA0-ZA1 to be accessed, encoded in the 'ZAn' field. For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3 to be accessed, encoded in the 'ZAn' field. For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7 to be accessed, encoded in the 'ZAn' field. For the '128-bit' variant: is the name of the ZA tile ZA0-ZA15 to be accessed, encoded in the 'ZAn' field.
```

## Alias Conditions

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(32) index = X[s, 32]; constant integer slice = (UInt(index) + offset) MOD dim; constant bits(VL) operand = ZAslice[n, esize, vertical, slice, VL]; bits(VL) result = Z[d, VL]; for e = 0 to dim-1 constant bits(esize) element = Elem[operand, e, esize]; if ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = element; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

## Alias

MOV

(tile to vector,

single)

## Is preferred when

Unconditionally