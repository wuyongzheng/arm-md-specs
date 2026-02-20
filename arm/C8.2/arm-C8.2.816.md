## C8.2.816 UDOT (4-way, indexed)

Unsigned integer dot product by indexed element (four-way)

This instruction computes the dot product of a group of four unsigned 8-bit or 16-bit integer values held in each 32-bit or 64-bit element of the first source vector multiplied by a group of four unsigned 8-bit or 16-bit integer values in an indexed 32-bit or 64-bit element of the second source vector, and then destructively adds the widened dot product to the corresponding 32-bit or 64-bit element of the destination vector.

The groups within the second source vector are specified using an immediate index that selects the same group position within each 128-bit vector segment. The index range is from 0 to one less than the number of groups per 128-bit segment.

This instruction is unpredicated.

It has encodings from 2 classes: 8-bit to 32-bit and 16-bit to 64-bit

```
8-bit to 32-bit
```

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
UDOT <Zda>.S, <Zn>.B, <Zm>.B[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer index = UInt(i2); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

```
16-bit to 64-bit (FEAT_SVE || FEAT_SME)
```

<!-- image -->

## Encoding

```
UDOT <Zda>.D, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer index = UInt(i1); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

For the '8-bit to 32-bit' variant: is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

For the '16-bit to 64-bit' variant: is the name of the second source scalable vector register Z0-Z15, encoded in the 'Zm' field.

## &lt;imm&gt;

For the '8-bit to 32-bit' variant: is the immediate index of a 32-bit group of four 8-bit values within each 128-bit vector segment, in the range 0 to 3, encoded in the 'i2' field.

For the '16-bit to 64-bit' variant: is the immediate index of a 64-bit group of four 16-bit values within each 128-bit vector segment, in the range 0 to 1, encoded in the 'i1' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer eltspersegment = 128 DIV esize; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; bits(esize) res = Elem[operand3, e, esize]; for i = 0 to 3 constant integer element1 = UInt(Elem[operand1, 4 * e + i, esize DIV 4]); constant integer element2 = UInt(Elem[operand2, 4 * s + i, esize DIV 4]); res = res + element1 * element2; Elem[result, e, esize] = res; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.