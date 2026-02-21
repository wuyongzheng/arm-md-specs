## 6.3.147 SMMU\_R\_EVENTQ\_BASE

The SMMU\_R\_EVENTQ\_BASE characteristics are:

## Purpose

Event queue base address register for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_EVENTQ\_BASE is a 64-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bit [63]

Reserved, RES0.

## WA, bit [62]

Write Allocate hint.

| WA   | Meaning            |
|------|--------------------|
| 0b0  | No Write-Allocate. |
| 0b1  | Write-Allocate.    |

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## ADDR, bits [55:5]

PA of queue base, bits [55:5].

- Address bits above and below this field range are treated as zero.
- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.
- -Note: An implementation is not required to store these bits.
- The effective base address is aligned by the SMMU to the larger of the queue size in bytes or 32 bytes, ignoring the least-significant bits of ADDR as required.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## LOG2SIZE, bits [4:0]

Queue size as log2(entries).

- LOG2SIZE is less than or equal to SMMU\_IDR1.EVENTQS. Except for the purposes of readback of this register, any use of the value of this field is capped at the maximum, SMMU\_IDR1.EVENTQS.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Additional Information

See SMMU\_R\_CMDQ\_BASE for initialization order with respect to the PROD and CONS registers.

Events destined for the Realm Event queue are delivered into the queue if SMMU\_R\_CR0.EVENTQEN == 1 and the queue is writable. If SMMU\_R\_CR0.EVENTQEN == 0, no events are delivered into the queue. See section 7.2 Event queue recorded faults and events ; some events might be lost in these situations.

Access attributes of the Realm Event queue are set using the SMMU\_R\_CR1.QUEUE\_* fields. A Write-Allocate hint is provided for Event queue accesses with the WA field.

## Accessing SMMU\_R\_EVENTQ\_BASE

SMMU\_R\_EVENTQ\_BASE is Guarded by SMMU\_R\_CR0.EVENTQEN and must only be modified when SMMU\_R\_CR0.EVENTQEN == 0

These update conditions are common for all SMMU\_R\_EVENTQ\_{BASE, PROD} registers in the SMMU with respect to their corresponding EVENTQEN.

Accesses to this register use the following encodings:

Accessible at offset 0x00A0 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_IDR1.QUEUES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_R\_CR0.EVENTQEN == 0 and SMMU\_R\_CR0ACK.EVENTQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.