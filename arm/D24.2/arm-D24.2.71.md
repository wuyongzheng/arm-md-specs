## D24.2.71 HFGITR\_EL2, Hypervisor Fine-Grained Instruction Trap Register

The HFGITR\_EL2 characteristics are:

## Purpose

Provides instruction trap controls.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HFGITR\_EL2 are UNDEFINED.

## Attributes

HFGITR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## PSBCSYNC, bit [63]

## When FEAT\_SPEv1p5 is implemented:

Trap execution of PSB CSYNC at EL1 and EL0 using AArch64 to EL2.

| PSBCSYNC   | Meaning                                                                                                                                                                                                                                                                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution of PSB CSYNCis not trapped by this mechanism.                                                                                                                                                                                                                                                                                                             |
| 0b1        | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of PSB CSYNCat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x0A , unless the instruction generates higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATS1E1A, bit [62]

## When FEAT\_ATS1A is implemented:

Trap execution of AT S1E1A at EL1 using AArch64 to EL2.

| ATS1E1A   | Meaning                                                                                                                                                                                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of AT S1E1A is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E1A at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [61]

Reserved, RES0.

## COSPRCTX, bit [60]

When FEAT\_SPECRES2 is implemented:

Trap execution of COSP RCTX at EL1 and EL0 using AArch64 and execution of COSPRCTX at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| COSPRCTX   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution of COSP RCTXat EL1 and EL0 using AArch64 and execution of COSPRCTX at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                        |
| 0b1        | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the instruction generates a higher priority exception: • Execution of COSP RCTXat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 . • Execution of COSPRCTX at EL0 using AArch32 when EL1 is using AArch64 is trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCSEPP, bit [59]

## When FEAT\_GCS is implemented:

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- GCSPUSHX .
- GCSPOPCX .

| nGCSEPP   | Meaning                                                                                                                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |
| 0b1       | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                     |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCSSTR\_EL1, bit [58]

## When FEAT\_GCS is implemented:

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- GCSSTR .
- GCSSTTR when PSTATE.UAO is 1.
- GCSSTTR when the Effective value of HCR\_EL2.{NV, NV1} is {1, 1}.

| nGCSSTR_EL1   | Meaning                                                                                                                                                                                                                                                                                                                  |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 using AArch64 of any of the specified instructions generates a GCS exception with EC syndrome value 0x2D , unless the instruction generates a higher priority exception. |
| 0b1           | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                |

## The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nGCSPUSHM\_EL1, bit [57]

## When FEAT\_GCS is implemented:

Trap execution of GCSPUSHM at EL1 using AArch64 to EL2.

| nGCSPUSHM_EL1   | Meaning                                                                                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of GCSPUSHM at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |
| 0b1             | Execution of GCSPUSHM is not trapped by this mechanism.                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nBRBIALL, bit [56]

## When FEAT\_BRBE is implemented:

Trap execution of BRB IALL at EL1 using AArch64 to EL2.

| nBRBIALL   | Meaning                                                                                                                                                                                                                                                                                             |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of BRBIALL at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |
| 0b1        | Execution of BRBIALL is not trapped by this mechanism.                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## nBRBINJ, bit [55]

## When FEAT\_BRBE is implemented:

Trap execution of BRB INJ at EL1 using AArch64 to EL2.

| nBRBINJ   | Meaning                                                                                                                                                                                                                                                                                            |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of BRBINJ at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |
| 0b1       | Execution of BRBINJ is not trapped by this mechanism.                                                                                                                                                                                                                                              |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DCCVAC, bit [54]

Trap execution of any of the following AArch64 instructions at EL1 and EL0 to EL2:

- DCCVAC.
- DCCGVAC, if FEAT\_MTE is implemented.
- DCCGDVAC,if FEAT\_MTE is implemented.
- DCCVAOC, if FEAT\_OCCMO is implemented.
- DCCGDVAOC,if FEAT\_OCCMO is implemented.

| DCCVAC   | Meaning                                                                   |
|----------|---------------------------------------------------------------------------|
| 0b0      | Execution of the specified instructions is not trapped by this mechanism. |

