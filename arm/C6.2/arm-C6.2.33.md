## C6.2.33 AXFLAG

Convert floating-point condition flags from Arm to external format

This instruction converts the state of the PSTATE.{N,Z,C,V} flags from a form representing the result of an Arm floating-point scalar compare instruction to an alternative representation required by some software.

## System

(FEAT\_FlagM2)

<!-- image -->

## Encoding

AXFLAG

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_FlagM2) then EndOfDecode(Decode\_UNDEF);

## Operation

```
constant bit z = PSTATE.Z OR PSTATE.V; constant bit c = PSTATE.C AND NOT(PSTATE.V); PSTATE.<N,Z,C,V> = '0' : z : c : '0';
```
