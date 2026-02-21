## 6.3.54 SMMU\_S\_IDR2

The SMMU\_S\_IDR2 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_IDR2 are RES0.

## Attributes

SMMU\_S\_IDR2 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:10]

Reserved, RES0.

## BA\_S\_VATOS, bits [9:0]

## When SMMU\_IDR0.VATOS == 1:

S\_VATOS page base address offset. If SMMU\_IDR0.VATOS == 0, no S\_VATOS page is present.

If Secure state is supported and SMMU\_S\_IDR1.SEL2 == 1 and SMMU\_IDR0.VATOS == 1, the S\_VATOS registers are present.

The address of the S\_VATOS page is determined from this field and is referred to as O\_S\_VATOS:

```
O_S_VATOS = SMMU_BASE + 0x20000 + (SMMU_S_IDR2.BA_S_VATOS * 0x10000)
```

## Otherwise:

Reserved, RES0.

## Accessing SMMU\_S\_IDR2

Accesses to this register use the following encodings:

Accessible at offset 0x8008 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.