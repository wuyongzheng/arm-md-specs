## D24.2.18 AMAIR\_EL2, Auxiliary Memory Attribute Indirection Register (EL2)

The AMAIR\_EL2 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED memory attributes for the memory regions specified by MAIR\_EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register AMAIR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HAMAIR0[31:0].

AArch64 System register AMAIR\_EL2 bits [63:32] are architecturally mapped to AArch32 System register HAMAIR1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AMAIR\_EL2 are UNDEFINED.

## Attributes

AMAIR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32                     |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
| 31                     | 0                      |
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

AMAIR\_EL2 is permitted to be cached in a TLB.

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMAIR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name AMAIR\_EL2 or AMAIR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, AMAIR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = AMAIR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = AMAIR_EL2;
```

MSR AMAIR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then AMAIR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then AMAIR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, AMAIR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGRTR_EL2.AMAIR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x148]; else X[t, 64] = AMAIR_EL1; elsif PSTATE.EL == EL2 then
```

```
if ELIsInHost(EL2) then X[t, 64] = AMAIR_EL2; else X[t, 64] = AMAIR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = AMAIR_EL1;
```

When FEAT\_VHE is implemented MSR AMAIR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0011 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.AMAIR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x148] = X[t, 64]; else AMAIR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then AMAIR_EL2 = X[t, 64]; else AMAIR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then AMAIR_EL1 = X[t, 64];
```