## D24.2.188 SMPRI\_EL1, Streaming Mode Priority Register

The SMPRI\_EL1 characteristics are:

## Purpose

Configures the streaming execution priority for instructions executed on a shared Streaming Mode Compute Unit (SMCU) when the PE is in Streaming SVE mode at any Exception level.

## Configuration

When SMIDR\_EL1.SMPS is '0', this register is RES0.

This register is present only when FEAT\_SME is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SMPRI\_EL1 are UNDEFINED.

## Attributes

SMPRI\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:4]

Reserved, RES0.

## Priority, bits [3:0]

Streaming execution priority value.

Either this value is used directly, or it is mapped into an effective priority value using SMPRIMAP\_EL2.

This value is used directly when any of the following are true:

- The current Exception level is EL3 or EL2.
- The current Exception level is EL1 or EL0, if EL2 is implemented and enabled in the current Security state and HCRX\_EL2.SMPME is '0'.
- The current Exception level is EL1 or EL0, if EL2 is either not implemented or not enabled in the current Security state.

The precise meaning and behavior of each streaming execution priority value is IMPLEMENTATION DEFINED.

In an implementation that shares execution resources between PEs, higher priority values are allocated more processing resource than other PEs configured with lower priority values in the same Priority domain.

If FEAT\_SME2p2 is implemented, and this field is greater than the Highest Implemented Priority value indicated by SMIDR\_EL1.HIP, then the PE uses the Highest Implemented Priority value as the priority.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SMPRI\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SMPRI\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nSMPRI_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SMPRI_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SMPRI_EL1; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SMPRI_EL1;
```

MSR SMPRI\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0010 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_SME) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nSMPRI_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SMPRI_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.ESM == '0' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.ESM == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else SMPRI_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.ESM == '0' then AArch64.SystemAccessTrap(EL3, 0x18); else SMPRI_EL1 = X[t, 64];
```