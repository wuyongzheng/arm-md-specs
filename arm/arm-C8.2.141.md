## C8.2.141 EORS

Bitwise exclusive-OR predicates, setting the condition flags

This instruction performs a bitwise exclusive-OR on active elements of the second source predicate with the corresponding elements of the first source predicate and places the results in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

This instruction is used by the alias NOTS.

## Setting the condition flags

```
(FEAT_SVE || FEAT_SME)
```

<!-- image -->

## Encoding

```
EORS <Pd>.B, <Pg>/Z, <Pn>.B, <Pm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer m = UInt(Pm); constant integer d = UInt(Pd); constant boolean setflags = TRUE;
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

| Alias   | Is preferred when   |
|---------|---------------------|
| NOTS    | Pm == Pg            |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand1 = P[n, PL]; constant bits(PL) operand2 = P[m, PL]; bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bit element1 = PredicateElement(operand1, e, esize); constant bit element2 = PredicateElement(operand2, e, esize); if ActivePredicateElement(mask, e, esize) then Elem[result, e, psize] = ZeroExtend(element1 EOR element2, else Elem[result, e, psize] = ZeroExtend('0', psize); if setflags then PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.

```
psize);
```