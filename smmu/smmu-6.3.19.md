## 6.3.19 SMMU\_GERROR

The SMMU\_GERROR characteristics are:

## Purpose

Reporting of Global Error conditions.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_GERROR is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

This register, in conjunction with SMMU\_GERRORN, indicates whether global error conditions exist. See section 7.5 Global error recording .

An error is active if the value of SMMU\_GERROR[x] is different to the corresponding SMMU\_GERRORN[x] bit.

The SMMU toggles SMMU\_GERROR[x] when an error becomes active. An external agent acknowledges the error by toggling the corresponding SMMU\_GERRORN[x], making the GERRORN[x] bit the same value as the corresponding GERROR[x] bit. Acknowledging an error deactivates the error, allowing a new occurrence to be reported at a later time, however:

- SFM\_ERR indicates that Service failure mode has been entered. Acknowledging this GERROR bit does not exit Service failure mode which remains active and is resolved in an IMPLEMENTATION DEFINED way.

The SMMU does not toggle a bit when an error is already active. An error is only activated if it is in an inactive state.

Note: Software is not intended to trigger interrupts by arranging for GERRORN[x] to differ from GERROR[x]. See SMMU\_GERRORN.

## Bits [31:11]

Reserved, RES0.

## DPT\_ERR, bit [10]

## When SMMU\_IDR3.DPT == 1:

DPT Lookup fault.

When this bit is different from SMMU\_GERRORN.DPT\_ERR, it indicates that one or more DPT lookup faults have occurred, and that syndrome information is available in SMMU\_DPT\_CFG\_FAR.

For more information see 3.24.4 DPT lookup errors

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## CMDQP\_ERR, bit [9]

## When SMMU\_IDR1.ECMDQ == 1:

When this bit is different to SMMU\_GERRORN.CMDQP\_ERR, it indicates that one or more errors have been encountered on a Command queue control page interface.

See section 3.5.6.3 Errors relating to an ECMDQ interface .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SFM\_ERR, bit [8]

- When this bit is different to SMMU\_GERRORN[8], the SMMU has entered Service failure mode.
- -Traffic through the SMMU has stopped. The SMMU has stopped processing commands and recording events. The RAS registers describe the error.
- -Acknowledgement of this error through GERRORN does not clear the Service failure mode error, which is cleared in an IMPLEMENTATION DEFINED way. See Section 12.3 Service Failure Mode (SFM) .
- -SFM triggers SFM\_ERR in SMMU\_GERROR, and when SMMU\_S\_IDR1.SECURE\_IMPL == 1 in SMMU\_S\_GERROR.

The reset behavior of this field is:

- This field resets to '0' .

## MSI\_GERROR\_ABT\_ERR, bit [7]

## When SMMU\_IDR0.MSI == 1:

- When this bit is different to SMMU\_GERRORN[7], a GERROR MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_PRIQ\_ABT\_ERR, bit [6]

## When SMMU\_IDR0.MSI == 1 and SMMU\_IDR0.PRI == 1:

- When this bit is different to SMMU\_GERRORN[6], a PRI queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_EVENTQ\_ABT\_ERR, bit [5]

## When SMMU\_IDR0.MSI == 1:

- When this bit is different to SMMU\_GERRORN[5], an Event queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_CMDQ\_ABT\_ERR, bit [4]

## When SMMU\_IDR0.MSI == 1:

- When this bit is different to SMMU\_GERRORN[4], a CMD\_SYNC MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## PRIQ\_ABT\_ERR, bit [3]

## When SMMU\_IDR0.PRI == 1:

- When this bit is different to SMMU\_GERRORN[3], an access to the PRI queue was terminated with abort.
- -Page Request records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## EVENTQ\_ABT\_ERR, bit [2]

- When this bit is different to SMMU\_GERRORN[2], an access to the Event queue was terminated with abort.
- -Event records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## CMDQ\_ERR, bit [0]

- When this bit is different to SMMU\_GERRORN[0], a command has been encountered that cannot be processed.

- -SMMU\_CMDQ\_CONS.ERR has been updated with a reason code and command processing has stopped.
- -Commands are not processed while this error is active.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_GERROR

Accesses to this register use the following encodings:

Accessible at offset 0x0060 from SMMUv3\_PAGE\_0

Accesses to this register are RO.