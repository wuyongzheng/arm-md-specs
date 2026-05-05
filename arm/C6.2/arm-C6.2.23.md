## C6.2.23 AUTDA, AUTDZA

Authenticate data address, using key A

This instruction authenticates a data address, using a modifier and key A.

The address is in the general-purpose register that is specified by &lt;Xd&gt; .

The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xn|SP&gt; , for AUTDA .
- The value zero, for AUTDZA .

If the authentication passes, the upper bits of the address are restored to enable subsequent use of the address. For information on behavior if the authentication fails, see Faulting on pointer authentication.

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the AUTDA variant

```
Applies when (Z == 0) AUTDA <Xd>, <Xn|SP>
```

## Encoding for the AUTDZA variant

```
Applies when (Z == 1 && Rn == 11111)
```

```
AUTDZA <Xd>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_UNDEF); if Z == '1' && Rn != '11111' then EndOfDecode(Decode_UNDEF); constant boolean auth_combined = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean source_is_sp = Z == '0' && n == 31;
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if source_is_sp then X[d, 64] = AuthDA(X[d, 64], SP[64], auth_combined); else X[d, 64] = AuthDA(X[d, 64], X[n, 64], auth_combined);
```
