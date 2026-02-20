## C8.2.906 UZPQ2

Concatenate odd elements within each pair of quadword vector segments

This instruction concatenates adjacent odd-numbered elements from the corresponding 128-bit vector segments of the first and second source vectors and places in elements of the corresponding destination vector segment. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2p1 || FEAT\_SME2p1)

<!-- image -->

## Encoding

```
UZPQ2 <Zd>.<T>, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p1) && !IsFeatureImplemented(FEAT_SME2p1) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer part = 1;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

## &lt;Zn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV 128; constant integer elements = 128 DIV esize; constant integer pairs = elements DIV 2; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for s = 0 to segments-1 constant integer soff = s * elements; for p = 0 to pairs-1 Elem[result, soff + p, esize] = Elem[operand1, soff + 2 * p + part, esize]; for p = 0 to pairs-1 Elem[result, soff + pairs + p, esize] = Elem[operand2, soff + 2 * p + part, esize]; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.