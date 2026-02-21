## 6.3.55 SMMU\_S\_IDR3

The SMMU\_S\_IDR3 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_IDR3 are RES0.

## Attributes

SMMU\_S\_IDR3 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:7]

Reserved, RES0.

## SAMS, bit [6]

Secure ATS Maintenance Support.

| SAMS   | Meaning                                                                                                                                                                                                                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If SMMU_IDR0.ATS == 1, the CMD_ATC_INV command is supported when issued on the Non-secure and Secure Command queues. If SMMU_IDR0.PRI == 1, the CMD_PRI_RESP command is supported, when issued on the Non-secure and Secure Command queues.                                                                                                      |
| 0b1    | If SMMU_IDR0.ATS == 1, the CMD_ATC_INV command is supported when issued on the Non-secure Command queue, but raises CERROR_ILL when issued on the Secure Command queue. If SMMU_IDR0.PRI == 1, the CMD_PRI_RESP command is supported when issued on the Non-secure Command queue, but raises CERROR_ILL when issued on the Secure Command queue. |

If SMMU\_IDR0.ATS == 0, this field is RES0.

Note: This ID field has the opposite polarity from most ID fields.

## Bits [5:0]

Reserved, RES0.

## Accessing SMMU\_S\_IDR3

Accesses to this register use the following encodings:

Accessible at offset 0x800C from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.