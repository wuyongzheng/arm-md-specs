## C8.2.541 RDFFR (predicated)

Return predicate of succesfully loaded elements

This instruction reads the first-fault register ( FFR ) and places active elements in the corresponding elements of the destination predicate. Inactive elements in the destination predicate register are set to zero. This instruction does not set the condition flags.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## Not setting the condition flags

(FEAT\_SVE)

<!-- image -->

## Encoding

```
RDFFR <Pd>.B, <Pg>/Z
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer g = UInt(Pg); constant integer d = UInt(Pd); constant boolean setflags = FALSE;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

<!-- image -->

Is the name of the governing scalable predicate register, encoded in the 'Pg' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) mask = P[g, PL]; constant bits(PL) ffr = FFR[PL]; constant bits(PL) result = ffr AND mask; if setflags then PSTATE.<N,Z,C,V> = P[d, PL] = result;
```

```
PredTest(mask, result, 8);
```