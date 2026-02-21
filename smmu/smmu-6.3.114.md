## 6.3.114 SMMU\_ROOT\_GPT\_BASE

The SMMU\_ROOT\_GPT\_BASE characteristics are:

## Purpose

Control register for Granule Protection Table base address.

This register is analogous to GPTBR\_EL3.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_GPT\_BASE is a 64-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

| 63          | 52 51   |             | 32   |
|-------------|---------|-------------|------|
| RES0        |         | ADDR[51:12] |      |
| 31          | 12 11   |             | 0    |
| ADDR[51:12] |         | RES0        |      |

## Bits [63:52]

Reserved, RES0.

## ADDR, bits [51:12]

Base address of the L0GPT, bits [51:12].

The SMMU always treats this address as being in the Root physical address space.

This field represents bits [51:12] of the level 0 GPT base address.

Bits that are taken to be zero are RES0 and the SMMU treats them as zero when computing addresses for lookups.

Bits above the implemented output address size, advertised in SMMU\_IDR5.OAS, are RES0.

The level 0 GPT is aligned in memory to the greater of:

- The size of the level 0 GPT in bytes.
- 4KB.

Bits [x:0] of the base address are taken to be zero, where:

- x = Max(pps - l0gptsz + 2, 11)
- pps is derived from SMMU\_ROOT\_GPT\_BASE\_CFG.PPS as follows:

| PPS   |   pps |
|-------|-------|
| 0b000 |    32 |
| 0b001 |    36 |
| 0b010 |    40 |
| 0b011 |    42 |

| PPS   |   pps |
|-------|-------|
| 0b100 |    44 |
| 0b101 |    48 |
| 0b110 |    52 |

- l0gptsz is derived from SMMU\_ROOT\_GPT\_BASE\_CFG.L0GPTSZ as follows:

| L0GPTSZ   |   l0gptsz |
|-----------|-----------|
| 0b0000    |        30 |
| 0b0100    |        34 |
| 0b0110    |        36 |
| 0b1001    |        39 |

If x is greater than 11, then BADDR[x - 12:0] are RES0.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Accessing SMMU\_ROOT\_GPT\_BASE

After a write of this register, the SMMU is not required to use the new base address value until completion of a subsequent TLBI by PA ALL operation.

Completion of such a TLBI by PA ALL operation also guarantees that the SMMU has completed all outstanding GPT walks that used the old configuration.

Accesses to this register use the following encodings:

Accessible at offset 0x0028 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_ROOT\_CR0.GPCEN == 0 and SMMU\_ROOT\_CR0ACK.GPCEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.