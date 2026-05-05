## C6.2.287 MSR (immediate)

Move immediate value to special register

This instruction moves an immediate value to selected bits of the PSTATE. For more information, see Process state, PSTATE.

The bits that can be written by this instruction are:

- PSTATE.D, PSTATE.A, PSTATE.I, PSTATE.F, and PSTATE.SP.
- If FEAT\_SSBS is implemented, PSTATE.SSBS.
- If FEAT\_PAN is implemented, PSTATE.PAN.
- If FEAT\_UAO is implemented, PSTATE.UAO.
- If FEAT\_DIT is implemented, PSTATE.DIT.
- If FEAT\_MTE is implemented, PSTATE.TCO.
- If FEAT\_NMI is implemented, PSTATE.ALLINT.
- If FEAT\_SME is implemented, PSTATE.SM and PSTATE.ZA.
- If FEAT\_EBEP is implemented, PSTATE.PM.

If FEAT\_MTE is implemented and FEAT\_MTE2 is not implemented, it is IMPLEMENTATION DEFINED whether writes to PSTATE.TCO by this instruction are ignored.

This instruction is used by the aliases SMSTART and SMSTOP.

<!-- image -->

## Encoding

```
Applies when (!(op1 == 000 && op2 IN {00x, 010}))
```

```
MSR
```

```
<pstatefield>, #<imm>
```

## Decode for this encoding

```
if op1 == '000' && op2 == '000' then SEE "CFINV"; if op1 == '000' && op2 == '001' then SEE "XAFLAG"; if op1 == '000' && op2 == '010' then SEE "AXFLAG"; bits(2) min_EL; boolean need_secure = FALSE; case op1 of when '00x' min_EL = EL1; when '010' min_EL = EL1; when '011' min_EL = EL0; when '100' min_EL = EL2; when '101' if !IsFeatureImplemented(FEAT_VHE) then EndOfDecode(Decode_UNDEF); min_EL = EL2; when '110' min_EL = EL3; when '111' min_EL = EL1; need_secure = TRUE;
```

