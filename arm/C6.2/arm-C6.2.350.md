## C6.2.350 SB

Speculation barrier

This instruction is a barrier that controls speculation. For more information and details of the semantics, see Speculation Barrier (SB).

## System

(FEAT\_SB)

<!-- image -->

## Encoding

SB

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_SB) then EndOfDecode(Decode\_UNDEF);

## Operation

SpeculationBarrier();
