## 6.3.107 SMMU\_ECMDQ\_BASE&lt;n&gt;, n = 0 - 255

The SMMU\_ECMDQ\_BASE&lt;n&gt; characteristics are:

## Purpose

Configuration of the Command queue base address.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ECMDQ\_BASE&lt;n&gt; is a 64-bit register.

This register is part of the SMMUv3\_CMDQCP block.

## Field descriptions

<!-- image -->

| 63                  | 62 61               | 56 55               | 32                  |
|---------------------|---------------------|---------------------|---------------------|
| RA                  | RES0                |                     |                     |
| RES0                | RES0                | RES0                | RES0                |
| 31 5 4 0            | 31 5 4 0            | 31 5 4 0            | 31 5 4 0            |
| ADDR[55:5] LOG2SIZE | ADDR[55:5] LOG2SIZE | ADDR[55:5] LOG2SIZE | ADDR[55:5] LOG2SIZE |

## Bit [63]

Reserved, RES0.

## RA, bit [62]

Read-Allocate hint.

| RA   | Meaning           |
|------|-------------------|
| 0b0  | No Read-Allocate. |
| 0b1  | Read-Allocate.    |

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [61:56]

Reserved, RES0.

## ADDR, bits [55:5]

Non-secure PA of Command queue base, bits [55:5].

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## LOG2SIZE, bits [4:0]

Queue size as log2(entries).

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

The fields in this register all have equivalent meaning to the corresponding fields in SMMU\_CMDQ\_BASE.

LOG2SIZE must be less than or equal to SMMU\_IDR1.CMDQS, with the same constraints as SMMU\_CMDQ\_BASE.LOG2SIZE.

See section 3.5.6 Enhanced Command queue interfaces .

## Accessing SMMU\_ECMDQ\_BASE&lt;n&gt;

There are many copies of the SMMU\_ECMDQ\_* registers.

The offset presented here is relative to each group of ECMDQ registers.

For the definition of how the groups are organised in memory, see section 6.2.5 Registers in a Command queue control page .

Accesses to this register use the following encodings:

Accessible at offset 0x00 + (0x100 * n) from SMMUv3\_CMDQCP

- When SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 0 and SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.