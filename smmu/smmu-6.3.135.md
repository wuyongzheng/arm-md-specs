## 6.3.135 SMMU\_R\_IRQ\_CTRL

The SMMU\_R\_IRQ\_CTRL characteristics are:

## Purpose

Realm state Interrupt control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_IRQ\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## EVENTQ\_IRQEN, bit [2]

Event queue interrupt enable for Realm state.

| EVENTQ_IRQEN   | Meaning                                                       |
|----------------|---------------------------------------------------------------|
| 0b0            | Interrupts from the Event queue for Realm state are disabled. |
| 0b1            | Interrupts from the Event queue for Realm state are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## PRIQ\_IRQEN, bit [1]

## When SMMU\_R\_IDR0.PRI == 1:

PRI queue interrupt enable for Realm state.

| PRIQ_IRQEN   | Meaning                                                 |
|--------------|---------------------------------------------------------|
| 0b0          | Interrupts from PRI queue for Realm state are disabled. |
| 0b1          | Interrupts from PRI queue for Realm state are enabled.  |

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

Each field in this register has a corresponding field in the SMMU\_R\_IRQ\_CTRLACK, with the same Update observability semantics as fields in SMMU\_R\_CR0 versus SMMU\_R\_CR0ACK.

This register contains IRQ enable flags for GERROR, PRI queue and Event queue interrupt sources for Realm state. These enables allow or inhibit both edge-triggered wired outputs if implemented and MSI writes if implemented.

IRQ enable flags Guard the MSI address and payload registers when MSIs supported, SMMU\_R\_IDR0.MSI == 1, which must only be changed when their respective enable flag is 0. See SMMU\_R\_GERROR\_IRQ\_CFG0 for details.

## Accessing SMMU\_R\_IRQ\_CTRL

Accesses to this register use the following encodings:

Accessible at offset 0x0050 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.