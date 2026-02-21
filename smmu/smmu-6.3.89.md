## 6.3.89 SMMU\_S\_GBPMPAM

The SMMU\_S\_GBPMPAM characteristics are:

## Purpose

MPAM configuration register for global bypass transactions relating to the Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1 and SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_S\_GBPMPAM are RES0.

## Attributes

SMMU\_S\_GBPMPAM is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

The fields and their behavior are the same as SMMU\_GBPMPAM, but for the Secure programming interface. Any references to Non-secure registers in the SMMU\_GBPMPAM definition are replaced by their corresponding Secure equivalent.

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

## GBP\_PMG, bits [23:16]

PMG value for transactions in Global ByPass.

- This field determines the default PMG applied to all Secure client transactions that bypass translation, for more information see SMMU\_GBPMPAM.
- If SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and MPAM\_NS == 1, the maximum PMG value is SMMU\_MPAMIDR.PMG\_MAX.
- Otherwise, the maximum PMG value is SMMU\_S\_MPAMIDR.PMG\_MAX.
- Bits above the supported PMG bit width are RES0.
- If a value is programmed that is greater than the maximum supported PMG value, an UNKNOWN PMG is used.

The reset behavior of this field is:

- This field resets to 0x00 .

## GBP\_PARTID, bits [15:0]

PARTID value for transactions in Global ByPass.

- This field determines the default PARTID applied to all Secure client transactions that bypass translation. For more information see SMMU\_GBPMPAM.
- If SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and MPAM\_NS == 1, the maximum PARTID value is SMMU\_MPAMIDR.PARTID\_MAX.
- Otherwise, the maximum PARTID value is SMMU\_S\_MPAMIDR.PARTID\_MAX.
- Bits above the supported PARTID bit width are RES0.
- If a value is programmed that is greater than the maximum supported PARTID value, an UNKNOWN PARTID is used.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Accessing SMMU\_S\_GBPMPAM

Accesses to this register use the following encodings:

Accessible at offset 0x813C from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_S\_GBPMPAM.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.