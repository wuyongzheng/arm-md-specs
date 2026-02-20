## D24.5 Performance Monitors registers

This section lists the Performance Monitoring registers in AArch64.

## D24.5.1 PMCCFILTR\_EL0, Performance Monitors Cycle Count Filter Register

The PMCCFILTR\_EL0 characteristics are:

## Purpose

Determines the modes in which the Cycle Counter, PMCCNTR\_EL0, increments.

## Configuration

AArch64 System register PMCCFILTR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCCFILTR[31:0].

When FEAT\_PMUv3\_TH is implemented, or FEAT\_PMUv3p8 is implemented, or FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_SME is implemented, AArch64 System register PMCCFILTR\_EL0 bits [63:32] are architecturally mapped to External register PMCCFILTR\_EL0[63:32].

AArch64 System register PMCCFILTR\_EL0 bits [31:0] are architecturally mapped to External register PMCCFILTR\_EL0[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCCFILTR\_EL0 are UNDEFINED.

## Attributes

PMCCFILTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:58]

Reserved, RES0.

## VS, bits [57:56]

## When FEAT\_PMUv3\_SME is implemented:

SVE mode filtering. Controls counting cycles in Streaming and Non-streaming SVE modes.

| VS   | Meaning                                                  |
|------|----------------------------------------------------------|
| 0b00 | This mechanism has no effect on the filtering of cycles. |
| 0b01 | The PE does not count cycles in Streaming SVE mode.      |
| 0b10 | The PE does not count cycles in Non-streaming SVE mode.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:

- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [55:32]

Reserved, RES0.

## P, bit [31]

EL1 filtering. Controls counting cycles in EL1.

| P   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of cycles. |
| 0b1 | The PE does not count cycles in EL1.                 |

If Secure and Non-secure states are implemented, then counting cycles in Non-secure EL1 is further controlled by PMCCFILTR\_EL0.NSK.

If FEAT\_RME is implemented, then counting cycles in Realm EL1 is further controlled by PMCCFILTR\_EL0.RLK.

If EL3 is implemented, then counting cycles in EL3 is further controlled by PMCCFILTR\_EL0.M.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

EL0 filtering. Controls counting cycles in EL0.

| U   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of cycles. |
| 0b1 | The PE does not count cycles in EL0.                 |

If Secure and Non-secure states are implemented, then counting cycles in Non-secure EL0 is further controlled by PMCCFILTR\_EL0.NSU.

If FEAT\_RME is implemented, then counting cycles in Realm EL0 is further controlled by PMCCFILTR\_EL0.RLU.

The reset behavior of this field is:

- On a Cold reset:

- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting cycles in Non-secure EL1. If PMCCFILTR\_EL0.NSK is not equal to PMCCFILTR\_EL0.P, then the PE does not count cycles in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of cycles in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.P == 1, the PE does not count cycles in Non-secure EL1. |
| 0b1   | When PMCCFILTR_EL0.P == 0, the PE does not count cycles in Non-secure EL1. When PMCCFILTR_EL0.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting cycles in Non-secure EL0. If PMCCFILTR\_EL0.NSU is not equal to PMCCFILTR\_EL0.U, then the PE does not count cycles in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of cycles in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.U == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.U == 1, the PE does not count cycles in Non-secure EL0. |
| 0b1   | When PMCCFILTR_EL0.U == 0, the PE does not count cycles in Non-secure EL0. When PMCCFILTR_EL0.U == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting cycles in EL2.

| NSH   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE does not count cycles in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of cycles. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting cycles in Secure EL2 is further controlled by PMCCFILTR\_EL0.SH.

If FEAT\_RME is implemented, then counting cycles in Realm EL2 is further controlled by PMCCFILTR\_EL0.RLH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## M, bit [26]

## When EL3 is implemented:

EL3 filtering. Controls counting cycles in EL3. If PMCCFILTR\_EL0.M is not equal to PMCCFILTR\_EL0.P, then the PE does not count cycles in EL3. Otherwise, this mechanism has no effect on filtering of cycles in EL3.

| M   | Meaning                                                                                                                                         |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When PMCCFILTR_EL0.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.P == 1, the PE does not count cycles in EL3. |
| 0b1 | When PMCCFILTR_EL0.P == 0, the PE does not count cycles in EL3. When PMCCFILTR_EL0.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [25]

Reserved, RES0.

## SH, bit [24]

## When EL3 is implemented and FEAT\_SEL2 is implemented:

Secure EL2 filtering. Controls counting cycles in Secure EL2. If PMCCFILTR\_EL0.SH is equal to PMCCFILTR\_EL0.NSH, then the PE does not count cycles in Secure EL2. Otherwise, this mechanism has no effect on filtering of cycles in Secure EL2.

| SH   | Meaning                                                                                                                                                    |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMCCFILTR_EL0.NSH == 0, the PE does not count cycles in Secure EL2. When PMCCFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of cycles. |
| 0b1  | When PMCCFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.NSH == 1, the PE does not count cycles in Secure EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

When Secure EL2 is not implemented, access to this field is RES0.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## RLK, bit [22]

## When FEAT\_RME is implemented:

Realm EL1 filtering. Controls counting cycles in Realm EL1. If PMCCFILTR\_EL0.RLK is not equal to PMCCFILTR\_EL0.P, then the PE does not count cycles in Realm EL1. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL1.

| RLK   | Meaning                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.P == 1, the PE does not count cycles in Realm EL1. |
| 0b1   | When PMCCFILTR_EL0.P == 0, the PE does not count cycles in Realm EL1. When PMCCFILTR_EL0.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting cycles in Realm EL0. If PMCCFILTR\_EL0.RLU is not equal to PMCCFILTR\_EL0.U, then the PE does not count cycles in Realm EL0. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL0.

| RLU   | Meaning                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.U == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.U == 1, the PE does not count cycles in Realm EL0. |
| 0b1   | When PMCCFILTR_EL0.U == 0, the PE does not count cycles in Realm EL0. When PMCCFILTR_EL0.U == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLH, bit [20]

## When FEAT\_RME is implemented:

Realm EL2 filtering. Controls counting cycles in Realm EL2. If PMCCFILTR\_EL0.RLH is equal to PMCCFILTR\_EL0.NSH, then the PE does not count cycles in Realm EL2. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL2.

| RLH   | Meaning                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.NSH == 0, the PE does not count cycles in Realm EL2. When PMCCFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of cycles. |
| 0b1   | When PMCCFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.NSH == 1, the PE does not count cycles in Realm EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [19:0]

Reserved, RES0.

## Accessing PMCCFILTR\_EL0

PMCCFILTR\_EL0 can also be accessed by using PMXEVTYPER\_EL0 with PMSELR\_EL0.SEL set to 0b11111 .

Permitted reads and writes of PMCCFILTR\_EL0 are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.C == 0.

Permitted writes of PMCCFILTR\_EL0 are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.{UEN,CR} == {1,1}.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMCCFILTR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b1111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMCCFILTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.C == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMCCFILTR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMCCFILTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCCFILTR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCCFILTR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCCFILTR_EL0;
```

MSR PMCCFILTR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1110 | 0b1111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMCCFILTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.C == '0' || ↪ → PMUSERENR_EL0.CR == '1') then return; else PMCCFILTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMCCFILTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCCFILTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCCFILTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMCCFILTR_EL0 = X[t, 64];
```

## D24.5.2 PMCCNTR\_EL0, Performance Monitors Cycle Count Register

The PMCCNTR\_EL0 characteristics are:

## Purpose

Holds the value of the processor Cycle Counter, CCNT, that counts processor clock cycles. See 'Time as measured by the Performance Monitors cycle counter' for more information.

PMCCFILTR\_EL0 determines the modes and states in which the PMCCNTR\_EL0 can increment.

## Configuration

All counters are subject to any changes in clock frequency, including clock stopping caused by the WFI and WFE instructions. This means that it is CONSTRAINED UNPREDICTABLE whether or not PMCCNTR\_EL0 continues to increment when clocks are stopped by WFI and WFE instructions.

AArch64 System register PMCCNTR\_EL0 bits [63:0] are architecturally mapped to AArch32 System register PMCCNTR[63:0].

AArch64 System register PMCCNTR\_EL0 bits [63:0] are architecturally mapped to External register PMCCNTR\_EL0[63:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCCNTR\_EL0 are UNDEFINED.

## Attributes

PMCCNTR\_EL0 is a 64-bit register.

## Field descriptions

CCNT

63

32

CCNT

31

0

<!-- image -->

## CCNT, bits [63:0]

Cycle count. Depending on the values of PMCR\_EL0.{LC,D}, this field increments in one of the following ways:

- Every processor clock cycle.
- Every 64th processor clock cycle.

Writing 1 to PMCR\_EL0.C sets this field to 0.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMCCNTR\_EL0

Permitted reads and writes of PMCCNTR\_EL0 are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.

- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.C == 0.

Permitted writes of PMCCNTR\_EL0 are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.{UEN,CR} == {1,1}.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMCCNTR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,CR,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<CR,EN> == '00') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMCCNTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.C == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMCCNTR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMCCNTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCCNTR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCCNTR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCCNTR_EL0;
```

MSR PMCCNTR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMCCNTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.C == '0' || ↪ → PMUSERENR_EL0.CR == '1') then return; else PMCCNTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMCCNTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCCNTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCCNTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMCCNTR_EL0 = X[t, 64];
```

## D24.5.3 PMCCNTSVR\_EL1, Performance Monitors Cycle Count Saved Value Register

The PMCCNTSVR\_EL1 characteristics are:

## Purpose

Captures the PMU Cycle counter, PMCCNTR\_EL0.

## Configuration

AArch64 System register PMCCNTSVR\_EL1 bits [63:0] are architecturally mapped to External register PMCCNTSVR\_EL1[63:0].

This register is present only when FEAT\_PMUv3\_SS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCCNTSVR\_EL1 are UNDEFINED.

## Attributes

PMCCNTSVR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |      |
|------|------|------|
| CCNT | CCNT | CCNT |
| 31   | 0    |      |
| CCNT | CCNT | CCNT |

## CCNT, bits [63:0]

Sampled Cycle Count. The value of PMCCNTR\_EL0 at the last successful Capture event.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMCCNTSVR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMCCNTSVR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1110 | 0b1011 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_SS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMSSDATA == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCCNTSVR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCCNTSVR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMCCNTSVR_EL1;
```

## D24.5.4 PMCEID0\_EL0, Performance Monitors Common Event Identification Register 0

The PMCEID0\_EL0 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the ranges 0x0000 to 0x001F and 0x4000 to 0x401F .

For more information about the Common events and the use of the PMCEID&lt;n&gt;\_EL0 registers see 'The PMU event number space and common events'.

## Configuration

AArch64 System register PMCEID0\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCEID0[31:0].

AArch64 System register PMCEID0\_EL0 bits [63:32] are architecturally mapped to AArch32 System register PMCEID2[31:0].

AArch64 System register PMCEID0\_EL0 bits [31:0] are architecturally mapped to External register PMCEID0[31:0].

AArch64 System register PMCEID0\_EL0 bits [63:32] are architecturally mapped to External register PMCEID2[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCEID0\_EL0 are UNDEFINED.

## Attributes

PMCEID0\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

IDhi&lt;n&gt; , bits [n+32], for n = 31 to 0

## When FEAT\_PMUv3p1 is implemented:

IDhi[n] corresponds to Common event ( 0x4000 + n).

For each bit:

| IDhi<n>   | Meaning                                              |
|-----------|------------------------------------------------------|
| 0b0       | The Common event is not implemented, or not counted. |
| 0b1       | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt;\_EL0 registers of that earlier version of the PMU architecture.

## Otherwise:

Reserved, RES0.

## ID&lt;n&gt; , bits [n], for n = 31 to 0

ID[n] corresponds to Common event n.

For each bit:

ID&lt;n&gt;

0b0

0b1

Meaning

The Common event is not implemented, or not counted.

The Common event is implemented.

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt;\_EL0 registers of that earlier version of the PMU architecture.

## Accessing PMCEID0\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMCEID0\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.TID == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCEID0_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCEID0_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCEID0_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCEID0_EL0;
```

## D24.5.5 PMCEID1\_EL0, Performance Monitors Common Event Identification Register 1

The PMCEID1\_EL0 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the ranges 0x0020 to 0x003F and 0x4020 to 0x403F .

For more information about the Common events and the use of the PMCEID&lt;n&gt;\_EL0 registers see 'The PMU event number space and common events'.

## Configuration

AArch64 System register PMCEID1\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCEID1[31:0].

AArch64 System register PMCEID1\_EL0 bits [63:32] are architecturally mapped to AArch32 System register PMCEID3[31:0].

AArch64 System register PMCEID1\_EL0 bits [31:0] are architecturally mapped to External register PMCEID1[31:0].

