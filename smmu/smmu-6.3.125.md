## 6.3.125 SMMU\_R\_IDR3

The SMMU\_R\_IDR3 characteristics are:

## Purpose

Provides information about the features implemented for the SMMU Realm state programming interface.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_IDR3 is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

| 31   | 18 17 16 15 14   |
|------|------------------|
| RES0 | XT MEC DPT RES0  |

## Bits [31:18]

Reserved, RES0.

## XT, bit [17]

## When SMMU\_R\_IDR0.ATS == 1:

Support for both:

- The XT encoding in all of the following:
- -Untranslated transactions.
- -ATS Translation requests.
- -Translated transactions.
- The TE encoding in ATS Translation Completions.

| XT   | Meaning                                |
|------|----------------------------------------|
| 0b0  | XT and TE encodings are not supported. |
| 0b1  | XT and TE encodings are supported.     |

## See also:

- 3.9.4.3 XT bit on Untranslated transactions, Translation requests and Translated transactions .
- 3.9.4.2 TE bit on ATS Translation Completions .

## Otherwise:

Reserved, RES0.

## MEC, bit [16]

Support for Memory Encryption Contexts for the Realm programming interface.

| MEC   | Meaning                                       |
|-------|-----------------------------------------------|
| 0b0   | Memory Encryption Contexts are not supported. |

| MEC   | Meaning                                   |
|-------|-------------------------------------------|
| 0b1   | Memory Encryption Contexts are supported. |

If this field is 1, then SMMU\_R\_MECIDR and SMMU\_R\_GMECID are present.

See also:

- Chapter 18 Support for Memory Encryption Contexts .

## DPT, bit [15]

Support for Device Permission Table and EATS encoding 0b11 .

| DPT   | Meaning               |
|-------|-----------------------|
| 0b0   | DPT is not supported. |
| 0b1   | DPT is supported.     |

If this bit is 1, then SMMU\_R\_IDR0.ATS is 1.

See also:

- STE.EATS
- Section 3.9.1.3 Handling of ATS Translated transactions .
- 3.24 Device Permission Table .

## Bits [14:0]

Reserved, RES0.

## Accessing SMMU\_R\_IDR3

Accesses to this register use the following encodings:

Accessible at offset 0x000C from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.