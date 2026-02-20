## C8.2.642 SQDMULLT (vectors)

Signed saturating doubling multiply (top)

This instruction multiplies the corresponding odd-numbered signed elements of the first and second source vectors, then doubles and places the results in the overlapping double-width elements of the destination vector. Each result element is saturated to the double-width N-bit element's signed integer range -2 (N-1) to (2 (N-1) )-1. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SQDMULLT <Zd>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Tb&gt;

Is the size specifier, encoded in 'size':

<!-- image -->

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, 2*e + 1, esize DIV 2]); constant integer element2 = SInt(Elem[operand2, 2*e + 1, esize DIV 2]); constant integer res = 2 * element1 * element2; Elem[result, e, esize] = SignedSat(res, esize); Z[d, VL] = result;
```

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | B        |
|     10 | H        |
|     11 | S        |