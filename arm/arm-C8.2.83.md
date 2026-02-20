## C8.2.83 BRKBS

Break before first true condition, setting the condition flags

This instruction sets the destination predicate elements up to but not including the first active and true source element to true, then sets subsequent elements to false. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## Setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
BRKBS <Pd>.B, <Pg>/Z,
```

```
<Pn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer d = UInt(Pd); constant boolean merging = FALSE; constant boolean setflags = TRUE;
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand = P[n, PL]; constant bits(PL) operand2 = if merging then P[d, PL] else Zeros(PL); boolean break = FALSE; bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant boolean element = ActivePredicateElement(operand, e, esize);
```

```
if ActivePredicateElement(mask, e, esize) then break = break || element; constant bit pbit = if !break then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); elsif merging then constant bit pbit = PredicateElement(operand2, e, esize); Elem[result, e, psize] = ZeroExtend(pbit, psize); else Elem[result, e, psize] = ZeroExtend('0', psize); if setflags then PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.