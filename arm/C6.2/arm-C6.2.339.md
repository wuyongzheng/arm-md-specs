## C6.2.339 RETAASPPC, RETABSPPC

Return from subroutine, with enhanced pointer authentication using an immediate offset

This instruction authenticates the address that is held in LR, using SP as the first modifier, the specified immediate subtracted from PC as the second modifier, and the specified key, and branches to the authenticated address.

Key A is used for RETAASPPC . Key B is used for RETABSPPC .

If the authentication passes, the PE continues execution at the target of the branch. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The authenticated address is not written back to LR.

This instruction provides a hint that this is a subroutine return.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding for the RETAASPPC variant

```
Applies when (opc == 000)
```

```
RETAASPPC <label>
```

## Encoding for the RETABSPPC variant

```
Applies when (opc == 001) RETABSPPC <label>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth_LR) then EndOfDecode(Decode_UNDEF);
```

```
constant boolean use_key_a = opc<0> == '0'; constant bits(64) offset = ZeroExtend(imm16:'00', 64); constant boolean auth_then_branch = TRUE;
```

## Assembler Symbols

## &lt;label&gt;

Is the program label whose address is to be calculated. Its negative offset from the address of this instruction, a multiple of 4 in the range -262140 to 0, is encoded as an unsigned value in the 'imm16' field as &lt;label&gt;/4.

## Operation

```
GCSInstruction inst_type; bits(64) target = X[30, 64]; constant bits(64) modifier = SP[64]; constant bits(64) modifier2 = PC64 -offset; if use_key_a then target =
```

```
AuthIA2(target, modifier, modifier2, auth_then_branch); else
```

```
target = AuthIB2(target, modifier, modifier2, auth_then_branch); if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) then inst_type = if use_key_a then GCSInstType_PRETAA else GCSInstType_PRETAB; target = LoadCheckGCSRecord(target, inst_type); SetCurrentGCSPointer(GetCurrentGCSPointer() + 8); // Value in BTypeNext will be used to set PSTATE.BTYPE BTypeNext = '00'; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_RET, branch_conditional);
```
