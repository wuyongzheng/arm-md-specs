## 6.3.166 SMMU\_R\_EVENTQ\_PROD

The SMMU\_R\_EVENTQ\_PROD characteristics are:

## Purpose

Allows Event queue producer to update the read index for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_EVENTQ\_PROD is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_1 block.

## Field descriptions

<!-- image -->

## OVFLG, bit [31]

Event queue overflowed flag.

- An Event queue overflow is indicated using this flag. This flag is toggled by the SMMU when a queue overflow is detected, if OVFLG == SMMU\_R\_EVENTQ\_CONS.OVACKFLG.
- This flag will not be updated until a prior overflow is acknowledged by setting

SMMU\_R\_EVENTQ\_CONS.OVACKFLG equal to OVFLG.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [30:20]

Reserved, RES0.

## WR, bits [19:0]

Event queue write index.

This field is treated as two sub-fields, depending on the configured queue size:

Bit [QS]: WR\_WRAP - Queue write index wrap flag.

Bits [QS-1:0]: WR - Queue write index.

- Next space to be written by SMMU.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

QS == SMMU\_R\_EVENTQ\_BASE.LOG2SIZE, see SMMU\_R\_EVENTQ\_CONS.

If QS &lt; 19, bits [19:QS+1] are RAZ. When incremented by the SMMU, the WR index is always wrapped to the current queue size given by QS.

If QS == 0 the queue has one entry. Zero bits of WR index are present and WR\_WRAP is bit zero.

When SMMU\_R\_EVENTQ\_BASE.LOG2SIZE is increased within its valid range, the value of the bits of this registers that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

Arm recommends that software initializes the register to a valid value before SMMU\_R\_CR0.EVENTQEN is transitioned from 0 to 1.

Note: See section 7.4 Event queue overflow for details on queue overflow. An overflow condition is entered when a record has been discarded due to a full enabled Event queue. The following conditions do not cause an overflow condition:

- Event records discarded when the Event queue is disabled, that is when SMMU\_R\_CR0.EVENTQEN == 0.
- A stalled faulting transaction, as stall event records do not get discarded when the Event queue is full or disabled.

## Accessing SMMU\_R\_EVENTQ\_PROD

This register is Guarded by SMMU\_R\_CR0.EVENTQEN and must only be modified when SMMU\_R\_CR0.EVENTQEN == 0.

See SMMU\_R\_EVENTQ\_BASE for detailed behavior.

Accesses to this register use the following encodings:

Accessible at offset 0x00A8 from SMMUv3\_R\_PAGE\_1

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- When SMMU\_R\_CR0.EVENTQEN == 0 and SMMU\_R\_CR0ACK.EVENTQEN == 0, accesses to this register are RW.
- Otherwise, accesses to this register are RO.