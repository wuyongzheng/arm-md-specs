## 6.3.120 SMMU\_ROOT\_GPT\_BASE2

The SMMU\_ROOT\_GPT\_BASE2 characteristics are:

## Purpose

Shadow register for updating SMMU\_ROOT\_GPT\_BASE, in systems that do not support 64-bit single-copy-atomic register accesses.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ROOT\_GPT\_BASE2 is a 64-bit register.

This register is part of the SMMUv3\_ROOT block.

## Field descriptions

<!-- image -->

| 63          | 52 51   |             | 32   |
|-------------|---------|-------------|------|
| RES0        |         | ADDR[51:12] |      |
| 31          |         | 12 11       | 0    |
| ADDR[51:12] |         | RES0        |      |

## Bits [63:52]

Reserved, RES0.

## ADDR, bits [51:12]

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Additional Information

See also: SMMU\_ROOT\_GPT\_BASE\_UPDATE.

## Accessing SMMU\_ROOT\_GPT\_BASE2

Accesses to this register use the following encodings:

Accessible at offset 0x0060 from SMMUv3\_ROOT

- When an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.