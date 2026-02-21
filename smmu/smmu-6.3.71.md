## 6.3.71 SMMU\_S\_GERROR\_IRQ\_CFG2

The SMMU\_S\_GERROR\_IRQ\_CFG2 characteristics are:

## Purpose

Secure Global Error interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1 and SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_GERROR\_IRQ\_CFG2 are RES0.

## Attributes

SMMU\_S\_GERROR\_IRQ\_CFG2 is a 32-bit register.

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

- Encoded the same as the STE.MemAttr field.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

MemAttr and SH allow the memory type and Shareability of the MSI to be configured, see section 3.18 Interrupts and notifications . When a cacheable type is specified in MemAttr, the allocation and transient hints are IMPLEMENTATION DEFINED.

## Accessing SMMU\_S\_GERROR\_IRQ\_CFG2

SMMU\_S\_GERROR\_IRQ\_CFG2 is Guarded by SMMU\_S\_IRQ\_CTRL.GERROR\_IRQEN, and must only be modified when SMMU\_S\_IRQ\_CTRL.GERROR\_IRQEN == 0.

See SMMU\_GERROR\_IRQ\_CFG0 for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8074 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_IRQ\_CTRL.GERROR\_IRQEN == 0 and SMMU\_S\_IRQ\_CTRLACK.GERROR\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.