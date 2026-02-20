## C8.2.51 BFMAX

BFloat16 maximum (predicated)

This instruction determines the maximum of active BFloat16 elements of the second source vector and the corresponding BFloat16 elements of the first source vector and destructively places the results in the corresponding elements of the first source vector.

When FPCR.AH is 0, the behavior is as follows:

- Negative zero compares less than positive zero.
- When FPCR.DN is 0, if either element is a NaN, the result is a quiet NaN.
- When FPCR.DN is 1, if either element is a NaN, the result is Default NaN.

When FPCR.AH is 1, the behavior is as follows:

- If both elements are zeros, regardless of the sign of either zero, the result is the second element.
- If either element is a NaN, regardless of the value of FPCR.DN, the result is the second element.

Inactive elements in the destination vector register remain unmodified.

This instruction follows SVE2 non-widening BFloat16 numerical behaviors.

ID\_AA64ZFR0\_EL1.B16B16 indicates whether this instruction is implemented.

## SVE2

(FEAT\_SVE\_B16B16)

<!-- image -->

## Encoding

```
BFMAX <Zdn>.H, <Pg>/M, <Zdn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_B16B16) then constant integer g = UInt(Pg); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

## &lt;Pg&gt;

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

```
EndOfDecode(Decode_UNDEF);
```

## Operation

```
if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV 16; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = if AnyActiveElement(mask, 16) then Z[m, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 constant bits(16) element1 = Elem[operand1, e, 16]; if ActivePredicateElement(mask, e, 16) then constant bits(16) element2 = Elem[operand2, e, 16]; Elem[result, e, 16] = BFMax(element1, element2, FPCR); else Elem[result, e, 16] = element1; Z[dn, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.