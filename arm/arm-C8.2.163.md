## C8.2.163 FCADD

Floating-point complex add (predicated)

This instruction adds the real and imaginary components of the active floating-point complex numbers from the first source vector to the complex numbers from the second source vector that have first been rotated by 90 or 270 degrees in the direction from the positive real axis towards the positive imaginary axis, when considered in polar representation, equivalent to multiplying the complex numbers in the second source vector by ±j beforehand. The results are destructively placed in the corresponding elements of the first source vector. Inactive elements in the destination vector register remain unmodified.

Each complex number is represented in a vector register as an even/odd pair of elements with the real part in the even-numbered element and the imaginary part in the odd-numbered element.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCADD <Zdn>.<T>, <Pg>/M, <Zdn>.<T>, <Zm>.<T>, <const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm); constant boolean sub_i = (rot == '0'); constant boolean sub_r = (rot == '1');
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

&lt;Pg&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## &lt;const&gt;

Is the const specifier, encoded in 'rot':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer pairs = VL DIV (2 * esize); constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(VL) result; for p = 0 to pairs-1 bits(esize) acc_r = Elem[operand1, 2 * p + 0, esize]; bits(esize) acc_i = Elem[operand1, 2 * p + 1, esize]; if ActivePredicateElement(mask, 2 * p + 0, esize) then bits(esize) elt2_i = Elem[operand2, 2 * p + 1, esize]; if sub_i then elt2_i = FPNeg(elt2_i, FPCR); acc_r = FPAdd(acc_r, elt2_i, FPCR); if ActivePredicateElement(mask, 2 * p + 1, esize) then bits(esize) elt2_r = Elem[operand2, 2 * p + 0, esize]; if sub_r then elt2_r = FPNeg(elt2_r, FPCR); acc_i = FPAdd(acc_i, elt2_r, FPCR); Elem[result, 2 * p + 0, esize] = acc_r; Elem[result, 2 * p + 1, esize] = acc_i; Z[dn, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   rot | <const>   |
|-------|-----------|
|     0 | #90       |
|     1 | #270      |