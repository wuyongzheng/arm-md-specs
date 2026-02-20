## D24.2.190 TCR2\_EL1, Extended Translation Control Register (EL1)

The TCR2\_EL1 characteristics are:

## Purpose

The control register for stage 1 of the EL1&amp;0 translation regime.

## Configuration

This register is present only when FEAT\_TCR2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TCR2\_EL1 are UNDEFINED.

## Attributes

TCR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

Unless stated otherwise, all the bits in TCR2\_EL1 are permitted to be cached in a TLB.

## Bits [63:22]

Reserved, RES0.

## FNGNA1, bit [21]

## When FEAT\_THE is implemented:

Force non-global for unassured translations using TTBR1\_EL1.

| FNGNA1   | Meaning                                                                                                                                                                                                                                                                                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | This bit has no effect on the interpretation of the nG bit.                                                                                                                                                                                                                                                                                                       |
| 0b1      | Translations using TTBR1_EL1 are treated as non-global regardless of the value of the nG bit if all of the following is true: • The translation is for the EL1&0 translation regime. • Stage 1 and stage 2 translation are enabled. • Protection is enabled. • The final stage 1 translation using the descriptor does not have the Assured Translation property. |

This bit is permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

FNGNA0, bit [20]

## When FEAT\_THE is implemented:

Force non-global for unassured translations using TTBR0\_EL1.

| FNGNA0   | Meaning                                                                                                                                                                                                                                                                                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | This bit has no effect on the interpretation of the nG bit.                                                                                                                                                                                                                                                                                                       |
| 0b1      | Translations using TTBR0_EL1 are treated as non-global regardless of the value of the nG bit if all of the following is true: • The translation is for the EL1&0 translation regime. • Stage 1 and stage 2 translation are enabled. • Protection is enabled. • The final stage 1 translation using the descriptor does not have the Assured Translation property. |

This bit is permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [19]

Reserved, RES0.

FNG1, bit [18]

## When FEAT\_ASID2 is implemented:

Force non-global translations for TTBR1\_EL1.

| FNG1   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | This bit has no effect on the interpretation of the nG bit.                                   |
| 0b1    | Translations using TTBR1_EL1 are treated as non-global regardless of the value of the nG bit. |

This bit is permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FNG0, bit [17]

## When FEAT\_ASID2 is implemented:

Force non-global translations for TTBR0\_EL1.

| FNG0   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | This bit has no effect on the interpretation of the nG bit.                                   |
| 0b1    | Translations using TTBR0_EL1 are treated as non-global regardless of the value of the nG bit. |

This bit is permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## A2, bit [16]

## When FEAT\_ASID2 is implemented:

Enable use of two ASIDs.

This bit is permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

DisCH1, bit [15]

## When FEAT\_D128 is implemented and TCR2\_EL1.D128 == '1':

Disable the Contiguous bit for the Start Table for TTBR1\_EL1.

| DisCH1   | Meaning                                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------------------|
| 0b0      | The Contiguous bit of Block or Page descriptors of the Start Table for TTBR1_EL1 is not affected by this field. |
| 0b1      | The Contiguous bit of Block or Page descriptors of the Start Table for TTBR1_EL1 is treated as 0.               |

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

DisCH0, bit [14]

## When FEAT\_D128 is implemented and TCR2\_EL1.D128 == '1':

Disable the Contiguous bit for the Start Table for TTBR0\_EL1.

| A2   | Meaning                       |
|------|-------------------------------|
| 0b0  | Use of two ASIDs is disabled. |
| 0b1  | Use of two ASIDs is enabled.  |

| DisCH0   | Meaning                                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------------------|
| 0b0      | The Contiguous bit of Block or Page descriptors of the Start Table for TTBR0_EL1 is not affected by this field. |
| 0b1      | The Contiguous bit of Block or Page descriptors of the Start Table for TTBR0_EL1 is treated as 0.               |

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [13:12]

Reserved, RES0.

## HAFT, bit [11]

## When FEAT\_HAFT is implemented:

Hardware managed Access Flag for Table descriptors.

Enables the Hardware managed Access Flag for Table descriptors.

| HAFT   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0    | Hardware managed Access Flag for Table descriptors is disabled. |
| 0b1    | Hardware managed Access Flag for Table descriptors is enabled.  |

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PTTWI, bit [10]

## When FEAT\_THE is implemented:

Permit Translation table walk Incoherence.

Permits RCWS instructions to generate writes that have the Reduced Coherence property.

| PTTWI   | Meaning                                                                                              |
|---------|------------------------------------------------------------------------------------------------------|
| 0b0     | Write accesses generated by RCWSat EL1&0 do not have the Reduced Coherence property.                 |
| 0b1     | Write accesses generated by RCWSat EL1&0 have the Reduced Coherence property if HCRX_EL2.PTTWI is 1. |

This bit is permitted to be implemented as a read-only bit with a fixed value of 0.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [9:6]

Reserved, RES0.

## D128, bit [5]

## When FEAT\_D128 is implemented:

Enables VMSAv9-128 translation system.

