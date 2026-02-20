## C8.2.583 SLI

Shift left and insert (immediate)

This instruction shifts each source vector element left by an immediate value, and inserts the result into the corresponding vector element in the destination vector register, merging the shifted bits from each source element with existing bits in each destination vector element. The immediate shift amount is an unsigned value in the range 0 to number of bits per element minus 1. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SLI <Zd>.<T>, <Zn>.<T>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(4) tsize = tszh:tszl; if tsize == '0000' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer shift = UInt(tsize:imm3) esize;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tszh:tszl':

| tszh   | tszl   | <T>      |
|--------|--------|----------|
| 00     | 00     | RESERVED |
| 00     | 01     | B        |
| 00     | 1x     | H        |
| 01     | xx     | S        |
| 1x     | xx     | D        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;const&gt;

Is the immediate shift amount, in the range 0 to number of bits per element minus 1, encoded in 'tszh:tszl:imm3'.

<!-- image -->

&lt;Zn&gt;

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand = Z[n, VL]; bits(VL) result = Z[d, VL]; for e = 0 to elements-1 constant bits(esize) element1 = Elem[result, e, esize]; constant bits(esize) element2 = Elem[operand, e, esize]; constant bits(esize) mask = LSL(Ones(esize), shift); constant bits(esize) shiftedval = LSL(element2, shift); Elem[result, e, esize] = (element1 AND (NOT mask)) Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
OR shiftedval;
```