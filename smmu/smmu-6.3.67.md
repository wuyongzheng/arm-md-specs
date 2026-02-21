## 6.3.67 SMMU\_S\_GERROR

The SMMU\_S\_GERROR characteristics are:

## Purpose

Reporting of Secure Global Error conditions.

## Configuration

This register is present only when SMMU\_S\_IDR1.SECURE\_IMPL == 1. Otherwise, direct accesses to SMMU\_S\_GERROR are RES0.

## Attributes

SMMU\_S\_GERROR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

See SMMU\_GERROR for information on GERROR behavior. This register provides a similar facility to SMMU\_GERROR, except for errors relating to the Secure programming interface.

This register, in conjunction with SMMU\_S\_GERRORN, indicates whether global error conditions exist. See section 7.5 Global error recording .

An error is active if the value of SMMU\_S\_GERROR[x] is different to the corresponding SMMU\_S\_GERRORN[x] bit.

The SMMU toggles SMMU\_S\_GERROR[x] when an error becomes active. An external agent acknowledges the error by toggling the corresponding SMMU\_S\_GERRORN[x], making the GERRORN[x] bit the same value as the corresponding GERROR[x] bit. Acknowledging an error deactivates the error, allowing a new occurrence to be reported at a later time, however:

- SFM\_ERR indicates that Service failure mode has been entered. Acknowledging this GERROR bit does not exit Service failure mode which remains active and is resolved in an IMPLEMENTATION DEFINED way.

The SMMU does not toggle a bit when an error is already active. An error is only activated if it is in an inactive state.

Note: Software is not intended to trigger interrupts by arranging for GERRORN[x] to differ from GERROR[x]. See section SMMU\_GERRORN.

## Bits [31:10]

Reserved, RES0.

## CMDQP\_ERR, bit [9]

## When SMMU\_S\_IDR0.ECMDQ == 1:

When this bit is different to SMMU\_S\_GERRORN.CMDQP\_ERR, it indicates that one or more errors have been encountered on a Secure Command queue control page interface.

See section 3.5.6.3 Errors relating to an ECMDQ interface .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SFM\_ERR, bit [8]

- When this bit is different to SMMU\_S\_GERRORN[8], the SMMU has entered Service failure mode.
- -Traffic through the SMMU has stopped. The SMMU has stopped processing commands and recording events. The RAS registers describe the error.
- -Acknowledgement of this error through GERRORN does not clear the Service failure mode error, which is cleared in an IMPLEMENTATION DEFINED way. See Section 12.3 Service Failure Mode (SFM) .
- SFM triggers SFM\_ERR in SMMU\_GERROR, and when SMMU\_S\_IDR1.SECURE\_IMPL == 1 in SMMU\_S\_GERROR.

The reset behavior of this field is:

- This field resets to '0' .

## MSI\_GERROR\_ABT\_ERR, bit [7]

## When SMMU\_S\_IDR0.MSI == 1:

- When this bit is different to SMMU\_S\_GERRORN[7], a Secure GERROR MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [6]

Reserved, RES0.

## MSI\_EVENTQ\_ABT\_ERR, bit [5]

## When SMMU\_S\_IDR0.MSI == 1:

- When this bit is different to SMMU\_S\_GERRORN[5], a Secure Event queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_CMDQ\_ABT\_ERR, bit [4]

When SMMU\_S\_IDR0.MSI == 1:

- When this bit is different to SMMU\_S\_GERRORN[4], a Secure CMD\_SYNC MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [3]

Reserved, RES0.

## EVENTQ\_ABT\_ERR, bit [2]

- When this bit is different to SMMU\_S\_GERRORN[2], an access to the Secure Event queue was terminated with abort.
- -Event records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## CMDQ\_ERR, bit [0]

- When this bit is different to SMMU\_S\_GERRORN[0], a command has been encountered that cannot be processed on the Secure Command queue.
- -SMMU\_S\_CMDQ\_CONS.ERR has been updated with a reason code and command processing has stopped.
- Commands are not processed while this error is active.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_S\_GERROR

Accesses to this register use the following encodings:

Accessible at offset 0x8060 from SMMUv3\_PAGE\_0

- When an access is not Secure and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.