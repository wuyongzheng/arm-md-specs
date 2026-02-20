## C8.2.901 UUNPKHI, UUNPKLO

Unsigned unpack and extend half of vector

This instruction unpacks elements from the lowest or highest half of the source vector and then zero-extends them to place in elements of twice their size within the destination vector. This instruction is unpredicated.

It has encodings from 2 classes: High half and Low half

## High half

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UUNPKHI <Zd>.<T>, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean unsigned = TRUE; constant boolean hi = TRUE;
```

## Low half

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UUNPKLO <Zd>.<T>, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean unsigned = TRUE; constant boolean hi = FALSE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

&lt;Zn&gt;

&lt;Tb&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer hsize = esize DIV 2; constant integer offset = if hi then elements else 0; constant bits(VL) operand = Z[n, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(hsize) element = Elem[operand, e + offset, hsize]; Elem[result, e, esize] = Extend(element, esize, unsigned); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | B        |
|     10 | H        |
|     11 | S        |