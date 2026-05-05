## C7.2.16 BFDOT (by element)

BFloat16 dot product to single-precision (vector, by element)

This instruction delimits the source vectors into pairs of BFloat16 elements. The BFloat16 pair within the second source vector is specified using an immediate index. The index range is from 0 to 3 inclusive.

If FEAT\_EBF16 is not implemented or FPCR.EBF is 0, this instruction:

- Performs an unfused sum-of-products of each pair of adjacent BFloat16 elements in the first source vector with the specified pair of elements in the second source vector. The intermediate single-precision products are rounded before they are summed, and the intermediate sum is rounded before accumulation into the single-precision destination element that overlaps with the corresponding pair of BFloat16 elements in the first source vector.
- Uses the non-IEEE 754 Round-to-Odd rounding mode, which forces bit 0 of an inexact result to 1, and rounds an overflow to an appropriately signed Infinity.
- Flushes denormalized inputs and results to zero, as if FPCR.{FZ, FIZ} is {1, 1}.
- Honors FPCR.AH when generating a default NaN result, otherwise disables alternative floating point behaviors, as if FPCR.AH is 0.

If FEAT\_EBF16 is implemented and FPCR.EBF is 1, then this instruction:

- Performs a fused sum-of-products of each pair of adjacent BFloat16 elements in the first source vector with the specified pair of elements in the second source vector. The intermediate single-precision products are not rounded before they are summed, but the intermediate sum is rounded before accumulation into the single-precision destination element that overlaps with the corresponding pair of BFloat16 elements in the first source vector.
- Follows all other floating-point behaviors that apply to single-precision arithmetic, as governed by FPCR.RMode, FPCR.FZ, FPCR.AH, and FPCR.FIZ.

Irrespective of FEAT\_EBF16 and FPCR.EBF, this instruction:

- Does not modify the cumulative FPSR exception bits (IDC, IXC, UFC, OFC, DZC, and IOC).
- Disables trapped floating-point exceptions, as if the FPCR trap enable bits (IDE, IXE, UFE, OFE, DZE, and IOE) are all zero.
- Generates only the default NaN, as if FPCR.DN is 1.

ID\_AA64ISAR1\_EL1.BF16 indicates whether this instruction is supported.

## Advanced SIMD

(FEAT\_BF16)

<!-- image -->

## Encoding

```
BFDOT <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.2H[<index>]
```

## Decode for this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_BF16) then constant integer n = UInt(Rn); constant integer m = UInt(M:Rm); constant integer d = UInt(Rd); constant integer i = UInt(H:L); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV 32;
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Ta&gt;

## &lt;Vn&gt;

&lt;Tb&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 2S     |
|   1 | 4S     |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'M:Rm' fields.

## &lt;index&gt;

Is the immediate index of a pair of 16-bit elements in the range 0 to 3, encoded in the 'H:L' fields.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(128) operand2 = V[m, 128]; constant bits(datasize) operand3 = V[d, datasize]; bits(datasize) result; for e = 0 to elements-1 constant bits(16) elt1_a = Elem[operand1, 2 * e + 0, 16]; constant bits(16) elt1_b = Elem[operand1, 2 * e + 1, 16]; constant bits(16) elt2_a = Elem[operand2, 2 * i + 0, 16]; constant bits(16) elt2_b = Elem[operand2, 2 * i + 1, 16]; constant bits(32) sum = Elem[operand3, e, 32]; Elem[result, e, 32] = BFDotAdd(sum, elt1_a, elt1_b, elt2_a, elt2_b, FPCR); V[d, datasize] = result;
```

|   Q | <Tb>   |
|-----|--------|
|   0 | 4H     |
|   1 | 8H     |
