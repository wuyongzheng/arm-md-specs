## C8.2.442 LSL (wide elements, unpredicated)

Logical shift left by 64-bit wide elements (unpredicated)

This instruction shifts left all elements of the first source vector by the corresponding overlapping 64-bit elements of the second source vector and places the first in the corresponding elements of the destination vector. The shift amount is a vector of unsigned 64-bit doubleword elements in which all bits are significant, and not used modulo the destination element size. Inactive elements in the destination vector register remain unmodified.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
LSL <Zd>.<T>, <Zn>.<T>, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;T&gt;

&lt;Zn&gt;

|   size | <T>      |
|--------|----------|
|     00 | B        |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

<!-- image -->

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; constant bits(64) element2 = Elem[operand2, (e * esize) constant integer shift = Min(UInt(element2), esize); Elem[result, e, esize] = LSL(element1, shift); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
DIV 64, 64];
```