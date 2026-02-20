## C8.2.826 UMIN (immediate)

Unsigned minimum with immediate (unpredicated)

This instruction determines the unsigned minimum of an immediate and each element of the source vector, and destructively places the results in the corresponding elements of the source vector. The immediate is an unsigned 8-bit value in the range 0 to 255, inclusive. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UMIN <Zdn>.<T>, <Zdn>.<T>, #<imm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn); constant boolean unsigned = TRUE; constant integer imm = if unsigned then UInt(imm8) else SInt(imm8);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

Is the size specifier, encoded in 'size':

## &lt;imm&gt;

Is the unsigned immediate operand, in the range 0 to 255, encoded in the 'imm8' field.

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) operand1 = Z[dn, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) op1elt = Elem[operand1, e, esize]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); Elem[result, e, esize] = Min(element1, imm)<esize-1:0>; Z[dn, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.