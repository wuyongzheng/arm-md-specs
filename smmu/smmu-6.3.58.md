## 6.3.58 SMMU\_S\_CR0ACK

The SMMU\_S\_CR0ACK characteristics are:

## Purpose

Provides acknowledgment of changes to configurations and controls in Secure SMMU programming interface, SMMU\_S\_CR0.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_CR0ACK are RES0.

## Attributes

SMMU\_S\_CR0ACK is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:10]

Reserved, RES0.

## NSSTALLD, bit [9]

Non-secure stall disable.

| NSSTALLD   | Meaning                                                             |
|------------|---------------------------------------------------------------------|
| 0b0        | Non-secure programming interface might use Stall model.             |
| 0b1        | Non-secure programming interface prohibited from using Stall model. |

When SMMU\_S\_IDR0.STALL\_MODEL != 0b00 , this bit is RES0 and SMMU\_IDR0.STALL\_MODEL == SMMU\_S\_IDR0.STALL\_MODEL.

- Note: A reserved SMMU\_S\_CR0 bit is not reflected into SMMU\_S\_CR0ACK.

The reset behavior of this field is:

- This field resets to '0' .

## VMW, bits [8:6]

When SMMU\_IDR0.VMW == 1:

Secure VMID Wildcard.

| VMW   | Meaning                                    |
|-------|--------------------------------------------|
| 0b000 | TLB invalidations match VMID tags exactly. |

| VMW   | Meaning                            |
|-------|------------------------------------|
| 0b001 | TLB invalidations match VMID[N:1]. |
| 0b010 | TLB invalidations match VMID[N:2]. |
| 0b011 | TLB invalidations match VMID[N:3]. |
| 0b100 | TLB invalidations match VMID[N:4]. |

- The VMW field is defined in the same way as SMMU\_CR0.VMW, but affects Secure VMID matching on invalidation.

The reset behavior of this field is:

- This field resets to '000' .

## Otherwise:

Reserved, RES0.

## SIF, bit [5]

Secure Instruction Fetch.

| SIF   | Meaning                                                                                              |
|-------|------------------------------------------------------------------------------------------------------|
| 0b0   | Secure transactions might exit the SMMUas a Non-secure instruction fetch.                            |
| 0b1   | Secure transactions determined to be Non-secure instruction fetch are treated as a Permission fault. |

The reset behavior of this field is:

- This field resets to '0' .

## Bit [4]

Reserved, RES0.

## CMDQEN, bit [3]

Enable Secure Command queue processing.

| CMDQEN   | Meaning                                                           |
|----------|-------------------------------------------------------------------|
| 0b0      | Processing of commands from the Secure Command queue is disabled. |
| 0b1      | Processing of commands from the Secure Command queue is enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## EVENTQEN, bit [2]

Enable Secure Event queue writes.

| EVENTQEN   | Meaning                                        |
|------------|------------------------------------------------|
| 0b0        | Writes to the Secure Event queue are disabled. |
| 0b1        | Writes to the Secure Event queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## SMMUEN, bit [0]

Secure SMMU enable.

| SMMUEN   | Meaning                                                                                         |
|----------|-------------------------------------------------------------------------------------------------|
| 0b0      | All Secure streams bypass the SMMU, with attributes determined from SMMU_S_GBPA.                |
| 0b1      | All Secure streams are checked against configuration structures, and might undergo translation. |

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Undefined bits read as zero. Fields in this register are RAZ if their corresponding SMMU\_S\_CR0 field is IGNORED.

An Update to a field in SMMU\_S\_CR0 is considered complete, along with any side effects, when the respective field in this register is observed to take the new value.

The Update procedure, with respect to flags reflected in SMMU\_S\_CR0ACK, is the same as for SMMU\_CR0 and SMMU\_CR0ACK.

## Accessing SMMU\_S\_CR0ACK

Accesses to this register use the following encodings:

Accessible at offset 0x8024 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.