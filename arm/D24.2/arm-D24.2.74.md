## D24.2.74 HFGWTR2\_EL2, Hypervisor Fine-Grained Write Trap Register 2

The HFGWTR2\_EL2 characteristics are:

## Purpose

Provides controls for traps of MSRR , MSR and MCR writes of System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HFGWTR2\_EL2 are UNDEFINED.

## Attributes

HFGWTR2\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

Bits [63:15]

Reserved, RES0.

## nACTLRALIAS\_EL1, bit [14]

When FEAT\_SRMASK is implemented:

Trap MSR writes of ACTLRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nACTLRALIAS_EL1   | Meaning                                                                                                                                                                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MSR writes of ACTLRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1               | MSR writes of ACTLRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nACTLRMASK\_EL1, bit [13]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of ACTLRMASK\_EL1 at EL1 using AArch64 to EL2.

| nACTLRMASK_EL1   | Meaning                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MSR writes of ACTLRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1              | MSR writes of ACTLRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nTCR2ALIAS\_EL1, bit [12]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of TCR2ALIAS\_EL1 at EL1 using AArch64 to EL2.

| nTCR2ALIAS_EL1   | Meaning                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MSR writes of TCR2ALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1              | MSR writes of TCR2ALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nTCRALIAS\_EL1, bit [11]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of TCRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nTCRALIAS_EL1   | Meaning                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then MSR writes of TCRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1             | MSR writes of TCRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSCTLR2ALIAS\_EL1, bit [10]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of SCTLR2ALIAS\_EL1 at EL1 using AArch64 to EL2.

| nSCTLR2ALIAS_EL1   | Meaning                                                                                                                                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                | If EL2 is implemented and enabled in the current Security state, then MSR writes of SCTLR2ALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1                | MSR writes of SCTLR2ALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSCTLRALIAS\_EL1, bit [9]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of SCTLRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nSCTLRALIAS_EL1   | Meaning                                                                                                                                                                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MSR writes of SCTLRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1               | MSR writes of SCTLRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nCPACRALIAS\_EL1, bit [8]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of CPACRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nCPACRALIAS_EL1   | Meaning                                                                                                                                                                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MSR writes of CPACRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1               | MSR writes of CPACRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nTCR2MASK\_EL1, bit [7]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of TCR2MASK\_EL1 at EL1 using AArch64 to EL2.

| nTCR2MASK_EL1   | Meaning                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then MSR writes of TCR2MASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1             | MSR writes of TCR2MASK_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nTCRMASK\_EL1, bit [6]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of TCRMASK\_EL1 at EL1 using AArch64 to EL2.

| nTCRMASK_EL1   | Meaning                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, then MSR writes of TCRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1            | MSR writes of TCRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSCTLR2MASK\_EL1, bit [5]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of SCTLR2MASK\_EL1 at EL1 using AArch64 to EL2.

| nSCTLR2MASK_EL1   | Meaning                                                                                                                                                                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MSR writes of SCTLR2MASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1               | MSR writes of SCTLR2MASK_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSCTLRMASK\_EL1, bit [4]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of SCTLRMASK\_EL1 at EL1 using AArch64 to EL2.

| nSCTLRMASK_EL1   | Meaning                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MSR writes of SCTLRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1              | MSR writes of SCTLRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nCPACRMASK\_EL1, bit [3]

## When FEAT\_SRMASK is implemented:

Trap MSR writes of CPACRMASK\_EL1 at EL1 using AArch64 to EL2.

| nCPACRMASK_EL1   | Meaning                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MSR writes of CPACRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1              | MSR writes of CPACRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nRCWSMASK\_EL1, bit [2]

When FEAT\_THE is implemented:

Trap MSR or MSRR writes of RCWSMASK\_EL1 at EL1 using AArch64 to EL2.

| nRCWSMASK_EL1   | Meaning                                                                                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then unless the write generates a higher priority exception: • MSR writes of RCWSMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MSRR writes of RCWSMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |
| 0b1             | MSR and MSRR writes of RCWSMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                         |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [1]

Reserved, RES0.

## nPFAR\_EL1, bit [0]

## When FEAT\_PFAR is implemented:

Trap MSR writes of PFAR\_EL1 at EL1 using AArch64 to EL2.

| nPFAR_EL1   | Meaning                                                                                                                                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If EL2 is implemented and enabled in the current Security state, then MSR writes of PFAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1         | MSR writes of PFAR_EL1 are not trapped by this mechanism.                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing HFGWTR2\_EL2

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x2C8]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HFGWTR2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HFGWTR2_EL2;
```

MSR HFGWTR2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x2C8] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HFGWTR2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HFGWTR2_EL2 = X[t, 64];
```

```
then
```

```
then
```