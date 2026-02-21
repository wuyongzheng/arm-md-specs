## 6.3.18 SMMU\_IRQ\_CTRLACK

The SMMU\_IRQ\_CTRLACK characteristics are:

## Purpose

Provides acknowledgment of changes to configurations and controls of interrupts in SMMU\_IRQ\_CTRL.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IRQ\_CTRLACK is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## EVENTQ\_IRQEN, bit [2]

Event queue interrupt enable.

| EVENTQ_IRQEN   | Meaning                                                  |
|----------------|----------------------------------------------------------|
| 0b0            | Interrupts from the Non-secure Event Queue are disabled. |
| 0b1            | Interrupts from the Non-secure Event Queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## PRIQ\_IRQEN, bit [1]

## When SMMU\_IDR0.PRI == 1:

PRI queue interrupt enable.

| PRIQ_IRQEN   | Meaning                                 |
|--------------|-----------------------------------------|
| 0b0          | Interrupts from PRI Queue are disabled. |
| 0b1          | Interrupts from PRI Queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## GERROR\_IRQEN, bit [0]

GERROR interrupt enable.

| GERROR_IRQEN   | Meaning                                                |
|----------------|--------------------------------------------------------|
| 0b0            | Interrupts from Non-secure Global errors are disabled. |
| 0b1            | Interrupts from Non-secure Global errors are enabled.  |

The reset behavior of this field is:

· This field resets to '0' .

## Additional Information

Undefined bits read as zero. Fields in this register are RAZ if their corresponding SMMU\_IRQ\_CTRL field is reserved.

## Accessing SMMU\_IRQ\_CTRLACK

Accesses to this register use the following encodings: Accessible at offset 0x0054 from SMMUv3\_PAGE\_0

Accesses to this register are RO.