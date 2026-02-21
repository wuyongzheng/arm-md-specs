## 6.3.109 SMMU\_ECMDQ\_CONS&lt;n&gt;, n = 0 - 255

The SMMU\_ECMDQ\_CONS&lt;n&gt; characteristics are:

## Purpose

Command queue consumer read index.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_ECMDQ\_CONS&lt;n&gt; is a 32-bit register.

This register is part of the SMMUv3\_CMDQCP block.

## Field descriptions

<!-- image -->

## ENACK, bit [31]

Non-secure state Queue enable acknowledge.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:27]

Reserved, RES0.

## ERR\_REASON, bits [26:24]

Non-secure state Error reason code

| ERR_REASON   | Meaning                                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------------------|
| 0b000        | CERROR_NONE - No error.                                                                                     |
| 0b001        | CERROR_ILL - Command illegal and cannot be correctly consumed.                                              |
| 0b010        | CERROR_ABT - Abort on command fetch.                                                                        |
| 0b011        | CERROR_ATC_INV_SYNC - A CMD_SYNC failed to successfully complete one or more previous CMD_ATC_INV commands. |

ERR\_REASON is UNKNOWN if an error is not active.

The CERROR\_NONE encoding is defined for completeness only, and is not provided by the SMMU in any error case.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## ERR, bit [23]

Non-secure state Error status

The reset behavior of this field is:

- This field resets to '0' .

## Bits [22:20]

Reserved, RES0.

## RD, bits [19:0]

Non-secure state Command queue read index.

This field is treated as RD and RD\_WRAP sub-fields, with equivalent meaning to the corresponding fields in SMMU\_CMDQ\_CONS.

QS is derived from SMMU\_ECMDQ\_BASEn.LOG2SIZE with the same constraints as for other queues.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

See sections 3.5.6.2 Enabling and disabling an ECMDQ interface and 3.5.6.3 Errors relating to an ECMDQ interface .

## Accessing SMMU\_ECMDQ\_CONS&lt;n&gt;

There are many copies of the SMMU\_ECMDQ\_* registers.

The offset presented here is relative to each group of ECMDQ registers.

For the definition of how the groups are organised in memory, see section 6.2.5 Registers in a Command queue control page .

Accesses to this register use the following encodings:

Accessible at offset 0x0C + (0x100 * n) from SMMUv3\_CMDQCP

- When SMMU\_ECMDQ\_PROD&lt;n&gt;.EN == 0 and SMMU\_ECMDQ\_CONS&lt;n&gt;.ENACK == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.