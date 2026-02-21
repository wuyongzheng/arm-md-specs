## 6.3.8 SMMU\_AIDR

The SMMU\_AIDR characteristics are:

## Purpose

This register identifies the SMMU architecture version to which the implementation conforms.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_AIDR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

| 31   | 8 7 4 3 0                 |
|------|---------------------------|
| RES0 | ArchMajorRev ArchMinorRev |

## Bits [31:8]

Reserved, RES0.

## ArchMajorRev, bits [7:4]

Major Architecture revision.

| ArchMajorRev   | Meaning   |
|----------------|-----------|
| 0b0000         | SMMUv3.x. |

## ArchMinorRev, bits [3:0]

Minor Architecture revision.

| ArchMinorRev   | Meaning   |
|----------------|-----------|
| 0b0000         | SMMUv3.0. |
| 0b0001         | SMMUv3.1. |
| 0b0010         | SMMUv3.2. |
| 0b0011         | SMMUv3.3. |
| 0b0100         | SMMUv3.4. |

## Accessing SMMU\_AIDR

Accesses to this register use the following encodings:

Accessible at offset 0x001C from SMMUv3\_PAGE\_0

Accesses to this register are RO.