## C9.2.164 LUTI4 (four registers, 16-bit and 32-bit)

Lookup table read with 4-bit indexes (four registers)

This instruction copies 16-bit or 32-bit elements from ZT0 to four destination vectors using packed 4-bit indices from a segment of the source vector register. A segment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index modulo the total number of segments.

This instruction is unpredicated.

It has encodings from 2 classes: Consecutive and Strided

## Consecutive

(FEAT\_SME2)

<!-- image -->

## Encoding

```
LUTI4 { <Zd1>.<T>-<Zd4>.<T> }, ZT0, <Zn>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if size == '00' || size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 4; constant integer n = UInt(Zn); constant integer dstride = 1; constant integer d = UInt(Zd:'00'); constant integer imm = UInt(i1); constant integer nreg = 4;
```

## Strided

(FEAT\_SME2p1)

<!-- image -->

## Encoding

```
LUTI4 { <Zd1>.H, <Zd2>.H, <Zd3>.H, <Zd4>.H }, ZT0, <Zn>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); if size != '01' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 4; constant integer n = UInt(Zn); constant integer dstride = 4; constant integer d = UInt(D:'00':Zd); constant integer imm = UInt(i1); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Consecutive' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

For the 'Strided' variant: is the name of the first scalable vector register Z0-Z3 or Z16-Z19 of the destination multi-vector group, encoded as 'D:'00':Zd'.

Is the size specifier, encoded in 'size':

## &lt;Zd4&gt;

For the 'Consecutive' variant: is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

For the 'Strided' variant: is the name of the fourth scalable vector register Z12-Z15 or Z28-Z31 of the destination multi-vector group, encoded as 'D:'11':Zd'.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;index&gt;

Is the vector segment index, in the range 0 to 1, encoded in the 'i1' field.

## &lt;Zd2&gt;

Is the name of the second scalable vector register Z4-Z7 or Z20-Z23 of the destination multi-vector group, encoded as 'D:'01':Zd'.

## &lt;Zd3&gt;

Is the name of the third scalable vector register Z8-Z11 or Z24-Z27 of the destination multi-vector group, encoded as 'D:'10':Zd'.

&lt;T&gt;

## &lt;Zn&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

## Operation

```
CheckStreamingSVEEnabled(); CheckSMEZT0Enabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer segments = esize DIV (isize * nreg); constant integer segment = imm MOD segments; constant bits(VL) indexes = Z[n, VL]; integer dst = d; constant bits(512) table = ZT0[512]; for r = 0 to nreg-1 constant integer base = (segment * nreg + r) * elements; bits(VL) result; for e = 0 to elements-1 constant integer index = UInt(Elem[indexes, base+e, isize]); Elem[result, e, esize] = Elem[table, index, 32]<esize-1:0>; Z[dst, VL] = result; dst = dst + dstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.