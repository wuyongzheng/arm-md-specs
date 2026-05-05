## C6.2.25 AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA

Authenticate instruction address, using key A

This instruction authenticates an instruction address, using a modifier and key A.

If the authentication passes, the upper bits of the address are restored to enable subsequent use of the address. For information on behavior if the authentication fails, see Faulting on pointer authentication.

## The address is:

- In the general-purpose register that is specified by &lt;Xd&gt; for AUTIA and AUTIZA .
- In X17, for AUTIA1716 .
- In X30, for AUTIASP and AUTIAZ .

## The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xn|SP&gt; for AUTIA .
- The value zero, for AUTIZA and AUTIAZ .
- In X16, for AUTIA1716 .
- In SP, for AUTIASP .

If FEAT\_PAuth\_LR is implemented and PSTATE.PACM is 1, then AUTIA1716 and AUTIASP include a second modifier that is:

- In X15, for AUTIA1716 .
- In X16, for AUTIASP .

It has encodings from 2 classes: Integer and System

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the AUTIA variant

Applies when (Z == 0)

```
AUTIA <Xd>, <Xn|SP>
```

## Encoding for the AUTIZA variant

```
Applies when (Z == 1 && Rn == 11111)
```

```
AUTIZA <Xd>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_UNDEF); if Z == '1' && Rn != '11111' then EndOfDecode(Decode_UNDEF); constant boolean autia1716 = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant boolean auth_combined = FALSE; constant boolean source_is_sp = Z == '0' && n == 31;
```

## System

(FEAT\_PAuth)

<!-- image -->

## Encoding for the AUTIA1716 variant

```
Applies when (CRm == 0001 && op2 == 100)
```

AUTIA1716

## Encoding for the AUTIASP variant

```
Applies when (CRm == 0011 && op2 == 101)
```

AUTIASP

## Encoding for the AUTIAZ variant

```
Applies when (CRm == 0011 && op2 == 100)
```

AUTIAZ

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then integer d; integer n; boolean source_is_sp = FALSE; boolean autia1716 = FALSE; constant boolean auth_combined = FALSE; case CRm:op2 of when '0011 100' // AUTIAZ d = 30; n = 31; when '0011 101' // AUTIASP d = 30; source_is_sp = TRUE; when '0001 100' // AUTIA1716 d = 17; n = 16; autia1716 = TRUE;
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rn' field.

```
EndOfDecode(Decode_NOP);
```

## Operation

```
if source_is_sp then if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' then X[d, 64] = AuthIA2(X[d, 64], SP[64], X[16, 64], auth_combined); else X[d, 64] = AuthIA(X[d, 64], SP[64], auth_combined); else if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' && autia1716 then X[d, 64] = AuthIA2(X[d, 64], X[n, 64], X[15, 64], auth_combined); else X[d, 64] = AuthIA(X[d, 64], X[n, 64], auth_combined);
```
