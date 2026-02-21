## 6.3.43 SMMU\_GBPMPAM

The SMMU\_GBPMPAM characteristics are:

## Purpose

MPAMconfiguration register for global bypass transactions relating to the Non-secure programming interface.

## Configuration

This register is present only when SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_GBPMPAM are RES0.

## Attributes

SMMU\_GBPMPAM is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31 30   | 24 23   | 16 15   | 0   |
|---------|---------|---------|-----|
|         | RES0    | GBP_PMG |     |
| Update  |         |         |     |

## Update, bit [31]

Update completion flag.

For more information see below.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:24]

Reserved, RES0.

## GBP\_PMG, bits [23:16]

PMG value for transactions in Global ByPass

- This field determines the default PMG applied to all client transactions that bypass translation for the reasons described below.
- Bits above the supported PMG bit width, as indicated by SMMU\_MPAMIDR.PMG\_MAX, are RES0.
- If a value is programmed that is greater than SMMU\_MPAMIDR.PMG\_MAX, an UNKNOWN PMG is used.

The reset behavior of this field is:

- This field resets to 0x00 .

## GBP\_PARTID, bits [15:0]

PARTID value for transactions in Global ByPass.

- This field determines the default PARTID applied to all client transactions that bypass translation for the reasons described below.
- Bits above the supported PARTID bit width, as indicated by SMMU\_MPAMIDR.PARTID\_MAX, are RES0.
- If a value is programmed that is greater than SMMU\_MPAMIDR.PARTID\_MAX, an UNKNOWN PARTID is used.

The reset behavior of this field is:

- This field resets to 0x0000 .

## Additional Information

The GBP\_PMG and GBP\_PARTID attributes apply to client transactions from Non-secure streams that bypass translation because:

- The SMMU programming interface is disabled with SMMU\_CR0.SMMUEN == 0, or,
- The transaction is ATS Translated and ATSCHK == 0. See section 3.9.1 ATS Interface .

When SMMU\_CR0.SMMUEN == 1, the PMG and PARTID of a non-ATS Translated transaction are determined by STE, and if appropriate, CD configuration.

The Update flag behaves the same as the SMMU\_GBPA.Update mechanism. It indicates that a change to this register has been accepted and when the Update flag is observed to be zero after a correct update procedure, the new values are guaranteed to be applied to future client transactions.

## Accessing SMMU\_GBPMPAM

This register must only be written when Update == 0 (prior updates are complete). A write when an Update == 1, that is when a prior update is underway, is IGNORED. A write of new values that does not set Update == 1 is IGNORED.

When this register is written, correctly observing the requirements in this section, the new value is observable to future reads of the register even if they occur before the Update has completed.

Accesses to this register use the following encodings:

Accessible at offset 0x013C from SMMUv3\_PAGE\_0

- When SMMU\_GBPMPAM.Update == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.