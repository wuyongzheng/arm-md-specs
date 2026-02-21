## 6.3.121 SMMU\_ROOT\_GPT\_BASE\_UPDATE

The SMMU\_ROOT\_GPT\_BASE\_UPDATE characteristics are:

## Purpose

Control register to trigger an update of the Granule Protection Table base address.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_GPT\_BASE\_UPDATE is a 32-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## Update, bit [0]

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_ROOT\_GPT\_BASE\_UPDATE

A write to this register that does not set Update to 1 is IGNORED.

A write to this register that sets Update to 1 causes the SMMU to perform the following sequence in an atomic manner:

1. The value of SMMU\_ROOT\_GPT\_BASE2 is copied into SMMU\_ROOT\_GPT\_BASE, in an atomic manner.
2. The value of Update is set to 0.

Accesses to this register use the following encodings:

Accessible at offset 0x0068 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.