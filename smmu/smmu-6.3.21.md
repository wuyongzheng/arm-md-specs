## 6.3.21 SMMU\_GERROR\_IRQ\_CFG0

The SMMU\_GERROR\_IRQ\_CFG0 characteristics are:

## Purpose

Global Error interrupt configuration register.

## Configuration

This register is present only when SMMU\_IDR0.MSI == 1. Otherwise, direct accesses to SMMU\_GERROR\_IRQ\_CFG0 are RES0.

## Attributes

SMMU\_GERROR\_IRQ\_CFG0 is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## ADDR, bits [55:2]

Physical address of MSI target register, bits [55:2].

- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.

Note: An implementation is not required to store these bits.

- Bits [1:0] of the effective address that results from this field are zero.
- If ADDR == 0, no MSI is sent. This allows a wired IRQ, if implemented, to be used when SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 1 instead of an MSI.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## Accessing SMMU\_GERROR\_IRQ\_CFG0

SMMU\_GERROR\_IRQ\_CFG0 is Guarded by SMMU\_IRQ\_CTRL.GERROR\_IRQEN and must only be modified when SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 0.

These update conditions are common for all SMMU\_*\_IRQ\_CFG{0,1,2} register sets in the SMMU with respect to their corresponding SMMU\_IRQ\_CTRL.*\_IRQEN flag.

In SMMUv3.1 and earlier, a write while SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 1 is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The register takes on any value, which might cause MSIs to be written to UNPREDICTABLE addresses or with UNPREDICTABLE payload values.

- The write is IGNORED.
- A read following such a write will return an UNKNOWN value.

In SMMUv3.2 and later, a write while SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 1 is IGNORED.

Accesses to this register use the following encodings:

Accessible at offset 0x0068 from SMMUv3\_PAGE\_0

- When SMMU\_IRQ\_CTRL.GERROR\_IRQEN == 0 and SMMU\_IRQ\_CTRLACK.GERROR\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.