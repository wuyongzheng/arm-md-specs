## 6.3.49 SMMU\_CMDQ\_CONTROL\_PAGE\_BASE&lt;n&gt;, n = 0 - 255

The SMMU\_CMDQ\_CONTROL\_PAGE\_BASE&lt;n&gt; characteristics are:

## Purpose

Provides information about the Enhanced Command queue interface for the SMMU Non-secure programming interface.

## Configuration

This register is present only when SMMU\_IDR1.ECMDQ == 1. Otherwise, direct accesses to SMMU\_CMDQ\_CONTROL\_PAGE\_BASE&lt;n&gt; are RES0.

## Attributes

SMMU\_CMDQ\_CONTROL\_PAGE\_BASE&lt;n&gt; is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## ADDR, bits [55:16]

Base address of the Command queue control page, bits [55:16].

The bits [15:0] of the base address are 0.

Bits above the system physical address size, as advertised in SMMU\_IDR5.OAS, are RES0.

The value of this field is an offset from the base address of SMMU Register Page 0, not an absolute address.

The values of all SMMU\_CMDQ\_CONTROL\_PAGE\_BASEn.ADDR are such that the pages occupy a contiguous region of address space within the SMMU register file, and they are arranged in ascending value of n.

## Bits [15:3]

Reserved, RES0.

## CMDQGS, bits [2:1]

Granule size to use for the Command queue control page.

| CMDQGS   | Meaning   |
|----------|-----------|
| 0b01     | 64KB      |

## CMDQ\_CONTROL\_PAGE\_PRESET, bit [0]

Indicates whether queue controls for this interface are stored in Normal memory or registers.

| CMDQ_CONTROL_PAGE_PRESET   | Meaning                                                                      |
|----------------------------|------------------------------------------------------------------------------|
| 0b1                        | The ECMDQ interfaces for this page are implemented as registers in the SMMU. |

This bit is 1 in implementations of SMMUv3.3.

## Accessing SMMU\_CMDQ\_CONTROL\_PAGE\_BASE&lt;n&gt;

Accesses to this register use the following encodings:

Accessible at offset 0x4000 + (32 * n) from SMMUv3\_PAGE\_0

When SMMU\_IDR1.ECMDQ == 1, accesses to this register are RO.