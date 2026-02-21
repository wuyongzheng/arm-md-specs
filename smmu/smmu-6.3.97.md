## 6.3.97 SMMU\_PRIQ\_PROD

The SMMU\_PRIQ\_PROD characteristics are:

## Purpose

PRI queue write index status.

## Configuration

This register is present only when SMMU\_IDR0.PRI == 1. Otherwise, direct accesses to SMMU\_PRIQ\_PROD are RES0.

## Attributes

SMMU\_PRIQ\_PROD is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_1 block.

## Field descriptions

<!-- image -->

## OVFLG, bit [31]

- This flag is toggled by the SMMU when a queue overflow is detected, in which case one or more requests have been lost.
- An overflow condition is present when this flag is different from SMMU\_PRIQ\_CONS.OVACKFLG. This flag is not updated until the overflow is acknowledged by setting SMMU\_PRIQ\_CONS.OVACKFLG equal to OVFLG.

The reset behavior of this field is:

- This field resets to '0' .

## Bits [30:20]

Reserved, RES0.

## WR, bits [19:0]

Queue write index.

This field is treated as two sub-fields, depending on the configured queue size:

Bit [QS]: WR\_WRAP - Queue write index wrap flag.

Bits [QS-1:0]: WR - Queue write index.

- Next space to be written by SMMU.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

QS == SMMU\_PRIQ\_BASE.LOG2SIZE; see SMMU\_PRIQ\_CONS.

If QS &lt; 19, bits [19:QS + 1] are RAZ. When incremented by the SMMU, the WR index is always wrapped to the current queue size given by QS.

If QS == 0 the queue has one entry: zero bits of WR index are present and WR\_WRAP is bit zero.

When SMMU\_PRIQ\_BASE.LOG2SIZE is increased within its valid range, the value of the bits of this register that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

Arm recommends that software initializes the register to a valid value before transitioning SMMU\_CR0.PRIQEN from 0 to 1.

## Accessing SMMU\_PRIQ\_PROD

SMMU\_PRIQ\_PROD is Guarded by SMMU\_CR0.PRIQEN and must only be modified when PRIQEN == 0.

See SMMU\_PRIQ\_BASE for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x00C8 from SMMUv3\_PAGE\_1

- When SMMU\_CR0.PRIQEN == 0 and SMMU\_CR0ACK.PRIQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.