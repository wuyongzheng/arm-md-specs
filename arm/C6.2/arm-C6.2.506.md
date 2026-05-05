## C6.2.506 XPACD, XPACI, XPACLRI

Strip Pointer Authentication Code

This instruction removes the Pointer Authentication Code from an address. The address is in the specified general-purpose register for XPACI and XPACD , and is in LR for XPACLRI .

The XPACD instruction is used for data addresses, and XPACI and XPACLRI are used for instruction addresses.

It has encodings from 2 classes: Integer and System

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the XPACD variant

Applies when

(D == 1)

XPACD

&lt;Xd&gt;

## Encoding for the XPACI variant

Applies when

(D == 0)

XPACI

&lt;Xd&gt;

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then constant integer d = UInt(Rd); constant boolean data = (D == '1');
```

## System

(FEAT\_PAuth)

<!-- image -->

## Encoding

XPACLRI

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then constant integer d = 30; constant boolean data = FALSE;
```

```
EndOfDecode(Decode_UNDEF);
```

```
EndOfDecode(Decode_NOP);
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

X[d, 64] = Strip(X[d, 64], data);
