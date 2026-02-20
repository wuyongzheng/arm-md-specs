## C8.2.791 TBL

Programmable table lookup in one or two vector table (zeroing)

This instruction reads each element of the second source (index) vector and uses its value to select an indexed element from a table of elements consisting of one or two consecutive vector registers, where the first or only vector holds the lower numbered elements, and places the indexed table element in the destination vector element corresponding to the index vector element. If an index value is greater than or equal to the number of vector elements, then it places zero in the corresponding destination vector element.

Since the index values can select any element in a vector this operation is not naturally vector length agnostic.

It has encodings from 2 classes: Single register table and Two register table

```
Single register table (FEAT_SVE || FEAT_SME)
```

<!-- image -->

## Encoding

```
TBL <Zd>.<T>, { <Zn>.<T> }, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant boolean double_table = FALSE;
```

## Two register table

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
TBL <Zd>.<T>, { <Zn1>.<T>, <Zn2>.<T> }, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant boolean double_table = TRUE;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

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

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the first source multi-vector group, encoded in the 'Zn' field.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the first source multi-vector group, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) indexes = Z[m, VL]; bits(VL) result; constant integer table_size = if double_table then VL*2 else VL; constant integer table_elems = table_size DIV esize; bits(table_size) table; if double_table then constant bits(VL) top = Z[(n + 1) MOD 32, VL]; constant bits(VL) bottom = Z[n, VL]; table = (top:bottom)<table_size-1:0>; else table = Z[n, table_size]; for e = 0 to elements-1 constant integer idx = UInt(Elem[indexes, e, esize]); Elem[result, e, esize] = if idx < table_elems then Elem[table, idx, esize] else Zeros(esize); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.