## C6.2.157 ERET

Exception return

This instruction restores PSTATE from the SPSR, and branches to the address held in the ELR.

The SPSR is checked for the current Exception level for an illegal return event. See Illegal exception returns from AArch64 state.

ERET is UNDEFINED at EL0.

<!-- image -->

## Encoding

ERET

## Decode for this encoding

```
constant boolean pac = FALSE; constant boolean use_key_a =
```

```
TRUE;
```

## Operation

```
if PSTATE.EL == EL0 then UNDEFINED; AArch64.CheckForERetTrap(pac, use_key_a); constant bits(64) target = ELR_ELx[];
```

AArch64.ExceptionReturn(target, SPSR\_ELx[]);
