## C8.2.531 PTEST

Set condition flags for predicate

This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate source register, and sets the V flag to zero.

```
SVE
```

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
PTEST <Pg>, <Pn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8; constant integer g = UInt(Pg); constant integer n = UInt(Pn);
```

## Assembler Symbols

&lt;Pg&gt;

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

&lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) mask = P[g, PL]; constant bits(PL) result = P[n, PL]; PSTATE.<N,Z,C,V> = PredTest(mask, result, esize);
```

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the predicate register written by this instruction might be significantly delayed.