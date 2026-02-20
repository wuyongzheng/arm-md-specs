## D24.2.66 HDFGRTR2\_EL2, Hypervisor Debug Fine-Grained Read Trap Register 2

The HDFGRTR2\_EL2 characteristics are:

## Purpose

Provides controls for traps of MRS and MRC reads of debug, trace, PMU, and Statistical Profiling System registers.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HDFGRTR2\_EL2 are UNDEFINED.

## Attributes

HDFGRTR2\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

Bits [63:25]

Reserved, RES0.

nPMBMAR\_EL1, bit [24]

When FEAT\_SPE\_nVM is implemented:

Trap MRS reads of PMBMAR\_EL1 at EL1 using AArch64 to EL2.

| nPMBMAR_EL1   | Meaning                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, then MRS reads of PMBMAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |

0b1

MRS reads of PMBMAR\_EL1 are not trapped by this mechanism.

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nMDSTEPOP\_EL1, bit [23]

## When FEAT\_STEP2 is implemented:

Trap MRS reads of MDSTEPOP\_EL1 at EL1 using AArch64 to EL2.

| nMDSTEPOP_EL1   | Meaning                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then MRS reads of MDSTEPOP_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1             | MRS reads of MDSTEPOP_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nTRBMPAM\_EL1, bit [22]

When FEAT\_TRBE\_MPAM is implemented:

Trap MRS reads of TRBMPAM\_EL1 at EL1 using AArch64 to EL2.

| nTRBMPAM_EL1   | Meaning                                                                                                                                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, then MRS reads of TRBMPAM_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1            | MRS reads of TRBMPAM_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [21]

Reserved, RES0.

## nTRCITECR\_EL1, bit [20]

## When FEAT\_ITE is implemented:

Trap MRS reads of TRCITECR\_EL1 at EL1 using AArch64 to EL2.

| nTRCITECR_EL1   | Meaning                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, then MRS reads of TRCITECR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1             | MRS reads of TRCITECR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMSDSFR\_EL1, bit [19]

## When FEAT\_SPE\_FDS is implemented:

Trap MRS reads of PMSDSFR\_EL1 at EL1 using AArch64 to EL2.

| nPMSDSFR_EL1   | Meaning                                                                                                                                                                                                                                  |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, then MRS reads of PMSDSFR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1            | MRS reads of PMSDSFR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMDEVAFF\_EL1, bit [18]

## When FEAT\_SPMU is implemented:

Trap MRS reads of SPMDEVAFF\_EL1 at EL1 using AArch64 to EL2.

| nSPMDEVAFF_EL1   | Meaning                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, then MRS reads of SPMDEVAFF_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1              | MRS reads of SPMDEVAFF_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMID, bit [17]

## When FEAT\_SPMU is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- SPMCFGR\_EL1.
- SPMCGCR&lt;n&gt;\_EL1.
- SPMDEVARCH\_EL1.
- SPMIIDR\_EL1.

| nSPMID   | Meaning                                                                                                                                                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | If EL2 is implemented and enabled in the current Security state, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1      | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                     |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMSCR\_EL1, bit [16]

## When FEAT\_SPMU is implemented:

Trap MRS reads of SPMSCR\_EL1 at EL1 using AArch64 to EL2.

| nSPMSCR_EL1   | Meaning                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, then MRS reads of SPMSCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of SPMSCR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMACCESSR\_EL1, bit [15]

## When FEAT\_SPMU is implemented:

Trap MRS reads of SPMACCESSR\_EL1 at EL1 using AArch64 to EL2.

| nSPMACCESSR_EL1   | Meaning                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, then MRS reads of SPMACCESSR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1               | MRS reads of SPMACCESSR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMCR\_EL0, bit [14]

## When FEAT\_SPMU is implemented:

Trap MRS reads of SPMCR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nSPMCR_EL0   | Meaning                                                                                                                                                                                                                                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads of SPMCR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of SPMCR_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                   |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMOVS, bit [13]

## When FEAT\_SPMU is implemented:

Trap MRS reads at EL1 and EL0 using AArch64 of any of the following AArch64 System registers to EL2:

- SPMOVSCLR\_EL0.
- SPMOVSSET\_EL0.

| nSPMOVS   | Meaning                                                                                                                                                                                                                                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads at EL1 and EL0 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1       | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                                          |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMINTEN, bit [12]

## When FEAT\_SPMU is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- SPMINTENCLR\_EL1.
- SPMINTENSET\_EL1.

| nSPMINTEN   | Meaning                                                                                                                                                                                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If EL2 is implemented and enabled in the current Security state, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1         | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                     |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMCNTEN, bit [11]

## When FEAT\_SPMU is implemented:

Trap MRS reads at EL1 and EL0 using AArch64 of any of the following AArch64 System registers to EL2:

- SPMCNTENCLR\_EL0.
- SPMCNTENSET\_EL0.

| nSPMCNTEN   | Meaning                                                                                                                                                                                                                                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads at EL1 and EL0 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1         | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                                          |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMSELR\_EL0, bit [10]

## When FEAT\_SPMU is implemented:

Trap

