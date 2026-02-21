## 6.3.6 SMMU\_IDR5

The SMMU\_IDR5 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Non-secure programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IDR5 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## STALL\_MAX, bits [31:16]

Maximum number of outstanding stalled transactions supported by the SMMU and system.

- The SMMU guarantees that the total number of Stall fault records that will be recorded in any Event queue, without any having been the subject of a resume or terminate command, will not exceed this number.
- This field is RES0 if SMMU\_S\_IDR1.SECURE\_IMPL == 0 and SMMU\_IDR0.STALL\_MODEL == 0b01 , or if SMMU\_S\_IDR1.SECURE\_IMPL == 1 and SMMU\_S\_IDR0.STALL\_MODEL == 0b01 .

## Bits [15:12]

Reserved, RES0.

## VAX, bits [11:10]

Virtual Address eXtend.

| VAX   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b00  | Virtual addresses of up to 48 bits can be translated per CD.TTBx. |
| 0b01  | Virtual addresses of up to 52 bits can be translated per CD.TTBx. |
| 0b10  | Virtual addresses of up to 56 bits can be translated by CD.TTBx.  |

- Other values reserved.
- In SMMUv3.0, this field is RES0.
- An implementation is permitted to support VAX == 0b01 independently of whether OAS == 0b110 .
- If VAX &gt;= 0b01 , then at least one of the following must be true:
- SMMU\_IDR5.GRAN64K == 1.
- SMMU\_IDR5.DS == 1 and one or both of SMMU\_IDR5.GRAN4K and SMMU\_IDR5.GRAN16K are 1.

- If SMMU\_IDR5.VAX indicates support for 56-bit input addresses, then SMMU\_IDR5.D128 is 1.

## Bit [9]

Reserved, RES0.

## D128, bit [8]

Support for 128-bit translation table descriptors.

| D128   | Meaning                                           |
|--------|---------------------------------------------------|
| 0b0    | 128-bit VMSAv9-128 descriptors are not supported. |
| 0b1    | 128-bit VMSAv9-128 descriptors are supported.     |

Note: Support for VMSAv8-64 and VMSAv8-32 descriptor formats is indicated in SMMU\_IDR0.TTF.

If this field is 1, then the following bits are all 1:

- SMMU\_IDR0.TTF[1], indicating support for VMSAv8-64 descriptors.
- SMMU\_IDR3.{S1PI, S2PO, AIE, MTEPERM}.

If this field is 1, then SMMU\_IDR0.TTF[0] is 0, meaning that VMSAv8-32 LPAE format descriptors are not supported.

## DS, bit [7]

Support for 52-bit address sizes when using 4KB and 16KB granules, if they are implemented.

| DS   | Meaning                                                                                      |
|------|----------------------------------------------------------------------------------------------|
| 0b0  | 52-bit address sizes when using 4KB and 16KB granules not supported.                         |
| 0b1  | 52-bit address sizes supported when using 4KB and 16KB granules, if they are each supported. |

This feature requires that the SMMU supports both or either of 4KB or 16KB granules.

If this bit is 1, the SMMU implements behaviors equivalent to the FEAT\_LPA2 feature in the PE architecture.

If this bit is 1 then the SMMU must additionally support at least 52-bit VA size, as indicated by SMMU\_IDR5.VAX.

This field is RES0 if both SMMU\_IDR5.GRAN4K == 0 and SMMU\_IDR5.GRAN16K == 0.

## GRAN64K, bit [6]

64KB translation granule supported.

| GRAN64K   | Meaning                                 |
|-----------|-----------------------------------------|
| 0b0       | 64KB translation granule not supported. |
| 0b1       | 64KB translation granule supported.     |

## GRAN16K, bit [5]

16KB translation granule supported.

| GRAN16K   | Meaning                                 |
|-----------|-----------------------------------------|
| 0b0       | 16KB translation granule not supported. |
| 0b1       | 16KB translation granule supported.     |

## GRAN4K, bit [4]

4KB translation granule supported.

| GRAN4K   | Meaning                                |
|----------|----------------------------------------|
| 0b0      | 4KB translation granule not supported. |
| 0b1      | 4KB translation granule supported.     |

- When SMMU\_IDR0.TTF[0] == 1, that is when VMSAv8-32 LPAE translation tables are supported, this field is RES1.

## Bit [3]

Reserved, RES0.

## OAS, bits [2:0]

Output Address Size.

Size of physical address output from SMMU.

| OAS   | Meaning                                       |
|-------|-----------------------------------------------|
| 0b000 | 32 bits.                                      |
| 0b001 | 36 bits.                                      |
| 0b010 | 40 bits.                                      |
| 0b011 | 42 bits.                                      |
| 0b100 | 44 bits.                                      |
| 0b101 | 48 bits.                                      |
| 0b110 | 52 bits. In SMMUv3.0, this value is Reserved. |
| 0b111 | 56 bits. In SMMUv3.3, this value is Reserved. |

- This value must match the system physical address size, see section 3.4 Address sizes .
- Note: Where reference is made to OAS, it is the size value that is referenced, not the literal value of this field.
- If OAS indicates 52 bits, at least one of the following must be true:
- -SMMU\_IDR5.GRAN64K == 1.
- -SMMU\_IDR5.DS == 1.
- -SMMU\_IDR5.D128 == 1.

- If OAS indicates 56 bits, then SMMU\_IDR5.D128 == 1.

Note: Arm recommends that SMMUv3 implementations support at least 4KB and 64KB granules.

## Accessing SMMU\_IDR5

Accesses to this register use the following encodings: Accessible at offset 0x0014 from SMMUv3\_PAGE\_0

Accesses to this register are RO.