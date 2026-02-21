## 6.3.7 SMMU\_IIDR

The SMMU\_IIDR characteristics are:

## Purpose

Provides information about the implementation and implementer of the SMMU, and architecture version supported.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IIDR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31        | 20 19   | 16 15    | 12 11       |
|-----------|---------|----------|-------------|
| ProductID | Variant | Revision | Implementer |

## ProductID, bits [31:20]

ProductID.

- IMPLEMENTATION DEFINED value identifying the SMMU part.
- Note: Normally, when the SMMU\_PIDR{0,1} registers are present, Arm expects that the SMMU\_PIDR{0,1}.PART\_{0,1} fields match the value of SMMU\_IIDR.ProductID. If required, however, an implementation is permitted to provide values for SMMU\_PIDR.{0,1}.PART\_{0,1} that do not match the value of SMMU\_IIDR.ProductID.

## Variant, bits [19:16]

Variant.

- IMPLEMENTATION DEFINED value used to distinguish product variants, or major revisions of the product

## Revision, bits [15:12]

Revision.

- IMPLEMENTATION DEFINED value used to distinguish minor revisions of the product

## Implementer, bits [11:0]

Implementer.

- Contains the JEP106 code of the company that implemented the SMMU:
- -[11:8] The JEP106 continuation code of the implementer.
- -[7] Always 0.
- -[6:0] The JEP106 identity code of the implementer.
- For an Arm implementation, bits[11:0] are 0x43B .
- Matches the SMMU\_PIDR{1,2,4}.DES\_{0,1,2} fields, if SMMU\_PIDR{1,2,4} are present.

## Additional Information

Note: This register duplicates some of the information that might be present in the ID\_REGS SMMU\_CIDRx/ SMMU\_PIDRx fields. However, those fields are not required to be present in all

implementations, so this register provides a way for software to probe this information in a generic way. Arm expects that the SMMU\_CIDRx/SMMU\_PIDRx fields are used by Arm CoreSight and related debug mechanisms rather than primarily being for the use of drivers.

## Accessing SMMU\_IIDR

Accesses to this register use the following encodings:

Accessible at offset 0x0018 from SMMUv3\_PAGE\_0

Accesses to this register are RO.