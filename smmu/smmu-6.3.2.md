## 6.3.2 SMMU\_IDR1

The SMMU\_IDR1 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Non-secure programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IDR1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## ECMDQ, bit [31]

Support for enhanced Command queue interface.

| ECMDQ   | Meaning                                                               |
|---------|-----------------------------------------------------------------------|
| 0b0     | Enhanced Command queue interface not supported. SMMU_IDR6 is RES0.    |
| 0b1     | Enhanced Command queue interface details are advertised in SMMU_IDR6. |

If this field is 1, then all of the following are true:

- SMMU\_IDR0.COHACC == 1.
- SMMU\_IDR0.MSI == 1.
- SMMU\_IDR1.QUEUES\_PRESET == 0.

See section 3.5.6 Enhanced Command queue interfaces .

## TABLES\_PRESET, bit [30]

Table base addresses fixed.

| TABLES_PRESET   | Meaning                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------|
| 0b0             | The contents of the registers SMMU_(*_)STRTAB_BASE and SMMU_(*_)STRTAB_BASE_CFG are not fixed. |
| 0b1             | The contents of the registers SMMU_(*_)STRTAB_BASE and SMMU_(*_)STRTAB_BASE_CFG are fixed.     |

## QUEUES\_PRESET, bit [29]

Queue base addresses fixed.

| QUEUES_PRESET   | Meaning                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| 0b0             | The contents of the registers SMMU_(*_)CMDQ_BASE, SMMU_(*_)EVENTQ_BASE, and if present, SMMU_(R_)PRIQ_BASE are not fixed. |
| 0b1             | The contents of the registers SMMU_(*_)CMDQ_BASE, SMMU_(*_)EVENTQ_BASE, and if present, SMMU_(R_)PRIQ_BASE are fixed.     |

This field must be 0 if any of the following are true:

- SMMU\_IDR1.ECMDQ == 1.
- SMMU\_S\_IDR0.ECMDQ == 1.
- SMMU\_R\_IDR0.ECMDQ == 1.

## REL, bit [28]

Relative base pointers.

| REL   | Meaning                                                                                                                                                                                                        |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When the corresponding preset field is set, base address registers report an absolute address.                                                                                                                 |
| 0b1   | When the corresponding preset field is set, base address registers report an address offset. • Relative addresses are calculated using an addition of the unsigned ADDR field onto the base address of Page 0. |

When SMMU\_IDR1.TABLES\_PRESET == 0 and SMMU\_IDR1.QUEUES\_PRESET == 0, this field is RES0.

## ATTR\_TYPES\_OVR, bit [27]

Incoming MemType, Shareability, allocation and transient hints override.

| ATTR_TYPES_OVR   | Meaning                                                                          |
|------------------|----------------------------------------------------------------------------------|
| 0b0              | Incoming attributes cannot be overridden before translation or by global bypass. |
| 0b1              | Incoming attributes can be overridden.                                           |

## ATTR\_PERMS\_OVR, bit [26]

Incoming Data or Instruction, User or Privileged, input NS attribute override.

| ATTR_PERMS_OVR   | Meaning                                                                          |
|------------------|----------------------------------------------------------------------------------|
| 0b0              | Incoming attributes cannot be overridden before translation or by global bypass. |
| 0b1              | Incoming attributes can be overridden.                                           |

## CMDQS, bits [25:21]

Maximum number of Command queue entries.

- Maximum number of entries as log2(entries).
- -Maximum value 19.
- Note: The index register values include an extra bit for wrap. Therefore a queue with 2 N entries has indices of N bits, but an index register containing (N+1) bits.

## EVENTQS, bits [20:16]

Maximum number of Event queue entries.

- Maximum number of entries as log2(entries).
- -Maximum value 19.

## PRIQS, bits [15:11]

Maximum number of PRI queue entries.

- Maximum number of entries as log2(entries).
- -Maximum value 19.
- -If SMMU\_IDR0.PRI == 0, this field has an IMPLEMENTATION SPECIFIC value.

## SSIDSIZE, bits [10:6]

Max bits of SubstreamID.

- Valid range 0 to 20 inclusive, 0 meaning no substreams are supported.
- Reflects physical SubstreamID representation size, that is the SMMU cannot represent or be presented with SubstreamIDs greater than SSIDSIZE.

## SIDSIZE, bits [5:0]

Max bits of StreamID.

- This value is between 0 and 32 inclusive.
- -Note: 0 is a legal value. In this case the SMMU supports one stream.
- This must reflect the physical StreamID size, that is the SMMU cannot represent or be presented with StreamIDs greater than SIDSIZE.
- When SMMU\_IDR1.SIDSIZE &gt;= 7, SMMU\_IDR0.ST\_LEVEL != 0b00 .

## Accessing SMMU\_IDR1

Accesses to this register use the following encodings:

Accessible at offset 0x0004 from SMMUv3\_PAGE\_0

Accesses to this register are RO.