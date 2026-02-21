## 6.3.26 SMMU\_CMDQ\_BASE

The SMMU\_CMDQ\_BASE characteristics are:

## Purpose

Configuration of the Command queue base address.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_CMDQ\_BASE is a 64-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bit [63]

Reserved, RES0.

## RA, bit [62]

Read-Allocate hint.

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

PA of Command queue base, bits [55:5].

- Address bits above and below this field range are treated as zero.
- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.
- -Note: An implementation is not required to store these bits.
- The effective base address is aligned by the SMMU to the larger of the queue size in bytes or 32 bytes, ignoring the least-significant bits of ADDR as required. ADDR bits [4:0] are treated as zero.

- -Note: For example, a queue with 2 8 entries is 4096 bytes in size so software must align an allocation, and therefore ADDR, to a 4KB boundary.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## LOG2SIZE, bits [4:0]

Queue size as log2(entries).

- LOG2SIZE must be less than or equal to SMMU\_IDR1.CMDQS. Except for the purposes of readback of this register, any use of the value of this field is capped at the maximum, SMMU\_IDR1.CMDQS.
- The minimum size is 0, for one entry, but this must be aligned to a 32-byte (2 entry) boundary as above.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Additional Information

Upon initialization, if SMMU\_IDR1.QUEUES\_PRESET == 0 then the SMMU\_CMDQ\_BASE.LOG2SIZE field might affect which bits of SMMU\_CMDQ\_CONS.RD and SMMU\_CMDQ\_PROD.WR can be written upon initialization. The registers must be initialized in this order:

1. Write SMMU\_CMDQ\_BASE to set the queue base and size.
2. Write initial values to SMMU\_CMDQ\_CONS and SMMU\_CMDQ\_PROD.
3. Enable the queue with an Update of the respective SMMU\_CR0.CMDQEN to 1.

This also applies to the initialization of Event queue and PRI queue registers.

Access attributes of the Command queue are set using the SMMU\_CR1.QUEUE\_* fields. A Read-Allocate hint is provided for Command queue accesses with the RA field.

## Accessing SMMU\_CMDQ\_BASE

SMMU\_CMDQ\_BASE is Guarded by SMMU\_CR0.CMDQEN and must only be modified when SMMU\_CR0.CMDQEN == 0

These update conditions are common for all SMMU\_(S\_)CMDQ\_{BASE, CONS} registers in the SMMU with respect to their corresponding CMDQEN.

In SMMUv3.1 and earlier, a write while SMMU\_CR0.CMDQEN == 1 is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The register takes on any value, which might cause commands to be fetched from an UNPREDICTABLE address.
- The write is ignored.
- A read following such a write will return an UNKNOWN value.

In SMMUv3.2 and later, a write while SMMU\_CR0.CMDQ\_EN == 1 is IGNORED.

Accesses to this register use the following encodings:

Accessible at offset 0x0090 from SMMUv3\_PAGE\_0

- When SMMU\_IDR1.QUEUES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_CR0.CMDQEN == 0 and SMMU\_CR0ACK.CMDQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.