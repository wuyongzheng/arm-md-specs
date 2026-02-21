## 6.3.111 SMMU\_ROOT\_IIDR

The SMMU\_ROOT\_IIDR characteristics are:

## Purpose

Implementation identification register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_IIDR is a 32-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## ProductID, bits [31:20]

IMPLEMENTATION DEFINED value identifying the SMMU part.

## Variant, bits [19:16]

IMPLEMENTATION DEFINED value used to distinguish product variants, or major revisions of the product.

## Revision, bits [15:12]

IMPLEMENTATION DEFINED value used to distinguish minor revisions of the product.

## Implementer, bits [11:0]

Contains the JEP106 code of the company that implemented the SMMU.

- SMMU\_ROOT\_IIDR[11:8] - The JEP106 continuation code of the implementer.
- SMMU\_ROOT\_IIDR[7] - Always 0.
- SMMU\_ROOT\_IIDR[6:0] - The JEP106 identity code of the implementer.

For an Arm implementation, bits[11:0] are 0x43B .

## Accessing SMMU\_ROOT\_IIDR

Accesses to this register use the following encodings:

Accessible at offset 0x0008 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.