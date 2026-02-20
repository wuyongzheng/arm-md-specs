## G8.4 Performance Monitors registers

This section lists the Performance Monitors registers in AArch32.

## G8.4.1 PMCCFILTR, Performance Monitors Cycle Count Filter Register

The PMCCFILTR characteristics are:

## Purpose

Determines the modes in which the Cycle Counter, PMCCNTR, increments.

## Configuration

AArch32 System register PMCCFILTR bits [31:0] are architecturally mapped to AArch64 System register PMCCFILTR\_EL0[31:0].

AArch32 System register PMCCFILTR bits [31:0] are architecturally mapped to External register PMCCFILTR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCCFILTR are UNDEFINED.

## Attributes

PMCCFILTR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 30 29 28 27 26   | 22 21 20   | 0    |
|------|------------------|------------|------|
| P    | U NSK NSU NSH    | RLU        | RES0 |

## P, bit [31]

Privileged filtering. Controls counting cycles in EL1 and, if EL3 is using AArch32, EL3.

| P   | Meaning                                                                |
|-----|------------------------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of cycles.                   |
| 0b1 | The PE does not count cycles in EL1 and, if EL3 is using AArch32, EL3. |

If Secure and Non-secure states are implemented, then counting cycles in Non-secure EL1 is further controlled by PMCCFILTR.NSK.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

User filtering. Controls counting cycles in EL0.

| U   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of cycles. |
| 0b1 | The PE does not count cycles in EL0.                 |

If Secure and Non-secure states are implemented, then counting cycles in Non-secure EL0 is further controlled by PMCCFILTR.NSU.

If FEAT\_RME is implemented, then counting cycles in Realm EL0 is further controlled by PMCCFILTR.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting cycles in Non-secure EL1. If PMCCFILTR.NSK is not equal to PMCCFILTR.P, then the PE does not count cycles in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of cycles in Non-secure EL1.

| NSK   | Meaning                                                                                                                                            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR.P == 1, the PE does not count cycles in Non-secure EL1. |
| 0b1   | When PMCCFILTR.P == 0, the PE does not count cycles in Non-secure EL1. When PMCCFILTR.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting cycles in Non-secure EL0. If PMCCFILTR.NSU is not equal to PMCCFILTR.U, then the PE does not count cycles in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of cycles in Non-secure EL0.

| NSU   | Meaning                                                                                                                                            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR.U == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR.U == 1, the PE does not count cycles in Non-secure EL0. |
| 0b1   | When PMCCFILTR.U == 0, the PE does not count cycles in Non-secure EL0. When PMCCFILTR.U == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting cycles in EL2.

| NSH   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE does not count cycles in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of cycles. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting cycles in Secure EL2 is further controlled by PMCCFILTR.SH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [26:22]

Reserved, RES0.

RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting cycles in Realm EL0. If PMCCFILTR.RLU is not equal to PMCCFILTR.U, then the PE does not count cycles in Realm EL0. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL0.

| RLU   | Meaning                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR.U == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR.U == 1, the PE does not count cycles in Realm EL0. |
| 0b1   | When PMCCFILTR.U == 0, the PE does not count cycles in Realm EL0. When PMCCFILTR.U == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [20:0]

Reserved, RES0.

## Accessing PMCCFILTR

PMCCFILTR can also be accessed by using PMXEVTYPER with PMSELR.SEL set to 0b11111 .

Permitted reads and writes of PMCCFILTR are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.C == 0.

Permitted writes of PMCCFILTR are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.{UEN,CR} == {1,1}.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b1111 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCCFILTR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.C == '0' then R[t] = Zeros(32); else R[t] = PMCCFILTR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCCFILTR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCCFILTR; elsif PSTATE.EL == EL3 then R[t] = PMCCFILTR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b1111 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMCCFILTR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.C == '0' || ↪ → PMUSERENR_EL0.CR == '1') then return;
```

```
else PMCCFILTR = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCCFILTR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCCFILTR = R[t]; elsif PSTATE.EL == EL3 then PMCCFILTR = R[t];
```

## G8.4.2 PMCCNTR, Performance Monitors Cycle Count Register

The PMCCNTR characteristics are:

## Purpose

Holds the value of the processor Cycle Counter, CCNT, that counts processor clock cycles. See 'Time as measured by the Performance Monitors cycle counter' for more information.

PMCCFILTR determines the modes and states in which the PMCCNTR can increment.

## Configuration

PMCCNTRis a 64-bit register that can also be accessed as a 32-bit value. If it is accessed as a 32-bit register, accesses read and write bits [31:0] and do not modify bits [63:32].

All counters are subject to any changes in clock frequency, including clock stopping caused by the WFI and WFE instructions. This means that it is CONSTRAINED UNPREDICTABLE whether or not PMCCNTR continues to increment when clocks are stopped by WFI and WFE instructions.

AArch32 System register PMCCNTR bits [63:0] are architecturally mapped to AArch64 System register PMCCNTR\_EL0[63:0].

AArch32 System register PMCCNTR bits [63:0] are architecturally mapped to External register PMCCNTR\_EL0[63:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCCNTR are UNDEFINED.

## Attributes

PMCCNTRis a 64-bit register.

## Field descriptions

CCNT

63

32

CCNT

31

0

<!-- image -->

## CCNT, bits [63:0]

Cycle count. Depending on the values of PMCR.{LC,D}, this field increments in one of the following ways:

- Every processor clock cycle.
- Every 64th processor clock cycle.

Writing 1 to PMCR.C sets this field to 0.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMCCNTR

Permitted reads and writes of PMCCNTR are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.C == 0.

Permitted writes of PMCCNTR are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.{UEN,CR} == {1,1}.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1101 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,CR,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<CR,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<CR,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCCNTR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.C == '0' then R[t] = Zeros(32); else R[t] = PMCCNTR<31:0>; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCCNTR<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCCNTR<31:0>; elsif PSTATE.EL == EL3 then R[t] = PMCCNTR<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1101 | 0b000  |

if !(IsFeatureImplemented(FEAT\_AA32) &amp;&amp; IsFeatureImplemented(FEAT\_PMUv3)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMCCNTR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.C == '0' || ↪ → PMUSERENR_EL0.CR == '1') then return; else PMCCNTR<31:0> = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCCNTR<31:0> = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCCNTR<31:0> = R[t]; elsif PSTATE.EL == EL3 then PMCCNTR<31:0> = R[t];
```

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1001 | 0b0000 |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,CR,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<CR,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<CR,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCCNTR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1.C == '0' then R[t, t2] = Zeros(64); else R[t, t2] = PMCCNTR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else R[t, t2] = PMCCNTR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else R[t, t2] = PMCCNTR; elsif PSTATE.EL == EL3 then R[t, t2] = PMCCNTR;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b1001 | 0b0000 |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); else AArch64.AArch32SystemAccessTrap(EL1, 0x04); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMCCNTR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1.C == '0' || ↪ → PMUSERENR_EL0.CR == '1') then return; else PMCCNTR = R[t, t2]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x04);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else PMCCNTR = R[t, t2]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x04); else PMCCNTR = R[t, t2]; elsif PSTATE.EL == EL3 then PMCCNTR = R[t, t2];
```

## G8.4.3 PMCEID0, Performance Monitors Common Event Identification register 0

The PMCEID0 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x0000 to 0x001F .

For more information about the Common events and the use of the PMCEIDn registers, see 'The PMU event number space and common events'.

## Configuration

AArch32 System register PMCEID0 bits [31:0] are architecturally mapped to AArch64 System register PMCEID0\_EL0[31:0].

AArch32 System register PMCEID0 bits [31:0] are architecturally mapped to External register PMCEID0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCEID0 are UNDEFINED.

## Attributes

PMCEID0 is a 32-bit register.

## Field descriptions

<!-- image -->

## ID&lt;n&gt; , bits [n], for n = 31 to 0

ID[n] corresponds to Common event n.

For each bit:

| ID<n>   | Meaning                                              |
|---------|------------------------------------------------------|
| 0b0     | The Common event is not implemented, or not counted. |
| 0b1     | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID0

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b110  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID0; elsif PSTATE.EL == EL3 then R[t] = PMCEID0;
```

