## D24.2.73 HFGRTR\_EL2, Hypervisor Fine-Grained Read Trap Register

The HFGRTR\_EL2 characteristics are:

## Purpose

Provides controls for traps of MRRS , MRS and MRC reads of System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HFGRTR\_EL2 are UNDEFINED.

## Attributes

HFGRTR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## nAMAIR2\_EL1, bit [63]

## When FEAT\_AIE is implemented:

Trap MRS reads of AMAIR2\_EL1 at EL1 using AArch64 to EL2.

| nAMAIR2_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of AMAIR2_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of AMAIR2_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nMAIR2\_EL1, bit [62]

When FEAT\_AIE is implemented:

Trap MRS reads of MAIR2\_EL1 at EL1 using AArch64 to EL2.

| nMAIR2_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of MAIR2_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of MAIR2_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nS2POR\_EL1, bit [61]

## When FEAT\_S2POE is implemented:

Trap MRS reads of S2POR\_EL1 at EL1 using AArch64 to EL2.

| nS2POR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of S2POR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of S2POR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPOR\_EL1, bit [60]

## When FEAT\_S1POE is implemented:

Trap MRS reads of POR\_EL1 at EL1 using AArch64 to EL2.

| nPOR_EL1   | Meaning                                                                                                                                                                                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of POR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1        | MRS reads of POR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPOR\_EL0, bit [59]

## When FEAT\_S1POE is implemented:

Trap MRS reads of POR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nPOR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of POR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

| nPOR_EL0   | Meaning                                                 |
|------------|---------------------------------------------------------|
| 0b1        | MRS reads of POR_EL0 are not trapped by this mechanism. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nPIR\_EL1, bit [58]

## When FEAT\_S1PIE is implemented:

Trap MRS reads of PIR\_EL1 at EL1 using AArch64 to EL2.

| nPIR_EL1   | Meaning                                                                                                                                                                                                                                                                                       |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1        | MRS reads of PIR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPIRE0\_EL1, bit [57]

## When FEAT\_S1PIE is implemented:

Trap MRS reads of PIRE0\_EL1 at EL1 using AArch64 to EL2.

| nPIRE0_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of PIRE0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of PIRE0_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nRCWMASK\_EL1,bit [56]

When FEAT\_THE is implemented:

Trap MRS or MRRS reads of RCWMASK\_EL1 at EL1 using AArch64 to EL2.

| nRCWMASK_EL1   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of RCWMASK_EL1at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRRS reads of RCWMASK_EL1at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |
| 0b1            | MRS and MRRS reads of RCWMASK_EL1are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

nTPIDR2\_EL0, bit [55]

## When FEAT\_SME is implemented:

Trap MRS reads of TPIDR2\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nTPIDR2_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TPIDR2_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of TPIDR2_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSMPRI\_EL1, bit [54]

## When FEAT\_SME is implemented:

Trap MRS reads of SMPRI\_EL1 at EL1 using AArch64 to EL2.

| nSMPRI_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of SMPRI_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of SMPRI_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCS\_EL1, bit [53]

## When FEAT\_GCS is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- GCSCR\_EL1.
- GCSPR\_EL1.

| nGCS_EL1   | Meaning                                                                                                                                                                                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1        | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCS\_EL0, bit [52]

## When FEAT\_GCS is implemented:

Trap MRS reads at EL1 and EL0 using AArch64 of any of the following AArch64 System registers to EL2:

- GCSCRE0\_EL1, at EL1 only.

- GCSPR\_EL0.

| nGCS_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 and EL0 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1        | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                               |

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

Trap MRS reads of ACCDATA\_EL1 at EL1 using AArch64 to EL2.

| nACCDATA_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ACCDATA_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1            | MRS reads of ACCDATA_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ERXADDR\_EL1, bit [49]

## When FEAT\_RAS is implemented:

Trap MRS reads of ERXADDR\_EL1 at EL1 using AArch64 to EL2.

| ERXADDR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of ERXADDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXADDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

