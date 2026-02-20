## C8.2.8 ADDHNT

Add narrow high part (top)

This instruction adds each vector element of the first source vector to the corresponding vector element of the second source vector, and places the most significant half of the result in the odd-numbered half-width destination elements, leaving the even-numbered elements unchanged. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
ADDHNT <Zd>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
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
|     01 | B        |
|     10 | H        |
|     11 | S        |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Tb&gt;

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result = Z[d, VL]; constant integer halfesize = esize DIV 2; for e = 0 to elements-1 constant integer element1 = UInt(Elem[operand1, e, esize]); constant integer element2 = UInt(Elem[operand2, e, esize]); constant integer res = (element1 + element2) >> halfesize; Elem[result, 2*e + 1, halfesize] = res<halfesize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |