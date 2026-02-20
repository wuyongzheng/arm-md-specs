## C8.2.512 PMULLT

Polynomial multiply long (top)

This instruction performs a polynomial multiplication over [0, 1] of the corresponding odd-numbered elements of the first and second source vectors, and places the results in the overlapping double-width elements of the destination vector. This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.AES indicates whether the 128-bit element variant is implemented. The 128-bit element variant is legal when executed in Streaming SVE mode if one of the following is true:

- Both FEAT\_SSVE\_AES and FEAT\_SVE\_PMULL128 are implemented.
- FEAT\_SME\_FA64 is implemented and enabled.

It has encodings from 2 classes: 16-bit or 64-bit elements and 128-bit element

```
16-bit or 64-bit elements (FEAT_SVE2 || FEAT_SME)
```

<!-- image -->

## Encoding

```
PMULLT <Zd>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size<0> == '0' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## 128-bit element

```
(FEAT_SVE_PMULL128)
```

<!-- image -->

## Encoding

```
PMULLT <Zd>.Q, <Zn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_PMULL128) then EndOfDecode(Decode_UNDEF); constant integer esize = 128; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

&lt;Zn&gt;

&lt;Tb&gt;

| size   | <T>   |
|--------|-------|
| 01     | H     |
| 1x     | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size':

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
if esize == 128 then if IsFeatureImplemented(FEAT_SSVE_AES) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); else CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize DIV 2) element1 = Elem[operand1, 2*e + 1, esize DIV
```

```
2]; constant bits(esize DIV 2) element2 = Elem[operand2, 2*e + 1, esize DIV 2];
```

| size   | <Tb>   |
|--------|--------|
| 01     | B      |
| 1x     | S      |

```
Elem[result, e, esize] = PolynomialMult(element1, element2); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.