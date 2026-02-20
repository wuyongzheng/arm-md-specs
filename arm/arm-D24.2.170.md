## D24.2.170 SCTLR2\_EL1, System Control Register (EL1)

The SCTLR2\_EL1 characteristics are:

## Purpose

Provides top-level control of the system, including its memory system, at EL1 and EL0.

## Configuration

This register is present only when FEAT\_SCTLR2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SCTLR2\_EL1 are UNDEFINED.

## Attributes

SCTLR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:13]

Reserved, RES0.

## CPTM0, bit [12]

## When FEAT\_CPA2 is implemented:

This field controls unprivileged Checked Pointer Arithmetic for Multiplication.

| CPTM0   | Meaning                                               |
|---------|-------------------------------------------------------|
| 0b0     | Pointer Arithmetic for Multiplication is not checked. |
| 0b1     | Pointer Arithmetic for Multiplication is checked.     |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this bit has no effect on execution.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

If the Effective value of SCTLR2\_EL1.CPTA0 is 0, then the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CPTM, bit [11]

## When FEAT\_CPA2 is implemented:

This field controls Checked Pointer Arithmetic for Multiplication at EL1.

| CPTM   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0    | Pointer Arithmetic for Multiplication is not checked. |
| 0b1    | Pointer Arithmetic for Multiplication is checked.     |

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

If the Effective value of SCTLR2\_EL1.CPTA is 0, then the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CPTA0, bit [10]

## When FEAT\_CPA2 is implemented:

This field controls unprivileged Checked Pointer Arithmetic for Addition.

| CPTA0   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Pointer Arithmetic for Addition is not checked. |
| 0b1     | Pointer Arithmetic for Addition is checked.     |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this bit has no effect on execution.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CPTA, bit [9]

## When FEAT\_CPA2 is implemented:

This field controls Checked Pointer Arithmetic for Addition at EL1.

| CPTA   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Pointer Arithmetic for Addition is not checked. |
| 0b1    | Pointer Arithmetic for Addition is checked.     |

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnPACM0, bit [8]

## When FEAT\_PAuth\_LR is implemented:

PACMEnable at EL0. Controls the effect of a PACM instruction at EL0.

| EnPACM0   | Meaning                                                     |
|-----------|-------------------------------------------------------------|
| 0b0       | The effects of PACMare disabled at EL0.                     |
| 0b1       | APACMinstruction at EL0 causes PSTATE.PACM to be set to 0b1 |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this bit has no effect on execution at EL0.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.PACMEn == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnPACM, bit [7]

## When FEAT\_PAuth\_LR is implemented:

PACMEnable at EL1. Controls the effect of a PACM instruction at EL1.

| EnPACM   | Meaning                                                       |
|----------|---------------------------------------------------------------|
| 0b0      | The effects of PACMare disabled at EL1.                       |
| 0b1      | APACMinstruction at EL1 causes PSTATE.PACM to be set to 0b1 . |

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.PACMEn == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnIDCP128, bit [6]

## When FEAT\_SYSREG128 is implemented:

Enables access to IMPLEMENTATION DEFINED 128-bit System registers.

| EnIDCP128   | Meaning                                                                                                                                                                                                                                                                                          |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Accesses at EL0 to IMPLEMENTATION DEFINED 128-bit System registers are trapped to EL1 using an ESR_EL1.EC value of 0x14 , unless the access generates a higher priority exception. Disables the functionality of the 128-bit IMPLEMENTATION DEFINED System registers that are accessible at EL1. |
| 0b1         | No accesses are trapped by this control.                                                                                                                                                                                                                                                         |

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EASE, bit [5]

## When FEAT\_DoubleFault2 is implemented:

External Aborts to SError exception vector.

| EASE   | Meaning                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Synchronous External abort exceptions taken to EL1 are taken to the appropriate synchronous exception vector offset from VBAR_EL1. |
| 0b1    | Synchronous External abort exceptions taken to EL1 are taken to the appropriate SError exception vector offset from VBAR_EL1.      |

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnANERR, bit [4]

## When FEAT\_ANERR is implemented:

Enable Asynchronous Normal Read Error.

| EnANERR   | Meaning                                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | External aborts on Normal memory reads generate synchronous Data Abort exceptions in the EL1&0 translation regime.                        |
| 0b1       | External aborts on Normal memory reads generate synchronous Data Abort or asynchronous SError exceptions in the EL1&0 translation regime. |

Implementation-specific exceptions to applications of this field are described in 'Taking error exceptions'.

Setting this field to 0 does not guarantee that the PE is able to take a synchronous Data Abort exception for an External abort on a Normal memory read in every case. There might be implementation-specific circumstances when an error on a load cannot be taken synchronously. These circumstances should be rare enough that treating such occurrences as fatal does not cause a significant increase in failure rate.

If FEAT\_SVE is implemented, SCTLR2\_EL1.EnANERR is 0, and the access generating the External abort is due to any Active element of an SVE Non-fault vector load instruction or an Active element that is not the First active element of an SVE First-fault vector load instruction, then no exception is generated and the External abort is reported in the FFR.

