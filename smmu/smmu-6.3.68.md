## 6.3.68 SMMU\_S\_GERRORN

The SMMU\_S\_GERRORN characteristics are:

## Purpose

Acknowledgement of Secure Global Error conditions.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_GERRORN are RES0.

## Attributes

SMMU\_S\_GERRORN is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

Software must not toggle fields in this register that correspond to errors that are inactive. It is CONSTRAINED UNPREDICTABLE whether or not an SMMU activates errors if this is done.

## Bits [31:10]

Reserved, RES0.

## CMDQP\_ERR, bit [9]

## When SMMU\_S\_IDR0.ECMDQ == 1:

See SMMU\_S\_GERROR.CMDQP\_ERR.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SFM\_ERR, bit [8]

- When this bit is different to SMMU\_S\_GERROR[8], the SMMU has entered Service failure mode.

The reset behavior of this field is:

- This field resets to '0' .

## MSI\_GERROR\_ABT\_ERR, bit [7]

## When SMMU\_S\_IDR0.MSI == 1:

- When this bit is different to SMMU\_S\_GERROR[7], a Secure GERROR MSI was terminated with abort.

- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [6]

Reserved, RES0.

## MSI\_EVENTQ\_ABT\_ERR, bit [5]

## When SMMU\_S\_IDR0.MSI == 1:

- When this bit is different to SMMU\_S\_GERROR[5], a Secure Event queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_CMDQ\_ABT\_ERR, bit [4]

## When SMMU\_S\_IDR0.MSI == 1:

- When this bit is different to SMMU\_S\_GERROR[4], a Secure CMD\_SYNC MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [3]

Reserved, RES0.

## EVENTQ\_ABT\_ERR, bit [2]

- When this bit is different to SMMU\_S\_GERROR[2], an access to the Secure Event queue was terminated with abort.
- -Event records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## CMDQ\_ERR, bit [0]

- When this bit is different to SMMU\_S\_GERROR[0], a command has been encountered that cannot be processed on the Secure Command queue.

- -SMMU\_S\_CMDQ\_CONS.ERR has been updated with a reason code and command processing has stopped.
- -Commands are not processed while this error is active.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Fields that are RES0 in SMMU\_S\_GERROR are also RES0 in this register.

## Accessing SMMU\_S\_GERRORN

Accesses to this register use the following encodings:

Accessible at offset 0x8064 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.