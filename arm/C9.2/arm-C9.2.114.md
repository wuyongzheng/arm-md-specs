## C9.2.114 FMOPA (widening, 4-way)

8-bit floating-point sum of outer products to single-precision, accumulating

This instruction works with a 32-bit element ZA tile.

This instruction widens the SVLS × 4 sub-matrix of 8-bit floating-point values held in the first source vector to single-precision values and multiplies it by the widened 4 × SVLS sub-matrix of 8-bit floating-point values in the second source vector to single-precision values.

Each source vector is independently predicated by a corresponding governing predicate. When a 8-bit source element is Inactive it is treated as having the value +0.0, but if both groups of source vector elements that correspond to a 32-bit destination element contain Inactive elements, then the destination element remains unmodified.

The resulting SVLS × SVLS single-precision sum of outer products are scaled by 2 -UInt(FPMR.LSCALE) , before being destructively added to the single-precision destination tile. This is equivalent to performing a downscaled 4-way dot product and accumulate to each of the destination tile elements.

Each 32-bit container of the first source vector holds 4 consecutive column elements of each row of a SVLS × 4 sub-matrix. Similarly, each 32-bit container of the second source vector holds 4 consecutive row elements of each column of a 4 × SVLS sub-matrix.

The 8-bit floating-point encoding format for the elements of the first source vector and the second source vector is selected by FPMR.F8S1 and FPMR.F8S2 respectively.

## SME2

(FEAT\_SME\_F8F32)

<!-- image -->

## Encoding

```
FMOPA <ZAda>.S, <Pn>/M, <Pm>/M, <Zn>.B, <Zm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_F8F32) then EndOfDecode(Decode_UNDEF); constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda);
```

## Assembler Symbols

## &lt;ZAda&gt;

Is the name of the ZA tile ZA0-ZA3, encoded in the 'ZAda' field.

## &lt;Pn&gt;

Is the name of the first governing scalable predicate register P0-P7, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second governing scalable predicate register P0-P7, encoded in the 'Pm' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckFPMREnabled(); CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV 32; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(dim*dim*32) operand3 = ZAtile[da, 32, dim*dim*32]; bits(dim*dim*32) result; for row = 0 to dim-1 for col = 0 to dim-1 array [0..3] of boolean prow; array [0..3] of boolean pcol; boolean any_active = FALSE; for i = 0 to 3 prow[i] = ActivePredicateElement(mask1, 4*row + i, 8); pcol[i] = ActivePredicateElement(mask2, 4*col + i, 8); any_active = any_active || (prow[i] && pcol[i]); if any_active then bits(32) sum = Elem[operand3, row*dim+col, 32]; bits(32) rowop = Zeros(32); bits(32) colop = Zeros(32); for i = 0 to 3 if prow[i] then Elem[rowop, i, 8] = Elem[operand1, 4*row + i, 8]; if pcol[i] then Elem[colop, i, 8] = Elem[operand2, 4*col + i, 8]; sum = FP8DotAddFP(sum, rowop, colop, FPCR, FPMR); Elem[result, row*dim+col, 32] = sum; else Elem[result, row*dim+col, 32] = ZAtile[da, 32, dim*dim*32] = result;
```

```
Elem[operand3, row*dim+col, 32];
```