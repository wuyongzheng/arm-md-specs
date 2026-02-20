## C9.2.46 BFMOPS (non-widening)

BFloat16 outer product, subtracting

This instruction works with a 16-bit element ZA tile.

This instruction generates an outer product of the first source vector and the second source vector. The first source is SVLH × 1 vector and the second source is 1 × SVLH vector.

Each source vector is independently predicated by a corresponding governing predicate. When either source vector element is Inactive the corresponding destination tile element remains unmodified.

The resulting outer product, SVLH × SVLH, is then destructively subtracted from the destination tile. This is equivalent to performing a single multiply-subtract from each of the destination tile elements.

This instruction follows SME2 ZA-targeting non-widening BFloat16 numerical behaviors.

ID\_AA64SMFR0\_EL1.B16B16 indicates whether this instruction is implemented.

## SME2

(FEAT\_SME\_B16B16)

<!-- image -->

## Encoding

```
BFMOPS <ZAda>.H, <Pn>/M, <Pm>/M, <Zn>.H, <Zm>.H
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_B16B16) then EndOfDecode(Decode_UNDEF); constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda);
```

## Assembler Symbols

## &lt;ZAda&gt;

Is the name of the ZA tile ZA0-ZA1, encoded in the 'ZAda' field.

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
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV 16; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) op1 = Z[n, VL]; constant bits(VL) op2 = Z[m, VL]; constant bits(dim*dim*16) op3 = ZAtile[da, 16, dim*dim*16]; bits(dim*dim*16) result; for row = 0 to dim-1 for col = 0 to dim-1 constant bits(16) elem2 = Elem[op2, col, 16]; constant bits(16) elem3 = Elem[op3, row*dim+col, 16]; if ActivePredicateElement(mask1, row, 16) && ActivePredicateElement(mask2, col, 16) then constant bits(16) elem1 = BFNeg(Elem[op1, row, 16]); Elem[result, row*dim+col, 16] = BFMulAdd_ZA(elem3, elem1, elem2, FPCR); else Elem[result, row*dim+col, 16] = elem3; ZAtile[da, 16, dim*dim*16] = result;
```