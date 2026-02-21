## 6.3.70 SMMU\_S\_GERROR\_IRQ\_CFG1

The SMMU\_S\_GERROR\_IRQ\_CFG1 characteristics are:

## Purpose

Secure Global Error interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1 and SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_GERROR\_IRQ\_CFG1 are RES0.

## Attributes

SMMU\_S\_GERROR\_IRQ\_CFG1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## DATA, bits [31:0]

Secure MSI Data Payload.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_S\_GERROR\_IRQ\_CFG1

SMMU\_S\_GERROR\_IRQ\_CFG1 is Guarded by SMMU\_S\_IRQ\_CTRL.GERROR\_IRQEN, and must only be modified when SMMU\_S\_IRQ\_CTRL.GERROR\_IRQEN == 0.

See SMMU\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8070 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_IRQ\_CTRL.GERROR\_IRQEN == 0 and SMMU\_S\_IRQ\_CTRLACK.GERROR\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.