| DCCVAC   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1      | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution at EL1 and EL0 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## SVC\_EL1, bit [53]

Trap execution of SVC at EL1 using AArch64 to EL2.

| SVC_EL1   | Meaning                                                                                                                                                                                                                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of SVC is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of SVC at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x15 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## SVC\_EL0, bit [52]

Trap execution of SVC at EL0 using AArch64 and execution of SVC at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| SVC_EL0   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of SVC at EL0 using AArch64 and execution of SVC at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the instruction generates a higher priority exception: • Execution of SVC at EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x15 . • Execution of SVC at EL0 using AArch32 when EL1 is using AArch64 is trapped to EL2 and reported with EC syndrome value 0x11 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .

- Otherwise, this field resets to an architecturally UNKNOWN value.

## ERET, bit [51]

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- ERET .
- ERETAA , if FEAT\_PAuth is implemented.
- ERETAB , if FEAT\_PAuth is implemented.

| ERET   | Meaning                                                                                                                                                                                                                                                                                                                       |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                     |
| 0b1    | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x1A , unless the instruction generates a higher priority exception. |

If EL2 is implemented and enabled in the current Security state, HCR\_EL2.API == 0, and this field enables a fine-grained trap on the instruction, then execution at EL1 using AArch64 of ERETAA or ERETAB instructions is trapped to EL2 and reported with EC syndrome value 0x1A with its associated ISS field, as the fine-grained trap has higher priority than the trap enabled by HCR\_EL2.API == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## CPPRCTX, bit [50]

## When FEAT\_SPECRES is implemented:

Trap execution of CPP RCTX at EL1 and EL0 using AArch64 and execution of CPPRCTX at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| CPPRCTX   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of CPP RCTXat EL1 and EL0 using AArch64 and execution of CPPRCTX at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the instruction generates a higher priority exception: • Execution of CPP RCTXat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 . • Execution of CPPRCTX at EL0 using AArch32 when EL1 is using AArch64 is trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DVPRCTX, bit [49]

## When FEAT\_SPECRES is implemented:

Trap execution of DVP RCTX at EL1 and EL0 using AArch64 and execution of DVPRCTX at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| DVPRCTX   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of DVPRCTXat EL1 and EL0 using AArch64 and execution of DVPRCTXat EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the instruction generates a higher priority exception: • Execution of DVPRCTXat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 . • Execution of DVPRCTXat EL0 using AArch32 when EL1 is using AArch64 is trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CFPRCTX, bit [48]

## When FEAT\_SPECRES is implemented:

Trap execution of CFP RCTX at EL1 and EL0 using AArch64 and execution of CFPRCTX at EL0 using AArch32 when EL1 is using AArch64 to EL2.

| CFPRCTX   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of CFP RCTXat EL1 and EL0 using AArch64 and execution of CFPRCTX at EL0 using AArch32 are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                                        |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then unless the instruction generates a higher priority exception: • Execution of CFP RCTXat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 . • Execution of CFPRCTX at EL0 using AArch32 when EL1 is using AArch64 is trapped to EL2 and reported with EC syndrome value 0x03 . |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVAALE1, bit [47]

Trap execution of TLBI VAALE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAALE1NXS.

| TLBIVAALE1   | Meaning                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Execution of TLBI VAALE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAALE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVALE1, bit [46]

Trap execution of TLBI VALE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VALE1NXS.

| TLBIVALE1   | Meaning                                                                                                                                                                                                                                                                                                |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Execution of TLBI VALE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VALE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVAAE1, bit [45]

Trap execution of TLBI VAAE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAAE1NXS.

| TLBIVAAE1   | Meaning                                                   |
|-------------|-----------------------------------------------------------|
| 0b0         | Execution of TLBI VAAE1 is not trapped by this mechanism. |

| TLBIVAAE1   | Meaning                                                                                                                                                                                                                                                                                                |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAAE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIASIDE1, bit [44]

Trap execution of TLBI ASIDE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI ASIDE1NXS.

