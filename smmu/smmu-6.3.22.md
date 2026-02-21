## 6.3.22 SMMU\_GERROR\_IRQ\_CFG1

The SMMU\_GERROR\_IRQ\_CFG1 characteristics are:

## Purpose

Global Error interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1. Otherwise, direct accesses to SMMU\_GERROR\_IRQ\_CFG1 are RES0.

## Attributes

SMMU\_GERROR\_IRQ\_CFG1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## DATA, bits [31:0]

MSI Data payload.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_GERROR\_IRQ\_CFG1

SMMU\_GERROR\_IRQ\_CFG1is Guarded by SMMU\_IRQ\_CTRL.GERROR\_IRQEN, and must only be modified when SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 0.

See SMMU\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x0070 from SMMUv3\_PAGE\_0

- When SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 0 and SMMU\_IRQ\_CTRLACK.GERROR\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.