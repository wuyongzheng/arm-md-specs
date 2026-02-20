## C8.2.172 FCVT

Floating-point convert (predicated)

This instruction converts the size and precision of each active floating-point element of the source vector, and places the results in the corresponding elements of the destination vector. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

Since the input and result types have a different size the smaller type is held unpacked in the least significant bits of elements of the larger size. When the input is the smaller type the upper bits of each source element are ignored. When the result is the smaller type the results are zero-extended to fill each destination element.

It has encodings from 12 classes: Half-precision to single-precision, merging, Half-precision to single-precision, zeroing, Half-precision to double-precision, merging, Half-precision to double-precision, zeroing, Single-precision to half-precision, merging, Single-precision to half-precision, zeroing, Single-precision to double-precision, merging, Single-precision to double-precision, zeroing, Double-precision to half-precision, merging, Double-precision to half-precision, zeroing, Double-precision to single-precision, merging, and Double-precision to single-precision, zeroing

## Half-precision to single-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVT <Zd>.S, <Pg>/M, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 16; constant integer d_esize = 32; constant boolean merging = TRUE;
```

Half-precision to single-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVT <Zd>.S, <Pg>/Z, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 16; constant integer d_esize = 32; constant boolean merging = FALSE;
```

Half-precision to double-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVT <Zd>.D, <Pg>/M, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 16; constant integer d_esize = 64; constant boolean merging = TRUE;
```

Half-precision to double-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVT <Zd>.D, <Pg>/Z, <Zn>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 16; constant integer d_esize = 64; constant boolean merging = FALSE;
```

Single-precision to half-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVT <Zd>.H, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 16; constant boolean merging = TRUE;
```

Single-precision to half-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVT <Zd>.H, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 16; constant boolean merging = FALSE;
```

Single-precision to double-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVT <Zd>.D, <Pg>/M, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 64; constant boolean merging = TRUE;
```

Single-precision to double-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVT <Zd>.D, <Pg>/Z, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 32; constant integer d_esize = 64; constant boolean merging = FALSE;
```

Double-precision to half-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVT <Zd>.H, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 16; constant boolean merging = TRUE;
```

Double-precision to half-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVT <Zd>.H, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 16; constant boolean merging = FALSE;
```

Double-precision to single-precision, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVT <Zd>.S, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 32; constant boolean merging = TRUE;
```

Double-precision to single-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVT <Zd>.S, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 32; constant boolean merging = FALSE;
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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; constant bits(d_esize) res = FPConvertSVE(element<s_esize-1:0>, FPCR, d_esize); Elem[result, e, esize] = ZeroExtend(res, esize); Z[d, VL] = result;
```

## Operational Information

For the Half-precision to single-precision, merging, Half-precision to double-precision, merging, Single-precision to half-precision, merging, Single-precision to double-precision, merging, Double-precision to half-precision, merging, Double-precision to single-precision, merging variants:

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.