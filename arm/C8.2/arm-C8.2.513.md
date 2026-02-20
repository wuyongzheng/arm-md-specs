## C8.2.513 PNEXT

Find next active predicate

This instruction constructs a loop that iterates over all true elements in the vector select predicate register. If all elements in the first source predicate register are false it determines the first true element in the vector select predicate register, otherwise it determines the next true element in the vector select predicate register that follows the last true element in the first source predicate register. All elements of the destination predicate register are set to false, except the element corresponding to the determined vector select element, if any, which is set to true. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

|   31 | 29 28                              | 25 24 23 22 21 20 19 16 15 14 13 11 10 9 8 5 4 3   |
|------|------------------------------------|----------------------------------------------------|
|    0 | 0 1 0 0 1 0 1 size 0 1 1 0 0 1 1 1 | 0 0 0 1 0 Pv 0 Pdn                                 |

## Encoding

```
PNEXT <Pdn>.<T>, <Pv>, <Pdn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer v = UInt(Pv); constant integer dn = UInt(Pdn);
```

## Assembler Symbols

## &lt;Pdn&gt;

Is the name of the first source and destination scalable predicate register, encoded in the 'Pdn' field.

<!-- image -->

<!-- image -->

&lt;Pv&gt;

Is the size specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the name of the vector select predicate register, encoded in the 'Pv' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[v, PL]; constant bits(PL) operand = P[dn, PL]; bits(PL) result; constant integer psize = esize DIV 8; integer next = LastActiveElement(operand, esize) + 1; while next < elements && (!ActivePredicateElement(mask, next, esize)) do next = next + 1; result = Zeros(PL); if next < elements then Elem[result, next, psize] = ZeroExtend('1', psize); PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[dn, PL] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.