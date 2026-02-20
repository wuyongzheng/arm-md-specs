## D24.2.75 HFGWTR\_EL2, Hypervisor Fine-Grained Write Trap Register

The HFGWTR\_EL2 characteristics are:

## Purpose

Provides controls for traps of MSRR , MSR and MCR writes of System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HFGWTR\_EL2 are UNDEFINED.

## Attributes

HFGWTR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

nAMAIR2\_EL1, bit [63]

## When FEAT\_AIE is implemented:

Trap MSR writes of AMAIR2\_EL1 at EL1 using AArch64 to EL2.

| nAMAIR2_EL1   | Meaning                                                                                                                                                                                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of AMAIR2_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1           | MSR writes of AMAIR2_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nMAIR2\_EL1, bit [62]

When FEAT\_AIE is implemented:

Trap MSR writes of MAIR2\_EL1 at EL1 using AArch64 to EL2.

| nMAIR2_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of MAIR2_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1          | MSR writes of MAIR2_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nS2POR\_EL1, bit [61]

## When FEAT\_S2POE is implemented:

Trap MSR writes of S2POR\_EL1 at EL1 using AArch64 to EL2.

| nS2POR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of S2POR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1          | MSR writes of S2POR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPOR\_EL1, bit [60]

## When FEAT\_S1POE is implemented:

Trap MSR writes of POR\_EL1 at EL1 using AArch64 to EL2.

| nPOR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of POR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1        | MSR writes of POR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPOR\_EL0, bit [59]

## When FEAT\_S1POE is implemented:

Trap MSR writes of POR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nPOR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                          |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of POR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

| nPOR_EL0   | Meaning                                                  |
|------------|----------------------------------------------------------|
| 0b1        | MSR writes of POR_EL0 are not trapped by this mechanism. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nPIR\_EL1, bit [58]

## When FEAT\_S1PIE is implemented:

Trap MSR writes of PIR\_EL1 at EL1 using AArch64 to EL2.

| nPIR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of PIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1        | MSR writes of PIR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPIRE0\_EL1, bit [57]

## When FEAT\_S1PIE is implemented:

Trap MSR writes of PIRE0\_EL1 at EL1 using AArch64 to EL2.

| nPIRE0_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of PIRE0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1          | MSR writes of PIRE0_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nRCWMASK\_EL1,bit [56]

## When FEAT\_THE is implemented:

Trap MSR or MSRR writes of RCWMASK\_EL1 at EL1 using AArch64 to EL2.

| nRCWMASK_EL1   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the write generates a higher priority exception: • MSR writes of RCWMASK_EL1at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MSRR writes of RCWMASK_EL1at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |
| 0b1            | MSR and MSRR writes of RCWMASK_EL1are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nTPIDR2\_EL0, bit [55]

## When FEAT\_SME is implemented:

Trap MSR writes of TPIDR2\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nTPIDR2_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of TPIDR2_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1           | MSR writes of TPIDR2_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                         |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

ARM DDI 0487 M.a.a

## nSMPRI\_EL1, bit [54]

## When FEAT\_SME is implemented:

Trap MSR writes of SMPRI\_EL1 at EL1 using AArch64 to EL2.

| nSMPRI_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of SMPRI_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1          | MSR writes of SMPRI_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCS\_EL1, bit [53]

## When FEAT\_GCS is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- GCSCR\_EL1.
- GCSPR\_EL1.

| nGCS_EL1   | Meaning                                                                                                                                                                                                                                                                                                                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1        | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCS\_EL0, bit [52]

## When FEAT\_GCS is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- GCSCRE0\_EL1.

- GCSPR\_EL0.

| nGCS_EL0   | Meaning                                                                                                                                                                                                                                                                                                                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1        | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [51]

Reserved, RES0.

## nACCDATA\_EL1, bit [50]

## When FEAT\_LS64\_ACCDATA is implemented:

Trap MSR writes of ACCDATA\_EL1 at EL1 using AArch64 to EL2.

| nACCDATA_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ACCDATA_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |
| 0b1            | MSR writes of ACCDATA_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ERXADDR\_EL1, bit [49]

## When FEAT\_RAS is implemented:

Trap MSR writes of ERXADDR\_EL1 at EL1 using AArch64 to EL2.

| ERXADDR_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MSR writes of ERXADDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ERXADDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

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

## ERXPFGCDN\_EL1, bit [48]

## When FEAT\_RASv1p1 is implemented:

Trap MSR writes of ERXPFGCDN\_EL1 at EL1 using AArch64 to EL2.

| ERXPFGCDN_EL1   | Meaning                                                                                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MSR writes of ERXPFGCDN_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ERXPFGCDN_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

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

## ERXPFGCTL\_EL1, bit [47]

## When FEAT\_RASv1p1 is implemented:

