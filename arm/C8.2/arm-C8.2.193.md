## C8.2.193 FLOGB

Floating-point base 2 logarithm as integer

This instruction returns the signed integer base 2 logarithm of each floating-point input element |x| after normalization.

This is the unbiased exponent of x used in the representation of the floating-point value, such that, for positive x, x = significand × 2 exponent .

The integer results are placed in elements of the destination vector that have the same width (esize) as the floating-point input elements:

- If x is normal, the result is the base 2 logarithm of x.
- If x is subnormal, the result corresponds to the normalized representation.
- If x is infinite, the result is 2 (esize-1) -1.
- If x is ±0.0 or NaN, the result is -2 (esize-1) .

Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

It has encodings from 2 classes: Merging and Zeroing

## Merging

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
FLOGB <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = TRUE;
```

## Zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FLOGB <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant boolean merging = FALSE;
```

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

&lt;Pg&gt;

&lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then constant bits(esize) element = Elem[operand, e, esize]; Elem[result, e, esize] = FPLogB(element, FPCR); Z[d, VL] = result;
```

## Operational Information

For the Merging variant:

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.