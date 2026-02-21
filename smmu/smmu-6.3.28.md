## 6.3.28 SMMU\_CMDQ\_CONS

The SMMU\_CMDQ\_CONS characteristics are:

## Purpose

Command queue consumer read index.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_CMDQ\_CONS is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES0.

## ERR, bits [30:24]

Error reason code.

- When a command execution error is detected, ERR is set to a reason code and then the SMMU\_GERROR.CMDQ\_ERR global error becomes active.
- The value in this field is UNKNOWN when the CMDQ\_ERR global error is not active.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [23:20]

Reserved, RES0.

## RD, bits [19:0]

Command queue read index.

This field is treated as two sub-fields, depending on the configured queue size:

Bit [QS]: RD\_WRAP - Queue read index wrap flag.

Bits [QS-1:0]: RD - Queue read index.

- Updated by the SMMU (consumer) to point at the queue entry after the entry it has just consumed.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

QS == SMMU\_CMDQ\_BASE.LOG2SIZE and SMMU\_CMDQ\_BASE.LOG2SIZE &lt;= SMMU\_IDR1.CMDQS &lt;= 19.

This gives a configurable-sized index pointer followed immediately by the wrap bit.

If QS &lt; 19, bits [19:QS + 1] are RAZ. When incremented by the SMMU, the RD index is always wrapped to the current queue size given by SMMU\_CMDQ\_BASE.LOG2SIZE.

If QS == 0 the queue has one entry. Zero bits of RD index are present and RD\_WRAP is bit zero.

When SMMU\_CMDQ\_BASE.LOG2SIZE is increased within its valid range, the value of the bits of this register that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

Arm recommends that software initializes the register to a valid value before SMMU\_CR0.CMDQEN is transitioned from 0 to 1.

Upon a write to this register, when SMMU\_CR0.CMDQEN == 0, the ERR field is permitted to either take the written value or ignore the written value.

Note: There is no requirement for the SMMU to update this value after every command consumed. It might be updated only after an IMPLEMENTATION SPECIFIC number of commands have been consumed. However, an SMMU must ultimately update RD in finite time to indicate free space to software.

When a command execution error is detected, ERR is set to a reason code and then the respective SMMU\_GERROR.CMDQ\_ERR error becomes active. RD remains pointing at the infringing command for debug. The SMMU resumes processing commands after the CMDQ\_ERR error is acknowledged, if the Command queue is enabled at that time. SMMU\_GERROR.CMDQ\_ERR has no other interaction with SMMU\_CR0.CMDQEN than that a Command queue error can only be detected when the queue is enabled and therefore consuming commands. A change to SMMU\_CR0.CMDQEN does not affect, or acknowledge, SMMU\_GERROR.CMDQ\_ERR which must be explicitly acknowledged. See section 7.1 Command queue errors .

## Accessing SMMU\_CMDQ\_CONS

This register is Guarded by SMMU\_CR0.CMDQEN and must only be modified when SMMU\_CR0.CMDQEN == 0.

See SMMU\_CMDQ\_BASE for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x009C from SMMUv3\_PAGE\_0

- When SMMU\_CR0.CMDQEN == 0 and SMMU\_CR0ACK.CMDQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.