AArch64 System register PMCEID1\_EL0 bits [63:32] are architecturally mapped to External register PMCEID3[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCEID1\_EL0 are UNDEFINED.

## Attributes

PMCEID1\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

IDhi&lt;n&gt; , bits [n+32], for n = 31 to 0

## When FEAT\_PMUv3p1 is implemented:

IDhi[n] corresponds to Common event ( 0x4020 + n).

For each bit:

| IDhi<n>   | Meaning                                              |
|-----------|------------------------------------------------------|
| 0b0       | The Common event is not implemented, or not counted. |
| 0b1       | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt;\_EL0 registers of that earlier version of the PMU architecture.

## Otherwise:

Reserved, RES0.

## ID&lt;n&gt; , bits [n], for n = 31 to 0

ID[n] corresponds to Common event ( 0x0020 + n).

For each bit:

ID&lt;n&gt;

0b0

0b1

Meaning

The Common event is not implemented, or not counted.

The Common event is implemented.

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt;\_EL0 registers of that earlier version of the PMU architecture.

## Accessing PMCEID1\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMCEID1\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.TID == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCEID1_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCEID1_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCEID1_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCEID1_EL0;
```

## D24.5.6 PMCNTENCLR\_EL0, Performance Monitors Count Enable Clear Register

The PMCNTENCLR\_EL0 characteristics are:

## Purpose

Allows software to disable the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which counters are enabled.

## Configuration

AArch64 System register PMCNTENCLR\_EL0 bits [63:0] are architecturally mapped to AArch64 System register PMCNTENSET\_EL0[63:0].

AArch64 System register PMCNTENCLR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCNTENCLR[31:0].

AArch64 System register PMCNTENCLR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCNTENSET[31:0].

AArch64 System register PMCNTENCLR\_EL0 bits [31:0] are architecturally mapped to External register PMCNTENCLR\_EL0[31:0].

AArch64 System register PMCNTENCLR\_EL0 bits [31:0] are architecturally mapped to External register PMCNTENSET\_EL0[31:0].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMCNTENCLR\_EL0 bits [63:32] are architecturally mapped to External register PMCNTENCLR\_EL0[63:32].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMCNTENCLR\_EL0 bits [63:32] are architecturally mapped to External register PMCNTENSET\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCNTENCLR\_EL0 are UNDEFINED.

## Attributes

PMCNTENCLR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| C 31 30   | P30 P29 29 P28 28 P27 27 P26 26 P25 25 P24 24 P23 23 P22 22 P21 21 P20 20 P19 19 P18 18 P17 17 P16 16 P15 15 P14 14 P13 13 P12 12 P11 11 P10 10 P9 9 P8 8 P7 7 P6 6 P5 5 P4 4 P3 3 P2 2 P1 1 P0 0   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Bits [63:33]

Reserved, RES0.

F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

PMICNTR\_EL0 disable. On writes, allows software to disable PMICNTR\_EL0. On reads, returns the PMICNTR\_EL0 enable status.

## The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- PSTATE.EL == EL0
- Any of the following are true:
- PMUSERENR\_EL0.UEN == '0'
- PMUACR\_EL1.F0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- All of the following are true:
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL0
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- PMUSERENR\_EL0.IR == '1'
- Access to this field is WO/RAZ if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()

| F0   | Meaning               |
|------|-----------------------|
| 0b0  | PMICNTR_EL0 disabled. |
| 0b1  | PMICNTR_EL0 enabled.  |

- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- PSTATE.EL == EL0
- PMUSERENR\_EL0.IR == '1'
- Otherwise, access to this field is W1C.

## Otherwise:

Reserved, RES0.

## C, bit [31]

PMCCNTR\_EL0 disable. On writes, allows software to disable PMCCNTR\_EL0. On reads, returns the PMCCNTR\_EL0 enable status.

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | PMCCNTR_EL0 disabled. |
| 0b1 | PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;\_EL0 disable. On writes, allows software to disable PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the PMEVCNTR&lt;m&gt;\_EL0 enable status.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1C.

## Accessing PMCNTENCLR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMCNTENCLR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

| P<m>   | Meaning                   |
|--------|---------------------------|
| 0b0    | PMEVCNTR<m>_EL0 disabled. |
| 0b1    | PMEVCNTR<m>_EL0 enabled.  |

```
else X[t, 64] = PMCNTENCLR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCNTENCLR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCNTENCLR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCNTENCLR_EL0;
```

MSR PMCNTENCLR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCNTENCLR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCNTENCLR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCNTENCLR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMCNTENCLR_EL0 = X[t, 64];
```

## D24.5.7 PMCNTENSET\_EL0, Performance Monitors Count Enable Set Register

The PMCNTENSET\_EL0 characteristics are:

## Purpose

Allows software to enable the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which counters are enabled.

## Configuration

AArch64 System register PMCNTENSET\_EL0 bits [63:0] are architecturally mapped to AArch64 System register PMCNTENCLR\_EL0[63:0].

AArch64 System register PMCNTENSET\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCNTENSET[31:0].

AArch64 System register PMCNTENSET\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCNTENCLR[31:0].

AArch64 System register PMCNTENSET\_EL0 bits [31:0] are architecturally mapped to External register PMCNTENSET\_EL0[31:0].

AArch64 System register PMCNTENSET\_EL0 bits [31:0] are architecturally mapped to External register PMCNTENCLR\_EL0[31:0].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMCNTENSET\_EL0 bits [63:32] are architecturally mapped to External register PMCNTENSET\_EL0[63:32].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMCNTENSET\_EL0 bits [63:32] are architecturally mapped to External register PMCNTENCLR\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCNTENSET\_EL0 are UNDEFINED.

## Attributes

PMCNTENSET\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| C 31 30   | P30 P29 29 P28 28 P27 27 P26 26 P25 25 P24 24 P23 23 P22 22 P21 21 P20 20 P19 19 P18 18 P17 17 P16 16 P15 15 P14 14 P13 13 P12 12 P11 11 P10 10 P9 9 P8 8 P7 7 P6 6 P5 5 P4 4 P3 3 P2 2 P1 1 P0 0   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Bits [63:33]

Reserved, RES0.

F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

PMICNTR\_EL0 enable. On writes, allows software to enable PMICNTR\_EL0. On reads, returns the PMICNTR\_EL0 enable status.

## The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- PSTATE.EL == EL0
- Any of the following are true:
- PMUSERENR\_EL0.UEN == '0'
- PMUACR\_EL1.F0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- All of the following are true:
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL0
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- PMUSERENR\_EL0.IR == '1'
- Access to this field is WO/RAZ if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()

| F0   | Meaning               |
|------|-----------------------|
| 0b0  | PMICNTR_EL0 disabled. |
| 0b1  | PMICNTR_EL0 enabled.  |

- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- PSTATE.EL == EL0
- PMUSERENR\_EL0.IR == '1'
- Otherwise, access to this field is W1S.

## Otherwise:

Reserved, RES0.

## C, bit [31]

PMCCNTR\_EL0 enable. On writes, allows software to enable PMCCNTR\_EL0. On reads, returns the PMCCNTR\_EL0 enable status.

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | PMCCNTR_EL0 disabled. |
| 0b1 | PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;\_EL0 enable. On writes, allows software to enable PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the PMEVCNTR&lt;m&gt;\_EL0 enable status.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1S.

## Accessing PMCNTENSET\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMCNTENSET_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

| P<m>   | Meaning                   |
|--------|---------------------------|
| 0b0    | PMEVCNTR<m>_EL0 disabled. |
| 0b1    | PMEVCNTR<m>_EL0 enabled.  |

```
else X[t, 64] = PMCNTENSET_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCNTENSET_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCNTENSET_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCNTENSET_EL0;
```

MSR PMCNTENSET\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCNTENSET_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMCNTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCNTENSET_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCNTENSET_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMCNTENSET_EL0 = X[t, 64];
```

## D24.5.8 PMCR\_EL0, Performance Monitors Control Register

The PMCR\_EL0 characteristics are:

## Purpose

Provides details of the Performance Monitors implementation, including the number of counters implemented, and configures and controls the counters.

## Configuration

AArch64 System register PMCR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMCR[31:0].

AArch64 System register PMCR\_EL0 bits [31:0] are architecturally mapped to External register PMCR\_EL0[31:0].

When FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMCR\_EL0 bits [63:32] are architecturally mapped to External register PMCR\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMCR\_EL0 are UNDEFINED.

## Attributes

PMCR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## FZS, bit [32]

## When FEAT\_SPEv1p2 is implemented:

Freeze-on-SPE event. Stop counters when PMBLIMITR\_EL1.{PMFZ,E} is {1,1} and profiling is stopped.

| FZS   | Meaning                                                                                   |
|-------|-------------------------------------------------------------------------------------------|
| 0b0   | Do not freeze on a Statistical Profiling Buffer Management event.                         |
| 0b1   | Affected counters do not count following a Statistical Profiling Buffer Management event. |

The pseudocode function SPEProfilingStopped describes when profiling is stopped.

The counters affected by this field are:

- The event counters in the first range.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

- If FEAT\_SPE\_DPFZS is implemented and PMCR\_EL0.DP is 1, the cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

When FEAT\_SPE\_DPFZS is not implemented or PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA32 is implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IMP, bits [31:24]

## When FEAT\_PMUv3p7 is not implemented:

Implementer code.

If this field is zero, then PMCR\_EL0.IDCODE is RES0 and software must use MIDR\_EL1 to identify the PE.

Otherwise, this field and PMCR\_EL0.IDCODE identify the PMU implementation to software. The implementer codes are allocated by Arm. A nonzero value has the same interpretation as MIDR\_EL1.Implementer.

This field has an IMPLEMENTATION DEFINED value.

Arm deprecates use of this field.

Access to this field is RO.

## Otherwise:

Reserved, RAZ.

## IDCODE, bits [23:16]

## When PMCR\_EL0.IMP != '00000000':

Identification code. Arm deprecates use of this field.

Each implementer must maintain a list of identification codes that are specific to the implementer. A specific implementation is identified by the combination of the implementer code and the identification code.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## N, bits [15:11]

Indicates the number of event counters implemented. This value is in the range of 0b00000 -0b11111 . If the value is 0b00000 , then only PMCCNTR\_EL0 is implemented. If the value is 0b11111 , then PMCCNTR\_EL0 and 31 event counters are implemented.

When EL2 is implemented and enabled for the current Security state, reads of this field from EL1 and EL0 return the Effective value of MDCR\_EL2.HPMN.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bit [10]

Reserved, RES0.

## FZO, bit [9]

## When FEAT\_PMUv3p7 is implemented:

Freeze-on-overflow. Stop event counters on overflow.

| FZO   | Meaning                                                                                                                                                                                                                                     |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Do not freeze on overflow.                                                                                                                                                                                                                  |
| 0b1   | Affected counters do not count when any of the following applies:                                                                                                                                                                           |
|       | • For any event counter PMEVCNTR<m>_EL0 in the first range, PMOVSCLR_EL0[m] is 1, and either FEAT_SEBEP is not implemented or PMEVTYPER<m>_EL0.SYNC is 0. • FEAT_PMUv3_ICNTR is implemented, PMOVSCLR_EL0.F0 is 1, and either FEAT_SEBEP is |
|       | not implemented or PMICFILTR_EL0.SYNC is 0.                                                                                                                                                                                                 |

The counters affected by this field are:

- The event counters in the first range.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- If PMCR\_EL0.DP is 1, the cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [8]

Reserved, RES0.

## LP, bit [7]

## When FEAT\_PMUv3p5 is implemented:

Long event counter enable. Determines when unsigned overflow is recorded by PMOVSCLR\_EL0.P[n].

| LP   | Meaning                                                                                     |
|------|---------------------------------------------------------------------------------------------|
| 0b0  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[31:0]. |
| 0b1  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

The counters affected by this field are the event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

Other event counters and PMCCNTR\_EL0 are not affected by this field.

When FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0 is not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LC, bit [6]

## When FEAT\_AA32 is implemented:

Long cycle counter enable. Determines when unsigned overflow is recorded by PMOVSCLR\_EL0.C.

| LC   | Meaning                                                                                 |
|------|-----------------------------------------------------------------------------------------|
| 0b0  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR_EL0[31:0]. |
| 0b1  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

Arm deprecates use of PMCR\_EL0.LC = 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

DP, bit [5]

When ((HaveEL(EL3) || (IsFeatureImplemented(FEAT\_PMUv3p1) &amp;&amp; HaveEL(EL2))) || IsFeatureImplemented(FEAT\_PMUv3p7)) || IsFeatureImplemented(FEAT\_SPE\_DPFZS):

Disable cycle counter when event counting is prohibited.

| DP   | Meaning                                                          |
|------|------------------------------------------------------------------|
| 0b0  | Cycle counting by PMCCNTR_EL0 is not affected by this mechanism. |

| DP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1  | Cycle counting by PMCCNTR_EL0 is disabled in prohibited regions and when event counting is frozen: • If FEAT_PMUv3p1 is implemented, EL2 is implemented, and MDCR_EL2.HPMD is 1, then cycle counting by PMCCNTR_EL0 is disabled at EL2. • If FEAT_SPE_DPFZS is implemented and event counting is frozen by PMCR_EL0.FZS, then cycle counting by PMCCNTR_EL0 is disabled. • If FEAT_PMUv3p7 is implemented and event counting is frozen by PMCR_EL0.FZO, then cycle counting by PMCCNTR_EL0 is disabled. • If FEAT_PMUv3p7 is implemented, EL3 is implemented, and MDCR_EL3.MPMX is 1, then cycle counting by PMCCNTR_EL0 is disabled at EL3. • If EL3 is implemented, MDCR_EL3.SPME is 0, and either FEAT_PMUv3p7 is not implemented or MDCR_EL3.MPMX is 0, then cycle counting by PMCCNTR_EL0 is disabled at EL3 and in Secure state. |

The conditions when this field disables the cycle counter are the same as when event counting by an event counter in the first range is prohibited or frozen. For more information about event counter ranges, see MDCR\_EL2.HPMN.

If FEAT\_PMUv3p7 and FEAT\_SPEv1p2 are implemented, meaning PMCR\_EL0.FZS is implemented, and FEAT\_SPE\_DPFZS is not implemented, then cycle counting by PMCCNTR\_EL0 is not affected by PMCR\_EL0.FZS.

For more information, see 'Prohibiting event and cycle counting'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## X, bit [4]

## When the implementation includes a PMU event export bus:

Enable export of events in an IMPLEMENTATION DEFINED PMU event export bus.

| X   | Meaning                             |
|-----|-------------------------------------|
| 0b0 | Do not export events.               |
| 0b1 | Export events where not prohibited. |

This field enables the exporting of events over an IMPLEMENTATION DEFINED PMU event export bus to another device.

No events are exported when counting is prohibited.

This field does not affect the generation of Performance Monitors overflow interrupt requests or signaling to a cross-trigger interface (CTI) that can be implemented as signals exported from the PE.

If FEAT\_ETE is implemented, this field does not affect the use of PMU events as an External Input by the trace unit.

If FEAT\_ETMv4 is implemented, this field does affect the use of PMU events as an External Input by the trace unit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## D, bit [3]

## When FEAT\_AA32 is implemented:

Clock divider.

| D   | Meaning                                                      |
|-----|--------------------------------------------------------------|
| 0b0 | When enabled, PMCCNTR_EL0 counts every clock cycle.          |
| 0b1 | When enabled, PMCCNTR_EL0 counts once every 64 clock cycles. |

If the Effective value of PMCR\_EL0.LC is 1, then this field is ignored and the cycle counter counts every clock cycle.

Arm deprecates use of PMCR\_EL0.D = 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## C, bit [2]

Cycle counter reset. The effects of writing to this field are:

| C   | Meaning                    |
|-----|----------------------------|
| 0b0 | No action.                 |
| 0b1 | Reset PMCCNTR_EL0 to zero. |

Note

Resetting PMCCNTR\_EL0 does not change the cycle counter overflow field. The value of PMCR\_EL0.LC is ignored, and bits [63:0] of the cycle counter are reset.

Access to this field is WO/RAZ.

## P, bit [1]

Event counter reset.

| P   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | No action.                                                 |
| 0b1 | Reset all affected event counters PMEVCNTR<n>_EL0 to zero. |

The event counters affected by this field are:

- All event counters in the first range.
- If any of the following are true, all event counters in the second range:
- EL2 is disabled or not implemented in the current Security state.
- The PE is executing at EL2 or EL3.

Writes to this field do not affect other event counters, the cycle counter PMCCNTR\_EL0, or the instruction counter PMICNTR\_EL0.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

Note

Resetting the event counters does not change the event counter overflow fields. If FEAT\_PMUv3p5 is implemented, the values of MDCR\_EL2.HLP and PMCR\_EL0.LP are ignored, and bits [63:0] of all affected event counters are reset.

Access to this field is WO/RAZ.

## E, bit [0]

Enable.

| E   | Meaning                                          |
|-----|--------------------------------------------------|
| 0b0 | Affected counters are disabled and do not count. |
| 0b1 | Affected counters are enabled by PMCNTENSET_EL0. |

The counters affected by this field are:

- The event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- The cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing PMCR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMCR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' || (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1') ↪ → then
```

```
if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMCR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMCR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMCR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMCR_EL0;
```

MSR PMCR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' || (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMCR_EL0 == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMCR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMCR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPMCR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMCR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMCR_EL0 = X[t, 64];
```

## D24.5.9 PMECR\_EL1, Performance Monitors Extended Control Register (EL1)

The PMECR\_EL1 characteristics are:

## Purpose

Provides EL1 configuration options for the Performance Monitors.

## Configuration

This register is present only when (FEAT\_EBEP is implemented or FEAT\_PMUv3\_SS is implemented) and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMECR\_EL1 are UNDEFINED.

## Attributes

PMECR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:5]

Reserved, RES0.

## SSE, bits [4:3]

## When FEAT\_PMUv3\_SS is implemented:

Snapshot Enable. Controls the generation of Capture events.

| SSE   | Meaning                                    |
|-------|--------------------------------------------|
| 0b00  | Capture events are disabled.               |
| 0b10  | Capture events are enabled and prohibited. |
| 0b11  | Capture events are enabled and allowed.    |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:
- When the highest implemented Exception level is EL1, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## KPME, bit [2]

## When FEAT\_EBEP is implemented:

Local (Kernel) PMU Exception Enable. Enables PMU Profiling exceptions taken to the current Exception level.

| KPME   | Meaning                                                                                      |
|--------|----------------------------------------------------------------------------------------------|
| 0b0    | PMUProfiling exceptions taken to the current Exception level are disabled.                   |
| 0b1    | PMUProfiling exceptions taken to the current Exception level are not affected by this field. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMEE, bits [1:0]

## When FEAT\_EBEP is implemented:

Performance Monitors Exception Enable. Controls the generation of the PMUIRQ signal and the PMU Profiling exception at EL0 and EL1.

| PMEE   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b00   | The PMUIRQ signal is asserted on a PMUoverflow, and the PMUProfiling exception is disabled. |
| 0b11   | The PMUIRQ signal is deasserted, and the PMUProfiling exception is enabled.                 |

All other values are reserved.

This field is ignored by the PE when any of the following are true:

- All of the following are true:
- EL3 is implemented.
- MDCR\_EL3.PMEE != 0b01 .
- All of the following are true:
- EL2 is implemented and enabled in the current Security State.
- MDCR\_EL2.PMEE != 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing PMECR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMECR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b101 |

```
if !((IsFeatureImplemented(FEAT_EBEP) || IsFeatureImplemented(FEAT_PMUv3_SS)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMECR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMECR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMECR_EL1;
```

MSR PMECR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b101 |

```
if !((IsFeatureImplemented(FEAT_EBEP) || IsFeatureImplemented(FEAT_PMUv3_SS)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMECR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMECR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMECR_EL1 = X[t, 64];
```

## D24.5.10 PMEVCNTR&lt;n&gt;\_EL0, Performance Monitors Event Count Registers, n = 0 - 30

The PMEVCNTR&lt;n&gt;\_EL0 characteristics are:

## Purpose

Holds event counter n, which counts events, where n is 0 to 30.

## Configuration

AArch64 System register PMEVCNTR&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMEVCNTR&lt;n&gt;[31:0].

AArch64 System register PMEVCNTR&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to External register PMEVCNTR\_EL0[31:0].

When FEAT\_PMUv3p5 is implemented, AArch64 System register PMEVCNTR&lt;n&gt;\_EL0 bits [63:32] are architecturally mapped to External register PMEVCNTR\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMEVCNTR&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

PMEVCNTR&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

When FEAT\_PMUv3p5 is implemented:

Event counter n

63

32

Event counter n

31

0

<!-- image -->

## EVCNT, bits [63:0]

Event counter n. Value of event counter n, where n is the number of this register and is a number from 0 to 30. The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## EVCNT, bits [31:0]

Event counter n. Value of event counter n, where n is the number of this register and is a number from 0 to 30.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVCNTR&lt;n&gt;\_EL0

PMEVCNTR&lt;n&gt;\_EL0 can also be accessed by using PMXEVCNTR\_EL0 with PMSELR\_EL0.SEL set to the value of &lt;n&gt;.

If FEAT\_FGT is implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMEVCNTR&lt;n&gt;\_EL0 is as follows:

- If &lt;n&gt; is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then reads and writes of PMEVCNTR&lt;n&gt;\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP .
- Accesses to the register behave as if &lt;n&gt; is an UNKNOWN value less-than-or-equal-to the index of the highest accessible event counter.
- If EL2 is implemented and enabled in the current Security state, and &lt;n&gt; is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMEVCNTR&lt;n&gt;\_EL0 are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.P&lt;n&gt; == 0.

Permitted writes of PMEVCNTR&lt;n&gt;\_EL0 are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.{UEN,ER} == {1,1}.

## Note

In EL0, an access is permitted if it is enabled by PMUSERENR\_EL0.{UEN,ER,EN}.

If EL2 is implemented and enabled in the current Security state, in EL1 and EL0, MDCR\_EL2.HPMN identifies the number of accessible event counters. Otherwise, the number of accessible event counters is the number of implemented event counters. For more information, see MDCR\_EL2.HPMN.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMEVCNTR<m>_EL0 ; Where m = 0-30
```

| op0   | op1   | CRn    | CRm          | op2    |
|-------|-------|--------|--------------|--------|
| 0b11  | 0b011 | 0b1110 | 0b10 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1[m] == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMEVCNTR_EL0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVCNTR_EL0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVCNTR_EL0[m]; elsif PSTATE.EL == EL3 then X[t, 64] = PMEVCNTR_EL0[m];
```

MSR PMEVCNTR&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-30

| op0   | op1   | CRn    | CRm          | op2    |
|-------|-------|--------|--------------|--------|
| 0b11  | 0b011 | 0b1110 | 0b10 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1[m] == '0' || ↪ → PMUSERENR_EL0.ER == '1') then return; else PMEVCNTR_EL0[m] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMEVCNTR_EL0[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMEVCNTR_EL0[m] = X[t, 64]; elsif PSTATE.EL == EL3 then PMEVCNTR_EL0[m] = X[t, 64];
```

## D24.5.11 PMEVCNTSVR&lt;n&gt;\_EL1, Performance Monitors Event Count Saved Value Registers, n = 0 - 30

The PMEVCNTSVR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Captures the PMU Event counter &lt;n&gt;, PMEVCNTR&lt;n&gt;\_EL0.

## Configuration

AArch64 System register PMEVCNTSVR&lt;n&gt;\_EL1 bits [63:0] are architecturally mapped to External register PMEVCNTSVR\_EL1[63:0].

This register is present only when FEAT\_PMUv3\_SS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMEVCNTSVR&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

PMEVCNTSVR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

EVCNT

63

32

EVCNT

31

0

## EVCNT, bits [63:0]

Sampled Event Count. The value of PMEVCNTR&lt;n&gt;\_EL0 at the last successful Capture event.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVCNTSVR&lt;n&gt;\_EL1

If &lt;n&gt; is greater-than-or-equal-to the Effective value of PMCCR.EPMN, then direct reads of PMEVCNTSVR&lt;n&gt;\_EL1 are UNDEFINED.

Otherwise, direct reads of PMEVCNTSVR&lt;n&gt;\_EL1 generate a Trap exception to EL2 when all of the following are true:

- &lt;n&gt; is greater-than-or-equal-to the number of snapshot registers accessible at the current Exception level.
- EL2 is implemented and enabled in the current Security state.
- The access is from EL1.

Note

If EL2 is implemented and enabled in the current Security state, MDCR\_EL2.HPMN identifies the number of accessible snapshot registers at EL1. Otherwise, the number of accessible snapshot registers is the number of implemented event counters. See MDCR\_EL2.HPMN for more details.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm          | op2    |
|-------|-------|--------|--------------|--------|
| 0b10  | 0b000 | 0b1110 | 0b10 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_PMUv3_SS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMSSDATA == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVCNTSVR_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVCNTSVR_EL1[m]; elsif PSTATE.EL == EL3 then X[t, 64] = PMEVCNTSVR_EL1[m];
```

## D24.5.12 PMEVTYPER&lt;n&gt;\_EL0, Performance Monitors Event Type Registers, n = 0 - 30

The PMEVTYPER&lt;n&gt;\_EL0 characteristics are:

## Purpose

Configures event counter n, where n is 0 to 30.

## Configuration

AArch64 System register PMEVTYPER&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMEVTYPER&lt;n&gt;[31:0].

AArch64 System register PMEVTYPER&lt;n&gt;\_EL0 bits [31:0] are architecturally mapped to External register PMEVTYPER\_EL0[31:0].

When FEAT\_PMUv3\_TH is implemented, or FEAT\_PMUv3p8 is implemented, or FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_SME is implemented, AArch64 System register PMEVTYPER&lt;n&gt;\_EL0 bits [63:32] are architecturally mapped to External register PMEVTYPER\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMEVTYPER&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

PMEVTYPER&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## TC, bits [63:61]

When (IsFeatureImplemented(FEAT\_PMUv3\_TH) &amp;&amp; ((!IsFeatureImplemented(FEAT\_PMUv3\_EDGE)) || (PMEVTYPER&lt;n&gt;\_EL0.TE == '0'))) &amp;&amp; (((!IsFeatureImplemented(FEAT\_PMUv3\_TH2)) || ((n MOD 2) == 0)) || (PMEVTYPER&lt;n&gt;\_EL0.TLC IN {'0x'})):

Threshold Control. Defines the threshold function. In the description of this field:

- VB[n] is the value the event specified by PMEVTYPER&lt;n&gt;\_EL0 would increment event counter n by on a processor cycle if the threshold function is disabled.
- For odd values of n, V[n-1] is the value that event counter n-1 increments by on the same processor cycle. V[n-1] is the result of applying the threshold and edge functions on event counter n-1. If event counter n-1 is disabled, then V[n-1] is zero. V[n-1] is not defined for even values of n.
- TH[n] is the value of PMEVTYPER&lt;n&gt;\_EL0.TH.

| TC    | Meaning                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------|
| 0b000 | Not-equal. The counter increments byV B [n] on each processor cycle whenV B [n] is not equal to TH[n].   |
| 0b001 | Not-equal, count. The counter increments by 1 on each processor cycle whenV B [n] is not equal to TH[n]. |

| TC    | Meaning                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b010 | Equals. The counter increments byV B [n] on each processor cycle whenV B [n] is equal to TH[n].                                  |
| 0b011 | Equals, count. The counter increments by 1 on each processor cycle whenV B [n] is equal to TH[n].                                |
| 0b100 | Greater-than-or-equal. The counter increments byV B [n] on each processor cycle whenV B [n] is greater than or equal to TH[n].   |
| 0b101 | Greater-than-or-equal, count. The counter increments by 1 on each processor cycle whenV B [n] is greater than or equal to TH[n]. |
| 0b110 | Less-than. The counter increments byV B [n] on each processor cycle whenV B [n] is less than TH[n].                              |
| 0b111 | Less-than, count. The counter increments by 1 on each processor cycle whenV B [n] is less than TH[n].                            |

Comparisons treat VB[n] and TH[n] as unsigned integer values.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC[2:1] is true:

- If PMEVTYPER&lt;n&gt;\_EL0.TC[0] is 0, then the counter increments by VB[n].
- If PMEVTYPER&lt;n&gt;\_EL0.TC[0] is 1, then the counter increments by 1.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC[2:1] is false:

- If FEAT\_PMUv3\_TH2 is implemented, n is odd, and PMEVTYPER&lt;n&gt;\_EL0.TLC is 0b01 , then the counter increments by V[n-1].
- Otherwise, the counter does not increment.

If PMEVTYPER&lt;n&gt;\_EL0.{TC, TLC, TH} are zero, then the threshold function is disabled.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '000' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## When FEAT\_PMUv3\_TH2 is implemented, PMEVTYPER&lt;n&gt;\_EL0.TE == '0', (n MOD 2) == 1, and PMEVTYPER&lt;n&gt;\_EL0.TLC == '10':

Threshold Control. Defines the threshold function. In the description of this field:

- VB[n] is the value the event specified by PMEVTYPER&lt;n&gt;\_EL0 would increment event counter n by on a processor cycle if the threshold function is disabled.
- V[n-1] is the value that event counter n-1 increments by on the same processor cycle. V[n-1] is the result of applying the threshold and edge functions on event counter n-1. If event counter n-1 is disabled, then V[n-1] is zero.
- TH[n] is the value of PMEVTYPER&lt;n&gt;\_EL0.TH.

| TC    | Meaning                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b000 | Not-equal. The counter increments by V[n-1] on each processor cycle whenV B [n] is not equal to TH[n].                         |
| 0b010 | Equals. The counter increments by V[n-1] on each processor cycle whenV B [n] is equal to TH[n].                                |
| 0b100 | Greater-than-or-equal. The counter increments by V[n-1] on each processor cycle whenV B [n] is greater than or equal to TH[n]. |
| 0b110 | Less-than. The counter increments by V[n-1] on each processor cycle whenV B [n] is less than TH[n].                            |

All other values are reserved.

Comparisons treat VB[n] and TH[n] as unsigned integer values.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is true, the counter increments by V[n-1].

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is false, the counter does not increment.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '000' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## When FEAT\_PMUv3\_EDGE is implemented and PMEVTYPER&lt;n&gt;\_EL0.TE == '1':

Threshold Control. Defines the threshold function. In the description of this field:

- VB[n] is the value the event specified by PMEVTYPER&lt;n&gt;\_EL0 would increment event counter n by on a processor cycle if the threshold function is disabled.
- For odd values of n, V[n-1] is the value that event counter n-1 increments by on the same processor cycle. V[n-1] is the result of applying the threshold and edge functions on event counter n-1. If event counter n-1 is disabled, then V[n-1] is zero. V[n-1] is not defined for even values of n.
- TH[n] is the value of PMEVTYPER&lt;n&gt;\_EL0.TH.

| TC    | Meaning                                                                                                                                                                                                                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b001 | Equal to not-equal. The counter increments on each processor cycle whenV B [n] is not equal to TH[n] andV B [n] was equal to TH[n] on the previous processor cycle.                                                                                                                                                          |
| 0b010 | Equal to/from not-equal. The counter increments on each processor cycle when either: • V B [n] is not equal to TH[n] andV B [n] was equal to TH[n] on the previous processor cycle. • V B [n] is equal to TH[n] andV B [n] was not equal to TH[n] on the previous processor cycle.                                           |
| 0b011 | Not-equal to equal. The counter increments on each processor cycle whenV B [n] is equal to TH[n] and V B [n] was not equal to TH[n] on the previous processor cycle.                                                                                                                                                         |
| 0b101 | Less-than to greater-than-or-equal. The counter increments on each processor cycle whenV B [n] is greater than or equal to TH[n] andV B [n] was less than TH[n] on the previous processor cycle.                                                                                                                             |
| 0b110 | Less-than to/from greater-than-or-equal. The counter increments on each processor cycle when either: • V B [n] is greater than or equal to TH[n] andV B [n] was less than TH[n] on the previous processor cycle. • V B [n] is less than TH[n] andV B [n] was greater than or equal to TH[n] on the previous processor cycle. |
| 0b111 | Greater-than-or-equal to less-than. The counter increments on each processor cycle whenV B [n] is less than TH[n] andV B [n] was greater than or equal to TH[n] on the previous processor cycle.                                                                                                                             |

All other values are reserved.

Comparisons treat VB[n] and TH[n] as unsigned integer values.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is true:

- If FEAT\_PMUv3\_TH2 is implemented, n is odd, and PMEVTYPER&lt;n&gt;\_EL0.TLC is 0b10 , then the counter increments by V[n-1].
- Otherwise, the counter increments by 1.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is false, the counter does not increment.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '000' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TE, bit [60]

## When FEAT\_PMUv3\_EDGE is implemented:

Threshold Edge. Enables the edge condition. When PMEVTYPER&lt;n&gt;\_EL0.TE is 1, the event counter increments on cycles when the result of the threshold condition changes. See PMEVTYPER&lt;n&gt;\_EL0.TC for more information.

| TE   | Meaning                            |
|------|------------------------------------|
| 0b0  | Threshold edge condition disabled. |
| 0b1  | Threshold edge condition enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [59]

Reserved, RES0.

## SYNC, bit [58]

## When FEAT\_SEBEP is implemented:

Synchronous mode. Controls whether a PMU Profiling exception generated by the counter is synchronous or asynchronous.

| SYNC   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Asynchronous PMUProfiling exception is enabled. |
| 0b1    | Synchronous PMUProfiling exception is enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VS, bits [57:56]

## When FEAT\_PMUv3\_SME is implemented:

SVE mode filtering. Controls counting events in Streaming and Non-streaming SVE modes.

| VS   | Meaning                                                  |
|------|----------------------------------------------------------|
| 0b00 | This mechanism has no effect on the filtering of events. |
| 0b01 | The PE does not count events in Streaming SVE mode.      |
| 0b10 | The PE does not count events in Non-streaming SVE mode.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLC, bits [55:54]

## When FEAT\_PMUv3\_TH2 is implemented and (n MOD 2) == 1:

Threshold Linking Control. Extends PMEVTYPER&lt;n&gt;\_EL0.TC with additional controls for event linking. See PMEVTYPER&lt;n&gt;\_EL0.TC.

| TLC   | Meaning                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | Threshold linking disabled.                                                                                                                                                                               |
| 0b01  | Threshold linking enabled. If the threshold condition described by PMEVTYPER<n>_EL0.TC is false, the counter increments by V[n-1]. Otherwise, the counter increments as described by PMEVTYPER<n>_EL0.TC. |
| 0b10  | Threshold linking enabled. If the threshold condition described by PMEVTYPER<n>_EL0.TC is true, the counter increments by V[n-1]. Otherwise, the counter does not increment.                              |

All other values are reserved.

See PMEVTYPER&lt;n&gt;\_EL0.TC for more information

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [53:44]

Reserved, RES0.

## TH, bits [43:32]

## When FEAT\_PMUv3\_TH is implemented:

Threshold value. Provides the unsigned value for the threshold function defined by PMEVTYPER&lt;n&gt;\_EL0.TC.

If PMEVTYPER&lt;n&gt;\_EL0.{TC, TH} are both zero and either FEAT\_PMUv3\_TH2 is not implemented or PMEVTYPER&lt;n&gt;\_EL0.TLC is also zero, then the threshold function is disabled.

If PMMIR\_EL1.THWIDTH is less than 12, then bits

PMEVTYPER&lt;n&gt;\_EL0.TH[11:UInt(PMMIR\_EL1.THWIDTH)] are RES0. This accounts for the behavior when writing a value greater-than-or-equal-to 2 UInt(PMMIR\_EL1.THWIDTH) .

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to 0x000 .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## P, bit [31]

EL1 filtering. Controls counting events in EL1.

| P   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of events. |
| 0b1 | The PE does not count events in EL1.                 |

If Secure and Non-secure states are implemented, then counting events in Non-secure EL1 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.NSK.

If FEAT\_RME is implemented, then counting events in Realm EL1 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.RLK.

If EL3 is implemented, then counting events in EL3 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.M.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

EL0 filtering. Controls counting events in EL0.

| U   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of events. |
| 0b1 | The PE does not count events in EL0.                 |

If Secure and Non-secure states are implemented, then counting events in Non-secure EL0 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.NSU.

If FEAT\_RME is implemented, then counting events in Realm EL0 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting events in Non-secure EL1. If PMEVTYPER&lt;n&gt;\_EL0.NSK is not equal to PMEVTYPER&lt;n&gt;\_EL0.P, then the PE does not count events in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of events in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.P == 1, the PE does not count events in Non-secure EL1. |
| 0b1   | When PMEVTYPER<n>_EL0.P == 0, the PE does not count events in Non-secure EL1. When PMEVTYPER<n>_EL0.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting events in Non-secure EL0. If PMEVTYPER&lt;n&gt;\_EL0.NSU is not equal to PMEVTYPER&lt;n&gt;\_EL0.U, then the PE does not count events in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of events in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.U == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.U == 1, the PE does not count events in Non-secure EL0. |
| 0b1   | When PMEVTYPER<n>_EL0.U == 0, the PE does not count events in Non-secure EL0. When PMEVTYPER<n>_EL0.U == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting events in EL2.

| NSH   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE does not count events in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of events. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting events in Secure EL2 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.SH.

If FEAT\_RME is implemented, then counting events in Realm EL2 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.RLH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## M, bit [26]

## When EL3 is implemented:

EL3 filtering. Controls counting events in EL3. If PMEVTYPER&lt;n&gt;\_EL0.M is not equal to PMEVTYPER&lt;n&gt;\_EL0.P, then the PE does not count events in EL3. Otherwise, this mechanism has no effect on filtering of events in EL3.

| M   | Meaning                                                                                                                                               |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When PMEVTYPER<n>_EL0.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.P == 1, the PE does not count events in EL3. |
| 0b1 | When PMEVTYPER<n>_EL0.P == 0, the PE does not count events in EL3. When PMEVTYPER<n>_EL0.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MT, bit [25]

When FEAT\_MTPMU is implemented or an IMPLEMENTATION DEFINED multi-threaded PMU extension is implemented:

Multithreading.

| MT   | Meaning                                                                          |
|------|----------------------------------------------------------------------------------|
| 0b0  | Count events only on controlling PE.                                             |
| 0b1  | Count events from any PE with the same affinity at level 1 and above as this PE. |

## Unless otherwise stated:

- If the event counts PE cycles when a stall condition is true and a second condition is true, then the counter counts Processor cycles when the stall condition is true for all of these PEs, and the second condition is true for any of these PEs.
- If the event counts PE cycles when any other condition is true, then the counter counts Processor cycles when the condition is true for any of these PEs.
- Otherwise, the event counts by the sum of the count across all of these PEs.

For the stall events, the stall condition means the applicable condition described by the STALL, STALL\_FRONTEND, or STALL\_BACKEND event.

The second condition is any condition in addition to this.

For example, for the STALL\_FRONTEND\_L1I event, the stall condition is STALL\_FRONTEND, and the second condition is when there is a demand instruction miss in the first level of instruction cache.

For the STALL, STALL\_FRONTEND, and STALL\_BACKEND events themselves, the second condition is the null TRUE condition.

See 'Multithreaded implementations' and 'Cycle event counting in multithreaded implementations'.

From Armv8.6, the IMPLEMENTATION DEFINED multi-threaded PMU extension is not permitted, meaning if FEAT\_MTPMU is not implemented, this field is RES0. See ID\_AA64DFR0\_EL1.MTPMU.

This field is ignored by the PE and treated as zero when FEAT\_MTPMU is implemented and disabled.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SH, bit [24]

## When EL3 is implemented and FEAT\_SEL2 is implemented:

Secure EL2 filtering. Controls counting events in Secure EL2. If PMEVTYPER&lt;n&gt;\_EL0.SH is equal to PMEVTYPER&lt;n&gt;\_EL0.NSH, then the PE does not count events in Secure EL2. Otherwise, this mechanism has no effect on filtering of events in Secure EL2.

| SH   | Meaning                                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMEVTYPER<n>_EL0.NSH == 0, the PE does not count events in Secure EL2. When PMEVTYPER<n>_EL0.NSH == 1, this mechanism has no effect on filtering of events. |

| SH   | Meaning                                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1  | When PMEVTYPER<n>_EL0.NSH == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.NSH == 1, the PE does not count events in Secure EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

When Secure EL2 is not implemented, access to this field is RES0.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## RLK, bit [22]

## When FEAT\_RME is implemented:

Realm EL1 filtering. Controls counting events in Realm EL1. If PMEVTYPER&lt;n&gt;\_EL0.RLK is not equal to PMEVTYPER&lt;n&gt;\_EL0.P, then the PE does not count events in Realm EL1. Otherwise, this mechanism has no effect on filtering of events in Realm EL1.

| RLK   | Meaning                                                                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.P == 1, the PE does not count events in Realm EL1. |
| 0b1   | When PMEVTYPER<n>_EL0.P == 0, the PE does not count events in Realm EL1. When PMEVTYPER<n>_EL0.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting events in Realm EL0. If PMEVTYPER&lt;n&gt;\_EL0.RLU is not equal to PMEVTYPER&lt;n&gt;\_EL0.U, then the PE does not count events in Realm EL0. Otherwise, this mechanism has no effect on filtering of events in Realm EL0.

| RLU   | Meaning                                                                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.U == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.U == 1, the PE does not count events in Realm EL0. |
| 0b1   | When PMEVTYPER<n>_EL0.U == 0, the PE does not count events in Realm EL0. When PMEVTYPER<n>_EL0.U == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLH, bit [20]

## When FEAT\_RME is implemented:

Realm EL2 filtering. Controls counting events in Realm EL2. If PMEVTYPER&lt;n&gt;\_EL0.RLH is equal to PMEVTYPER&lt;n&gt;\_EL0.NSH, then the PE does not count events in Realm EL2. Otherwise, this mechanism has no effect on filtering of events in Realm EL2.

| RLH   | Meaning                                                                                                                                                         |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.NSH == 0, the PE does not count events in Realm EL2. When PMEVTYPER<n>_EL0.NSH == 1, this mechanism has no effect on filtering of events. |
| 0b1   | When PMEVTYPER<n>_EL0.NSH == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.NSH == 1, the PE does not count events in Realm EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [19:16]

Reserved, RES0.

evtCount[15:10], bits [15:10]

## When FEAT\_PMUv3p1 is implemented:

Extension to evtCount[9:0]. For more information, see evtCount[9:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## evtCount[9:0], bits [9:0]

Event to count.

The event number of the event that is counted by event counter PMEVCNTR&lt;n&gt;\_EL0.

The ranges of event numbers allocated to each type of event are shown in 'Allocation of the PMU event number space'.

If FEAT\_PMUv3p8 is implemented and PMEVTYPER&lt;n&gt;\_EL0.evtCount is programmed to an event that is reserved or not supported by the PE, no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is the value written to the field.

Note

Arm recommends this behavior for all implementations of FEAT\_PMUv3.

Otherwise, if PMEVTYPER&lt;n&gt;\_EL0.evtCount is programmed to an event that is reserved or not supported by the PE, the behavior depends on the value written:

- For the range 0x0000 to 0x003F , no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is the value written to the field.
- If FEAT\_PMUv3p1 is implemented, for the range 0x4000 to 0x403F , no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is the value written to the field.
- For other values, it is UNPREDICTABLE what event, if any, is counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is UNKNOWN.

Note

UNPREDICTABLE means the event must not expose privileged information.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVTYPER&lt;n&gt;\_EL0

PMEVTYPER&lt;n&gt;\_EL0 can also be accessed by using PMXEVTYPER\_EL0 with PMSELR\_EL0.SEL set to n.

If FEAT\_FGT is implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMEVTYPER&lt;n&gt;\_EL0 is as follows:

- If &lt;n&gt; is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then reads and writes of PMEVTYPER&lt;n&gt;\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP .
- Accesses to the register behave as if &lt;n&gt; is an UNKNOWN value less-than-or-equal-to the index of the highest accessible event counter.
- If EL2 is implemented and enabled in the current Security state, and &lt;n&gt; is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMEVTYPER&lt;n&gt;\_EL0 are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.P&lt;n&gt; == 0.

Permitted writes of PMEVTYPER&lt;n&gt;\_EL0 are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.{UEN,ER} == {1,1}.

Note

In EL0, an access is permitted if it is enabled by PMUSERENR\_EL0.{UEN,EN}.

If EL2 is implemented and enabled in the current Security state, in EL1 and EL0, MDCR\_EL2.HPMN identifies the number of accessible event counters. Otherwise, the number of accessible event counters is the number of implemented event counters. For more information, see MDCR\_EL2.HPMN.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMEVTYPER<m>_EL0 ; Where m = 0-30
```

| op0   | op1   | CRn    | CRm          | op2    |
|-------|-------|--------|--------------|--------|
| 0b11  | 0b011 | 0b1110 | 0b11 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMEVTYPERn_EL0 == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1[m] == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMEVTYPER_EL0[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVTYPER_EL0[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVTYPER_EL0[m]; elsif PSTATE.EL == EL3 then X[t, 64] = PMEVTYPER_EL0[m];
```

MSR PMEVTYPER&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-30

| op0   | op1   | CRn    | CRm          | op2    |
|-------|-------|--------|--------------|--------|
| 0b11  | 0b011 | 0b1110 | 0b11 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then
```

then

```
if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1[m] == '0' || ↪ → PMUSERENR_EL0.ER == '1') then return; else PMEVTYPER_EL0[m] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMEVTYPER_EL0[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMEVTYPER_EL0[m] = X[t, 64]; elsif PSTATE.EL == EL3 then PMEVTYPER_EL0[m] = X[t, 64];
```

## D24.5.13 PMIAR\_EL1, Performance Monitors Instruction Address Register

The PMIAR\_EL1 characteristics are:

## Purpose

Captures the address of the instruction generating a PMU Profiling exception.

## Configuration

This register is present only when FEAT\_SEBEP is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMIAR\_EL1 are UNDEFINED.

## Attributes

PMIAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      | 32   |
|---------|------|
| ADDRESS | 0    |
| 31      |      |
| ADDRESS |      |

## ADDRESS, bits [63:0]

Instruction virtual address.

For writes to PMIAR\_EL1, PMIAR\_EL1.ADDRESS[63:P] is RESS. P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

PMIAR\_EL1.ADDRESS[1:0] is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMIAR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMIAR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_SEBEP) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMIAR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMIAR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMIAR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMIAR_EL1;
```

MSR PMIAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_SEBEP) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMIAR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMIAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMIAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMIAR_EL1 = X[t, 64];
```

## D24.5.14 PMICFILTR\_EL0, Performance Monitors Instruction Counter Filter Register

The PMICFILTR\_EL0 characteristics are:

## Purpose

Configures the Instruction Counter.

## Configuration

AArch64 System register PMICFILTR\_EL0 bits [63:0] are architecturally mapped to External register PMICFILTR\_EL0[63:0].

This register is present only when FEAT\_PMUv3\_ICNTR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMICFILTR\_EL0 are UNDEFINED.

## Attributes

PMICFILTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:59]

Reserved, RES0.

## SYNC, bit [58]

## When FEAT\_SEBEP is implemented:

Synchronous mode. Controls whether a PMU Profiling exception generated by the counter is synchronous or asynchronous.

| SYNC   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Asynchronous PMUProfiling exception is enabled. |
| 0b1    | Synchronous PMUProfiling exception is enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

VS, bits [57:56]

## When FEAT\_PMUv3\_SME is implemented:

SVE mode filtering. Controls counting instructions in Streaming and Non-streaming SVE modes.

| VS   | Meaning                                                        |
|------|----------------------------------------------------------------|
| 0b00 | This mechanism has no effect on the filtering of instructions. |
| 0b01 | The PE does not count instructions in Streaming SVE mode.      |
| 0b10 | The PE does not count instructions in Non-streaming SVE mode.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [55:32]

Reserved, RES0.

## P, bit [31]

EL1 filtering. Controls counting instructions in EL1.

| P   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of instructions. |
| 0b1 | The PE does not count instructions in EL1.                 |

If Secure and Non-secure states are implemented, then counting instructions in Non-secure EL1 is further controlled by PMICFILTR\_EL0.NSK.

If FEAT\_RME is implemented, then counting instructions in Realm EL1 is further controlled by PMICFILTR\_EL0.RLK.

If EL3 is implemented, then counting instructions in EL3 is further controlled by PMICFILTR\_EL0.M.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:

## U, bit [30]

EL0 filtering. Controls counting instructions in EL0.

| U   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of instructions. |
| 0b1 | The PE does not count instructions in EL0.                 |

If Secure and Non-secure states are implemented, then counting instructions in Non-secure EL0 is further controlled by PMICFILTR\_EL0.NSU.

If FEAT\_RME is implemented, then counting instructions in Realm EL0 is further controlled by PMICFILTR\_EL0.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting instructions in Non-secure EL1. If PMICFILTR\_EL0.NSK is not equal to PMICFILTR\_EL0.P, then the PE does not count instructions in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of instructions in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.P == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.P == 1, the PE does not count instructions in Non-secure EL1. |
| 0b1   | When PMICFILTR_EL0.P == 0, the PE does not count instructions in Non-secure EL1. When PMICFILTR_EL0.P == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting instructions in Non-secure EL0. If PMICFILTR\_EL0.NSU is not equal to PMICFILTR\_EL0.U, then the PE does not count instructions in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of instructions in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.U == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.U == 1, the PE does not count instructions in Non-secure EL0. |
| 0b1   | When PMICFILTR_EL0.U == 0, the PE does not count instructions in Non-secure EL0. When PMICFILTR_EL0.U == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting instructions in EL2.

| NSH   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | The PE does not count instructions in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of instructions. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting instructions in Secure EL2 is further controlled by PMICFILTR\_EL0.SH.

If FEAT\_RME is implemented, then counting instructions in Realm EL2 is further controlled by PMICFILTR\_EL0.RLH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

M, bit [26]

## When EL3 is implemented:

EL3 filtering. Controls counting instructions in EL3. If PMICFILTR\_EL0.M is not equal to PMICFILTR\_EL0.P, then the PE does not count instructions in EL3. Otherwise, this mechanism has no effect on filtering of instructions in EL3.

| M   | Meaning                                                                                                                                                     |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When PMICFILTR_EL0.P == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.P == 1, the PE does not count instructions in EL3. |
| 0b1 | When PMICFILTR_EL0.P == 0, the PE does not count instructions in EL3. When PMICFILTR_EL0.P == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [25]

Reserved, RES0.

## SH, bit [24]

## When EL3 is implemented and FEAT\_SEL2 is implemented:

Secure EL2 filtering. Controls counting instructions in Secure EL2. If PMICFILTR\_EL0.SH is equal to PMICFILTR\_EL0.NSH, then the PE does not count instructions in Secure EL2. Otherwise, this mechanism has no effect on filtering of instructions in Secure EL2.

| SH   | Meaning                                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMICFILTR_EL0.NSH == 0, the PE does not count instructions in Secure EL2. When PMICFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of instructions. |
| 0b1  | When PMICFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.NSH == 1, the PE does not count instructions in Secure EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

When Secure EL2 is not implemented, access to this field is RES0.

## Otherwise:

Reserved, RES0.

Bit [23]

Reserved, RES0.

## RLK, bit [22]

## When FEAT\_RME is implemented:

Realm EL1 filtering. Controls counting instructions in Realm EL1. If PMICFILTR\_EL0.RLK is not equal to PMICFILTR\_EL0.P, then the PE does not count instructions in Realm EL1. Otherwise, this mechanism has no effect on filtering of instructions in Realm EL1.

| RLK   | Meaning                                                                                                                                                           |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.P == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.P == 1, the PE does not count instructions in Realm EL1. |
| 0b1   | When PMICFILTR_EL0.P == 0, the PE does not count instructions in Realm EL1. When PMICFILTR_EL0.P == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting instructions in Realm EL0. If PMICFILTR\_EL0.RLU is not equal to PMICFILTR\_EL0.U, then the PE does not count instructions in Realm EL0. Otherwise, this mechanism has no effect on filtering of instructions in Realm EL0.

| RLU   | Meaning                                                                                                                                                           |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.U == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.U == 1, the PE does not count instructions in Realm EL0. |
| 0b1   | When PMICFILTR_EL0.U == 0, the PE does not count instructions in Realm EL0. When PMICFILTR_EL0.U == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.

- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLH, bit [20]

## When FEAT\_RME is implemented:

Realm EL2 filtering. Controls counting instructions in Realm EL2. If PMICFILTR\_EL0.RLH is equal to PMICFILTR\_EL0.NSH, then the PE does not count instructions in Realm EL2. Otherwise, this mechanism has no effect on filtering of instructions in Realm EL2.

| RLH   | Meaning                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.NSH == 0, the PE does not count instructions in Realm EL2. When PMICFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of instructions. |
| 0b1   | When PMICFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.NSH == 1, the PE does not count instructions in Realm EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [19:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count.

Reads as 0x0008

Access to this field is RO.

## Accessing PMICFILTR\_EL0

Permitted reads and writes of PMICFILTR\_EL0 are RAZ/WI if all of the following are true:

```
· PSTATE.EL == EL0. · PMUACR_EL1.F0 == 0.
```

Permitted writes of PMICFILTR\_EL0 are ignored if all of the following are true:

- PSTATE.EL == EL0.
- PMUSERENR\_EL0.IR == 1.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b0110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_ICNTR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.UEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nPMICFILTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.F0 == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMICFILTR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMICFILTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMICFILTR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED;
```

```
elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMICFILTR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMICFILTR_EL0;
```

MSR PMICFILTR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b0110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_ICNTR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.UEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nPMICFILTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.F0 == '0' || ↪ → PMUSERENR_EL0.IR == '1') then return; else PMICFILTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMICFILTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMICFILTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMICFILTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMICFILTR_EL0 = X[t, 64];
```

## D24.5.15 PMICNTR\_EL0, Performance Monitors Instruction Counter Register

The PMICNTR\_EL0 characteristics are:

## Purpose

If event counting is not prohibited and the instruction counter is enabled, the counter increments for each architecturally-executed instruction, according to the configuration specified by PMICFILTR\_EL0.

## Configuration

AArch64 System register PMICNTR\_EL0 bits [63:0] are architecturally mapped to External register PMICNTR\_EL0[63:0].

This register is present only when FEAT\_PMUv3\_ICNTR is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMICNTR\_EL0 are UNDEFINED.

## Attributes

PMICNTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## ICNT, bits [63:0]

Instruction Counter.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMICNTR\_EL0

PMICNTR\_EL0 treats permitted reads-as-zero and ignores permitted writes if all of the following are true:

- PSTATE.EL == EL0.
- PMUACR\_EL1.F0 == 0.

PMICNTR\_EL0 ignores permitted writes if all of the following are true:

- PSTATE.EL == EL0.
- PMUSERENR\_EL0.IR == 1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMICNTR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_ICNTR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.UEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nPMICNTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.F0 == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMICNTR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMICNTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMICNTR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED;
```

```
elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMICNTR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMICNTR_EL0;
```

MSR PMICNTR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_ICNTR) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.UEN == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nPMICNTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.F0 == '0' || ↪ → PMUSERENR_EL0.IR == '1') then return; else PMICNTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMICNTR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMICNTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMICNTR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMICNTR_EL0 = X[t, 64];
```

## D24.5.16 PMICNTSVR\_EL1, Performance Monitors Instruction Count Saved Value Register

The PMICNTSVR\_EL1 characteristics are:

## Purpose

Captures the PMU Instruction counter, PMICNTR\_EL0.

## Configuration

AArch64 System register PMICNTSVR\_EL1 bits [63:0] are architecturally mapped to External register PMICNTSVR\_EL1[63:0].

This register is present only when FEAT\_PMUv3\_ICNTR is implemented, FEAT\_PMUv3\_SS is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMICNTSVR\_EL1 are UNDEFINED.

## Attributes

PMICNTSVR\_EL1 is a 64-bit register.

## Field descriptions

ICNT

63

32

ICNT

31

0

<!-- image -->

## ICNT, bits [63:0]

Sampled Instruction Count. The value of PMICNTR\_EL0 at the last successful Capture event.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMICNTSVR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1110 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_ICNTR) && IsFeatureImplemented(FEAT_PMUv3_SS) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMSSDATA == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMICNTSVR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMICNTSVR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMICNTSVR_EL1;
```

## D24.5.17 PMINTENCLR\_EL1, Performance Monitors Interrupt Enable Clear Register

The PMINTENCLR\_EL1 characteristics are:

## Purpose

Allows software to disable the generation of interrupt requests or, when FEAT\_EBEP is implemented, PMU Profiling exceptions on overflows from the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which overflow interrupt requests or PMU Profiling exceptions are enabled.

## Configuration

AArch64 System register PMINTENCLR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register PMINTENSET\_EL1[63:0].

AArch64 System register PMINTENCLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register PMINTENCLR[31:0].

AArch64 System register PMINTENCLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register PMINTENSET[31:0].

AArch64 System register PMINTENCLR\_EL1 bits [31:0] are architecturally mapped to External register PMINTENCLR\_EL1[31:0].

AArch64 System register PMINTENCLR\_EL1 bits [31:0] are architecturally mapped to External register PMINTENSET\_EL1[31:0].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMINTENCLR\_EL1 bits [63:32] are architecturally mapped to External register PMINTENCLR\_EL1[63:32].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMINTENCLR\_EL1 bits [63:32] are architecturally mapped to External register PMINTENSET\_EL1[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMINTENCLR\_EL1 are UNDEFINED.

## Attributes

PMINTENCLR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 31 30 29 28 27 26   | 16 15 14 13 12 11   |
|---------------------|---------------------|

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of

PMICNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 enable status.

| F0   | Meaning                                                                                   |
|------|-------------------------------------------------------------------------------------------|
| 0b0  | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 disabled. |
| 0b1  | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL1
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- All of the following are true:
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is WO/RAZ if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL1
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL1
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Otherwise, access to this field is W1C.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of

PMCCNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable status.

| C   | Meaning                                                                                   |
|-----|-------------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 disabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing PMINTENCLR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMINTENCLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMINTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMINTENCLR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMINTENCLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMINTENCLR_EL1;
```

MSR PMINTENCLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMINTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
PMINTENCLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMINTENCLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMINTENCLR_EL1 = X[t, 64];
```

## D24.5.18 PMINTENSET\_EL1, Performance Monitors Interrupt Enable Set Register

The PMINTENSET\_EL1 characteristics are:

## Purpose

Allows software to enable the generation of interrupt requests or, when FEAT\_EBEP is implemented, PMU Profiling exceptions on overflows from the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which overflow interrupt requests or PMU Profiling exceptions are enabled.

## Configuration

AArch64 System register PMINTENSET\_EL1 bits [63:0] are architecturally mapped to AArch64 System register PMINTENCLR\_EL1[63:0].

AArch64 System register PMINTENSET\_EL1 bits [31:0] are architecturally mapped to AArch32 System register PMINTENSET[31:0].

AArch64 System register PMINTENSET\_EL1 bits [31:0] are architecturally mapped to AArch32 System register PMINTENCLR[31:0].

AArch64 System register PMINTENSET\_EL1 bits [31:0] are architecturally mapped to External register PMINTENSET\_EL1[31:0].

AArch64 System register PMINTENSET\_EL1 bits [31:0] are architecturally mapped to External register PMINTENCLR\_EL1[31:0].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMINTENSET\_EL1 bits [63:32] are architecturally mapped to External register PMINTENSET\_EL1[63:32].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMINTENSET\_EL1 bits [63:32] are architecturally mapped to External register PMINTENCLR\_EL1[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMINTENSET\_EL1 are UNDEFINED.

## Attributes

PMINTENSET\_EL1 is a 64-bit register.

## Field descriptions

| 63   | 33 32   |
|------|---------|
|      | F0      |

| 31 30 29 28 27 26   | 16 15 14 13 12 11   |
|---------------------|---------------------|

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of

PMICNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 enable status.

| F0   | Meaning                                                                                   |
|------|-------------------------------------------------------------------------------------------|
| 0b0  | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 disabled. |
| 0b1  | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL1
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- All of the following are true:
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is WO/RAZ if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL1
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL1
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Otherwise, access to this field is W1S.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0.

On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable status.

| C   | Meaning                                                                                   |
|-----|-------------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 disabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing PMINTENSET\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMINTENSET_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMINTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMINTENSET_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMINTENSET_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMINTENSET_EL1;
```

MSR PMINTENSET\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMINTEN == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
PMINTENSET_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMINTENSET_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMINTENSET_EL1 = X[t, 64];
```

## D24.5.19 PMMIR\_EL1, Performance Monitors Machine Identification Register

The PMMIR\_EL1 characteristics are:

## Purpose

Describes Performance Monitors parameters specific to the implementation to software.

## Configuration

AArch64 System register PMMIR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register PMMIR[31:0].

When FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p4 is implemented, AArch64 System register PMMIR\_EL1 bits [31:0] are architecturally mapped to External register PMMIR[31:0].

When (IsFeatureImplemented(FEAT\_PMUv3\_EXT) &amp;&amp; IsFeatureImplemented(FEAT\_PMUv3p4)) &amp;&amp; (IsFeatureImplemented(FEAT\_PMUv3\_EXT64) || IsFeatureImplemented(FEAT\_PMUv3p9)), AArch64 System register PMMIR\_EL1 bits [63:32] are architecturally mapped to External register PMMIR[63:32].

This register is present only when FEAT\_PMUv3p4 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMMIR\_EL1 are UNDEFINED.

## Attributes

PMMIR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |          |       |           |     |       | 32   |
|------|----------|-------|-----------|-----|-------|------|
| 31   | 29 28 27 | 24 23 | 20 19     | 8 7 |       | 0    |
|      | SME      | EDGE  | BUS_WIDTH |     | SLOTS |      |

## Bits [63:29]

Reserved, RES0.

## SME, bit [28]

PMUv3 for SME. Adds support for the Streaming SVE mode filter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SME   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Streaming SVE mode filter not implemented.      |
| 0b1   | Adds support for the Streaming SVE mode filter. |

All other values are reserved.

FEAT\_PMUv3\_SME implements the functionality identified by the value 1.

Access to this field is RO.

## EDGE, bits [27:24]

PMUevent edge detection. With PMMIR\_EL1.THWIDTH, indicates implementation of event counter thresholding features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EDGE   | Meaning                                                                              |
|--------|--------------------------------------------------------------------------------------|
| 0b0000 | FEAT_PMUv3_EDGE is not implemented.                                                  |
| 0b0001 | FEAT_PMUv3_EDGE is implemented.                                                      |
| 0b0010 | As 0b0001 , and adds support for threshold value linking between a pair of counters. |

All other values are reserved.

If FEAT\_PMUv3\_TH is not implemented, the only permitted value is 0b0000 .

FEAT\_PMUv3\_EDGE implements the functionality identified by the value 0b0001 .

FEAT\_PMUv3\_TH2 implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## THWIDTH, bits [23:20]

PMEVTYPER&lt;n&gt;\_EL0.TH width. Indicates implementation of the FEAT\_PMUv3\_TH feature, and, if implemented, the size of the PMEVTYPER&lt;n&gt;\_EL0.TH field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| THWIDTH   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0000    | FEAT_PMUv3_TH is not implemented.             |
| 0b0001    | 1 bit. PMEVTYPER<n>_EL0.TH[11:1] are RES0.    |
| 0b0010    | 2 bits. PMEVTYPER<n>_EL0.TH[11:2] are RES0.   |
| 0b0011    | 3 bits. PMEVTYPER<n>_EL0.TH[11:3] are RES0.   |
| 0b0100    | 4 bits. PMEVTYPER<n>_EL0.TH[11:4] are RES0.   |
| 0b0101    | 5 bits. PMEVTYPER<n>_EL0.TH[11:5] are RES0.   |
| 0b0110    | 6 bits. PMEVTYPER<n>_EL0.TH[11:6] are RES0.   |
| 0b0111    | 7 bits. PMEVTYPER<n>_EL0.TH[11:7] are RES0.   |
| 0b1000    | 8 bits. PMEVTYPER<n>_EL0.TH[11:8] are RES0.   |
| 0b1001    | 9 bits. PMEVTYPER<n>_EL0.TH[11:9] are RES0.   |
| 0b1010    | 10 bits. PMEVTYPER<n>_EL0.TH[11:10] are RES0. |
| 0b1011    | 11 bits. PMEVTYPER<n>_EL0.TH[11] is RES0.     |
| 0b1100    | 12 bits.                                      |

All other values are reserved.

If FEAT\_PMUv3\_TH is not implemented, this field is zero.

Otherwise, the largest value that can be written to PMEVTYPER&lt;n&gt;\_EL0.TH is 2 (PMMIR\_EL1.THWIDTH) minus one.

Access to this field is RO.

## BUS\_WIDTH, bits [19:16]

Bus width. Indicates the number of bytes each BUS\_ACCESS event relates to. Encoded as Log2(number of bytes), plus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BUS_WIDTH   | Meaning                           |
|-------------|-----------------------------------|
| 0b0000      | The information is not available. |
| 0b0011      | Four bytes.                       |
| 0b0100      | 8 bytes.                          |
| 0b0101      | 16 bytes.                         |
| 0b0110      | 32 bytes.                         |
| 0b0111      | 64 bytes.                         |
| 0b1000      | 128 bytes.                        |
| 0b1001      | 256 bytes.                        |
| 0b1010      | 512 bytes.                        |
| 0b1011      | 1024 bytes.                       |
| 0b1100      | 2048 bytes.                       |

All other values are reserved.

Each transfer is up to this number of bytes. An access might be smaller than the bus width.

When this field is nonzero, each access counted by BUS\_ACCESS is at most BUS\_WIDTH bytes. An implementation might treat a wide bus as multiple narrower buses, such that a wide access on the bus increments the BUS\_ACCESS counter by more than one.

Access to this field is RO.

## BUS\_SLOTS, bits [15:8]

Bus count. The largest value by which the BUS\_ACCESS event might increment in a single BUS\_CYCLES cycle.

This field has an IMPLEMENTATION DEFINED value.

When this field is nonzero, the largest value by which the BUS\_ACCESS event might increment in a single BUS\_CYCLES cycle is BUS\_SLOTS.

If the bus count information is not available, this field will read as zero.

Access to this field is RO.

## SLOTS, bits [7:0]

Operation width. The largest value by which the STALL\_SLOT event might increment in a single cycle. If the STALL\_SLOT event is not implemented, this field might read as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMMIR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMMIR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_PMUv3p4) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMMIR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMMIR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMMIR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMMIR_EL1;
```

## D24.5.20 PMOVSCLR\_EL0, Performance Monitors Overflow Flag Status Clear Register

The PMOVSCLR\_EL0 characteristics are:

## Purpose

Allows software to clear the unsigned overflow flags for the following counters to 0:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows the current unsigned overflow flag values.

## Configuration

AArch64 System register PMOVSCLR\_EL0 bits [63:0] are architecturally mapped to AArch64 System register PMOVSSET\_EL0[63:0].

AArch64 System register PMOVSCLR\_EL0 bits [63:0] are architecturally mapped to External register PMOVS[63:0].

AArch64 System register PMOVSCLR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMOVSR[31:0].

AArch64 System register PMOVSCLR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMOVSSET[31:0].

AArch64 System register PMOVSCLR\_EL0 bits [31:0] are architecturally mapped to External register PMOVSCLR\_EL0[31:0].

AArch64 System register PMOVSCLR\_EL0 bits [31:0] are architecturally mapped to External register PMOVSSET\_EL0[31:0].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMOVSCLR\_EL0 bits [63:32] are architecturally mapped to External register PMOVSCLR\_EL0[63:32].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMOVSCLR\_EL0 bits [63:32] are architecturally mapped to External register PMOVSSET\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMOVSCLR\_EL0 are UNDEFINED.

## Attributes

PMOVSCLR\_EL0 is a 64-bit register.

## Field descriptions

| C 31 30   | P30 P29 29 P28 28 P27 27 P26 26 P25 25 P24 24 P23 23 P22 22 P21 21 P20 20 P19 19 P18 18 P17 17 P16 16 P15 15 P14 14 P13 13 P12 12 P11 11 P10 10 P9 9 P8 8 P7 7 P6 6 P5 5 P4 4 P3 3 P2 2 P1 1 P0 0   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

Bits [63:33]

Reserved, RES0.

F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Unsigned overflow flag for PMICNTR\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMICNTR\_EL0 to 0. On reads, returns the unsigned overflow flag for PMICNTR\_EL0 overflow status.

| F0   | Meaning                         |
|------|---------------------------------|
| 0b0  | PMICNTR_EL0 has not overflowed. |
| 0b1  | PMICNTR_EL0 has overflowed.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- PSTATE.EL == EL0
- Any of the following are true:
- PMUSERENR\_EL0.UEN == '0'
- PMUACR\_EL1.F0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- All of the following are true:
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL0
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- PMUSERENR\_EL0.IR == '1'
- Access to this field is WO/RAZ if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented

- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- PSTATE.EL == EL0
- PMUSERENR\_EL0.IR == '1'
- Otherwise, access to this field is W1C.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Unsigned overflow flag for PMCCNTR\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMCCNTR\_EL0 to 0. On reads, returns the unsigned overflow flag for PMCCNTR\_EL0 overflow status.

| C   | Meaning                         |
|-----|---------------------------------|
| 0b0 | PMCCNTR_EL0 has not overflowed. |
| 0b1 | PMCCNTR_EL0 has overflowed.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 to 0. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 overflow status.

| P<m>   | Meaning                             |
|--------|-------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1C.

## Accessing PMOVSCLR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMOVSCLR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMOVSCLR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMOVSCLR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMOVSCLR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMOVSCLR_EL0;
```

MSR PMOVSCLR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else PMOVSCLR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMOVSCLR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMOVSCLR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMOVSCLR_EL0 = X[t, 64];
```

## D24.5.21 PMOVSSET\_EL0, Performance Monitors Overflow Flag Status Set Register

The PMOVSSET\_EL0 characteristics are:

## Purpose

Allows software to set the unsigned overflow flags for the following counters to 1:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows the current unsigned overflow flag values.

## Configuration

AArch64 System register PMOVSSET\_EL0 bits [63:0] are architecturally mapped to AArch64 System register PMOVSCLR\_EL0[63:0].

AArch64 System register PMOVSSET\_EL0 bits [63:0] are architecturally mapped to External register PMOVS[63:0].

AArch64 System register PMOVSSET\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMOVSSET[31:0].

AArch64 System register PMOVSSET\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMOVSR[31:0].

AArch64 System register PMOVSSET\_EL0 bits [31:0] are architecturally mapped to External register PMOVSCLR\_EL0[31:0].

AArch64 System register PMOVSSET\_EL0 bits [31:0] are architecturally mapped to External register PMOVSSET\_EL0[31:0].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMOVSSET\_EL0 bits [63:32] are architecturally mapped to External register PMOVSCLR\_EL0[63:32].

When FEAT\_PMUv3p9 is implemented or FEAT\_PMUv3\_EXT64 is implemented, AArch64 System register PMOVSSET\_EL0 bits [63:32] are architecturally mapped to External register PMOVSSET\_EL0[63:32].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMOVSSET\_EL0 are UNDEFINED.

## Attributes

PMOVSSET\_EL0 is a 64-bit register.

## Field descriptions

| C 31 30   | P30 P29 29 P28 28 P27 27 P26 26 P25 25 P24 24 P23 23 P22 22 P21 21 P20 20 P19 19 P18 18 P17 17 P16 16 P15 15 P14 14 P13 13 P12 12 P11 11 P10 10 P9 9 P8 8 P7 7 P6 6 P5 5 P4 4 P3 3 P2 2 P1 1 P0 0   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

Bits [63:33]

Reserved, RES0.

F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Unsigned overflow flag for PMICNTR\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMICNTR\_EL0 to 1. On reads, returns the unsigned overflow flag for PMICNTR\_EL0 overflow status.

| F0   | Meaning                         |
|------|---------------------------------|
| 0b0  | PMICNTR_EL0 has not overflowed. |
| 0b1  | PMICNTR_EL0 has overflowed.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- PSTATE.EL == EL0
- Any of the following are true:
- PMUSERENR\_EL0.UEN == '0'
- PMUACR\_EL1.F0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- All of the following are true:
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL == EL0
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- PMUSERENR\_EL0.IR == '1'
- Access to this field is WO/RAZ if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'

- HDFGRTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICFILTR\_EL0 == '0'
- Access to this field is RO if all of the following are true:
- PSTATE.EL == EL0
- PMUSERENR\_EL0.IR == '1'
- Otherwise, access to this field is W1S.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Unsigned overflow flag for PMCCNTR\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMCCNTR\_EL0 to 1. On reads, returns the unsigned overflow flag for PMCCNTR\_EL0 overflow status.

| C   | Meaning                         |
|-----|---------------------------------|
| 0b0 | PMCCNTR_EL0 has not overflowed. |
| 0b1 | PMCCNTR_EL0 has overflowed.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 to 1. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 overflow status.

| P<m>   | Meaning                             |
|--------|-------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1S.

## Accessing PMOVSSET\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMOVSSET_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1110 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMOVSSET_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMOVSSET_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMOVSSET_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMOVSSET_EL0;
```

MSR PMOVSSET\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1110 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else PMOVSSET_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMOVS == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMOVSSET_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMOVSSET_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMOVSSET_EL0 = X[t, 64];
```

## D24.5.22 PMSELR\_EL0, Performance Monitors Event Counter Selection Register

The PMSELR\_EL0 characteristics are:

## Purpose

Selects the current event counter PMEVCNTR&lt;n&gt;\_EL0 or the cycle counter PMCCNTR\_EL0.

Used in conjunction with PMXEVTYPER\_EL0 to determine the event that increments a selected counter, and the modes and states in which the selected counter increments.

Used in conjunction with PMXEVCNTR\_EL0 to determine the value of a selected counter.

## Configuration

AArch64 System register PMSELR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMSELR[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMSELR\_EL0 are UNDEFINED.

## Attributes

PMSELR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

|   63 |
|------|
|   31 |

## Bits [63:5]

Reserved, RES0.

## SEL, bits [4:0]

Event counter select. Selects the counter accessed by subsequent accesses to PMXEVTYPER\_EL0 and PMXEVCNTR\_EL0.

| SEL                | Meaning                                                                                                                                                                                             |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00000 .. 0b11110 | Select event counter PMEVCNTR<n>_EL0, where n is the value of this field: • MRS and MSR of PMXEVTYPER_EL0 access PMEVTYPER<n>_EL0. • MRS and MSR of PMXEVCNTR_EL0 access PMEVCNTR<n>_EL0.           |
| 0b11111            | Select the cycle counter, PMCCNTR_EL0: • MRS and MSR of PMXEVTYPER_EL0 access PMCCFILTR_EL0. • MRS and MSR of PMXEVCNTR_EL0 are CONSTRAINED UNPREDICTABLE. For more information, see PMXEVCNTR_EL0. |

If FEAT\_FGT is not implemented and this field is set to a value greater than or equal to the number of implemented counters, but not equal to 31, then direct reads of this field return an UNKNOWN value.

For more information about the results of accesses to the event counters, including when PMSELR\_EL0.SEL is set to the index of an unimplemented or inaccessible event counter, see PMXEVTYPER\_EL0 and PMXEVCNTR\_EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSELR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSELR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMSELR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSELR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMSELR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSELR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSELR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMSELR_EL0;
```

MSR PMSELR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMSELR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSELR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSELR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSELR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSELR_EL0 = X[t, 64];
```

```
elsif PSTATE.EL == EL3 then PMSELR_EL0 = X[t, 64];
```

## D24.5.23 PMSSCR\_EL1, Performance Monitors Snapshot Status and Capture Register

The PMSSCR\_EL1 characteristics are:

## Purpose

Holds status information about the captured counters and provides a mechanism for software to initiate a sample.

## Configuration

AArch64 System register PMSSCR\_EL1 bits [63:0] are architecturally mapped to External register PMSSCR\_EL1[63:0].

This register is present only when FEAT\_PMUv3\_SS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMSSCR\_EL1 are UNDEFINED.

## Attributes

PMSSCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 33 32   |
|------|---------|
| RES0 | NC      |
| 31   | 1 0     |
| RES0 | SS      |

## Bits [63:33]

Reserved, RES0.

## NC, bit [32]

No Capture. Indicates whether the PMU counters have been captured.

| NC   | Meaning                   |
|------|---------------------------|
| 0b0  | PMUcounters captured.     |
| 0b1  | PMUcounters not captured. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Bits [31:1]

Reserved, RES0.

## SS, bit [0]

Snapshot Capture and Status.

| SS   | Meaning                                                                              |
|------|--------------------------------------------------------------------------------------|
| 0b0  | On a read, the Capture event has completed.                                          |
| 0b1  | On a read, the Capture event has not completed. On a write, request a Capture event. |

Awrite of 0 to this field is ignored.

It is CONSTRAINED UNPREDICTABLE whether a Capture event has completed if this field is modified when the Capture event is ongoing.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When PMU capture events are disabled, access to this field is RO.
- Otherwise, access to this field is RW.

## Accessing PMSSCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMSSCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_SS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMSSCR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSSCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMSSCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMSSCR_EL1;
```

MSR PMSSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_PMUv3_SS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMSSCR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPMSS == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPMSS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSSCR_EL1 = X[t, 64];
```

## D24.5.24 PMSWINC\_EL0, Performance Monitors Software Increment Register

The PMSWINC\_EL0 characteristics are:

## Purpose

Increments a counter that is configured to count the Software increment event, event 0x00 . For more information, see 'SW\_INCR'.

## Configuration

AArch64 System register PMSWINC\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMSWINC[31:0].

When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p9 is not implemented, AArch64 System register PMSWINC\_EL0 bits [31:0] are architecturally mapped to External register PMSWINC\_EL0[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMSWINC\_EL0 are UNDEFINED.

## Attributes

PMSWINC\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:31]

Reserved, RES0.

P&lt;m&gt; , bits [m], for m = 30 to 0

Software increment.

| P<m>   | Meaning                                                                                         |
|--------|-------------------------------------------------------------------------------------------------|
| 0b0    | Write is ignored.                                                                               |
| 0b1    | Increment PMEVCNTR<m>_EL0, if PMEVCNTR<m>_EL0 is configured to count software increment events. |

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.SW] == '10'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Otherwise, access to this field is WO/RAZ.

RES0

## Accessing PMSWINC\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MSR PMSWINC\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1100 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,SW,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<SW,EN> == '00') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMSWINC_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSWINC_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMSWINC_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSWINC_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMSWINC_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMSWINC_EL0 = X[t, 64];
```

## D24.5.25 PMUACR\_EL1, Performance Monitors User Access Control Register

The PMUACR\_EL1 characteristics are:

## Purpose

Enables or disables EL0 access to specfic Performance Monitors.

## Configuration

This register is present only when FEAT\_PMUv3p9 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMUACR\_EL1 are UNDEFINED.

## Attributes

PMUACR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |
|------|

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

EL0 accesses to PMICNTR\_EL0 enable. With PMUSERENR\_EL0.UEN and PMUSERENR\_EL0.IR, controls EL0 accesses to PMICNTR\_EL0.

| F0   | Meaning                                                                                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | If the Effective value of PMUSERENR_EL0.UEN is 1, then EL0 accesses to PMICNTR_EL0 and associated controls are RAZ/WI, and permitted EL0 writes to PMZR_EL0.F0 are ignored.                |
| 0b1  | If the Effective value of PMUSERENR_EL0.UEN is 1, then EL0 accesses to PMICNTR_EL0 and associated controls are either read-only or read/write, depending on the value of PMUSERENR_EL0.IR. |

The controls associated with PMICNTR\_EL0 that are accessible at EL0 are PMCNTENSET\_EL0.F0, PMCNTENCLR\_EL0.F0, PMOVSSET\_EL0.F0, and PMOVSCLR\_EL0.F0.

This field is ignored by the PE when any of the following are true:

- EL1 is using AArch32.
- PMUSERENR\_EL0.UEN is 0.
- The access generates an exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## C, bit [31]

EL0 accesses to PMCCNTR\_EL0 enable. With PMUSERENR\_EL0.EN, PMUSERENR\_EL0.UEN, and PMUSERENR\_EL0.CR, controls EL0 accesses to PMCCNTR\_EL0.

| C   | Meaning                                                                                                                                                                                    |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | If the Effective value of PMUSERENR_EL0.UEN is 1, then EL0 accesses to PMCCNTR_EL0 and associated controls are RAZ/WI, and permitted EL0 writes to PMZR_EL0.C are ignored.                 |
| 0b1 | If the Effective value of PMUSERENR_EL0.UEN is 1, then EL0 accesses to PMCCNTR_EL0 and associated controls are either read-only or read/write, depending on the value of PMUSERENR_EL0.CR. |

The controls associated with PMCCNTR\_EL0 that are accessible at EL0 are PMCNTENSET\_EL0.C, PMCNTENCLR\_EL0.C, PMOVSSET\_EL0.C, and PMOVSCLR\_EL0.C.

This field is ignored by the PE when any of the following are true:

- EL1 is using AArch32.
- PMUSERENR\_EL0.UEN is 0.
- The access generates an exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## P&lt;m&gt; , bits [m], for m = 30 to 0

EL0 accesses to PMEVCNTR&lt;m&gt;\_EL0 enable. With PMUSERENR\_EL0.EN, PMUSERENR\_EL0.UEN, and PMUSERENR\_EL0.ER, controls EL0 accesses to PMEVCNTR&lt;m&gt;\_EL0.

| P<m>   | Meaning                                                                                                                                                                                        |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If the Effective value of PMUSERENR_EL0.UEN is 1, then EL0 accesses to PMEVCNTR<m>_EL0 and associated controls are RAZ/WI, and permitted EL0 writes to PMZR_EL0.P<m> are ignored.              |
| 0b1    | If the Effective value of PMUSERENR_EL0.UEN is 1, then EL0 accesses to PMEVCNTR<m>_EL0 and associated controls are either read-only or read/write, depending on the value of PMUSERENR_EL0.ER. |

The controls associated with PMEVCNTR&lt;m&gt;\_EL0 that are accessible at EL0 are PMCNTENSET\_EL0.P&lt;m&gt;, PMCNTENCLR\_EL0.P&lt;m&gt;, PMOVSSET\_EL0.P&lt;m&gt;, and PMOVSCLR\_EL0.P&lt;m&gt;.

This field is ignored by the PE when any of the following are true:

- EL1 is using AArch32.
- PMUSERENR\_EL0.UEN is 0.
- The access generates an exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Otherwise, access to this field is RW.

## Accessing PMUACR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMUACR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nPMUACR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMUACR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMUACR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = PMUACR_EL1;
```

MSR PMUACR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1110 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMUACR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMUACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMUACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then PMUACR_EL1 = X[t, 64];
```

## D24.5.26 PMUSERENR\_EL0, Performance Monitors User Enable Register

The PMUSERENR\_EL0 characteristics are:

## Purpose

Enables or disables EL0 access to the Performance Monitors.

## Configuration

AArch64 System register PMUSERENR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMUSERENR[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMUSERENR\_EL0 are UNDEFINED.

## Attributes

PMUSERENR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      | 32          |
|---------|-------------|
| RES0 31 | 3 2 1 0     |
| RES0    | ER CR SW EN |

## Bits [63:7]

Reserved, RES0.

## TID, bit [6]

## When FEAT\_PMUv3p9 is implemented:

Trap ID registers. Traps EL0 read access to common event identification registers.

| TID   | Meaning                                                                    |
|-------|----------------------------------------------------------------------------|
| 0b0   | Accesses to PMCEID<n>_EL0 and PMCEID<n> are not trapped by this mechanism. |
| 0b1   | EL0 read accesses to PMCEID<n>_EL0 and PMCEID<n> are trapped.              |

In AArch64 state, the register accesses affected by this control are:

- MRS reads of PMCEID0\_EL0 and PMCEID1\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MRC reads of PMCEID0, PMCEID1, PMCEID2, and PMCEID3.

When trapped, reads generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS reads are reported using EC syndrome value 0x18 .
- AArch32 MRC reads are reported using EC syndrome value 0x03 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IR, bit [5]

## When FEAT\_PMUv3\_ICNTR is implemented:

Instruction counter Read-only. When PMUSERENR\_EL0.UEN is 1, controls whether EL0 writes to instruction counter are ignored.

| IR   | Meaning                                                                                                                                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 accesses are not affected by this mechanism.                                                                                                                                                                                   |
| 0b1  | If the Effective value of PMUSERENR_EL0.UEN is 1, then all of the following apply at EL0: • Writes to PMICNTR_EL0 are ignored. • The controls associated with instruction counter are RAZ/WI. • Writes to PMZR_EL0.F0 are ignored. |

The controls associated with PMICNTR\_EL0 that are accessible at EL0 are PMCNTENSET\_EL0.F0, PMCNTENCLR\_EL0.F0, PMOVSSET\_EL0.F0, and PMOVSCLR\_EL0.F0.

Ignored writes are not trapped and do not generate an exception.

This field is ignored by the PE when any of the following are true:

- PMUSERENR\_EL0.UEN is 0.
- The access generates an exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UEN, bit [4]

## When FEAT\_PMUv3p9 is implemented:

User Enable, with access controlled by PMUACR\_EL1. Enables EL0 read/write access to PMU registers, other than PMCR\_EL0.

| UEN   | Meaning                                                                                                                                                                                                                                    |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If FEAT_PMUv3_ICNTR is implemented, then EL0 accesses to PMICFILTR_EL0 and PMICNTR_EL0 are trapped. EL0 accesses to the other specified PMUregisters, PMCR_EL0, and PMCRare trapped, unless enabled by PMUSERENR_EL0.{ER,CR,SW,EN}.        |
| 0b1   | EL0 accesses to the specified PMUregisters are enabled, unless trapped by another control. The behavior of permitted accesses is controlled by PMUSERENR_EL0.{ IR, ER,CR,SW} and PMUACR_EL1. EL0 accesses to PMCR_EL0 and PMCRare trapped. |

In AArch64 state, the register accesses affected by this control are:

- MRS or MSR accesses to the following registers:
- PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMOVSCLR\_EL0, PMOVSSET\_EL0, PMSELR\_EL0, PMXEVCNTR\_EL0, and PMXEVTYPER\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, PMICFILTR\_EL0 and PMICNTR\_EL0.
- MRS reads of PMCEID0\_EL0 and PMCEID1\_EL0.
- MSR writes to PMSWINC\_EL0 and PMZR\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MRC or MCR accesses to PMCCFILTR, PMCCNTR, PMCNTENCLR, PMCNTENSET, PMEVCNTR&lt;n&gt;, PMEVTYPER&lt;n&gt;, PMOVSR, PMOVSSET, PMSELR, PMXEVCNTR, and PMXEVTYPER.
- MRC reads of PMCEID0, PMCEID1, PMCEID2, and PMCEID3.
- MCR writes to PMSWINC.
- MRRC or MCRR accesses to PMCCNTR.

When trapped, reads and writes generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS and MSR accesses are reported using EC syndrome value 0x18 .
- AArch32 MRC and MCR accesses are reported using EC syndrome value 0x03 .
- AArch32 MRRC and MCRR accesses are reported using EC syndrome value 0x04 .

This field is ignored by the PE and treated as zero when EL1 is using AArch32.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ER, bit [3]

## When FEAT\_PMUv3p9 is implemented:

Event counters Read enable or Read-only.

When PMUSERENR\_EL0.{UEN,EN} is {0,0}, PMUSERENR\_EL0.ER enables EL0 reads of the event counters and EL0 reads and writes of the select register.

When PMUSERENR\_EL0.UEN is 1, EL0 reads of the event counters and EL0 writes to PMZR\_EL0 are enabled by PMUSERENR\_EL0.UEN, unless trapped by another control, and PMUSERENR\_EL0.ER controls the behavior of EL0 writes to the event counters and PMZR\_EL0.

| ER   | Meaning                                                                                                                                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMUSERENR_EL0.UEN == 0, EL0 reads of the event counters and EL0 reads and writes of the select register are disabled, unless enabled by PMUSERENR_EL0.EN. When PMUSERENR_EL0.UEN == 1, permitted EL0 writes are not affected by this mechanism.                   |
| 0b1  | When PMUSERENR_EL0.UEN == 0, EL0 reads of the event counters and EL0 reads and writes of the select register are enabled, unless trapped by another control. When PMUSERENR_EL0.UEN == 1, permitted EL0 writes to the event counters and PMZR_EL0.P[30:0] are ignored. |

In AArch64 state, the register accesses affected by this control are:

- When PMUSERENR\_EL0.{UEN,EN} is {0,0}:

- MRS reads of PMEVCNTR&lt;n&gt;\_EL0 and PMXEVCNTR\_EL0.
- MRS and MSR accesses to PMSELR\_EL0.
- When PMUSERENR\_EL0.UEN is 1, MSR writes to PMZR\_EL0.P&lt;n&gt;, PMEVCNTR&lt;n&gt;\_EL0, and PMXEVCNTR\_EL0.

In AArch32 state, the register accesses affected by this control are:

- When PMUSERENR\_EL0.{UEN,EN} is {0,0}:
- MRC reads of PMEVCNTR&lt;n&gt; and PMXEVCNTR.
- MRC and MCR accesses to PMSELR.
- When PMUSERENR\_EL0.UEN is 1, MCR writes to PMEVCNTR&lt;n&gt; and PMXEVCNTR.

When disabled, reads and writes generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS and MSR accesses are reported using EC syndrome value 0x18 .
- AArch32 MRC and MCR accesses are reported using EC syndrome value 0x03 .

Ignored writes are not trapped and do not generate an exception.

This field is ignored by the PE when PMUSERENR\_EL0.{UEN,EN} == {0,1}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Event counters Read enable.

When PMUSERENR\_EL0.EN is 0, PMUSERENR\_EL0.ER enables EL0 reads of the event counters and EL0 reads and writes of the select register.

| ER   | Meaning                                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 reads of the event counters and EL0 reads and writes of the select register are disabled, unless enabled by PMUSERENR_EL0.EN. |
| 0b1  | EL0 reads of the event counters and EL0 reads and writes of the select register are enabled, unless trapped by another control.   |

In AArch64 state, the register accesses affected by this control are:

- MRS reads of PMEVCNTR&lt;n&gt;\_EL0 and PMXEVCNTR\_EL0.
- MRS and MSR accesses to PMSELR\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MRC reads of PMEVCNTR&lt;n&gt; and PMXEVCNTR.
- MRC and MCR accesses to PMSELR.

When disabled, reads and writes generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS and MSR accesses are reported using EC syndrome value 0x18 .
- AArch32 MRC and MCR accesses are reported using EC syndrome value 0x03 .

This field is ignored by the PE when PMUSERENR\_EL0.EN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CR, bit [2]

## When FEAT\_PMUv3p9 is implemented:

Cycle counter Read enable or Read-only.

When PMUSERENR\_EL0.{UEN,EN} is {0,0}, PMUSERENR\_EL0.CR enables EL0 reads of the cycle counter.

When PMUSERENR\_EL0.UEN is 1, EL0 reads of the cycle counter and EL0 writes to PMZR\_EL0 are enabled by PMUSERENR\_EL0.UEN, unless trapped by another control, and PMUSERENR\_EL0.CR controls the behavior of EL0 writes to the cycle counter and PMZR\_EL0.

| CR   | Meaning                                                                                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMUSERENR_EL0.UEN == 0, EL0 reads of the cycle counter are disabled, unless enabled by PMUSERENR_EL0.EN. When PMUSERENR_EL0.UEN == 1, permitted EL0 writes are not affected by this mechanism.            |
| 0b1  | When PMUSERENR_EL0.UEN == 0, EL0 reads of the cycle counter are enabled, unless trapped by another control. When PMUSERENR_EL0.UEN == 1, permitted EL0 writes to the cycle counter and PMZR_EL0.C are ignored. |

In AArch64 state, the register accesses affected by this control are:

- When PMUSERENR\_EL0.{UEN,EN} is {0,0}, MRS reads of PMCCNTR\_EL0.
- When PMUSERENR\_EL0.UEN is 1, MSR writes to PMZR\_EL0.C and PMCCNTR\_EL0.

In AArch32 state, the register accesses affected by this control are:

- When PMUSERENR\_EL0.{UEN,EN} is {0,0}:
- MRC reads of PMCCNTR.
- MRRC reads of PMCCNTR.
- When PMUSERENR\_EL0.UEN is 1:
- MCR writes to PMCCNTR.
- MCRR writes to PMCCNTR.

When disabled, reads generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS reads are reported using EC syndrome value 0x18 .
- AArch32 MRC reads are reported using EC syndrome value 0x03 .
- AArch32 MRRC reads are reported using EC syndrome value 0x04 .

Ignored writes are not trapped and do not generate an exception.

This field is ignored by the PE when PMUSERENR\_EL0.{UEN,EN} == {0,1}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Cycle counter Read enable.

When PMUSERENR\_EL0.EN is 0, PMUSERENR\_EL0.CR enables EL0 reads of the cycle counter.

| CR   | Meaning                                                                          |
|------|----------------------------------------------------------------------------------|
| 0b0  | EL0 reads of the cycle counter are disabled, unless enabled by PMUSERENR_EL0.EN. |
| 0b1  | EL0 reads of the cycle counter are enabled, unless trapped by another control.   |

In AArch64 state, the register accesses affected by this control are:

- MRS reads of PMCCNTR\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MRC reads of PMCCNTR.
- MRRC reads of PMCCNTR.

When disabled, reads generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS reads are reported using EC syndrome value 0x18 .
- AArch32 MRC reads are reported using EC syndrome value 0x03 .
- AArch32 MRRC reads are reported using EC syndrome value 0x04 .

This field is ignored by the PE when PMUSERENR\_EL0.EN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SW, bit [1]

## When FEAT\_PMUv3p9 is implemented:

Software increment register Write enable.

When PMUSERENR\_EL0.UEN is 0, PMUSERENR\_EL0.SW enables EL0 writes to the Software increment register.

When PMUSERENR\_EL0.UEN is 1, EL0 writes to the Software increment register are enabled by PMUSERENR\_EL0.UEN, unless trapped by another control, and PMUSERENR\_EL0.SW controls the behavior of EL0 writes to the Software increment register.

| SW   | Meaning                                                                                                                                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMUSERENR_EL0.UEN == 0, EL0 writes to the Software increment register are disabled, unless enabled by PMUSERENR_EL0.EN. When PMUSERENR_EL0.UEN == 1, permitted EL0 writes are not affected by this mechanism.                              |
| 0b1  | When PMUSERENR_EL0.UEN == 0, EL0 writes to the Software increment register are enabled, unless trapped by another control. When PMUSERENR_EL0.UEN == 1, permitted EL0 writes to the Software increment register ignore the value of PMUACR_EL1. |

In AArch64 state, the register accesses affected by this control are:

- MSR writes to PMSWINC\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MCR writes to PMSWINC.

When disabled, writes generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MSR writes are reported using EC syndrome value 0x18 .
- AArch32 MCR writes are reported using EC syndrome value 0x03 .

This field is ignored by the PE when PMUSERENR\_EL0.{UEN,EN} == {0,1}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Software increment register Write enable.

When PMUSERENR\_EL0.EN is 0, PMUSERENR\_EL0.SW enables EL0 writes to the Software increment register.

| SW   | Meaning                                                                                         |
|------|-------------------------------------------------------------------------------------------------|
| 0b0  | EL0 writes to the Software increment register are disabled, unless enabled by PMUSERENR_EL0.EN. |
| 0b1  | EL0 writes to the Software increment register are enabled, unless trapped by another control.   |

In AArch64 state, the register accesses affected by this control are:

- MSR writes to PMSWINC\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MCR writes to PMSWINC.

When disabled, writes generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MSR writes are reported using EC syndrome value 0x18 .
- AArch32 MCR writes are reported using EC syndrome value 0x03 .

This field is ignored by the PE when PMUSERENR\_EL0.EN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EN, bit [0]

Enable.

Enables EL0 read/write access to PMU registers, other than the instruction counter.

| EN   | Meaning                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 accesses to the specified PMUSystem registers are trapped, unless enabled by PMUSERENR_EL0.{UEN,ER,CR,SW}. |
| 0b1  | EL0 accesses to the specified PMUSystem registers are enabled, unless trapped by another control.              |

In AArch64 state, the register accesses affected by this control are:

- MRS or MSR accesses to PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMCR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMOVSCLR\_EL0, PMOVSSET\_EL0, PMSELR\_EL0, PMXEVCNTR\_EL0, and PMXEVTYPER\_EL0.
- MRS reads of PMCEID0\_EL0 and PMCEID1\_EL0.

- MSR writes to the following registers:
- PMSWINC\_EL0.
- If FEAT\_PMUv3p9 is implemented, PMZR\_EL0.

Note

When FEAT\_PMUv3\_ICNTR is implemented, this field does not affect MRS and MSR accesses to PMICNTR\_EL0 and PMICFILTR\_EL0.

In AArch32 state, the register accesses affected by this control are:

- MRC or MCR accesses to PMCCFILTR, PMCCNTR, PMCNTENCLR, PMCNTENSET, PMCR, PMEVCNTR&lt;n&gt;, PMEVTYPER&lt;n&gt;, PMOVSR, PMOVSSET, PMSELR, PMXEVCNTR, and PMXEVTYPER.
- MRC reads of the following registers:
- PMCEID0 and PMCEID1.
- If FEAT\_PMUv3p1 is implemented, PMCEID2 and PMCEID3.
- MCR writes to PMSWINC.
- MRRC or MCRR accesses to PMCCNTR.

When trapped, reads and writes generate an exception to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, and:

- AArch64 MRS and MSR accesses are reported using EC syndrome value 0x18 .
- AArch32 MRC and MCR accesses are reported using EC syndrome value 0x03 .
- AArch32 MRRC and MCRR accesses are reported using EC syndrome value 0x04 .

This field is ignored by the PE when FEAT\_PMUv3p9 is implemented and PMUSERENR\_EL0.UEN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMUSERENR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMUSERENR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMUSERENR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMUSERENR_EL0; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMUSERENR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMUSERENR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMUSERENR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = PMUSERENR_EL0;
```

MSR PMUSERENR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1110 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMUSERENR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMUSERENR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
PMUSERENR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then PMUSERENR_EL0 = X[t, 64];
```

## D24.5.27 PMXEVCNTR\_EL0, Performance Monitors Selected Event Count Register

The PMXEVCNTR\_EL0 characteristics are:

## Purpose

Reads or writes the value of the selected event counter, PMEVCNTR&lt;n&gt;\_EL0. PMSELR\_EL0.SEL determines which event counter is selected.

## Configuration

AArch64 System register PMXEVCNTR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMXEVCNTR[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMXEVCNTR\_EL0 are UNDEFINED.

## Attributes

PMXEVCNTR\_EL0 is a 64-bit register.

## Field descriptions

When FEAT\_PMUv3p5 is implemented:

<!-- image -->

## PMEVCNTR&lt;n&gt;, bits [63:0]

Value of the selected event counter, PMEVCNTR&lt;n&gt;\_EL0, where n is the value stored in PMSELR\_EL0.SEL. The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## PMEVCNTR&lt;n&gt;, bits [31:0]

Value of the selected event counter, PMEVCNTR&lt;n&gt;\_EL0, where n is the value stored in PMSELR\_EL0.SEL.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMXEVCNTR\_EL0

If FEAT\_FGT is implemented and PMSELR\_EL0.SEL is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMXEVCNTR\_EL0 is as follows:

- If PMSELR\_EL0.SEL is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented and PMSELR\_EL0.SEL is greater than or equal to the number of accessible event counters, then reads and writes of PMXEVCNTR\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP
- Accesses to the register behave as if PMSELR\_EL0.SEL has an UNKNOWN value less than the number of counters accessible at the current Exception level and Security state.
- If EL2 is implemented and enabled in the current Security state, and PMSELR\_EL0.SEL is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMXEVCNTR\_EL0 are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.P&lt;UInt(PMSELR\_EL0.SEL)&gt; == 0.

Permitted writes of PMXEVCNTR\_EL0 are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.{UEN,ER} == {1,1}.

## Note

In EL0, an access is permitted if it is enabled by PMUSERENR\_EL0.{UEN,ER,EN}.

If EL2 is implemented and enabled in the current Security state, in EL1 and EL0, MDCR\_EL2.HPMN identifies the number of accessible event counters.

Otherwise, the number of accessible event counters is determined by the Effective value of PMCCR.EPMN. For more information, see MDCR\_EL2.HPMN and PMCCR.EPMN.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, PMXEVCNTR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif UInt(PMSELR_EL0.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED;
```

```
then
```

```
elsif (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00') then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && ↪ → PMUACR_EL1[UInt(PMSELR_EL0.SEL)] == '0' then X[t, 64] = Zeros(64); else X[t, 64] = PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)];
```

MSR PMXEVCNTR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif UInt(PMSELR_EL0.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && ↪ → (PMUACR_EL1[UInt(PMSELR_EL0.SEL)] == '0' || PMUSERENR_EL0.ER == '1') then return; else PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then PMEVCNTR_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64];
```

## D24.5.28 PMXEVTYPER\_EL0, Performance Monitors Selected Event Type Register

The PMXEVTYPER\_EL0 characteristics are:

## Purpose

When PMSELR\_EL0.SEL selects an event counter, this accesses a PMEVTYPER&lt;n&gt;\_EL0 register. When PMSELR\_EL0.SEL selects the cycle counter, this accesses PMCCFILTR\_EL0.

## Configuration

AArch64 System register PMXEVTYPER\_EL0 bits [31:0] are architecturally mapped to AArch32 System register PMXEVTYPER[31:0].

This register is present only when FEAT\_PMUv3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMXEVTYPER\_EL0 are UNDEFINED.

## Attributes

PMXEVTYPER\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                                   | 32   |
|--------------------------------------|------|
| Event type register or PMCCFILTR_EL0 |      |
| 31                                   | 0    |
| Event type register or PMCCFILTR_EL0 |      |

## EVTYPERn, bits [63:0]

When PMSELR\_EL0.SEL == 31, this register accesses PMCCFILTR\_EL0.

Otherwise, this register accesses PMEVTYPER&lt;n&gt;\_EL0 where n is the value in PMSELR\_EL0.SEL.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMXEVTYPER\_EL0

If FEAT\_FGT is implemented, and PMSELR\_EL0.SEL is not 31 and is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMXEVTYPER\_EL0 is as follows:

- If PMSELR\_EL0.SEL is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented, and PMSELR\_EL0.SEL is not 31 and is greater than or equal to the number of accessible event counters, then reads and writes of PMXEVTYPER\_EL0 are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP .
- Accesses to the register behave as if PMSELR\_EL0.SEL has an UNKNOWN value less than the number of event counters accessible at the current Exception level and Security state.
- Accesses to the register behave as if PMSELR\_EL0.SEL is 31.
- If EL2 is implemented and enabled in the current Security state, PMSELR\_EL0 is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMXEVTYPER\_EL0 are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.UEN == 1.
- Any of the following are true:
- PMSELR\_EL0.SEL != 31 and PMUACR\_EL1.P&lt;UInt(PMSELR\_EL0.SEL)&gt; == 0.
- PMSELR\_EL0.SEL == 31 and PMUACR\_EL1.C == 0.

Permitted writes of PMXEVTYPER\_EL0 are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- PMUSERENR\_EL0.UEN == 1.
- Any of the following are true:
- PMSELR\_EL0.SEL != 31 and PMUSERENR\_EL0.ER == 1.
- PMSELR\_EL0.SEL == 31 and PMUSERENR\_EL0.CR == 1.

Note

In EL0, an access is permitted if it is enabled by PMUSERENR\_EL0.{UEN,EN}.

If EL2 is implemented and enabled in the current Security state, in EL1 and EL0, MDCR\_EL2.HPMN identifies the number of accessible event counters.

Otherwise, the number of accessible event counters is determined by the Effective value of PMCCR.EPMN. For more information, see MDCR\_EL2.HPMN and PMCCR.EPMN.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, PMXEVTYPER\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif UInt(PMSELR_EL0.SEL) != 31 && UInt(PMSELR_EL0.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGRTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) != 31 && UInt(PMSELR_EL0.SEL) >= ↪ → GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER);
```

```
else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && ((UInt(PMSELR_EL0.SEL) != 31 ↪ → && PMUACR_EL1[UInt(PMSELR_EL0.SEL)] == '0') || (UInt(PMSELR_EL0.SEL) == 31 && PMUACR_EL1.C == ↪ → '0')) then X[t, 64] = Zeros(64); elsif UInt(PMSELR_EL0.SEL) == 31 then X[t, 64] = PMCCFILTR_EL0; else X[t, 64] = PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) != 31 && UInt(PMSELR_EL0.SEL) >= ↪ → GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif UInt(PMSELR_EL0.SEL) == 31 then X[t, 64] = PMCCFILTR_EL0; else X[t, 64] = PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif UInt(PMSELR_EL0.SEL) == 31 then X[t, 64] = PMCCFILTR_EL0; else X[t, 64] = PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)]; elsif PSTATE.EL == EL3 then if UInt(PMSELR_EL0.SEL) == 31 then X[t, 64] = PMCCFILTR_EL0; else X[t, 64] = PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)];
```

MSR PMXEVTYPER\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PMUv3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif UInt(PMSELR_EL0.SEL) != 31 && UInt(PMSELR_EL0.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HDFGWTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) != 31 && UInt(PMSELR_EL0.SEL) >= ↪ → GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1' && ((UInt(PMSELR_EL0.SEL) != 31 ↪ → && (PMUACR_EL1[UInt(PMSELR_EL0.SEL)] == '0' || PMUSERENR_EL0.ER == '1')) || ↪ → (UInt(PMSELR_EL0.SEL) == 31 && (PMUACR_EL1.C == '0' || PMUSERENR_EL0.CR == '1'))) then return; elsif UInt(PMSELR_EL0.SEL) == 31 then PMCCFILTR_EL0 = X[t, 64]; else PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && UInt(PMSELR_EL0.SEL) != 31 && UInt(PMSELR_EL0.SEL) >= ↪ → GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); else AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif UInt(PMSELR_EL0.SEL) == 31 then PMCCFILTR_EL0 = X[t, 64]; else PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif UInt(PMSELR_EL0.SEL) == 31 then PMCCFILTR_EL0 = X[t, 64]; else PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then if UInt(PMSELR_EL0.SEL) == 31 then PMCCFILTR_EL0 = X[t, 64]; else PMEVTYPER_EL0[UInt(PMSELR_EL0.SEL)] = X[t, 64];
```

## D24.5.29 PMZR\_EL0, Performance Monitors Zero with Mask

The PMZR\_EL0 characteristics are:

## Purpose

Zero the set of counters specified by the mask written to PMZR\_EL0.

## Configuration

When FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p9 is implemented, AArch64 System register PMZR\_EL0 bits [63:0] are architecturally mapped to External register PMZR\_EL0[63:0].

This register is present only when FEAT\_PMUv3p9 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PMZR\_EL0 are UNDEFINED.

## Attributes

PMZR\_EL0 is a 64-bit register.

## Field descriptions

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Zero PMICNTR\_EL0.

| F0   | Meaning                  |
|------|--------------------------|
| 0b0  | Write is ignored.        |
| 0b1  | Set PMICNTR_EL0 to zero. |

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- PSTATE.EL != EL3
- MDCR\_EL3.EnPM2 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- PSTATE.EL == EL0
- Any of the following are true:
- PMUSERENR\_EL0.UEN == '0'
- PMUACR\_EL1.F0 == '0'
- Access to this field is RAZ/WI if all of the following are true:

- FEAT\_FGT2 is implemented
- EL2Enabled()
- PSTATE.EL IN {EL1, EL0}
- [HCR\_EL2.E2H, HCR\_EL2.TGE] != '11'
- Any of the following are true:
- All of the following are true:
- EL3 is implemented
- SCR\_EL3.FGTEn2 == '0'
- HDFGWTR2\_EL2.nPMICNTR\_EL0 == '0'
- Access to this field is RAZ/WI if all of the following are true:
- PSTATE.EL == EL0
- PMUSERENR\_EL0.IR == '1'
- Otherwise, access to this field is WO/RAZ.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Zero PMCCNTR\_EL0.

| C   | Meaning                  |
|-----|--------------------------|
| 0b0 | Write is ignored.        |
| 0b1 | Set PMCCNTR_EL0 to zero. |

## Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is WO/RAZ.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Zero PMEVCNTR&lt;m&gt;\_EL0.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented

| P<m>   | Meaning                      |
|--------|------------------------------|
| 0b0    | Write is ignored.            |
| 0b1    | Set PMEVCNTR<m>_EL0 to zero. |

- PSTATE.EL == EL0
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is WO/RAZ.

## Accessing PMZR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MSR PMZR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1001 | 0b1101 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif PMUSERENR_EL0.EN == '0' && (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0') ↪ → then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nPMZR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ZeroPMUCounters(X[t, 64]); elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nPMZR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.TPM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ZeroPMUCounters(X[t, 64]); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TPM == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else ZeroPMUCounters(X[t, 64]); elsif PSTATE.EL == EL3 then ZeroPMUCounters(X[t, 64]);
```

## D24.5.30 SPMACCESSR\_EL1, System Performance Monitors Access Register (EL1)

The SPMACCESSR\_EL1 characteristics are:

## Purpose

Controls access to System PMUs from EL0.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMACCESSR\_EL1 are UNDEFINED.

## Attributes

SPMACCESSR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63 62   | 61 60   | 59 58   | 57 56   | 55 54   | 53 52   | 51 50   | 49 48   | 47 46   | 45 44   | 43 42   | 41 40   | 39 38   | 37 36   | 35 34   | 33 32   |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| P31     | P30     | P29     | P28     | P27     | P26     | P25     | P24     | P23     | P22     | P21     | P20     | P19     | P18     | P17     | P16     |

<!-- image -->

## P&lt;m&gt; , bits [2m+1:2m], for m = 31 to 0

System PMU &lt;m&gt; access. Controls access to System PMU &lt;m&gt;.

| P<m>   | Meaning                                                                                                                                                |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | MRS read and MSR write System register accesses to System PMU<m>atEL0are trapped to EL1, unless the instruction generates a higher priority exception. |
| 0b01   | MSR write System register accesses to System PMU<m>at EL0 are trapped to EL1, unless the instruction generates a higher priority exception.            |
| 0b11   | This control does not cause any instructions to be trapped.                                                                                            |

All other values are reserved.

The registers trapped by this control are:

AArch64: SPMCNTENCLR\_EL0, SPMCNTENSET\_EL0, SPMCR\_EL0, SPMEVCNTR&lt;n&gt;\_EL0, SPMEVFILT2R&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, SPMEVTYPER&lt;n&gt;\_EL0, SPMOVSCLR\_EL0, and SPMOVSSET\_EL0.

This field is ignored by the PE when all of the following are true:

- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCR\_EL2.{E2H,TGE} is {1,1}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt; UInt(ID\_AA64DFR1\_EL1.SYSPMUID), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing SPMACCESSR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name SPMACCESSR\_EL1 or SPMACCESSR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMACCESSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMACCESSR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8E8]; else X[t, 64] = SPMACCESSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = SPMACCESSR_EL2; else X[t, 64] = SPMACCESSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SPMACCESSR_EL1;
```

MSR SPMACCESSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMACCESSR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8E8] = X[t, 64]; else SPMACCESSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then SPMACCESSR_EL2 = X[t, 64]; else SPMACCESSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SPMACCESSR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SPMACCESSR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b101 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x8E8]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMACCESSR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = SPMACCESSR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR SPMACCESSR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b101 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x8E8] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMACCESSR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then SPMACCESSR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.5.31 SPMACCESSR\_EL2, System Performance Monitors Access Register (EL2)

The SPMACCESSR\_EL2 characteristics are:

## Purpose

Controls access to System PMUs from EL1 and EL0.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMACCESSR\_EL2 are UNDEFINED.

## Attributes

SPMACCESSR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 62   | 61    | 60 59   | 58   | 57    | 56 55   | 54 53 52   | 51 50   | 49    | 48   | 47 46   | 45 44   | 43 42   | 41   | 40   | 39   | 38   | 37 36 35   | 34 33   | 32   |
|------|------|-------|---------|------|-------|---------|------------|---------|-------|------|---------|---------|---------|------|------|------|------|------------|---------|------|
| P31  | P30  | P30   | P29     | P28  |       | P27     | P26        | P25     | P24   |      | P23     | P22     | P21     | P20  |      | P19  | P18  | P17        | P16     |      |
| 31   | 30   | 29 28 | 27      | 26   | 25 24 | 23 22   | 21         | 20 19   | 18 17 | 16   | 15 14   | 13 12   | 11      | 10   | 9 8  | 7    | 6 5  | 4 3        | 2 1     | 0    |
| P15  | P14  | P14   |         | P13  | P12   | P11     | P10        | P9      | P8    |      | P7      | P6      | P5      | P4   |      | P3   | P2   | P1         | P0      |      |

## P&lt;m&gt; , bits [2m+1:2m], for m = 31 to 0

System PMU &lt;m&gt; access. Controls access to System PMU &lt;m&gt;.

| P<m>   | Meaning                                                                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | MRS read and MSR write System register accesses to System PMU<m>at EL1 and EL0 are trapped to EL2, unless the instruction generates a higher priority exception. |
| 0b01   | MSR write System register accesses to System PMU<m>at EL1 and EL0 are trapped to EL2, unless the instruction generates a higher priority exception.              |
| 0b11   | This control does not cause any instructions to be trapped.                                                                                                      |

All other values are reserved.

The registers trapped by this control are:

AArch64: SPMCFGR\_EL1, SPMCGCR&lt;n&gt;\_EL1, SPMCNTENCLR\_EL0, SPMCNTENSET\_EL0, SPMCR\_EL0, SPMDEVAFF\_EL1, SPMDEVARCH\_EL1, SPMEVCNTR&lt;n&gt;\_EL0, SPMEVFILT2R&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, SPMEVTYPER&lt;n&gt;\_EL0, SPMIIDR\_EL1, SPMINTENCLR\_EL1, SPMINTENSET\_EL1, SPMOVSCLR\_EL0, SPMOVSSET\_EL0, and SPMSCR\_EL1.

This field is ignored by the PE when EL2 is not implemented or disabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt; UInt(ID\_AA64DFR1\_EL1.SYSPMUID), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing SPMACCESSR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name SPMACCESSR\_EL2 or SPMACCESSR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMACCESSR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b100 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMACCESSR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = SPMACCESSR_EL2;
```

MSR SPMACCESSR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b100 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
then
```

else

```
AArch64.SystemAccessTrap(EL3, 0x18); else SPMACCESSR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then SPMACCESSR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, SPMACCESSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMACCESSR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8E8]; else X[t, 64] = SPMACCESSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = SPMACCESSR_EL2; else X[t, 64] = SPMACCESSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SPMACCESSR_EL1;
```

MSR SPMACCESSR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMACCESSR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8E8] = X[t, 64]; else SPMACCESSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then SPMACCESSR_EL2 = X[t, 64]; else SPMACCESSR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SPMACCESSR_EL1 = X[t, 64];
```

## D24.5.32 SPMACCESSR\_EL3, System Performance Monitors Access Register (EL3)

The SPMACCESSR\_EL3 characteristics are:

## Purpose

Controls access to System PMUs from EL2, EL1 and EL0.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMACCESSR\_EL3 are UNDEFINED.

## Attributes

SPMACCESSR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## P&lt;m&gt; , bits [2m+1:2m], for m = 31 to 0

System PMU &lt;m&gt; access. Controls access to System PMU &lt;m&gt;.

| P<m>   | Meaning                                                                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | MRS read and MSR write System register accesses to System PMU<m>at EL2, EL1, and EL0 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b01   | MSR write System register accesses to System PMU<m>at EL2, EL1, and EL0 are trapped to EL3, unless the instruction generates a higher priority exception.              |
| 0b11   | This control does not cause any instructions to be trapped.                                                                                                            |

All other values are reserved.

The registers trapped by this control are:

AArch64: SPMCFGR\_EL1, SPMCGCR&lt;n&gt;\_EL1, SPMCNTENCLR\_EL0, SPMCNTENSET\_EL0, SPMCR\_EL0, SPMDEVAFF\_EL1, SPMDEVARCH\_EL1, SPMEVCNTR&lt;n&gt;\_EL0, SPMEVFILT2R&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, SPMEVTYPER&lt;n&gt;\_EL0, SPMIIDR\_EL1, SPMINTENCLR\_EL1, SPMINTENSET\_EL1, SPMOVSCLR\_EL0, SPMOVSSET\_EL0, and SPMSCR\_EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt; UInt(ID\_AA64DFR1\_EL1.SYSPMUID), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing SPMACCESSR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMACCESSR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b110 | 0b1001 | 0b1101 | 0b011 |

if !(IsFeatureImplemented(FEAT\_SPMU) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

X[t, 64] = SPMACCESSR\_EL3;

MSR SPMACCESSR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b110 | 0b1001 | 0b1101 | 0b011 |

if !(IsFeatureImplemented(FEAT\_SPMU) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

SPMACCESSR\_EL3 = X[t, 64];

## D24.5.33 SPMCFGR\_EL1, System Performance Monitors Configuration Register

The SPMCFGR\_EL1 characteristics are:

## Purpose

Describes the capabilities of System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMCFGR\_EL1 are UNDEFINED.

## Attributes

SPMCFGR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NCG, bits [31:28]

Counter Groups.

Defines the number of counter groups implemented by System PMU &lt;s&gt;, minus one.

If this field is zero, then one counter group is implemented and SPMCGCR&lt;n&gt;\_EL1 read-as-zero.

Otherwise, for each counter group &lt;m&gt;, SPMCGCR&lt;m DIV 8&gt;\_EL1.N&lt;m MOD 8&gt; defines the number of counters in the group.

Locating the first counter in each group depends on the number of implemented groups. Each counter group starts with counter:

- SPMEVTYPER&lt;m × 32&gt;\_EL0, meaning there are at most 32 counters per group, if there are 2 counter groups.
- SPMEVTYPER&lt;m × 16&gt;\_EL0, meaning there are at most 16 counters per group, if there are 3 or 4 counter groups.
- SPMEVTYPER&lt;m × 8&gt;\_EL0, meaning there are at most 8 counters per group, if there are between 5 and 8 counter groups.
- SPMEVTYPER&lt;m × 4&gt;\_EL0, meaning there are at most 4 counters per group, if there are more than 8 counter groups.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bits [27:25]

Reserved, RES0.

## HDBG, bit [24]

Halt-on-debug supported. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## TRO, bit [23]

Trace output supported. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SS, bit [22]

Snapshot supported. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## FZO, bit [21]

Freeze-on-overflow supported. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## MSI, bit [20]

Message-signaled interrupts supported. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bit [19]

Reserved, RAO.

## Bit [18]

Reserved, RES0.

## NA, bit [17]

No write access when running. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## EX, bit [16]

Export supported. For more information on this field, see 'CoreSight PMU Architecture'.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bits [15:14]

Reserved, RAZ.

SIZE, bits [13:8]

Counter size. The size of the largest counter implemented by System PMU &lt;s&gt;.

| SIZE     | Meaning          |
|----------|------------------|
| 0b000111 | 8-bit counters.  |
| 0b001001 | 10-bit counters. |
| 0b001011 | 12-bit counters. |
| 0b001111 | 16-bit counters. |
| 0b010011 | 20-bit counters. |
| 0b010111 | 24-bit counters. |
| 0b011111 | 32-bit counters. |
| 0b100011 | 36-bit counters. |
| 0b100111 | 40-bit counters. |
| 0b101011 | 44-bit counters. |
| 0b101111 | 48-bit counters. |
| 0b110011 | 52-bit counters. |
| 0b110111 | 56-bit counters. |
| 0b111111 | 64-bit counters. |

All other values are reserved.

Not all counters must be this size. For example, a System PMU might include a mix of 32-bit and 64-bit counters.

## N, bits [7:0]

Number of event counters implemented by System PMU &lt;s&gt;, minus 1.

| N            | Meaning                                                         |
|--------------|-----------------------------------------------------------------|
| 0x00 .. 0x3F | Number of event counters implemented by System PMU<s>, minus 1. |

All other values are reserved.

## Accessing SPMCFGR\_EL1

To access SPMCFGR\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMCFGR\_EL1 reads-as-zero if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMCFGR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMID == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCFGR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCFGR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMCFGR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

## D24.5.34 SPMCGCR&lt;n&gt;\_EL1, System PMU Counter Group Configuration Registers, n = 0 - 1

The SPMCGCR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Describes the configuration of counter groups in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMCGCR&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

SPMCGCR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 56 55   | 40 39   | 32   |
|------|---------|---------|------|
| N7   | N6      | N4      |      |
| 31   | 24 23   | 8 7     | 0    |
| N3   | N2      | N0      |      |

## N&lt;m&gt;, bits [8m+7:8m], for m = 7 to 0

Number of counters in counter group 8n+m.

The maximum size of each counter group depends on the number of implemented groups and the largest implemented counter size. For more information, see SPMCFGR\_EL1.NCG.

## Accessing SPMCGCR&lt;n&gt;\_EL1

To access SPMCGCR&lt;n&gt;\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMCGCR&lt;n&gt;\_EL1 reads-as-zero if any of the following are true:

- System PMU &lt;s&gt; implements one counter group (SPMCFGR\_EL1.NCG is zero).
- System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SPMCGCR<m>_EL1 ; Where m = 0-1
```

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b00 :m[0] |

```
integer m = UInt(op2<0>); if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMID == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCGCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL), m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCGCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL), m]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMCGCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL), m];
```

## D24.5.35 SPMCNTENCLR\_EL0, System Performance Monitors Count Enable Clear Register

The SPMCNTENCLR\_EL0 characteristics are:

## Purpose

Disable event counters in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMCNTENCLR\_EL0 are UNDEFINED.

## Attributes

SPMCNTENCLR\_EL0 is a 64-bit register.

## Field descriptions

| 63   | 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32   |
|------|------------------------------------------------------------------------------------------------|

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Event counter &lt;m&gt; disable.

| P<m>   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Event counter <m> in System PMU<s> is disabled. |
| 0b1    | Event counter <m> in System PMU<s> is enabled.  |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing SPMCNTENCLR\_EL0

To access SPMCNTENCLR\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMCNTENCLR\_EL0 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMCNTENCLR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMCNTENCLR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMCNTENCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.36 SPMCNTENSET\_EL0, System Performance Monitors Count Enable Set Register

The SPMCNTENSET\_EL0 characteristics are:

## Purpose

Enables event counters in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMCNTENSET\_EL0 are UNDEFINED.

## Attributes

SPMCNTENSET\_EL0 is a 64-bit register.

## Field descriptions

60

59

58

57

56

55

P60

63

P63

62

P62

61

P61

P59

P58

P57

P56

P55

54

P54

53

P53

52

P52

51

P51

50

P50

49

P49

48

P48

47

P47

46

P46

45

P45

44

P44

43

P43

42

P42

41

P41

40

P40

39

P39

38

P38

37

P37

36

P36

35

P35

34

P34

33

P33

32

P32

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Event counter &lt;m&gt; enable.

| P<m>   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Event counter <m> in System PMU<s> is disabled. |
| 0b1    | Event counter <m> in System PMU<s> is enabled.  |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;, access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing SPMCNTENSET\_EL0

To access SPMCNTENSET\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMCNTENSET\_EL0 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMCNTENSET\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMCNTENSET\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMCNTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMCNTENSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.37 SPMCR\_EL0, System Performance Monitor Control Register

The SPMCR\_EL0 characteristics are:

## Purpose

Main control register for System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMCR\_EL0 are UNDEFINED.

## Attributes

SPMCR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## TRO, bit [11]

## When SPMCFGR\_EL1.TRO == '1':

Trace enable. For more information on this field, see 'CoreSight PMU Architecture'.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When PSTATE.EL == EL0, access to this field is RO.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## HDBG, bit [10]

## When SPMCFGR\_EL1.HDBG == '1':

Halt-on-debug. For more information on this field, see 'CoreSight PMU Architecture'.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When PSTATE.EL == EL0, access to this field is RO.

- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## FZO, bit [9]

## When SPMCFGR\_EL1.FZO == '1':

Freeze-on-overflow. For more information on this field, see 'CoreSight PMU Architecture'.

Note

If implemented by a System PMU, then freeze-on-overflow affects only the counters of System PMU &lt;s&gt;, not other System PMUs nor the PE PMU.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NA, bit [8]

## When SPMCFGR\_EL1.NA == '1':

Not accessible. For more information on this field, see 'CoreSight PMU Architecture'.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Bits [7:5]

Reserved, RES0.

## EX, bit [4]

## When SPMCFGR\_EL1.EX == '1':

Export enable. For more information on this field, see 'CoreSight PMU Architecture'.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [3:2]

Reserved, RES0.

## P, bit [1]

Event counter reset.

Note

Resetting the event counters does not affect any overflow flags.

Access to this field is WO/RAZ.

## E, bit [0]

Count enable. This field controls System PMU &lt;s&gt;.

| P   | Meaning                                            |
|-----|----------------------------------------------------|
| 0b0 | Write is ignored.                                  |
| 0b1 | Reset all event counters in System PMU<s> to zero. |

| E   | Meaning              |
|-----|----------------------|
| 0b0 | Monitor is disabled. |
| 0b1 | Monitor is enabled.  |

Performance monitor overflow IRQs are only signaled by System PMU &lt;s&gt; when this field is 1.

The reset behavior of this field is:

- On a System PMU reset, this field resets to '0' .

## Accessing SPMCR\_EL0

To access SPMCR\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMCR\_EL0 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMCR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMCR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMCR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then
```

