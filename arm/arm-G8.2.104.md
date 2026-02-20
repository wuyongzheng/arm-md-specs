## G8.2.104 ISR, Interrupt Status Register

The ISR characteristics are:

## Purpose

Shows the pending status of the IRQ and FIQ interrupts and the SError exceptions.

## Configuration

AArch32 System register ISR bits [31:0] are architecturally mapped to AArch64 System register ISR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ISR are UNDEFINED.

## Attributes

ISR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 9 8 7 6 5   |
|------|-------------|
| RES0 | A I F RES0  |

## Bits [31:9]

Reserved, RES0.

## A, bit [8]

SError exception pending bit:

| A   | Meaning                         |
|-----|---------------------------------|
| 0b0 | No pending SError exception.    |
| 0b1 | An SError exception is pending. |

If all of the following apply then this field shows the pending status of virtual SError exceptions:

- EL2 is implemented and enabled in the current Security state.
- Any of the following apply:
- EL2 is using AArch64 and HCR\_EL2.AMO is 1.
- EL2 is using AArch64, FEAT\_DoubleFault2 is implemented, and the Effective value of HCRX\_EL2.TMEA is 1.
- EL2 is using AArch32 and HCR.AMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical SError exceptions.

If the SError exception is edge-triggered, this field is cleared to zero when the physical SError exception is taken.

## I, bit [7]

IRQ pending bit. Indicates whether an IRQ interrupt is pending:

| I   | Meaning                      |
|-----|------------------------------|
| 0b0 | No pending IRQ.              |
| 0b1 | An IRQ interrupt is pending. |

If all of the following apply then this field shows the pending status of virtual IRQ interrupts:

- EL2 is implemented and enabled in the current Security state.
- Any of the following apply:
- EL2 is using AArch64 and HCR\_EL2.IMO is 1.
- EL2 is using AArch32 and HCR.IMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical IRQ interrupts.

## F, bit [6]

FIQ pending bit. Indicates whether an FIQ interrupt is pending.

| F   | Meaning                      |
|-----|------------------------------|
| 0b0 | No pending FIQ.              |
| 0b1 | An FIQ interrupt is pending. |

If all of the following apply then this field shows the pending status of virtual FIQ interrupts:

- EL2 is implemented and enabled in the current Security state.
- Any of the following apply:
- EL2 is using AArch64 and HCR\_EL2.FMO is 1.
- EL2 is using AArch32 and HCR.FMO is 1.
- The PE is executing at EL1.

Otherwise, this field shows the pending status of physical FIQ interrupts.

## Bits [5:0]

Reserved, RES0.

## Accessing ISR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == '1' ↪ → then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ISR; elsif PSTATE.EL == EL2 then R[t] = ISR; elsif PSTATE.EL == EL3 then R[t] = ISR;
```