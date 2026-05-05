## C6.2.26 AUTIA171615

Authenticate instruction address, using key A

This instruction authenticates an instruction address, using two modifiers and key A. The address is in X17. The 64-bit value of modifier1 is the value in X16. The 64-bit value of modifier2 is the value in X15.

If the authentication passes, the upper bits of the address are restored to enable subsequent use of the address. For information on behavior if the authentication fails, see Faulting on pointer authentication.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

AUTIA171615

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_PAuth\_LR) then EndOfDecode(Decode\_UNDEF);

## Operation

```
constant boolean is_combined = FALSE; X[17, 64] = AuthIA2(X[17, 64], X[16, 64], X[15, 64], is_combined);
```
