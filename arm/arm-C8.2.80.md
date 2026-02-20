## C8.2.80 BRKA

Break after first true condition

This instruction sets the destination predicate elements up to and including the first active and true source element to true, then sets subsequent elements to false.

Inactive elements in the destination predicate register remain unmodified or are set to zero, depending on whether merging or zeroing predication is selected. This instruction does not set the condition flags.

## Not setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
BRKA <Pd>.B, <Pg>/<ZM>, <Pn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer d = UInt(Pd); constant boolean merging = (M == '1'); constant boolean setflags = FALSE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

<!-- image -->

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;ZM&gt;

Is the predication qualifier, encoded in 'M':

<!-- image -->

&lt;Pn&gt;

|   M | <ZM>   |
|-----|--------|
|   0 | Z      |
|   1 | M      |

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand = P[n, PL]; constant bits(PL) operand2 = if merging then P[d, PL] else Zeros(PL); boolean break = FALSE; bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant boolean element = ActivePredicateElement(operand, e, esize); if ActivePredicateElement(mask, e, esize) then constant bit pbit = if !break then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); break = break || element; elsif merging then constant bit pbit = PredicateElement(operand2, e, esize); Elem[result, e, psize] = ZeroExtend(pbit, psize); else Elem[result, e, psize] = ZeroExtend('0', psize); if setflags then PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```