## G8.4.4 PMCEID1, Performance Monitors Common Event Identification register 1

The PMCEID1 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x0020 to 0x003F .

For more information about the Common events and the use of the PMCEIDn registers see 'The PMU event number space and common events'.

## Configuration

AArch32 System register PMCEID1 bits [31:0] are architecturally mapped to AArch64 System register PMCEID1\_EL0[31:0].

AArch32 System register PMCEID1 bits [31:0] are architecturally mapped to External register PMCEID1[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCEID1 are UNDEFINED.

## Attributes

PMCEID1 is a 32-bit register.

## Field descriptions

<!-- image -->

## ID&lt;n&gt; , bits [n], for n = 31 to 0

ID[n] corresponds to Common event ( 0x0020 + n).

For each bit:

| ID<n>   | Meaning                                              |
|---------|------------------------------------------------------|
| 0b0     | The Common event is not implemented, or not counted. |
| 0b1     | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID1

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b111  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID1; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID1; elsif PSTATE.EL == EL3 then R[t] = PMCEID1;
```

## G8.4.5 PMCEID2, Performance Monitors Common Event Identification register 2

The PMCEID2 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x4000 to 0x401F .

For more information about the Common events and the use of the PMCEIDn registers see 'The PMU event number space and common events'.

## Configuration

AArch32 System register PMCEID2 bits [31:0] are architecturally mapped to AArch64 System register PMCEID0\_EL0[63:32].

AArch32 System register PMCEID2 bits [31:0] are architecturally mapped to External register PMCEID2[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3p1 is implemented. Otherwise, direct accesses to PMCEID2 are UNDEFINED.

## Attributes

PMCEID2 is a 32-bit register.

## Field descriptions

<!-- image -->

## IDhi&lt;n&gt; , bits [n], for n = 31 to 0

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

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID2

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3p1)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else
```

```
UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID2; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID2; elsif PSTATE.EL == EL3 then R[t] = PMCEID2;
```

## G8.4.6 PMCEID3, Performance Monitors Common Event Identification register 3

The PMCEID3 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x4020 to 0x403F .

For more information about the Common events and the use of the PMCEIDn registers see 'The PMU event number space and common events'.

## Configuration

AArch32 System register PMCEID3 bits [31:0] are architecturally mapped to AArch64 System register PMCEID1\_EL0[63:32].

AArch32 System register PMCEID3 bits [31:0] are architecturally mapped to External register PMCEID3[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3p1 is implemented. Otherwise, direct accesses to PMCEID3 are UNDEFINED.

## Attributes

PMCEID3 is a 32-bit register.

## Field descriptions

<!-- image -->

## IDhi&lt;n&gt; , bits [n], for n = 31 to 0

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

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID3

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3p1)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && ↪ → IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR.TID == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else
```

```
UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCEIDn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID3; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID3; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCEID3; elsif PSTATE.EL == EL3 then R[t] = PMCEID3;
```

## G8.4.7 PMCNTENCLR, Performance Monitors Count Enable Clear register

The PMCNTENCLR characteristics are:

## Purpose

Allows software to disable the following counters:

- The cycle counter PMCCNTR.
- The event counters PMEVCNTR&lt;n&gt;.

Reading from this register shows which counters are enabled.

## Configuration

AArch32 System register PMCNTENCLR bits [31:0] are architecturally mapped to AArch32 System register PMCNTENSET[31:0].

AArch32 System register PMCNTENCLR bits [31:0] are architecturally mapped to AArch64 System register PMCNTENCLR\_EL0[31:0].

AArch32 System register PMCNTENCLR bits [31:0] are architecturally mapped to AArch64 System register PMCNTENSET\_EL0[31:0].

AArch32 System register PMCNTENCLR bits [31:0] are architecturally mapped to External register PMCNTENCLR\_EL0[31:0].

AArch32 System register PMCNTENCLR bits [31:0] are architecturally mapped to External register PMCNTENSET\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCNTENCLR are UNDEFINED.

## Attributes

PMCNTENCLRis a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------------------------------------------------|

## C, bit [31]

PMCCNTRdisable. On writes, allows software to disable PMCCNTR. On reads, returns the PMCCNTR enable status.

| C   | Meaning          |
|-----|------------------|
| 0b0 | PMCCNTRdisabled. |
| 0b1 | PMCCNTRenabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:

- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;disable. On writes, allows software to disable PMEVCNTR&lt;m&gt;. On reads, returns the PMEVCNTR&lt;m&gt;enable status.

| P<m>   | Meaning              |
|--------|----------------------|
| 0b0    | PMEVCNTR<m>disabled. |
| 0b1    | PMEVCNTR<m>enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1C.

## Accessing PMCNTENCLR

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCNTEN == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCNTENCLR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCNTENCLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCNTENCLR; elsif PSTATE.EL == EL3 then R[t] = PMCNTENCLR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMCNTEN == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCNTENCLR = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCNTENCLR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCNTENCLR = R[t]; elsif PSTATE.EL == EL3 then PMCNTENCLR = R[t];
```

## G8.4.8 PMCNTENSET, Performance Monitors Count Enable Set register

The PMCNTENSET characteristics are:

## Purpose

Allows software to enable the following counters:

- The cycle counter PMCCNTR.
- The event counters PMEVCNTR&lt;n&gt;.

Reading from this register shows which counters are enabled.

## Configuration

AArch32 System register PMCNTENSET bits [31:0] are architecturally mapped to AArch32 System register PMCNTENCLR[31:0].

AArch32 System register PMCNTENSET bits [31:0] are architecturally mapped to AArch64 System register PMCNTENSET\_EL0[31:0].

AArch32 System register PMCNTENSET bits [31:0] are architecturally mapped to AArch64 System register PMCNTENCLR\_EL0[31:0].

AArch32 System register PMCNTENSET bits [31:0] are architecturally mapped to External register PMCNTENSET\_EL0[31:0].

AArch32 System register PMCNTENSET bits [31:0] are architecturally mapped to External register PMCNTENCLR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCNTENSET are UNDEFINED.

## Attributes

PMCNTENSET is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------------------------------------------------|

## C, bit [31]

PMCCNTRenable. On writes, allows software to enable PMCCNTR. On reads, returns the PMCCNTR enable status.

| C   | Meaning          |
|-----|------------------|
| 0b0 | PMCCNTRdisabled. |
| 0b1 | PMCCNTRenabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:

- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;enable. On writes, allows software to enable PMEVCNTR&lt;m&gt;. On reads, returns the PMEVCNTR&lt;m&gt;enable status.

| P<m>   | Meaning              |
|--------|----------------------|
| 0b0    | PMEVCNTR<m>disabled. |
| 0b1    | PMEVCNTR<m>enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1S.

## Accessing PMCNTENSET

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMCNTEN == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCNTENSET; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCNTENSET; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCNTENSET; elsif PSTATE.EL == EL3 then R[t] = PMCNTENSET;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMCNTEN == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCNTENSET = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCNTENSET = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCNTENSET = R[t]; elsif PSTATE.EL == EL3 then PMCNTENSET = R[t];
```

## G8.4.9 PMCR, Performance Monitors Control Register

The PMCR characteristics are:

## Purpose

Provides details of the Performance Monitors implementation, including the number of counters implemented, and configures and controls the counters.

## Configuration

AArch32 System register PMCR bits [31:0] are architecturally mapped to AArch64 System register PMCR\_EL0[31:0].

AArch32 System register PMCR bits [10:0] are architecturally mapped to External register PMCR\_EL0[10:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMCR are UNDEFINED.

## Attributes

PMCRis a 32-bit register.

## Field descriptions

<!-- image -->

## IMP, bits [31:24]

## When FEAT\_PMUv3p7 is not implemented:

Implementer code.

If this field is zero, then PMCR.IDCODE is RES0 and software must use MIDR to identify the PE.

Otherwise, this field and PMCR.IDCODE identify the PMU implementation to software. The implementer codes are allocated by Arm. A nonzero value has the same interpretation as MIDR.Implementer.

This field has an IMPLEMENTATION DEFINED value.

Arm deprecates use of this field.

Access to this field is RO.

## Otherwise:

Reserved, RAZ.

## IDCODE, bits [23:16]

## When PMCR.IMP != '00000000':

Identification code. Arm deprecates use of this field.

Each implementer must maintain a list of identification codes that are specific to the implementer. A specific implementation is identified by the combination of the implementer code and the identification code.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## N, bits [15:11]

Indicates the number of event counters implemented. This value is in the range of 0b00000 -0b11111 . If the value is 0b00000 , then only PMCCNTR is implemented. If the value is 0b11111 , then PMCCNTR and 31 event counters are implemented.

If EL2 is implemented, then all of the following apply:

- If EL2 is using AArch32, then reads of this field from Non-secure EL1 and Non-secure EL0 return the Effective value of HDCR.HPMN.
- If EL2 is enabled in the current Security state and using AArch64, then reads of this field from EL1 and EL0 return the Effective value of MDCR\_EL2.HPMN.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bit [10]

Reserved, RES0.

## FZO, bit [9]

## When FEAT\_PMUv3p7 is implemented:

Freeze-on-overflow. Stop event counters on overflow.

| FZO   | Meaning                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------|
| 0b0   | Do not freeze on overflow.                                                                              |
| 0b1   | Affected counters do not count when PMOVSR[m] is 1 for any event counter PMEVCNTR<m>in the first range. |

The counters affected by this field are:

- The event counters in the first range.
- If PMCR.DP is 1, the cycle counter PMCCNTR.

Other event counters are not affected by this field.

When PMCR.DP is 0, PMCCNTR is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN or HDCR.HPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [8]

Reserved, RES0.

LP, bit [7]

## When FEAT\_PMUv3p5 is implemented:

Long event counter enable. Determines when unsigned overflow is recorded by PMOVSR.P[n].

| LP   | Meaning                                                                                 |
|------|-----------------------------------------------------------------------------------------|
| 0b0  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>[31:0]. |
| 0b1  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>[63:0]. |

The counters affected by this field are the event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN or HDCR.HPMN.

Other event counters and PMCCNTR are not affected by this field.

PMEVCNTR&lt;n&gt;[63:32] is not accessible in AArch32 state.

If the highest implemented Exception level is using AArch32, it is IMPLEMENTATION DEFINED whether this field is read/write or RAZ/WI.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LC, bit [6]

Long cycle counter enable. Determines when unsigned overflow is recorded by PMOVSR.C.

| LC   | Meaning                                                                             |
|------|-------------------------------------------------------------------------------------|
| 0b0  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR[31:0]. |
| 0b1  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR[63:0]. |

Arm deprecates use of PMCR.LC = 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DP, bit [5]

When ((HaveEL(EL3) || (IsFeatureImplemented(FEAT\_PMUv3p1) &amp;&amp; HaveEL(EL2))) || IsFeatureImplemented(FEAT\_PMUv3p7)) || IsFeatureImplemented(FEAT\_SPE\_DPFZS):

Disable cycle counter when event counting is prohibited.

| DP   | Meaning                                                     |
|------|-------------------------------------------------------------|
| 0b0  | Cycle counting by PMCCNTRis not affected by this mechanism. |

| DP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1  | Cycle counting by PMCCNTRis disabled in prohibited regions and when event counting is frozen: • If FEAT_PMUv3p1 is implemented, EL2 is implemented, and MDCR_EL2.HPMD or HDCR.HPMD is 1, then cycle counting by PMCCNTRis disabled at EL2. • If FEAT_PMUv3p7 is implemented and event counting is frozen by PMCR.FZO, then cycle counting by PMCCNTRis disabled. • If FEAT_PMUv3p7 is implemented, EL3 is implemented and using AArch64, and MDCR_EL3.MPMX is 1, then cycle counting by PMCCNTRis disabled at EL3. • If EL3 is implemented, MDCR_EL3.SPME or SDCR.SPME is 0, and one of FEAT_PMUv3p7 is not implemented, EL3 is using AArch32, or MDCR_EL3.MPMX is 0, then cycle counting by PMCCNTRis disabled at EL3 and in Secure state. |

The conditions when this field disables the cycle counter are the same as when event counting by an event counter in the first range is prohibited or frozen. For more information about event counter ranges, see MDCR\_EL2.HPMN or HDCR.HPMN.

For more information, see 'Prohibiting event and cycle counting'.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

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

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## D, bit [3]

Clock divider.

| D   | Meaning                                                 |
|-----|---------------------------------------------------------|
| 0b0 | When enabled, PMCCNTRcounts every clock cycle.          |
| 0b1 | When enabled, PMCCNTRcounts once every 64 clock cycles. |

If the Effective value of PMCR.LC is 1, then this field is ignored and the cycle counter counts every clock cycle.

Arm deprecates use of PMCR.D = 1.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## C, bit [2]

Cycle counter reset. The effects of writing to this field are:

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | No action.            |
| 0b1 | Reset PMCCNTRto zero. |

Note

Resetting PMCCNTR does not change the cycle counter overflow field. The value of PMCR.LC is ignored, and bits [63:0] of the cycle counter are reset.

Access to this field is WO/RAZ.

## P, bit [1]

Event counter reset.

| P   | Meaning                                                |
|-----|--------------------------------------------------------|
| 0b0 | No action.                                             |
| 0b1 | Reset all affected event counters PMEVCNTR<n> to zero. |

The event counters affected by this field are:

- All event counters in the first range.
- If any of the following are true, all event counters in the second range:
- EL2 is disabled or not implemented in the current Security state.
- The PE is executing at EL2 or EL3.

Writes to this field do not affect other event counters or the cycle counter PMCCNTR.

For more information about event counter ranges, see MDCR\_EL2.HPMN or HDCR.HPMN.

Note

Resetting the event counters does not change the event counter overflow fields. If FEAT\_PMUv3p5 is implemented, the values of MDCR\_EL2.HLP or HDCR.HLP and PMCR.LP are ignored, and bits [63:0] of all affected event counters are reset.

Access to this field is WO/RAZ.

## E, bit [0]

Enable.

| E   | Meaning                                          |
|-----|--------------------------------------------------|
| 0b0 | Affected counters are disabled and do not count. |
| 0b1 | Affected counters are enabled by PMCNTENSET.     |

The counters affected by this field are:

- The event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN or HDCR.HPMN.
- The cycle counter PMCCNTR.

Other event counters are not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing PMCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' || ↪ → (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPMCR ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPMCR == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPMCR ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPMCR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM ==
```

```
↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMCR; elsif PSTATE.EL == EL3 then R[t] = PMCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' || ↪ → (IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.UEN == '1')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMCR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPMCR ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPMCR == ↪ → '1' then AArch32.TakeHypTrapException(0x03);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCR = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPMCR ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPMCR == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMCR = R[t]; elsif PSTATE.EL == EL3 then PMCR = R[t];
```

## G8.4.10 PMEVCNTR&lt;n&gt;, Performance Monitors Event Count Registers, n = 0 - 30

The PMEVCNTR&lt;n&gt; characteristics are:

## Purpose

Holds event counter n, which counts events, where n is 0 to 30.

## Configuration

AArch32 System register PMEVCNTR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register PMEVCNTR&lt;n&gt;\_EL0[31:0].

AArch32 System register PMEVCNTR&lt;n&gt; bits [31:0] are architecturally mapped to External register PMEVCNTR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMEVCNTR&lt;n&gt; are UNDEFINED.

## Attributes

PMEVCNTR&lt;n&gt; is a 32-bit register.

## Field descriptions

Event counter n

31

0

<!-- image -->

## EVCNT, bits [31:0]

Event counter n. Value of event counter n, where n is the number of this register and is a number from 0 to 30.

If FEAT\_PMUv3p5 is implemented, the event counter is 64 bits and only the least-significant part of the event counter is accessible in AArch32 state:

- Reads from PMEVCNTR&lt;n&gt; return bits [31:0] of the counter.
- Writes to PMEVCNTR&lt;n&gt; update bits [31:0] and leave bits [63:32] unchanged.
- There is no means to access bits [63:32] directly from AArch32 state.
- If the implementation does not support AArch64, bits [63:32] are not required to be implemented.

If FEAT\_PMUv3p5 is not implemented, the event counter is 32 bits.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVCNTR&lt;n&gt;

PMEVCNTR&lt;n&gt; can also be accessed by using PMXEVCNTR with PMSELR.SEL set to n.

If FEAT\_FGT is implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMEVCNTR&lt;n&gt; is as follows:

- If &lt;n&gt; is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then reads and writes of PMEVCNTR&lt;n&gt; are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP .
- Accesses to the register behave as if &lt;n&gt; is an UNKNOWN value less-than-or-equal-to the index of the highest accessible event counter.
- If EL2 is implemented and enabled in the current Security state, and &lt;n&gt; is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMEVCNTR&lt;n&gt; are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.P&lt;n&gt; == 0.

Permitted writes of PMEVCNTR&lt;n&gt; are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.{UEN,ER} == {1,1}.

## Note

In EL0, an access is permitted if it is enabled by PMUSERENR.{ER,EN} or PMUSERENR\_EL0.{UEN,ER,EN}. If EL2 is implemented and enabled in the current Security state, at EL0 and EL1:

- If EL2 is using AArch32, HDCR.HPMN identifies the number of accessible event counters.
- If EL2 is using AArch64, MDCR\_EL2.HPMN identifies the number of accessible event counters.

Otherwise, the number of accessible event counters is the number of implemented event counters. For more information, see HDCR.HPMN and MDCR\_EL2.HPMN.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-30

| coproc   | opc1   | CRn    | CRm          | opc2   |
|----------|--------|--------|--------------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b10 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED;
```

```
elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<ER,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1[m] == '0' then R[t] = Zeros(32); else R[t] = PMEVCNTR[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMEVCNTR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMEVCNTR[m]; elsif PSTATE.EL == EL3 then R[t] = PMEVCNTR[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-30

| coproc   | opc1   | CRn    | CRm          | opc2   |
|----------|--------|--------|--------------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b10 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1[m] == '0' || ↪ → PMUSERENR_EL0.ER == '1') then return; else PMEVCNTR[m] = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMEVCNTR[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMEVCNTR[m] = R[t]; elsif PSTATE.EL == EL3 then PMEVCNTR[m] = R[t];
```

## G8.4.11 PMEVTYPER&lt;n&gt;, Performance Monitors Event Type Registers, n = 0 - 30

The PMEVTYPER&lt;n&gt; characteristics are:

## Purpose

Configures event counter n, where n is 0 to 30.

## Configuration

AArch32 System register PMEVTYPER&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register PMEVTYPER&lt;n&gt;\_EL0[31:0].

AArch32 System register PMEVTYPER&lt;n&gt; bits [31:0] are architecturally mapped to External register PMEVTYPER\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMEVTYPER&lt;n&gt; are UNDEFINED.

## Attributes

PMEVTYPER&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## P, bit [31]

Privileged filtering. Controls counting events in EL1 and, if EL3 is using AArch32, EL3.

| P   | Meaning                                                                |
|-----|------------------------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of events.                   |
| 0b1 | The PE does not count events in EL1 and, if EL3 is using AArch32, EL3. |

If Secure and Non-secure states are implemented, then counting events in Non-secure EL1 is further controlled by PMEVTYPER&lt;n&gt;.NSK.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

User filtering. Controls counting events in EL0.

| U   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of events. |
| 0b1 | The PE does not count events in EL0.                 |

If Secure and Non-secure states are implemented, then counting events in Non-secure EL0 is further controlled by PMEVTYPER&lt;n&gt;.NSU.

If FEAT\_RME is implemented, then counting events in Realm EL0 is further controlled by PMEVTYPER&lt;n&gt;.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting events in Non-secure EL1. If PMEVTYPER&lt;n&gt;.NSK is not equal to PMEVTYPER&lt;n&gt;.P, then the PE does not count events in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of events in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>.P == 1, the PE does not count events in Non-secure EL1. |
| 0b1   | When PMEVTYPER<n>.P == 0, the PE does not count events in Non-secure EL1. When PMEVTYPER<n>.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting events in Non-secure EL0. If PMEVTYPER&lt;n&gt;.NSU is not equal to PMEVTYPER&lt;n&gt;.U, then the PE does not count events in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of events in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>.U == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>.U == 1, the PE does not count events in Non-secure EL0. |
| 0b1   | When PMEVTYPER<n>.U == 0, the PE does not count events in Non-secure EL0. When PMEVTYPER<n>.U == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting events in EL2.

| NSH   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE does not count events in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of events. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting events in Secure EL2 is further controlled by PMEVTYPER&lt;n&gt;.SH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [26]

Reserved, RES0.

## MT, bit [25]

## When FEAT\_MTPMU is implemented or an IMPLEMENTATION DEFINED multi-threaded PMU extension is implemented:

Multithreading.

| MT   | Meaning                                                                          |
|------|----------------------------------------------------------------------------------|
| 0b0  | Count events only on controlling PE.                                             |
| 0b1  | Count events from any PE with the same affinity at level 1 and above as this PE. |

Unless otherwise stated:

- If the event counts PE cycles when a stall condition is true and a second condition is true, then the counter counts Processor cycles when the stall condition is true for all of these PEs, and the second condition is true for any of these PEs.
- If the event counts PE cycles when any other condition is true, then the counter counts Processor cycles when the condition is true for any of these PEs.
- Otherwise, the event counts by the sum of the count across all of these PEs.

For the stall events, the stall condition means the applicable condition described by the STALL, STALL\_FRONTEND, or STALL\_BACKEND event.

The second condition is any condition in addition to this.

For example, for the STALL\_FRONTEND\_L1I event, the stall condition is STALL\_FRONTEND, and the second condition is when there is a demand instruction miss in the first level of instruction cache.

For the STALL, STALL\_FRONTEND, and STALL\_BACKEND events themselves, the second condition is the null TRUE condition.

See 'Multithreaded implementations' and 'Cycle event counting in multithreaded implementations'.

From Armv8.6, the IMPLEMENTATION DEFINED multi-threaded PMU extension is not permitted, meaning if FEAT\_MTPMU is not implemented, this field is RES0. See ID\_DFR1.MTPMU.

This field is ignored by the PE and treated as zero when FEAT\_MTPMU is implemented and disabled.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [24:22]

Reserved, RES0.

## RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting events in Realm EL0. If PMEVTYPER&lt;n&gt;.RLU is not equal to PMEVTYPER&lt;n&gt;.U, then the PE does not count events in Realm EL0. Otherwise, this mechanism has no effect on filtering of events in Realm EL0.

| RLU   | Meaning                                                                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>.U == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>.U == 1, the PE does not count events in Realm EL0. |

| RLU   | Meaning                                                                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | When PMEVTYPER<n>.U == 0, the PE does not count events in Realm EL0. When PMEVTYPER<n>.U == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [20:16]

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

The event number of the event that is counted by event counter PMEVCNTR&lt;n&gt;.

The ranges of event numbers allocated to each type of event are shown in 'Allocation of the PMU event number space'.

If FEAT\_PMUv3p8 is implemented and PMEVTYPER&lt;n&gt;.evtCount is programmed to an event that is reserved or not supported by the PE, no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;.evtCount field is the value written to the field.

Note

Arm recommends this behavior for all implementations of FEAT\_PMUv3.

Otherwise, if PMEVTYPER&lt;n&gt;.evtCount is programmed to an event that is reserved or not supported by the PE, the behavior depends on the value written:

- For the range 0x0000 to 0x003F , no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;.evtCount field is the value written to the field.
- If FEAT\_PMUv3p1 is implemented, for the range 0x4000 to 0x403F , no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;.evtCount field is the value written to the field.
- For other values, it is UNPREDICTABLE what event, if any, is counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;.evtCount field is UNKNOWN.

Note

UNPREDICTABLE means the event must not expose privileged information.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVTYPER&lt;n&gt;

PMEVTYPER&lt;n&gt; can also be accessed by using PMXEVTYPER with PMSELR.SEL set to n.

If FEAT\_FGT is implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMEVTYPER&lt;n&gt; is as follows:

- If &lt;n&gt; is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented and &lt;n&gt; is greater than or equal to the number of accessible event counters, then reads and writes of PMEVTYPER&lt;n&gt; are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP .
- Accesses to the register behave as if &lt;n&gt; is an UNKNOWN value less-than-or-equal-to the index of the highest accessible event counter.
- If EL2 is implemented and enabled in the current Security state, and &lt;n&gt; is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMEVTYPER&lt;n&gt; are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.P&lt;n&gt; == 0.

Permitted writes of PMEVTYPER&lt;n&gt; are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.{UEN,ER} == {1,1}.

Note

In EL0, an access is permitted if it is enabled by PMUSERENR.EN or PMUSERENR\_EL0.{UEN,EN}. If EL2 is implemented and enabled in the current Security state, at EL0 and EL1:

- If EL2 is using AArch32, HDCR.HPMN identifies the number of accessible event counters.
- If EL2 is using AArch64, MDCR\_EL2.HPMN identifies the number of accessible event counters.

Otherwise, the number of accessible event counters is the number of implemented event counters. For more information, see HDCR.HPMN and MDCR\_EL2.HPMN.

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | opc1   | CRn    | CRm          | opc2   |
|----------|--------|--------|--------------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b11 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1[m] == '0' then R[t] = Zeros(32);
```

```
else R[t] = PMEVTYPER[m]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMEVTYPER[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMEVTYPER[m]; elsif PSTATE.EL == EL3 then R[t] = PMEVTYPER[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-30

| coproc   | opc1   | CRn    | CRm          | opc2   |
|----------|--------|--------|--------------|--------|
| 0b1111   | 0b000  | 0b1110 | 0b11 :m[4:3] | m[2:0] |

```
integer m = UInt(CRm<1:0>:opc2<2:0>); if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif m >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED;
```

```
elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1[m] == '0' || ↪ → PMUSERENR_EL0.ER == '1') then return; else PMEVTYPER[m] = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && m >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMEVTYPER[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMEVTYPER[m] = R[t]; elsif PSTATE.EL == EL3 then PMEVTYPER[m] = R[t];
```

## G8.4.12 PMINTENCLR, Performance Monitors Interrupt Enable Clear register

The PMINTENCLR characteristics are:

## Purpose

Allows software to disable the generation of interrupt requests on overflows from the following counters:

- The cycle counter PMCCNTR.
- The event counters PMEVCNTR&lt;n&gt;.

Reading from this register shows which overflow interrupt requests are enabled.

## Configuration

AArch32 System register PMINTENCLR bits [31:0] are architecturally mapped to AArch32 System register PMINTENSET[31:0].

AArch32 System register PMINTENCLR bits [31:0] are architecturally mapped to AArch64 System register PMINTENCLR\_EL1[31:0].

AArch32 System register PMINTENCLR bits [31:0] are architecturally mapped to AArch64 System register PMINTENSET\_EL1[31:0].

AArch32 System register PMINTENCLR bits [31:0] are architecturally mapped to External register PMINTENCLR\_EL1[31:0].

AArch32 System register PMINTENCLR bits [31:0] are architecturally mapped to External register PMINTENSET\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMINTENCLR are UNDEFINED.

## Attributes

PMINTENCLR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------------------------------------------------|

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR enable status.

| C   | Meaning                                                                              |
|-----|--------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTRdisabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTRenabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.

- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt; disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;enable status.

| P<m>   | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow ofPMEVCNTR<m> disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow ofPMEVCNTR<m> enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing PMINTENCLR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMINTENCLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMINTENCLR; elsif PSTATE.EL == EL3 then R[t] = PMINTENCLR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMINTENCLR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMINTENCLR = R[t]; elsif PSTATE.EL == EL3 then PMINTENCLR = R[t];
```

## G8.4.13 PMINTENSET, Performance Monitors Interrupt Enable Set register

The PMINTENSET characteristics are:

## Purpose

Allows software to enable the generation of interrupt requests on overflows from the following counters:

- The cycle counter PMCCNTR.
- The event counters PMEVCNTR&lt;n&gt;.

Reading from this register shows which overflow interrupt requests are enabled.

## Configuration

AArch32 System register PMINTENSET bits [31:0] are architecturally mapped to AArch32 System register PMINTENCLR[31:0].

AArch32 System register PMINTENSET bits [31:0] are architecturally mapped to AArch64 System register PMINTENCLR\_EL1[31:0].

AArch32 System register PMINTENSET bits [31:0] are architecturally mapped to AArch64 System register PMINTENSET\_EL1[31:0].

AArch32 System register PMINTENSET bits [31:0] are architecturally mapped to External register PMINTENCLR\_EL1[31:0].

AArch32 System register PMINTENSET bits [31:0] are architecturally mapped to External register PMINTENSET\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMINTENSET are UNDEFINED.

## Attributes

PMINTENSET is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------------------------------------------------|

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR enable status.

| C   | Meaning                                                                              |
|-----|--------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTRdisabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTRenabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.

- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt; enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;enable status.

| P<m>   | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow ofPMEVCNTR<m> disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow ofPMEVCNTR<m> enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing PMINTENSET

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMINTENSET; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMINTENSET; elsif PSTATE.EL == EL3 then R[t] = PMINTENSET;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMINTENSET = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMINTENSET = R[t]; elsif PSTATE.EL == EL3 then PMINTENSET = R[t];
```

## G8.4.14 PMOVSR, Performance Monitors Overflow Flag Status Register

The PMOVSR characteristics are:

## Purpose

Allows software to clear the unsigned overflow flags for the following counters to 0:

- The cycle counter PMCCNTR.
- The event counters PMEVCNTR&lt;n&gt;.

Reading from this register shows the current unsigned overflow flag values.

## Configuration

AArch32 System register PMOVSR bits [31:0] are architecturally mapped to AArch32 System register PMOVSSET[31:0].

AArch32 System register PMOVSR bits [31:0] are architecturally mapped to AArch64 System register PMOVSCLR\_EL0[31:0].

AArch32 System register PMOVSR bits [31:0] are architecturally mapped to AArch64 System register PMOVSSET\_EL0[31:0].

AArch32 System register PMOVSR bits [31:0] are architecturally mapped to External register PMOVSCLR\_EL0[31:0].

AArch32 System register PMOVSR bits [31:0] are architecturally mapped to External register PMOVSSET\_EL0[31:0].

AArch32 System register PMOVSR bits [31:0] are architecturally mapped to External register PMOVS[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMOVSR are UNDEFINED.

## Attributes

PMOVSRis a 32-bit register.

## Field descriptions

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1   |
|------|------------------------------------------------------------------------------------|

## C, bit [31]

Unsigned overflow flag for PMCCNTR clear. On writes, allows software to clear the unsigned overflow flag for PMCCNTRto 0. On reads, returns the unsigned overflow flag for PMCCNTR overflow status.

| C   | Meaning                    |
|-----|----------------------------|
| 0b0 | PMCCNTRhas not overflowed. |
| 0b1 | PMCCNTRhas overflowed.     |

PMCR.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR[31:0] or unsigned overflow of PMCCNTR[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt; clear. On writes, allows software to clear the unsigned overflow flag for PMEVCNTR&lt;m&gt; to 0. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt; overflow status.

| P<m>   | Meaning                        |
|--------|--------------------------------|
| 0b0    | PMEVCNTR<m>has not overflowed. |
| 0b1    | PMEVCNTR<m>has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP, HDCR.HLP, and PMCR.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;[63:0].

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
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1C.

## Accessing PMOVSR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMOVS == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMOVSR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMOVSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMOVSR; elsif PSTATE.EL == EL3 then R[t] = PMOVSR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED;
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMOVS == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMOVSR = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMOVSR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMOVSR = R[t]; elsif PSTATE.EL == EL3 then PMOVSR = R[t];
```

## G8.4.15 PMOVSSET, Performance Monitors Overflow Flag Status Set register

The PMOVSSET characteristics are:

## Purpose

Allows software to set the unsigned overflow flags for the following counters to 1:

- The cycle counter PMCCNTR.
- The event counters PMEVCNTR&lt;n&gt;.

Reading from this register shows the current unsigned overflow flag values.

## Configuration

AArch32 System register PMOVSSET bits [31:0] are architecturally mapped to AArch32 System register PMOVSR[31:0].

AArch32 System register PMOVSSET bits [31:0] are architecturally mapped to AArch64 System register PMOVSSET\_EL0[31:0].

AArch32 System register PMOVSSET bits [31:0] are architecturally mapped to AArch64 System register PMOVSCLR\_EL0[31:0].

AArch32 System register PMOVSSET bits [31:0] are architecturally mapped to External register PMOVSSET\_EL0[31:0].

AArch32 System register PMOVSSET bits [31:0] are architecturally mapped to External register PMOVSCLR\_EL0[31:0].

AArch32 System register PMOVSSET bits [31:0] are architecturally mapped to External register PMOVS[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMOVSSET are UNDEFINED.

## Attributes

PMOVSSET is a 32-bit register.

## Field descriptions

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1   |
|------|------------------------------------------------------------------------------------|

## C, bit [31]

Unsigned overflow flag for PMCCNTR set. On writes, allows software to set the unsigned overflow flag for PMCCNTRto 1. On reads, returns the unsigned overflow flag for PMCCNTR overflow status.

| C   | Meaning                    |
|-----|----------------------------|
| 0b0 | PMCCNTRhas not overflowed. |
| 0b1 | PMCCNTRhas overflowed.     |

PMCR.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR[31:0] or unsigned overflow of PMCCNTR[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.C == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.CR] == '11'
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt; set. On writes, allows software to set the unsigned overflow flag for PMEVCNTR&lt;m&gt;to 1. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt; overflow status.

| P<m>   | Meaning                        |
|--------|--------------------------------|
| 0b0    | PMEVCNTR<m>has not overflowed. |
| 0b1    | PMEVCNTR<m>has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP, HDCR.HLP, and PMCR.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;[63:0].

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
- EL1 is using AArch64
- PMUSERENR\_EL0.UEN == '1'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Access to this field is RO if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.ER] == '11'
- Otherwise, access to this field is W1S.

## Accessing PMOVSSET

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMOVS == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMOVSSET; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMOVSSET; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMOVSSET; elsif PSTATE.EL == EL3 then R[t] = PMOVSSET;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b011  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED;
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMOVS == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMOVSSET = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMOVSSET = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMOVSSET = R[t]; elsif PSTATE.EL == EL3 then PMOVSSET = R[t];
```

## G8.4.16 PMSELR, Performance Monitors Event Counter Selection Register

The PMSELR characteristics are:

## Purpose

Selects the current event counter PMEVCNTR&lt;n&gt; or the cycle counter PMCCNTR.

Used in conjunction with PMXEVTYPER to determine the event that increments a selected counter, and the modes and states in which the selected counter increments.

Used in conjunction with PMXEVCNTR to determine the value of a selected counter.

## Configuration

AArch32 System register PMSELR bits [31:0] are architecturally mapped to AArch64 System register PMSELR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMSELR are UNDEFINED.

## Attributes

PMSELR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 5 4   |
|------|-------|
|      | SEL   |

## Bits [31:5]

Reserved, RES0.

## SEL, bits [4:0]

Event counter select. Selects the counter accessed by subsequent accesses to PMXEVTYPER and PMXEVCNTR.

| SEL                | Meaning                                                                                                                                                                      |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00000 .. 0b11110 | Select event counter PMEVCNTR<n>, where n is the value of this field: • MRC and MCR of PMXEVTYPERaccess PMEVTYPER<n>. • MRC and MCR of PMXEVCNTRaccess PMEVCNTR<n>.          |
| 0b11111            | Select the cycle counter, PMCCNTR: • MRC and MCR of PMXEVTYPERaccess PMCCFILTR. • MRC and MCR of PMXEVCNTRareCONSTRAINED UNPREDICTABLE. For more information, see PMXEVCNTR. |

For more information about the results of accesses to the event counters, including when PMSELR.SEL is set to the index of an unimplemented or inaccessible event counter, see PMXEVTYPER and PMXEVCNTR.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMSELR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<ER,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMSELR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMSELR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMSELR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMSELR; elsif PSTATE.EL == EL3 then R[t] = PMSELR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b101  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<ER,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else
```

```
UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMSELR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMSELR = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMSELR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMSELR = R[t]; elsif PSTATE.EL == EL3 then PMSELR = R[t];
```

## G8.4.17 PMSWINC, Performance Monitors Software Increment register

The PMSWINC characteristics are:

## Purpose

Increments a counter that is configured to count the Software increment event, event 0x00 . For more information, see 'SW\_INCR'.

## Configuration

AArch32 System register PMSWINC bits [31:0] are architecturally mapped to AArch64 System register PMSWINC\_EL0[31:0].

When FEAT\_PMUv3p9 is not implemented, AArch32 System register PMSWINC bits [31:0] are architecturally mapped to External register PMSWINC\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMSWINC are UNDEFINED.

## Attributes

PMSWINCis a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES0.

P&lt;m&gt; , bits [m], for m = 30 to 0

Software increment.

| P<m>   | Meaning                                                                                |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | Write is ignored.                                                                      |
| 0b1    | Increment PMEVCNTR<m>, if PMEVCNTR<m>is configured to count software increment events. |

Accessing this field has the following behavior:

- When m &gt;= GetNumEventCountersAccessible(), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3p9 is implemented
- PSTATE.EL == EL0
- EL1 is using AArch64
- [PMUSERENR\_EL0.UEN, PMUSERENR\_EL0.SW] == '10'
- PMUACR\_EL1.P&lt;m&gt; == '0'
- Otherwise, access to this field is WO/RAZ.

RES0

## Accessing PMSWINC

Accesses to this register use the following encodings in the System register encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1100 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,SW,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<SW,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<SW,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMSWINC_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMSWINC = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMSWINC = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMSWINC = R[t]; elsif PSTATE.EL == EL3 then PMSWINC = R[t];
```

## G8.4.18 PMUSERENR, Performance Monitors User Enable Register

The PMUSERENR characteristics are:

## Purpose

Enables or disables EL0 access to the Performance Monitors.

## Configuration

AArch32 System register PMUSERENR bits [31:0] are architecturally mapped to AArch64 System register PMUSERENR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMUSERENR are UNDEFINED.

## Attributes

PMUSERENRis a 32-bit register.

## Field descriptions

| 31   | 7 6 5 4 3 2 1 0   |
|------|-------------------|

## Bits [31:7]

Reserved, RES0.

## TID, bit [6]

## When FEAT\_PMUv3p9 is implemented:

Trap ID registers. Traps EL0 read access to common event identification registers.

| TID   | Meaning                                                  |
|-------|----------------------------------------------------------|
| 0b0   | Accesses to PMCEID<n> are not trapped by this mechanism. |
| 0b1   | EL0 read accesses to PMCEID<n> are trapped.              |

The register accesses affected by this control are:

- MRC reads of PMCEID0, PMCEID1, PMCEID2, and PMCEID3.

When trapped, reads are UNDEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [5:4]

Reserved, RES0.

## ER, bit [3]

Event counters Read enable.

When PMUSERENR.EN is 0, PMUSERENR.ER enables EL0 reads of the event counters and EL0 reads and writes of the select register.

| ER   | Meaning                                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 reads of the event counters and EL0 reads and writes of the select register are disabled, unless enabled by PMUSERENR.EN.   |
| 0b1  | EL0 reads of the event counters and EL0 reads and writes of the select register are enabled, unless trapped by another control. |

The register accesses affected by this control are:

- MRC reads of PMEVCNTR&lt;n&gt; and PMXEVCNTR.
- MRC and MCR accesses to PMSELR.

When disabled, reads and writes are UNDEFINED.

This field is ignored by the PE when PMUSERENR.EN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CR, bit [2]

Cycle counter Read enable.

When PMUSERENR.EN is 0, PMUSERENR.CR enables EL0 reads of the cycle counter.

| CR   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | EL0 reads of the cycle counter are disabled, unless enabled by PMUSERENR.EN.   |
| 0b1  | EL0 reads of the cycle counter are enabled, unless trapped by another control. |

The register accesses affected by this control are:

- MRC reads of PMCCNTR.
- MRRC reads of PMCCNTR.

When disabled, reads are UNDEFINED.

This field is ignored by the PE when PMUSERENR.EN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SW, bit [1]

Software increment register Write enable.

When PMUSERENR.EN is 0, PMUSERENR.SW enables EL0 writes to the Software increment register.

| SW   | Meaning                                                                                       |
|------|-----------------------------------------------------------------------------------------------|
| 0b0  | EL0 writes to the Software increment register are disabled, unless enabled by PMUSERENR.EN.   |
| 0b1  | EL0 writes to the Software increment register are enabled, unless trapped by another control. |

The register accesses affected by this control are:

- MCR writes to PMSWINC.

When disabled, writes are UNDEFINED.

This field is ignored by the PE when PMUSERENR.EN == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EN, bit [0]

Enable. Enables EL0 read/write access to PMU registers.

| EN   | Meaning                                                                                                |
|------|--------------------------------------------------------------------------------------------------------|
| 0b0  | EL0 accesses to the specified PMUSystem registers are trapped, unless enabled by PMUSERENR.{ER,CR,SW}. |
| 0b1  | EL0 accesses to the specified PMUSystem registers are enabled, unless trapped by another control.      |

The register accesses affected by this control are:

- MRC or MCR accesses to PMCCFILTR, PMCCNTR, PMCNTENCLR, PMCNTENSET, PMCR, PMEVCNTR&lt;n&gt;, PMEVTYPER&lt;n&gt;, PMOVSR, PMOVSSET, PMSELR, PMXEVCNTR, and PMXEVTYPER.
- MRC reads of the following registers:
- PMCEID0 and PMCEID1.
- If FEAT\_PMUv3p1 is implemented, PMCEID2 and PMCEID3.
- MCR writes to PMSWINC.
- MRRC or MCRR accesses to PMCCNTR.

When trapped, reads and writes are UNDEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMUSERENR

When FEAT\_PMUv3p9 is implemented and EL1 is using AArch64, PMUSERENR\_EL0 contains additional controls that affect the behavior of this register.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMUSERENR_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMUSERENR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMUSERENR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else
```

```
R[t] = PMUSERENR; elsif PSTATE.EL == EL3 then R[t] = PMUSERENR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b000  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMUSERENR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMUSERENR = R[t]; elsif PSTATE.EL == EL3 then PMUSERENR = R[t];
```

## G8.4.19 PMXEVCNTR, Performance Monitors Selected Event Count Register

The PMXEVCNTR characteristics are:

## Purpose

Reads or writes the value of the selected event counter, PMEVCNTR&lt;n&gt;. PMSELR.SEL determines which event counter is selected.

## Configuration

AArch32 System register PMXEVCNTR bits [31:0] are architecturally mapped to AArch64 System register PMXEVCNTR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMXEVCNTR are UNDEFINED.

## Attributes

PMXEVCNTRis a 32-bit register.

## Field descriptions

PMEVCNTR&lt;n&gt;

31

0

<!-- image -->

## PMEVCNTR&lt;n&gt;, bits [31:0]

Value of the selected event counter, PMEVCNTR&lt;n&gt;, where n is the value stored in PMSELR.SEL.

If FEAT\_PMUv3p5 is implemented, the event counter is 64 bits and only the least-significant part of the event counter is accessible in AArch32 state:

- Reads from PMXEVCNTR return bits [31:0] of the counter.
- Writes to PMXEVCNTR update bits [31:0] and leave bits [63:32] unchanged.
- There is no means to access bits [63:32] directly from AArch32 state.
- If the implementation does not support AArch64, bits [63:32] are not required to be implemented.

If FEAT\_PMUv3p5 is not implemented, the event counter is 32 bits.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMXEVCNTR

If FEAT\_FGT is implemented and PMSELR.SEL is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMXEVCNTR is as follows:

- If PMSELR.SEL is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented and PMSELR.SEL is greater than or equal to the number of accessible event counters, then reads and writes of PMXEVCNTR are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP
- Accesses to the register behave as if PMSELR.SEL has an UNKNOWN value less than the number of event counters accessible at the current Exception level and Security state.

- If EL2 is implemented and enabled in the current Security state, and PMSELR.SEL is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMXEVCNTR are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.UEN == 1.
- PMUACR\_EL1.P&lt;UInt(PMSELR.SEL)&gt; == 0.

Permitted writes of PMXEVCNTR are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.{UEN,ER} == {1,1}.

Note

In EL0, an access is permitted if it is enabled by PMUSERENR.{ER,EN} or PMUSERENR\_EL0.{UEN,ER,EN}. If EL2 is implemented and enabled in the current Security state, at EL0 and EL1:

- If EL2 is using AArch32, HDCR.HPMN identifies the number of accessible event counters.
- If EL2 is using AArch64, MDCR\_EL2.HPMN identifies the number of accessible event counters.

Otherwise, the number of accessible event counters is determined by the Effective value of PMCCR.EPMN. For more information, see HDCR.HPMN, MDCR\_EL2.HPMN and PMCCR.EPMN.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1101 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif UInt(PMSELR.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && ↪ → ((IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<UEN,ER,EN> == '000') || ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) && PMUSERENR_EL0.<ER,EN> == '00')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.<ER,EN> == '00' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && PMUACR_EL1[UInt(PMSELR.SEL)] == '0' ↪ → then R[t] = Zeros(32); else R[t] = PMEVCNTR[UInt(PMSELR.SEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMEVCNTR[UInt(PMSELR.SEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMEVCNTR[UInt(PMSELR.SEL)]; elsif PSTATE.EL == EL3 then R[t] = PMEVCNTR[UInt(PMSELR.SEL)];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1101 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif UInt(PMSELR.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMEVCNTRn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && (PMUACR_EL1[UInt(PMSELR.SEL)] == '0' ↪ → || PMUSERENR_EL0.ER == '1') then return; else PMEVCNTR[UInt(PMSELR.SEL)] = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMEVCNTR[UInt(PMSELR.SEL)] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM ==
```

```
↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else PMEVCNTR[UInt(PMSELR.SEL)] = R[t]; elsif PSTATE.EL == EL3 then PMEVCNTR[UInt(PMSELR.SEL)] = R[t];
```

## G8.4.20 PMXEVTYPER, Performance Monitors Selected Event Type Register

The PMXEVTYPER characteristics are:

## Purpose

When PMSELR.SEL selects an event counter, this accesses a PMEVTYPER&lt;n&gt; register. When PMSELR.SEL selects the cycle counter, this accesses PMCCFILTR.

## Configuration

AArch32 System register PMXEVTYPER bits [31:0] are architecturally mapped to AArch64 System register PMXEVTYPER\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented and FEAT\_PMUv3 is implemented. Otherwise, direct accesses to PMXEVTYPER are UNDEFINED.

## Attributes

PMXEVTYPERis a 32-bit register.

## Field descriptions

```
Event type register or PMCCFILTR 31 0
```

## ETR, bits [31:0]

Event type register or PMCCFILTR.

When PMSELR.SEL == 31, this register accesses PMCCFILTR.

Otherwise, this register accesses PMEVTYPER&lt;n&gt; where n is the value in PMSELR.SEL.

## Accessing PMXEVTYPER

If FEAT\_FGT is implemented, and PMSELR.SEL is not 31 and is greater than or equal to the number of accessible event counters, then the behavior of permitted reads and writes of PMXEVTYPER is as follows:

- If PMSELR.SEL is greater than or equal to the Effective value of PMCCR.EPMN, the access is UNDEFINED.
- Otherwise, the access is trapped to EL2.

If FEAT\_FGT is not implemented, and PMSELR.SEL is not 31 and is greater than or equal to the number of accessible event counters, then reads and writes of PMXEVTYPER are CONSTRAINED UNPREDICTABLE, and the following behaviors are permitted:

- Accesses to the register are UNDEFINED.
- Accesses to the register behave as RAZ/WI.
- Accesses to the register execute as a NOP
- Accesses to the register behave as if PMSELR.SEL has an UNKNOWN value less than the number of event counters accessible at the current Exception level and Security state.
- Accesses to the register behave as if PMSELR.SEL is 31.
- If EL2 is implemented and enabled in the current Security state, and PMSELR.SEL is less than the number of implemented event counters, accesses from EL1 or permitted accesses from EL0 are trapped to EL2.

Permitted reads and writes of PMXEVTYPER are RAZ/WI if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.

- PMUSERENR\_EL0.UEN == 1.
- Any of the following are true:
- PMSELR.SEL != 31 and PMUACR\_EL1.P&lt;UInt(PMSELR.SEL)&gt; == 0.
- PMSELR.SEL == 31 and PMUACR\_EL1.C == 0.

Permitted writes of PMXEVTYPER are ignored if all of the following are true:

- FEAT\_PMUv3p9 is implemented.
- PSTATE.EL == EL0.
- EL1 is using AArch64.
- PMUSERENR\_EL0.UEN == 1.
- Any of the following are true:
- PMSELR.SEL != 31 and PMUSERENR\_EL0.ER == 1.
- PMSELR.SEL == 31 and PMUSERENR\_EL0.CR == 1.

## Note

In EL0, an access is permitted if it is enabled by PMUSERENR.EN or PMUSERENR\_EL0.{UEN,EN}. If EL2 is implemented and enabled in the current Security state, at EL0 and EL1:

- If EL2 is using AArch32, HDCR.HPMN identifies the number of accessible event counters.
- If EL2 is using AArch64, MDCR\_EL2.HPMN identifies the number of accessible event counters.

Otherwise, the number of accessible event counters is determined by the Effective value of PMCCR.EPMN. For more information, see HDCR.HPMN, MDCR\_EL2.HPMN and PMCCR.EPMN.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1101 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif UInt(PMSELR.SEL) != 31 && UInt(PMSELR.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else
```

```
UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGRTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) != 31 && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() ↪ → then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && ((UInt(PMSELR.SEL) != 31 && ↪ → PMUACR_EL1[UInt(PMSELR.SEL)] == '0') || (UInt(PMSELR.SEL) == 31 && PMUACR_EL1.C == '0')) ↪ → then R[t] = Zeros(32); elsif UInt(PMSELR.SEL) == 31 then R[t] = PMCCFILTR; else R[t] = PMEVTYPER[UInt(PMSELR.SEL)]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) != 31 && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() ↪ → then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM ==
```

```
↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if UInt(PMSELR.SEL) == 31 then R[t] = PMCCFILTR; else R[t] = PMEVTYPER[UInt(PMSELR.SEL)]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if UInt(PMSELR.SEL) == 31 then R[t] = PMCCFILTR; else R[t] = PMEVTYPER[UInt(PMSELR.SEL)]; elsif PSTATE.EL == EL3 then if UInt(PMSELR.SEL) == 31 then R[t] = PMCCFILTR; else R[t] = PMEVTYPER[UInt(PMSELR.SEL)];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1101 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_PMUv3)) then UNDEFINED; elsif UInt(PMSELR.SEL) != 31 && UInt(PMSELR.SEL) >= GetNumEventCountersSelfHosted() then if IsFeatureImplemented(FEAT_FGT) then UNDEFINED; else ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && (PMUSERENR_EL0.EN == '0' && ↪ → (!IsFeatureImplemented(FEAT_PMUv3p9) || PMUSERENR_EL0.UEN == '0')) then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && PMUSERENR.EN == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then
```

```
AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T9 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HDFGWTR_EL2.PMEVTYPERn_EL0 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && MDCR_EL2.TPM ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) != 31 && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() ↪ → then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if IsFeatureImplemented(FEAT_PMUv3p9) && IsFeatureImplemented(FEAT_AA64EL1) && ↪ → !ELUsingAArch32(EL2) && PMUSERENR_EL0.UEN == '1' && ((UInt(PMSELR.SEL) != 31 && ↪ → (PMUACR_EL1[UInt(PMSELR.SEL)] == '0' || PMUSERENR_EL0.ER == '1')) || (UInt(PMSELR.SEL) == ↪ → 31 && (PMUACR_EL1.C == '0' || PMUSERENR_EL0.CR == '1'))) then return; elsif UInt(PMSELR.SEL) == 31 then PMCCFILTR = R[t]; else PMEVTYPER[UInt(PMSELR.SEL)] = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && UInt(PMSELR.SEL) != 31 && UInt(PMSELR.SEL) >= GetNumEventCountersAccessible() ↪ → then if !IsFeatureImplemented(FEAT_FGT) then ConstrainUnpredictableProcedure(Unpredictable_PMUEVENTCOUNTER); elsif IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then AArch32.TakeHypTrapException(0x03); else
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if UInt(PMSELR.SEL) == 31 then PMCCFILTR = R[t]; else PMEVTYPER[UInt(PMSELR.SEL)] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else if UInt(PMSELR.SEL) == 31 then PMCCFILTR = R[t]; else PMEVTYPER[UInt(PMSELR.SEL)] = R[t]; elsif PSTATE.EL == EL3 then if UInt(PMSELR.SEL) == 31 then PMCCFILTR = R[t]; else PMEVTYPER[UInt(PMSELR.SEL)] = R[t];
```