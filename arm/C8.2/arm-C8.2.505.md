## C8.2.505 PFIRST

Set the First active predicate element to true

This instruction sets the First active element in the destination predicate to true, otherwise elements from the source predicate are passed through unchanged. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
PFIRST
```

```
<Pdn>.B, <Pg>, <Pdn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer dn = UInt(Pdn);
```

## Assembler Symbols

## &lt;Pdn&gt;

Is the name of the source and destination scalable predicate register, encoded in the 'Pdn' field.

<!-- image -->

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = P[g, PL]; bits(PL) result = P[dn, PL]; integer first = -1; constant integer psize = esize DIV 8; for e = 0 to elements-1 if ActivePredicateElement(mask, e, esize) && first == -1 then first = e; if first >= 0 then Elem[result, first, psize] = ZeroExtend('1', psize); PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[dn, PL] = result;
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.