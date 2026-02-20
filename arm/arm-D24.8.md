## D24.8 Branch Record Buffer Extension registers

This section lists the Branch Record Buffer registers in AArch64.

## D24.8.1 BRBCR\_EL1, Branch Record Buffer Control Register (EL1)

The BRBCR\_EL1 characteristics are:

## Purpose

Controls the Branch Record Buffer.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBCR\_EL1 are UNDEFINED.

## Attributes

BRBCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## EXCEPTION, bit [23]

Enable the recording of entry to EL1 via an exception.

| EXCEPTION   | Meaning                                                                   |
|-------------|---------------------------------------------------------------------------|
| 0b0         | Disable the recording of Branch records for exceptions when taken to EL1. |
| 0b1         | Enable the recording of Branch records for exceptions when taken to EL1.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## ERTN, bit [22]

Allow the recording Branch records for exception return instructions from EL1.

| ERTN   | Meaning                                                                          |
|--------|----------------------------------------------------------------------------------|
| 0b0    | Disable the recording Branch records for exception return instructions from EL1. |
| 0b1    | Enable the recording Branch records for exception return instructions from EL1.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Bits [21:10]

Reserved, RES0.

## FZPSS, bit [9]

## When FEAT\_PMUv3\_SS is implemented:

Freeze BRBE on PMU Snapshot.

| FZPSS   | Meaning                                                                                                                           |
|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Branch recording is not affected by this control.                                                                                 |
| 0b1     | If either EL2 is not implemented or BRBCR_EL2.FZPSS is 1, then a BRBE freeze event occurs when a successful Capture event occurs. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FZP, bit [8]

## When FEAT\_PMUv3 is implemented:

Freeze BRBE on PMU overflow.

| FZP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Branch recording is not affected by this control.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 0b1   | ABRBEfreeze event occurs when the PE is in a Non-prohibited region, BRBFCR_EL1.PAUSED is 0, and any of the following applies: • For any event counter PMEVCNTR<m>_EL0 in the first range, PMOVSCLR_EL0[m] is 1, and either FEAT_SEBEP is not implemented or PMEVTYPER<m>_EL0.SYNC is 0. • FEAT_PMUv3_ICNTR is implemented, PMOVSCLR_EL0.F0 is 1, and either FEAT_SEBEP is not implemented or PMICFILTR_EL0.SYNC is 0. For more information about event counter ranges, see MDCR_EL2.HPMN. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control.

| TS   | Meaning                                                                                                                                                                                                                                                                                                                                                                | Applies when            |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b01 | Virtual timestamp. The BRBE recorded timestamp is the physical counter value, minus the value of CNTVOFF_EL2.                                                                                                                                                                                                                                                          |                         |
| 0b10 | Guest physical timestamp. The BRBE recorded timestamp is the physical counter value minus a physical offset. If any of the following are true, the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • EL3 is implemented and SCR_EL3.ECVEn == 0. • EL2 is implemented and CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |
| 0b11 | Physical timestamp. The BRBE recorded timestamp is the physical counter value.                                                                                                                                                                                                                                                                                         |                         |

All other values are reserved.

This field is ignored by the PE when EL2 is implemented and BRBCR\_EL2.TS != 0b00 .

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## MPRED, bit [4]

Mask the recording of mispredicts.

| MPRED   | Meaning                                          |
|---------|--------------------------------------------------|
| 0b0     | Disable the recording of mispredict information. |
| 0b1     | Allow the recording of mispredict information.   |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.

- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## CC, bit [3]

Enable the recording of cycle count information.

| CC   | Meaning                                           |
|------|---------------------------------------------------|
| 0b0  | Disable the recording of cycle count information. |
| 0b1  | Allow the recording of cycle count information.   |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Bit [2]

Reserved, RES0.

## E1BRE, bit [1]

EL1 Branch recording enable.

| E1BRE   | Meaning                             |
|---------|-------------------------------------|
| 0b0     | Branch recording prohibited at EL1. |
| 0b1     | Branch recording enabled at EL1.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0BRE, bit [0]

EL0 Branch recording enable.

| E0BRE   | Meaning                             |
|---------|-------------------------------------|
| 0b0     | Branch recording prohibited at EL0. |
| 0b1     | Branch recording enabled at EL0.    |

This field is ignored by the PE when all of the following are true:

