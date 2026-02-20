## C8.2.265 FRINT&lt;r&gt;

Floating-point round to integral value (predicated)

This instruction rounds to an integral floating-point value with the specified rounding option from each active floating-point element of the source vector, and places the results in the corresponding elements of the destination vector. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

| <r>   | Rounding Option                                |
|-------|------------------------------------------------|
| N     | to nearest, with ties to even                  |
| A     | to nearest, with ties away from zero           |
| M     | toward minus Infinity                          |
| P     | toward plus Infinity                           |
| Z     | toward zero                                    |
| I     | current FPCR rounding mode                     |
| X     | current FPCR rounding mode, signalling inexact |

It has encodings from 14 classes: Current mode signalling inexact, merging, Current mode signalling inexact, zeroing, Current mode, merging, Current mode, zeroing, Nearest with ties to away, merging, Nearest with ties to away, zeroing, Nearest with ties to even, merging, Nearest with ties to even, zeroing, Toward zero, merging, Toward zero, zeroing, Toward minus infinity, merging, Toward minus infinity, zeroing, Toward plus infinity, merging, and Toward plus infinity, zeroing

## Current mode signalling inexact, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRINTX <Zd>.<T>,
```

```
<Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## Current mode signalling inexact, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTX <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## Current mode, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRINTI <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## Current mode, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTI <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## Nearest with ties to away, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRINTA <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_TIEAWAY; constant boolean merging = TRUE;
```

## Nearest with ties to away, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTA <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_TIEAWAY; constant boolean merging = FALSE;
```

## Nearest with ties to even, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRINTN <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_TIEEVEN; constant boolean merging = TRUE;
```

## Nearest with ties to even, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTN <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_TIEEVEN; constant boolean merging = FALSE;
```

```
Toward zero, merging (FEAT_SVE || FEAT_SME)
```

<!-- image -->

## Encoding

```
FRINTZ <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_ZERO; constant boolean merging = TRUE;
```

## Toward zero, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTZ <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_ZERO; constant boolean merging = FALSE;
```

## Toward minus infinity, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRINTM <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_NEGINF; constant boolean merging = TRUE;
```

## Toward minus infinity, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTM <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_NEGINF; constant boolean merging = FALSE;
```

## Toward plus infinity, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FRINTP <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_POSINF; constant boolean merging = TRUE;
```

## Toward plus infinity, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FRINTP <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean exact = FALSE; constant FPRounding rounding = FPRounding_POSINF; constant boolean merging = FALSE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Pg&gt;

&lt;Zn&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; Elem[result, e, esize] = FPRoundInt(element, FPCR, rounding, exact); Z[d, VL] = result;
```

## Operational Information

For the Current mode signalling inexact, merging, Current mode, merging, Nearest with ties to away, merging, Nearest with ties to even, merging, Toward zero, merging, Toward minus infinity, merging, Toward plus infinity, merging variants:

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.