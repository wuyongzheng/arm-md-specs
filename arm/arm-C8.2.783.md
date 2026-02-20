## C8.2.783 SUBPT (predicated)

Subtract checked pointer vectors (predicated)

This instruction subtracts, with pointer check, Active elements of the second source vector from corresponding elements of the first source vector and destructively places the results in the corresponding elements of the first source vector. Inactive elements in the destination vector register remain unmodified.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE2

(FEAT\_SVE &amp;&amp; FEAT\_CPA)

<!-- image -->

## Encoding

```
SUBPT <Zdn>.D, <Pg>/M, <Zdn>.D, <Zm>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) || !IsFeatureImplemented(FEAT_CPA) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Pg&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV 64; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = if AnyActiveElement(mask, 64) then Z[m, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 constant bits(64) element1 = Elem[operand1, e, 64]; constant bits(64) element2 = Elem[operand2, e, 64]; if ActivePredicateElement(mask, e, 64) then constant bits(64) res = element1 - element2; Elem[result, e, 64] = PointerAddCheck(res, element1);
```

```
else Elem[result, e, 64] = Elem[operand1, e, 64]; Z[dn, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.