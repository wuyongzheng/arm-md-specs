## C8.2.933 WRFFR

Write the first-fault register

This instruction reads the source predicate register and places in the first-fault register ( FFR ). This instruction is intended to restore a saved FFR and is not recommended for general use by applications.

This instruction requires that the source predicate contains a monotonic predicate value, in which starting from bit 0 there are zero or more 1 bits, followed only by 0 bits in any remaining bit positions. If the source is not a monotonic predicate value, then the resulting value in the FFR will be UNPREDICTABLE. It is not possible to generate a non-monotonic value in FFR when using SETFFR followed by first-fault or non-fault loads.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE)

<!-- image -->

## Encoding

```
WRFFR <Pn>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer n = UInt(Pn);
```

## Assembler Symbols

&lt;Pn&gt;

Is the name of the source scalable predicate register, encoded in the 'Pn' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant bits(PL) operand = P[n, PL]; constant integer hsb = if hsb < 0 || IsOnes(operand<hsb:0>) then FFR[PL] = operand; else // not a monotonic predicate FFR[PL] = bits(PL) UNKNOWN;
```

```
HighestSetBit(operand);
```