Trap MSR writes of ERXPFGCTL\_EL1 at EL1 using AArch64 to EL2.

| ERXPFGCTL_EL1   | Meaning                                                                                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MSR writes of ERXPFGCTL_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ERXPFGCTL_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

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

## Bit [46]

Reserved, RES0.

## ERXMISCn\_EL1, bit [45]

## When FEAT\_RAS is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- ERXMISC0\_EL1.
- ERXMISC1\_EL1.
- ERXMISC2\_EL1.
- ERXMISC3\_EL1.

| ERXMISCn_EL1   | Meaning                                                                                                                                                                                                                                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

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

## ERXSTATUS\_EL1, bit [44]

## When FEAT\_RAS is implemented:

Trap MSR writes of ERXSTATUS\_EL1 at EL1 using AArch64 to EL2.

| ERXSTATUS_EL1   | Meaning                                                                                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MSR writes of ERXSTATUS_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ERXSTATUS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

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

## ERXCTLR\_EL1, bit [43]

## When FEAT\_RAS is implemented:

Trap MSR writes of ERXCTLR\_EL1 at EL1 using AArch64 to EL2.

| ERXCTLR_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MSR writes of ERXCTLR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ERXCTLR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

Accessing this field has the following behavior:

- This field is permitted to be RES0 if all of the following are true:

•

ERRSELR\_EL1 and all ERX* registers are implemented as UNDEFINED or RAZ/WI.

- ERRIDR\_EL1.NUM is zero.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [42]

Reserved, RES0.

## ERRSELR\_EL1, bit [41]

## When FEAT\_RAS is implemented:

Trap MSR writes of ERRSELR\_EL1 at EL1 using AArch64 to EL2.

| ERRSELR_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MSR writes of ERRSELR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ERRSELR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

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

## Bit [40]

Reserved, RES0.

## ICC\_IGRPENn\_EL1, bit [39]

## When GICv3 is implemented:

Trap MSR writes of ICC\_IGRPEN&lt;n&gt;\_EL1 at EL1 using AArch64 to EL2.

| ICC_IGRPENn_EL1   | Meaning                                                            |
|-------------------|--------------------------------------------------------------------|
| 0b0               | MSR writes of ICC_IGRPEN<n>_EL1 are not trapped by this mechanism. |

| ICC_IGRPENn_EL1   | Meaning                                                                                                                                                                                                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1               | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ICC_IGRPEN<n>_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VBAR\_EL1, bit [38]

Trap MSR writes of VBAR\_EL1 at EL1 using AArch64 to EL2.

| VBAR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MSR writes of VBAR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of VBAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TTBR1\_EL1, bit [37]

Trap MSR or MSRR writes of TTBR1\_EL1 at EL1 using AArch64 to EL2.

| TTBR1_EL1   | Meaning                                                                                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR and MSRR writes of TTBR1_EL1 are not trapped by this mechanism.                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the write generates a higher priority exception:                                     |
|             | • MSR writes of TTBR1_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MSRR writes of TTBR1_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TTBR0\_EL1, bit [36]

Trap MSR or MSRR writes of TTBR0\_EL1 at EL1 using AArch64 to EL2.

| TTBR0_EL1   | Meaning                                                                                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR and MSRR writes of TTBR0_EL1 are not trapped by this mechanism.                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the write generates a higher priority exception:                                     |
|             | • MSR writes of TTBR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MSRR writes of TTBR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPIDR\_EL0, bit [35]

Trap MSR writes of TPIDR\_EL0 at EL1 and EL0 using AArch64 and MCR writes of TPIDRURW at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| TPIDR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of TPIDR_EL0 at EL1 and EL0 using AArch64 and MCR writes ofTPIDRURW at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                     |
| 0b1         | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the write generates a higher priority exception: • MSR writes of TPIDR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MCR writes of TPIDRURW at EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPIDRRO\_EL0, bit [34]

Trap MSR writes of TPIDRRO\_EL0 at EL1 using AArch64 to EL2.

| TPIDRRO_EL0   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MSR writes of TPIDRRO_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of TPIDRRO_EL0 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPIDR\_EL1, bit [33]

Trap MSR writes of TPIDR\_EL1 at EL1 using AArch64 to EL2.

| TPIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of TPIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of TPIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TCR\_EL1, bit [32]

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- TCR\_EL1.
- TCR2\_EL1, if FEAT\_TCR2 is implemented.

| TCR_EL1   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## SCXTNUM\_EL0, bit [31]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Trap MSR writes of SCXTNUM\_EL0 at EL1 and EL0 using AArch64 to EL2.

| SCXTNUM_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                              |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MSR writes of SCXTNUM_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                         |
| 0b1           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of SCXTNUM_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SCXTNUM\_EL1, bit [30]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Trap MSR writes of SCXTNUM\_EL1 at EL1 using AArch64 to EL2.

