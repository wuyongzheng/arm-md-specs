## C8.2.677 SQSHRUNT

Signed saturating shift right narrow by immediate to unsigned integer (top)

This instruction shifts each signed integer value in the source vector elements right by an immediate value, and places the truncated results in the odd-numbered half-width destination elements, leaving the even-numbered elements unchanged. Each result element is saturated to the half-width N-bit element's unsigned integer range 0 to (2 N )-1. The immediate shift amount is an unsigned value in the range 1 to number of bits per element. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQSHRUNT <Zd>.<T>, <Zn>.<Tb>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(3) tsize = tszh:tszl; if tsize == '000' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer shift = (2 * esize) UInt(tsize:imm3);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <T>      |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | B        |
|      0 | 1x     | H        |
|      1 | xx     | S        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

<!-- image -->

&lt;Zn&gt;

## &lt;Tb&gt;

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <Tb>     |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | H        |
|      0 | 1x     | S        |
|      1 | xx     | D        |

## &lt;const&gt;

Is the immediate shift amount, in the range 1 to number of bits per element, encoded in 'tszh:tszl:imm3'.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant bits(VL) operand = Z[n, VL]; bits(VL) result = Z[d, VL]; for e = 0 to elements-1 constant bits(2*esize) element = Elem[operand, e, 2*esize]; constant integer res = SInt(element) >> shift; Elem[result, 2*e + 1, esize] = UnsignedSat(res, esize); Z[d, VL] = result;
```