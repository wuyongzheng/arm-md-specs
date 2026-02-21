## 6.3.167 SMMU\_R\_EVENTQ\_CONS

The SMMU\_R\_EVENTQ\_CONS characteristics are:

## Purpose

Event queue consumer read index for Realm state.

## Configuration

There are no configuration notes.

## Attributes

SMMU\_R\_EVENTQ\_CONS is a 32-bit register.

This register is part of the SMMUv3\_R\_PAGE\_1 block.

## Field descriptions

<!-- image -->

## OVACKFLG, bit [31]

Overflow acknowledge flag.

- Software must set this flag to the value of SMMU\_R\_EVENTQ\_PROD.OVFLG when it is safe for the SMMUto report a future EVENT queue overflow. Arm recommends that this is done on initialization and after a previous Event queue overflow is handled by software.
- See section 7.4 Event queue overflow .

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [30:20]

Reserved, RES0.

## RD, bits [19:0]

Event queue read index.

This field is treated as two sub-fields, depending on the configured queue size:

Bit [QS]: RD\_WRAP - Event queue read index wrap flag.

Bits [QS-1:0]: RD - Event queue read index.

- Updated by the PE to point at the queue entry after the entry it has just consumed.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

QS == SMMU\_R\_EVENTQ\_BASE.LOG2SIZE and SMMU\_R\_EVENTQ\_BASE.LOG2SIZE &lt;= SMMU\_IDR1.EVENTQS &lt;= 19.

This gives a configurable-sized index pointer followed immediately by the wrap bit.

If QS &lt; 19, bits [19:QS + 1] are RES0. If software writes a non-zero value to these bits, the value might be stored but has no other effect. In addition, if SMMU\_IDR1.EVENTQS &lt; 19, bits [19:EVENTQS + 1] are UNKNOWN on read.

If QS == 0 the queue has one entry. Zero bits of RD index are present and RD\_WRAP is bit zero.

When software increments RD, if the index would pass off the end of the queue it must be correctly wrapped to the queue size given by QS and RD\_WRAP toggled.

Arm recommends that software initializes the register to a valid value before SMMU\_R\_CR0.EVENTQEN is transitioned from 0 to 1.

When SMMU\_R\_EVENTQ\_BASE.LOG2SIZE is increased within its valid range, the value of the bits of this register that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

## Accessing SMMU\_R\_EVENTQ\_CONS

Accesses to this register use the following encodings:

Accessible at offset 0x00AC from SMMUv3\_R\_PAGE\_1

- When an access is not Realm and an access is not Root, accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.