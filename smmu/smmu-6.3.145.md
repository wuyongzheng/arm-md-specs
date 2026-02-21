## 6.3.145 SMMU\_R\_CMDQ\_PROD

The SMMU\_R\_CMDQ\_PROD characteristics are:

## Purpose

Allows Command queue producer to update the write index for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_CMDQ\_PROD is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_0 block.

## Field descriptions

<!-- image -->

## Bits [31:20]

Reserved, RES0.

## WR, bits [19:0]

Command queue write index.

This field is treated as two sub-fields, depending on the configured queue size:

Bit [QS]: WR\_WRAP - Command queue write index wrap flag.

Bits [QS-1:0]: WR - Command queue write index.

- Updated by the host PE (producer) indicating the next empty space in the queue after new data.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

QS == SMMU\_R\_CMDQ\_BASE.LOG2SIZE, see SMMU\_R\_CMDQ\_CONS.

If QS &lt; 19, bits [19:QS + 1] are RES0. If software writes a non-zero value to these bits, the value might be stored but has no other effect. In addition, if SMMU\_IDR1.CMDQS &lt; 19, bits [19:CMDQS+1] are UNKNOWN on read.

If QS == 0 the queue has one entry. Zero bits of WR index are present and WR\_WRAP is bit zero.

When software increments WR, if the index would pass off the end of the queue it must be correctly wrapped to the queue size given by QS and WR\_WRAP toggled.

Note: In the degenerate case of a one-entry queue, an increment of WR consists solely of a toggle of WR\_WRAP.

There is space in the queue for additional commands if:

```
SMMU_R_CMDQ_CONS.RD != SMMU_R_CMDQ_PROD.WR || SMMU_R_CMDQ_CONS.RD_WRAP == SMMU_R_CMDQ_PROD.WR_WRAP
```

The value written to this register must only move the pointer in a manner consistent with adding N consecutive entries to the Command queue, updating WR\_WRAP when appropriate.

When SMMU\_R\_CMDQ\_BASE.LOG2SIZE is increased within its valid range, the value of the bits of this register that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

Arm recommends that software initializes the register to a valid value before SMMU\_R\_CR0.CMDQEN is transitioned from 0 to 1.

A write to this register causes the SMMU to consider the Command queue for processing if SMMU\_R\_CR0.CMDQEN == 1 and SMMU\_R\_GERROR.CMDQ\_ERR is not active.

## Accessing SMMU\_R\_CMDQ\_PROD

Accesses to this register use the following encodings:

Accessible at offset 0x0098 from SMMUv3\_R\_PAGE\_0

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.