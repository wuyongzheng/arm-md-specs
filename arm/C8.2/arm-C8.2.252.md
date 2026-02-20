## C8.2.252 FMULX

Floating-point multiply extended (predicated)

This instruction multiplies active floating-point elements of the first source vector by the corresponding floating-point elements of the second source vector except that ∞× 0.0 gives 2.0 instead of NaN, and destructively places the results in the corresponding elements of the first source vector. Inactive elements in the destination vector register remain unmodified.

The instruction can be used with FRECPX to safely convert arbitrary elements in mathematical vector space to unit vectors or direction vectors with length 1.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FMULX <Zdn>.<T>, <Pg>/M, <Zdn>.<T>, <Zm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer dn = UInt(Zdn); constant integer m = UInt(Zm);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the first source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

&lt;T&gt;

<!-- image -->

Is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand1 = Z[dn, VL]; constant bits(VL) operand2 = if AnyActiveElement(mask, esize) then Z[m, VL] else Zeros(VL); bits(VL) result; for e = 0 to elements-1 constant bits(esize) element1 = Elem[operand1, e, esize]; if ActivePredicateElement(mask, e, esize) then constant bits(esize) element2 = Elem[operand2, e, esize]; Elem[result, e, esize] = FPMulX(element1, element2, FPCR); else Elem[result, e, esize] = element1; Z[dn, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.