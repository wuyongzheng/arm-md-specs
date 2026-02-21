## 6.3.110 SMMU\_ROOT\_IDR0

The SMMU\_ROOT\_IDR0 characteristics are:

## Purpose

Feature identification register

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_IDR0 is a 32-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## BA\_REALM, bits [31:22]

## When SMMU\_ROOT\_IDR0.REALM\_IMPL == 1:

The base address offset of Realm Register Page 0.

The offset is determined from the following calculation:

O\_REALM = 0x20000 + (BA\_REALM * 0x10000 )

SMMU\_REALM\_BASE = SMMU\_PAGE\_0\_BASE + O\_REALM

Bit BA\_REALM[0] is always zero, and the offset is therefore always aligned to a multiple of 128KB.

Note: The offset is relative to Page 0 of the SMMU programmers' interface and not related to the IMPLEMENTATION DEFINED base address of the SMMU Root Control page.

## Otherwise:

Reserved, RES0.

## Bits [21:4]

Reserved, RES0.

## REALM\_IMPL, bit [3]

Presence of Realm programming interface.

| REALM_IMPL   | Meaning                                     |
|--------------|---------------------------------------------|
| 0b0          | Realm programming interface is not present. |
| 0b1          | Realm programming interface is present.     |

The Realm programming interface includes:

- The Realm register pages.

- The Realm StreamID space and Stream table.
- The Realm queues and tables.

If this field is 1, then SMMU\_IDR0.RME\_IMPL is 1.

## RGPTM, bit [2]

Register TLBI by PA support.

| RGPTM   | Meaning                                                 |
|---------|---------------------------------------------------------|
| 0b0     | SMMU_ROOT_TLBI and SMMU_ROOT_TLBI_CTRL are not present. |
| 0b1     | SMMU_ROOT_TLBI and SMMU_ROOT_TLBI_CTRL are present.     |

If SMMU\_ROOT\_IDR0.BGPTM is 0, then this field is 1.

See also:

- SMMU\_ROOT\_TLBI.
- SMMU\_ROOT\_TLBI\_CTRL.

## BGPTM, bit [1]

Broadcast TLBI by PA support.

| BGPTM   | Meaning                                                           |
|---------|-------------------------------------------------------------------|
| 0b0     | This SMMU does not participate in broadcast TLBI *PA* operations. |
| 0b1     | This SMMUdoes participate in broadcast TLBI *PA* operations.      |

This field indicates both that:

- The SMMU supports receipt of broadcast TLBI *PA* operations issued by PEs.
- The SMMU is integrated in the memory system such that TLBI *PA* operations issued to the Outer Shareable shareability domain by PEs correctly reach the SMMU.

The value of this field is independent of the value of SMMU\_IDR0.BTM, SMMU\_CR2.PTM, and SMMU\_S\_CR2.PTM.

See also:

- 3.17.7 Broadcast TLB maintenance for GPT information .

## ROOT\_IMPL, bit [0]

Presence of Root registers.

Reads as 0b1

Access to this field is RO.

## Accessing SMMU\_ROOT\_IDR0

Accesses to this register use the following encodings:

Accessible at offset 0x0000 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.