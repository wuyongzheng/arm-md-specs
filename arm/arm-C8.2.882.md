## C8.2.882 UQXTNT

Unsigned saturating extract narrow (top)

This instruction saturates the unsigned integer value in each source element to half the original source element width, and places the results in the odd-numbered half-width destination elements, leaving the even-numbered elements unchanged.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

| 31   | 29   | 28    | 25 24   |    | 23 22   | 21   | 20 19   | 18   | 17 16   | 15   | 14   | 13   | 12 11   | 10   |    | 5 4   | 0   |
|------|------|-------|---------|----|---------|------|---------|------|---------|------|------|------|---------|------|----|-------|-----|
| 0    | 1 0  | 0 0 1 | 0       | 1  | 0       | 1    | tszl    | 0    | 0 0     | 0    | 1    | 0    | 0 1     | 1    | Zn |       | Zd  |
|      |      |       |         |    |         | tszh |         |      |         |      |      |      | U       | T    |    |       |     |

## Encoding

```
UQXTNT <Zd>.<T>, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(3) tsize = tszh:tszl; if !(tsize IN {'001', '010', '100'}) then EndOfDecode(Decode_UNDEF); constant integer esize = 16 << HighestSetBitNZ(tsize); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <T>      |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | B        |
|      0 | 10     | H        |
|      0 | 11     | RESERVED |
|      1 | 00     | S        |
|      1 | 01     | RESERVED |
|      1 | 1x     | RESERVED |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

<!-- image -->

## &lt;Tb&gt;

Is the size specifier, encoded in 'tszh:tszl':

|   tszh | tszl   | <Tb>     |
|--------|--------|----------|
|      0 | 00     | RESERVED |
|      0 | 01     | H        |
|      0 | 10     | S        |
|      0 | 11     | RESERVED |
|      1 | 00     | D        |
|      1 | 01     | RESERVED |
|      1 | 1x     | RESERVED |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; bits(VL) result = Z[d, VL]; constant integer halfesize = esize DIV 2; for e = 0 to elements-1 constant integer element1 = UInt(Elem[operand1, e, esize]); constant bits(halfesize) res = UnsignedSat(element1, halfesize); Elem[result, 2*e + 1, halfesize] = res; Z[d, VL] = result;
```