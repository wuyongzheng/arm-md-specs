## C6.2.158 ERETAA, ERETAB

Exception return, with pointer authentication

This instruction authenticates the address in ELR, using SP as the modifier and the specified key, restores PSTATE from the SPSR for the current Exception level, and branches to the authenticated address.

Key A is used for ERETAA . Key B is used for ERETAB .

If the authentication passes, the PE continues execution at the target of the branch. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to ELR.

The SPSR is checked for the current Exception level for an illegal return event. See Illegal exception returns from AArch64 state.

ERETAA and ERETAB are UNDEFINED at EL0.

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the ERETAA variant

```
Applies when (M == 0)
```

ERETAA

## Encoding for the ERETAB variant

```
Applies when (M == 1)
```

ERETAB

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then constant boolean pac = TRUE; constant boolean use_key_a = (M == '0'); constant boolean auth_then_branch = TRUE;
```

## Operation

```
if PSTATE.EL == EL0 then UNDEFINED; AArch64.CheckForERetTrap(pac, use_key_a); bits(64) target = ELR_ELx[]; constant bits(64) modifier = SP[64]; if use_key_a then target = AuthIA(target, modifier, else target = AuthIB(target, modifier, AArch64.ExceptionReturn(target, SPSR_ELx[]);
```

```
EndOfDecode(Decode_UNDEF);
```

```
auth_then_branch); auth_then_branch);
```
