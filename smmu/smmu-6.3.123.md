## 6.3.123 SMMU\_R\_IDR1

The SMMU\_R\_IDR1 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Realm state programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_IDR1 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## RME\_DA\_IMPL, bit [31]

Indicates support for the Realm programming interface.

| RME_DA_IMPL   | Meaning                                     |
|---------------|---------------------------------------------|
| 0b0           | Realm programming interface is not present. |
| 0b1           | Realm programming interface is present.     |

This field reads as one.

## Bits [30:0]

Reserved, RES0.

## Accessing SMMU\_R\_IDR1

Accesses to this register use the following encodings:

Accessible at offset 0x0004 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.