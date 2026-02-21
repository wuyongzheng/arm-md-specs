## 6.3.11 SMMU\_CR1

The SMMU\_CR1 characteristics are:

## Purpose

Non-secure SMMU programming interface control and configuration register.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_CR1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:12]

Reserved, RES0.

## TABLE\_SH, bits [11:10]

Table access Shareability.

| TABLE_SH   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-shareable.              |
| 0b01       | Reserved, treated as 0b00 . |
| 0b10       | Outer Shareable.            |
| 0b11       | Inner Shareable.            |

- Note: When SMMU\_CR1.TABLE\_OC == 0b00 and SMMU\_CR1.TABLE\_IC == 0b00 , this field is IGNORED and behaves as Outer Shareable.

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_CR0.SMMUEN == 0
- -SMMU\_CR0ACK.SMMUEN == 0
- Otherwise, access to this field is RO.

## TABLE\_OC, bits [9:8]

Table access Outer Cacheability.

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
- -SMMU\_CR0.SMMUEN == 0
- -SMMU\_CR0ACK.SMMUEN == 0
- Otherwise, access to this field is RO.

## TABLE\_IC, bits [7:6]

Table access Inner Cacheability.

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
- -SMMU\_CR0.SMMUEN == 0
- -SMMU\_CR0ACK.SMMUEN == 0
- Otherwise, access to this field is RO.

## QUEUE\_SH, bits [5:4]

Queue access Shareability.

| QUEUE_SH   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-shareable.              |
| 0b01       | Reserved, treated as 0b00 . |
| 0b10       | Outer Shareable.            |

| QUEUE_SH   | Meaning          |
|------------|------------------|
| 0b11       | Inner Shareable. |

- When SMMU\_CR1.QUEUE\_OC == 0b00 and SMMU\_CR1.QUEUE\_IC == 0b00 , this field is IGNORED and behaves as Outer Shareability.

## The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_CR0.EVENTQEN == 0
- -SMMU\_CR0ACK.EVENTQEN == 0
- -SMMU\_CR0.CMDQEN == 0
- -SMMU\_CR0ACK.CMDQEN == 0
- -SMMU\_CR0.PRIQEN == 0
- -SMMU\_CR0ACK.PRIQEN == 0
- -Any of the following are true:
* SMMU\_IDR1.ECMDQ == 0
* All of the following are true:
- SMMU\_IDR1.ECMDQ == 1
- SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 0
- SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0
- Otherwise, access to this field is RO.

## QUEUE\_OC, bits [3:2]

Queue access Outer Cacheability.

| QUEUE_OC   | Meaning                     |
|------------|-----------------------------|
| 0b00       | Non-cacheable.              |
| 0b01       | Write-Back Cacheable.       |
| 0b10       | Write-Through Cacheable.    |
| 0b11       | Reserved, treated as 0b00 . |

## The reset behavior of this field is:

- When SMMU\_IDR1.QUEUES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Accessing this field has the following behavior:

- Access to this field is RW if all of the following are true:
- -SMMU\_CR0.EVENTQEN == 0
- -SMMU\_CR0ACK.EVENTQEN == 0
- -SMMU\_CR0.CMDQEN == 0
- -SMMU\_CR0ACK.CMDQEN == 0
- -SMMU\_CR0.PRIQEN == 0
- -SMMU\_CR0ACK.PRIQEN == 0
- -Any of the following are true:

* SMMU\_IDR1.ECMDQ == 0
* All of the following are true:
- SMMU\_IDR1.ECMDQ == 1
- SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 0
- SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0
- Otherwise, access to this field is RO.

## QUEUE\_IC, bits [1:0]

Queue access Inner Cacheability.

| QUEUE_IC   | Meaning                     |
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
- -SMMU\_CR0.EVENTQEN == 0
- -SMMU\_CR0ACK.EVENTQEN == 0
- -SMMU\_CR0.CMDQEN == 0
- -SMMU\_CR0ACK.CMDQEN == 0
- -SMMU\_CR0.PRIQEN == 0
- -SMMU\_CR0ACK.PRIQEN == 0
- -Any of the following are true:
* SMMU\_IDR1.ECMDQ == 0
* All of the following are true:
- SMMU\_IDR1.ECMDQ == 1
- SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 0
- SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0
- Otherwise, access to this field is RO.

