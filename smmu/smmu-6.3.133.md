## 6.3.133 SMMU\_R\_GBPA

The SMMU\_R\_GBPA characteristics are:

## Purpose

Global ByPass Attribute for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_GBPA is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:21]

Reserved, RES0.

## ABORT, bit [20]

Abort all incoming transactions for Realm state.

| ABORT   | Meaning                          |
|---------|----------------------------------|
| 0b1     | Abort all incoming transactions. |

Note: Consistent with the behavior of SMMU\_GBPA.ABORT for Non-secure state, configuration of SMMU\_CR0.SMMUEN = 0 might result in F\_BAD\_ATS\_TREQ and F\_TRANSL\_FORBIDDEN for ATS translation requests and ATS-translated transactions respectively.

Access to this field is RO.

## Bits [19:0]

Reserved, RES0.

## Accessing SMMU\_R\_GBPA

Accesses to this register use the following encodings:

Accessible at offset 0x0044 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.