## D24.2.208 TPIDRRO\_EL0, EL0 Read-Only Software Thread ID Register

The TPIDRRO\_EL0 characteristics are:

## Purpose

Provides a location where software executing at EL1 or higher can store thread identifying information that is visible to software executing at EL0, for OS management purposes.

The PE makes no use of this register.

## Configuration

AArch64 System register TPIDRRO\_EL0 bits [31:0] are architecturally mapped to AArch32 System register TPIDRURO[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to TPIDRRO\_EL0 are UNDEFINED.

## Attributes

TPIDRRO\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| Thread ID | Thread ID | Thread ID |
| 31        | 0         |           |
| Thread ID | Thread ID | Thread ID |

## ThreadID, bits [63:0]

Thread ID. Thread identifying information stored by software running at this Exception level.

## Accessing TPIDRRO\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TPIDRRO_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0000 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then if EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGRTR_EL2.TPIDRRO_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = TPIDRRO_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.TPIDRRO_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
else X[t, 64] = TPIDRRO_EL0; elsif PSTATE.EL == EL2 then X[t, 64] = TPIDRRO_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = TPIDRRO_EL0;
```

MSR TPIDRRO\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0000 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.TPIDRRO_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else TPIDRRO_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then TPIDRRO_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then TPIDRRO_EL0 = X[t, 64];
```