MSR SPMCR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMCR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMCR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMCR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.38 SPMDEVAFF\_EL1, System Performance Monitors Device Affinity Register

The SPMDEVAFF\_EL1 characteristics are:

## Purpose

For additional information, see the CoreSight Architecture Specification.

For a System PMU that has affinity with a single PE or a group of PEs, SPMDEV AFF\_EL1 is a copy of MPIDR\_EL1 or part of MPIDR\_EL1:

- If the System PMU has affinity with a single PE, then the affinity level is 0 and SPMDEV AFF\_EL1 reads the same value as MPIDR\_EL1, and SPMDEVAFF\_EL1.F0V reads-as-one to indicate affinity level 0.
- If the System PMU has affinity with a group of PEs, then the affinity level is 1, 2, or 3, parts of SPMDEVAFF\_EL1 reads the same value as parts of MPIDR\_EL1, and the rest of SPMDEVAFF\_EL1 indicates the level.

For example, if the group of PEs is a subset of the PEs at affinity level 1, then all of the following are true:

- All the PEs in the group have the same values in MPIDR\_EL1.{Aff3,Aff2}, and these values are equal to SPMDEVAFF\_EL1.{Aff3,Aff2}.
- SPMDEVAFF\_EL1.Aff1 is nonzero and not 0x80 , and SPMDEVAFF\_EL1.{Aff0,F0V} read-as-zero, to indicate at least affinity level 1. The subset of PEs at level 1 that the System PMU has affinity with is indicated by the least-significant set bit in SPMDEV AFF\_EL1.Aff1. In this example, if SPMDEVAFF\_EL1.Aff1[2:0] is 0b100 , then the System PMU has affinity with the up-to 8 PEs that have MPIDR\_EL1.Aff1[7:3] == SPMDEVAFF\_EL1.Aff1[7:3].