Trap MRS reads of ERXPFGCDN\_EL1 at EL1 using AArch64 to EL2.

| ERXPFGCDN_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of ERXPFGCDN_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXPFGCDN_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

Trap MRS reads of ERXPFGCTL\_EL1 at EL1 using AArch64 to EL2.

| ERXPFGCTL_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of ERXPFGCTL_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXPFGCTL_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

## ERXPFGF\_EL1, bit [46]

## When FEAT\_RASv1p1 is implemented:

Trap

MRS reads of ERXPFGF\_EL1 at EL1 using AArch64 to EL2.

| ERXPFGF_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of ERXPFGF_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXPFGF_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

## ERXMISCn\_EL1, bit [45]

## When FEAT\_RAS is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- ERXMISC0\_EL1.
- ERXMISC1\_EL1.
- ERXMISC2\_EL1.
- ERXMISC3\_EL1.

| ERXMISCn_EL1   | Meaning                                                                                                                                                                                                                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

Trap MRS reads of ERXSTATUS\_EL1 at EL1 using AArch64 to EL2.

| ERXSTATUS_EL1   | Meaning                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | MRS reads of ERXSTATUS_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXSTATUS_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

Trap MRS reads of ERXCTLR\_EL1 at EL1 using AArch64 to EL2.

| ERXCTLR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of ERXCTLR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXCTLR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

## ERXFR\_EL1, bit [42]

## When FEAT\_RAS is implemented:

Trap MRS reads of ERXFR\_EL1 at EL1 using AArch64 to EL2.

| ERXFR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of ERXFR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERXFR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

## ERRSELR\_EL1, bit [41]

## When FEAT\_RAS is implemented:

Trap MRS reads of ERRSELR\_EL1 at EL1 using AArch64 to EL2.

| ERRSELR_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of ERRSELR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERRSELR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

## ERRIDR\_EL1, bit [40]

## When FEAT\_RAS is implemented:

Trap MRS reads of ERRIDR\_EL1 at EL1 using AArch64 to EL2.

| ERRIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of ERRIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ERRIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

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

## ICC\_IGRPENn\_EL1, bit [39]

## When GICv3 is implemented:

Trap MRS reads of ICC\_IGRPEN&lt;n&gt;\_EL1 at EL1 using AArch64 to EL2.

| ICC_IGRPENn_EL1   | Meaning                                                                                                                                                                                                                                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | MRS reads of ICC_IGRPEN<n>_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1               | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ICC_IGRPEN<n>_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VBAR\_EL1, bit [38]

Trap MRS reads of VBAR\_EL1 at EL1 using AArch64 to EL2.

| VBAR_EL1   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of VBAR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of VBAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TTBR1\_EL1, bit [37]

Trap MRS or MRRS reads of TTBR1\_EL1 at EL1 using AArch64 to EL2.

| TTBR1_EL1   | Meaning                                                                                                                                                                                                                  |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS and MRRS reads of TTBR1_EL1 are not trapped by this mechanism.                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception:                                    |
|             | • MRS reads of TTBR1_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRRS reads of TTBR1_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TTBR0\_EL1, bit [36]

Trap MRS or MRRS reads of TTBR0\_EL1 at EL1 using AArch64 to EL2.

| TTBR0_EL1   | Meaning                                                                                                                                                                                                                  |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS and MRRS reads of TTBR0_EL1 are not trapped by this mechanism.                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception:                                    |
|             | • MRS reads of TTBR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRRS reads of TTBR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPIDR\_EL0, bit [35]

Trap MRS reads of TPIDR\_EL0 at EL1 and EL0 using AArch64 and MRC reads of TPIDRURW at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| TPIDR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TPIDR_EL0 at EL1 and EL0 using AArch64 and MRC reads of TPIDRURW at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1         | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of TPIDR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of TPIDRURW at EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPIDRRO\_EL0, bit [34]