| TLBIASIDE1   | Meaning                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Execution of TLBI ASIDE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI ASIDE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVAE1, bit [43]

Trap execution of TLBI VAE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAE1NXS.

| TLBIVAE1   | Meaning                                                                                                                                                                                                                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution of TLBI VAE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVMALLE1, bit [42]

Trap execution of TLBI VMALLE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VMALLE1NXS.

| TLBIVMALLE1   | Meaning                                                                                                                                                                                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI VMALLE1is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VMALLE1at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIRVAALE1, bit [41]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVAALE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAALE1NXS.

| TLBIRVAALE1   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI RVAALE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAALE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVALE1, bit [40]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVALE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVALE1NXS.

| TLBIRVALE1   | Meaning                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Execution of TLBI RVALE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVALE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAAE1, bit [39]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVAAE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAAE1NXS.

| TLBIRVAAE1   | Meaning                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Execution of TLBI RVAAE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAAE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAE1, bit [38]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVAE1 at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAE1NXS.

| TLBIRVAE1   | Meaning                                                                                                                                                                                                                                                                                                |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Execution of TLBI RVAE1 is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAE1 at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAALE1IS, bit [37]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVAALE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAALE1ISNXS.

| TLBIRVAALE1IS   | Meaning                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Execution of TLBI RVAALE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAALE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVALE1IS, bit [36]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVALE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVALE1ISNXS.

| TLBIRVALE1IS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI RVALE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVALE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAAE1IS, bit [35]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVAAE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAAE1ISNXS.

| TLBIRVAAE1IS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI RVAAE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAAE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAE1IS, bit [34]

## When FEAT\_TLBIRANGE is implemented:

Trap execution of TLBI RVAE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAE1ISNXS.

| TLBIRVAE1IS   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI RVAE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVAALE1IS, bit [33]

Trap execution of TLBI VAALE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAALE1ISNXS.

| TLBIVAALE1IS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI VAALE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAALE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVALE1IS, bit [32]

Trap execution of TLBI VALE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VALE1ISNXS.

| TLBIVALE1IS   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI VALE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VALE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVAAE1IS, bit [31]

Trap execution of TLBI VAAE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAAE1ISNXS.

| TLBIVAAE1IS   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI VAAE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAAE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIASIDE1IS, bit [30]

Trap execution of TLBI ASIDE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI ASIDE1ISNXS.

| TLBIASIDE1IS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI ASIDE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI ASIDE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVAE1IS, bit [29]

Trap execution of TLBI VAE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAE1ISNXS.

| TLBIVAE1IS   | Meaning                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Execution of TLBI VAE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIVMALLE1IS, bit [28]

Trap execution of TLBI VMALLE1IS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VMALLE1ISNXS.

| TLBIVMALLE1IS   | Meaning                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Execution of TLBI VMALLE1IS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VMALLE1IS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TLBIRVAALE1OS, bit [27]

## When FEAT\_TLBIRANGE is implemented and FEAT\_TLBIOS is implemented:

Trap execution of TLBI RVAALE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAALE1OSNXS.

| TLBIRVAALE1OS   | Meaning                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Execution of TLBI RVAALE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAALE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVALE1OS, bit [26]

## When FEAT\_TLBIRANGE is implemented and FEAT\_TLBIOS is implemented:

Trap execution of TLBI RVALE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVALE1OSNXS.

| TLBIRVALE1OS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI RVALE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVALE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAAE1OS, bit [25]

## When FEAT\_TLBIRANGE is implemented and FEAT\_TLBIOS is implemented:

Trap execution of TLBI RVAAE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAAE1OSNXS.

| TLBIRVAAE1OS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI RVAAE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAAE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIRVAE1OS, bit [24]

## When FEAT\_TLBIRANGE is implemented and FEAT\_TLBIOS is implemented:

Trap execution of TLBI RVAE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI RVAE1OSNXS.

| TLBIRVAE1OS   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI RVAE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI RVAE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVAALE1OS, bit [23]

## When FEAT\_TLBIOS is implemented:

Trap execution of TLBI VAALE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAALE1OSNXS.