Depending on the IMPLEMENTATION DEFINED nature of the system, it might be possible that SPMDEV AFF\_EL1 is read before system firmware has configured the System PMU and/or the PE or group of PEs that the System PMU has affinity with. When this is the case, SPMDEV AFF\_EL1 reads-as-zero.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMDEVAFF\_EL1 are UNDEFINED.

## Attributes

SPMDEVAFF\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63    |      |          |      |       | 40 39   |      | 32   |
|-------|------|----------|------|-------|---------|------|------|
|       |      |          | RES0 |       |         | Aff3 |      |
| 31 30 | 29   | 25 24 23 |      | 16 15 | 8       | 7    | 0    |
| F0V U | RES0 | MT       | Aff2 |       |         | Aff0 |      |

## Bits [63:40]

Reserved, RES0.

## Aff3, bits [39:32]

PE affinity level 3. The MPIDR\_EL1.Aff3 field, viewed from the highest Exception level of the associated PE or PEs.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## F0V, bit [31]

Indicates that the SPMDEVAFF\_EL1.Aff0 field is valid.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F0V   | Meaning                                                                                       |
|-------|-----------------------------------------------------------------------------------------------|
| 0b0   | SPMDEVAFF_EL1.Aff0 is not valid, and the PE affinity is above level 0 or a subset of level 0. |
| 0b1   | SPMDEVAFF_EL1.Aff0 is valid, and the PE affinity is at level 0.                               |

