## 6.3.63 SMMU\_S\_GBPA

The SMMU\_S\_GBPA characteristics are:

## Purpose

Secure Global Bypass Attributes.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_GBPA are RES0.

## Attributes

SMMU\_S\_GBPA is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Update, bit [31]

Update completion flag, see section 6.3.14.1 Update procedure .

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

Instruction/Data override.

| INSTCFG   | Meaning       |
|-----------|---------------|
| 0b00      | Use incoming. |

| INSTCFG   | Meaning                     |
|-----------|-----------------------------|
| 0b01      | Reserved, behaves as 0b00 . |
| 0b10      | Data.                       |
| 0b11      | Instruction.                |

- INSTCFG only affects reads. Writes are always output as Data.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## PRIVCFG, bits [17:16]

User/Privileged override.

| PRIVCFG   | Meaning                     |
|-----------|-----------------------------|
| 0b00      | Use incoming.               |
| 0b01      | Reserved, behaves as 0b00 . |
| 0b10      | Unprivileged.               |
| 0b11      | Privileged.                 |

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## NSCFG, bits [15:14]

NS attribute override.

| NSCFG   | Meaning                     |
|---------|-----------------------------|
| 0b00    | Use incoming.               |
| 0b01    | Reserved, behaves as 0b00 . |
| 0b10    | Secure.                     |
| 0b11    | Non-secure.                 |

- If SMMU\_IDR1.ATTR\_PERMS\_OVR == 0 NSCFG is fixed as Use incoming and it is IMPLEMENTATION SPECIFIC whether this field reads as zero or a previously written value.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## SHCFG, bits [13:12]

Shareability override.

| SHCFG   | Meaning        |
|---------|----------------|
| 0b00    | Non-shareable. |

| SHCFG   | Meaning          |
|---------|------------------|
| 0b01    | Use incoming.    |
| 0b10    | Outer Shareable. |
| 0b11    | Inner Shareable. |

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## ALLOCCFG, bits [11:8]

Allocation configuration

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

Memory type override.

| MTCFG   | Meaning                                            |
|---------|----------------------------------------------------|
| 0b0     | Use incoming memory type.                          |
| 0b1     | Override incoming memory type using MemAttr field. |

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## MemAttr, bits [3:0]

Memory type.

The reset behavior of this field is:

- This field resets to an IMPLEMENTATION DEFINED value.

## Additional Information

This register controls the Secure global bypass attributes used for transactions from Secure StreamIDs when SMMU\_S\_CR0.SMMUEN == 0. Transactions passing through the SMMU when it is disabled might have their attributes overridden or assigned using this register.

## Accessing SMMU\_S\_GBPA

Accesses to this register use the following encodings:

Accessible at offset 0x8044 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_GBPA.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.