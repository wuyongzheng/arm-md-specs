## C8.2.577 SETFFR

Initialize the first-fault register to all true

This instruction initializes the first-fault register ( FFR ) to all true prior to a sequence of first-fault or non-fault loads. This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE)

<!-- image -->

## Encoding

SETFFR

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; FFR[PL] = Ones(PL);
```