Access to this field is RO.

## U, bit [30]

## When SPMDEVAFF\_EL1.F0V == '1':

Uniprocessor. The MPIDR\_EL1.U field, viewed from the highest Exception level of the associated PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, UNKNOWN.

## Bits [29:25]

Reserved, RES0.

## MT, bit [24]

## When SPMDEVAFF\_EL1.F0V == '1':

Multithreaded. The MPIDR\_EL1.MT field, viewed from the highest Exception level of the associated PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, UNKNOWN.

## Aff2, bits [23:16]

## When affine with a PE or PEs at affinity level 2 or below:

PE affinity level 2. The MPIDR\_EL1.Aff2 field, viewed from the highest Exception level of the associated PE or PEs.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## When affine with a sub-set of PEs at affinity level 2:

PE affinity level 2. Defines part of the MPIDR\_EL1.Aff2 field, viewed from the highest Exception level of the associated PEs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Aff2       | Meaning                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0bxxxxxxx1 | SPMDEVAFF_EL1.Aff2[7:1] is the value of MPIDR_EL1.Aff2[7:1], viewed from the highest Exception level of the associated PEs. |
| 0bxxxxxx10 | SPMDEVAFF_EL1.Aff2[7:2] is the value of MPIDR_EL1.Aff2[7:2], viewed from the highest Exception level of the associated PEs. |
| 0bxxxxx100 | SPMDEVAFF_EL1.Aff2[7:3] is the value of MPIDR_EL1.Aff2[7:3], viewed from the highest Exception level of the associated PEs. |
| 0bxxxx1000 | SPMDEVAFF_EL1.Aff2[7:4] is the value of MPIDR_EL1.Aff2[7:4], viewed from the highest Exception level of the associated PEs. |
| 0bxxx10000 | SPMDEVAFF_EL1.Aff2[7:5] is the value of MPIDR_EL1.Aff2[7:5], viewed from the highest Exception level of the associated PEs. |
| 0bxx100000 | SPMDEVAFF_EL1.Aff2[7:6] is the value of MPIDR_EL1.Aff2[7:6], viewed from the highest Exception level of the associated PEs. |
| 0bx1000000 | SPMDEVAFF_EL1.Aff2[7] is the value of MPIDR_EL1.Aff2[7], viewed from the highest Exception level of the associated PEs.     |

