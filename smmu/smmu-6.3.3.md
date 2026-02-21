## 6.3.3 SMMU\_IDR2

The SMMU\_IDR2 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Non-secure programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IDR2 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:10]

Reserved, RES0.

## BA\_VATOS, bits [9:0]

## When SMMU\_IDR0.VATOS == 1:

VATOS page base address offset.

All BA values are encoded as an unsigned offset from SMMU address 0x20000 in units of 64KB.

Page\_Address = SMMU\_BASE + 0x20000 + (BA * 0x10000 ).

## Otherwise:

Reserved, RES0.

## Accessing SMMU\_IDR2

Accesses to this register use the following encodings:

Accessible at offset 0x0008 from SMMUv3\_PAGE\_0

Accesses to this register are RO.