```
constant bits(4) operand = CRm; PSTATEField field; case op1:op2 of when '000 011' if !IsFeatureImplemented(FEAT_UAO) then EndOfDecode(Decode_UNDEF); field = PSTATEField_UAO; when '000 100' if !IsFeatureImplemented(FEAT_PAN) then EndOfDecode(Decode_UNDEF); field = PSTATEField_PAN; when '000 101' field = PSTATEField_SP; when '001 000' case CRm of when '000x' if !IsFeatureImplemented(FEAT_NMI) then EndOfDecode(Decode_UNDEF); field = PSTATEField_ALLINT; when '001x' if !IsFeatureImplemented(FEAT_EBEP) then EndOfDecode(Decode_UNDEF); field = PSTATEField_PM; otherwise EndOfDecode(Decode_UNDEF); when '011 010' if !IsFeatureImplemented(FEAT_DIT) then EndOfDecode(Decode_UNDEF); field = PSTATEField_DIT; when '011 011' case CRm of when '001x' if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); field = PSTATEField_SVCRSM; when '010x' if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); field = PSTATEField_SVCRZA; when '011x' if !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); field = PSTATEField_SVCRSMZA; otherwise EndOfDecode(Decode_UNDEF); when '011 100' if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF); field = PSTATEField_TCO; when '011 110' field = PSTATEField_DAIFSet; when '011 111' field = PSTATEField_DAIFClr; when '011 001' if !IsFeatureImplemented(FEAT_SSBS) then EndOfDecode(Decode_UNDEF); field = PSTATEField_SSBS; otherwise EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;pstatefield&gt;

Is a PSTATE field name. For the MSR instruction, this is encoded in 'CRm:op1:op2':

| CRm   |   op1 |   op2 | <pstatefield>   | Architectural Feature   |
|-------|-------|-------|-----------------|-------------------------|
| 000x  |   001 |   000 | ALLINT          | FEAT_NMI                |
| 000x  |   011 |   011 | RESERVED        | -                       |
| 001x  |   001 |   000 | PM              | FEAT_EBEP               |
| 001x  |   011 |   011 | SVCRSM          | FEAT_SME                |
| 010x  |   011 |   011 | SVCRZA          | FEAT_SME                |

| CRm   | op1   | op2   | <pstatefield>   | Architectural Feature   |
|-------|-------|-------|-----------------|-------------------------|
| 01xx  | 001   | 000   | RESERVED        | -                       |
| 011x  | 011   | 011   | SVCRSMZA        | FEAT_SME                |
| xxxx  | 000   | 011   | UAO             | FEAT_UAO                |
| xxxx  | 000   | 100   | PAN             | FEAT_PAN                |
| xxxx  | 000   | 101   | SPSel           | -                       |
| xxxx  | 000   | 11x   | RESERVED        | -                       |
| xxxx  | 001   | 001   | RESERVED        | -                       |
| xxxx  | 001   | 01x   | RESERVED        | -                       |
| xxxx  | 001   | 1xx   | RESERVED        | -                       |
| xxxx  | 010   | xxx   | RESERVED        | -                       |
| xxxx  | 011   | 000   | RESERVED        | -                       |
| xxxx  | 011   | 001   | SSBS            | FEAT_SSBS               |
| xxxx  | 011   | 010   | DIT             | FEAT_DIT                |
| xxxx  | 011   | 100   | TCO             | FEAT_MTE                |
| xxxx  | 011   | 101   | RESERVED        | -                       |
| xxxx  | 011   | 110   | DAIFSet         | -                       |
| xxxx  | 011   | 111   | DAIFClr         | -                       |
| xxxx  | 1xx   | xxx   | RESERVED        | -                       |
| 1xxx  | 001   | 000   | RESERVED        | -                       |
| 1xxx  | 011   | 011   | RESERVED        | -                       |

For the SMSTART and SMSTOP aliases, this is encoded in 'CRm&lt;2:1&gt;', where 0b01 specifies SVCRSM, 0b10 specifies SVCRZA, and 0b11 specifies SVCRSMZA.

## &lt;imm&gt;

Is a 4-bit unsigned immediate, in the range 0 to 15, encoded in the 'CRm' field. Restricted to the range 0 to 1, encoded in 'CRm&lt;0&gt;', when &lt;pstatefield&gt; is ALLINT, PM, SVCRSM, SVCRSMZA, or SVCRZA.

## Alias Conditions

## Operation

```
if UInt(PSTATE.EL) < UInt(min_EL) then UNDEFINED; if need_secure && CurrentSecurityState() != SS_Secure then UNDEFINED; case field of when PSTATEField_SSBS PSTATE.SSBS = operand<0>; when PSTATEField_SP
```

| Alias   | Is preferred when                            |
|---------|----------------------------------------------|
| SMSTART | op1 == '011' && CRm IN {'0xx1'}              |
| SMSTOP  | op1 == '011' && CRm IN {'0xx0'} op2 == '011' |

```
PSTATE.SP = operand<0>; when PSTATEField_DAIFSet AArch64.CheckDAIFAccess(PSTATEField_DAIFSet); PSTATE.D = PSTATE.D OR operand<3>; PSTATE.A = PSTATE.A OR operand<2>; PSTATE.I = PSTATE.I OR operand<1>; PSTATE.F = PSTATE.F OR operand<0>; when PSTATEField_DAIFClr AArch64.CheckDAIFAccess(PSTATEField_DAIFClr); PSTATE.D = PSTATE.D AND NOT(operand<3>); PSTATE.A = PSTATE.A AND NOT(operand<2>); PSTATE.I = PSTATE.I AND NOT(operand<1>); PSTATE.F = PSTATE.F AND NOT(operand<0>); when PSTATEField_PAN PSTATE.PAN = operand<0>; when PSTATEField_UAO PSTATE.UAO = operand<0>; when PSTATEField_DIT PSTATE.DIT = operand<0>; when PSTATEField_TCO PSTATE.TCO = operand<0>; when PSTATEField_ALLINT if (PSTATE.EL == EL1 && IsHCRXEL2Enabled() && HCRX_EL2.TALLINT == '1' && operand<0> == '1') then AArch64.SystemAccessTrap(EL2, \texttt{0x18}); PSTATE.ALLINT = operand<0>; when PSTATEField_SVCRSM CheckSMEAccess(); SetPSTATE_SM(operand<0>); when PSTATEField_SVCRZA CheckSMEAccess(); SetPSTATE_ZA(operand<0>); when PSTATEField_SVCRSMZA CheckSMEAccess(); SetPSTATE_SM(operand<0>); SetPSTATE_ZA(operand<0>); when PSTATEField_PM PSTATE.PM = operand<0>;
```
