## C8.2.61 BFMLS (vectors)

BFloat16 fused multiply-subtract

This instruction multiplies the corresponding active BFloat16 elements of the first and second source vectors. The results are then subtracted from elements of the third source (addend) vector without intermediate rounding and destructively placed in the destination and third source (addend) vector. Inactive elements in the destination vector register remain unmodified.

This instruction follows SVE2 non-widening BFloat16 numerical behaviors.

ID\_AA64ZFR0\_EL1.B16B16 indicates whether this instruction is implemented.

## SVE2

(FEAT\_SVE\_B16B16)

<!-- image -->

## Encoding

```
BFMLS <Zda>.H, <Pg>/M, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE_B16B16) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean op1_neg = TRUE; constant boolean op3_neg = FALSE;
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

&lt;Pg&gt;

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## Operation

```
if IsFeatureImplemented(FEAT_SME2) then CheckSVEEnabled(); else CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV 16; constant bits(PL) mask = P[g, PL]; constant bits(VL) op1 = if AnyActiveElement(mask, 16) then Z[n, VL] else Zeros(VL); constant bits(VL) op2 = if AnyActiveElement(mask, 16) then Z[m, VL] else Zeros(VL); constant bits(VL) op3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 if ActivePredicateElement(mask, e, 16) then constant bits(16) elem1 = if op1_neg then BFNeg(Elem[op1, e, 16]) else Elem[op1, e, 16]; constant bits(16) elem2 = Elem[op2, e, 16]; constant bits(16) elem3 = if op3_neg then BFNeg(Elem[op3, e, 16]) else Elem[op3, e, 16]; Elem[result, e, 16] = BFMulAdd(elem3, elem1, elem2, FPCR); else Elem[result, e, 16] = Elem[op3, e, 16]; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.