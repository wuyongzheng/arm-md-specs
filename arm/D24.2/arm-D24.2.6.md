## D24.2.6 ACTLRMASK\_EL2, Auxiliary Control Masking Register (EL2)

The ACTLRMASK\_EL2 characteristics are:

## Purpose

Mask register to prevent updates of fields in ACTLR\_EL2 on writes.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to ACTLRMASK\_EL2 are UNDEFINED.

## Attributes

ACTLRMASK\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63                     | 32   |
|------------------------|------|
| IMPLEMENTATION DEFINED |      |
| 31                     | 0    |

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

## Accessing ACTLRMASK\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name ACTLRMASK\_EL2 or ACTLRMASK\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ACTLRMASK\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ACTLRMASK_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLRMASK_EL2;
```

MSR ACTLRMASK\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsZero(EffectiveACTLRMASK_EL2()) then UNDEFINED; else ACTLRMASK_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then ACTLRMASK_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, ACTLRMASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nACTLRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx ↪ → accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then X[t, 64] = NVMem[0x340]; else X[t, 64] = ACTLRMASK_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) ↪ → then X[t, 64] = ACTLRMASK_EL2; else X[t, 64] = ACTLRMASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLRMASK_EL1;
```

MSR ACTLRMASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nACTLRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx ↪ → accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then NVMem[0x340] = X[t, 64]; elsif !IsZero(EffectiveACTLRMASK_EL1()) then UNDEFINED; else ACTLRMASK_EL1 = X[t, 64];
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) ↪ → then if !IsZero(EffectiveACTLRMASK_EL2()) then UNDEFINED; else ACTLRMASK_EL2 = X[t, 64]; else ACTLRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ACTLRMASK_EL1 = X[t, 64];
```