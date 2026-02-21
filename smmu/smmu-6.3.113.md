## 6.3.113 SMMU\_ROOT\_CR0ACK

The SMMU\_ROOT\_CR0ACK characteristics are:

## Purpose

Provides acknowledgment of changes to configuration in SMMU\_ROOT\_CR0.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_CR0ACK is a 32-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## GPCEN, bit [1]

Acknowledgment that granule protection checks are enabled.

See: SMMU\_ROOT\_CR0.GPCEN.

The reset behavior of this field is:

- This field resets to '0' .

## ACCESSEN, bit [0]

Acknowledgment that SMMU-originated and client-originated accesses are enabled.

See: SMMU\_ROOT\_CR0.ACCESSEN.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_ROOT\_CR0ACK

Accesses to this register use the following encodings:

Accessible at offset 0x0024 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.