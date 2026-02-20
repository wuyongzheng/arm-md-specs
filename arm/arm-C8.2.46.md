## C8.2.46 BFCVT

Single-precision convert to BFloat16 (predicated)

This instruction converts to BFloat16 from single-precision in each active floating-point element of the source vector, and places the results in the corresponding elements of the destination vector. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

Since the result type is smaller than the input type, the results are zero-extended to fill each destination element.

ID\_AA64ZFR0\_EL1.BF16 indicates whether this instruction is implemented.

It has encodings from 2 classes: Merging and Zeroing

## Merging

((FEAT\_SVE || FEAT\_SME) &amp;&amp; FEAT\_BF16)

<!-- image -->

## Encoding

```
BFCVT <Zd>.H, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME)) || !IsFeatureImplemented(FEAT_BF16)) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = TRUE;
```

## Zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
BFCVT <Zd>.H, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = FALSE;
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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV 32; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, 32) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, 32) then constant bits(32) element = Elem[operand, e, 32]; Elem[result, 2*e, 16] = FPConvertBF(element, FPCR); Elem[result, 2*e+1, 16] = Zeros(16); Z[d, VL] = result;
```

## Operational Information

For the Merging variant:

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.