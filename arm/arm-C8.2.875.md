## C8.2.875 UQSHRNB

Unsigned saturating shift right narrow by immediate (bottom)

This instruction shifts each unsigned integer value in the source vector elements right by an immediate value, and places the truncated results in the even-numbered half-width destination elements, while setting the odd-numbered elements to zero. Each result element is saturated to the half-width N-bit element's unsigned integer range 0 to (2 N )-1. The immediate shift amount is an unsigned value in the range 1 to number of bits per element. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
UQSHRNB <Zd>.<T>, <Zn>.<Tb>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(3) tsize = tszh:tszl; if tsize == '000' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer shift = (2 * esize) UInt(tsize:imm3);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <T>      |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | B        |
|      0 | 1x     | H        |
|      1 | xx     | S        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

&lt;T&gt;

<!-- image -->

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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV (2 * esize); constant bits(VL) operand = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(2*esize) element = Elem[operand, e, 2*esize]; constant integer res = UInt(element) >> shift; Elem[result, 2*e + 0, esize] = UnsignedSat(res, esize); Elem[result, 2*e + 1, esize] = Zeros(esize); Z[d, VL] = result;
```