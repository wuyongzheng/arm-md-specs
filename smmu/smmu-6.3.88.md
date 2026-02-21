## 6.3.88 SMMU\_S\_GMPAM

The SMMU\_S\_GMPAM characteristics are:

## Purpose

Global MPAM configuration register for SMMU-originated transactions relating to the Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1 and SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_S\_GMPAM are RES0.

## Attributes

SMMU\_S\_GMPAM is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

The fields and their behavior are the same as SMMU\_GMPAM, but for the Secure programming interface. Any references to Non-secure registers in the SMMU\_GMPAM definition are replaced by their corresponding Secure equivalent.

## Update, bit [31]

Update completion flag.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:25]

Reserved, RES0.

## MPAM\_NS, bit [24]

## When SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1:

| MPAM_NS   | Meaning                                                           |
|-----------|-------------------------------------------------------------------|
| 0b0       | Accesses controlled by this register use Secure PARTID space.     |
| 0b1       | Accesses controlled by this register use Non-secure PARTID space. |

PARTID and PMG values for accesses for Secure state are determined according to section 17.7 Determination of PARTID space values .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SO\_PMG, bits [23:16]

PMG for SMMU-originated accesses.

- This field determines the PMG of the SMMU-originated transactions for Secure state, for more information see SMMU\_GMPAM.
- If SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and MPAM\_NS == 1, the maximum PMG value is SMMU\_MPAMIDR.PMG\_MAX.
- Otherwise, the maximum PMG value is SMMU\_S\_MPAMIDR.PMG\_MAX.
- Bits above the supported PMG bit width, as indicated by the maximum PMG value, are RES0.
- If a value is programmed that is greater than the maximum supported PMG value, an UNKNOWN PMG is used.

The reset behavior of this field is:

- This field resets to 0x00 .

## SO\_PARTID, bits [15:0]

PARTID for SMMU-originated accesses.

- This field determines the PARTID of SMMU-originated transactions for Secure state. For more information see SMMU\_GMPAM.
- If SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and MPAM\_NS == 1, the maximum PARTID value is SMMU\_MPAMIDR.PARTID\_MAX.
- Otherwise, the maximum PARTID value is SMMU\_S\_MPAMIDR.PARTID\_MAX.
- Bits above the supported PARTID bit width, as indicated by the maximum PARTID value, are RES0.
- If a value is programmed that is greater than the maximum supported PARTID value, an UNKNOWN PARTID is used.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Accessing SMMU\_S\_GMPAM

Accesses to this register use the following encodings:

Accessible at offset 0x8138 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_GMPAM.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.