## C6.2.308 PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB

Pointer Authentication Code for instruction address, using key B

This instruction computes and inserts a Pointer Authentication Code for an instruction address, using a modifier and key B.

The address is:

- In the general-purpose register that is specified by &lt;Xd&gt; for PACIB and PACIZB .
- In X17, for PACIB1716 .
- In X30, for PACIBSP and PACIBZ .

The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xn|SP&gt; for PACIB .
- The value zero, for PACIZB and PACIBZ .
- In X16, for PACIB1716 .
- In SP, for PACIBSP .

If FEAT\_PAuth\_LR is implemented and PSTATE.PACM is 1, then PACIB1716 and PACIBSP include a second modifier that is:

- In X15, for PACIB1716 .
- The value of PC, for PACIBSP .

A PACIBSP instruction has an implicit BTI instruction. The implicit BTI instruction of a PACIBSP instruction is always compatible with PSTATE.BTYPE == 0b01 and PSTATE.BTYPE == 0b10 . Controls in SCTLR\_ELx configure whether the implicit BTI instruction of a PACIBSP instruction is compatible with PSTATE.BTYPE == 0b11 . For more information, see PSTATE.BTYPE.

It has encodings from 2 classes: Integer and System

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the PACIB variant

```
Applies when (Z == 0) PACIB <Xd>, <Xn|SP>
```

## Encoding for the PACIZB variant

Applies when

(Z == 1

PACIZB

&lt;Xd&gt;

&amp;&amp;

Rn

==

11111)

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_UNDEF); boolean source_is_sp = FALSE; constant boolean pacib1716 = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); if Z == '0' then // PACIB if n == 31 then source_is_sp = TRUE; else // PACIZB if n != 31 then EndOfDecode(Decode_UNDEF);
```

## System

(FEAT\_PAuth)

<!-- image -->

## Encoding for the PACIB1716 variant

```
Applies when (CRm == 0001 && op2 == 010)
```

PACIB1716

## Encoding for the PACIBSP variant

```
Applies when (CRm == 0011 && op2 == 011)
```

PACIBSP

## Encoding for the PACIBZ variant

```
Applies when (CRm == 0011 && op2 == 010)
```

PACIBZ

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_NOP); integer d; integer n; boolean source_is_sp = FALSE; boolean pacib1716 = FALSE; case CRm:op2 of when '0011 010' // PACIBZ d = 30; n = 31; when '0011 011' // PACIBSP d = 30; source_is_sp = TRUE; if IsFeatureImplemented(FEAT_BTI) then // Check for branch target compatibility between PSTATE.BTYPE // and implicit branch target of PACIBSP instruction. constant PACInstType pacinst = PACIxSP; SetBTypeCompatible(BTypeCompatible_PAC(pacinst)); when '0001 010' // PACIB1716 d = 17;
```

```
n = 16; pacib1716 = TRUE;
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if source_is_sp then if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' then X[d, 64] = AddPACIB2(X[d, 64], SP[64], PC64); else X[d, 64] = AddPACIB(X[d, 64], SP[64]); else if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' && pacib1716 then X[d, 64] = AddPACIB2(X[d, 64], X[n, 64], X[15, 64]); else X[d, 64] = AddPACIB(X[d, 64], X[n, 64]);
```
