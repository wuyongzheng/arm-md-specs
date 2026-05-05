## C6.2.44 BLR

Branch with link to register

This instruction calls a subroutine at an address in a register, setting register X30 to PC+4. This instruction provides a hint that this is a subroutine call.

<!-- image -->

## Encoding

BLR

&lt;Xn&gt;

## Decode for this encoding

```
constant integer n = UInt(Rn);
```

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose register holding the address to be branched to, encoded in the 'Rn' field.

## Operation

```
constant bits(64) target = X[n, 64]; if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) AddGCSRecord(PC64 + 4); // Value in BTypeNext will be used to set PSTATE.BTYPE BTypeNext = '10'; X[30, 64] = PC64 + 4; constant boolean branch_conditional = FALSE; BranchTo(target, BranchType_INDCALL, branch_conditional);
```

```
then
```
