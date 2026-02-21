## 6.3.156 SMMU\_R\_GMPAM

The SMMU\_R\_GMPAM characteristics are:

## Purpose

Global MPAM configuration register for SMMU-originated transactions relating to the Realm state programming interface.

## Configuration

This register is present only when SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_R\_GMPAM are RES0.

## Attributes

SMMU\_R\_GMPAM is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Update, bit [31]

Update completion flag.

For more information see below.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:25]

Reserved, RES0.

## MPAM\_NS, bit [24]

## When SMMU\_R\_MPAMIDR.HAS\_MPAM\_NS == 1:

| MPAM_NS   | Meaning                                                           |
|-----------|-------------------------------------------------------------------|
| 0b0       | Accesses controlled by this register use Realm PARTID space.      |
| 0b1       | Accesses controlled by this register use Non-secure PARTID space. |

PARTID and PMG values for accesses for Realm state are determined according to Chapter 17 Memory System Resource Partitioning and Monitoring .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SO\_PMG, bits [23:16]

PMG for SMMU-originated accesses.

- This field determines the PMG of the SMMU-originated transactions described below.
- Bits above the supported PMG bit width, as indicated by SMMU\_R\_MPAMIDR.PMG\_MAX, are RES0.
- If a value is programmed that is greater than the corresponding PMG\_MAX, an UNKNOWN PMG is used.

The reset behavior of this field is:

- This field resets to 0x00 .

## SO\_PARTID, bits [15:0]

PARTID for SMMU-originated accesses.

- This field determines the PARTID of the SMMU-originated transactions described below.
- Bits above the supported PARTID bit width, as indicated by SMMU\_R\_MPAMIDR.PARTID\_MAX, are RES0.
- If a value is programmed that is greater than SMMU\_R\_MPAMIDR.PARTID\_MAX, an UNKNOWN PARTID is used.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Additional Information

The SO\_PMG and SO\_PARTID values determine the MPAM attributes applied to the following SMMU-originated accesses that are associated with the Realm programming interface:

- L1STD, STE and VMS accesses.
- Queue accesses.
- SMMUcore MSIs.

The Update flag behaves the same as the SMMU\_GBPA.Update mechanism. It indicates that a change to this register has been accepted and when the Update flag is observed to be zero after a correct update procedure, the new values are guaranteed to be applied to future SMMU-originated accesses.

## Accessing SMMU\_R\_GMPAM

This register must only be written when Update == 0 (prior updates are complete). A write when an Update == 1, that is when a prior update is underway, is IGNORED. A write of new values that does not set Update == 1 is IGNORED.

When this register is written, correctly observing the requirements in this section, the new value is observable to future reads of the register even if they occur before the Update has completed.

Accesses to this register use the following encodings:

Accessible at offset 0x0138 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_GMPAM.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.