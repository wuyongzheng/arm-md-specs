## C8.2.94 CDOT (vectors)

## Complex integer dot product

This instruction delimits the source vectors into pairs of 8-bit or 16-bit signed integer complex numbers. Within each pair, the complex numbers in the first source vector are multiplied by the corresponding complex numbers in the second source vector and the resulting wide real or wide imaginary part of the product is accumulated into a 32-bit or 64-bit destination vector element that overlaps all four of the elements that comprise a pair of complex number values in the first source vector.

As a result each instruction implicitly deinterleaves the real and imaginary components of their complex number inputs, so that the destination vector accumulates 4 × wide real sums or 4 × wide imaginary sums.

The complex numbers in the second source vector are rotated by 0, 90, 180 or 270 degrees in the direction from the positive real axis towards the positive imaginary axis, when considered in polar representation, by performing the following transformations prior to the dot product operations:

- If the rotation is #0, the imaginary parts of the complex numbers in the second source vector are negated. The destination vector therefore accumulates the real parts of a complex dot product.
- If the rotation is #90, the real and imaginary parts of the complex numbers the second source vector are swapped. The destination vector therefore accumulates the imaginary parts of a complex dot product.
- If the rotation is #180, there is no transformation. The destination vector therefore accumulates the real parts of a complex conjugate dot product.
- If the rotation is #270, the real parts of the complex numbers in the second source vector are negated and then swapped with the imaginary parts. The destination vector therefore accumulates the imaginary parts of a complex conjugate dot product.

Each complex number is represented in a vector register as an even/odd pair of elements with the real part in the even-numbered element and the imaginary part in the odd-numbered element.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

| 31   | 29 28                     | 25 24 23 22 21 20 16 15 14 12 11 10 9 5 4   |
|------|---------------------------|---------------------------------------------|
| 0 1  | 0 0 0 1 0 0 size 0 Zm 0 0 | 0 1 rot Zn Zda                              |

## Encoding

```
CDOT <Zda>.<T>, <Zn>.<Tb>, <Zm>.<Tb>, <const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size IN {'0x'} then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel_a = UInt(rot<0>); constant integer sel_b = UInt(NOT(rot<0>)); constant boolean sub_i = (rot<0> == rot<1>);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;T&gt;

## &lt;Zn&gt;

## &lt;Tb&gt;

Is the size specifier, encoded in 'size&lt;0&gt;':

|   size<0> | <T>   |
|-----------|-------|
|         0 | S     |
|         1 | D     |

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size&lt;0&gt;':

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;const&gt;

Is the const specifier, encoded in 'rot':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL];
```

```
esize; bits(VL) result;
```

|   size<0> | <Tb>   |
|-----------|--------|
|         0 | B      |
|         1 | H      |

|   rot | <const>   |
|-------|-----------|
|    00 | #0        |
|    01 | #90       |
|    10 | #180      |
|    11 | #270      |

```
for e = 0 to elements-1 bits(esize) res = Elem[operand3, e, esize]; for i = 0 to 1 constant integer elt1_r = SInt(Elem[operand1, 4 * e + 2 * i + 0, esize DIV 4]); constant integer elt1_i = SInt(Elem[operand1, 4 * e + 2 * i + 1, esize DIV 4]); constant integer elt2_a = SInt(Elem[operand2, 4 * e + 2 * i + sel_a, esize DIV 4]); constant integer elt2_b = SInt(Elem[operand2, 4 * e + 2 * i + sel_b, esize DIV 4]); if sub_i then res = (res + (elt1_r * elt2_a)) - (elt1_i * elt2_b); else res = res + (elt1_r * elt2_a) + (elt1_i * elt2_b); Elem[result, e, esize] = res; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.