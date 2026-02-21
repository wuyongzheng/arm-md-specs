## 6.3.32 SMMU\_EVENTQ\_IRQ\_CFG2

The SMMU\_EVENTQ\_IRQ\_CFG2 characteristics are:

## Purpose

Event queue interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1. Otherwise, direct accesses to SMMU\_EVENTQ\_IRQ\_CFG2 are RES0.

## Attributes

SMMU\_EVENTQ\_IRQ\_CFG2 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

| 31   | 6 5 4 3   | 0       |
|------|-----------|---------|
|      | SH        | MemAttr |

## Bits [31:6]

Reserved, RES0.

## SH, bits [5:4]

Shareability.

| SH   | Meaning                     |
|------|-----------------------------|
| 0b00 | Non-shareable.              |
| 0b01 | Reserved, treated as 0b00 . |
| 0b10 | Outer Shareable.            |
| 0b11 | Inner Shareable.            |

- When MemAttr specifies a Device memory type, the contents of this field are IGNORED and the Shareability is effectively Outer Shareable.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## MemAttr, bits [3:0]

Memory type.

- Encoded in the same way as STE.MemAttr.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

MemAttr and SH allow the memory type and Shareability of the MSI to be configured, see section 3.18 Interrupts and notifications .

Note: The encodings of all of the SMMU\_*\_IRQ\_CFG2 MemAttr and SH fields are the same. When a cacheable type is specified in MemAttr, the allocation and transient hints are IMPLEMENTATION DEFINED.

## Accessing SMMU\_EVENTQ\_IRQ\_CFG2

SMMU\_EVENTQ\_IRQ\_CFG2 is Guarded by SMMU\_IRQ\_CTRL.EVENTQ\_IRQEN, and must only be modified when SMMU\_IRQ\_CTRL.EVENTQ\_IRQEN == 0.

See SMMU\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x00BC from SMMUv3\_PAGE\_0

- When SMMU\_IRQ\_CTRL.EVENTQ\_IRQEN == 0 and SMMU\_IRQ\_CTRLACK.EVENTQ\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.