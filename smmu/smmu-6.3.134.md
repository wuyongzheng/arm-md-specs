## 6.3.134 SMMU\_R\_AGBPA

The SMMU\_R\_AGBPA characteristics are:

## Purpose

Alternate Global ByPass Attribute for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_AGBPA is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

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

The process used to change contents of this register is IMPLEMENTATION DEFINED.

## Accessing SMMU\_R\_AGBPA

Accesses to this register use the following encodings:

Accessible at offset 0x0048 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.