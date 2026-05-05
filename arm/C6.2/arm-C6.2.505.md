## C6.2.505 XAFLAG

Convert floating-point condition flags from external format to Arm format

This instruction converts the state of the PSTATE.{N,Z,C,V} flags from an alternative representation required by some software to a form representing the result of an Arm floating-point scalar compare instruction.

## System

(FEAT\_FlagM2)

<!-- image -->

## Encoding

XAFLAG

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_FlagM2) then EndOfDecode(Decode\_UNDEF);

## Operation

```
constant bit n = NOT(PSTATE.C) AND constant bit z = PSTATE.Z AND PSTATE.C; constant bit c = PSTATE.C OR PSTATE.Z; constant bit v = NOT(PSTATE.C) AND PSTATE.Z; PSTATE.N = n; PSTATE.Z = z; PSTATE.C = c; PSTATE.V = v;
```

```
NOT(PSTATE.Z);
```