- HCR\_EL2.TGE == 1.
- EL2 is implemented and enabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing BRBCR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name BRBCR\_EL1 or BRBCR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBCTL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8E0]; else X[t, 64] = BRBCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = BRBCR_EL2; else X[t, 64] = BRBCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBCR_EL1;
```

MSR BRBCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBCTL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8E0] = X[t, 64]; else BRBCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then BRBCR_EL2 = X[t, 64]; else BRBCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, BRBCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b101 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x8E0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = BRBCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR BRBCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b101 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x8E0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

```
if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then BRBCR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.8.2 BRBCR\_EL2, Branch Record Buffer Control Register (EL2)

The BRBCR\_EL2 characteristics are:

## Purpose

Controls the Branch Record Buffer.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBCR\_EL2 are UNDEFINED.

## Attributes

BRBCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## EXCEPTION, bit [23]

Enable the recording of entry to EL2 via an exception.

| EXCEPTION   | Meaning                                                                   |
|-------------|---------------------------------------------------------------------------|
| 0b0         | Disable the recording of Branch records for exceptions when taken to EL2. |
| 0b1         | Enable the recording of Branch records for exceptions when taken to EL2.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## ERTN, bit [22]

Allow the recording Branch records for exception return instructions from EL2.

| ERTN   | Meaning                                                                          |
|--------|----------------------------------------------------------------------------------|
| 0b0    | Disable the recording Branch records for exception return instructions from EL2. |
| 0b1    | Enable the recording Branch records for exception return instructions from EL2.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Bits [21:10]

Reserved, RES0.

## FZPSS, bit [9]

## When FEAT\_PMUv3\_SS is implemented:

Freeze BRBE on PMU Snapshot.

| FZPSS   | Meaning                                                                             |
|---------|-------------------------------------------------------------------------------------|
| 0b0     | Branch recording is not affected by this control.                                   |
| 0b1     | If BRBCR_EL1.FZPSS is 1, then a BRBE freeze event occurs when a PMUsnapshot occurs. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FZP, bit [8]

## When FEAT\_PMUv3 is implemented:

Freeze BRBE on PMU overflow.

| FZP   | Meaning                                                                                                                                                                                                                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Branch recording is not affected by this control.                                                                                                                                                                                                                                                                                                       |
| 0b1   | ABRBEfreeze event occurs when the PE is in a Non-prohibited region, BRBFCR_EL1.PAUSED is 0, and all the following are true for any event counter PMEVCNTR<m>_EL0 in the second range: • PMOVSCLR_EL0[m] is 1. • Either FEAT_SEBEP is not implemented or PMEVTYPER<m>_EL0.SYNC is 0. For more information about event counter ranges, see MDCR_EL2.HPMN. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control.

| TS   | Meaning                                                                                                                                                                                                                                                                                                                                                                | Applies when            |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b00 | Timestamp controlled by BRBCR_EL1.TS.                                                                                                                                                                                                                                                                                                                                  |                         |
| 0b01 | Virtual timestamp. The BRBE recorded timestamp is the physical counter value, minus the value of CNTVOFF_EL2.                                                                                                                                                                                                                                                          |                         |
| 0b10 | Guest physical timestamp. The BRBE recorded timestamp is the physical counter value minus a physical offset. If any of the following are true, the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • EL3 is implemented and SCR_EL3.ECVEn == 0. • EL2 is implemented and CNTHCTL_EL2.ECV == 0. • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |
| 0b11 | Physical timestamp. The BRBE recorded timestamp is the physical counter value.                                                                                                                                                                                                                                                                                         |                         |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## MPRED, bit [4]

Mask the recording of mispredicts.

| MPRED   | Meaning                                          |
|---------|--------------------------------------------------|
| 0b0     | Disable the recording of mispredict information. |
| 0b1     | Allow the recording of mispredict information.   |

If EL2 is not implemented, then the Effective value of this field is 1, other than for a direct read of the register.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.

- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## CC, bit [3]

Enable the recording of cycle count information.

| CC   | Meaning                                           |
|------|---------------------------------------------------|
| 0b0  | Disable the recording of cycle count information. |
| 0b1  | Allow the recording of cycle count information.   |

If EL2 is not implemented, then the Effective value of this field is 1, other than for a direct read of the register.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Bit [2]

Reserved, RES0.

## E2BRE, bit [1]

EL2 Branch recording enable.

| E2BRE   | Meaning                             |
|---------|-------------------------------------|
| 0b0     | Branch recording prohibited at EL2. |
| 0b1     | Branch recording enabled at EL2.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0HBRE, bit [0]

