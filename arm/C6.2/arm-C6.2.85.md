## C6.2.85 CHKFEAT

Check feature status

This instruction indicates the status of features. For more information, see Check Feature.

If FEAT\_CHK is not implemented, this instruction executes as a NOP .

## System

(FEAT\_CHK)

<!-- image -->

## Encoding

CHKFEAT X16

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_CHK) then EndOfDecode(Decode\_NOP);

## Operation

X[16, 64] = AArch64.ChkFeat(X[16, 64]);
