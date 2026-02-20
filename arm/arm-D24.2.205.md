## D24.2.205 TPIDR\_EL1, EL1 Software Thread ID Register

The TPIDR\_EL1 characteristics are:

## Purpose

Provides a location where software executing at EL1 can store thread identifying information, for OS management purposes.

The PE makes no use of this register.

## Configuration

AArch64 System register TPIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register TPIDRPRW[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to TPIDR\_EL1 are UNDEFINED.

## Attributes

TPIDR\_EL1 is a 64-bit register.

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

## Accessing TPIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TPIDR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.TPIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else X[t, 64] = TPIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = TPIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TPIDR_EL1;
```

MSR TPIDR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1101 | 0b0000 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.TPIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else TPIDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then TPIDR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TPIDR_EL1 = X[t, 64];
```