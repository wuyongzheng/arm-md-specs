## C8.2.450 LUTI2 (8-bit and 16-bit)

Lookup table read with 2-bit indices (8-bit and 16-bit)

This instruction copies indexed 8-bit or 16-bit elements from the low 128 bits of the table vector to the destination vector using packed 2-bit indices from a segment of the source vector. A segment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index. This instruction is unpredicated.

It has encodings from 2 classes: Byte and Halfword

## Byte

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_LUT)

<!-- image -->

## Encoding

```
LUTI2 <Zd>.B, { <Zn>.B }, <Zm>[<index>]
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_LUT)) then EndOfDecode(Decode_UNDEF); constant integer isize = 2; constant integer esize = 8; constant integer m = UInt(Zm); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer part = UInt(i2);
```

## Halfword

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_LUT)

<!-- image -->

## Encoding

```
LUTI2 <Zd>.H, { <Zn>.H }, <Zm>[<index>]
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_LUT)) then EndOfDecode(Decode_UNDEF); constant integer isize = 2; constant integer esize = 16; constant integer m = UInt(Zm); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer part = UInt(i3h:i3l);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the table vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the source scalable vector register, encoded in the 'Zm' field.

## &lt;index&gt;

For the 'Byte' variant: is the vector segment index, in the range 0 to 3, encoded in the 'i2' field.

For the 'Halfword' variant: is the vector segment index, in the range 0 to 7, encoded in the 'i3h:i3l' fields.

## Operation

```
if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer ibase = elements * part; constant bits(VL) indexes = Z[m, VL]; constant bits(VL) table = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant integer index = UInt(Elem[indexes, ibase + e, isize]); Elem[result, e, esize] = Elem[table, index, esize]; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.