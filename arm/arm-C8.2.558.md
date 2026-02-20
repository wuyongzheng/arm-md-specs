## C8.2.558 SADALP

Signed add and accumulate long pairwise

This instruction adds pairs of adjacent signed integer values and accumulates the results into the overlapping double-width elements of the destination vector.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
SADALP <Zda>.<T>, <Pg>/M, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the second source and destination scalable vector register, encoded in the 'Zda' field.

<!-- image -->

## &lt;Pg&gt;

&lt;Zn&gt;

Is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Tb&gt;

Is the size specifier, encoded in 'size':

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand_acc = Z[da, VL]; constant bits(VL) operand_src = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 if !ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = Elem[operand_acc, e, esize]; else constant integer element1 = SInt(Elem[operand_src, 2*e + 0, esize DIV 2]); constant integer element2 = SInt(Elem[operand_src, 2*e + 1, esize DIV 2]); constant bits(esize) sum = (element1 + element2)<esize-1:0>; Elem[result, e, esize] = Elem[operand_acc, e, esize] + sum; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | B        |
|     10 | H        |
|     11 | S        |