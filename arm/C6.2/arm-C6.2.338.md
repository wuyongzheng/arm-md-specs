## C6.2.338 RETAA, RETAB

Return from subroutine, with pointer authentication

This instruction authenticates the address that is held in LR, using SP as the modifier and the specified key, and branches to the authenticated address.

Key A is used for RETAA . Key B is used for RETAB .

If the authentication passes, the PE continues execution at the target of the branch. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to LR.

This instruction provides a hint that this is a subroutine return.

If FEAT\_PAuth\_LR is implemented and PSTATE.PACM is 1, then RETAA and RETAB include a second modifier that is in X16.

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the RETAA variant

```
Applies when (M == 0)
```

RETAA

## Encoding for the RETAB variant

```
Applies when (M == 1)
```

RETAB

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then constant boolean use_key_a = (M == '0'); constant boolean auth_then_branch = TRUE;
```

## Operation

```
GCSInstruction inst_type; bits(64) target = X[30, 64]; constant bits(64) modifier = SP[64]; bits(64) modifier2; boolean use_modifier2 = FALSE; if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' then modifier2 = X[16, 64]; use_modifier2 = TRUE; if use_key_a then if use_modifier2 && IsFeatureImplemented(FEAT_PAuth_LR) then target = AuthIA2(target, modifier, modifier2, auth_then_branch); else
```

```
EndOfDecode(Decode_UNDEF);
```

```
target = AuthIA(target, modifier, auth_then_branch); else if use_modifier2 && IsFeatureImplemented(FEAT_PAuth_LR) then target = AuthIB2(target, modifier, modifier2, auth_then_branch); else target = AuthIB(target, modifier, auth_then_branch); if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) then inst_type = if use_key_a then GCSInstType_PRETAA else GCSInstType_PRETAB; target = LoadCheckGCSRecord(target, inst_type); SetCurrentGCSPointer(GetCurrentGCSPointer() + 8); // Value in BTypeNext will be used to set PSTATE.BTYPE BTypeNext = '00'; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_RET, branch_conditional);
```
