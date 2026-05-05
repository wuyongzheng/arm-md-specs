## C6.2.307 PACIASPPC

Pointer Authentication Code for return address, using key A

This instruction computes and inserts a Pointer Authentication Code for an instruction address, using two modifiers and key A.

The address is in X30.

The first modifier is in SP.

The second modifier is the value of PC.

A PACIASPPC instruction has an implicit BTI instruction. The implicit BTI instruction of a PACIASPPC instruction is always compatible with PSTATE.BTYPE == 0b01 and PSTATE.BTYPE == 0b10 . Controls in SCTLR\_ELx configure whether the implicit BTI instruction of a PACIASPPC instruction is compatible with PSTATE.BTYPE == 0b11 . For more information, see PSTATE.BTYPE.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

PACIASPPC

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PAuth_LR) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = 30; if IsFeatureImplemented(FEAT_BTI) then // Check for branch target compatibility between PSTATE.BTYPE // and implicit branch target of PACIxSPPC instruction. constant PACInstType pacinst = PACIxSPPC; SetBTypeCompatible(BTypeCompatible_PAC(pacinst));
```

## Operation

```
X[d, 64] = AddPACIA2(X[d, 64], SP[64], PC64);
```
