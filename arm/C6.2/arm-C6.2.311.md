## C6.2.311 PACM

Pointer authentication modifier

This instruction is used to set the value of PSTATE.PACM to 1.

If FEAT\_PAuth\_LR is not implemented, this instruction behaves as a NOP.

## System

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

PACM

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_PAuth\_LR) then EndOfDecode(Decode\_NOP);

## Operation

PSTATE.PACM = if IsPACMEnabled() then '1' else '0';
