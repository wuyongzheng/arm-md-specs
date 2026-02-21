## 6.3.56 SMMU\_S\_IDR4

The SMMU\_S\_IDR4 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_IDR4 are RES0.

## Attributes

SMMU\_S\_IDR4 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## IMPLEMENTATION DEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

## Additional Information

The contents of this register are IMPLEMENTATION DEFINED and can be used to identify the presence of other IMPLEMENTATION DEFINED register regions elsewhere in the memory map.

## Accessing SMMU\_S\_IDR4

Accesses to this register use the following encodings:

Accessible at offset 0x8010 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.