Access to this field is RO.

## Otherwise:

PE affinity level NOT DEFINED. Indicates whether the PE affinity is at level 3.

| Aff2   | Meaning                    |
|--------|----------------------------|
| 0x80   | PE affinity is at level 3. |

All other values are reserved.

Access to this field is RO.

## Aff1, bits [15:8]

## When affine with a PE or PEs at affinity level 1 or below:

PE affinity level 1. The MPIDR\_EL1.Aff1 field, viewed from the highest Exception level of the associated PE or PEs.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## When affine with a sub-set of PEs at affinity level 1:

PE affinity level 1. Defines part of the MPIDR\_EL1.Aff1 field, viewed from the highest Exception level of the associated PEs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Aff1       | Meaning                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0bxxxxxxx1 | SPMDEVAFF_EL1.Aff1[7:1] is the value of MPIDR_EL1.Aff1[7:1], viewed from the highest Exception level of the associated PEs. |

| Aff1       | Meaning                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0bxxxxxx10 | SPMDEVAFF_EL1.Aff1[7:2] is the value of MPIDR_EL1.Aff1[7:2], viewed from the highest Exception level of the associated PEs. |
| 0bxxxxx100 | SPMDEVAFF_EL1.Aff1[7:3] is the value of MPIDR_EL1.Aff1[7:3], viewed from the highest Exception level of the associated PEs. |
| 0bxxxx1000 | SPMDEVAFF_EL1.Aff1[7:4] is the value of MPIDR_EL1.Aff1[7:4], viewed from the highest Exception level of the associated PEs. |
| 0bxxx10000 | SPMDEVAFF_EL1.Aff1[7:5] is the value of MPIDR_EL1.Aff1[7:5], viewed from the highest Exception level of the associated PEs. |
| 0bxx100000 | SPMDEVAFF_EL1.Aff1[7:6] is the value of MPIDR_EL1.Aff1[7:6], viewed from the highest Exception level of the associated PEs. |
| 0bx1000000 | SPMDEVAFF_EL1.Aff1[7] is the value of MPIDR_EL1.Aff1[7], viewed from the highest Exception level of the associated PEs.     |

