## C8.2.167 FCMLA (vectors)

Floating-point complex multiply-add (predicated)

This instruction multiplies the duplicated real components for rotations 0 and 180, or imaginary components for rotations 90 and 270, of the floating-point complex numbers in the first source vector by the corresponding complex number in the second source vector rotated by 0, 90, 180 or 270 degrees in the direction from the positive real axis towards the positive imaginary axis, when considered in polar representation.

This instruction then destructively adds the products to the corresponding components of the complex numbers in the addend and destination vector, without intermediate rounding.

These transformations permit the creation of a variety of multiply-add and multiply-subtract operations on complex numbers by combining two of these instructions with the same vector operands but with rotations that are 90 degrees apart.

Each complex number is represented in a vector register as an even/odd pair of elements with the real part in the even-numbered element and the imaginary part in the odd-numbered element. Inactive elements in the destination vector register remain unmodified.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCMLA <Zda>.<T>, <Pg>/M, <Zn>.<T>, <Zm>.<T>, <const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer sel_a = UInt(rot<0>); constant integer sel_b = UInt(NOT(rot<0>)); constant boolean neg_i = (rot<1> == '1'); constant boolean neg_r = (rot<0> != rot<1>);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;T&gt;

Is the size specifier, encoded in 'size':

## &lt;Pg&gt;

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;const&gt;

Is the const specifier, encoded in 'rot':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer pairs = VL DIV (2 * esize); constant bits(PL) mask = P[g, PL]; constant bits(VL) op1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) op2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); constant bits(VL) op3 = Z[da, VL]; bits(VL) result; for p = 0 to pairs-1 bits(esize) addend_r = Elem[op3, 2 * p + 0, esize]; bits(esize) addend_i = Elem[op3, 2 * p + 1, esize]; if ActivePredicateElement(mask, 2 * p + 0, esize) then constant bits(esize) elt1_a = Elem[op1, 2*p + sel_a, esize]; constant bits(esize) elt2_a = (if neg_r then FPNeg(Elem[op2, 2 * p + sel_a, esize], FPCR) else Elem[op2, 2 * p + sel_a, esize]); addend_r = FPMulAdd(addend_r, elt1_a, elt2_a, FPCR); if ActivePredicateElement(mask, 2 * p + 1, esize) then constant bits(esize) elt1_a = Elem[op1, 2 * p + sel_a, esize]; constant bits(esize) elt2_b = (if neg_i then FPNeg(Elem[op2, 2 * p + sel_b, esize], FPCR) else Elem[op2, 2 * p + sel_b, esize]); addend_i = FPMulAdd(addend_i, elt1_a, elt2_b, FPCR); Elem[result, 2 * p + 0, esize] = addend_r; Elem[result, 2 * p + 1, esize] = addend_i; Z[da, VL] = result;
```

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

|   rot | <const>   |
|-------|-----------|
|    00 | #0        |
|    01 | #90       |
|    10 | #180      |
|    11 | #270      |

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.