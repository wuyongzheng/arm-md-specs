## 6.3.137 SMMU\_R\_GERROR

The SMMU\_R\_GERROR characteristics are:

## Purpose

Reporting of Global Error conditions for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_GERROR is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

This register, in conjunction with SMMU\_R\_GERRORN, indicates whether global error conditions for Realm state exist. See section 7.5 Global error recording .

An error is active if the value of SMMU\_R\_GERROR[x] is different to the corresponding SMMU\_R\_GERRORN[x] bit.

The SMMU toggles SMMU\_R\_GERROR[x] when an error becomes active. An external agent acknowledges the error by toggling the corresponding SMMU\_GERRORN[x], making the GERRORN[x] bit the same value as the corresponding GERROR[x] bit. Acknowledging an error deactivates the error, allowing a new occurrence to be reported at a later time.

The SMMU does not toggle a bit when an error is already active. An error is only activated if it is in an inactive state.

Note: Software is not intended to trigger interrupts by arranging for GERRORN[x] to differ from GERROR[x]. See SMMU\_R\_GERRORN.

## Bits [31:11]

Reserved, RES0.

## DPT\_ERR, bit [10]

## When SMMU\_R\_IDR3.DPT == 1:

DPT Lookup fault.

When this bit is different from SMMU\_R\_GERRORN.DPT\_ERR, it indicates that one or more DPT lookup faults have occurred, and that syndrome information is available in SMMU\_R\_DPT\_CFG\_FAR.

For more information see 3.24.4 DPT lookup errors

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## CMDQP\_ERR, bit [9]

## When SMMU\_R\_IDR0.ECMDQ == 1:

When this bit is different to SMMU\_R\_GERRORN.CMDQP\_ERR, it indicates that one or more errors have been encountered on a Command queue control page interface of the Realm state.

See section 3.5.6.3 Errors relating to an ECMDQ interface .

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [8]

Reserved, RES0.

## MSI\_GERROR\_ABT\_ERR, bit [7]

## When SMMU\_R\_IDR0.MSI == 1:

- When this bit is different to SMMU\_R\_GERRORN[7], a GERROR MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_PRIQ\_ABT\_ERR, bit [6]

## When SMMU\_R\_IDR0.MSI == 1 and SMMU\_R\_IDR0.PRI == 1:

- When this bit is different to SMMU\_R\_GERRORN[6], a Realm state PRI queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_EVENTQ\_ABT\_ERR, bit [5]

## When SMMU\_R\_IDR0.MSI == 1:

- When this bit is different to SMMU\_R\_GERRORN[5], a Realm state Event queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_CMDQ\_ABT\_ERR, bit [4]

## When SMMU\_R\_IDR0.MSI == 1:

- When this bit is different to SMMU\_R\_GERRORN[4], a CMD\_SYNC Realm state MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## PRIQ\_ABT\_ERR, bit [3]

## When SMMU\_R\_IDR0.PRI == 1:

- When this bit is different to SMMU\_R\_GERRORN[3], an access to the Realm state PRI queue was terminated with abort.
- -Page Request records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## EVENTQ\_ABT\_ERR, bit [2]

- When this bit is different to SMMU\_R\_GERRORN[2], an access to the Realm state Event queue was terminated with abort.
- -Event records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## CMDQ\_ERR, bit [0]

- When this bit is different to SMMU\_R\_GERRORN[0], a Realm state command has been encountered that cannot be processed.
- -SMMU\_R\_CMDQ\_CONS.ERR has been updated with a reason code and command processing has stopped.
- -Commands are not processed while this error is active.

The reset behavior of this field is:

- This field resets to '0' .

## Accessing SMMU\_R\_GERROR

Accesses to this register use the following encodings:

Accessible at offset 0x0060 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.