| TLBIVAALE1OS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI VAALE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAALE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVALE1OS, bit [22]

## When FEAT\_TLBIOS is implemented:

Trap execution of TLBI VALE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VALE1OSNXS.

| TLBIVALE1OS   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI VALE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VALE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVAAE1OS, bit [21]

## When FEAT\_TLBIOS is implemented:

Trap execution of TLBI VAAE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAAE1OSNXS.

| TLBIVAAE1OS   | Meaning                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Execution of TLBI VAAE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1           | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAAE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIASIDE1OS, bit [20]

## When FEAT\_TLBIOS is implemented:

Trap execution of TLBI ASIDE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI ASIDE1OSNXS.

| TLBIASIDE1OS   | Meaning                                                                                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0            | Execution of TLBI ASIDE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1            | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI ASIDE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVAE1OS, bit [19]

## When FEAT\_TLBIOS is implemented:

Trap execution of TLBI VAE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VAE1OSNXS.

| TLBIVAE1OS   | Meaning                                                                                                                                                                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Execution of TLBI VAE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1          | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VAE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLBIVMALLE1OS, bit [18]

## When FEAT\_TLBIOS is implemented:

Trap execution of TLBI VMALLE1OS at EL1 using AArch64 to EL2.

If FEAT\_XS is implemented and HCRX\_EL2.FGTnXS == 0, this field also traps execution of TLBI VMALLE1OSNXS.

| TLBIVMALLE1OS   | Meaning                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Execution of TLBIVMALLE1OS is not trapped by this mechanism.                                                                                                                                                                                                                                               |
| 0b1             | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of TLBI VMALLE1OS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATS1E1WP, bit [17]

## When FEAT\_PAN2 is implemented:

Trap execution of AT S1E1WP at EL1 using AArch64 to EL2.

| ATS1E1WP   | Meaning                                                                                                                                                                                                                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution of AT S1E1WP is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E1WP at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATS1E1RP, bit [16]

## When FEAT\_PAN2 is implemented:

Trap execution of AT S1E1RP at EL1 using AArch64 to EL2.

| ATS1E1RP   | Meaning                                                                                                                                                                                                                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution of AT S1E1RP is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E1RP at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATS1E0W, bit [15]

Trap execution of AT S1E0W at EL1 using AArch64 to EL2.

| ATS1E0W   | Meaning                                                                                                                                                                                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of AT S1E0W is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E0W at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ATS1E0R, bit [14]

Trap execution of AT S1E0R at EL1 using AArch64 to EL2.

| ATS1E0R   | Meaning                                                                                                                                                                                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of AT S1E0R is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E0R at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ATS1E1W, bit [13]

Trap execution of AT S1E1W at EL1 using AArch64 to EL2.

| ATS1E1W   | Meaning                                                                                                                                                                                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of AT S1E1W is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E1W at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ATS1E1R, bit [12]

Trap execution of AT S1E1R at EL1 using AArch64 to EL2.

| ATS1E1R   | Meaning                                                                                                                                                                                                                                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of AT S1E1R is not trapped by this mechanism.                                                                                                                                                                                                                                              |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution of AT S1E1R at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCZVA, bit [11]

Trap execution of any of the following AArch64 instructions at EL1 and EL0 to EL2:

- DCZVA.
- DCGVA, if FEAT\_MTE is implemented.
- DCGZVA, if FEAT\_MTE is implemented.

Note

Unlike HCR\_EL2.TDZ, this field has no effect on DCZID\_EL0.DZP.

| DCZVA   | Meaning                                                                   |
|---------|---------------------------------------------------------------------------|
| 0b0     | Execution of the specified instructions is not trapped by this mechanism. |

| DCZVA   | Meaning                                                                                                                                                                                                                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1     | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 and EL0 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCCIVAC, bit [10]

Trap execution of any of the following AArch64 instructions at EL1 and EL0 to EL2:

