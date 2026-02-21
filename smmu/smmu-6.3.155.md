## 6.3.155 SMMU\_R\_MPAMIDR

The SMMU\_R\_MPAMIDR characteristics are:

## Purpose

MPAM capability identification register for Realm state.

## Configuration

This register is present only when SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_R\_MPAMIDR are RES0.

## Attributes

SMMU\_R\_MPAMIDR is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:26]

Reserved, RES0.

## HAS\_MPAM\_NS, bit [25]

Support for MPAM\_NS configuration for Realm state.

| HAS_MPAM_NS   | Meaning                                               |
|---------------|-------------------------------------------------------|
| 0b0           | No support for MPAM_NS configuration for Realm state. |
| 0b1           | Support for MPAM_NS configuration for Realm state.    |

If Secure state is implemented this field has the same value as SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS. If Secure state is not implemented this field is permitted to be zero or one.

## Bit [24]

Reserved, RES0.

## PMG\_MAX, bits [23:16]

- This field has the same value as SMMU\_MPAMIDR.PMG\_MAX.
- The maximum PMG value that is permitted to be used in Realm state.

## PARTID\_MAX, bits [15:0]

- This field has the same value as SMMU\_MPAMIDR.PARTID\_MAX.
- The maximum PARTID value that is permitted to be used in Realm state.

## Additional Information

This register has the same behavior as the SMMU\_MPAMIDR register.

## Accessing SMMU\_R\_MPAMIDR

Accesses to this register use the following encodings:

Accessible at offset 0x0130 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.