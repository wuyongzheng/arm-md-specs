## C6.2.32 AUTIBSPPCR

Authenticate return address using key B, using a register

This instruction authenticates an instruction address, using two modifiers and key B.

If the authentication passes, the upper bits of the address are restored to enable subsequent use of the address. For information on behavior if the authentication fails, see Faulting on pointer authentication.

The address is in X30.

The first modifier is in SP.

The second modifier is in the general-purpose register that is specified by &lt;Xn&gt; .

## Integer

(FEAT\_PAuth\_LR)

<!-- image -->

## Encoding

AUTIBSPPCR

&lt;Xn&gt;

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PAuth_LR) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = 30; constant integer n = UInt(Rn); constant boolean auth_combined = FALSE;
```

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
X[d, 64] = AuthIB2(X[d, 64], SP[64], X[n, 64], auth_combined);
```
