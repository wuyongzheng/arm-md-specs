## 6.3.36 SMMU\_PRIQ\_IRQ\_CFG2

The SMMU\_PRIQ\_IRQ\_CFG2 characteristics are:

## Purpose

PRI queue interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1 and SMMU\_IDR0.PRI == 1. Otherwise, direct accesses to SMMU\_PRIQ\_IRQ\_CFG2 are RES0.

## Attributes

SMMU\_PRIQ\_IRQ\_CFG2 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31 30   | 6 5 4 3    |
|---------|------------|
| LO      | SH MemAttr |

Similar to SMMU\_GERROR\_IRQ\_CFG2 but for PRI queue MSIs.

## LO, bit [31]

Last Only: only interrupt if PRI message received with L bit set.

| LO   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Send PRI queue interrupt when PRI queue transitions from empty to non-empty.                                                                                                                                                                                                                                                                                                                                  |
| 0b1  | Send PRI queue interrupt when PRI message received with L bit set. • When the message is written to PRI queue, the interrupt is visible after the queue entry becomes visible. See section 3.18 Interrupts and notifications • When the message is discarded because of a PRI queue overflow, the interrupt is generated. When the message is discarded for any other reason, the interrupt is not generated. |

Note: The LO field applies to wired and MSI interrupts.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [30:6]

Reserved, RES0.

## SH, bits [5:4]

Shareability.

| SH   | Meaning                     |
|------|-----------------------------|
| 0b00 | Non-shareable.              |
| 0b01 | Reserved, treated as 0b00 . |

| SH   | Meaning          |
|------|------------------|
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## MemAttr, bits [3:0]

Memory type.

- Encoded the same as the STE.MemAttr field.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

MemAttr and SH allow the memory type and Shareability of the MSI to be configured, see section 3.18 Interrupts and notifications . The encodings of all of the SMMU\_*\_IRQ\_CFG2 MemAttr and SH fields are the same. When a cacheable type is specified in MemAttr, the allocation and transient hints are IMPLEMENTATION DEFINED.

## Accessing SMMU\_PRIQ\_IRQ\_CFG2

SMMU\_PRIQ\_IRQ\_CFG2 is Guarded by SMMU\_IRQ\_CTRL.PRIQ\_IRQEN, and must only be modified when SMMU\_IRQ\_CTRL.PRIQ\_IRQEN == 0.

See SMMU\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x00DC from SMMUv3\_PAGE\_0

- When SMMU\_IRQ\_CTRL.PRIQ\_IRQEN == 0 and SMMU\_IRQ\_CTRLACK.PRIQ\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.