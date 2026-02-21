## 6.3.4 SMMU\_IDR3

The SMMU\_IDR3 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Non-secure programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_IDR3 is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:24]

Reserved, RES0.

## AIE, bit [23]

Indicates support for stage 1 Attribute Index Extension

| AIE   | Meaning                                             |
|-------|-----------------------------------------------------|
| 0b0   | Stage 1 Attribute Index Extension is not supported. |
| 0b1   | Stage 1 Attribute Index Extension is supported.     |

If SMMU\_IDR0.S1P is 0, then this field is RES0.

Otherwise, if SMMU\_IDR5.D128 is 1, then this bit is 1.

If this bit is 1, then the CD.AIE field is present.

See also:

- CD.{MAIR0, MAIR1}.
- CD.AIE.

## MTEPERM, bit [22]

SMMUsupport for stage 2 MemAttr NoTagAccess encodings

| MTEPERM   | Meaning                                     |
|-----------|---------------------------------------------|
| 0b0       | Stage 2 NoTagAccess encodings are reserved. |

| MTEPERM   | Meaning                                                  |
|-----------|----------------------------------------------------------|
| 0b1       | Stage 2 NoTagAccess encodings are supported by the SMMU. |

If SMMU\_IDR0.S2P is 0, this field is RES0.

In SMMUv3.4 and later, this bit is 1.

## THE, bit [21]

Support for translation hardening extension

| THE   | Meaning                                           |
|-------|---------------------------------------------------|
| 0b0   | Translation hardening extension is not supported. |
| 0b1   | Translation hardening extension is supported.     |

If this bit is 1 and SMMU\_IDR0.S2P is 1, then SMMU\_IDR3.S2PI is 1.

If SMMU\_IDR0.S1P is 0, then this field is RES0.

See also:

- 3.27 Translation Hardening .

## S2PO, bit [20]

Support for stage 2 permission overlays

| S2PO   | Meaning                                        |
|--------|------------------------------------------------|
| 0b0    | Stage 2 permission overlays are not supported. |
| 0b1    | Stage 2 permission overlays are supported.     |

If this bit is 1, then SMMU\_IDR3.S2PI is 1.

See also:

- 3.26.2 Stage 2 permission indirections .

## S2PI, bit [19]

Support for stage 2 permission indirections

| S2PI   | Meaning                                            |
|--------|----------------------------------------------------|
| 0b0    | Stage 2 permission indirections are not supported. |
| 0b1    | Stage 2 permission indirections are supported.     |

If SMMU\_IDR0.S2P is 0, then this field is RES0.

Otherwise, if SMMU\_IDR5.D128 is 1, then this bit is 1.

See also:

- 3.26.2 Stage 2 permission indirections .

## S1PI, bit [18]

Support for stage 1 permission indirections

| S1PI   | Meaning                                            |
|--------|----------------------------------------------------|
| 0b0    | Stage 1 permission indirections are not supported. |
| 0b1    | Stage 1 permission indirections are supported.     |

If SMMU\_IDR0.S1P is 0, then this field is RES0.

Otherwise, if SMMU\_IDR5.D128 is 1, then this bit is 1.

See also:

- 3.26.1 Stage 1 permission indirections .

## EPAN, bit [17]

Support for the Enhanced PAN mechanism

| EPAN   | Meaning                        |
|--------|--------------------------------|
| 0b0    | Enhanced PAN is not supported. |
| 0b1    | Enhanced PAN is supported.     |

This bit is 1 in any implementation of SMMUv3.4 or later.

## PASIDTT, bit [16]

| PASIDTT   | Meaning                                                                                                                                                                                                                                                  |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Use of the PASID TLP prefix on ATS Translated transactions is not supported architecturally. It is IMPLEMENTATION DEFINED whether ATS Translated transactions with a SubstreamID are assigned MPAM values as though they were untranslated transactions. |
| 0b1       | Use of the PASID TLP prefix on ATS Translated transactions is supported.                                                                                                                                                                                 |

This field indicates only that the SMMU supports use of PASID on ATS Translated transactions.

Whether the PASID TLP prefix can be presented to the SMMU depends additionally on:

- Support for the Translated Memory Requests with PASID capability in the device [1].
- Support for forwarding PASID on Translated Memory Requests in the Root Port.

If SMMU\_IDR0.ATS is 0, or SMMU\_IDR1.SSIDSIZE is 0, then this field is RES0.

Note: Issue E.a of the IO Remapping Table [9] specification introduces a bit in the ATS Attribute field of the Root Complex Node to express support for forwarding PASID on Translated Memory Requests.

## DPT, bit [15]

Support for Device Permission Table, and EATS encoding 0b11 , for Non-secure streams.

| DPT   | Meaning               |
|-------|-----------------------|
| 0b0   | DPT is not supported. |
| 0b1   | DPT is supported.     |

If this bit is 1, then SMMU\_IDR0.ATS is 1.

For more information see:

- STE.EATS
- 3.9.1.3 Handling of ATS Translated transactions .
- 3.24 Device Permission Table .

## PTWNNC, bit [14]

Behavior of STE.S2PTW bit.

| PTWNNC   | Meaning                                                                                                          |
|----------|------------------------------------------------------------------------------------------------------------------|
| 0b0      | STE.S2PTW == 0 permits stage 1 translation table walks mapped as Device memory.                                  |
| 0b1      | STE.S2PTW == 0 treats stage 1 translation table walks mapped as Device memory, as Normal Non-cacheable accesses. |

