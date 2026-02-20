## D24.2.118 ISR\_EL1, Interrupt Status Register

The ISR\_EL1 characteristics are:

## Purpose

Shows the pending status of IRQ and FIQ interrupts and SError exceptions.

When FEAT\_NMI is implemented, also shows whether a pending IRQ or FIQ interrupt has Superpriority.

## Configuration

AArch64 System register ISR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ISR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ISR\_EL1 are UNDEFINED.

## Attributes

ISR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:11]

Reserved, RES0.

## IS, bit [10]

## When FEAT\_NMI is implemented:

IRQ with Superpriority pending bit. Indicates whether an IRQ interrupt with Superpriority is pending.

| IS   | Meaning                                         |
|------|-------------------------------------------------|
| 0b0  | No pending IRQ with Superpriority.              |
| 0b1  | An IRQ interrupt with Superpriority is pending. |

If all of the following apply, then this field shows the pending status of virtual IRQ interrupts with Superpriority:

- EL2 is implemented and enabled in the current Security state.
- HCR\_EL2.IMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical IRQ interrupts with Superpriority.

## Otherwise:

Reserved, RES0.

## FS, bit [9]

## When FEAT\_NMI is implemented:

FIQ with Superpriority pending bit. Indicates whether an FIQ interrupt with Superpriority is pending.

| FS   | Meaning                                         |
|------|-------------------------------------------------|
| 0b0  | No pending FIQ with Superpriority.              |
| 0b1  | An FIQ interrupt with Superpriority is pending. |

If all of the following apply, then this field shows the pending status of virtual FIQ interrupts with Superpriority:

- EL2 is implemented and enabled in the current Security state.
- HCR\_EL2.FMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical FIQ interrupts with Superpriority.

## Otherwise:

Reserved, RES0.

## A, bit [8]

SError exception pending bit. Indicates whether an SError exception is pending.

| A   | Meaning                         |
|-----|---------------------------------|
| 0b0 | No pending SError.              |
| 0b1 | An SError exception is pending. |

If all of the following apply, then this field shows the pending status of virtual SError exceptions:

- EL2 is implemented and enabled in the current Security state.
- Any of the following apply:
- HCR\_EL2.AMO is 1.
- FEAT\_DoubleFault2 is implemented and the Effective value of HCRX\_EL2.TMEA is 1.
- The PE is executing at EL1.

Otherwise, if all of the following apply, then this field shows the pending status of delegated SError exceptions:

- FEAT\_E3DSE is implemented.
- SCR\_EL3.EnDSE is 1.
- The PE is executing at EL2 or EL1.

Otherwise, this field shows the pending status of physical SError exceptions.

If the physical SError exception is edge-triggered, this field is cleared to zero when the physical SError exception is taken.

## I, bit [7]

IRQ pending bit. Indicates whether an IRQ interrupt is pending.

| I   | Meaning                      |
|-----|------------------------------|
| 0b0 | No pending IRQ.              |
| 0b1 | An IRQ interrupt is pending. |

If all of the following apply, then this field shows the pending status of virtual IRQ interrupts:

- EL2 is implemented and enabled in the current Security state.
- HCR\_EL2.IMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical IRQ interrupts.

Note

This bit indicates the presence of a pending IRQ interrupt regardless of whether the interrupt has Superpriority.

## F, bit [6]

FIQ pending bit. Indicates whether an FIQ interrupt is pending.

| F   | Meaning                      |
|-----|------------------------------|
| 0b0 | No pending FIQ.              |
| 0b1 | An FIQ interrupt is pending. |

If all of the following apply, then this field shows the pending status of virtual FIQ interrupts:

- EL2 is implemented and enabled in the current Security state.
- HCR\_EL2.FMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical FIQ interrupts.

Note

This bit indicates the presence of a pending FIQ interrupt regardless of whether the interrupt has Superpriority.

## Bits [5:0]

Reserved, RES0.

## Accessing ISR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ISR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1100 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.ISR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = ISR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = ISR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ISR_EL1;
```