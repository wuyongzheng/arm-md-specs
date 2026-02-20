## C8.2.477 MSB

Multiply-subtract to multiplicand

This instruction multiplies the corresponding active elements of the first and second source vectors and subtracts the result from elements of the third (addend) vector. The results are destructively placed in the destination and first source (multiplicand) vector. Inactive elements in the destination vector register remain unmodified.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
MSB <Zdn>.<T>, <Pg>/M, <Zm>.<T>, <Za>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm); constant integer a = UInt(Za); constant boolean sub_op = TRUE;
```

## Assembler Symbols

&lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

&lt;Pg&gt;

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

<!-- image -->

&lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

<!-- image -->

Is the name of the third source scalable vector register, encoded in the 'Za' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); constant bits(VL) operand3 = if AnyActiveElement(mask, esize) then Z[a, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant integer element1 = UInt(Elem[operand1, e, esize]); constant integer element2 = UInt(Elem[operand2, e, esize]); constant integer product = element1 * element2; if sub_op then Elem[result, e, esize] = Elem[operand3, e, esize] product; else Elem[result, e, esize] = Elem[operand3, e, esize] + product; else Elem[result, e, esize] = Elem[operand1, e, esize]; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.