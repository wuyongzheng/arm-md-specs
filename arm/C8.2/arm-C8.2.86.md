## C8.2.86 BRKPA

Break after first true condition, propagating from previous partition

This instruction breaks after first true condition, propagating from previous partition. If the Last active element of the first source predicate is false, then the destination predicate is set to all-false. Otherwise, the destination predicate elements up to and including the first active and true source element are set to true, then the subsequent elements are set to false. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

## Not setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
BRKPA <Pd>.B, <Pg>/Z,
```

```
<Pn>.B, <Pm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer m = UInt(Pm); constant integer d = UInt(Pd); constant boolean setflags = FALSE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the first source scalable predicate register, encoded in the 'Pn' field.

## &lt;Pm&gt;

Is the name of the second source scalable predicate register, encoded in the 'Pm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV constant bits(PL) mask = P[g, PL]; constant bits(PL) operand1 = P[n, PL]; constant bits(PL) operand2 = P[m, PL];
```

```
esize; bits(PL) result;
```

```
boolean last = (LastActive(mask, operand1, 8) == '1'); for e = 0 to elements-1 if ActivePredicateElement(mask, e, 8) then constant bit pbit = if last then '1' else '0'; Elem[result, e, 1] = ZeroExtend(pbit, 1); last = last && (!ActivePredicateElement(operand2, e, 8)); else Elem[result, e, 1] = ZeroExtend('0', 1); if setflags then PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```