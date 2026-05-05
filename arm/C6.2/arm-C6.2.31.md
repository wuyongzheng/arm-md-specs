## C6.2.31 AUTIBSPPC

Authenticate return address using key B, using an immediate offset

This instruction authenticates an instruction address, using two modifiers and key B.

If the authentication passes, the upper bits of the address are restored to enable subsequent use of the address. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The address is in X30.

The first modifier is in SP.

The second modifier is the address of a program label.

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

```
AUTIBSPPC <label>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PAuth_LR) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = 30; constant bits(64) offset = ZeroExtend(imm16:'00', 64); constant boolean auth_combined = FALSE;
```

## Assembler Symbols

## &lt;label&gt;

Is the program label whose address is to be calculated. Its negative offset from the address of this instruction, a multiple of 4 in the range -262140 to 0, is encoded as an unsigned value in the 'imm16' field as &lt;label&gt;/4.

## Operation

```
constant bits(64) pac_addr = PC64 -offset; X[d, 64] = AuthIB2(X[d, 64], SP[64],
```

```
pac_addr, auth_combined);
```
