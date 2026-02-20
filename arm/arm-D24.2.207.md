## D24.2.207 TPIDR\_EL3, EL3 Software Thread ID Register

The TPIDR\_EL3 characteristics are:

## Purpose

Provides a location where software executing at EL3 can store thread identifying information, for OS management purposes.

The PE makes no use of this register.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TPIDR\_EL3 are UNDEFINED.

## Attributes

TPIDR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| Thread ID | Thread ID | Thread ID |
| 31        | 0         |           |
| Thread ID | Thread ID | Thread ID |

## ThreadID, bits [63:0]

Thread ID. Thread identifying information stored by software running at this Exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing TPIDR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1101 | 0b0000 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = TPIDR_EL3;
```

MSR TPIDR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1101 | 0b0000 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.TPIDR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else TPIDR_EL3 = X[t, 64];
```