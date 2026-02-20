## C8.2.118 COMPACT

Copy Active vector elements to lower-numbered elements

This instruction copies Active elements from the source vector to consecutive elements of the destination vector, in increasing order of element number, and sets any remaining elements to zero.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled, or FEAT\_SME2p2 is implemented.

It has encodings from 2 classes: Byte and halfword and Word and doubleword

## Byte and halfword

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

|   31 | 29 28   | 25 24   | 23   |    | 22   |   21 |   20 | 19   | 17   | 16 15   | 14   |   13 12 | 10   | 9   | 5 4   | 0   |
|------|---------|---------|------|----|------|------|------|------|------|---------|------|---------|------|-----|-------|-----|
|    0 | 0 0 0   | 0 1 0   | 1 0  | sz |      |    1 |    0 | 0 0  | 0 1  | 1 0     |      |       0 | Pg   | Zn  |       | Zd  |

## Encoding

```
COMPACT <Zd>.<T>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(sz); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Word and doubleword

(FEAT\_SVE || FEAT\_SME2p2)

<!-- image -->

|   31 | 29 28   | 25 24 23 22 21 20   | 19 17      |    |    |    |    |   16 | 15 14   |   13 | 12   | 10 9   | 5 4   | 0   |
|------|---------|---------------------|------------|----|----|----|----|------|---------|------|------|--------|-------|-----|
|    0 | 0 0     | 0 0 1               | 0 1 sz 0 0 |  1 |  1 |  0 |  0 |    1 | 1 0     |    0 | Pg   | Zn     |       | Zd  |

## Encoding

```
COMPACT <Zd>.<T>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

For the 'Byte and halfword' variant: is the size specifier, encoded in 'sz':

|   sz | <T>   |
|------|-------|
|    0 | B     |
|    1 | H     |

For the 'Word and doubleword' variant: is the size specifier, encoded in 'sz':

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;T&gt;

&lt;Pg&gt;

<!-- image -->

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
if IsFeatureImplemented(FEAT_SME2p2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = Zeros(VL); integer x = 0; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand1, e, esize]; Elem[result, x, esize] = element; x = x + 1; Z[d, VL] = result;
```