| D128   | Meaning                                                    |
|--------|------------------------------------------------------------|
| 0b0    | Translation system follows VMSAv8-64 translation process.  |
| 0b1    | Translation system follows VMSAv9-128 translation process. |

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AIE, bit [4]

## When FEAT\_AIE is implemented:

Enable Attribute Indexing Extension.

| AIE   | Meaning                                |
|-------|----------------------------------------|
| 0b0   | Attribute Indexing Extension Disabled. |
| 0b1   | Attribute Indexing Extension Enabled.  |

This field is RES1 when TCR2\_EL1.D128 is 1.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

POE, bit [3]

## When FEAT\_S1POE is implemented:

Enables Permission Overlays for privileged accesses from EL1&amp;0 translation regime.

| POE   | Meaning                                                                            |
|-------|------------------------------------------------------------------------------------|
| 0b0   | Permission overlay disabled for EL1 access in stage 1 of EL1&0 translation regime. |
| 0b1   | Permission overlay enabled for EL1 access in stage 1 of EL1&0 translation regime.  |

This bit is not permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0POE, bit [2]

## When FEAT\_S1POE is implemented:

Enables Permission Overlays for unprivileged accesses from EL1&amp;0 translation regime.

| E0POE   | Meaning                                                                            |
|---------|------------------------------------------------------------------------------------|
| 0b0     | Permission overlay disabled for EL0 access in stage 1 of EL1&0 translation regime. |
| 0b1     | Permission overlay enabled for EL0 access in stage 1 of EL1&0 translation regime.  |

This bit is not permitted to be cached in a TLB.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PIE, bit [1]

## When FEAT\_S1PIE is implemented:

Enables usage of Indirect Permission Scheme.

This field is RES1 when TCR2\_EL1.D128 is 1.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

| PIE   | Meaning                    |
|-------|----------------------------|
| 0b0   | Direct permission model.   |
| 0b1   | Indirect permission model. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PnCH, bit [0]

## When FEAT\_THE is implemented:

Protected attribute enable. Enables use of bit[52] of the stage 1 translation table entries as the Protected bit, for translations using TTBRn\_EL1.

| PnCH   | Meaning                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------|
| 0b0    | For translations using TTBRn_EL1, bit[52] of each stage 1 translation table entry is not the Protected bit. |
| 0b1    | For translations using TTBRn_EL1, bit[52] of each stage 1 translation table entry is the Protected bit.     |

If bit[52] is used as the Protected bit, it is not used as the Contiguous bit.

This field is RES0 when TCR2\_EL1.D128 is 1.

This field is ignored by the PE and treated as zero when any of the following are true:

- All of the following are true:
- EL2 is implemented and enabled in the current Security state.
- The Effective value of HCRX\_EL2.TCR2En is 0.
- EL3 is implemented and SCR\_EL3.TCR2En == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TCR2\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TCR2\_EL1 or TCR2\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

If FEAT\_SRMASK is implemented, accesses to TCR2\_EL1 are masked by TCR2MASK\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TCR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TCR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.TCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.TCR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x270]; else X[t, 64] = TCR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TCR2_EL2; else X[t, 64] = TCR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TCR2_EL1;
```

MSR TCR2\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TCR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.TCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.TCR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x270] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then TCR2_EL1 = (X[t, 64] AND NOT EffectiveTCR2MASK_EL1()) OR (TCR2_EL1 AND ↪ → EffectiveTCR2MASK_EL1()); else TCR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then TCR2_EL2 = (X[t, 64] AND NOT EffectiveTCR2MASK_EL2()) OR (TCR2_EL2 AND ↪ → EffectiveTCR2MASK_EL2()); else TCR2_EL2 = X[t, 64]; else TCR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TCR2_EL1 = X[t, 64];
```

MRS &lt;Xt&gt;, TCR2\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TCR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x270]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = TCR2_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TCR2_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TCR2\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0000 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_TCR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x270] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TCR2_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TCR2_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_SRMASK is implemented MRS &lt;Xt&gt;, TCR2ALIAS\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_TCR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGRTR2_EL2.nTCR2ALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.TCR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x270]; else X[t, 64] = TCR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TCR2_EL2; else X[t, 64] = TCR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TCR2_EL1;
```

When FEAT\_SRMASK is implemented MSR TCR2ALIAS\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_TCR2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGWTR2_EL2.nTCR2ALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.TCR2En == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x270] = X[t, 64]; else
```

```
if IsFeatureImplemented(FEAT_SRMASK) then TCR2_EL1 = (X[t, 64] AND NOT EffectiveTCR2MASK_EL1()) OR (TCR2_EL1 AND ↪ → EffectiveTCR2MASK_EL1()); else TCR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.TCR2En == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.TCR2En == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then TCR2_EL2 = (X[t, 64] AND NOT EffectiveTCR2MASK_EL2()) OR (TCR2_EL2 AND ↪ → EffectiveTCR2MASK_EL2()); else TCR2_EL2 = X[t, 64]; else TCR2_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TCR2_EL1 = X[t, 64];
```