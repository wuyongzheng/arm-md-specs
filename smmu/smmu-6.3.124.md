## 6.3.124 SMMU\_R\_IDR2

The SMMU\_R\_IDR2 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Realm state programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_IDR2 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

## Bits [31:0]

Reserved, RES0.

## Accessing SMMU\_R\_IDR2

Accesses to this register use the following encodings:

Accessible at offset 0x0008 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

31

RES0

0