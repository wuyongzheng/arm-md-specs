## C8.2.810 UCVTF (predicated)

Unsigned integer convert to floating-point (predicated)

This instruction converts to floating-point from the unsigned integer in each active element of the source vector, and places the results in the corresponding elements of the destination vector. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

If the input and result types have a different size the smaller type is held unpacked in the least significant bits of elements of the larger size. When the input is the smaller type the upper bits of each source element are ignored. When the result is the smaller type the results are zero-extended to fill each destination element.

It has encodings from 14 classes: 16-bit to half-precision, merging, 16-bit to half-precision, zeroing, 32-bit to half-precision, merging, 32-bit to half-precision, zeroing, 32-bit to single-precision, merging, 32-bit to single-precision, zeroing, 32-bit to double-precision, merging, 32-bit to double-precision, zeroing, 64-bit to half-precision, merging, 64-bit to half-precision, zeroing, 64-bit to single-precision, merging, 64-bit to single-precision, zeroing, 64-bit to double-precision, merging, and 64-bit to double-precision, zeroing

```
16-bit to half-precision, merging (FEAT_SVE || FEAT_SME)
```

<!-- image -->

## Encoding

```
UCVTF <Zd>.H, <Pg>/M, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 16; constant integer d_esize = 16; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

```
16-bit to half-precision, zeroing (FEAT_SVE2p2 || FEAT_SME2p2)
```

<!-- image -->

## Encoding

```
UCVTF <Zd>.H, <Pg>/Z, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 16; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 16; constant integer d_esize = 16; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## 32-bit to half-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UCVTF <Zd>.H, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 16; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## 32-bit to half-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
UCVTF <Zd>.H, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 16; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## 32-bit to single-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UCVTF <Zd>.S, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 32; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## 32-bit to single-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
UCVTF <Zd>.S, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 32; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## 32-bit to double-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UCVTF <Zd>.D, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 64; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## 32-bit to double-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
UCVTF <Zd>.D, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 64; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## 64-bit to half-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UCVTF <Zd>.H, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 16; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## 64-bit to half-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
UCVTF <Zd>.H, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 16; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## 64-bit to single-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UCVTF <Zd>.S, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 32; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## 64-bit to single-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
UCVTF <Zd>.S, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 32; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## 64-bit to double-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UCVTF <Zd>.D, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 64; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = TRUE;
```

## 64-bit to double-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
UCVTF <Zd>.D, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 64; constant boolean unsigned = TRUE; constant FPRounding rounding = FPRoundingMode(FPCR); constant boolean merging = FALSE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; constant bits(d_esize) fpval = FixedToFP(element<s_esize-1:0>, 0, unsigned, FPCR, rounding, d_esize); Elem[result, e, esize] = ZeroExtend(fpval, esize); Z[d, VL] = result;
```

## Operational Information

For the 16-bit to half-precision, merging, 32-bit to half-precision, merging, 32-bit to single-precision, merging, 32-bit to double-precision, merging, 64-bit to half-precision, merging, 64-bit to single-precision, merging, 64-bit to double-precision, merging variants:

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.