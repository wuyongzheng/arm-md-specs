## 6.3.159 SMMU\_R\_DPT\_BASE\_CFG

The SMMU\_R\_DPT\_BASE\_CFG characteristics are:

## Purpose

Provides the configuraton for the Device Permission Table for Realm state.

## Configuration

This register is present only when SMMU\_R\_IDR3.DPT == 1. Otherwise, direct accesses to SMMU\_R\_DPT\_BASE\_CFG are RES0.

## Attributes

SMMU\_R\_DPT\_BASE\_CFG is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

| 31   | 24 23   | 20 19   | 16 15 14 13   | 3 2 0   |
|------|---------|---------|---------------|---------|
| RES0 | L0DPTSZ | RES0    | DPTGS         | DPTPS   |

## Bits [31:24]

Reserved, RES0.

## L0DPTSZ, bits [23:20]

This field advertises the number of least-significant address bits protected by each entry in the level 0 DPT.

| L0DPTSZ   | Meaning                                            |
|-----------|----------------------------------------------------|
| 0b0000    | 30-bits. Each entry covers 1GB of address space.   |
| 0b0100    | 34-bits. Each entry covers 16GB of address space.  |
| 0b0110    | 36-bits. Each entry covers 64GB of address space.  |
| 0b1001    | 39-bits. Each entry covers 512GB of address space. |

All other values are reserved.

It is invalid to configure this field to any of the following:

- A reserved encoding.
- An address size that exceeds the implemented physical address size advertised in SMMU\_IDR5.OAS.
- An address size that exceeds the DPT region size configured in SMMU\_R\_DPT\_BASE\_CFG.DPTPS.

This field is permitted to be cached in a TLB.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [19:16]

Reserved, RES0.

## DPTGS, bits [15:14]

DPT Granule size.

| DPTGS   | Meaning                                 |
|---------|-----------------------------------------|
| 0b00    | 4KB Invalid if SMMU_IDR5.GRAN4K == 0.   |
| 0b01    | 64KB Invalid if SMMU_IDR5.GRAN64K == 0. |
| 0b10    | 16KB Invalid if SMMU_IDR5.GRAN16K == 0. |
| 0b11    | Reserved                                |

This field is permitted to be cached in a TLB.

Note: Software should program this field to the mininal value that could be returned as the size of an ATS Translation Completion.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [13:3]

Reserved, RES0.

## DPTPS, bits [2:0]

The size of the memory region protected by the DPT, in terms of an encoded number of least-significant address bits.

| DPTPS   | Meaning        |
|---------|----------------|
| 0b000   | 32-bits 4GB.   |
| 0b001   | 36-bits 64GB.  |
| 0b010   | 40-bits 1TB.   |
| 0b011   | 42-bits 4TB.   |
| 0b100   | 44-bits 16TB.  |
| 0b101   | 48-bits 256TB. |
| 0b110   | 52-bits 4PB.   |
| 0b111   | Reserved.      |

Values exceeding the implemented physical address size, advertised in SMMU\_IDR5.OAS are invalid.

This field is permitted to be cached in a TLB.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_R\_DPT\_BASE\_CFG

Accesses to this register use the following encodings:

Accessible at offset 0x0208 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_CR0.DPT\_WALK\_EN == 1 or SMMU\_R\_CR0ACK.DPT\_WALK\_EN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.