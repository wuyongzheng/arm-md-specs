## D24.2.206 TPIDR\_EL2, EL2 Software Thread ID Register

The TPIDR\_EL2 characteristics are:

## Purpose

Provides a location where software executing at EL2 can store thread identifying information, for OS management purposes.

The PE makes no use of this register.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register TPIDR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HTPIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to TPIDR\_EL2 are UNDEFINED.

## Attributes

TPIDR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## ThreadID, bits [63:0]

Thread ID. Thread identifying information stored by software running at this Exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing TPIDR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TPIDR_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1101 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x090]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = TPIDR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = TPIDR_EL2;
```

MSR TPIDR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1101 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x090] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then TPIDR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then TPIDR_EL2 = X[t, 64];
```