EL0 Branch recording enable.

| E0HBRE   | Meaning                                                   |
|----------|-----------------------------------------------------------|
| 0b0      | Branch recording prohibited at EL0 when HCR_EL2.TGE == 1. |
| 0b1      | Branch recording enabled at EL0 when HCR_EL2.TGE == 1.    |

This field is ignored by the PE when any of the following are true:

- HCR\_EL2.TGE == 0.
- EL2 is disabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing BRBCR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name BRBCR\_EL2 or BRBCR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBCTL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8E0]; else X[t, 64] = BRBCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = BRBCR_EL2; else X[t, 64] = BRBCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBCR_EL1;
```

MRS &lt;Xt&gt;, BRBCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b100 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = BRBCR_EL2;
```

MSR BRBCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBCTL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8E0] = X[t, 64]; else BRBCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then BRBCR_EL2 = X[t, 64]; else BRBCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBCR_EL1 = X[t, 64];
```

MSR BRBCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b100 | 0b1001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else
```

AArch64.SystemAccessTrap(EL3, 0x18);

```
else = X[t, 64];
```

<!-- formula-not-decoded -->

## D24.8.3 BRBFCR\_EL1, Branch Record Buffer Function Control Register

The BRBFCR\_EL1 characteristics are:

## Purpose

Functional controls for the Branch Record Buffer.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBFCR\_EL1 are UNDEFINED.

## Attributes

BRBFCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:30]

Reserved, RES0.

## BANK, bits [29:28]

Branch record buffer bank access control.

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:23]

Reserved, RES0.

## CONDDIR, bit [22]

Match on conditional direct branch instructions.

| BANK   | Meaning                         |
|--------|---------------------------------|
| 0b00   | Select branch records 0 to 31.  |
| 0b01   | Select branch records 32 to 63. |

| CONDDIR   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | Do not match on conditional direct branch instructions. |
| 0b1       | Match on conditional direct branch instructions.        |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## DIRCALL, bit [21]

Match on direct branch with link instructions.

| DIRCALL   | Meaning                                               |
|-----------|-------------------------------------------------------|
| 0b0       | Do not match on direct branch with link instructions. |
| 0b1       | Match on direct branch with link instructions.        |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## INDCALL, bit [20]

Match on indirect branch with link instructions.

| INDCALL   | Meaning                                                 |
|-----------|---------------------------------------------------------|
| 0b0       | Do not match on indirect branch with link instructions. |
| 0b1       | Match on indirect branch with link instructions.        |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## RTN, bit [19]

Match on function return instructions.

| RTN   | Meaning                                       |
|-------|-----------------------------------------------|
| 0b0   | Do not match on function return instructions. |
| 0b1   | Match on function return instructions.        |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## INDIRECT, bit [18]

Match on indirect branch instructions.

| INDIRECT   | Meaning                                       |
|------------|-----------------------------------------------|
| 0b0        | Do not match on indirect branch instructions. |
| 0b1        | Match on indirect branch instructions.        |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## DIRECT, bit [17]

Match on unconditional direct branch instructions.

| DIRECT   | Meaning                                                   |
|----------|-----------------------------------------------------------|
| 0b0      | Do not match on unconditional direct branch instructions. |
| 0b1      | Match on unconditional direct branch instructions.        |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## EnI, bit [16]

Include or exclude matches.

| EnI   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b0   | Include records for matches, and exclude records for non-matches. |
| 0b1   | Exclude records for matches, and include records for non-matches. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Bits [15:8]

Reserved, RES0.

## PAUSED, bit [7]

Branch recording Paused status.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_BRBEv1p1 is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to an architecturally UNKNOWN value.

## Bits [6:0]

Reserved, RES0.

## Accessing BRBFCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then
```

| PAUSED   | Meaning                         |
|----------|---------------------------------|
| 0b0      | Branch recording is not Paused. |
| 0b1      | Branch recording is Paused.     |

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBCTL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBFCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBFCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBFCR_EL1;
```