| SCXTNUM_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MSR writes of SCXTNUM_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of SCXTNUM_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SCTLR\_EL1, bit [29]

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- SCTLR\_EL1.
- SCTLR2\_EL1, if FEAT\_SCTLR2 is implemented.

| SCTLR_EL1   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [28]

Reserved, RES0.

## PAR\_EL1, bit [27]

Trap MSR or MSRR writes of PAR\_EL1 at EL1 using AArch64 to EL2.

| PAR_EL1   | Meaning                                                                                                                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR and MSRR writes of PAR_EL1 are not trapped by this mechanism.                                                                                                                                                      |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the write generates a higher priority exception:                                 |
|           | • MSR writes of PAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MSRR writes of PAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [26:25]

Reserved, RES0.

## MAIR\_EL1, bit [24]

Trap MSR writes of MAIR\_EL1 at EL1 using AArch64 to EL2.

| MAIR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MSR writes of MAIR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of MAIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## LORSA\_EL1, bit [23]

## When FEAT\_LOR is implemented:

Trap MSR writes of LORSA\_EL1 at EL1 using AArch64 to EL2.

| LORSA_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of LORSA_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of LORSA_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

LORN\_EL1, bit [22]

## When FEAT\_LOR is implemented:

Trap MSR writes of LORN\_EL1 at EL1 using AArch64 to EL2.

| LORN_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MSR writes of LORN_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of LORN_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [21]

Reserved, RES0.

## LOREA\_EL1, bit [20]

## When FEAT\_LOR is implemented:

Trap MSR writes of LOREA\_EL1 at EL1 using AArch64 to EL2.

| LOREA_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of LOREA_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of LOREA_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LORC\_EL1, bit [19]

## When FEAT\_LOR is implemented:

Trap MSR writes of LORC\_EL1 at EL1 using AArch64 to EL2.

| LORC_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MSR writes of LORC_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of LORC_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [18]

Reserved, RES0.

## FAR\_EL1, bit [17]

Trap MSR writes of FAR\_EL1 at EL1 using AArch64 to EL2.

| FAR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of FAR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of FAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ESR\_EL1, bit [16]

Trap MSR writes of ESR\_EL1 at EL1 using AArch64 to EL2.

| ESR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of ESR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of ESR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [15:14]

Reserved, RES0.

## CSSELR\_EL1, bit [13]

Trap MSR writes of CSSELR\_EL1 at EL1 using AArch64 to EL2.

| CSSELR_EL1   | Meaning                                                                                                                                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MSR writes of CSSELR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of CSSELR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CPACR\_EL1, bit [12]

Trap MSR writes of CPACR\_EL1 at EL1 using AArch64 to EL2.

| CPACR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of CPACR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of CPACR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CONTEXTIDR\_EL1, bit [11]

Trap MSR writes of CONTEXTIDR\_EL1 at EL1 using AArch64 to EL2.

| CONTEXTIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | MSR writes of CONTEXTIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1              | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of CONTEXTIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [10:9]

Reserved, RES0.

## APIBKey, bit [8]

## When FEAT\_PAuth is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APIBKeyHi\_EL1.
- APIBKeyLo\_EL1.

| APIBKey   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APIAKey, bit [7]

## When FEAT\_PAuth is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APIAKeyHi\_EL1.
- APIAKeyLo\_EL1.

| APIAKey   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APGAKey, bit [6]

## When FEAT\_PAuth is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APGAKeyHi\_EL1.
- APGAKeyLo\_EL1.

| APGAKey   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APDBKey, bit [5]

## When FEAT\_PAuth is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APDBKeyHi\_EL1.
- APDBKeyLo\_EL1.

| APDBKey   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APDAKey, bit [4]

## When FEAT\_PAuth is implemented:

Trap MSR writes at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APDAKeyHi\_EL1.
- APDAKeyLo\_EL1.

| APDAKey   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MSR writes of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AMAIR\_EL1, bit [3]

Trap MSR writes of AMAIR\_EL1 at EL1 using AArch64 to EL2.

| AMAIR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of AMAIR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of AMAIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [2]

Reserved, RES0.

## AFSR1\_EL1, bit [1]

Trap MSR writes of AFSR1\_EL1 at EL1 using AArch64 to EL2.

| AFSR1_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of AFSR1_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of AFSR1_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## AFSR0\_EL1, bit [0]

Trap MSR writes of AFSR0\_EL1 at EL1 using AArch64 to EL2.

| AFSR0_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MSR writes of AFSR0_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                        |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MSR writes of AFSR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the write generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HFGWTR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, HFGWTR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1C0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HFGWTR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HFGWTR_EL2;
```

MSR HFGWTR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1C0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HFGWTR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HFGWTR_EL2 = X[t, 64];
```