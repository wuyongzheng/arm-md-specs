## 6.3.158 SMMU\_R\_DPT\_BASE

The SMMU\_R\_DPT\_BASE characteristics are:

## Purpose

Provides the base address for the Device Permission Table for Realm state.

## Configuration

This register is present only when SMMU\_R\_IDR3.DPT == 1. Otherwise, direct accesses to SMMU\_R\_DPT\_BASE are RES0.

## Attributes

SMMU\_R\_DPT\_BASE is a 64-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 63 61   | 62   | 56           | 55 32        |
|---------|------|--------------|--------------|
|         | RA   | RES0         | BADDR[55:12] |
| RES0    |      |              |              |
| 31      |      | 12 11        | 0            |
|         |      | BADDR[55:12] | RES0         |

## Bit [63]

Reserved, RES0.

## RA, bit [62]

Read-Allocate hint.

| RA   | Meaning           |
|------|-------------------|
| 0b0  | No Read-Allocate. |
| 0b1  | Read-Allocate.    |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## BADDR, bits [55:12]

Base address of level 0 DPT.

This is a Realm physical address.

The address is aligned by the SMMU to the greater of 4KB and the size of the table.

Least-significant bits that are unused because of alignment are treated as zero by the SMMU, and are RES0.

Bits above the implemented output address size, advertised in SMMU\_IDR5.OAS, are RES0, an SMMU implementation is not required to provide storage for these bits, and they are treated as zero by the SMMU.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

```
Bits [11:0] Reserved, RES0.
```

## Accessing SMMU\_R\_DPT\_BASE

Accesses to this register use the following encodings:

Accessible at offset 0x0200 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_CR0.DPT\_WALK\_EN == 1 or SMMU\_R\_CR0ACK.DPT\_WALK\_EN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.