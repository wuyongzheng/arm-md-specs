## 6.3.108 SMMU\_ECMDQ\_PROD&lt;n&gt;, n = 0 - 255

The SMMU\_ECMDQ\_PROD&lt;n&gt; characteristics are:

## Purpose

Allows Command queue producer to update the write index.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ECMDQ\_PROD&lt;n&gt; is a 32-bit register.

This register is part of the SMMUv3\_CMDQCP block.

## Field descriptions

<!-- image -->

## EN, bit [31]

Non-secure state Queue enable.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:24]

Reserved, RES0.

## ERRACK, bit [23]

Non-secure state Error status acknowledge.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [22:20]

Reserved, RES0.

## WR, bits [19:0]

Non-secure state Command queue write index.

This field is treated as WR and WR\_WRAP sub-fields, with equivalent meaning to the corresponding fields in SMMU\_CMDQ\_PROD.

QS is derived from SMMU\_ECMDQ\_BASEn.LOG2SIZE with the same constraints as for other queues.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

See sections 3.5.6.2 Enabling and disabling an ECMDQ interface and 3.5.6.3 Errors relating to an ECMDQ interface .

## Accessing SMMU\_ECMDQ\_PROD&lt;n&gt;

There are many copies of the SMMU\_ECMDQ\_* registers.

The offset presented here is relative to each group of ECMDQ registers.

For the definition of how the groups are organised in memory, see section 6.2.5 Registers in a Command queue control page .

Accesses to this register use the following encodings:

Accessible at offset 0x08 + (0x100 * n) from SMMUv3\_CMDQCP

- When SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 0 and SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0, accesses to this register are RW.
- When SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 1 and SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 1, accesses to this register are RW.
- Otherwise, accesses to this register are RO.