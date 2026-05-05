## C6.2.305 PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA

Pointer Authentication Code for instruction address, using key A

This instruction computes and inserts a Pointer Authentication Code for an instruction address, using a modifier and key A.

The address is:

- In the general-purpose register that is specified by &lt;Xd&gt; for PACIA and PACIZA .
- In X17, for PACIA1716 .
- In X30, for PACIASP and PACIAZ .

The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xn|SP&gt; for PACIA .
- The value zero, for PACIZA and PACIAZ .
- In X16, for PACIA1716 .
- In SP, for PACIASP .

If FEAT\_PAuth\_LR is implemented and PSTATE.PACM is 1, then PACIA1716 and PACIASP include a second modifier that is:

- In X15, for PACIA1716 .
- The value of PC, for PACIASP .

A PACIASP instruction has an implicit BTI instruction. The implicit BTI instruction of a PACIASP instruction is always compatible with PSTATE.BTYPE == 0b01 and PSTATE.BTYPE == 0b10 . Controls in SCTLR\_ELx configure whether the implicit BTI instruction of a PACIASP instruction is compatible with PSTATE.BTYPE == 0b11 . For more information, see PSTATE.BTYPE.

It has encodings from 2 classes: Integer and System

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the PACIA variant

```
Applies when (Z == 0) PACIA <Xd>, <Xn|SP>
```

## Encoding for the PACIZA variant

Applies when

(Z == 1

PACIZA

&lt;Xd&gt;

&amp;&amp;

Rn

==

11111)

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_PAuth) then boolean source_is_sp = FALSE; constant boolean pacia1716 = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); if Z == '0' then // PACIA if n == 31 then source_is_sp = TRUE; else // PACIZA if n != 31 then EndOfDecode(Decode_UNDEF);
```

## System

(FEAT\_PAuth)

<!-- image -->

## Encoding for the PACIA1716 variant

```
Applies when (CRm == 0001 && op2 == 000)
```

PACIA1716

## Encoding for the PACIASP variant

```
Applies when (CRm == 0011 && op2 == 001)
```

PACIASP

## Encoding for the PACIAZ variant

```
Applies when (CRm == 0011 && op2 == 000)
```

PACIAZ

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_NOP); integer d; integer n; boolean source_is_sp = FALSE; boolean pacia1716 = FALSE; case CRm:op2 of when '0011 000' // PACIAZ d = 30; n = 31; when '0011 001' // PACIASP d = 30; source_is_sp = TRUE; if IsFeatureImplemented(FEAT_BTI) then // Check for branch target compatibility between PSTATE.BTYPE // and implicit branch target of PACIASP instruction. constant PACInstType pacinst = PACIxSP; SetBTypeCompatible(BTypeCompatible_PAC(pacinst)); when '0001 000' // PACIA1716 d = 17;
```

```
n = 16; pacia1716 = TRUE;
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if source_is_sp then if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' then X[d, 64] = AddPACIA2(X[d, 64], SP[64], PC64); else X[d, 64] = AddPACIA(X[d, 64], SP[64]); else if IsFeatureImplemented(FEAT_PAuth_LR) && PSTATE.PACM == '1' && pacia1716 then X[d, 64] = AddPACIA2(X[d, 64], X[n, 64], X[15, 64]); else X[d, 64] = AddPACIA(X[d, 64], X[n, 64]);
```