MSR BRBFCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBCTL == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBFCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBFCR_EL1 = X[t, 64];
```

## D24.8.4 BRBIDR0\_EL1, Branch Record Buffer ID0 Register

The BRBIDR0\_EL1 characteristics are:

## Purpose

Indicates the features of the branch buffer unit.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBIDR0\_EL1 are UNDEFINED.

## Attributes

BRBIDR0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## CC, bits [15:12]

Cycle counter support. Defined values are:

All other values are reserved.

Access to this field is RO.

## FORMAT, bits [11:8]

Data format of records of the Branch record buffer. Defined values are:

| FORMAT   | Meaning   |
|----------|-----------|
| 0b0000   | Format 0. |

All other values are reserved.

Access to this field is RO.

| CC     | Meaning                           |
|--------|-----------------------------------|
| 0b0101 | 20-bit cycle counter implemented. |

## NUMREC,bits [7:0]

Number of records supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMREC   | Meaning                        |
|----------|--------------------------------|
| 0x08     | 8 branch records implemented.  |
| 0x10     | 16 branch records implemented. |
| 0x20     | 32 branch records implemented. |
| 0x40     | 64 branch records implemented. |

All other values are reserved.

Access to this field is RO.

## Accessing BRBIDR0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBIDR0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBIDR == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBIDR0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBIDR0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBIDR0_EL1;
```

## D24.8.5 BRBINFINJ\_EL1, Branch Record Buffer Information Injection Register

The BRBINFINJ\_EL1 characteristics are:

## Purpose

The information of a Branch record for injection.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBINFINJ\_EL1 are UNDEFINED.

## Attributes

BRBINFINJ\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:47]

Reserved, RES0.

## CCU, bit [46]

The number of PE clock cycles since the last Branch record entry is UNKNOWN.

| CCU   | Meaning                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------|
| 0b0   | Indicates that the number of PE clock cycles since the last Branch record is indicated by BRBINFINJ_EL1.CC. |
| 0b1   | Indicates that the number of PE clock cycles since the last Branch record is UNKNOWN.                       |

The value in this field is only valid when BRBINFINJ\_EL1.V ALID != 0b00 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When BRBINFINJ\_EL1.VALID == '00', access to this field is RES0.
- Otherwise, access to this field is RW.

## CC, bits [45:32]

The number of PE clock cycles since the last Branch record entry.

The format of this field uses a mantissa and exponent to express the cycle count value, as follows:

- CCbits[7:0] indicate the mantissa M.
- CCbits[13:8] indicate the exponent E.

The cycle count is expressed using the following function:

```
if IsZero(E), then UInt(M) else UInt('1':M:Zeros(UInt(E)-1))
```

If required, the cycle count is rounded to a multiple of 2 (E-1) towards zero before being encoded.

Avalue of all ones in both the mantissa and exponent indicates the cycle count value exceeded the size of the cycle counter.

The value in this field is only valid when BRBINFINJ\_EL1.V ALID != 0b00 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINFINJ\_EL1.CCU == '1'
- BRBINFINJ\_EL1.VALID == '00'
- Otherwise, access to this field is RW.

Bits [31:14]

Reserved, RES0.

## TYPE, bits [13:8]

Branch type.

| TYPE     | Meaning                                                                                    |
|----------|--------------------------------------------------------------------------------------------|
| 0b000000 | Unconditional direct branch, excluding Branch with link.                                   |
| 0b000001 | Indirect branch, excluding Branch with link, Return from subroutine, and Exception return. |
| 0b000010 | Direct Branch with link.                                                                   |
| 0b000011 | Indirect Branch with link.                                                                 |
| 0b000101 | Return from subroutine.                                                                    |
| 0b000111 | Exception return.                                                                          |
| 0b001000 | Conditional direct branch.                                                                 |
| 0b100001 | Debug halt.                                                                                |
| 0b100010 | Call.                                                                                      |
| 0b100011 | Trap.                                                                                      |
| 0b100100 | SError.                                                                                    |
| 0b100110 | Instruction debug.                                                                         |
| 0b100111 | Data debug.                                                                                |
| 0b101010 | Alignment.                                                                                 |
| 0b101011 | Inst Fault.                                                                                |
| 0b101100 | Data Fault.                                                                                |
| 0b101110 | IRQ.                                                                                       |

| TYPE     | Meaning                                  |
|----------|------------------------------------------|
| 0b101111 | FIQ.                                     |
| 0b110000 | IMPLEMENTATION DEFINED exception to EL3. |
| 0b111001 | Debug State Exit.                        |

All other values are reserved.

The value in this field is only valid when BRBINFINJ\_EL1.V ALID != 0b00 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When BRBINFINJ\_EL1.VALID == '00', access to this field is RES0.
- Otherwise, access to this field is RW.

