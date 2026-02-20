## C8.2.130 DUP (indexed)

Broadcast indexed element to vector (unpredicated)

This instruction unconditionally broadcasts the indexed source vector element into each element of the destination vector. This instruction is unpredicated.

The immediate element index is in the range of 0 to 63 (bytes), 31 (halfwords), 15 (words), 7 (doublewords) or 3 (quadwords). Selecting an element beyond the accessible vector length causes the destination vector to be set to zero.

This instruction is used by the alias MOV (SIMD&amp;FP scalar, unpredicated).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
DUP <Zd>.<T>, <Zn>.<T>[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if tsz == '00000' then EndOfDecode(Decode_UNDEF); constant integer lsb = LowestSetBit(tsz); constant integer esize = 8 << lsb; constant bits(7) imm = imm2:tsz; constant integer index = UInt(imm<6:(lsb+1)>); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tsz':

<!-- image -->

| tsz   | <T>      |
|-------|----------|
| 00000 | RESERVED |
| xxxx1 | B        |
| xxx10 | H        |
| xx100 | S        |
| x1000 | D        |
| 10000 | Q        |

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;imm&gt;

Is the immediate index, in the range 0 to one less than the number of elements in 512 bits, encoded in 'imm2:tsz'.

## Alias Conditions

| Alias                              | Is preferred when    |
|------------------------------------|----------------------|
| MOV (SIMD&FP scalar, unpredicated) | BitCount(imm2 : tsz) |
| MOV (SIMD&FP scalar, unpredicated) | BitCount(imm2 : tsz) |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = if index < elements then Z[n, VL] else Zeros(VL); bits(VL) result; bits(esize) element; if index >= elements then element = Zeros(esize); else element = Elem[operand1, index, esize]; result = Replicate(element, VL DIV esize); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.