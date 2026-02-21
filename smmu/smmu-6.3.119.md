## 6.3.119 SMMU\_ROOT\_TLBI\_CTRL

The SMMU\_ROOT\_TLBI\_CTRL characteristics are:

## Purpose

TLBI by PA control register.

## Configuration

This register is present only when SMMU\_ROOT\_IRD0.RGPTM == 1. Otherwise, direct accesses to SMMU\_ROOT\_TLBI\_CTRL are RES0.

## Attributes

SMMU\_ROOT\_TLBI\_CTRL is a 32-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

| 31   | 1 0   |
|------|-------|

## Bits [31:1]

Reserved, RES0.

## RUN, bit [0]

| RUN   | Meaning                       |
|-------|-------------------------------|
| 0b0   | Invalidation not in progress. |
| 0b1   | Invalidation in progress.     |

Writes to this register only have an effect if both of the following are true:

- The value of RUN in the register before the write is 0.
- The value of RUN in the write data payload is 1.

Any write that does not satisfy both these conditions is IGNORED.

When the requirements for RUN are met for a given write, the following all apply:

- The values provided for ALL, L, SIZE, and Address are taken from SMMU\_ROOT\_TLBI.
- The SMMU performs the TLBI by PA operation, interpreted as follows:
- -If ALL == 1, the operation behaves as TLBI PAALL as issued on a PE.
- -If ALL == 0 and L == 0, the operation behaves as TLBI RPAOS as issued on a PE, with SIZE and Address interpreted in the same manner as for TLBI RPAOS .
- -If ALL == 0 and L == 1, the operation behaves as TLBI RPALOS as issued on a PE, with SIZE and Address interpreted in the same manner as for TLBI RPALOS .
- A TLBI by PA operation is complete when all the following requirements are met:
- -All matching GPT information in TLB entries has been invalidated.
- -All SMMU-originated and client-originated accesses that were in progress to physical addresses targeted by the TLBI by PA operation, are globally observable to their Shareability domain.

- Once the TLBI by PA operation is complete, the SMMU clears the whole register to 0.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_ROOT\_TLBI\_CTRL

Accesses to this register use the following encodings:

Accessible at offset 0x0058 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.