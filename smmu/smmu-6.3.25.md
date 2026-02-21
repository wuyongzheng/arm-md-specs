## 6.3.25 SMMU\_STRTAB\_BASE\_CFG

The SMMU\_STRTAB\_BASE\_CFG characteristics are:

## Purpose

Configuration of Stream table.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_STRTAB\_BASE\_CFG is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

| 31   | 18 17 16 15   | 11 10   | 6 5   | 0        |
|------|---------------|---------|-------|----------|
| RES0 | FMT           | RES0    | SPLIT | LOG2SIZE |

## Bits [31:18]

Reserved, RES0.

## FMT, bits [17:16]

## When SMMU\_IDR0.ST\_LEVEL != 0b00:

Format of Stream table.

| FMT   | Meaning                                                                |
|-------|------------------------------------------------------------------------|
| 0b00  | Linear - ADDR points to an array of STEs.                              |
| 0b01  | 2-level - ADDR points to an array of Level 1 Stream Table Descriptors. |

- Other values are reserved, behave as 0b00 .

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:11]

Reserved, RES0.

## SPLIT, bits [10:6]

## When SMMU\_IDR0.ST\_LEVEL != 0b00:

StreamID split point for multi-level table.

- This field determines the split point of a 2-level Stream table, selected by the number of bits at the bottom level.
- This field is IGNORED if FMT == 0b00 .

| SPLIT   | Meaning                     |
|---------|-----------------------------|
| 0b00110 | 6 bits - 4KB leaf tables.   |
| 0b01000 | 8 bits - 16KB leaf tables.  |
| 0b01010 | 10 bits - 64KB leaf tables. |

- Other values are reserved, behave as 6 ( 0b0110 ).
- The upper-level L1STD is located using StreamID[LOG2SIZE - 1:SPLIT] and this indicates the lowest-level table which is indexed by StreamID[SPLIT - 1:0].
- -For example, selecting SPLIT == 6 ( 0b0110 ) causes StreamID[5:0] to be used to index the lowest level Stream table and StreamID[LOG2SIZE - 1:6] to index the upper level table.
- Note: If SPLIT &gt;= LOG2SIZE, a single upper-level descriptor indicates one bottom-level Stream table with 2 LOG2SIZE usable entries. The L1STD.Span value's valid range is up to SPLIT + 1, but not all of this Span is accessible, as it is not possible to use a StreamID &gt;= 2 LOG2SIZE .

Note: Arm recommends that a Linear table, FMT == 0b00 , is used instead of programming SPLIT &gt;= LOG2SIZE.

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LOG2SIZE, bits [5:0]

Table size as log2(entries).

- The maximum StreamID value that can be used to index into the Stream table is 2 LOG2SIZE - 1. The StreamID range is equal to the number of STEs in a linear Stream table or the maximum sum of the STEs in all second-level tables. The number of L1STDs in the upper level of a 2-level table is MAX(1, 2 LOG2SIZE-SPLIT ). Except for readback of a written value, the effective LOG2SIZE is MIN(LOG2SIZE, SMMU\_IDR1.SIDSIZE) for the purposes of input StreamID range checking and upper/lower/linear Stream table index address calculation.

The reset behavior of this field is:

- When SMMU\_IDR1.TABLES\_PRESET == 1, this field resets to an IMPLEMENTATION DEFINED value.
- Otherwise, this field resets to an UNKNOWN value.

## Additional Information

A transaction having a StreamID &gt;= 2 LOG2SIZE is out of range. Such a transaction is terminated with abort and a C\_BAD\_STREAMID event is recorded if permitted by SMMU\_CR2.RECINVSID.

## Accessing SMMU\_STRTAB\_BASE\_CFG

SMMU\_STRTAB\_BASE\_CFG is Guarded by SMMU\_CR0.SMMUEN and must only be written when SMMU\_CR0.SMMUEN == 0.

See SMMU\_STRTAB\_BASE for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x0088 from SMMUv3\_PAGE\_0

Chapter 6. Memory map and registers 6.3. Register formats

- When SMMU\_IDR1.TABLES\_PRESET == 1, accesses to this register are RO.
- When SMMU\_CR0.SMMUEN == 0 and SMMU\_CR0ACK.SMMUEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.