Trap MRS reads of TPIDRRO\_EL0 at EL1 and EL0 using AArch64 and MRC reads of TPIDRURO at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| TPIDRRO_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of TPIDRRO_EL0 at EL1 and EL0 using AArch64 and MRC reads of TPIDRURO at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                   |
| 0b1           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception: • MRS reads of TPIDRRO_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRC reads of TPIDRURO at EL0 using AArch32 when EL1 is using AArch64 are trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPIDR\_EL1, bit [33]

Trap MRS reads of TPIDR\_EL1 at EL1 using AArch64 to EL2.

| TPIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of TPIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of TPIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TCR\_EL1, bit [32]

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- TCR\_EL1.
- TCR2\_EL1, if FEAT\_TCR2 is implemented.

| TCR_EL1   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## SCXTNUM\_EL0, bit [31]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Trap MRS reads of SCXTNUM\_EL0 at EL1 and EL0 using AArch64 to EL2.

| SCXTNUM_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of SCXTNUM_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                        |
| 0b1           | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of SCXTNUM_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SCXTNUM\_EL1, bit [30]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Trap MRS reads of SCXTNUM\_EL1 at EL1 using AArch64 to EL2.

| SCXTNUM_EL1   | Meaning                                                                                                                                                                                                                                                                                           |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | MRS reads of SCXTNUM_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of SCXTNUM_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SCTLR\_EL1, bit [29]

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- SCTLR\_EL1.
- SCTLR2\_EL1, if FEAT\_SCTLR2 is implemented.

| SCTLR_EL1   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## REVIDR\_EL1, bit [28]

Trap MRS reads of REVIDR\_EL1 at EL1 using AArch64 to EL2.

| REVIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of REVIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of REVIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## PAR\_EL1, bit [27]

Trap MRS or MRRS reads of PAR\_EL1 at EL1 using AArch64 to EL2.

| PAR_EL1   | Meaning                                                                                                                                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS and MRRS reads of PAR_EL1 are not trapped by this mechanism.                                                                                                                                                     |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the read generates a higher priority exception:                                |
|           | • MRS reads of PAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 . • MRRS reads of PAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x14 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## MPIDR\_EL1, bit [26]

Trap MRS reads of MPIDR\_EL1 at EL1 using AArch64 to EL2.

| MPIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of MPIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of MPIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## MIDR\_EL1, bit [25]

Trap MRS reads of MIDR\_EL1 at EL1 using AArch64 to EL2.

| MIDR_EL1   | Meaning                                                  |
|------------|----------------------------------------------------------|
| 0b0        | MRS reads of MIDR_EL1 are not trapped by this mechanism. |

| MIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of MIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## MAIR\_EL1, bit [24]

Trap MRS reads of MAIR\_EL1 at EL1 using AArch64 to EL2.

| MAIR_EL1   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of MAIR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of MAIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## LORSA\_EL1, bit [23]

## When FEAT\_LOR is implemented:

Trap MRS reads of LORSA\_EL1 at EL1 using AArch64 to EL2.

| LORSA_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of LORSA_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of LORSA_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LORN\_EL1, bit [22]

## When FEAT\_LOR is implemented:

Trap MRS reads of LORN\_EL1 at EL1 using AArch64 to EL2.

| LORN_EL1   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of LORN_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of LORN_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

LORID\_EL1, bit [21]

## When FEAT\_LOR is implemented:

Trap MRS reads of LORID\_EL1 at EL1 using AArch64 to EL2.

| LORID_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of LORID_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of LORID_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

LOREA\_EL1, bit [20]

## When FEAT\_LOR is implemented:

Trap MRS reads of LOREA\_EL1 at EL1 using AArch64 to EL2.

| LOREA_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of LOREA_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of LOREA_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

LORC\_EL1, bit [19]

## When FEAT\_LOR is implemented:

Trap MRS reads of LORC\_EL1 at EL1 using AArch64 to EL2.

| LORC_EL1   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of LORC_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of LORC_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ISR\_EL1, bit [18]

Trap MRS reads of ISR\_EL1 at EL1 using AArch64 to EL2.

