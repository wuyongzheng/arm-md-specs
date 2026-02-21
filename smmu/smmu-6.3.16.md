## 6.3.16 SMMU\_IRQ\_CTRL

The SMMU\_IRQ\_CTRL characteristics are:

## Purpose

Interrupt control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IRQ\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## EVENTQ\_IRQEN, bit [2]

Event queue interrupt enable.

| EVENTQ_IRQEN   | Meaning                                                  |
|----------------|----------------------------------------------------------|
| 0b0            | Interrupts from the Non-secure Event queue are disabled. |
| 0b1            | Interrupts from the Non-secure Event queue are enabled.  |

The reset behavior of this field is:

- This field resets to '0' .

## PRIQ\_IRQEN, bit [1]

## When SMMU\_IDR0.PRI == 1:

PRI queue interrupt enable.

| PRIQ_IRQEN   | Meaning                                 |
|--------------|-----------------------------------------|
| 0b0          | Interrupts from PRI queue are disabled. |
| 0b1          | Interrupts from PRI queue are enabled.  |

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

- This field resets to '0' .

## Additional Information

Each field in this register has a corresponding field in SMMU\_IRQ\_CTRLACK, with the same Update observability semantics as fields in SMMU\_CR0 versus SMMU\_CR0ACK.

This register contains IRQ enable flags for GERROR, PRI queue and Event queue interrupt sources. These enables allow or inhibit both edge-triggered wired outputs if implemented and MSI writes if implemented.

IRQ enable flags Guard the MSI address and payload registers when MSIs supported, SMMU\_IDR0.MSI == 1, which must only be changed when their respective enable flag is 0. See SMMU\_GERROR\_IRQ\_CFG0 for details.

## Accessing SMMU\_IRQ\_CTRL

Accesses to this register use the following encodings:

Accessible at offset 0x0050 from SMMUv3\_PAGE\_0

Accesses to this register are RW.

## Additional information

Completion of Update to IRQ enables guarantees the following side effects:

- Completion of an Update of x\_IRQEN from 0 to 1 guarantees that the MSI configuration in SMMU\_x\_IRQ\_CFG{0,1,2} will be used for all future MSIs generated from source x. All wired or MSI interrupts that are triggered from a source relate to occurrences that happened after the completion of the Update that enabled the source. It is not permitted to trigger an interrupt that relates to an occurrence that happened before the source was enabled, even if the source was previously enabled at the time of the occurrence.
- An Update of x\_IRQEN from 1 to 0 completes when all prior MSIs have completed. An MSI has completed when it is visible to its Shareability domain, or when it has aborted, and the abort is recorded in the appropriate SMMU\_(*\_)GERROR bit. Completion of this Update guarantees that no new MSI writes or wired edge events from source x become visible until the source is re-enabled. See section 3.18.1 MSI synchronization .