Access to this field is RO.

## Otherwise:

PE affinity level 1. Indicates whether the PE affinity is at level 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Aff1   | Meaning                                              |
|--------|------------------------------------------------------|
| 0x00   | PE affinity is above level 2 or a subset of level 2. |
| 0x80   | PE affinity is at level 2.                           |

Access to this field is RO.

## Aff0, bits [7:0]

## When affine with a PE at affinity level 0:

PE affinity level 0. The MPIDR\_EL1.Aff0 field, viewed from the highest Exception level of the associated PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## When affine with a sub-set of PEs at affinity level 0:

PE affinity level 0. Defines part of the MPIDR\_EL1.Aff0 field, viewed from the highest Exception level of the associated PEs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Aff0       | Meaning                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0bxxxxxxx1 | SPMDEVAFF_EL1.Aff0[7:1] is the value of MPIDR_EL1.Aff0[7:1], viewed from the highest Exception level of the associated PEs. |
| 0bxxxxxx10 | SPMDEVAFF_EL1.Aff0[7:2] is the value of MPIDR_EL1.Aff0[7:2], viewed from the highest Exception level of the associated PEs. |

| Aff0       | Meaning                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0bxxxxx100 | SPMDEVAFF_EL1.Aff0[7:3] is the value of MPIDR_EL1.Aff0[7:3], viewed from the highest Exception level of the associated PEs. |
| 0bxxxx1000 | SPMDEVAFF_EL1.Aff0[7:4] is the value of MPIDR_EL1.Aff0[7:4], viewed from the highest Exception level of the associated PEs. |
| 0bxxx10000 | SPMDEVAFF_EL1.Aff0[7:5] is the value of MPIDR_EL1.Aff0[7:5], viewed from the highest Exception level of the associated PEs. |
| 0bxx100000 | SPMDEVAFF_EL1.Aff0[7:6] is the value of MPIDR_EL1.Aff0[7:6], viewed from the highest Exception level of the associated PEs. |
| 0bx1000000 | SPMDEVAFF_EL1.Aff0[7] is the value of MPIDR_EL1.Aff0[7], viewed from the highest Exception level of the associated PEs.     |

Access to this field is RO.

## Otherwise:

PE affinity level 0. Indicates whether the PE affinity is at level 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Aff0   | Meaning                                              |
|--------|------------------------------------------------------|
| 0x00   | PE affinity is above level 1 or a subset of level 1. |
| 0x80   | PE affinity is at level 1.                           |

Access to this field is RO.

## Accessing SPMDEVAFF\_EL1

Reads of SPMDEVAFF\_EL1 are not affected by the value of VMPIDR\_EL2 at any Exception level.

If System PMU &lt;s&gt; has affinity only with this PE, then it is IMPLEMENTATION DEFINED whether SPMDEVAFF\_EL1 reads-as-zero or reads the same value as MPIDR\_EL1.

To access SPMDEVAFF\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMDEVAFF\_EL1 reads-as-zero if any of the following are true:

- System PMU &lt;s&gt; is not implemented.
- System PMU &lt;s&gt; has no affinity with the PE or cluster of PEs.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMDEVAFF\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMDEVAFF_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMDEVAFF_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMDEVAFF_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMDEVAFF_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

## D24.5.39 SPMDEVARCH\_EL1, System Performance Monitors Device Architecture Register

The SPMDEVARCH\_EL1 characteristics are:

## Purpose

Provides discovery information for System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMDEVARCH\_EL1 are UNDEFINED.

## Attributes

SPMDEVARCH\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ARCHITECT, bits [31:21]

Architect. Defines the architect of the component. Bits [31:28] are the JEP106 continuation code (JEP106 bank ID, minus 1) and bits [27:21] are the JEP106 ID code.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Defines that SPMDEVARCH\_EL1 register is present.

| PRESENT   | Meaning                                      |
|-----------|----------------------------------------------|
| 0b0       | Device Architecture information not present. |
| 0b1       | Device Architecture information present.     |

If SPMDEVARCH\_EL1 is not present, the register is RES0.

## REVISION, bits [19:16]

Revision. Defines the architecture revision of the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

PRESENT

## ARCHVER,bits [15:12]

Architecture Version. Defines the architecture version of the component.

This field has an IMPLEMENTATION DEFINED value.

SPMDEVARCH\_EL1.ARCHVER and SPMDEVARCH\_EL1.ARCHPART are also defined as a single field, SPMDEVARCH\_EL1.ARCHID, so that SPMDEVARCH\_EL1.ARCHVER is SPMDEVARCH\_EL1.ARCHID[15:12].

Access to this field is RO.

## ARCHPART, bits [11:0]

Architecture Part. Defines the architecture of the component.

This field has an IMPLEMENTATION DEFINED value.

SPMDEVARCH\_EL1.ARCHVER and SPMDEVARCH\_EL1.ARCHPART are also defined as a single field, SPMDEVARCH\_EL1.ARCHID, so that SPMDEVARCH\_EL1.ARCHPART is

SPMDEVARCH\_EL1.ARCHID[11:0].

Access to this field is RO.

## Accessing SPMDEVARCH\_EL1

To access SPMDEVARCH\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMDEVARCH\_EL1 reads-as-zero if any of the following are true:

- System PMU &lt;s&gt; is not implemented.
- System PMU &lt;s&gt; does not implement SPMDEVARCH\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMDEVARCH\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMID == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMDEVARCH_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMDEVARCH_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMDEVARCH_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

## D24.5.40 SPMEVCNTR&lt;n&gt;\_EL0, System Performance Monitors Event Count Register, n = 0 - 63

The SPMEVCNTR&lt;n&gt;\_EL0 characteristics are:

## Purpose

Event counter &lt;n&gt; in System PMU &lt;s&gt;, where n is 0 to 63.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMEVCNTR&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

SPMEVCNTR&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## CNTR, bits [63:0]

Event counter n.

The number of implemented bits for SPMEVCNTR&lt;n&gt;\_EL0 is IMPLEMENTATION DEFINED. Unimplemented bits are RES0.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPMEVCNTR&lt;n&gt;\_EL0

To access SPMEVCNTR&lt;n&gt;\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s and SPMSELR\_EL0.BANK to n[5:4].

SPMEVCNTR&lt;n&gt;\_EL0 reads-as-zero and ignores writes if any of the following are true:

- Event counter &lt;n&gt; is not implemented by System PMU &lt;s&gt;.
- System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMEVCNTR&lt;m&gt;\_EL0 ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b000 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMEVCNTRn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMEVCNTRn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then
```

```
X[t, 64] = Zeros(64); else X[t, 64] = SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m];
```

MSR SPMEVCNTR&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b000 :m[3] | m[2:0] |

integer m = UInt(CRm&lt;0&gt;:op2&lt;2:0&gt;);

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMEVCNTRn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMEVCNTRn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVCNTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else
```

## D24.5.41 SPMEVFILT2R&lt;n&gt;\_EL0, System Performance Monitors Event Filter Control Register 2, n = 0 - 63

The SPMEVFILT2R&lt;n&gt;\_EL0 characteristics are:

## Purpose

With SPMEVTYPER&lt;n&gt;\_EL0 and SPMEVFILTR&lt;n&gt;\_EL0, configures when event counter SPMEVCNTR&lt;n&gt;\_EL0 in System PMU &lt;s&gt; increments.

The contents of this register are IMPLEMENTATION DEFINED. For more information, see SPMEVTYPER&lt;n&gt;\_EL0.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMEVFILT2R&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

SPMEVFILT2R&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED |                        |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an IMPLEMENTATION DEFINED value.

## Accessing SPMEVFILT2R&lt;n&gt;\_EL0

To access SPMEVFILT2R&lt;n&gt;\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s and SPMSELR\_EL0.BANK to n[5:4].

SPMEVFILT2R&lt;n&gt;\_EL0 reads-as-zero and ignores writes if any of the following are true:

- Event counter &lt;n&gt; is not implemented by System PMU &lt;s&gt;.
- System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMEVFILT2R&lt;m&gt;\_EL0 ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b011 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then
```

```
X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m];
```

MSR SPMEVFILT2R&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b011 :m[3] | m[2:0] |

integer m = UInt(CRm&lt;0&gt;:op2&lt;2:0&gt;);

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVFILT2R_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else
```

## D24.5.42 SPMEVFILTR&lt;n&gt;\_EL0, System Performance Monitors Event Filter Control Register, n = 0 - 63

The SPMEVFILTR&lt;n&gt;\_EL0 characteristics are:

## Purpose

With SPMEVTYPER&lt;n&gt;\_EL0 and SPMEVFILT2R&lt;n&gt;\_EL0, configures when event counter SPMEVCNTR&lt;n&gt;\_EL0 in System PMU &lt;s&gt; increments.

The contents of this register are IMPLEMENTATION DEFINED. For more information, see SPMEVTYPER&lt;n&gt;\_EL0.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMEVFILTR&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

SPMEVFILTR&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED |                        |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an IMPLEMENTATION DEFINED value.

