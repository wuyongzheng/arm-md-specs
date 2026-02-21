## 6.3.59 SMMU\_S\_CR1

The SMMU\_S\_CR1 characteristics are:

## Purpose

Secure SMMU programming interface control and configuration register.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_CR1 are RES0.

## Attributes

SMMU\_S\_CR1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:12]

Reserved, RES0.

## TABLE\_SH, bits [11:10]

Secure Stream table access Shareability.

| TABLE_SH   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-shareable.              |
| 0b01       | Reserved, treated as 0b00 . |
| 0b10       | Outer Shareable.            |
| 0b11       | Inner Shareable.            |

When SMMU\_S\_CR1.TABLE\_OC == 0b00 and SMMU\_S\_CR1.TABLE\_IC == 0b00 , this field is IGNORED and behaves as Outer Shareable.

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_S\_CR0.SMMUEN == 0
- -SMMU\_S\_CR0ACK.SMMUEN == 0
- Otherwise, access to this field is RO.

## TABLE\_OC, bits [9:8]

Secure Stream table access Outer Cacheability.

| TABLE_OC   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-cacheable.              |
| 0b01       | Write-Back Cacheable.       |
| 0b10       | Write-Through Cacheable.    |
| 0b11       | Reserved, treated as 0b00 . |

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_S\_CR0.SMMUEN == 0
- -SMMU\_S\_CR0ACK.SMMUEN == 0
- Otherwise, access to this field is RO.

## TABLE\_IC, bits [7:6]

Secure Stream table Inner Cacheability.

| TABLE_IC   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-cacheable.              |
| 0b01       | Write-Back Cacheable.       |
| 0b10       | Write-Through Cacheable.    |
| 0b11       | Reserved, treated as 0b00 . |

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_S\_CR0.SMMUEN == 0
- -SMMU\_S\_CR0ACK.SMMUEN == 0
- Otherwise, access to this field is RO.

## QUEUE\_SH, bits [5:4]

Secure queue access Shareability.

| QUEUE_SH   | Meaning        |
|------------|----------------|
| 0b00       | Non-shareable. |

| QUEUE_SH   | Meaning                     |
|------------|-----------------------------|
| 0b01       | Reserved, treated as 0b00 . |
| 0b10       | Outer Shareable.            |
| 0b11       | Inner Shareable.            |

- When SMMU\_S\_CR1.QUEUE\_OC == 0b00 and SMMU\_S\_CR1.QUEUE\_IC == 0b00 , this field is IGNORED and behaves as Outer Shareable.

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_S\_CR0.EVENTQEN == 0
- -SMMU\_S\_CR0ACK.EVENTQEN == 0
- -SMMU\_S\_CR0.CMDQEN == 0
- -SMMU\_S\_CR0ACK.CMDQEN == 0
- -Any of the following are true:
* SMMU\_S\_IDR0.ECDMQ == 0
* All of the following are true:
- SMMU\_S\_IDR0.ECMDQ == 1
- SMMU\_S\_ECMDQ\_PROD&lt;n&gt;.EN == 0
- SMMU\_S\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0
- Otherwise, access to this field is RO.

## QUEUE\_OC, bits [3:2]

Secure queue access Outer Cacheability.

| QUEUE_OC   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-cacheable.              |
| 0b01       | Write-Back Cacheable.       |
| 0b10       | Write-Through Cacheable.    |
| 0b11       | Reserved, treated as 0b00 . |

The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_S\_CR0.EVENTQEN == 0
- -SMMU\_S\_CR0ACK.EVENTQEN == 0
- -SMMU\_S\_CR0.CMDQEN == 0
- -SMMU\_S\_CR0ACK.CMDQEN == 0
- -Any of the following are true:
* SMMU\_S\_IDR0.ECDMQ == 0

* All of the following are true:
- SMMU\_S\_IDR0.ECMDQ == 1
- SMMU\_S\_ECMDQ\_PROD&lt;n&gt;.EN == 0
- SMMU\_S\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0
- Otherwise, access to this field is RO.

## QUEUE\_IC, bits [1:0]

Secure queue access Inner Cacheability.

| QUEUE_IC   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-cacheable.              |
| 0b01       | Write-Back Cacheable.       |
| 0b10       | Write-Through Cacheable.    |
| 0b11       | Reserved, treated as 0b00 . |

## The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_S\_CR0.EVENTQEN == 0
- -SMMU\_S\_CR0ACK.EVENTQEN == 0
- -SMMU\_S\_CR0.CMDQEN == 0
- -SMMU\_S\_CR0ACK.CMDQEN == 0
- -Any of the following are true:
* SMMU\_S\_IDR0.ECDMQ == 0
* All of the following are true:
- SMMU\_S\_IDR0.ECMDQ == 1
- SMMU\_S\_ECMDQ\_PROD&lt;n&gt;.EN == 0
- SMMU\_S\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0
- Otherwise, access to this field is RO.

## Additional Information

The TABLE\_* fields set the attributes for access to memory through the SMMU\_S\_STRTAB\_BASE.ADDR pointer and any accesses made to a VMS through STE.VMSPtr in a Secure STE. The QUEUE\_* fields set the attributes for access to memory through SMMU\_S\_CMDQ\_BASE.ADDR and SMMU\_S\_EVENTQ\_BASE.ADDR pointers.

Cache allocation hints are present in each BASE register and are IGNORED unless a cacheable type is used for the table or queue to which the register corresponds. The transient attribute is IMPLEMENTATION DEFINED for each \_BASE register. See section 13.1.2 Attribute support . Use of an unsupported memory type for structure or queue access might cause the access to be treated as an external abort. For example, in the case of SMMU\_S\_STRTAB\_BASE, a F\_STE\_FETCH fault is raised.

## Accessing SMMU\_S\_CR1

The fields in this register are guarded by various queue and table enable bits.

See sections 6.3.11.1 TABLE\_* attributes and 6.3.11.2 QUEUE\_* attributes .

Accesses to this register use the following encodings:

Chapter 6. Memory map and registers 6.3. Register formats

Accessible at offset 0x8028 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.