## C6.2.43 BL

## Branch with link

This instruction branches to a PC-relative offset, setting register X30 to PC+4. This instruction provides a hint that this is a subroutine call.

<!-- image -->

## Encoding

```
BL <label>
```

## Decode for this encoding

```
constant bits(64) offset = SignExtend(imm26:'00', 64); constant integer d = 30;
```

## Assembler Symbols

## &lt;label&gt;

Is the program label to be unconditionally branched to. Its offset from the address of this instruction, in the range +/-128MB, is encoded as 'imm26' times 4.

## Operation

```
if IsFeatureImplemented(FEAT_GCS) && GCSPCREnabled(PSTATE.EL) AddGCSRecord(PC64 + 4); X[d, 64] = PC64 + 4; constant boolean branch_conditional = FALSE; BranchTo(PC64 + offset, BranchType_DIRCALL, branch_conditional);
```

```
then
```
