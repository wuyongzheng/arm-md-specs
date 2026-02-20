## C8.2.121 CPY (scalar)

Copy general-purpose register to vector elements (predicated)

This instruction copies the general-purpose scalar source register to each Active element in the destination vector. Inactive elements in the destination vector register remain unmodified.

This instruction is used by the alias MOV (scalar, predicated).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
CPY <Zd>.<T>, <Pg>/M, <R><n|SP>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Rn); constant integer d = UInt(Zd);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Pg&gt;

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is a width specifier, encoded in 'size':

## &lt;n|SP&gt;

Is the number [0-30] of the general-purpose source register or the name SP (31), encoded in the 'Rn' field.

## Alias Conditions

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; bits(VL) result = Z[d, VL]; if AnyActiveElement(mask, esize) then bits(64) operand1; if n == 31 then operand1 = SP[64]; else operand1 = X[n, 64]; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then Elem[result, e, esize] = operand1<esize-1:0>; Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of this instruction.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |
|     10 | W     |
|     11 | X     |

| Alias                    | Is preferred when   |
|--------------------------|---------------------|
| MOV (scalar, predicated) | Unconditionally     |