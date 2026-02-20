## C9.2.159 LUTI2 (two registers)

Lookup table read with 2-bit indexes (two registers)

This instruction copies 8-bit, 16-bit or 32-bit elements from ZT0 to two destination vectors using packed 2-bit indices from a segment of the source vector register. A segment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index modulo the total number of segments.

This instruction is unpredicated.

It has encodings from 2 classes: Consecutive and Strided

## Consecutive

(FEAT\_SME2)

<!-- image -->

## Encoding

```
LUTI2 { <Zd1>.<T>-<Zd2>.<T> }, ZT0, <Zn>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 2; constant integer n = UInt(Zn); constant integer dstride = 1; constant integer d = UInt(Zd:'0'); constant integer imm = UInt(i3); constant integer nreg = 2;
```

## Strided

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
LUTI2 { <Zd1>.<T>, <Zd2>.<T> }, ZT0, <Zn>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); if size == '10' || size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 2; constant integer n = UInt(Zn); constant integer dstride = 8; constant integer d = UInt(D:'0':Zd); constant integer imm = UInt(i3); constant integer nreg = 2;
```

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Consecutive' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Strided' variant: is the name of the first scalable vector register Z0-Z7 or Z16-Z23 of the destination multi-vector group, encoded as 'D:'0':Zd'.

For the 'Consecutive' variant: is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | B        |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

For the 'Strided' variant: is the size specifier, encoded in 'size&lt;0&gt;':

|   size<0> | <T>   |
|-----------|-------|
|         0 | B     |
|         1 | H     |

&lt;T&gt;

## &lt;Zd2&gt;

For the 'Consecutive' variant: is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

For the 'Strided' variant: is the name of the second scalable vector register Z8-Z15 or Z24-Z31 of the destination multi-vector group, encoded as 'D:'1':Zd'.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;index&gt;

Is the vector segment index, in the range 0 to 7, encoded in the 'i3' field.

## &lt;Zn&gt;

## Operation

```
CheckStreamingSVEEnabled(); CheckSMEZT0Enabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer segments = esize DIV (isize * nreg); constant integer segment = imm MOD segments; constant bits(VL) indexes = Z[n, VL]; integer dst = d; constant bits(512) table = ZT0[512]; for r = 0 to nreg-1 constant integer base = (segment * nreg + r) * elements; bits(VL) result; for e = 0 to elements-1 constant integer index = UInt(Elem[indexes, base+e, isize]); Elem[result, e, esize] = Elem[table, index, 32]<esize-1:0>; Z[dst, VL] = result; dst = dst + dstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.