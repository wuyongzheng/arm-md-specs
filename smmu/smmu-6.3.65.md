## 6.3.65 SMMU\_S\_IRQ\_CTRL

The SMMU\_S\_IRQ\_CTRL characteristics are:

## Purpose

Secure interrupt control and configuration register.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_IRQ\_CTRL are RES0.

## Attributes

SMMU\_S\_IRQ\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

This register is similar to SMMU\_IRQ\_CTRL, but controls interrupts from the Secure programming interface. It relates to SMMU\_S\_IRQ\_CTRLACK in the same way that SMMU\_IRQ\_CTRL relates to SMMU\_IRQ\_CTRLACK.

## Bits [31:3]

Reserved, RES0.

## EVENTQ\_IRQEN, bit [2]

Secure Event queue interrupt enable.

| EVENTQ_IRQEN   | Meaning                                              |
|----------------|------------------------------------------------------|
| 0b0            | Interrupts from the Secure Event queue are disabled. |
| 0b1            | Interrupts from the Secure Event queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## GERROR\_IRQEN, bit [0]

Secure GERROR interrupt enable.

| GERROR_IRQEN   | Meaning                                            |
|----------------|----------------------------------------------------|
| 0b0            | Interrupts from Secure Global errors are disabled. |
| 0b1            | Interrupts from Secure Global errors are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_S\_IRQ\_CTRL

Accesses to this register use the following encodings:

Accessible at offset 0x8050 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.