## 6.3.161 SMMU\_R\_MECIDR

The SMMU\_R\_MECIDR characteristics are:

## Purpose

Provides information about the number of bits of MECID supported by the SMMU.

## Configuration

This register is present only when SMMU\_R\_IDR3.MEC == 1. Otherwise, direct accesses to SMMU\_R\_MECIDR are RES0.

## Attributes

SMMU\_R\_MECIDR is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

| 31   | 4 3   |
|------|-------|

## Bits [31:4]

Reserved, RES0.

## MECIDSIZE, bits [3:0]

The number of bits minus one of MECID supported by the SMMU.

The maximum permitted value is 0xF which indicates a MECID width of 16 bits.

The value 0x0 is a valid encoding and indicates that one bit of MECID is supported.

## Additional Information

Arm strongly recommends that the MECID bit width supported by the SMMU matches or exceeds the width supported by the PEs in the system.

## Accessing SMMU\_R\_MECIDR

Accesses to this register use the following encodings:

Accessible at offset 0x0220 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.