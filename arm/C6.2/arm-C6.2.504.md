## C6.2.504 WFIT

Wait for interrupt with timeout

This instruction provides a hint that the PE can enter a low-power state and remain there until either a local timeout event or a wakeup event occurs. For more information, see Wait For Interrupt.

As described in Wait For Interrupt, the execution of a WFIT instruction that would otherwise cause entry to a low-power state can be trapped to a higher Exception level.

## System

(FEAT\_WFxT)

<!-- image -->

## Encoding

WFIT

&lt;Xt&gt;

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_WFxT) then constant integer d = UInt(Rd);
```

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rd' field.

## Operation

```
constant integer localtimeout = UInt(X[d, 64]); if Halted() && ExecuteAsNOP(); Hint_WFIT(localtimeout);
```

```
EndOfDecode(Decode_UNDEF);
```

```
ConstrainUnpredictableBool(Unpredictable_WFxTDEBUG) then
```
