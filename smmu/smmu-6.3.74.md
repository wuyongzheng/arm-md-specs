## 6.3.74 SMMU\_S\_CMDQ\_BASE

The SMMU\_S\_CMDQ\_BASE characteristics are:

## Purpose

Configuration of the Secure Command queue base address.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_CMDQ\_BASE are RES0.

## Attributes

SMMU\_S\_CMDQ\_BASE is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bit [63]

Reserved, RES0.

## RA, bit [62]

Read Allocate hint.

| RA   | Meaning           |
|------|-------------------|
| 0b0  | No Read-Allocate. |
| 0b1  | Read-Allocate.    |

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## ADDR, bits [55:5]

Physical address of Secure Command queue base, bits [55:5].

- Address bits above and below this field range are implied as zero.
- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.
- -Note: An implementation is not required to store these bits.
- The effective base address is aligned by the SMMU to the larger of the queue size in bytes or 32 bytes, ignoring the least-significant bits of ADDR as required.

- -Note: For example, a queue with 2 8 entries is 4096 bytes in size so software must align an allocation, and therefore ADDR, to a 4KB boundary.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## LOG2SIZE, bits [4:0]

Queue size as log2(entries).

LOG2SIZE must be less than or equal to SMMU\_IDR1.CMDQS. Except for the purposes of readback of this register, any use of this field's value is capped at the maximum, SMMU\_IDR1.CMDQS.

The minimum size is 0, for one entry, but this must be aligned to a 32-byte (2 entry) boundary as above.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Additional Information

Upon initialization, if SMMU\_IDR1.QUEUES\_PRESET == 0 then the SMMU\_S\_CMDQ\_BASE.LOG2SIZE field might affect which bits of SMMU\_S\_CMDQ\_CONS.RD and SMMU\_S\_CMDQ\_PROD.WR can be written upon initialization. The registers must be initialized in this order:

1. Write SMMU\_S\_CMDQ\_BASE to set the queue base and size.
2. Write initial values to SMMU\_S\_CMDQ\_CONS and SMMU\_S\_CMDQ\_PROD.
3. Enable the queue with an Update of the respective SMMU\_S\_CR0.CMDQEN to 1.

This also applies to the initialization of Secure Event queue registers.

Access attributes of the Secure Command queue are set using the SMMU\_S\_CR1.QUEUE\_* fields. A Read-Allocate hint is provided for Secure Command queue accesses with the RA field.

## Accessing SMMU\_S\_CMDQ\_BASE

This register is Guarded by SMMU\_S\_CR0.CMDQEN and must only be modified when SMMU\_S\_CR0.CMDQEN == 0.

See SMMU\_CMDQ\_BASE for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x8090 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_IDR1.QUEUES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_S\_CR0.CMDQEN == 0 and SMMU\_S\_CR0ACK.CMDQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.