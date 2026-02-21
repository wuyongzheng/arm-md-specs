## 6.3.64 SMMU\_S\_AGBPA

The SMMU\_S\_AGBPA characteristics are:

## Purpose

Secure Alternate Global ByPass Attribute.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_AGBPA are RES0.

## Attributes

SMMU\_S\_AGBPA is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## IMPLEMENTATION DEFINED, bits [31:0]

IMPLEMENTATION DEFINED attributes to assign.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Additional Information

- This register allows an implementation to apply an additional non-architected attributes or tag to bypassing transactions.
- If this field is unsupported by an implementation, it is RES0.
- Note: Arm does not recommend that this register further modifies existing architected bypass attributes.

The process used to change contents of this register in relation to SMMU\_S\_GBPA. Update is IMPLEMENTATION DEFINED.

## Accessing SMMU\_S\_AGBPA

Accesses to this register use the following encodings:

Accessible at offset 0x8048 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.