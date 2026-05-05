## C6.2.83 CFINV

Invert carry flag

This instruction inverts the value of the PSTATE.C flag.

## System

(FEAT\_FlagM)

<!-- image -->

## Encoding

CFINV

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_FlagM) then EndOfDecode(Decode\_UNDEF);

## Operation

PSTATE.C = NOT(PSTATE.C);

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