## EL, bits [7:6]

The Exception level at the target address.

| EL   | Meaning   | Applies when                 |
|------|-----------|------------------------------|
| 0b00 | EL0.      |                              |
| 0b01 | EL1.      |                              |
| 0b10 | EL2.      |                              |
| 0b11 | EL3.      | FEAT_BRBEv1p1 is implemented |

The value in this field is only valid when BRBINFINJ\_EL1.V ALID == 0b11 or BRBINFINJ\_EL1.VALID == 0b01 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINFINJ\_EL1.VALID == '00'
- BRBINFINJ\_EL1.VALID == '10'
- Otherwise, access to this field is RW.

## MPRED, bit [5]

Branch mispredict.

| MPRED   | Meaning                                                                          |
|---------|----------------------------------------------------------------------------------|
| 0b0     | Branch was correctly predicted or the result of the prediction was not captured. |
| 0b1     | Branch was incorrectly predicted.                                                |

The value in this field is only valid when BRBINFINJ\_EL1.V ALID == 0b11 or BRBINFINJ\_EL1.VALID == 0b10 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINFINJ\_EL1.VALID == '00'
- BRBINFINJ\_EL1.VALID == '01'
- BRBINFINJ\_EL1.TYPE[5] == '1'
- Otherwise, access to this field is RW.

## Bits [4:2]

Reserved, RES0.

## VALID, bits [1:0]

The Branch record is valid.

| VALID   | Meaning                                                                                                                                                                                                                                                                                   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | This Branch record is not valid. The values of following fields are not valid: • BRBTGTINJ_EL1.ADDRESS. • BRBSRCINJ_EL1.ADDRESS. • BRBINFINJ_EL1.MPRED. • BRBINFINJ_EL1.LASTFAILED. • BRBINFINJ_EL1.T. • BRBINFINJ_EL1.EL. • BRBINFINJ_EL1.TYPE. • BRBINFINJ_EL1.CC. • BRBINFINJ_EL1.CCU. |
| 0b01    | This Branch record is valid. The values of following fields are not valid: • BRBSRCINJ_EL1.ADDRESS. • BRBINFINJ_EL1.T. • BRBINFINJ_EL1.MPRED.                                                                                                                                             |
| 0b10    | This Branch record is valid. The values of following fields are not valid: • BRBTGTINJ_EL1.ADDRESS. • BRBINFINJ_EL1.EL.                                                                                                                                                                   |
| 0b11    | This Branch record is valid.                                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing BRBINFINJ\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBINFINJ\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBINFINJ_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBINFINJ_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBINFINJ_EL1;
```

MSR BRBINFINJ\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBINFINJ_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBINFINJ_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBINFINJ_EL1 = X[t, 64];
```

## D24.8.6 BRBINF&lt;n&gt;\_EL1, Branch Record Buffer Information Register &lt;n&gt;, n = 0 - 31

The BRBINF&lt;n&gt;\_EL1 characteristics are:

## Purpose

The information for Branch record n + (BRBFCR\_EL1.BANK × 32).

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBINF&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

BRBINF&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:47]

Reserved, RES0.

## CCU, bit [46]

The number of PE clock cycles since the last Branch record entry is UNKNOWN.

| CCU   | Meaning                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------|
| 0b0   | Indicates that the number of PE clock cycles since the last Branch record is indicated by BRBINF<n>_EL1.CC. |
| 0b1   | Indicates that the number of PE clock cycles since the last Branch record is UNKNOWN.                       |

The value in this field is only valid when BRBINF&lt;n&gt;\_EL1.VALID != 0b00 .

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When BRBINF&lt;n&gt;\_EL1.VALID == '00', access to this field is RES0.
- Otherwise, access to this field is RO.

## CC, bits [45:32]

The number of PE clock cycles since the last Branch record entry.

The format of this field uses a mantissa and exponent to express the cycle count value, as follows:

- CCbits[7:0] indicate the mantissa M.
- CCbits[13:8] indicate the exponent E.

The cycle count is expressed using the following function:

```
if IsZero(E), then UInt(M) else UInt('1':M:Zeros(UInt(E)-1))
```

If required, the cycle count is rounded to a multiple of 2 (E-1) towards zero before being encoded.

Avalue of all ones in both the mantissa and exponent indicates the cycle count value exceeded the size of the cycle counter.

