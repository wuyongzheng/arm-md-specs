## 6.3.53 SMMU\_S\_IDR1

The SMMU\_S\_IDR1 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Secure programming interface.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_IDR1 are RES0.

## Attributes

SMMU\_S\_IDR1 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

- Note: If the SMMU implementation supports SubstreamIDs, the size of the SubstreamID that is provided for Secure StreamIDs is the same as the size that is provided for Non-secure StreamIDs. Therefore, there is no separate Secure SSIDSIZE option.

## SECURE\_IMPL, bit [31]

Secure state implemented.

| SECURE_IMPL   | Meaning                                                                            |
|---------------|------------------------------------------------------------------------------------|
| 0b0           | The SMMUdoes not implement Secure state. All SMMU_S_* Secure registers are RAZ/WI. |
| 0b1           | The SMMUimplements Secure state.                                                   |

When SECURE\_IMPL == 1, stage 1 must be supported, and therefore SMMU\_IDR0.S1P == 1.

If SECURE\_IMPL == 1 and SMMU\_IDR0.RME\_IMPL == 1, then all the following apply:

- SMMU\_S\_IDR1.SEL2 == 1.
- The EL3 StreamWorld is not supported.
- It is possible to report each of F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH, and F\_WALK\_EABT with GPCF == 1 in the Secure Event queue.

See also:

- 3.10.2 Support for Secure state .

## Bit [30]

Reserved, RES0.

## SEL2, bit [29]

Secure EL2 and Secure stage 2 support.

| SEL2   | Meaning                                                                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Secure EL2 and Secure stage 2 are not supported.                                                                                                                                                     |
| 0b1    | Secure EL2 is supported and Secure STEs are permitted to be configured with STE.STRW == 0b10 . Secure stage 2 is supported and Secure STEs are permitted to be configured with STE.Config == 0b11x . |

- Secure EL2 and Secure stage 2 support is optional in SMMUv3.2 and later.
- SEL2 == 0 if SMMU\_IDR0.S1P == 0 or if SMMU\_IDR0.S2P == 0.

## Bits [28:6]

Reserved, RES0.

## S\_SIDSIZE, bits [5:0]

Max bits of Secure StreamID.

- Equivalent to SMMU\_IDR1.SIDSIZE and encoded the same way, this field determines the maximum Secure StreamID value and therefore the maximum size of the Secure Stream table.

## Accessing SMMU\_S\_IDR1

Accesses to this register use the following encodings:

Accessible at offset 0x8004 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.