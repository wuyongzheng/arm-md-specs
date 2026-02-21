## 6.3.41 SMMU\_MPAMIDR

The SMMU\_MPAMIDR characteristics are:

## Purpose

MPAM capability identification register for Non-secure state.

## Configuration

This register is present only when SMMU\_IDR3.MPAM == 1. Otherwise, direct accesses to SMMU\_MPAMIDR are RES0.

## Attributes

SMMU\_MPAMIDR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

| 31   | 24 23   | 16 15      | 0   |
|------|---------|------------|-----|
| RES0 | PMG_MAX | PARTID_MAX |     |

## Bits [31:24]

Reserved, RES0.

## PMG\_MAX, bits [23:16]

- The maximum PMG value that is permitted to be used in Non-secure state.

## PARTID\_MAX, bits [15:0]

- The maximum PARTID value that is permitted to be used in Non-secure state.

## Additional Information

The PMG bit width is defined as the bit position of the most significant 1 in PMG\_MAX[7:0], plus one, or is defined as zero if PMG\_MAX is zero.

Note: For example, if PMG\_MAX == 0x0f , the PMG bit width is 4.

The PARTID bit width is defined as the bit position of the most significant 1 in PARTID\_MAX[15:0], plus one, or is defined as zero if PARTID\_MAX is zero.

Note: For example, if PARTID\_MAX == 0x0034 , the PARTID bit width is 6.

Note: PMG\_MAX and PARTID\_MAX specify the maximum values of each ID type that can be configured in the corresponding Security state. These values do not describe properties of the rest of the system, which are discovered using mechanisms that are outside the scope of this specification.

Note: Either field is architecturally permitted to be zero-sized, but Arm recommends that PARTID\_MAX is non-zero when MPAM is implemented.

## Accessing SMMU\_MPAMIDR

Accesses to this register use the following encodings:

Accessible at offset 0x0130 from SMMUv3\_PAGE\_0

Accesses to this register are RO.