## C8.2.93 CADD

## Complex integer add

This instruction adds the real and imaginary components of the integral complex numbers from the first source vector to the complex numbers from the second source vector that have first been rotated by 90 or 270 degrees in the direction from the positive real axis towards the positive imaginary axis, when considered in polar representation, equivalent to multiplying the complex numbers in the second source vector by ±j beforehand. The results are destructively placed in the corresponding elements of the first source vector. This instruction is unpredicated.

Each complex number is represented in a vector register as an even/odd pair of elements with the real part in the even-numbered element and the imaginary part in the odd-numbered element.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
CADD <Zdn>.<T>, <Zdn>.<T>, <Zm>.<T>, <const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer m = UInt(Zm); constant integer dn = UInt(Zdn); constant boolean sub_i = (rot == '0'); constant boolean sub_r = (rot == '1');
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'size':

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;const&gt;

Is the const specifier, encoded in 'rot':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer pairs = VL DIV (2 * esize); constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = Z[m, VL]; bits(VL) result; for p = 0 to pairs-1 integer acc_r = SInt(Elem[operand1, 2 * p + 0, esize]); integer acc_i = SInt(Elem[operand1, 2 * p + 1, esize]); constant integer elt2_r = SInt(Elem[operand2, 2 * p + 0, constant integer elt2_i = SInt(Elem[operand2, 2 * p + 1, if sub_i then acc_r = acc_r - elt2_i; acc_i = acc_i + elt2_r; if sub_r then acc_r = acc_r + elt2_i; acc_i = acc_i - elt2_r; Elem[result, 2 * p + 0, esize] = acc_r<esize-1:0>; Elem[result, 2 * p + 1, esize] = acc_i<esize-1:0>; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   rot | <const>   |
|-------|-----------|
|     0 | #90       |
|     1 | #270      |

```
esize]); esize]);
```