The value in this field is only valid when BRBINF&lt;n&gt;\_EL1.VALID != 0b00 .

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINF&lt;n&gt;\_EL1.CCU == '1'
- BRBINF&lt;n&gt;\_EL1.VALID == '00'
- Otherwise, access to this field is RO.

Bits [31:14]

Reserved, RES0.

## TYPE, bits [13:8]

Branch type.

| TYPE     | Meaning                                                                                    |
|----------|--------------------------------------------------------------------------------------------|
| 0b000000 | Unconditional direct branch, excluding Branch with link.                                   |
| 0b000001 | Indirect branch, excluding Branch with link, Return from subroutine, and Exception return. |
| 0b000010 | Direct Branch with link.                                                                   |
| 0b000011 | Indirect Branch with link.                                                                 |
| 0b000101 | Return from subroutine.                                                                    |
| 0b000111 | Exception return.                                                                          |
| 0b001000 | Conditional direct branch.                                                                 |
| 0b100001 | Debug halt.                                                                                |
| 0b100010 | Call.                                                                                      |
| 0b100011 | Trap.                                                                                      |
| 0b100100 | SError.                                                                                    |
| 0b100110 | Instruction debug.                                                                         |
| 0b100111 | Data debug.                                                                                |
| 0b101010 | Alignment.                                                                                 |
| 0b101011 | Inst Fault.                                                                                |
| 0b101100 | Data Fault.                                                                                |
| 0b101110 | IRQ.                                                                                       |

| TYPE     | Meaning                                  |
|----------|------------------------------------------|
| 0b101111 | FIQ.                                     |
| 0b110000 | IMPLEMENTATION DEFINED exception to EL3. |
| 0b111001 | Debug State Exit.                        |

All other values are reserved.

The value in this field is only valid when BRBINF&lt;n&gt;\_EL1.VALID != 0b00 .

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When BRBINF&lt;n&gt;\_EL1.VALID == '00', access to this field is RES0.
- Otherwise, access to this field is RO.

## EL, bits [7:6]

The Exception level at the target address.

| EL   | Meaning   | Applies when                 |
|------|-----------|------------------------------|
| 0b00 | EL0.      |                              |
| 0b01 | EL1.      |                              |
| 0b10 | EL2.      |                              |
| 0b11 | EL3.      | FEAT_BRBEv1p1 is implemented |

The value in this field is only valid when BRBINF&lt;n&gt;\_EL1.VALID == 0b11 or BRBINF&lt;n&gt;\_EL1.VALID == 0b01 .

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINF&lt;n&gt;\_EL1.VALID == '00'
- BRBINF&lt;n&gt;\_EL1.VALID == '10'
- Otherwise, access to this field is RO.

## MPRED, bit [5]

Branch mispredict.

| MPRED   | Meaning                                                                          |
|---------|----------------------------------------------------------------------------------|
| 0b0     | Branch was correctly predicted or the result of the prediction was not captured. |
| 0b1     | Branch was incorrectly predicted.                                                |

The value in this field is only valid when BRBINF&lt;n&gt;\_EL1.VALID == 0b11 or BRBINF&lt;n&gt;\_EL1.VALID == 0b10 .

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINF&lt;n&gt;\_EL1.VALID == '00'
- BRBINF&lt;n&gt;\_EL1.VALID == '01'
- BRBINF&lt;n&gt;\_EL1.TYPE[5] == '1'
- Otherwise, access to this field is RO.

## Bits [4:2]

Reserved, RES0.

## VALID, bits [1:0]

The Branch record is valid.

| VALID   | Meaning                                                                                                                                                                                                                                                                                   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | This Branch record is not valid. The values of following fields are not valid: • BRBTGT<n>_EL1.ADDRESS. • BRBSRC<n>_EL1.ADDRESS. • BRBINF<n>_EL1.MPRED. • BRBINF<n>_EL1.LASTFAILED. • BRBINF<n>_EL1.T. • BRBINF<n>_EL1.EL. • BRBINF<n>_EL1.TYPE. • BRBINF<n>_EL1.CC. • BRBINF<n>_EL1.CCU. |
| 0b01    | This Branch record is valid. The values of following fields are not valid: • BRBSRC<n>_EL1.ADDRESS. • BRBINF<n>_EL1.T. • BRBINF<n>_EL1.MPRED.                                                                                                                                             |
| 0b10    | This Branch record is valid. The values of following fields are not valid: • BRBTGT<n>_EL1.ADDRESS. • BRBINF<n>_EL1.EL.                                                                                                                                                                   |
| 0b11    | This Branch record is valid.                                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing BRBINF&lt;n&gt;\_EL1

