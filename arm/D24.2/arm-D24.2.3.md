## D24.2.3 ACTLR\_EL2, Auxiliary Control Register (EL2)

The ACTLR\_EL2 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED configuration and control options for EL2.

Note

Arm recommends the contents of this register are updated to apply to EL0 when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, gaining configuration and control fields from the ACTLR\_EL1. This avoids the need for software to manage the contents of these register when switching between a Guest OS and a Host OS.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register ACTLR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HACTLR[31:0].

AArch64 System register ACTLR\_EL2 bits [63:32] are architecturally mapped to AArch32 System register HACTLR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ACTLR\_EL2 are UNDEFINED.

## Attributes

ACTLR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32   |
|------------------------|------|
| IMPLEMENTATION DEFINED |      |
| 31                     | 0    |
| IMPLEMENTATION DEFINED |      |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ACTLR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = ACTLR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLR_EL2;
```

MSR ACTLR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_SRMASK) then ACTLR_EL2 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL2()) OR (ACTLR_EL2 AND ↪ → EffectiveACTLRMASK_EL2()); else ACTLR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then ACTLR_EL2 = X[t, 64];
```

When an implementation implements ACTLR\_ELx accessor behavior MRS &lt;Xt&gt;, ACTLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TACR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED ↪ → "IMPLEMENTED_ACTLR_ELx accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then X[t, 64] = NVMem[0x118]; else
```

```
X[t, 64] = ACTLR_EL1; elsif PSTATE.EL == EL2 then if boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) ↪ → then X[t, 64] = ACTLR_EL2; else X[t, 64] = ACTLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLR_EL1;
```

When an implementation implements ACTLR\_ELx accessor behavior MSR ACTLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TACR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED ↪ → "IMPLEMENTED_ACTLR_ELx accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then NVMem[0x118] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then ACTLR_EL1 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL1()) OR (ACTLR_EL1 AND ↪ → EffectiveACTLRMASK_EL1()); else ACTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) ↪ → then if IsFeatureImplemented(FEAT_SRMASK) then ACTLR_EL2 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL2()) OR (ACTLR_EL2 AND ↪ → EffectiveACTLRMASK_EL2()); else ACTLR_EL2 = X[t, 64]; else ACTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ACTLR_EL1 = X[t, 64];
```