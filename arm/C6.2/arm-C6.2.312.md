## C6.2.312 PACNBIASPPC

Pointer Authentication Code for return address, using key A, not a branch target

This instruction computes and inserts a Pointer Authentication Code for an instruction address, using two modifiers and key A.

The address is in X30.

The first modifier is in SP.

The second modifier is the value of PC.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

PACNBIASPPC

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_PAuth\_LR) then EndOfDecode(Decode\_UNDEF);

```
constant integer d = 30;
```

## Operation

X[d, 64] = AddPACIA2(X[d, 64], SP[64], PC64);
