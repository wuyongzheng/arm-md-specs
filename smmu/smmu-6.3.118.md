## 6.3.118 SMMU\_ROOT\_TLBI

The SMMU\_ROOT\_TLBI characteristics are:

## Purpose

TLBI by PA attributes register.

## Configuration

This register is present only when SMMU\_ROOT\_IRD0.RGPTM == 1. Otherwise, direct accesses to SMMU\_ROOT\_TLBI are RES0.

## Attributes

SMMU\_ROOT\_TLBI is a 64-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

| 63   | 52 51     |           |      |      |      |      | 32   |      |      |      |
|------|-----------|-----------|------|------|------|------|------|------|------|------|
|      |           | RES0      | RES0 | RES0 | RES0 | RES0 | RES0 | RES0 | RES0 | RES0 |
| 31   | 12 11 8 7 | 12 11 8 7 |      |      | 3 2  | 1    | 0    |      |      |      |
|      | Address   | Address   | RES0 | SIZE | RES0 | L    | ALL  |      |      |      |

## Bits [63:52]

Reserved, RES0.

## Address, bits [51:12]

Base address from which to start invalidation.

Bits [11:0] of the base address are taken to be zero.

If ALL == 1, this field is IGNORED.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [11:8]

Reserved, RES0.

## SIZE, bits [7:4]

Range of addresses to be invalidated.

| SIZE   | Meaning   |
|--------|-----------|
| 0b0000 | 4KB.      |
| 0b0001 | 16KB.     |
| 0b0010 | 64KB.     |
| 0b0011 | 2MB.      |
| 0b0100 | 32MB.     |
| 0b0101 | 512MB.    |
| 0b0110 | 1GB.      |

| SIZE   | Meaning   |
|--------|-----------|
| 0b0111 | 16GB.     |
| 0b1000 | 64GB.     |
| 0b1001 | 512GB.    |

All other values are reserved.

If ALL == 1, this field is IGNORED.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [3:2]

Reserved, RES0.

## L, bit [1]

GPT Last-level only.

| L   | Meaning                                                              |
|-----|----------------------------------------------------------------------|
| 0b0 | Invalidate GPT information from all levels of the GPT walk.          |
| 0b1 | Invalidate GPT information from only the last level of the GPT walk. |

If ALL == 1, this field is IGNORED.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## ALL, bit [0]

GPT All.

| ALL   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | Invalidate GPT information from TLBs based on other fields. |
| 0b1   | Invalidate all GPT information from TLBs.                   |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_ROOT\_TLBI

Accesses to this register use the following encodings:

Accessible at offset 0x0050 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_ROOT\_TLBI\_CTRL.RUN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.