## Additional Information

The TABLE\_* fields set the attributes for access to memory through the SMMU\_STRTAB\_BASE.ADDR pointer and any accesses made to a VMS through STE.VMSPtr in a Non-secure STE. The QUEUE\_* fields set the attributes for access to memory through SMMU\_CMDQ\_BASE.ADDR, SMMU\_EVENTQ\_BASE.ADDR and SMMU\_PRIQ\_BASE.ADDR pointers.

Cache allocation hints are present in each \_BASE register and are ignored unless a cacheable type is used for the table or queue to which the register corresponds. The transient attribute is IMPLEMENTATION DEFINED for each \_BASE register. See section 13.1.2 Attribute support ; use of an unsupported memory type for structure or queue access might cause the access to be treated as an external abort. For example, in the case of SMMU\_STRTAB\_BASE, an F\_STE\_FETCH fault is raised.

## Accessing SMMU\_CR1

Accesses to this register use the following encodings:

Accessible at offset 0x0028 from SMMUv3\_PAGE\_0

Accesses to this register are RW.

## Additional information

## 6.3.11.1 TABLE\_* attributes

The TABLE\_* fields are preset when SMMU\_IDR1.TABLES\_PRESET == 1 and the effective attribute is unchangeable. In this case, a write of a different value to these fields is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write of the field is IGNORED.
- The new value is stored, making it visible to future reads of the field, but have no effect on the (fixed) access type.

Otherwise when not PRESET, the TABLE\_* attributes reset to an UNKNOWN value and must be initialized by software.

These fields are Guarded by SMMU\_(*\_)CR0.SMMUEN and must only be changed when SMMU\_(*\_)CR0.SMMUEN == 0. A write to these fields when SMMU\_(*\_)CR0.SMMUEN == 1 is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write to the fields is IGNORED. This is the only permitted behavior in SMMUv3.2 and later.
- The new attribute is applied, taking effect at an UNPREDICTABLE point before the SMMU is later disabled (SMMUEN transitioned 1 to 0). This behavior is permitted only in SMMUv3.1 and earlier.

## 6.3.11.2 QUEUE\_* attributes

The QUEUE\_* fields are fixed and preset when SMMU\_IDR1.QUEUES\_PRESET == 1 and the effective attribute is unchangeable. In this case, a write of a different value to these fields is CONSTRAINED UNPREDICTABLE in the same way as for preset TABLE\_* fields.

Otherwise when not preset, the QUEUE\_* attributes reset to an UNKNOWN value and must be initialized by software.

These fields are Guarded by SMMU\_(*\_)CR0.EVENTQEN, SMMU\_CR0.PRIQEN (for SMMU\_CR1 and SMMU\_(*\_)CR0.CMDQEN. They must only change when access to all queues is disabled through SMMU\_(*\_)CR0.EVENTQEN == 0 and SMMU\_CR0.PRIQEN == 0 and SMMU\_(*\_)CR0.CMDQEN == 0. In an implementation with Enhanced Command queues, they are additionally guarded by all SMMU\_ECMDQ\_PRODn.EN and SMMU\_ECMDQ\_CONSn.ENACK pairs associated with the respective Security state. They must only change when all SMMU\_ECMDQ\_PRODn.EN == SMMU\_ECMDQ\_CONSn.ENACK == 0 for the corresponding Security state. A write to these fields when any of these queues are enabled is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write to the fields is IGNORED. This is the only permitted behavior in SMMUv3.2 and later.
- The new attribute is applied, taking effect, with respect to an enabled queue access, at an UNPREDICTABLE point before the respective queue is later disabled (the enable flag transitioned from 1 to 0). This behavior is permitted only in SMMUv3.1 and earlier.