Setting this field to 0 might have a performance impact for Normal memory reads.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.EnSNERR is 1.

Otherwise, this field is ignored by the PE and treated as one when all of the following are true:

- FEAT\_ADERR is implemented.
- ID\_AA64MMFR3\_EL1.ANERR reads as 0b0010 .
- SCTLR2\_EL1.EnADERR is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnADERR, bit [3]

## When FEAT\_ADERR is implemented:

Enable Asynchronous Device Read Error.

| EnADERR   | Meaning                                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | External aborts on Device memory reads generate synchronous Data Abort exceptions in the EL1&0 translation regime.                        |
| 0b1       | External aborts on Device memory reads generate synchronous Data Abort or asynchronous SError exceptions in the EL1&0 translation regime. |

Implementation-specific exceptions to applications of this field are described in 'Taking error exceptions'.

Setting this field to 0 does not guarantee that the PE is able to take a synchronous Data Abort exception for an External abort on a Device memory read in every case. There might be implementation-specific circumstances when an error on a load cannot be taken synchronously. These circumstances should be rare enough that treating such occurrences as fatal does not cause a significant increase in failure rate.

If FEAT\_SVE is implemented, SCTLR2\_EL1.EnADERR is 0, and the access generating the External abort is due to any Active element of an SVE Non-fault vector load instruction or an Active element that is not the First active element of an SVE First-fault vector load instruction, then no exception is generated and the External abort is reported in the FFR.

Setting this field to 0 might have a performance impact for Device memory reads.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.EnSDERR is 1.

Otherwise, this field is ignored by the PE and treated as one when all of the following are true:

- FEAT\_ANERR is implemented.
- ID\_AA64MMFR3\_EL1.ADERR reads as 0b0010 .
- SCTLR2\_EL1.EnANERR is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NMEA,bit [2]

## When FEAT\_DoubleFault2 is implemented:

Non-maskable External Aborts. Controls whether PSTATE.A masks physical SError exceptions at EL1.

| NMEA   | Meaning                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Physical SError exceptions are not taken at EL1 if PSTATE.A == 1, unless routed to a higher Exception level.                |
| 0b1    | Physical SError exceptions are taken at EL1 regardless of the value of PSTATE.A, unless routed to a higher Exception level. |

This field has no effect on the masking of virtual and delegated SError interrupts.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and SCR\_EL3.SCTLR2En == 0.
- EL2 is implemented and enabled in the current Security state and the Effective value of HCRX\_EL2.SCTLR2En is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [1:0]

Reserved, RES0.

## Accessing SCTLR2\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name SCTLR2\_EL1 or SCTLR2\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

If FEAT\_SRMASK is implemented, accesses to SCTLR2\_EL1 are masked by SCTLR2MASK\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SCTLR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SCTLR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.SCTLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SCTLR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x278]; else X[t, 64] = SCTLR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = SCTLR2_EL2; else X[t, 64] = SCTLR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLR2_EL1;
```

MSR SCTLR2\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SCTLR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED;
```

```
elsif EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.SCTLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SCTLR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x278] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then SCTLR2_EL1 = (X[t, 64] AND NOT EffectiveSCTLR2MASK_EL1()) OR (SCTLR2_EL1 AND ↪ → EffectiveSCTLR2MASK_EL1()); else SCTLR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then SCTLR2_EL2 = (X[t, 64] AND NOT EffectiveSCTLR2MASK_EL2()) OR (SCTLR2_EL2 AND ↪ → EffectiveSCTLR2MASK_EL2()); else SCTLR2_EL2 = X[t, 64]; else SCTLR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLR2_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SCTLR2\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SCTLR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x278]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCTLR2_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = SCTLR2_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR SCTLR2\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SCTLR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x278] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SCTLR2_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then SCTLR2_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_SRMASK is implemented MRS &lt;Xt&gt;, SCTLR2ALIAS\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_SCTLR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGRTR2_EL2.nSCTLR2ALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SCTLR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x278]; else X[t, 64] = SCTLR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = SCTLR2_EL2; else X[t, 64] = SCTLR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLR2_EL1;
```

When FEAT\_SRMASK is implemented MSR SCTLR2ALIAS\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_SCTLR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGWTR2_EL2.nSCTLR2ALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SCTLR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x278] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then SCTLR2_EL1 = (X[t, 64] AND NOT EffectiveSCTLR2MASK_EL1()) OR (SCTLR2_EL1 AND ↪ → EffectiveSCTLR2MASK_EL1()); else SCTLR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SCTLR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SCTLR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then SCTLR2_EL2 = (X[t, 64] AND NOT EffectiveSCTLR2MASK_EL2()) OR (SCTLR2_EL2 AND ↪ → EffectiveSCTLR2MASK_EL2()); else SCTLR2_EL2 = X[t, 64]; else SCTLR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLR2_EL1 = X[t, 64];
```