BRBINF&lt;n&gt;\_EL1 reads-as-zero if n + (BRBFCR\_EL1.BANK × 32) &gt;= BRBIDR0\_EL1.NUMREC.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b1000 | m[3:0] | m[4]: 0b00 |

```
integer m = UInt(op2<2>:CRm<3:0>); if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBINF_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBINF_EL1[m]; elsif PSTATE.EL == EL3 then if m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBINF_EL1[m];
```

## D24.8.7 BRBSRCINJ\_EL1, Branch Record Buffer Source Address Injection Register

The BRBSRCINJ\_EL1 characteristics are:

## Purpose

The source address of a Branch record for injection.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBSRCINJ\_EL1 are UNDEFINED.

## Attributes

BRBSRCINJ\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## ADDRESS, bits [63:0]

Source virtual address of the Branch record.

When a direct write occurs with a value with ADDRESS bits [63:P] indicating an invalid address, an UNKNOWN value which indicates an invalid address is written to bits [63:P].

An invalid address is:

- For an address in a translation regime with 2 V A ranges, with bits [63:P] not all zeroes or all ones.
- For an address in a translation regime with a single V A range, with bits [63:P] not all zeroes.

## P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

The value in bits [P-1:0] is the value written.

When a direct write occurs with a value with ADDRESS bits [63:P] indicating a valid address, the written value is written to bits [63:0], and a read of the register returns the written value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINFINJ\_EL1.VALID == '00'
- BRBINFINJ\_EL1.VALID == '01'
- Otherwise, access to this field is RW.

## Accessing BRBSRCINJ\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBSRCINJ\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBSRCINJ_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBSRCINJ_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBSRCINJ_EL1;
```

MSR BRBSRCINJ\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBSRCINJ_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBSRCINJ_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBSRCINJ_EL1 = X[t, 64];
```

## D24.8.8 BRBSRC&lt;n&gt;\_EL1, Branch Record Buffer Source Address Register &lt;n&gt;, n = 0 - 31

The BRBSRC&lt;n&gt;\_EL1 characteristics are:

## Purpose

The source address of Branch record n + (BRBFCR\_EL1.BANK × 32).

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBSRC&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

BRBSRC&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## ADDRESS, bits [63:0]

Source virtual address of the Branch record.

When an indirect write occurs with a value with ADDRESS bits [63:P] indicating an invalid address, an UNKNOWN value which indicates an invalid address is written to bits [63:P].

An invalid address is:

- For an address in a translation regime with 2 V A ranges, with bits [63:P] not all zeroes or all ones.
- For an address in a translation regime with a single V A range, with bits [63:P] not all zeroes.

P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

The value in bits [P-1:0] is the value written.

When an indirect write occurs with a value with ADDRESS bits [63:P] indicating a valid address, the written value is written to bits [63:0], and a read of the register returns the written value.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINF&lt;n&gt;\_EL1.VALID == '00'
- BRBINF&lt;n&gt;\_EL1.VALID == '01'
- Otherwise, access to this field is RO.

## Accessing BRBSRC&lt;n&gt;\_EL1

BRBSRC&lt;n&gt;\_EL1 is RES0 if n + (BRBFCR\_EL1.BANK × 32) &gt;= BRBIDR0\_EL1.NUMREC.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBSRC&lt;m&gt;\_EL1 ; Where m = 0-31

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b1000 | m[3:0] | m[4]: 0b01 |

```
integer m = UInt(op2<2>:CRm<3:0>); if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBSRC_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBSRC_EL1[m]; elsif PSTATE.EL == EL3 then if m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBSRC_EL1[m];
```

## D24.8.9 BRBTGTINJ\_EL1, Branch Record Buffer Target Address Injection Register

The BRBTGTINJ\_EL1 characteristics are:

## Purpose

The target address of a Branch record for injection.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBTGTINJ\_EL1 are UNDEFINED.

## Attributes

BRBTGTINJ\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## ADDRESS, bits [63:0]

Target virtual address of the Branch record.

When a direct write occurs with a value with ADDRESS bits [63:P] indicating an invalid address, an UNKNOWN value which indicates an invalid address is written to bits [63:P].

An invalid address is:

