## C6.2.337 RET

Return from subroutine

This instruction branches unconditionally to an address in a register. This instruction provides a hint that this is a subroutine return.

<!-- image -->

## Encoding

<!-- image -->

## Decode for this encoding

```
constant integer n = UInt(Rn);
```

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose register holding the address to be branched to, encoded in the 'Rn' field. Defaults to X30 if absent.

## Operation

```
bits(64) target = X[n, 64]; if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) then target = LoadCheckGCSRecord(target, GCSInstType_PRET); SetCurrentGCSPointer(GetCurrentGCSPointer() + 8); // Value in BTypeNext will be used to set PSTATE.BTYPE BTypeNext = '00'; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_RET, branch_conditional);
```
