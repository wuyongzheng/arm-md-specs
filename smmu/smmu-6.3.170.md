If QS == 0 the queue has one entry: zero bits of RD index are present and RD\_WRAP is bit zero.

When software increments RD, if the index would pass off the end of the queue it must be correctly wrapped to the queue size given by QS and RD\_WRAP toggled.

When SMMU\_R\_PRIQ\_BASE.LOG2SIZE is increased within its valid range, the value of this register's bits that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

Arm recommends that software initializes the register to a valid value before SMMU\_R\_CR0.PRIQEN is transitioned from 0 to 1.

## Accessing SMMU\_R\_PRIQ\_CONS

Accesses to this register use the following encodings:

Accessible at offset 0x00CC from SMMUv3\_R\_PAGE\_1

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## 6.3.170 ID\_REGS

Register offsets 0xFD0 -0xFFC are defined as a read-only identification register space. For Arm implementations of the SMMU architecture the assignment of this register space, and naming of registers in this space, is consistent with the Arm identification scheme for Arm CoreLink and Arm CoreSight components. Arm strongly recommends that other implementers also use this scheme to provide a consistent software discovery model.

For Arm implementations, the following assignment of fields, consistent with CoreSight ID registers [10], is used:

| Offset   | Name                       | Field   | Value   | Meaning                                            |
|----------|----------------------------|---------|---------|----------------------------------------------------|
| 0xFF0    | SMMU_CIDR0, Component ID0  | [7:0]   | 0x0D    | Preamble                                           |
| 0xFF4    | SMMU_CIDR1, Component ID1  | [7:4]   | 0xF     | CLASS                                              |
| 0xFF4    | SMMU_CIDR1, Component ID1  | [3:0]   | 0x0     | Preamble                                           |
| 0xFF8    | SMMU_CIDR2, Component ID2  | [7:0]   | 0x05    | Preamble                                           |
| 0xFFC    | SMMU_CIDR3, Component ID3  | [7:0]   | 0xB1    | Preamble                                           |
| 0xFE0    | SMMU_PIDR0, Peripheral ID0 | [7:0]   | IMPDEF  | PART_0: bits [7:0] of the Part number              |
| 0xFE4    | SMMU_PIDR1, Peripheral ID1 | [7:4]   | IMPDEF  | DES_0: bits [3:0] of the JEP106 Designer code      |
| 0xFE4    | SMMU_PIDR1, Peripheral ID1 | [3:0]   | IMPDEF  | PART_1: bits [11:8] of the Part number             |
| 0xFE8    | SMMU_PIDR2, Peripheral ID2 | [7:4]   | IMPDEF  | REVISION                                           |
| 0xFE8    | SMMU_PIDR2, Peripheral ID2 | [3]     | 1       | JEDEC-assigned value for DES always used           |
| 0xFE8    | SMMU_PIDR2, Peripheral ID2 | [2:0]   | IMPDEF  | DES_1: bits [6:4] bits of the JEP106 Designer code |

6.3. Register formats

| Offset   | Name                       | Field   | Value   | Meaning                                  |
|----------|----------------------------|---------|---------|------------------------------------------|
| 0xFEC    | SMMU_PIDR3, Peripheral ID3 | [7:4]   | IMPDEF  | REVAND                                   |
| 0xFEC    | SMMU_PIDR3, Peripheral ID3 | [3:0]   | IMPDEF  | CMOD                                     |
| 0xFD0    | SMMU_PIDR4, Peripheral ID4 | [7:4]   | 0       | SIZE                                     |
| 0xFD0    | SMMU_PIDR4, Peripheral ID4 | [3:0]   | IMPDEF  | DES_2: JEP106 Designer continuation code |
| 0xFD4    | SMMU_PIDR5, Peripheral ID5 |         | RES0    | Reserved                                 |
| 0xFD8    | SMMU_PIDR6, Peripheral ID6 |         | RES0    | Reserved                                 |
| 0xFDC    | SMMU_PIDR7, Peripheral ID7 |         | RES0    | Reserved                                 |

Fields outside of those defined in this table are RES0.

Note: The Designer code fields (DES\_*) fields for Arm-designed implementations use continuation code 0x4 and Designer code 0x3B .

Note: Non-Arm implementations that follow this CoreSight ID register layout must set the Designer fields appropriate to the implementer.