- For an address in a translation regime with 2 V A ranges, with bits [63:P] not all zeroes or all ones.
- For an address in a translation regime with a single V A range, with bits [63:P] not all zeroes.

## P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

The value in bits [P-1:0] is the value written.

When a direct write occurs with a value with ADDRESS bits [63:P] indicating a valid address, the written value is written to bits [63:0], and a read of the register returns the written value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINFINJ\_EL1.VALID == '00'
- BRBINFINJ\_EL1.VALID == '10'
- Otherwise, access to this field is RW.

## Accessing BRBTGTINJ\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBTGTINJ\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBTGTINJ_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBTGTINJ_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBTGTINJ_EL1;
```

MSR BRBTGTINJ\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBTGTINJ_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBTGTINJ_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBTGTINJ_EL1 = X[t, 64];
```

## D24.8.10 BRBTGT&lt;n&gt;\_EL1, Branch Record Buffer Target Address Register &lt;n&gt;, n = 0 - 31

The BRBTGT&lt;n&gt;\_EL1 characteristics are:

## Purpose

The target address of Branch record n + (BRBFCR\_EL1.BANK × 32).

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBTGT&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

BRBTGT&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## ADDRESS, bits [63:0]

Target virtual address of the Branch record.

When an indirect write occurs with a value with ADDRESS bits [63:P] indicating an invalid address, an UNKNOWN value which indicates an invalid address is written to bits [63:P].

An invalid address is:

- For an address in a translation regime with 2 V A ranges, with bits [63:P] not all zeroes or all ones.
- For an address in a translation regime with a single V A range, with bits [63:P] not all zeroes.

P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

The value in bits [P-1:0] is the value written.

When an indirect write occurs with a value with ADDRESS bits [63:P] indicating a valid address, the written value is written to bits [63:0], and a read of the register returns the written value.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if any of the following are true:
- BRBINF&lt;n&gt;\_EL1.VALID == '00'
- BRBINF&lt;n&gt;\_EL1.VALID == '10'
- Otherwise, access to this field is RO.

## Accessing BRBTGT&lt;n&gt;\_EL1

BRBTGT&lt;n&gt;\_EL1 is RES0 if n + (BRBFCR\_EL1.BANK × 32) &gt;= BRBIDR0\_EL1.NUMREC.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, BRBTGT&lt;m&gt;\_EL1 ; Where m = 0-31

| op0   | op1   | CRn    | CRm    | op2        |
|-------|-------|--------|--------|------------|
| 0b10  | 0b001 | 0b1000 | m[3:0] | m[4]: 0b10 |

```
integer m = UInt(op2<2>:CRm<3:0>); if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBTGT_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBTGT_EL1[m]; elsif PSTATE.EL == EL3 then if m + (UInt(BRBFCR_EL1.BANK) * 32) >= NUM_BRBE_RECORDS then X[t, 64] = Zeros(64); else X[t, 64] = BRBTGT_EL1[m];
```

## D24.8.11 BRBTS\_EL1, Branch Record Buffer Timestamp Register

The BRBTS\_EL1 characteristics are:

Purpose

Captures the Timestamp value on a BRBE freeze event.

## Configuration

This register is present only when FEAT\_BRBE is implemented. Otherwise, direct accesses to BRBTS\_EL1 are UNDEFINED.

## Attributes

BRBTS\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |    | 32   |
|------|----|------|
|      | TS |      |
| 31   |    | 0    |
|      | TS |      |

## TS, bits [63:0]

Timestamp value at the time of a BRBE freeze event.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_BRBEv1p1 is not implemented, this field resets to 0x0000000000000000 .

When FEAT\_BRBEv1p1 is implemented, Arm recommends that this field is preserved on a Warm reset, but it is IMPLEMENTATION DEFINED whether this field resets to 0 or is preserved.

When FEAT\_BRBEv1p1 is implemented, on a Cold reset it is IMPLEMENTATION DEFINED whether this field resets to an architecturally UNKNOWN value.

## Accessing BRBTS\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, BRBTS_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED;
```

```
elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBTS_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = BRBTS_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = BRBTS_EL1;
```

MSR BRBTS\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b1001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_BRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.nBRBDATA == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBTS_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.SBRBE != '11' && SCR_EL3.NS == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.SBRBE IN {'x0'} && SCR_EL3.NS == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else BRBTS_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then BRBTS_EL1 = X[t, 64];
```