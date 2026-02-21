## 6.3.35 SMMU\_PRIQ\_IRQ\_CFG1

The SMMU\_PRIQ\_IRQ\_CFG1 characteristics are:

## Purpose

PRI queue interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1 and SMMU\_IDR0.PRI == 1. Otherwise, direct accesses to SMMU\_PRIQ\_IRQ\_CFG1 are RES0.

## Attributes

SMMU\_PRIQ\_IRQ\_CFG1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## DATA, bits [31:0]

MSI Data payload.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_PRIQ\_IRQ\_CFG1

SMMU\_PRIQ\_IRQ\_CFG1 is Guarded by SMMU\_IRQ\_CTRL.PRIQ\_IRQEN, and must only be modified when SMMU\_IRQ\_CTRL.PRIQ\_IRQEN == 0.

See SMMU\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x00D8 from SMMUv3\_PAGE\_0

- When SMMU\_IRQ\_CTRL.PRIQ\_IRQEN == 0 and SMMU\_IRQ\_CTRLACK.PRIQ\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.