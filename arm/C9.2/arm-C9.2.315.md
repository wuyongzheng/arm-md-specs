## C9.2.315 UMOPS (2-way)

Unsigned 16-bit integer sum of outer products to 32-bit integer, subtracting

This instruction works with a 32-bit element ZA tile.

This instruction multiplies the sub-matrix in the first source vector by the sub-matrix in the second source vector. The first source holds SVLS × 2 sub-matrix of unsigned 16-bit integer values, and the second source holds 2 × SVLS sub-matrix of unsigned 16-bit integer values.

Each source vector is independently predicated by a corresponding governing predicate. When a 16-bit source element is inactive, it is treated as having the value 0.

The resulting SVLS × SVLS widened 32-bit integer sum of outer products is then destructively subtracted from the 32-bit integer destination tile. This is equivalent to performing a 2-way dot product and subtract from each of the destination tile elements.

Each 32-bit container of the first source vector holds 2 consecutive column elements of each row of a SVLS × 2 sub-matrix, and each 32-bit container of the second source vector holds 2 consecutive row elements of each column of a 2 × SVLS sub-matrix.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
UMOPS <ZAda>.S, <Pn>/M, <Pm>/M,
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda); constant boolean unsigned = TRUE;
```

## Assembler Symbols

## &lt;ZAda&gt;

Is the name of the ZA tile ZA0-ZA3, encoded in the 'ZAda' field.

## &lt;Pn&gt;

Is the name of the first governing scalable predicate register P0-P7, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second governing scalable predicate register P0-P7, encoded in the 'Pm' field.

## &lt;Zn&gt;

```
<Zn>.H, <Zm>.H
```

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV esize; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(dim*dim*esize) operand3 = ZAtile[da, esize, dim*dim*esize]; bits(dim*dim*esize) result; integer prod; for row = 0 to dim-1 for col = 0 to dim-1 bits(esize) sum = Elem[operand3, row*dim+col, esize]; for k = 0 to 1 if (ActivePredicateElement(mask1, 2*row + k, esize DIV 2) && ActivePredicateElement(mask2, 2*col + k, esize DIV 2)) then constant bits(esize DIV 2) op1elt = Elem[operand1, 2*row + k, esize DIV 2]; constant bits(esize DIV 2) op2elt = Elem[operand2, 2*col + k, esize DIV 2]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); prod = element1 * element2; sum = sum prod; Elem[result, row*dim+col, esize] = sum; ZAtile[da, esize, dim*dim*esize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.