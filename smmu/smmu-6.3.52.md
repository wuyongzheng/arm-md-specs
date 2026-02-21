## 6.3.52 SMMU\_S\_IDR0

The SMMU\_S\_IDR0 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_IDR0 are RES0.

## Attributes

SMMU\_S\_IDR0 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## ECMDQ, bit [31]

Support for enhanced Command queue interface for Secure programming interface.

| ECMDQ   | Meaning                                                                        |
|---------|--------------------------------------------------------------------------------|
| 0b0     | Secure Enhanced Command queue interface not supported. SMMU_S_IDR6 is RES0.    |
| 0b1     | Secure Enhanced Command queue interface details are advertised in SMMU_S_IDR6. |

If this field is 1, then all of the following are true:

- SMMU\_IDR0.COHACC == 1.
- SMMU\_S\_IDR0.MSI == 1.
- SMMU\_IDR1.QUEUES\_PRESET == 0.

See section 3.5.6 Enhanced Command queue interfaces .

## Bits [30:26]

Reserved, RES0.

## STALL\_MODEL, bits [25:24]

Stalling fault model support.

| STALL_MODEL   | Meaning                                                                                                                                   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00          | Stall and Terminate models supported.                                                                                                     |
| 0b01          | Stall is not supported, all faults terminate transaction and STE.S2S and CD.S must be 0. CMD_RESUME and CMD_STALL_TERM are not available. |

| STALL_MODEL   | Meaning                                                                                      |
|---------------|----------------------------------------------------------------------------------------------|
| 0b10          | Stall is forced (all faults eligible to stall cause stall), STE.S2S and CD.S must be 1.      |
| 0b11          | Reserved. Note: STE.S2S must be in the states above only if stage 2 translation was enabled. |

- Encoded identically to SMMU\_IDR0.STALL\_MODEL, this field indicates the SMMU support for the Stall model and the Terminate model.
- For more information, see SMMU\_S\_CR0.NSSTALLD.

## Bits [23:14]

Reserved, RES0.

## MSI, bit [13]

Secure Message Signalled Interrupts are supported.

| MSI   | Meaning                                                                                                                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The SMMUsupports wired interrupt notifications only for Secure events and GERROR. • The MSI fields in SMMU_S_EVENTQ_IRQ_CFGn and SMMU_S_GERROR_IRQ_CFGn are RES0.                                           |
| 0b1   | Message Signalled Interrupts are supported for Secure events and GERROR. • Note: Arm strongly recommends that an implementation supports Non-secure MSIs (SMMU_IDR0.MSI == 1) if Secure MSIs are supported. |

## Bits [12:0]

Reserved, RES0.

## Accessing SMMU\_S\_IDR0

Accesses to this register use the following encodings:

Accessible at offset 0x8000 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.