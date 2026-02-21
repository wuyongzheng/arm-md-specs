## 6.3.42 SMMU\_GMPAM

The SMMU\_GMPAM characteristics are:

## Purpose

Global MPAM configuration register for SMMU-originated transactions relating to the Non-secure programming interface.

## Configuration

This register is present only when SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_GMPAM are RES0.

## Attributes

SMMU\_GMPAM is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31 30   | 24 23   | 16 15   | 0         |
|---------|---------|---------|-----------|
|         | RES0    | SO_PMG  | SO_PARTID |

Update

## Update, bit [31]

Update completion flag.

For more information see below.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:24]

Reserved, RES0.

## SO\_PMG, bits [23:16]

PMG for SMMU-originated accesses.

- This field determines the PMG of the SMMU-originated transactions described below.
- Bits above the supported PMG bit width, as indicated by SMMU\_MPAMIDR.PMG\_MAX, are RES0.
- If a value is programmed that is greater than the corresponding PMG\_MAX, an UNKNOWN PMG is used.

The reset behavior of this field is:

- This field resets to 0x00 .

## SO\_PARTID, bits [15:0]

PARTID for SMMU-originated accesses.

- This field determines the PARTID of the SMMU-originated transactions described below.
- Bits above the supported PARTID bit width, as indicated by SMMU\_MPAMIDR.PARTID\_MAX, are RES0.
- If a value is programmed that is greater than SMMU\_MPAMIDR.PARTID\_MAX, an UNKNOWN PARTID is used.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Additional Information

The SO\_PMG and SO\_PARTID values determine the MPAM attributes applied to the following SMMU-originated accesses that are associated with the Non-secure programming interface:

- L1STD and STE accesses.
- Queue accesses.
- SMMUcore MSIs.

The Update flag behaves the same as the SMMU\_GBPA.Update mechanism. It indicates that a change to this register has been accepted and when the Update flag is observed to be zero after a correct update procedure, the new values are guaranteed to be applied to future SMMU-originated accesses.

## Accessing SMMU\_GMPAM

This register must only be written when Update == 0 (prior updates are complete). A write when an Update == 1, that is when a prior update is underway, is IGNORED. A write of new values that does not set Update == 1 is IGNORED.

When this register is written, correctly observing the requirements in this section, the new value is observable to future reads of the register even if they occur before the Update has completed.

Accesses to this register use the following encodings:

Accessible at offset 0x0138 from SMMUv3\_PAGE\_0

- When SMMU\_GMPAM.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.