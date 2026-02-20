## D24.2.187 SMIDR\_EL1, Streaming Mode Identification Register

The SMIDR\_EL1 characteristics are:

## Purpose

Provides additional identification mechanisms for scheduling purposes, for a PE that supports Streaming SVE mode.

## Configuration

This register is present only when FEAT\_SME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SMIDR\_EL1 are UNDEFINED.

## Attributes

SMIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:60]

Reserved, RES0.

## NSMC, bits [59:56]

If SMIDR\_EL1.{SH,Affinity} indicates that the implementation of Streaming SVE mode is shared, then this field identifies the number of SMCUs, minus 1, associated with the concatenated SMIDR\_EL1.{Affinity2,Affinity} 32-bit value.

If SMIDR\_EL1.{SH,Affinity} indicates that the implementation of Streaming SVE mode is not shared, then this field is zero and should be ignored by software.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NSMC             | Meaning                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0000           | The implementation of Streaming SVE mode associated with this PE is not shared or is a single SMCU.                |
| 0b0001 .. 0b1110 | The number of SMCUs in the group of SMCUs providing the implementation of Streaming SVE mode for this PE, minus 1. |
| 0b1111           | Reserved.                                                                                                          |

Access to this field is RO.

HIP, bits [55:52]

## When FEAT\_SME2p2 is implemented and SMIDR\_EL1.SMPS == '1':

Highest Implemented Priority. If Streaming SVE mode execution priority is supported, this field indicates the range of priority levels implemented by the PE, and the Highest Implemented Priority value.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HIP              | Meaning                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000           | All streaming execution priorities from 0 to 15 are implemented. The Highest Implemented Priority value is 15.                                          |
| 0b0001 .. 0b1111 | All streaming execution priorities less than or equal to this value are implemented. The Highest Implemented Priority value is the value of this field. |

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Affinity2, bits [51:32]

The most significant 20 bits of the SMCU affinity for this PE, to be used in conjunction with SMIDR\_EL1.Affinity.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Implementer, bits [31:24]

The Implementer code. This field must hold an implementer code that has been assigned by Arm.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Implementer   | Meaning                                  |
|---------------|------------------------------------------|
| 0x00          | Reserved for software use.               |
| 0x41          | Arm Limited.                             |
| 0x42          | Broadcom Corporation.                    |
| 0x43          | Cavium Inc.                              |
| 0x44          | Digital Equipment Corporation.           |
| 0x46          | Fujitsu Ltd.                             |
| 0x49          | Infineon Technologies AG.                |
| 0x4D          | Motorola or Freescale Semiconductor Inc. |
| 0x4E          | NVIDIA Corporation.                      |
| 0x50          | Applied Micro Circuits Corporation.      |
| 0x51          | Qualcomm Inc.                            |
| 0x56          | Marvell International Ltd.               |
| 0x69          | Intel Corporation.                       |

| Implementer   | Meaning           |
|---------------|-------------------|
| 0xC0          | Ampere Computing. |

Arm can assign codes that are not published in this manual. All values not assigned by Arm are reserved and must not be used.

It is not required that this value is the same as the value of MIDR\_EL1.Implementer.

Access to this field is RO.

## Revision, bits [23:16]

Revision number for the Streaming Mode Compute Unit (SMCU).

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SMPS, bit [15]

Indicates support for Streaming SVE mode execution priority.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SMPS   | Meaning                         |
|--------|---------------------------------|
| 0b0    | Priority control not supported. |
| 0b1    | Priority control supported.     |

Access to this field is RO.

## SH, bits [14:13]

Indicates whether the implementation of Streaming SVE mode in this PE is shared with other PEs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SH   | Meaning                                                                |
|------|------------------------------------------------------------------------|
| 0b00 | Refer to SMIDR_EL1.Affinity.                                           |
| 0b01 | Reserved.                                                              |
| 0b10 | The implementation of Streaming SVE mode is not shared with other PEs. |
| 0b11 | The implementation of Streaming SVE mode is shared with other PEs.     |

Access to this field is RO.

## Bit [12]

Reserved, RES0.

## Affinity, bits [11:0]

The least significant 12 bits of the SMCU affinity for this PE.

This field has an IMPLEMENTATION DEFINED value.

If the implementation of Streaming SVE mode is shared, then the concatenated SMIDR\_EL1.{Affinity2,Affinity} 32-bit value identifies which shared SMCUs are associated with this PE. Every PE that shares the same SMCUs has the same 32-bit affinity value. The 32-bit affinity value is unique within the system as a whole.

The SMIDR\_EL1.SH field indicates whether the implementation of Streaming SVE mode is shared with other PEs. However, if SMIDR\_EL1.SH is zero, then SMIDR\_EL1.Affinity is used to indicate whether the implementation of Streaming SVE is shared, as follows:

- If SMIDR\_EL1.Affinity is zero, then the implementation of Streaming SVE mode is not shared with other PEs.
- If SMIDR\_EL1.Affinity is not zero, then the implementation of Streaming SVE mode is shared with other PEs.

Access to this field is RO.

## Accessing SMIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SMIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b001 | 0b0000 | 0b0000 | 0b110 |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(IsFeatureImplemented(FEAT_SME) && UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = SMIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = SMIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SMIDR_EL1;
```