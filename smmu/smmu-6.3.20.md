## 6.3.20 SMMU\_GERRORN

The SMMU\_GERRORN characteristics are:

## Purpose

Acknowledgement of Global Error conditions.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_GERRORN is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

This register has the same fields as SMMU\_GERROR.

Software must not toggle fields in this register that correspond to errors that are inactive. It is CONSTRAINED UNPREDICTABLE whether or not an SMMU activates errors if this is done.

The SMMU does not alter fields in this register. A read of this register returns the values that were last written to the defined fields of the register.

Note: Software might maintain an internal copy of the last value written to this register, for comparison against values read from SMMU\_GERROR when probing for errors.

## Bits [31:11]

Reserved, RES0.

## DPT\_ERR, bit [10]

## When SMMU\_IDR3.DPT == 1:

DPT Lookup fault.

See SMMU\_GERROR.DPT\_ERR.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

CMDQP\_ERR, bit [9]

## When SMMU\_IDR1.ECMDQ == 1:

See SMMU\_GERROR.CMDQP\_ERR.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## SFM\_ERR, bit [8]

- When this bit is different to SMMU\_GERROR[8], the SMMU has entered Service failure mode.
- -Traffic through the SMMU has stopped. The SMMU has stopped processing commands and recording events. The RAS registers describe the error.
- -Acknowledgement of this error through GERRORN does not clear the Service failure mode error, which is cleared in an IMPLEMENTATION DEFINED way. See Section 12.3 Service Failure Mode (SFM) .
- -SFM triggers SFM\_ERR in SMMU\_GERROR, and when SMMU\_S\_IDR1.SECURE\_IMPL == 1 in SMMU\_S\_GERROR.

The reset behavior of this field is:

- This field resets to '0' .

## MSI\_GERROR\_ABT\_ERR, bit [7]

## When SMMU\_IDR0.MSI == 1:

- When this bit is different to SMMU\_GERROR[7], a GERROR MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_PRIQ\_ABT\_ERR, bit [6]

## When SMMU\_IDR0.MSI == 1 and SMMU\_IDR0.PRI == 1:

- When this bit is different to SMMU\_GERROR[6], a PRI queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_EVENTQ\_ABT\_ERR, bit [5]

## When SMMU\_IDR0.MSI == 1:

- When this bit is different to SMMU\_GERROR[5], an Event queue MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## MSI\_CMDQ\_ABT\_ERR, bit [4]

## When SMMU\_IDR0.MSI == 1:

- When this bit is different to SMMU\_GERROR[4], a CMD\_SYNC MSI was terminated with abort.
- -Activation of this error does not affect future MSIs.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## PRIQ\_ABT\_ERR, bit [3]

## When SMMU\_IDR0.PRI == 1:

- When this bit is different to SMMU\_GERROR[3], an access to the PRI queue was terminated with abort.
- -Page Request records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Otherwise:

Reserved, RES0.

## EVENTQ\_ABT\_ERR, bit [2]

- When this bit is different to SMMU\_GERROR[2], an access to the Event queue was terminated with abort.
- -Event records might have been lost.

The reset behavior of this field is:

- This field resets to '0' .

## Bit [1]

Reserved, RES0.

## CMDQ\_ERR, bit [0]

- When this bit is different to SMMU\_GERROR[0], a command has been encountered that cannot be processed.
- -SMMU\_CMDQ\_CONS.ERR has been updated with a reason code and command processing has stopped.
- -Commands are not processed while this error is active.

The reset behavior of this field is:

- This field resets to '0' .

## Additional Information

Fields that are Reserved in SMMU\_GERROR are also Reserved in this register.

## Accessing SMMU\_GERRORN

Accesses to this register use the following encodings: Accessible at offset 0x0064 from SMMUv3\_PAGE\_0 Accesses to this register are RW.