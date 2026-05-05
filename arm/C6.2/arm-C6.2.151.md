## C6.2.151 DRPS

Debug restore PE state

This instruction restores PSTATE from the SPSR.

The SPSR is checked for the current Exception level for an illegal return event. See Illegal exception returns from AArch64 state.

This instruction is UNDEFINED in Non-debug state.

This instruction is UNDEFINED at EL0.

For more information on the operation of DRPS , see DRPS.

<!-- image -->

## Encoding

DRPS

## Decode for this encoding

// Empty.

## Operation

```
if !Halted() || PSTATE.EL == EL0 then UNDEFINED; DRPSInstruction();
```
