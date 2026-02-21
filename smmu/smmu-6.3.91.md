## 6.3.91 SMMU\_S\_IDR6

The SMMU\_S\_IDR6 characteristics are:

## Purpose

Provides information about the Enhanced Command queue interface for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR0.ECMDQ == 1. Otherwise, direct accesses to SMMU\_S\_IDR6 are RES0.

## Attributes

SMMU\_S\_IDR6 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:28]

Reserved, RES0.

## CMDQ\_CONTROL\_PAGE\_LOG2NUMP, bits [27:24]

Number of Secure Command queue control pages supported.

The number of Secure Command queue control pages supported is 2 CMDQ\_CONTROL\_PAGE\_LOG2NUMP .

This field has a maximum value of 0b1000 .

## Bits [23:20]

Reserved, RES0.

## CMDQ\_CONTROL\_PAGE\_LOG2NUMQ, bits [19:16]

Number of queues per Secure Command queue control page.

The number of queues supported per Secure Command queue control page is 2 CMDQ\_CONTROL\_PAGE\_LOG2NUMQ .

This field has a maximum value of 0b1000 .

## Bits [15:0]

Reserved, RES0.

## Additional Information

See section 3.5.6 Enhanced Command queue interfaces .

## Accessing SMMU\_S\_IDR6

Accesses to this register use the following encodings:

Accessible at offset 0x8190 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.