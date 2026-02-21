## 6.3.15 SMMU\_AGBPA

The SMMU\_AGBPA characteristics are:

## Purpose

Alternate Global ByPass Attribute.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_AGBPA is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## IMPLEMENTATION DEFINED, bits [31:0]

IMPLEMENTATION DEFINED attributes to assign.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Additional Information

- This register allows an implementation to apply an additional non-architected attributes or tag to bypassing transactions.
- If this field is unsupported by an implementation it is RES0.
- Note: Arm does not recommend that this register further modifies existing architected bypass attributes.

The process used to change contents of this register in relation to SMMU\_GBPA.Update is IMPLEMENTATION DEFINED.

## Accessing SMMU\_AGBPA

Accesses to this register use the following encodings:

Accessible at offset 0x0048 from SMMUv3\_PAGE\_0

Accesses to this register are RW.