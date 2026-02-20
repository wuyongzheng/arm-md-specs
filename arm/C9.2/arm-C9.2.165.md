## C9.2.165 LUTI4 (single)

Lookup table read with 4-bit indexes (single)

This instruction copies 8-bit, 16-bit or 32-bit elements from ZT0 to one destination vector using packed 4-bit indices from a segment of the source vector register. A segment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index modulo the total number of segments.

This instruction is unpredicated.

```
SME2 (FEAT_SME2)
```

<!-- image -->

## Encoding

```
LUTI4 <Zd>.<T>, ZT0, <Zn>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer isize = 4; constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer imm = UInt(i3); constant integer nreg = 1;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Zn&gt;

|   size | <T>      |
|--------|----------|
|     00 | B        |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;index&gt;

Is the vector segment index, in the range 0 to 7, encoded in the 'i3' field.

## Operation

```
CheckStreamingSVEEnabled(); CheckSMEZT0Enabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer segments = esize DIV (isize * nreg); constant integer segment = imm MOD segments; constant bits(VL) indexes = Z[n, VL]; constant integer dst = d; constant bits(512) table = ZT0[512]; for r = 0 to nreg-1 constant integer base = (segment * nreg + r) * elements; bits(VL) result; for e = 0 to elements-1 constant integer index = UInt(Elem[indexes, base+e, isize]); Elem[result, e, esize] = Elem[table, index, 32]<esize-1:0>; Z[dst+r, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.