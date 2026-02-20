## C8.2.887 URSHR

Unsigned rounding shift right by immediate

This instruction shifts right by immediate each active unsigned element of the source vector, and destructively places the rounded results in the corresponding elements of the source vector. The immediate shift amount is an unsigned value in the range 1 to number of bits per element. Inactive elements in the destination vector register remain unmodified.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
URSHR <Zdn>.<T>, <Pg>/M, <Zdn>.<T>, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant bits(4) tsize = tszh:tszl; if tsize == '0000' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << HighestSetBitNZ(tsize); constant integer g = UInt(Pg); constant integer dn = UInt(Zdn); constant integer shift = (2 * esize) UInt(tsize:imm3);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

<!-- image -->

Is the size specifier, encoded in 'tszh:tszl':

| tszh   | tszl   | <T>      |
|--------|--------|----------|
| 00     | 00     | RESERVED |
| 00     | 01     | B        |
| 00     | 1x     | H        |
| 01     | xx     | S        |
| 1x     | xx     | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;const&gt;

Is the immediate shift amount, in the range 1 to number of bits per element, encoded in 'tszh:tszl:imm3'.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[dn, VL]; constant bits(PL) mask = P[g, PL]; bits(VL) result; for e = 0 to elements-1 constant integer element1 = UInt(Elem[operand1, e, esize]); if ActivePredicateElement(mask, e, esize) then constant integer res = (element1 + (1 << (shift - 1))) >> Elem[result, e, esize] = res<esize-1:0>; else Elem[result, e, esize] = Elem[operand1, e, esize]; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
shift;
```