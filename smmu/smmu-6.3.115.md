## 6.3.115 SMMU\_ROOT\_GPT\_BASE\_CFG

The SMMU\_ROOT\_GPT\_BASE\_CFG characteristics are:

## Purpose

Control register for Granule Protection Checks.

The fields in SMMU\_ROOT\_GPT\_BASE\_CFG are the same as for GPCCR\_EL3, except there is no copy of GPCCR\_EL3.GPC. See SMMU\_ROOT\_CR0.GPCEN.

Configuration of reserved or invalid values leads to a GPT lookup error, reported as Invalid configuration of GPT configuration registers.

See also:

- 3.25.4 Reporting of GPC faults .

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_GPT\_BASE\_CFG is a 64-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## L0GPTSZ, bits [23:20]

Level 0 GPT entry size.

This field specifies the number of least significant address bits protected by each entry in the level 0 GPT.

| L0GPTSZ   | Meaning                                            |
|-----------|----------------------------------------------------|
| 0b0000    | 30-bits. Each entry covers 1GB of address space.   |
| 0b0100    | 34-bits. Each entry covers 16GB of address space.  |
| 0b0110    | 36-bits. Each entry covers 64GB of address space.  |
| 0b1001    | 39-bits. Each entry covers 512GB of address space. |

Access to this field is RO.

## Bits [19:18]

Reserved, RES0.

## GPCP, bit [17]

Granule Protection Check Priority.

| GPCP   | Meaning                                                                                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | All GPC faults are reported with a priority consistent with the GPC being performed on any access to physical address space.                                                                                                                                |
| 0b1    | A GPC fault for the fetch of a Table descriptor for a stage 2 translation table walk might not be generated or reported. All other GPC faults are reported with a priority consistent with the GPC being performed on any access to physical address space. |

This field is permitted to be cached in a TLB.

An implementation is permitted to treat this field as RES0, with an Effective value of 0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bit [16]

Reserved, RES0.

## PGS, bits [15:14]

Physical Granule size.

| PGS   | Meaning                                  |
|-------|------------------------------------------|
| 0b00  | 4KB. Invalid if SMMU_IDR5.GRAN4K == 0.   |
| 0b01  | 64KB. Invalid if SMMU_IDR5.GRAN64K == 0. |
| 0b10  | 16KB. Invalid if SMMU_IDR5.GRAN16K == 0. |
| 0b11  | Reserved.                                |

The value of this field is permitted to be cached in a TLB.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## SH, bits [13:12]

GPT fetch Shareability attribute

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b01 | Reserved.        |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

Fetches to the GPT are made to the shareability domain configured in this field.

If both ORGN and IRGN are configured with Non-cacheable attributes, it is invalid to configure this field to values other than Outer Shareable.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## ORGN, bits [11:10]

GPT fetch Outer cacheability attribute.

| ORGN   | Meaning                                                                       |
|--------|-------------------------------------------------------------------------------|
| 0b00   | Normal memory, Outer Non-cacheable.                                           |
| 0b01   | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10   | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11   | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

Fetches of GPT information are made with the Outer cacheability attributes configured in this field.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## IRGN, bits [9:8]

GPT fetch Inner cacheability attribute.

| IRGN   | Meaning                                                                       |
|--------|-------------------------------------------------------------------------------|
| 0b00   | Normal memory, Inner Non-cacheable.                                           |
| 0b01   | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10   | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11   | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

Fetches of GPT information are made with the Inner cacheability attributes configured in this field.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [7:3]

Reserved, RES0.

## PPS, bits [2:0]

Protected physical address size.

The bit width of the memory region protected by the GPT.

| PPS   | Meaning                                 |
|-------|-----------------------------------------|
| 0b000 | 32 bits, 4GB protected address space.   |
| 0b001 | 36 bits, 64GB protected address space.  |
| 0b010 | 40 bits, 1TB protected address space.   |
| 0b011 | 42 bits, 4TB protected address space.   |
| 0b100 | 44 bits, 16TB protected address space.  |
| 0b101 | 48 bits, 256TB protected address space. |
| 0b110 | 52 bits, 4PB protected address space.   |
| 0b111 | Reserved.                               |

Values exceeding the implemented physical address size, advertised in SMMU\_IDR5.OAS, are invalid.

This field is permitted to be cached in a TLB or Configuration cache.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Accessing SMMU\_ROOT\_GPT\_BASE\_CFG

Accesses to this register use the following encodings:

Accessible at offset 0x0030 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_ROOT\_CR0.GPCEN == 1 or SMMU\_ROOT\_CR0ACK.GPCEN == 1, accesses to this register are RO.
- Otherwise, accesses to this register are RW.