| ISR_EL1   | Meaning                                                                                                                                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of ISR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ISR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## FAR\_EL1, bit [17]

Trap MRS reads of FAR\_EL1 at EL1 using AArch64 to EL2.

| FAR_EL1   | Meaning                                                                                                                                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of FAR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of FAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ESR\_EL1, bit [16]

Trap MRS reads of ESR\_EL1 at EL1 using AArch64 to EL2.

| ESR_EL1   | Meaning                                                                                                                                                                                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of ESR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of ESR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCZID\_EL0, bit [15]

Trap MRS reads of DCZID\_EL0 at EL1 and EL0 using AArch64 to EL2.

| DCZID_EL0   | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| 0b0         | MRS reads of DCZID_EL0 are not trapped by this mechanism. |

| DCZID_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1         | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of DCZID_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CTR\_EL0, bit [14]

Trap MRS reads of CTR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| CTR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of CTR_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of CTR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CSSELR\_EL1, bit [13]

Trap MRS reads of CSSELR\_EL1 at EL1 using AArch64 to EL2.

| CSSELR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of CSSELR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of CSSELR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CPACR\_EL1, bit [12]

Trap MRS reads of CPACR\_EL1 at EL1 using AArch64 to EL2.

| CPACR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of CPACR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of CPACR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CONTEXTIDR\_EL1, bit [11]

Trap MRS reads of CONTEXTIDR\_EL1 at EL1 using AArch64 to EL2.

| CONTEXTIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | MRS reads of CONTEXTIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1              | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of CONTEXTIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CLIDR\_EL1, bit [10]

Trap MRS reads of CLIDR\_EL1 at EL1 using AArch64 to EL2.

| CLIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of CLIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of CLIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CCSIDR\_EL1, bit [9]

Trap MRS reads of CCSIDR\_EL1 at EL1 using AArch64 to EL2.

| CCSIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MRS reads of CCSIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of CCSIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## APIBKey, bit [8]

## When FEAT\_PAuth is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APIBKeyHi\_EL1.
- APIBKeyLo\_EL1.

| APIBKey   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APIAKey, bit [7]

## When FEAT\_PAuth is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APIAKeyHi\_EL1.
- APIAKeyLo\_EL1.

| APIAKey   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APGAKey, bit [6]

## When FEAT\_PAuth is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APGAKeyHi\_EL1.
- APGAKeyLo\_EL1.

| APGAKey   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APDBKey, bit [5]

## When FEAT\_PAuth is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APDBKeyHi\_EL1.
- APDBKeyLo\_EL1.

| APDBKey   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APDAKey, bit [4]

## When FEAT\_PAuth is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- APDAKeyHi\_EL1.
- APDAKeyLo\_EL1.

| APDAKey   | Meaning                                                                                                                                                                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AMAIR\_EL1, bit [3]

Trap MRS reads of AMAIR\_EL1 at EL1 using AArch64 to EL2.

| AMAIR_EL1   | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| 0b0         | MRS reads of AMAIR_EL1 are not trapped by this mechanism. |

| AMAIR_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of AMAIR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## AIDR\_EL1, bit [2]

Trap MRS reads of AIDR\_EL1 at EL1 using AArch64 to EL2.

| AIDR_EL1   | Meaning                                                                                                                                                                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | MRS reads of AIDR_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of AIDR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## AFSR1\_EL1, bit [1]

Trap MRS reads of AFSR1\_EL1 at EL1 using AArch64 to EL2.

| AFSR1_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of AFSR1_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of AFSR1_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## AFSR0\_EL1, bit [0]

Trap MRS reads of AFSR0\_EL1 at EL1 using AArch64 to EL2.

| AFSR0_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MRS reads of AFSR0_EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                       |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then MRS reads of AFSR0_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HFGRTR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HFGRTR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1B8]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HFGRTR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HFGRTR_EL2;
```

MSR HFGRTR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1B8] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HFGRTR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HFGRTR_EL2 = X[t, 64];
```