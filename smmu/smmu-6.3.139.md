## 6.3.139 SMMU\_R\_GERROR\_IRQ\_CFG0

The SMMU\_R\_GERROR\_IRQ\_CFG0 characteristics are:

## Purpose

Global Error interrupt configuration register for Realm state.

## Configuration

This register is present only when SMMU\_R\_IDR0.MSI == 1. Otherwise, direct accesses to SMMU\_R\_GERROR\_IRQ\_CFG0 are RES0.

## Attributes

SMMU\_R\_GERROR\_IRQ\_CFG0 is a 64-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## NS, bit [63]

MSI targets either the Realm physical address space or the Non-secure physical address space.

| NS   | Meaning                                                   |
|------|-----------------------------------------------------------|
| 0b0  | MSIs are issued to Realm physical address space.          |
| 0b1  | MSIs are issued to the Non-secure physical address space. |

## Bits [62:56]

Reserved, RES0.

## ADDR, bits [55:2]

Physical address of MSI target register, bits [55:2].

- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.

Note: An implementation is not required to store these bits.

- Bits [1:0] of the effective address that results from this field are zero.
- If ADDR == 0, no MSI is sent. This allows a wired IRQ, if implemented, to be used when SMMU\_R\_IRQ\_CTRL.GERROR\_IRQEN == 1 instead of an MSI.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## Accessing SMMU\_R\_GERROR\_IRQ\_CFG0

SMMU\_R\_GERROR\_IRQ\_CFG0 is Guarded by SMMU\_R\_IRQ\_CTRL.GERROR\_IRQEN and must only be modified when SMMU\_R\_IRQ\_CTRL.GERROR\_IRQEN == 0.

These update conditions are common for all SMMU\_R\_*\_IRQ\_CFG{0,1,2} register sets in the SMMU with respect to their corresponding SMMU\_R\_IRQ\_CTRL.*\_IRQEN flag.

Accesses to this register use the following encodings:

Accessible at offset 0x0068 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_IRQ\_CTRL.GERROR\_IRQEN == 0 and SMMU\_R\_IRQ\_CTRLACK.GERROR\_IRQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.