## 6.3.87 SMMU\_S\_MPAMIDR

The SMMU\_S\_MPAMIDR characteristics are:

## Purpose

MPAM capability identification register for Secure state.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1 and SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_S\_MPAMIDR are RES0.

## Attributes

SMMU\_S\_MPAMIDR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

Similar to SMMU\_MPAMIDR, but for MPAM capability identification for Secure state.

It is valid when SMMU\_IDR3.MPAM == 1 in the same manner as SMMU\_MPAMIDR.

## Bits [31:26]

Reserved, RES0.

## HAS\_MPAM\_NS, bit [25]

| HAS_MPAM_NS   | Meaning                                                    |
|---------------|------------------------------------------------------------|
| 0b0           | The MPAM_NS mechanism for Secure state is not implemented. |
| 0b1           | The MPAM_NS mechanism for Secure state is implemented.     |

See section 17.7 Determination of PARTID space values . If Realm state is implemented, this field has the same value as SMMU\_R\_MPAMIDR.HAS\_MPAM\_NS.

## Bit [24]

Reserved, RES0.

## PMG\_MAX, bits [23:16]

- The maximum PMG value that is permitted to be used in Secure state.

## PARTID\_MAX, bits [15:0]

- The maximum PARTID value that is permitted to be used in Secure state.

## Additional Information

The PMG bit width is defined as the bit position of the most significant 1 in PMG\_MAX[7:0], plus one, or is defined as zero if PMG\_MAX is zero.

Note: For example, if PMG\_MAX == 0x0f , the PMG bit width is 4.

The PARTID bit width is defined as the bit position of the most significant 1 in PARTID\_MAX[15:0], plus one, or is defined as zero if PARTID\_MAX is zero.

Note: For example, if PARTID\_MAX == 0x0034 , the PARTID bit width is 6.

Note: PMG\_MAX and PARTID\_MAX specify the maximum values of each ID type that can be configured in the corresponding Security state. These values do not describe properties of the rest of the system, which are discovered using mechanisms that are outside the scope of this specification.

Note: Either field is architecturally permitted to be zero-sized, but Arm recommends that PARTID\_MAX is non-zero when MPAM is implemented.

## Accessing SMMU\_S\_MPAMIDR

Accesses to this register use the following encodings:

Accessible at offset 0x8130 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.