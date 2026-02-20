## C9.2.55 BMOPA

Bitwise exclusive NOR population count outer product, accumulating

This instruction works with 32-bit element ZA tile. This instruction generates an outer product of the first source SVLS × 1 vector and the second source 1 × SVLS vector. Each outer product element is obtained as population count of the bitwise XNOR result of the corresponding 32-bit elements of the first source vector and the second source vector. Each source vector is independently predicated by a corresponding governing predicate. When either source vector element is inactive the corresponding destination tile element remains unmodified. The resulting SVLS × SVLS product is then destructively added to the destination tile.

## SME2

(FEAT\_SME2)

<!-- image -->

## Encoding

```
BMOPA <ZAda>.S, <Pn>/M, <Pm>/M, <Zn>.S, <Zm>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(ZAda);
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

S

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV esize; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(dim*dim*esize) operand3 = ZAtile[da, esize, dim*dim*esize]; bits(dim*dim*esize) result; for row = 0 to dim-1 constant bits(esize) element1 = Elem[operand1, row, esize]; for col = 0 to dim-1 constant bits(esize) element2 = Elem[operand2, col, esize]; constant bits(esize) element3 = Elem[operand3, row*dim + col, if (ActivePredicateElement(mask1, row, esize) && ActivePredicateElement(mask2, col, esize)) then constant integer res = BitCount(NOT(element1 EOR element2)); Elem[result, row*dim + col, esize] = element3 + res; else Elem[result, row*dim + col, esize] = element3; ZAtile[da, esize, dim*dim*esize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
esize];
```