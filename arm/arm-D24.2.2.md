## D24.2.2 ACTLR\_EL1, Auxiliary Control Register (EL1)

The ACTLR\_EL1 characteristics are:

## Purpose

Provides IMPLEMENTATION DEFINED configuration and control options for execution at EL1 and EL0.

Note

Arm recommends the contents of this register have no effect on the PE when the Effective value of HCR\_EL2.{E2H,TGE}is{1, 1}, and instead the configuration and control fields are provided by the ACTLR\_EL2 register. This avoids the need for software to manage the contents of these register when switching between a Guest OS and a Host OS.

## Configuration

AArch64 System register ACTLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ACTLR[31:0].

AArch64 System register ACTLR\_EL1 bits [63:32] are architecturally mapped to AArch32 System register ACTLR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ACTLR\_EL1 are UNDEFINED.

## Attributes

ACTLR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ACTLR\_EL1

If the IMPLEMENTATION DEFINED ACTLR\_EL12 accessor is implemented, the following behaviors are also implemented:

- MRS/MSR to ACTLR\_EL1 from EL2 when the Effective value of HCR\_EL2.E2H is 1 accesses ACTLR\_EL2.
- MRS/MSR to ACTLR\_EL1 from EL1 when the Effective value of HCR\_EL2.{NV2, NV1, NV} is {1,0,1} accesses ACTLR\_EL1 directly and is not transformed to a memory access.
- MRS/MSR to ACTLRALIAS\_EL1 behaves in the same way as ACTLR\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ACTLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TACR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx ↪ → accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then X[t, 64] = NVMem[0x118]; else X[t, 64] = ACTLR_EL1; elsif PSTATE.EL == EL2 then if boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) then X[t, 64] = ACTLR_EL2; else X[t, 64] = ACTLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLR_EL1;
```

MSR ACTLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TACR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx ↪ → accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then NVMem[0x118] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then ACTLR_EL1 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL1()) OR (ACTLR_EL1 AND ↪ → EffectiveACTLRMASK_EL1()); else ACTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then ACTLR_EL2 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL2()) OR (ACTLR_EL2 AND ↪ → EffectiveACTLRMASK_EL2()); else ACTLR_EL2 = X[t, 64]; else ACTLR_EL1 = X[t, 64];
```

```
elsif PSTATE.EL == EL3 then ACTLR_EL1 = X[t, 64];
```

When an implementation implements ACTLR\_ELx accessor behavior and FEAT\_VHE is implemented MRS &lt;Xt&gt;, ACTLR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x118]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = ACTLR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = ACTLR_EL1; else UNDEFINED;
```

When an implementation implements ACTLR\_ELx accessor behavior and FEAT\_VHE is implemented MSR ACTLR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x118] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then ACTLR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then
```

```
if ELIsInHost(EL2) then ACTLR_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_SRMASK is implemented MRS &lt;Xt&gt;, ACTLRALIAS\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TACR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGRTR2_EL2.nACTLRALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED ↪ → "IMPLEMENTED_ACTLR_ELx accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then X[t, 64] = NVMem[0x118]; else X[t, 64] = ACTLR_EL1; elsif PSTATE.EL == EL2 then if boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) ↪ → then X[t, 64] = ACTLR_EL2; else X[t, 64] = ACTLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ACTLR_EL1;
```

When FEAT\_SRMASK is implemented MSR ACTLRALIAS\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TACR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGWTR2_EL2.nACTLRALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} && (!boolean IMPLEMENTATION_DEFINED ↪ → "IMPLEMENTED_ACTLR_ELx accessor behavior" || EffectiveHCR_EL2_NVx() == '111') then NVMem[0x118] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then
```

```
ACTLR_EL1 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL1()) OR (ACTLR_EL1 AND ↪ → EffectiveACTLRMASK_EL1()); else ACTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if boolean IMPLEMENTATION_DEFINED "IMPLEMENTED_ACTLR_ELx accessor behavior" && ELIsInHost(EL2) ↪ → then if IsFeatureImplemented(FEAT_SRMASK) then ACTLR_EL2 = (X[t, 64] AND NOT EffectiveACTLRMASK_EL2()) OR (ACTLR_EL2 AND ↪ → EffectiveACTLRMASK_EL2()); else ACTLR_EL2 = X[t, 64]; else ACTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then ACTLR_EL1 = X[t, 64];
```