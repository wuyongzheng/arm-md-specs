## C8.2.171 FCPY

Copy floating-point immediate to vector elements (predicated)

This instruction copies a floating-point immediate into each Active element in the destination vector. Inactive elements in the destination vector register remain unmodified.

This instruction is used by the alias FMOV (immediate, predicated).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCPY <Zd>.<T>, <Pg>/M, #<const>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer d = UInt(Zd); constant bits(esize) imm = VFPExpandImm(imm8, esize);
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

<!-- image -->

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## &lt;const&gt;

Is a floating-point immediate value expressible as ±n÷16 × 2^r, where n and r are integers such that 16 ≤ n ≤ 31 and -3 ≤ r ≤ 4, i.e. a normalized binary floating-point encoding with 1 sign bit, 3-bit exponent, and 4-bit fractional part, encoded in the 'imm8' field.

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; bits(VL) result = Z[d, VL]; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = imm; Z[d, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

| Alias                        | Is preferred when   |
|------------------------------|---------------------|
| FMOV (immediate, predicated) | Unconditionally     |