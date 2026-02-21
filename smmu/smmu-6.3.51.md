## 6.3.51 SMMU\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt;, n = 0 - 255

The SMMU\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt; characteristics are:

## Purpose

Status of Enhanced Command queue interface for the SMMU Non-secure programming interface.

## Configuration

This register is present only when SMMU\_IDR1.ECMDQ == 1. Otherwise, direct accesses to SMMU\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt; are RES0.

## Attributes

SMMU\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt; is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## ENACK, bit [0]

Command queue control page enable.

| ENACK   | Meaning                                |
|---------|----------------------------------------|
| 0b1     | Command queue control page is enabled. |

This field is RES1.

## Accessing SMMU\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt;

Accesses to this register use the following encodings:

Accessible at offset 0x400C + (32 * n) from SMMUv3\_PAGE\_0

When SMMU\_IDR1.ECMDQ == 1, accesses to this register are RO.