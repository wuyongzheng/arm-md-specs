## C8.2.556 SABDLB

Signed absolute difference long (bottom)

This instruction computes the absolute difference between even-numbered signed integer values in elements of the second source vector and corresponding elements of the first source vector, and places the results in the overlapping double-width elements of the destination vector. This instruction is unpredicated.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SABDLB <Zd>.<T>, <Zn>.<Tb>, <Zm>.<Tb>
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

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant integer element1 = SInt(Elem[operand1, 2*e + 0, esize DIV 2]); constant integer element2 = SInt(Elem[operand2, 2*e + 0, esize DIV 2]); constant integer res = Abs(element1 - element2); Elem[result, e, esize] = res<esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | B        |
|     10 | H        |
|     11 | S        |