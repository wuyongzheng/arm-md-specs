## D24.2.72 HFGRTR2\_EL2, Hypervisor Fine-Grained Read Trap Register 2

The HFGRTR2\_EL2 characteristics are:

## Purpose

Provides controls for traps of MRRS , MRS and MRC reads of System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HFGRTR2\_EL2 are UNDEFINED.

## Attributes

HFGRTR2\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:15]

Reserved, RES0.

## nACTLRALIAS\_EL1, bit [14]

When FEAT\_SRMASK is implemented:

Trap MRS reads of ACTLRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nACTLRALIAS_EL1   | Meaning                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MRS reads of ACTLRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1               | MRS reads of ACTLRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of ACTLRMASK\_EL1 at EL1 using AArch64 to EL2.

| nACTLRMASK_EL1   | Meaning                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MRS reads of ACTLRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1              | MRS reads of ACTLRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of TCR2ALIAS\_EL1 at EL1 using AArch64 to EL2.

| nTCR2ALIAS_EL1   | Meaning                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MRS reads of TCR2ALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1              | MRS reads of TCR2ALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of TCRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nTCRALIAS_EL1   | Meaning                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then MRS reads of TCRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1             | MRS reads of TCRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of SCTLR2ALIAS\_EL1 at EL1 using AArch64 to EL2.

| nSCTLR2ALIAS_EL1   | Meaning                                                                                                                                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                | If EL2 is implemented and enabled in the current Security state, then MRS reads of SCTLR2ALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1                | MRS reads of SCTLR2ALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of SCTLRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nSCTLRALIAS_EL1   | Meaning                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MRS reads of SCTLRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1               | MRS reads of SCTLRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of CPACRALIAS\_EL1 at EL1 using AArch64 to EL2.

| nCPACRALIAS_EL1   | Meaning                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MRS reads of CPACRALIAS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1               | MRS reads of CPACRALIAS_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of TCR2MASK\_EL1 at EL1 using AArch64 to EL2.

| nTCR2MASK_EL1   | Meaning                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then MRS reads of TCR2MASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1             | MRS reads of TCR2MASK_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of TCRMASK\_EL1 at EL1 using AArch64 to EL2.

| nTCRMASK_EL1   | Meaning                                                                                                                                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, then MRS reads of TCRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1            | MRS reads of TCRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of SCTLR2MASK\_EL1 at EL1 using AArch64 to EL2.

| nSCTLR2MASK_EL1   | Meaning                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MRS reads of SCTLR2MASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1               | MRS reads of SCTLR2MASK_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of SCTLRMASK\_EL1 at EL1 using AArch64 to EL2.

| nSCTLRMASK_EL1   | Meaning                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MRS reads of SCTLRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1              | MRS reads of SCTLRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

Trap MRS reads of CPACRMASK\_EL1 at EL1 using AArch64 to EL2.

| nCPACRMASK_EL1   | Meaning                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MRS reads of CPACRMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1              | MRS reads of CPACRMASK_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

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

## When FEAT\_THE is implemented:

Trap MRS or MRRS reads of RCWSMASK\_EL1 at EL1 using AArch64 to EL2.

| nRCWSMASK_EL1   | Meaning                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then unless the read generates a higher priority exception: • MRS reads of RCWSMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRRS reads of RCWSMASK_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |
| 0b1             | MRS and MRRS reads of RCWSMASK_EL1are not trapped by this mechanism.                                                                                                                                                                                                                                                                                        |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nERXGSR\_EL1, bit [1]

## When FEAT\_RASv2 is implemented:

Trap MRS reads of ERXGSR\_EL1 at EL1 using AArch64 to EL2.

| nERXGSR_EL1   | Meaning                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, then MRS reads of ERXGSR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of ERXGSR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

Accessing this field has the following behavior:

- This field is permitted to be RES0 if all of the following are true:
- ERRSELR\_EL1 and all ERX* registers are implemented as UNDEFINED or RAZ/WI.
- ERRIDR\_EL1.NUM is zero.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPFAR\_EL1, bit [0]

## When FEAT\_PFAR is implemented:

Trap MRS reads of PFAR\_EL1 at EL1 using AArch64 to EL2.

| nPFAR_EL1   | Meaning                                                                                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If EL2 is implemented and enabled in the current Security state, then MRS reads of PFAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1         | MRS reads of PFAR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing HFGRTR2\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, HFGRTR2_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x2C0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HFGRTR2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HFGRTR2_EL2;
```

```
then
```

MSR HFGRTR2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x2C0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HFGRTR2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HFGRTR2_EL2 = X[t, 64];
```