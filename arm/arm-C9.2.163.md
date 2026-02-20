## C9.2.163 LUTI4 (four registers, 8-bit)

Lookup table read with 4-bit indexes and 8-bit elements (four registers)

This instruction copies 8-bit elements from ZT0 to four destination vectors using packed 4-bit indices in the two source vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Consecutive and Strided

## Consecutive

(FEAT\_SME\_LUTv2)

<!-- image -->

## Encoding

```
LUTI4 { <Zd1>.B-<Zd4>.B }, ZT0, { <Zn1>-<Zn2> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_LUTv2) then EndOfDecode(Decode_UNDEF); if size != '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 4; constant integer n = UInt(Zn:'0'); constant integer dstride = 1; constant integer d = UInt(Zd:'00'); constant integer nreg = 4;
```

## Strided

(FEAT\_SME2p1 &amp;&amp; FEAT\_SME\_LUTv2)

<!-- image -->

## Encoding

```
LUTI4 { <Zd1>.B, <Zd2>.B, <Zd3>.B, <Zd4>.B }, ZT0, { <Zn1>-<Zn2> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2p1) || !IsFeatureImplemented(FEAT_SME_LUTv2) then EndOfDecode(Decode_UNDEF); if size != '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 4; constant integer n = UInt(Zn:'0'); constant integer dstride = 4; constant integer d = UInt(D:'00':Zd); constant integer nreg = 4;
```

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Consecutive' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

For the 'Strided' variant: is the name of the first scalable vector register Z0-Z3 or Z16-Z19 of the destination multi-vector group, encoded as 'D:'00':Zd'.

## &lt;Zd4&gt;

For the 'Consecutive' variant: is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

For the 'Strided' variant: is the name of the fourth scalable vector register Z12-Z15 or Z28-Z31 of the destination multi-vector group, encoded as 'D:'11':Zd'.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

## &lt;Zd2&gt;

Is the name of the second scalable vector register Z4-Z7 or Z20-Z23 of the destination multi-vector group, encoded as 'D:'01':Zd'.

## &lt;Zd3&gt;

Is the name of the third scalable vector register Z8-Z11 or Z24-Z27 of the destination multi-vector group, encoded as 'D:'10':Zd'.

## Operation

```
CheckStreamingSVEEnabled(); CheckSMEZT0Enabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(2*VL) indexes = Z[n+1, VL] : Z[n+0, VL]; integer dst = d; constant bits(512) table = ZT0[512]; for r = 0 to nreg-1 constant integer base = r * elements; bits(VL) result; for e = 0 to elements-1 constant integer index = UInt(Elem[indexes, base+e, isize]); Elem[result, e, esize] = Elem[table, index, 32]<esize-1:0>; Z[dst, VL] = result; dst = dst + dstride;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.