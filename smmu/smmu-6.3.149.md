## 6.3.149 SMMU\_R\_EVENTQ\_IRQ\_CFG1

The SMMU\_R\_EVENTQ\_IRQ\_CFG1 characteristics are:

## Purpose

Event queue interrupt configuration register for Realm state.

## Configuration

This register is present only when SMMU\_R\_IDR0.MSI == 1. Otherwise, direct accesses to SMMU\_R\_EVENTQ\_IRQ\_CFG1 are RES0.

## Attributes

SMMU\_R\_EVENTQ\_IRQ\_CFG1 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## DATA, bits [31:0]

MSI Data payload.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_R\_EVENTQ\_IRQ\_CFG1

SMMU\_R\_EVENTQ\_IRQ\_CFG1 is Guarded by SMMU\_R\_IRQ\_CTRL.EVENTQ\_IRQEN, and must only be modified when SMMU\_R\_IRQ\_CTRL.EVENTQ\_IRQEN == 0.

See SMMU\_R\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x00B8 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_IRQ\_CTRL.EVENTQ\_IRQEN == 0 and SMMU\_R\_IRQ\_CTRLACK.EVENTQ\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.