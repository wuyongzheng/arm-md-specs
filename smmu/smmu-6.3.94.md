## 6.3.94 SMMU\_S\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt;, n = 0 - 255

The SMMU\_S\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt; characteristics are:

## Purpose

Status of Enhanced Command queue interface for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR0.ECMDQ == 1. Otherwise, direct accesses to SMMU\_S\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt; are RES0.

## Attributes

SMMU\_S\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt; is a 32-bit register.

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

## Accessing SMMU\_S\_CMDQ\_CONTROL\_PAGE\_STATUS&lt;n&gt;

Accesses to this register use the following encodings:

Accessible at offset 0xC00C + (32 * n) from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.