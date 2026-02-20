## C8.2.546 REVB, REVH, REVW

Reverse bytes / halfwords / words within elements (predicated)

This instruction reverses the order of 8-bit bytes, 16-bit halfwords or 32-bit words within each active element of the source vector, and places the results in the corresponding elements of the destination vector. Inactive elements in the destination vector register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected.

It has encodings from 6 classes: Byte, merging, Byte, zeroing, Halfword, merging, Halfword, zeroing, Word, merging, and Word, zeroing

## Byte, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
REVB <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer swsize = 8; constant boolean merging = TRUE;
```

## Byte, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
REVB <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer swsize = 8; constant boolean merging = FALSE;
```

## Halfword, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
REVH <Zd>.<T>, <Pg>/M, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size IN {'0x'} then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer swsize = 16; constant boolean merging = TRUE;
```

## Halfword, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
REVH <Zd>.<T>, <Pg>/Z, <Zn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size IN {'0x'} then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer swsize = 16; constant boolean merging = FALSE;
```

## Word, merging

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
REVW <Zd>.D, <Pg>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); if size != '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer swsize = 32; constant boolean merging = TRUE;
```

## Word, zeroing

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
REVW <Zd>.D, <Pg>/Z, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); if size != '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Zn); constant integer d = UInt(Zd); constant integer swsize = 32; constant boolean merging = FALSE;
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

For the 'Byte, merging' and 'Byte, zeroing' variants: is the size specifier, encoded in 'size':

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

For the 'Halfword, merging' and 'Halfword, zeroing' variants: is the size specifier, encoded in 'size&lt;0&gt;':

|   size<0> | <T>   |
|-----------|-------|
|         0 | S     |
|         1 | D     |

Is the name of the governing scalable predicate register P0-P7, encoded in the 'Pg' field.

&lt;T&gt;

## &lt;Pg&gt;

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(VL) operand = if AnyActiveElement(mask, esize) then Z[n, VL] else Zeros(VL); bits(VL) result = if merging then Z[d, VL] else Zeros(VL); for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) then
```

```
constant bits(esize) element = Elem[operand, e, esize]; Elem[result, e, esize] = Reverse(element, swsize); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

The merging variant of this instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and the merging variant of this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX can be predicated or unpredicated.
- Apredicated MOVPRFX must use the same governing predicate register as the merging variant this instruction.
- Apredicated MOVPRFX must use the larger of the destination element size and first source element size in the preferred disassembly of the merging variant of this instruction.
- The MOVPRFX must specify the same destination register as the merging variant of this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of the merging variant of this instruction.