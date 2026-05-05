## C6.2.88 CLRBHB

Clear branch history

This instruction can be used to clear the branch history.

For more information, see Branch history.

## System

(FEAT\_CLRBHB)

<!-- image -->

## Encoding

CLRBHB

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_CLRBHB) then EndOfDecode(Decode\_NOP);

## Operation

Hint\_CLRBHB();
