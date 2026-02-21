## 6.3.122 SMMU\_R\_IDR0

The SMMU\_R\_IDR0 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Realm state programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_IDR0 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## ECMDQ, bit [31]

Indicates support for Enhanced Command queue interface for Realm state.

| ECMDQ   | Meaning                                                             |
|---------|---------------------------------------------------------------------|
| 0b0     | Enhanced CMDQ for Realm state not supported.                        |
| 0b1     | Enhanced CMDQ for Realm state support is advertised in SMMU_R_IDR6. |

If this field is 1, then all of the following are true:

- SMMU\_IDR0.COHACC == 1.
- SMMU\_R\_IDR0.MSI == 1.
- SMMU\_IDR1.QUEUES\_PRESET == 0.

See section 3.5.6 Enhanced Command queue interfaces .

## Bits [30:26]

Reserved, RES0.

## STALL\_MODEL, bits [25:24]

Stall model support for Realm state.

| STALL_MODEL   | Meaning                                                                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00          | Stall and Terminate models supported.                                                                                                       |
| 0b01          | Stall is not supported, all faults terminate transaction and STE.S2S and CD.S must be 0. • CMD_RESUME and CMD_STALL_TERM are not available. |
| 0b10          | Stall is forced (all faults eligible to stall cause stall), STE.S2S and CD.S must be 1.                                                     |

| STALL_MODEL   | Meaning   |
|---------------|-----------|
| 0b11          | Reserved. |

In this revision of the architecture, the only permitted value is 0b01 .

## Bits [23:17]

Reserved, RES0.

## PRI, bit [16]

Page Request Interface supported for Realm state.

| PRI   | Meaning                                                                                           |
|-------|---------------------------------------------------------------------------------------------------|
| 0b0   | Page Request Interface not supported for Realm state. • All SMMU_R_PRIQ_* registers are Reserved. |
| 0b1   | Page Request Interface supported for Realm state.                                                 |

This field has the same value as SMMU\_IDR0.PRI.

## Bits [15:14]

Reserved, RES0.

## MSI, bit [13]

Indicates support for the SMMU-originated MSIs for Realm state.

| MSI   | Meaning                                             |
|-------|-----------------------------------------------------|
| 0b0   | SMMU-originated MSIs for Realm state not supported. |
| 0b1   | SMMU-originated MSIs for Realm state are supported. |

This field has the same value as SMMU\_IDR0.MSI.

## Bits [12:11]

Reserved, RES0.

## ATS, bit [10]

PCIe ATS supported for Realm state.

| ATS   | Meaning                                 |
|-------|-----------------------------------------|
| 0b0   | PCIe ATS not supported for Realm state. |
| 0b1   | PCIe ATS supported for Realm state.     |

This field has the same value as SMMU\_IDR0.ATS.

## Bits [9:0]

Reserved, RES0.

## Accessing SMMU\_R\_IDR0

Accesses to this register use the following encodings:

Accessible at offset 0x0000 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.