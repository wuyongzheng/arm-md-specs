## C6.2.313 PACNBIBSPPC

Pointer Authentication Code for return address, using key B, not a branch target

This instruction computes and inserts a Pointer Authentication Code for an instruction address, using two modifiers and key B.

The address is in X30.

The first modifier is in SP.

The second modifier is the value of PC.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

PACNBIBSPPC

## Decode for this encoding

if !IsFeatureImplemented(FEAT\_PAuth\_LR) then EndOfDecode(Decode\_UNDEF);

```
constant integer d = 30;
```

## Operation

X[d, 64] = AddPACIB2(X[d, 64], SP[64], PC64);
