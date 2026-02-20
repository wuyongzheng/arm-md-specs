## C8.2.132 DUPQ

Broadcast indexed element within each quadword vector segment (unpredicated)

This instruction unconditionally broadcasts the indexed element within each 128-bit source vector segment to all elements of the corresponding destination vector segment. This instruction is unpredicated.

The immediate element index is in the range of 0 to 15 (bytes), 7 (halfwords), 3 (words) or 1 (doublewords).

## SVE2

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
DUPQ <Zd>.<T>, <Zn>.<T>[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); if tsz == '0000' then EndOfDecode(Decode_UNDEF); constant integer lsb = LowestSetBit(tsz); constant integer esize = 8 << lsb; constant bits(5) imm = i1:tsz; constant integer index = UInt(imm<4:(lsb+1)>); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tsz':

<!-- image -->

&lt;Zn&gt;

| tsz   | <T>      |
|-------|----------|
| 0000  | RESERVED |
| xxx1  | B        |
| xx10  | H        |
| x100  | S        |
| 1000  | D        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;imm&gt;

Is the immediate index, in the range 0 to one less than the number of elements in 128 bits, encoded in 'i1:tsz'.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant integer elements = 128 DIV esize; constant bits(VL) operand = Z[n, VL]; bits(VL) result; bits(esize) element; for s = 0 to segments-1 element = Elem[operand, s * elements + index, esize]; Elem[result, s, 128] = Replicate(element, 128 Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
DIV esize);
```