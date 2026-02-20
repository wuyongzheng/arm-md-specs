## D24.2.203 TPIDR2\_EL0, EL0 Read/Write Software Thread ID Register 2

The TPIDR2\_EL0 characteristics are:

## Purpose

Provides a location where SME-aware software executing at EL0 can store thread identifying information, for context management purposes.

The PE makes no use of this register.

## Configuration

This register is present only when FEAT\_SME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TPIDR2\_EL0 are UNDEFINED.

## Attributes

TPIDR2\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63        | 32        |           |
|-----------|-----------|-----------|
| Thread ID | Thread ID | Thread ID |
| 31        | 0         |           |
| Thread ID | Thread ID | Thread ID |

## ThreadID, bits [63:0]

Thread identifying information stored by software running at this Exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing TPIDR2\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TPIDR2_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnTP2 == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.EnTP2 == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnTP2 == '0' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGRTR_EL2.nTPIDR2_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnTP2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TPIDR2_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnTP2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nTPIDR2_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnTP2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TPIDR2_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnTP2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnTP2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TPIDR2_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = TPIDR2_EL0;
```

MSR TPIDR2\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b1101 | 0b0000 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnTP2 == '0' then UNDEFINED; elsif !ELIsInHost(EL0) && SCTLR_EL1.EnTP2 == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.EnTP2 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGWTR_EL2.nTPIDR2_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnTP2 == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); else TPIDR2_EL0 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnTP2 == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nTPIDR2_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.EnTP2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TPIDR2_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.EnTP2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.EnTP2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TPIDR2_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then TPIDR2_EL0 = X[t, 64];
```