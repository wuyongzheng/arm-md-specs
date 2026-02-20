## C8.2.144 EXPAND

Copy lower-numbered vector elements to Active elements

This instruction copies consecutive elements from the source vector to Active elements of the destination vector, in increasing order of element number. Inactive elements in the destination vector register are set to zero.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled, or FEAT\_SME2p2 is implemented.

## SVE2

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

|   31 | 29 28   | 25 24   |   23 | 22   | 21   |   20 19 |     | 17 16   |   15 |   14 | 13 12   | 10 9   | 5 4   |
|------|---------|---------|------|------|------|---------|-----|---------|------|------|---------|--------|-------|
|    0 | 0 0     | 0 0 1 0 |    1 | size | 1 1  |       0 | 0 0 | 1 1     |    0 |    0 | Pg      | Zn     | Zd    |

## Encoding

```
EXPAND <Zd>.<T>, <Pg>, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

## &lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
if IsFeatureImplemented(FEAT_SME2p2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result; integer x = 0; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = Elem[operand1, x, esize]; x = x + 1; else Elem[result, e, esize] = Zeros(esize); Z[d, VL] = result;
```