## C8.2.451 LUTI4 (8-bit and 16-bit)

Lookup table read with 4-bit indices (8-bit and 16-bit)

This instruction copies indexed 8-bit or 16-bit elements from the low 128 or 256 bits of the table vector, or from the low 128 bits of the two table vectors to the destination vector using packed 4-bit indices from a segment of the source vector. Asegment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index. This instruction is unpredicated.

It has encodings from 3 classes: Byte, single register table, Halfword, two register table, and Halfword, single register table

## Byte, single register table

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_LUT)

<!-- image -->

| 31 29 28   | 25 24 23 22 21   | 13 12 10   | 9   | 5 4   |
|------------|------------------|------------|-----|-------|
| 0 1 0      | 0 0 1 0 1 i1 1 1 | 0 1 0 0 1  | Zn  | Zd    |

## Encoding

```
LUTI4 <Zd>.B, { <Zn>.B }, <Zm>[<index>]
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_LUT)) then EndOfDecode(Decode_UNDEF); constant integer isize = 4; constant integer esize = 8; constant integer ntblr = 1; constant integer m = UInt(Zm); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer part = UInt(i1);
```

## Halfword, two register table

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_LUT)

<!-- image -->

## Encoding

```
LUTI4 <Zd>.H, {
```

```
<Zn1>.H, <Zn2>.H }, <Zm>[<index>]
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_LUT)) then EndOfDecode(Decode_UNDEF); constant integer isize = 4; constant integer esize = 16; constant integer ntblr = 2; constant integer m = UInt(Zm); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer part = UInt(i2);
```

## Halfword, single register table

((FEAT\_SVE2 || FEAT\_SME2) &amp;&amp; FEAT\_LUT)

<!-- image -->

## Encoding

```
LUTI4 <Zd>.H, { <Zn>.H }, <Zm>[<index>]
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME2)) || !IsFeatureImplemented(FEAT_LUT)) then EndOfDecode(Decode_UNDEF); if MaxImplementedAnyVL() < 256 then EndOfDecode(Decode_UNDEF); constant integer isize = 4; constant integer esize = 16; constant integer ntblr = 1; constant integer m = UInt(Zm); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer part = UInt(i2);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

## &lt;Zn&gt;

Is the name of the table vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the source scalable vector register, encoded in the 'Zm' field.

## &lt;index&gt;

For the 'Byte, single register table' variant: is the vector segment index, in the range 0 to 1, encoded in the 'i1' field.

For the 'Halfword, single register table' and 'Halfword, two register table' variants: is the vector segment index, in the range 0 to 3, encoded in the 'i2' field.

## &lt;Zn1&gt;

Is the name of the first table vector register, encoded as 'Zn'.

<!-- image -->

Is the name of the second table vector register, encoded as 'Zn' plus 1 modulo 32.

## Operation

```
if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; if ntblr == 1 && esize == 16 && VL < 256 then EndOfDecode(Decode_UNDEF); constant integer elements = VL DIV esize; constant integer tablesize = if ntblr == 1 && esize == 16 then 256 else 128; constant integer eltspertable = tablesize DIV esize; constant integer ibase = elements * part; constant bits(VL) indexes = Z[m, VL]; constant bits(VL) table1 = Z[n+0, VL]; constant bits(VL) table2 = if ntblr == 2 then Z[(n+1) MOD 32, VL] else Zeros(VL); bits(VL) result; bits(esize) res; for e = 0 to elements-1 constant integer index = UInt(Elem[indexes, ibase + e, isize]); if index < eltspertable then res = Elem[table1, index, esize]; else assert ntblr == 2; res = Elem[table2, index -eltspertable, esize]; Elem[result, e, esize] = res; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.