- DCCIVAC.
- DCCIGVAC, if FEAT\_MTE is implemented.
- DCCIGDVAC, if FEAT\_MTE is implemented.
- DCCIVAOC, if FEAT\_OCCMO is implemented.
- DCCIGDVAOC, if FEAT\_OCCMO is implemented.

| DCCIVAC   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                       |
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution at EL1 and EL0 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCCVADP, bit [9]

## When FEAT\_DPB2 is implemented:

Trap execution of any of the following AArch64 instructions at EL1 and EL0 to EL2:

- DCCVADP.
- DCCGVADP, if FEAT\_MTE is implemented.
- DCCGDVADP, if FEAT\_MTE is implemented.

| DCCVADP   | Meaning                                                                   |
|-----------|---------------------------------------------------------------------------|
| 0b0       | Execution of the specified instructions is not trapped by this mechanism. |

| DCCVADP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1       | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution at EL1 and EL0 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DCCVAP, bit [8]

Trap execution of any of the following AArch64 instructions at EL1 and EL0 to EL2:

- DCCVAP.
- DCCGVAP, if FEAT\_MTE is implemented.
- DCCGDVAP, if FEAT\_MTE is implemented.

| DCCVAP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                    |
| 0b1      | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == then if the execution can be trapped, execution at EL1 and EL0 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCCVAU, bit [7]

Trap execution of DC CVAU at EL1 and EL0 using AArch64 to EL2.

| DCCVAU   | Meaning                                                                                                                                                                                                                                                                                                                                                                                            |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Execution of DCCVAUis not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                               |
| 0b1      | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution ofDCCVAUat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCCISW, bit [6]

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- DCCISW.
- DCCIGSW, if FEAT\_MTE2 is implemented.
- DCCIGDSW, if FEAT\_MTE2 is implemented.

| DCCISW   | Meaning                                                                                                                                                                                                                                                                                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                     |
| 0b1      | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCCSW, bit [5]

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- DCCSW.
- DCCGSW,if FEAT\_MTE2 is implemented.
- DCCGDSW,if FEAT\_MTE2 is implemented.

| DCCSW   | Meaning                                                                                                                                                                                                                                                                                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                     |
| 0b1     | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCISW, bit [4]

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- DCISW.
- DCIGSW, if FEAT\_MTE2 is implemented.
- DCIGDSW, if FEAT\_MTE2 is implemented.

| DCISW   | Meaning                                                                                                                                                                                                                                                                                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                     |
| 0b1     | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DCIVAC, bit [3]

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- DCIVAC.
- DCIGVAC, if FEAT\_MTE2 is implemented.
- DCIGDVAC, if FEAT\_MTE2 is implemented.

| DCIVAC   | Meaning                                                                                                                                                                                                                                                                                                                                                        |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                                                                                                                      |
| 0b1      | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ICIVAU, bit [2]

Trap execution of IC IV AU at EL1 and EL0 using AArch64 to EL2.

| ICIVAU   | Meaning                                                                                                                                                                                                                                                                                                                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Execution of IC IVAU is not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                |
| 0b1      | If EL2 is implemented and enabled in the current Security state, the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution of IC IVAU at EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ICIALLU, bit [1]

Trap execution of IC IALLU at EL1 using AArch64 to EL2.

| ICIALLU   | Meaning                                                                                                                                                                                                                                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Execution of IC IALLU is not trapped by this mechanism.                                                                                                                                                                                                                                                                               |
| 0b1       | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution of IC IALLU at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## ICIALLUIS, bit [0]

Trap execution of IC IALLUIS at EL1 using AArch64 to EL2.

| ICIALLUIS   | Meaning                                                                                                                                                                                                                                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Execution of IC IALLUIS is not trapped by this mechanism.                                                                                                                                                                                                                                                                               |
| 0b1         | If EL2 is implemented and enabled in the current Security state, and either EL3 is not implemented or SCR_EL3.FGTEn == 1, then if the execution can be trapped, execution of IC IALLUIS at EL1 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HFGITR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x1C8]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HFGITR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HFGITR_EL2;
```

MSR HFGITR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_FGT) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x1C8] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HFGITR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HFGITR_EL2 = X[t, 64];
```