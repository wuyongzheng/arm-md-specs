## C8.2.575 SEL (predicates)

Conditionally select elements from two predicates

This instruction reads Active elements from the first source predicate and Inactive elements from the second source predicate and places them in the corresponding elements of the destination predicate. This instruction does not set the condition flags.

This instruction is used by the alias MOV (predicate, merging).

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
SEL <Pd>.B, <Pg>, <Pn>.B, <Pm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer m = UInt(Pm); constant integer d = UInt(Pd);
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## &lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the first source scalable predicate register, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second source scalable predicate register, encoded in the 'Pm' field.

## Alias Conditions

| Alias                    | Is preferred when   |
|--------------------------|---------------------|
| MOV (predicate, merging) | Pd == Pm            |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand1 = P[n, PL]; constant bits(PL) operand2 = P[m, PL]; bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bit element1 = PredicateElement(operand1, e, esize); constant bit element2 = PredicateElement(operand2, e, esize); if ActivePredicateElement(mask, e, esize) then Elem[result, e, psize] = ZeroExtend(element1, psize); else Elem[result, e, psize] = ZeroExtend(element2, psize); P[d, PL] = result;
```