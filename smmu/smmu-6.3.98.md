## 6.3.98 SMMU\_PRIQ\_CONS

The SMMU\_PRIQ\_CONS characteristics are:

## Purpose

PRI queue consumer read index.

## Configuration

This register is present only when SMMU\_IDR0.PRI == 1. Otherwise, direct accesses to SMMU\_PRIQ\_CONS are RES0.

## Attributes

SMMU\_PRIQ\_CONS is a 32-bit register.

This register is part of the SMMUv3\_PAGE\_1 block.

## Field descriptions

<!-- image -->

## OVACKFLG, bit [31]

Overflow acknowledge flag.

- Note: Software sets this flag to the value of SMMU\_PRIQ\_PROD.OVFLG when it is ready for the SMMUto report a new PRI queue overflow. Arm expects this to be done on initialization and after a previous PRI queue overflow has been handled by software.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Bits [30:20]

Reserved, RES0.

## RD, bits [19:0]

Queue read index.

This field is treated as two sub-fields, depending on the configured queue size:

Bit [QS]: RD\_WRAP - Queue read index wrap flag.

Bits [QS-1:0]: RD - Queue read index.

- Updated by the PE to point at the queue entry after the entry it has just consumed.

The reset behavior of this field is:

- This field resets to an UNKNOWN value.

## Additional Information

QS == SMMU\_PRIQ\_BASE.LOG2SIZE and SMMU\_PRIQ\_BASE.LOG2SIZE &lt;= SMMU\_IDR1.PRIQS &lt;= 19. This gives a configurable-sized index pointer followed immediately by the wrap bit.

If QS &lt; 19, bits [19:QS + 1] are RES0. If software writes a non-zero value to these bits, the value might be stored but has no other effect. In addition, if SMMU\_IDR1.PRIQS &lt; 19, bits [19:PRIQS + 1] are UNKNOWN on read.

If QS == 0 the queue has one entry: zero bits of RD index are present and RD\_WRAP is bit zero.

When software increments RD, if the index would pass off the end of the queue it must be correctly wrapped to the queue size given by QS and RD\_WRAP toggled.

When SMMU\_PRIQ\_BASE.LOG2SIZE is increased within its valid range, the value of this register's bits that were previously above the old wrap flag position are UNKNOWN and when it is decreased, the value of the bits from the wrap flag downward are the effective truncation of the value in the old field.

Arm recommends that software initializes the register to a valid value before SMMU\_CR0.PRIQEN is transitioned from 0 to 1.

## Accessing SMMU\_PRIQ\_CONS

Accesses to this register use the following encodings:

Accessible at offset 0x00CC from SMMUv3\_PAGE\_1

Accesses to this register are RW.