## C6.2.306 PACIA171615

Pointer Authentication Code for instruction address, using key A

This instruction computes and inserts a pointer authentication code for an instruction address, using two modifiers and key A. The address is in X17. The 64-bit value of modifier1 is the value in X16. The 64-bit value of modifier2 is the value in X15.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

PACIA171615

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_PAuth\_LR) then EndOfDecode(Decode\_UNDEF);

## Operation

X[17, 64] = AddPACIA2(X[17, 64], X[16, 64], X[15, 64]);
