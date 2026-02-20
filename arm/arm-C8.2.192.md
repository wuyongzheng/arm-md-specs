## C8.2.192 FIRSTP

Scalar index of first true predicate element (predicated)

This instruction determines the index of the first active and true element of the source predicate, and places the scalar result in the destination general-purpose register. If there are no active and true elements, the destination general-purpose register is updated to the value minus one.

## SVE2

(FEAT\_SVE2p2 || FEAT\_SME2p2)

<!-- image -->

## Encoding

```
FIRSTP <Xd>, <Pg>, <Pn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2p2) && !IsFeatureImplemented(FEAT_SME2p2) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer d = UInt(Rd);
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the destination general-purpose register, encoded in the 'Rd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

Is the size specifier, encoded in 'size':

<!-- image -->

&lt;Pn&gt;

<!-- image -->

&lt;T&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand = P[n, PL]; integer index = -1; for e = 0 to elements-1 if (index == -1 && ActivePredicateElement(mask, e, esize) && ActivePredicateElement(operand, e, esize)) then index = e; X[d, 64] = index<63:0>;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the general-purpose register written by this instruction might be significantly delayed.