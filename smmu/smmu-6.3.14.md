## 6.3.14 SMMU\_GBPA

The SMMU\_GBPA characteristics are:

## Purpose

Global ByPass Attribute

## Configuration

There are no configuration notes.

## Attributes

SMMU\_GBPA is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Update, bit [31]

Update completion flag.

See section 6.3.14.1 Update procedure .

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:21]

Reserved, RES0.

## ABORT, bit [20]

Abort all incoming transactions.

| ABORT   | Meaning                                                                                                                 |
|---------|-------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Do not abort incoming transactions. Transactions bypass theSMMU with attributes given by other fields in this register. |
| 0b1     | Abort all incoming transactions.                                                                                        |

Note: An implementation can reset this field to 1, in order to implement a default deny policy on reset.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## INSTCFG, bits [19:18]

Instruction/data override.

| INSTCFG   | Meaning                     |
|-----------|-----------------------------|
| 0b00      | Use incoming.               |
| 0b01      | Reserved, behaves as 0b00 . |
| 0b10      | Data.                       |
| 0b11      | Instruction.                |

- INSTCFG only affects reads, writes are always output as Data.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## PRIVCFG, bits [17:16]

User/privileged override.

| PRIVCFG   | Meaning                     |
|-----------|-----------------------------|
| 0b00      | Use incoming.               |
| 0b01      | Reserved, behaves as 0b00 . |
| 0b10      | Unprivileged.               |
| 0b11      | Privileged.                 |

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Bits [15:14]

Reserved, RES0.

## SHCFG, bits [13:12]

Shareability override.

| SHCFG   | Meaning          |
|---------|------------------|
| 0b00    | Non-shareable.   |
| 0b01    | Use incoming.    |
| 0b10    | Outer Shareable. |
| 0b11    | Inner Shareable. |

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## ALLOCCFG, bits [11:8]

Allocation Configuration.

- 0b0xxx use incoming RA/WA/TR allocation/transient hints.

- 0b1RWT Hints are overridden to given values:
- -Read Allocate == R.
- -Write Allocate == W.
- -Transient == T.
- When overridden by this field, for each of RA, WA, and TR, both inner- and outer- hints are set to the same value. Because it is not architecturally possible to express hints for types that are Device or Normal Non-cacheable, this field has no effect on memory types that are not Normal-WB or Normal-WT, whether such types are provided with a transaction or overridden using MTCFG/MemAttr.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Bits [7:5]

Reserved, RES0.

## MTCFG, bit [4]

Memory Type override.

| MTCFG   | Meaning                                            |
|---------|----------------------------------------------------|
| 0b0     | Use incoming memory type.                          |
| 0b1     | Override incoming memory type using MemAttr field. |

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## MemAttr, bits [3:0]

Memory type.

- Encoded the same as the STE.MemAttr field.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Accessing SMMU\_GBPA

Accesses to this register use the following encodings:

Accessible at offset 0x0044 from SMMUv3\_PAGE\_0

- When SMMU\_GBPA.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.

## Additional information

This register controls the global bypass attributes used for transactions from Non-secure StreamIDs (as determined by SEC\_SID) when SMMU\_CR0.SMMUEN == 0. Transactions passing through the SMMU when it is disabled might have their attributes overridden/assigned using this register.

Where Use incoming is selected, the attribute is taken from that supplied on the incoming interconnect, if supported. If the incoming interconnect does not supply the attribute, the SMMU generates a default attribute, which is selected for Use incoming. See Chapter 13 Attribute Transformation for details.

It is IMPLEMENTATION DEFINED whether MTCFG, SHCFG and ALLOCCFG apply to streams associated with PCIe devices or whether these attributes are treated as Use incoming for such streams regardless of the field values.

If SMMU\_IDR1.ATTR\_TYPES\_OVR == 0, MTCFG, SHCFG, ALLOCCFG are effectively fixed as Use incoming and it is IMPLEMENTATION SPECIFIC whether these fields read as zero or a previously written value. In this case, MemAttr reads as UNKNOWN.

If SMMU\_IDR1.ATTR\_PERMS\_OVR == 0, INSTCFG and PRIVCFG are effectively fixed as Use incoming and it is IMPLEMENTATION SPECIFIC whether these fields read as zero or a previously written value.

If the outgoing interconnect does not support a particular attribute, the value written to the corresponding field of this register is IGNORED and it is IMPLEMENTATION SPECIFIC whether the field reads as zero or a previously written value.

Update resets to zero and all other fields reset to an IMPLEMENTATION DEFINED state. This allows an implementation to provide useful default transaction attributes when software leaves the SMMU uninitialized.

## 6.3.14.1 Update procedure

This register must be written with a single 32-bit write that simultaneously sets the Update bit to 1. Software must then poll the Update bit which is cleared when the attribute update has completed.

The Update flag allows software to determine when a change in attributes takes effect. Transactions arriving at the SMMUafter completion of a GBPA update are guaranteed to take the new attributes written.

If GBPA is altered in the middle of a stream of transactions, the exact point in the sequence at which the change takes effect is UNPREDICTABLE.

Note: It is the responsibility of client devices to ensure that transactions generated prior to an update have completed, meaning that no more transactions will become globally visible to the required Shareability domain of the overridden attributes with attributes given by a previous value of the register. This is achieved in an IMPLEMENTATION DEFINED manner.

This register must only be written when Update == 0 (prior updates are complete). A write when an Update == 1, that is when a prior update is underway, is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write is IGNORED and update completes using the initial value. This is the only permitted behavior in SMMUv3.2 and later.
- Update completes with any value.
- -Note: The effective attribute in use might not match that read back from this register.

If this register is written without simultaneously setting Update to 1, the effect is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The write is IGNORED. This is the only permitted behavior in SMMUv3.2 and later.
- The written value is stored and is visible to future reads of the register, but does not affect transactions.
- The written value affects transactions at an UNPREDICTABLE update point:
- -There is no guarantee that all transactions arriving at the SMMU after the write will take the new value, or that all transactions prior to the write have completed.

When this register is written (correctly observing the requirements in this section), the new value is observable to future reads of the register even if they occur before the Update has completed.