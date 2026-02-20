## C8.2.178 FCVTX

Double-precision convert to single-precision, rounding to odd (predicated)

This instruction converts active double-precision elements from the source vector to single-precision, rounding to Odd, and places the results in the even-numbered 32-bit elements of the destination vector, while setting the odd-numbered elements to zero. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

Rounding to Odd (aka Von Neumann rounding) permits a two-step conversion from double-precision to half-precision without incurring intermediate rounding errors.

It has encodings from 2 classes: Double-precision to single-precision, merging and Double-precision to single-precision, zeroing

## Double-precision to single-precision, merging

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
FCVTX <Zd>.S, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer s_esize = 64; constant integer d_esize = 32; constant boolean merging = TRUE;
```

Double-precision to single-precision, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FCVTX <Zd>.S, <Pg>/Z, <Zn>.D
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
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; constant bits(d_esize) res = FPConvertSVE(element<s_esize-1:0>, FPCR, FPRounding_ODD, d_esize); Elem[result, e, esize] = ZeroExtend(res, esize); Z[d, VL] = result;
```

## Operational Information

For the Double-precision to single-precision, merging variant:

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.