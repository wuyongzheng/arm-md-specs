## C8.2.455 MLA (vectors)

Multiply-add (predicated)

This instruction multiplies the corresponding active elements of the first and second source vectors and adds the result to elements of the third source (addend) vector. The results are destructively placed in the destination and third source (addend) vector. Inactive elements in the destination vector register remain unmodified.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MLA <Zda>.<T>, <Pg>/M, <Zn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean sub_op = FALSE;
```

## Assembler Symbols

&lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

<!-- image -->

&lt;Pg&gt;

<!-- image -->

&lt;Zn&gt;

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant integer element1 = UInt(Elem[operand1, e, esize]); constant integer element2 = UInt(Elem[operand2, e, esize]); constant integer product = element1 * element2; if sub_op then Elem[result, e, esize] = Elem[operand3, e, esize] product; else Elem[result, e, esize] = Elem[operand3, e, esize] + product; else Elem[result, e, esize] = Elem[operand3, e, esize]; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.