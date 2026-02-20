## C8.2.447 LSR (immediate, unpredicated)

Logical shift right by immediate (unpredicated)

This instruction shifts right by immediate, inserting zeroes, each element of the source vector, and places the results in the corresponding elements of the destination vector. The immediate shift amount is an unsigned value in the range 1 to number of bits per element. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
LSR <Zd>.<T>, <Zn>.<T>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(4) tsize = tszh:tszl; if tsize == '0000' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer shift = (2 * esize) UInt(tsize:imm3);
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

Is the immediate shift amount, in the range 1 to number of bits per element, encoded in 'tszh:tszl:imm3'.

<!-- image -->

&lt;Zn&gt;

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, Elem[result, e, esize] = LSR(element1, shift); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
esize];
```