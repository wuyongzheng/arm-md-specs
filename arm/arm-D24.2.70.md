## D24.2.70 HFGITR2\_EL2, Hypervisor Fine-Grained Instruction Trap Register 2

The HFGITR2\_EL2 characteristics are:

## Purpose

Provides instruction trap controls.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_FGT2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HFGITR2\_EL2 are UNDEFINED.

## Attributes

HFGITR2\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## nDCCIVAPS, bit [1]

## When FEAT\_PoPS is implemented:

Trap execution of any of the following AArch64 instructions at EL1 to EL2:

- DCCIVAPS.
- DCCIGDVAPS, if FEAT\_MTE2 is implemented.

If the Point of Physical Storage is before any level of data cache, it is IMPLEMENTATION DEFINED whether the execution of the affected instruction is trapped when the value of this control is 1.

| nDCCIVAPS   | Meaning                                                                                                                                                                                                                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If EL2 is implemented and enabled in the current Security state, then execution at EL1 using AArch64 of any of the specified instructions is trapped to EL2 and reported with EC syndrome value 0x18 , unless the instruction generates a higher priority exception. |
| 0b1         | Execution of the specified instructions is not trapped by this mechanism.                                                                                                                                                                                            |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.

- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TSBCSYNC, bit [0]

## When FEAT\_TRBEv1p1 is implemented:

Trap execution of TSB CSYNC at EL1 and EL0 using AArch64 to EL2.

| TSBCSYNC   | Meaning                                                                                                                                                                                                                                                                                                          |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution of TSB CSYNCis not trapped by this mechanism.                                                                                                                                                                                                                                                          |
| 0b1        | If EL2 is implemented and enabled in the current Security state, and the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, then execution of TSB CSYNCat EL1 and EL0 using AArch64 is trapped to EL2 and reported with EC syndrome value 0x0A , unless the instruction generates a higher priority exception. |

This field is ignored by the PE and treated as zero when all of the following are true:

- EL3 is implemented.
- SCR\_EL3.FGTEn2 == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing HFGITR2\_EL2

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x310];
```

```
elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HFGITR2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HFGITR2_EL2;
```

MSR HFGITR2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0001 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_FGT2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x310] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.FGTEn2 == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.FGTEn2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HFGITR2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HFGITR2_EL2 = X[t, 64];
```