## Accessing SPMEVFILTR&lt;n&gt;\_EL0

To access SPMEVFILTR&lt;n&gt;\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s and SPMSELR\_EL0.BANK to n[5:4].

SPMEVFILTR&lt;n&gt;\_EL0 reads-as-zero and ignores writes if any of the following are true:

- Event counter &lt;n&gt; is not implemented by System PMU &lt;s&gt;.
- System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMEVFILTR&lt;m&gt;\_EL0 ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b010 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then
```

```
X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m];
```

MSR SPMEVFILTR&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b010 :m[3] | m[2:0] |

integer m = UInt(CRm&lt;0&gt;:op2&lt;2:0&gt;);

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVFILTR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else
```

## D24.5.43 SPMEVTYPER&lt;n&gt;\_EL0, System Performance Monitors Event Type Register, n = 0 - 63

The SPMEVTYPER&lt;n&gt;\_EL0 characteristics are:

## Purpose

With SPMEVFILTR&lt;n&gt;\_EL0 and SPMEVFILT2R&lt;n&gt;\_EL0, configures when event counter SPMEVCNTR&lt;n&gt;\_EL0 in System PMU &lt;s&gt; increments.

The contents of this register are IMPLEMENTATION DEFINED. An Event Type Select Register typically contains:

- Afield defining the event that the counter is responsive to, in the least-significant bits.
- Controls for per-counter filtering, such as by mode or state.
- Additional controls, such as for a per-counter state machine.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMEVTYPER&lt;n&gt;\_EL0 are UNDEFINED.

## Attributes

SPMEVTYPER&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED |                        |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an IMPLEMENTATION DEFINED value.

## Accessing SPMEVTYPER&lt;n&gt;\_EL0

To access SPMEVTYPER&lt;n&gt;\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s and SPMSELR\_EL0.BANK to n[5:4].

SPMEVTYPER&lt;n&gt;\_EL0 reads-as-zero and ignores writes if any of the following are true:

- Event counter &lt;n&gt; is not implemented by System PMU &lt;s&gt;.
- System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMEVTYPER&lt;m&gt;\_EL0 ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b001 :m[3] | m[2:0] |

```
integer m = UInt(CRm<0>:op2<2:0>); if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then
```

```
X[t, 64] = Zeros(64); else X[t, 64] = SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then X[t, 64] = Zeros(64); else X[t, 64] = SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m];
```

MSR SPMEVTYPER&lt;m&gt;\_EL0, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm         | op2    |
|-------|-------|--------|-------------|--------|
| 0b10  | 0b011 | 0b1110 | 0b001 :m[3] | m[2:0] |

integer m = UInt(CRm&lt;0&gt;:op2&lt;2:0&gt;);

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMEVTYPERn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else SPMEVTYPER_EL0[UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m] = X[t, 64]; elsif PSTATE.EL == EL3 then if !IsSPMUCounterImplemented(UInt(SPMSELR_EL0.SYSPMUSEL), (UInt(SPMSELR_EL0.BANK) * 16) + m) then return; else
```

## D24.5.44 SPMIIDR\_EL1, System PMU Implementation Identification Register

The SPMIIDR\_EL1 characteristics are:

## Purpose

Provides discovery information for System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMIIDR\_EL1 are UNDEFINED.

## Attributes

SPMIIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |           |    |         |       |          |    |             | 32   |
|------|-----------|----|---------|-------|----------|----|-------------|------|
|      |           |    |         | RES0  |          |    |             |      |
| 31   |           | 20 | 19      | 16 15 | 12       | 11 | 0           |      |
|      | ProductID |    | Variant |       | Revision |    | Implementer |      |

## Bits [63:32]

Reserved, RES0.

## ProductID, bits [31:20]

Part number, bits [11:0]. The part number is selected by the designer of the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Variant, bits [19:16]

Component major revision.

Defines either a variant of the component defined by SPMIIDR\_EL1.ProductID, or the major revision of the component.

When defining a major revision, SPMIIDR\_EL1.Variant and SPMIIDR\_EL1.Revision together form the revision number of the component, with SPMIIDR\_EL1.Variant being the most significant part and SPMIIDR\_EL1.Revision the least significant part. When a component is changed, SPMIIDR\_EL1.Variant or SPMIIDR\_EL1.Revision is increased to ensure that software can differentiate the different revisions of the component. If SPMIIDR\_EL1.Variant is increased then SPMIIDR\_EL1.Revision should be set to 0b0000 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Revision, bits [15:12]

Component minor revision.

When a component is changed:

- If SPMIIDR\_EL1.Variant and SPMIIDR\_EL1.Revision together form the revision number of the component then:

- SPMIIDR\_EL1.Variant or SPMIIDR\_EL1.Revision is increased to ensure that software can differentiate the different revisions of the component.
- If Variant is increased then Revision should be set to 0b0000 .
- Otherwise, SPMIIDR\_EL1.Revision is increased to ensure that software can differentiate the different revisions of the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Implementer, bits [11:0]

Contains the JEP106 manufacturer's identification code of the designer of the System PMU.

The code identifies the designer of the component, which might not be the same as the implementer of the device containing the component.

For an implementation designed by Arm, this field reads as 0x43B .

This field has an IMPLEMENTATION DEFINED value.

Bits [11:8] contain the JEP106 bank identifier of the designer minus 1.

Bit 7 is RES0.

Bits [6:0] contain bits [6:0] of the JEP106 manufacturer's identification code of the designer.

Access to this field is RO.

## Accessing SPMIIDR\_EL1

To access SPMIIDR\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMIIDR\_EL1 reads-as-zero if any of the following are true:

- System PMU &lt;s&gt; is not implemented.
- System PMU &lt;s&gt; does not implement SPMIIDR\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMIIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1101 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMID == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMIIDR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMIIDR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMIIDR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

## D24.5.45 SPMINTENCLR\_EL1, System Performance Monitors Interrupt Enable Clear Register

The SPMINTENCLR\_EL1 characteristics are:

## Purpose

Disables the generation of interrupt requests on overflows from event counters in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMINTENCLR\_EL1 are UNDEFINED.

## Attributes

SPMINTENCLR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32   |
|------|------------------------------------------------------------------------------------------------|

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Event counter &lt;m&gt; overflow interrupt request disable.

| P<m>   | Meaning                                                           |
|--------|-------------------------------------------------------------------|
| 0b0    | Event counter <m> in System PMU<s> interrupt request is disabled. |
| 0b1    | Event counter <m> in System PMU<s> interrupt request is enabled.  |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if any of the following are true:
- event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;
- event counter &lt;m&gt; does not implement an overflow flag
- System PMU &lt;s&gt; does not implement an overflow interrupt request
- Otherwise, access to this field is W1C.

## Accessing SPMINTENCLR\_EL1

To access SPMINTENCLR\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMINTENCLR\_EL1 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1110 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMINTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMINTENCLR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMINTENCLR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMINTENCLR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMINTENCLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1110 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMINTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMINTENCLR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMINTENCLR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMINTENCLR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.46 SPMINTENSET\_EL1, System Performance Monitors Interrupt Enable Set Register

The SPMINTENSET\_EL1 characteristics are:

## Purpose

Enables the generation of interrupt requests on overflows from event counters in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMINTENSET\_EL1 are UNDEFINED.

## Attributes

SPMINTENSET\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32   |
|------|------------------------------------------------------------------------------------------------|

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Event counter &lt;m&gt; overflow interrupt request enable.

| P<m>   | Meaning                                                           |
|--------|-------------------------------------------------------------------|
| 0b0    | Event counter <m> in System PMU<s> interrupt request is disabled. |
| 0b1    | Event counter <m> in System PMU<s> interrupt request is enabled.  |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if any of the following are true:
- event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;
- event counter &lt;m&gt; does not implement an overflow flag
- System PMU &lt;s&gt; does not implement an overflow interrupt request
- Otherwise, access to this field is W1S.

## Accessing SPMINTENSET\_EL1

To access SPMINTENSET\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMINTENSET\_EL1 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1110 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMINTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMINTENSET_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMINTENSET_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMINTENSET_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMINTENSET\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b1001 | 0b1110 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMINTEN == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMINTENSET_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMINTENSET_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMINTENSET_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.47 SPMOVSCLR\_EL0, System Performance Monitors Overflow Flag Status Clear Register

The SPMOVSCLR\_EL0 characteristics are:

## Purpose

Clears the state of overflow bits for event counters in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMOVSCLR\_EL0 are UNDEFINED.

## Attributes

SPMOVSCLR\_EL0 is a 64-bit register.

## Field descriptions

| 63   | 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32   |
|------|------------------------------------------------------------------------------------------------|

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Event counter &lt;m&gt; unsigned overflow bit clear.

| P<m>   | Meaning                                                |
|--------|--------------------------------------------------------|
| 0b0    | Event counter <m> in System PMU<s> has not overflowed. |
| 0b1    | Event counter <m> in System PMU<s> has overflowed.     |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if any of the following are true:
- event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;
- event counter &lt;m&gt; does not implement an overflow flag
- Otherwise, access to this field is W1C.

## Accessing SPMOVSCLR\_EL0

To access SPMOVSCLR\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMOVSCLR\_EL0 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMOVSCLR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMOVSCLR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.48 SPMOVSSET\_EL0, System Performance Monitors Overflow Flag Status Set Register

The SPMOVSSET\_EL0 characteristics are:

## Purpose

Sets the state of overflow bits for event counters in System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMOVSSET\_EL0 are UNDEFINED.

## Attributes

SPMOVSSET\_EL0 is a 64-bit register.

## Field descriptions

| 63   | 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32   |
|------|------------------------------------------------------------------------------------------------|

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Event counter &lt;m&gt; unsigned overflow bit set.

| P<m>   | Meaning                                                |
|--------|--------------------------------------------------------|
| 0b0    | Event counter <m> in System PMU<s> has not overflowed. |
| 0b1    | Event counter <m> in System PMU<s> has overflowed.     |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if any of the following are true:
- event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;
- event counter &lt;m&gt; does not implement an overflow flag
- Otherwise, access to this field is W1S.

## Accessing SPMOVSSET\_EL0

To access SPMOVSSET\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMOVSSET\_EL0 reads-as-zero and ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1110 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMOVSSET\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1110 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMOVS == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMOVSSET_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.49 SPMROOTCR\_EL3, System Performance Monitors Root and Realm Control Register

The SPMROOTCR\_EL3 characteristics are:

## Purpose

Controls observability of Root and Realm events by System PMU &lt;s&gt;.

## Configuration

This register is present only when FEAT\_RME is implemented, FEAT\_SPMU is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMROOTCR\_EL3 are UNDEFINED.

## Attributes

SPMROOTCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63    |     | 32      |
|-------|-----|---------|
| 31 30 | 3   | 1 0     |
| RAO   | NAO | RLO RTO |

## IMPLEMENTATIONDEFINED, bits [63:32]

IMPLEMENTATION DEFINED observation controls. Additional IMPLEMENTATION DEFINED bits to control certain types of filter or events by System PMU &lt;s&gt;.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an IMPLEMENTATION DEFINED value.

## Bit [31]

Reserved, RAO.

Indicates SPMROOTCR\_EL3 is implemented by System PMU &lt;s&gt;.

## Bits [30:4]

Reserved, RES0.

## NAO, bit [3]

## When System PMU &lt;s&gt; can count or monitor non-attributable events:

Non-attributable Observation. Controls whether events or monitorable characteristics not attributable with any source can be monitored by System PMU &lt;s&gt;.

| NAO   | Meaning                                                                         |
|-------|---------------------------------------------------------------------------------|
| 0b0   | Events not attributable with any event source are not counted by System PMU<s>. |

| 0b1   | Counting non-attributable events by System PMU<s> is not prevented by this mechanism.   |
|-------|-----------------------------------------------------------------------------------------|

When both SPMROOTCR\_EL3 and SPMSCR\_EL1 are implemented, non-attributable events are counted only if both SPMROOTCR\_EL3.NAO is 1 and SPMSCR\_EL1.{NAO, SO} is nonzero.

SPMROOTCR\_EL3.NAO has the opposite reset polarity to SPMSCR\_EL1.NAO.

The reset behavior of this field is:

- On a System PMU reset, this field resets to '1' .

## Otherwise:

Reserved, RES0.

## Bit [2]

Reserved, RES0.

## RLO, bit [1]

Realm Observation. Controls whether events or monitorable characteristics attributable to a Realm event source can be monitored by System PMU &lt;s&gt;.

| RLO   | Meaning                                                                                                            |
|-------|--------------------------------------------------------------------------------------------------------------------|
| 0b0   | Events attributable to a Realm event source are not counted by System PMU<s>.                                      |
| 0b1   | Counting events by System PMU<s> that are attributable to a Realm event source is not prevented by this mechanism. |

The reset behavior of this field is:

- On a System PMU reset, this field resets to '0' .

## RTO, bit [0]

Root Observation. Controls whether events or monitorable characteristics attributable to a Root event source can be monitored by System PMU &lt;s&gt;.

| RTO   | Meaning                                                                                                           |
|-------|-------------------------------------------------------------------------------------------------------------------|
| 0b0   | Events attributable to a Root event source are not counted by System PMU<s>.                                      |
| 0b1   | Counting events by System PMU<s> that are attributable to a Root event source is not prevented by this mechanism. |

The reset behavior of this field is:

- On a System PMU reset, this field resets to '0' .

## Accessing SPMROOTCR\_EL3

To access SPMROOTCR\_EL3 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMROOTCR\_EL3 reads-as-zero and ignores writes if any of the following are true:

- System PMU &lt;s&gt; is not implemented.
- System PMU &lt;s&gt; does not implement SPMROOTCR\_EL3.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMROOTCR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b110 | 0b1001 | 0b1110 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_RME) && IsFeatureImplemented(FEAT_SPMU) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = SPMROOTCR_EL3[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMROOTCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b110 | 0b1001 | 0b1110 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_RME) && IsFeatureImplemented(FEAT_SPMU) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.SPMROOTCR_EL3 == '1' AArch64.SystemAccessTrap(EL3, 0x18); else SPMROOTCR_EL3[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

```
then
```

## D24.5.50 SPMSCR\_EL1, System Performance Monitors Secure Control Register

The SPMSCR\_EL1 characteristics are:

## Purpose

Controls observability of Secure events by System PMU &lt;s&gt;, and optionally controls Secure attributes for message signaled interrupts and Non-secure access to the performance monitor registers.

## Configuration

This register is present only when Secure EL1 is implemented, FEAT\_SPMU is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMSCR\_EL1 are UNDEFINED.

## Attributes

SPMSCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     |                        | 32                     |                        |                        |                        |                        |                        |
|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 31 30                  |                        | 0                      |                        |                        |                        |                        |                        |
| RAO                    | RES0                   | SO                     |                        |                        |                        |                        |                        |

## IMPLEMENTATIONDEFINED, bits [63:32]

IMPLEMENTATION DEFINED observation controls. Additional IMPLEMENTATION DEFINED bits to control certain types of filter or events by System PMU &lt;s&gt;.

The reset behavior of this field is:

- On a System PMU reset, this field resets to an IMPLEMENTATION DEFINED value.

## Bit [31]

Reserved, RAO.

Indicates SPMSCR\_EL1 is implemented by System PMU &lt;s&gt;.

This field reads-as-one.

## Bits [30:5]

Reserved, RES0.

## NAO, bit [4]

## When System PMU &lt;s&gt; can count or monitor non-attributable events:

Non-attributable Observation. Controls whether events or monitorable characteristics not attributable with any source can be monitored by System PMU &lt;s&gt;.

| NAO   | Meaning                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------|
| 0b0   | Events not attributable with any event source are not counted by System PMU<s>, unless overridden by SPMSCR_EL1.SO. |
| 0b1   | Counting non-attributable events by System PMU<s> is not prevented by this mechanism.                               |

When both SPMROOTCR\_EL3 and SPMSCR\_EL1 are implemented, non-attributable events are counted only if both SPMROOTCR\_EL3.NAO is 1 and SPMSCR\_EL1.{NAO, SO} is nonzero.

SPMSCR\_EL1.NAO has the opposite reset polarity to SPMROOTCR\_EL3.NAO.

This field is optional if Root and Realm states are not implemented. When this field is not implemented, System PMU &lt;s&gt; behaves as if SPMSCR\_EL1.NAO is 0, and whether events or monitorable characteristics not attributable with any source can be monitored is controlled by SPMSCR\_EL1.SO.

The reset behavior of this field is:

- On a System PMU reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bits [3:1]

Reserved, RES0.

## SO, bit [0]

Secure Observation. Controls whether events or monitorable characteristics attributable to a Secure event source can be monitored by System PMU &lt;s&gt;.

| SO   | Meaning                                                                                                             |
|------|---------------------------------------------------------------------------------------------------------------------|
| 0b0  | Events attributable to a Secure event source are not counted by System PMU<s>.                                      |
| 0b1  | Counting events by System PMU<s> that are attributable to a Secure event source is not prevented by this mechanism. |

Also controls whether events or monitorable characteristics not attributable with any source can be monitored by System PMU &lt;s&gt;. See SPMSCR\_EL1.NAO.

The reset behavior of this field is:

- On a System PMU reset, this field resets to '0' .

## Accessing SPMSCR\_EL1

To access SPMSCR\_EL1 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMSCR\_EL1 reads-as-zero and ignores writes if any of the following are true:

- System PMU &lt;s&gt; is not implemented.
- System PMU &lt;s&gt; does not implement SPMSCR\_EL1.

SPMSCR\_EL1 is UNDEFINED if accessed in Non-secure or Realm state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SPMSCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b111 | 0b1001 | 0b1110 | 0b111 |

```
if !(HaveELUsingSecurityState(EL1, TRUE) && IsFeatureImplemented(FEAT_SPMU) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif IsCurrentSecurityState(SS_NonSecure) || (IsFeatureImplemented(FEAT_RME) && ↪ → IsCurrentSecurityState(SS_Realm)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMSCR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMSCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == ↪ → '00' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> == '00' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMSCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)]; elsif PSTATE.EL == EL3 then X[t, 64] = SPMSCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)];
```

MSR SPMSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b111 | 0b1001 | 0b1110 | 0b111 |

```
if !(HaveELUsingSecurityState(EL1, TRUE) && IsFeatureImplemented(FEAT_SPMU) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif IsCurrentSecurityState(SS_NonSecure) || (IsFeatureImplemented(FEAT_RME) && ↪ → IsCurrentSecurityState(SS_Realm)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMSCR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMSCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMSCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMSCR_EL1[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```

## D24.5.51 SPMSELR\_EL0, System Performance Monitors Select Register

The SPMSELR\_EL0 characteristics are:

## Purpose

Selects the System PMU and event counter registers to access.

## Configuration

This register is present only when FEAT\_SPMU is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMSELR\_EL0 are UNDEFINED.

## Attributes

SPMSELR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## SYSPMUSEL, bits [9:4]

System PMU Select. Selects a System PMU &lt;s&gt; to access.

Values 0x20 to 0x3F are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [3:2]

Reserved, RES0.

## BANK, bits [1:0]

System PMU bank access control. Selects a bank of 16 System PMU event counters and related controls to access.

| BANK   | Meaning                         |
|--------|---------------------------------|
| 0b00   | Select event counters 0 to 15.  |
| 0b01   | Select event counters 16 to 31. |
| 0b10   | Select event counters 32 to 47. |
| 0b11   | Select event counters 48 to 63. |

The reset behavior of this field is:

· On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SPMSELR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SPMSELR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGRTR2_EL2.nSPMSELR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMSELR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nSPMSELR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMSELR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SPMSELR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = SPMSELR_EL0;
```

MSR SPMSELR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_SPMU) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMSELR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMSELR_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMSELR_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMSELR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMSELR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then SPMSELR_EL0 = X[t, 64];
```

## D24.5.52 SPMZR\_EL0, System Performance Monitors Zero with Mask

The SPMZR\_EL0 characteristics are:

## Purpose

Zero the set of System PMU event counters specified by the mask written to SPMZR\_EL0.

## Configuration

This register is present only when FEAT\_SPMU2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SPMZR\_EL0 are UNDEFINED.

## Attributes

SPMZR\_EL0 is a 64-bit register.

## Field descriptions

60

59

58

57

56

55

P60

63

P63

62

P62

61

P61

P59

P58

P57

P56

P55

54

P54

53

P53

52

P52

51

P51

50

P50

49

P49

48

P48

47

P47

46

P46

45

P45

44

P44

43

P43

42

P42

41

P41

40

P40

39

P39

38

P38

37

P37

36

P36

35

P35

34

P34

33

P33

32

P32

| 31 30   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|-----------------------------------------------------------------------------------|

## P&lt;m&gt; , bits [m], for m = 63 to 0

Zero event counter &lt;m&gt;.

| P<m>   | Meaning                                        |
|--------|------------------------------------------------|
| 0b0    | Write is ignored.                              |
| 0b1    | Set event counter<m> in System PMU<s> to zero. |

The reset behavior of this field is:

- On a System PMU reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When event counter &lt;m&gt; is not implemented by System PMU &lt;s&gt;, access to this field is RAZ/WI.
- Otherwise, access to this field is WO/RAZ.

## Accessing SPMZR\_EL0

To access SPMZR\_EL0 for System PMU &lt;s&gt;, set SPMSELR\_EL0.SYSPMUSEL to s.

SPMZR\_EL0 ignores writes if System PMU &lt;s&gt; is not implemented.

Accesses to this register use the following encodings in the System register encoding space:

MSR SPMZR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b1001 | 0b1100 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_SPMU2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif MDSCR_EL1.EnSPM == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif !ELIsInHost(EL0) && SPMACCESSR_EL1<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && ↪ → SCR_EL3.FGTEn2 == '0') || HDFGWTR2_EL2.nSPMEVCNTRn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMZR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nSPMEVCNTRn_EL0 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.EnSPM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && SPMACCESSR_EL2<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
SPMZR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnPM2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != ↪ → '11' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnPM2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && SPMACCESSR_EL3<UInt(SPMSELR_EL0.SYSPMUSEL) * 2+:2> != '11' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SPMZR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64]; elsif PSTATE.EL == EL3 then SPMZR_EL0[UInt(SPMSELR_EL0.SYSPMUSEL)] = X[t, 64];
```