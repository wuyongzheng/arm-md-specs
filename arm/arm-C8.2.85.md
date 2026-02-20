## C8.2.85 BRKNS

Propagate break to next partition, setting the condition flags

This instruction propagates break to next partition and sets the condition flags. If the Last active element of the first source predicate is false, then the destination predicate is set to all-false. Otherwise, the destination and second source predicates are left unchanged. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## Setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
BRKNS <Pdm>.B, <Pg>/Z, <Pn>.B, <Pdm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer g = UInt(Pg); constant integer n = UInt(Pn); constant integer dm = UInt(Pdm); constant boolean setflags = TRUE;
```

## Assembler Symbols

## &lt;Pdm&gt;

Is the name of the second source and destination scalable predicate register, encoded in the 'Pdm' field.

&lt;Pg&gt;

## &lt;Pn&gt;

Is the name of the first source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) mask = P[g, PL]; constant bits(PL) operand1 = P[n, PL]; constant bits(PL) operand2 = P[dm, PL]; bits(PL) result; if LastActive(mask, operand1, 8) == '1' then result = operand2; else result = Zeros(PL); if setflags then PSTATE.<N,Z,C,V> = PredTest(Ones(PL), result, 8); P[dm, PL] = result;
```

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.