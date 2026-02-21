## 6.3.13 SMMU\_STATUSR

The SMMU\_STATUSR characteristics are:

## Purpose

Provides information on the status of the component.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_STATUSR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## DORMANT, bit [0]

## When SMMU\_IDR0.DORMHINT == 1:

Dormant hint.

| DORMANT   | Meaning                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------|
| 0b0       | The SMMUmight have cached translation or configuration structure data, or be in the process of doing so.                |
| 0b1       | The SMMUguarantees that no translation or configuration structure data is cached, and that no prefetches are in-flight. |

- Software might avoid issuing configuration invalidation or TLB invalidation commands for changes to structures made visible to the SMMU before reading this hint as 1. See section 3.19.1 Dormant state .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## Accessing SMMU\_STATUSR

Accesses to this register use the following encodings:

Accessible at offset 0x0040 from SMMUv3\_PAGE\_0

Accesses to this register are RO.