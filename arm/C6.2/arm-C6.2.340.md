## C6.2.340 RETAASPPCR, RETABSPPCR

Return from subroutine, with enhanced pointer authentication using a register

This instruction authenticates the address that is held in LR, using SP as the first modifier, the value in the specified register as the second modifier, and the specified key, and branches to the authenticated address.

Key A is used for RETAASPPCR . Key B is used for RETABSPPCR .

If the authentication passes, the PE continues execution at the target of the branch. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to LR.

This instruction provides a hint that this is a subroutine return.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding for the RETAASPPCR variant

```
(M == 0)
```

```
Applies when RETAASPPCR <Xm>
```

## Encoding for the RETABSPPCR variant

```
(M == 1)
```

```
Applies when RETABSPPCR <Xm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth_LR) then EndOfDecode(Decode_UNDEF); constant integer m = UInt(Rm); constant boolean use_key_a = M == '0'; constant boolean auth_then_branch = TRUE;
```

## Assembler Symbols

&lt;Xm&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rm' field.

## Operation

```
GCSInstruction inst_type; bits(64) target = X[30, 64]; constant bits(64) modifier = SP[64]; constant bits(64) modifier2 = X[m, 64]; if use_key_a then target = AuthIA2(target, modifier, modifier2, auth_then_branch); else target = AuthIB2(target, modifier, modifier2, auth_then_branch);
```

```
if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) then inst_type = if use_key_a then GCSInstType_PRETAA else GCSInstType_PRETAB; target = LoadCheckGCSRecord(target, inst_type); SetCurrentGCSPointer(GetCurrentGCSPointer() + 8); // Value in BTypeNext will be used to set PSTATE.BTYPE BTypeNext = '00'; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_RET, branch_conditional);
```
