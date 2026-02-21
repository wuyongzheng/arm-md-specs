## 6.3.93 SMMU\_S\_CMDQ\_CONTROL\_PAGE\_CFG&lt;n&gt;, n = 0 - 255

The SMMU\_S\_CMDQ\_CONTROL\_PAGE\_CFG&lt;n&gt; characteristics are:

## Purpose

Control for Enhanced Command queue interface for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR0.ECMDQ == 1. Otherwise, direct accesses to SMMU\_S\_CMDQ\_CONTROL\_PAGE\_CFG&lt;n&gt; are RES0.

## Attributes

SMMU\_S\_CMDQ\_CONTROL\_PAGE\_CFG&lt;n&gt; is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

| 31   | 1 0   |
|------|-------|

## Bits [31:1]

Reserved, RES0.

## EN, bit [0]

Command queue control page enable.

| EN   | Meaning                                |
|------|----------------------------------------|
| 0b1  | Command queue control page is enabled. |

This field is RES1.

## Accessing SMMU\_S\_CMDQ\_CONTROL\_PAGE\_CFG&lt;n&gt;

Accesses to this register use the following encodings:

Accessible at offset 0xC008 + (32 * n) from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.