MRS reads of SPMSELR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nSPMSELR_EL0   | Meaning                                                                                                                                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads of SPMSELR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1            | MRS reads of SPMSELR_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                   |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMEVTYPERn\_EL0, bit [9]

## When FEAT\_SPMU is implemented:

Trap MRS reads at EL1 and EL0 using AArch64 of any of the following AArch64 System registers to EL2:

- SPMEVTYPER&lt;n&gt;\_EL0.
- SPMEVFILTR&lt;n&gt;\_EL0.
- SPMEVFILT2R&lt;n&gt;\_EL0.

| nSPMEVTYPERn_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0                | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads at EL1 and EL0 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1                | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                                                                                          |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nSPMEVCNTRn\_EL0, bit [8]

## When FEAT\_SPMU is implemented:

Trap MRS reads of SPMEVCNTR&lt;n&gt;\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nSPMEVCNTRn_EL0   | Meaning                                                                                                                                                                                                                                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0               | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads of SPMEVCNTR<n>_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1               | MRS reads of SPMEVCNTR<n>_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                   |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMSSCR\_EL1, bit [7]

## When FEAT\_PMUv3\_SS is implemented:

Trap MRS reads of PMSSCR\_EL1 at EL1 using AArch64 to EL2.

| nPMSSCR_EL1   | Meaning                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, then MRS reads of PMSSCR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of PMSSCR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMSSDATA, bit [6]

## When FEAT\_PMUv3\_SS is implemented:

Trap MRS reads at EL1 using AArch64 of any of the following AArch64 System registers to EL2:

- PMCCNTSVR\_EL1.
- PMEVCNTSVR&lt;n&gt;\_EL1.

- PMICNTSVR\_EL1, if FEAT\_PMUv3\_ICNTR is implemented.

| nPMSSDATA   | Meaning                                                                                                                                                                                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If EL2 is implemented and enabled in the current Security state, then MRS reads at EL1 using AArch64 of any of the specified System registers are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1         | MRS reads of the specified System registers are not trapped by this mechanism.                                                                                                                                                                                     |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nMDSELR\_EL1, bit [5]

When FEAT\_Debugv8p9 is implemented:

Trap MRS reads of MDSELR\_EL1 at EL1 using AArch64 to EL2.

| nMDSELR_EL1   | Meaning                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, then MRS reads of MDSELR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of MDSELR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

It is IMPLEMENTATION DEFINED whether this field is implemented or is RES0 when 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMUACR\_EL1, bit [4]

## When FEAT\_PMUv3p9 is implemented:

Trap MRS reads of PMUACR\_EL1 at EL1 using AArch64 to EL2.

| nPMUACR_EL1   | Meaning                                                                                                                                                                                                                                 |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, then MRS reads of PMUACR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1           | MRS reads of PMUACR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMICFILTR\_EL0, bit [3]

## When FEAT\_PMUv3\_ICNTR is implemented:

Trap MRS reads of PMICFILTR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nPMICFILTR_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then: • MRS reads of PMICFILTR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. • PMCNTENCLR_EL0.F0, PMCNTENSET_EL0.F0, PMOVSCLR_EL0.F0, and PMOVSSET_EL0.F0 read as zero at EL1 and EL0. • PMINTENCLR_EL1.F0 and PMINTENSET_EL1.F0 read as zero at EL1. |
| 0b1              | MRS reads of PMICFILTR_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                               |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMICNTR\_EL0, bit [2]

## When FEAT\_PMUv3\_ICNTR is implemented:

Trap MRS reads of PMICNTR\_EL0 at EL1 and EL0 using AArch64 to EL2.

| nPMICNTR_EL0   | Meaning                                                                                                                                                                                                                                                                                                       |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then MRS reads of PMICNTR_EL0 at EL1 and EL0 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1            | MRS reads of PMICNTR_EL0 are not trapped by this mechanism.                                                                                                                                                                                                                                                   |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMIAR\_EL1, bit [1]

## When FEAT\_SEBEP is implemented:

Trap MRS reads of PMIAR\_EL1 at EL1 using AArch64 to EL2.

| nPMIAR_EL1   | Meaning                                                                                                                                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, then MRS reads of PMIAR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of PMIAR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nPMECR\_EL1, bit [0]

## When FEAT\_EBEP is implemented or FEAT\_PMUv3\_SS is implemented:

Trap MRS reads of PMECR\_EL1 at EL1 using AArch64 to EL2.

| nPMECR_EL1   | Meaning                                                                                                                                                                                                                                |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | If EL2 is implemented and enabled in the current Security state, then MRS reads of PMECR_EL1 at EL1 using AArch64 are trapped to EL2 and reported with EC syndrome value 0x18 , unless the read generates a higher priority exception. |
| 0b1          | MRS reads of PMECR_EL1 are not trapped by this mechanism.                                                                                                                                                                              |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing HDFGRTR2\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HDFGRTR2\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1A0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HDFGRTR2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HDFGRTR2_EL2;
```

```
then
```

MSR HDFGRTR2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1A0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HDFGRTR2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HDFGRTR2_EL2 = X[t, 64];
```