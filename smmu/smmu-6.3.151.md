## 6.3.151 SMMU\_R\_PRIQ\_BASE

The SMMU\_R\_PRIQ\_BASE characteristics are:

## Purpose

Configuration of the PRI queue base address for Realm state.

## Configuration

This register is present only when SMMU\_R\_IDR0.PRI == 1. Otherwise, direct accesses to SMMU\_R\_PRIQ\_BASE are RES0.

## Attributes

SMMU\_R\_PRIQ\_BASE is a 64-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 63                  | 62 61               | 56                  | 55                  |
|---------------------|---------------------|---------------------|---------------------|
|                     | WA                  | RES0                |                     |
| RES0                | RES0                | RES0                | RES0                |
| 31 5 4 0            | 31 5 4 0            | 31 5 4 0            | 31 5 4 0            |
| ADDR[55:5] LOG2SIZE | ADDR[55:5] LOG2SIZE | ADDR[55:5] LOG2SIZE | ADDR[55:5] LOG2SIZE |

## Bit [63]

Reserved, RES0.

## WA, bit [62]

Write allocate hint.

| WA   | Meaning            |
|------|--------------------|
| 0b0  | No Write-Allocate. |
| 0b1  | Write-Allocate.    |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## ADDR, bits [55:5]

PA of queue base, bits [55:5].

- Address bits above and below this field range are implied as zero.
- High-order bits of the ADDR field above the system physical address size, as reported by SMMU\_IDR5.OAS, are RES0.
- -Note: An implementation is not required to store these bits.
- The effective base address is aligned by the SMMU to the larger of the queue size in bytes or 32 bytes, ignoring the least-significant bits of ADDR as required.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## LOG2SIZE, bits [4:0]

Queue size as log2(entries).

- LOG2SIZE &lt;= SMMU\_IDR1.PRIQS (which has a maximum value of 19). Except for the purposes of readback of this register, any use of this field's value is capped at SMMU\_IDR1.PRIQS.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

See SMMU\_R\_CMDQ\_BASE for initialization order with respect to the PROD and CONS registers.

Access attributes of the PRI queue are set using the SMMU\_R\_CR1.QUEUE\_* fields. A Write-Allocate hint is provided for PRI queue accesses with the WA field.

## Accessing SMMU\_R\_PRIQ\_BASE

SMMU\_R\_PRIQ\_BASE is Guarded by SMMU\_R\_CR0.PRIQEN and must only be modified when SMMU\_R\_CR0.PRIQEN == 0

These update conditions are common for both SMMU\_R\_PRIQ\_{BASE, PROD} registers in the SMMU with respect to PRIQEN.

Accesses to this register use the following encodings:

Accessible at offset 0x00C0 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_IDR1.QUEUES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_R\_CR0.PRIQEN == 0 and SMMU\_R\_CR0ACK.PRIQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.