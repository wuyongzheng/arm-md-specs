## C8.2.542 RDFFRS

Return predicate of succesfully loaded elements, setting the condition flags

This instruction reads the first-fault register ( FFR ) and places active elements in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

```
Setting the condition flags (FEAT_SVE)
```

<!-- image -->

## Encoding

```
RDFFRS <Pd>.B, <Pg>/Z
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer g = UInt(Pg); constant integer d = UInt(Pd); constant boolean setflags = TRUE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

<!-- image -->

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) mask = P[g, PL]; constant bits(PL) ffr = FFR[PL]; constant bits(PL) result = ffr AND mask; if setflags then PSTATE.<N,Z,C,V> = PredTest(mask, result, 8); P[d, PL] = result;
```