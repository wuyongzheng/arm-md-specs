## C6.2.29 AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB

Authenticate instruction address, using key B

This instruction authenticates an instruction address, using a modifier and key B.

If the authentication passes, the upper bits of the address are restored to enable subsequent use of the address. For information on behavior if the authentication fails, see Faulting on pointer authentication.

## The address is:

- In the general-purpose register that is specified by &lt;Xd&gt; for AUTIB and AUTIZB .
- In X17, for AUTIB1716 .
- In X30, for AUTIBSP and AUTIBZ .

## The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xn|SP&gt; for AUTIB .
- The value zero, for AUTIZB and AUTIBZ .
- In X16, for AUTIB1716 .
- In SP, for AUTIBSP .

If FEAT\_PAuth\_LR is implemented and PSTATE.PACM is 1, then AUTIB1716 and AUTIBSP include a second modifier that is:

- In X15, for AUTIB1716 .
- In X16, for AUTIBSP .

It has encodings from 2 classes: Integer and System

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the AUTIB variant

Applies when (Z == 0)

```
AUTIB <Xd>, <Xn|SP>
```

## Encoding for the AUTIZB variant

```
Applies when (Z == 1 && Rn == 11111)
```

AUTIZB

&lt;Xd&gt;

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_UNDEF); if Z == '1' && Rn != '11111' then EndOfDecode(Decode_UNDEF); constant boolean autib1716 = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean auth_combined = FALSE; constant boolean source_is_sp = Z == '0' && n == 31;
```

## System

(FEAT\_PAuth)

<!-- image -->

## Encoding for the AUTIB1716 variant

```
Applies when (CRm == 0001 && op2 == 110)
```

AUTIB1716

## Encoding for the AUTIBSP variant

```
Applies when (CRm == 0011 && op2 == 111)
```

AUTIBSP

## Encoding for the AUTIBZ variant

```
Applies when (CRm == 0011 && op2 == 110)
```

AUTIBZ

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then integer d; integer n; boolean source_is_sp = FALSE; boolean autib1716 = FALSE; constant boolean auth_combined = FALSE; case CRm:op2 of when '0011 110' // AUTIBZ d = 30; n = 31; when '0011 111' // AUTIBSP d = 30; source_is_sp = TRUE; when '0001 110' // AUTIB1716 d = 17; n = 16; autib1716 = TRUE;
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rn' field.

```
EndOfDecode(Decode_NOP);
```

## Operation

```
if source_is_sp then if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' then X[d, 64] = AuthIB2(X[d, 64], SP[64], X[16, 64], auth_combined); else X[d, 64] = AuthIB(X[d, 64], SP[64], auth_combined); else if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' && autib1716 then X[d, 64] = AuthIB2(X[d, 64], X[n, 64], X[15, 64], auth_combined); else X[d, 64] = AuthIB(X[d, 64], X[n, 64], auth_combined);
```
