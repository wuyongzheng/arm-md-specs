## C8.2.50 BFDOT (indexed)

BFloat16 dot product by indexed element to single-precision

This instruction delimits the source vectors into pairs of BFloat16 elements. The BFloat16 pairs within the second source vector are specified using an immediate index that selects the same BFloat16 pair position within each 128-bit vector segment. The index range is from 0 to 3.

If FEAT\_EBF16 is not implemented or FPCR.EBF is 0, this instruction:

- Performs an unfused sum-of-products of each pair of adjacent BFloat16 elements in the first source vector with the specified pair of elements in the second vector. The intermediate single-precision products are rounded before they are summed, and the intermediate sum is rounded before accumulation into the single-precision destination element that overlaps with the corresponding pair of BFloat16 elements in the first source vector.
- Uses the non-IEEE 754 Round-to-Odd rounding mode, which forces bit 0 of an inexact result to 1, and rounds an overflow to an appropriately signed Infinity.
- Flushes denormalized inputs and results to zero, as if FPCR.{FZ, FIZ} is {1, 1}.
- Honors FPCR.AH when generating a default NaN result, otherwise disables alternative floating point behaviors, as if FPCR.AH is 0.

If FEAT\_EBF16 is implemented and FPCR.EBF is 1, then this instruction:

- Performs a fused sum-of-products of each pair of adjacent BFloat16 elements in the first source vector with the specified pair of elements in the second vector. The intermediate single-precision products are not rounded before they are summed, but the intermediate sum is rounded before accumulation into the single-precision destination element that overlaps with the corresponding pair of BFloat16 elements in the first source vector.
- Follows all other floating-point behaviors that apply to single-precision arithmetic, as governed by FPCR.RMode, FPCR.FZ, FPCR.AH, and FPCR.FIZ.

Irrespective of FEAT\_EBF16 and FPCR.EBF, this instruction:

- Does not modify the cumulative FPSR exception bits (IDC, IXC, UFC, OFC, DZC, and IOC).
- Disables trapped floating-point exceptions, as if the FPCR trap enable bits (IDE, IXE, UFE, OFE, DZE, and IOE) are all zero.
- Generates only the default NaN, as if FPCR.DN is 1.

This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.BF16 indicates whether this instruction is implemented.

## SVE

((FEAT\_SVE || FEAT\_SME) &amp;&amp; FEAT\_BF16)

<!-- image -->

## Encoding

```
BFDOT <Zda>.S, <Zn>.H, <Zm>.H[<imm>]
```

## Decode for this encoding

```
if ((!IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME)) ||
```

```
!IsFeatureImplemented(FEAT_BF16)) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant integer index = UInt(i2);
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register Z0-Z7, encoded in the 'Zm' field.

## &lt;imm&gt;

Is the immediate index of a pair of 16-bit elements within each 128-bit vector segment, in the range 0 to 3, encoded in the 'i2' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV 32; constant integer eltspersegment = 128 DIV 32; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 = Z[da, VL]; bits(VL) result; for e = 0 to elements-1 constant integer segmentbase = e - (e MOD eltspersegment); constant integer s = segmentbase + index; constant bits(16) elt1_a = Elem[operand1, 2 * e + 0, 16]; constant bits(16) elt1_b = Elem[operand1, 2 * e + 1, 16]; constant bits(16) elt2_a = Elem[operand2, 2 * s + 0, 16]; constant bits(16) elt2_b = Elem[operand2, 2 * s + 1, 16]; bits(32) sum = Elem[operand3, e, 32]; sum = BFDotAdd(sum, elt1_a, elt1_b, elt2_a, elt2_b, FPCR); Elem[result, e, 32] = sum; Z[da, VL] = result;
```

## Operational Information

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.