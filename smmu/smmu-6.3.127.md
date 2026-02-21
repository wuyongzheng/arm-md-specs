## 6.3.127 SMMU\_R\_AIDR

The SMMU\_R\_AIDR characteristics are:

## Purpose

This register indicates which revision of the SMMU architecture for Realm Management Extension for Device Assignment to which the implementation conforms.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_AIDR is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

| 31   | 8 7 4 3   |
|------|-----------|

## Bits [31:8]

Reserved, RES0.

## ArchMajorRev, bits [7:4]

Major Architecture revision.

| ArchMajorRev   | Meaning                              |
|----------------|--------------------------------------|
| 0b0000         | Realm Management Extension for SMMU. |

## ArchMinorRev, bits [3:0]

Minor Architecture revision.

| ArchMinorRev   | Meaning                              |
|----------------|--------------------------------------|
| 0b0000         | Realm Management Extension for SMMU. |

## Accessing SMMU\_R\_AIDR

Accesses to this register use the following encodings:

Accessible at offset 0x001C from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.