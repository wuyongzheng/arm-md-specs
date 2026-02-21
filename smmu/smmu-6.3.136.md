## 6.3.136 SMMU\_R\_IRQ\_CTRLACK

The SMMU\_R\_IRQ\_CTRLACK characteristics are:

## Purpose

Provides acknowledgment of changes to configurations and controls of Realm state interrupts in SMMU\_R\_IRQ\_CTRL.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_IRQ\_CTRLACK is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## EVENTQ\_IRQEN, bit [2]

Event queue interrupt enable for Realm state.

| EVENTQ_IRQEN   | Meaning                                                       |
|----------------|---------------------------------------------------------------|
| 0b0            | Interrupts from the Event Queue for Realm state are disabled. |
| 0b1            | Interrupts from the Event Queue for Realm state are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## PRIQ\_IRQEN, bit [1]

## When SMMU\_R\_IDR0.PRI == 1:

PRI queue interrupt enable for Realm state.

| PRIQ_IRQEN   | Meaning                                                 |
|--------------|---------------------------------------------------------|
| 0b0          | Interrupts from PRI Queue for Realm state are disabled. |
| 0b1          | Interrupts from PRI Queue for Realm state are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## GERROR\_IRQEN, bit [0]

GERROR interrupt enable for Realm state.

| GERROR_IRQEN   | Meaning                                                     |
|----------------|-------------------------------------------------------------|
| 0b0            | Interrupts from Global errors for Realm state are disabled. |
| 0b1            | Interrupts from Global errors for Realm state are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Undefined bits read as zero. Fields in this register are RAZ if their corresponding SMMU\_R\_IRQ\_CTRL field is reserved.

## Accessing SMMU\_R\_IRQ\_CTRLACK

Accesses to this register use the following encodings:

Accessible at offset 0x0054 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.