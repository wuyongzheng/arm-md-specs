## C6.2.502 WFET

Wait for event with timeout

This instruction provides a hint that the PE can enter a low-power state and remain there until either a local timeout event or a wakeup event occurs. Wakeup events include the event signaled as a result of executing the SEV instruction on any PE in the multiprocessor system. For more information, see Wait For Event mechanism and Send event.

As described in Wait For Event mechanism and Send event, the execution of a WFET instruction that would otherwise cause entry to a low-power state can be trapped to a higher Exception level.

## System

(FEAT\_WFxT)

<!-- image -->

## Encoding

WFET

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
constant integer localtimeout = UInt(X[d, 64]); if Halted() && ConstrainUnpredictableBool(Unpredictable_WFxTDEBUG) then ExecuteAsNOP(); Hint_WFET(localtimeout);
```

```
EndOfDecode(Decode_UNDEF);
```
