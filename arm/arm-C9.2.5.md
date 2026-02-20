## C9.2.5 ADDHA

Add horizontally vector elements to ZA tile

This instruction adds each element of the source vector to the corresponding Active element of each horizontal slice of a ZAtile. The tile elements are predicated by a pair of governing predicates. An element of a horizontal slice is considered active if its corresponding element in the second governing predicate is TRUE and the element corresponding to its horizontal slice number in the first governing predicate is TRUE. Inactive elements in the destination tile remain unmodified.

ID\_AA64SMFR0\_EL1.I16I64 indicates whether the 64-bit integer variant is implemented.

It has encodings from 2 classes: 32-bit and 64-bit

32-bit

(FEAT\_SME)

<!-- image -->

## Encoding

```
ADDHA <ZAda>.S, <Pn>/M, <Pm>/M, <Zn>.S
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer da = UInt(ZAda);
```

## 64-bit

(FEAT\_SME\_I16I64)

<!-- image -->

## Encoding

```
ADDHA <ZAda>.D, <Pn>/M, <Pm>/M, <Zn>.D
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME_I16I64) then constant integer esize = 64; constant integer a = UInt(Pn); constant integer b = UInt(Pm); constant integer n = UInt(Zn); constant integer da = UInt(ZAda);
```

```
EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;ZAda&gt;

For the '32-bit' variant: is the name of the ZA tile ZA0-ZA3, encoded in the 'ZAda' field.

For the '64-bit' variant: is the name of the ZA tile ZA0-ZA7, encoded in the 'ZAda' field.

## &lt;Pn&gt;

Is the name of the first governing scalable predicate register P0-P7, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second governing scalable predicate register P0-P7, encoded in the 'Pm' field.

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## Operation

```
CheckStreamingSVEAndZAEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer dim = VL DIV esize; constant bits(PL) mask1 = P[a, PL]; constant bits(PL) mask2 = P[b, PL]; constant bits(VL) operand_src = Z[n, VL]; constant bits(dim*dim*esize) operand_acc = ZAtile[da, esize, dim*dim*esize]; bits(dim*dim*esize) result; for col = 0 to dim-1 constant bits(esize) element = Elem[operand_src, col, esize]; for row = 0 to dim-1 bits(esize) res = Elem[operand_acc, row*dim+col, esize]; if (ActivePredicateElement(mask1, row, esize) && ActivePredicateElement(mask2, col, esize)) then res = res + element; Elem[result, row*dim+col, esize] = res; ZAtile[da, esize, dim*dim*esize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.