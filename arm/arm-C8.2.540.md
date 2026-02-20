## C8.2.540 RDFFR (unpredicated)

Read the first-fault register

This instruction reads the first-fault register ( FFR ) and places the read values in the destination predicate without predication.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE)

<!-- image -->

## Encoding

```
RDFFR <Pd>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Pd);
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) ffr = FFR[PL]; P[d, PL] = ffr;
```