In implementations of SMMUv3.3 and later that have SMMU\_IDR0.S2P == 1, SMMU\_IDR3.PTWNNC == 1.

See STE.S2PTW for details.

If SMMU\_IDR0.S2P == 0, this bit is RES0.

## E0PD, bit [13]

| E0PD   | Meaning                                |
|--------|----------------------------------------|
| 0b0    | The E0PD mechanism is not implemented. |
| 0b1    | The E0PD mechanism is implemented.     |

This bit is 1 in all implementations of SMMUv3.3 and later.

See CD.E0PD0 and CD.E0PD1.

## BBML, bits [12:11]

Break-Before-Make behavior Level.

| BBML   | Meaning   |
|--------|-----------|
| 0b00   | Level 0.  |

| BBML   | Meaning   |
|--------|-----------|
| 0b01   | Level 1.  |
| 0b10   | Level 2.  |

- BBML is 0b01 or 0b10 in an implementation of SMMUv3.2 or later.
- See section 3.21.1 Translation tables and TLB invalidation completion behavior .

## RIL, bit [10]

Range-based Invalidations and Level hint support for TLBI.

| RIL   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | Range-based invalidation and level hint are not supported. |
| 0b1   | Range-based invalidation and level hint are supported.     |

- RIL is 1 in an implementation of SMMUv3.2 or later.
- See section 4.4.1.1 Range-based invalidation and level hint .

## STT, bit [9]

Small translation table support.

| STT   | Meaning                                     |
|-------|---------------------------------------------|
| 0b0   | Small translation tables are not supported. |
| 0b1   | Small translation tables are supported.     |

- STT is 1 in implementations where SMMU\_S\_IDR1.SEL2 == 1.

## FWB, bit [8]

Stage 2 control of memory types and attributes.

| FWB   | Meaning                                                                                        |
|-------|------------------------------------------------------------------------------------------------|
| 0b0   | Stage 2 control of memory types and attributes is not supported and the STE.S2FWB bit is RES0. |
| 0b1   | Stage 2 control of memory types and attributes is supported.                                   |

- FWB is 1 in an implementation of SMMUv3.2 or later.

## MPAM, bit [7]

Memory Partitioning And Monitoring (MPAM) support.

| MPAM   | Meaning                |
|--------|------------------------|
| 0b0    | MPAM is not supported. |

| MPAM   | Meaning                                                                                                                                                                                               |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1    | MPAM is supported in at least one Security state and the SMMU_(S_)MPAMIDR registers are present. The SMMU_(S_)MPAMIDR registers indicate whether MPAM is supported by a corresponding Security state. |

- MPAM support is optional.
- When MPAM is not supported, all MPAM-related register fields are RES0.
- See Chapter 17 Memory System Resource Partitioning and Monitoring .

## Bit [6]

Reserved, RES0.

## PPS, bit [5]

| PPS   | Meaning                                                                                                                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The STE.PPAR field determines whether the PASID is used on a PRI auto-generated response.                                                                                                           |
| 0b1   | If the request had a PASID, it is used on a PRI auto-generated response for PRI queue overflow, in the same way as when STE.PPAR == 1. The STE.PPAR field is not checked, and the value is IGNORED. |

- When SMMU\_IDR0.PRI == 0 or SMMU\_IDR1.SSIDSIZE == 0, this field is RES0.

## XNX, bit [4]

Indicates support for execute-never control distinction by Exception level at stage 2.

| XNX   | Meaning                                                                                                                                                                                                                                            |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | EL0/EL1 execute control distinction at stage 2 not supported.                                                                                                                                                                                      |
| 0b1   | EL0/EL1 execute control distinction at stage 2 supported for both VMSAv8-64 and VMSAv8-32 LPAE stage 2 translation tables. • This feature extends the stage 2 TTD.XN field bit to 2 bits which are encoded, and behave as described in Armv8.2[2]. |

- In SMMUv3.0, this field is RES0.
- In SMMUv3.1 and later, support for this feature is mandatory when stage 2 is supported, that is when SMMU\_IDR0.S2P == 1.

## PBHA, bit [3]

Page-Based Hardware Attributes presence.

| PBHA   | Meaning                                                                                                                    |
|--------|----------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Page-Based Hardware Attributes not supported. • SMMU_IDR3.HAD determines whether Hierachical Attribute Disables supported. |

| PBHA   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b1    | Page-Based Hardware Attributes supported. • If this field is one SMMU_IDR3.HAD must be one. |

- In SMMUv3.0, this field is RES0.
- See CD.HWU059 and STE.S2HWU59.

## HAD, bit [2]

Hierarchical Attribute Disable presence.

| HAD   | Meaning                                                                     |
|-------|-----------------------------------------------------------------------------|
| 0b0   | No Hierarchical Attribute Disable support. CD.HAD0 and CD.HAD1 are IGNORED. |
| 0b1   | CD.HAD0 and CD.HAD1 control Hierarchical Attribute Disable.                 |

- In SMMUv3.0, support for this feature is optional when stage 1 is supported, that is when SMMU\_IDR0.S1P == 1.
- In SMMUv3.1 and later, support for this feature is mandatory when stage 1 is supported, that is when SMMU\_IDR0.S1P == 1.
- When SMMU\_IDR0.S1P == 0, SMMU\_IDR3.HAD == 0.

## Bits [1:0]

Reserved, RES0.

## Accessing SMMU\_IDR3

Accesses to this register use the following encodings:

Accessible at offset 0x000C from SMMUv3\_PAGE\_0

Accesses to this register are RO.