## C8.2.892 USHLLB

Unsigned shift left long by immediate (bottom)

This instruction shifts left by immediate each even-numbered unsigned element of the source vector, and places the results in the overlapping double-width elements of the destination vector. The immediate shift amount is an unsigned value in the range 0 to number of bits per element minus 1. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
USHLLB <Zd>.<T>, <Zn>.<Tb>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(3) tsize = tszh:tszl; if tsize == '000' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer shift = UInt(tsize:imm3) esize;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <T>      |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | H        |
|      0 | 1x     | S        |
|      1 | xx     | D        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

<!-- image -->

&lt;Zn&gt;

## &lt;Tb&gt;

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <Tb>     |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | B        |
|      0 | 1x     | H        |
|      1 | xx     | S        |

## &lt;const&gt;

Is the immediate shift amount, in the range 0 to number of bits per element minus 1, encoded in 'tszh:tszl:imm3'.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant bits(VL) operand = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element = Elem[operand, 2*e + 0, esize]; constant integer shifted_value = UInt(element) << shift; Elem[result, e, 2*esize] = shifted_value<2*esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.