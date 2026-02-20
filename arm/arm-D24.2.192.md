## D24.2.192 TCR2MASK\_EL1, Extended Translation Control Masking Register (EL1)

The TCR2MASK\_EL1 characteristics are:

## Purpose

Mask register to prevent updates of fields in TCR2\_EL1 on writes to TCR2\_EL1 or TCR2ALIAS\_EL1.

## Configuration

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TCR2MASK\_EL1 are UNDEFINED.

## Attributes

TCR2MASK\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:22]

Reserved, RES0.

## FNGNA1, bit [21]

## When FEAT\_THE is implemented:

Mask bit for FNGNA1.

| FNGNA1   | Meaning                           |
|----------|-----------------------------------|
| 0b0      | TCR2_EL1.FNGNA1 is writeable.     |
| 0b1      | TCR2_EL1.FNGNA1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FNGNA0, bit [20]

FNG0

## When FEAT\_THE is implemented:

Mask bit for FNGNA0.

| FNGNA0   | Meaning                           |
|----------|-----------------------------------|
| 0b0      | TCR2_EL1.FNGNA0 is writeable.     |
| 0b1      | TCR2_EL1.FNGNA0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [19]

Reserved, RES0.

## FNG1, bit [18]

## When FEAT\_ASID2 is implemented:

Mask bit for FNG1.

| FNG1   | Meaning                         |
|--------|---------------------------------|
| 0b0    | TCR2_EL1.FNG1 is writeable.     |
| 0b1    | TCR2_EL1.FNG1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

FNG0, bit [17]

## When FEAT\_ASID2 is implemented:

Mask bit for FNG0.

| FNG0   | Meaning                     |
|--------|-----------------------------|
| 0b0    | TCR2_EL1.FNG0 is writeable. |

| FNG0   | Meaning                         |
|--------|---------------------------------|
| 0b1    | TCR2_EL1.FNG0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## A2, bit [16]

## When FEAT\_ASID2 is implemented:

Mask bit for A2.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DisCH1, bit [15]

## When FEAT\_D128 is implemented:

Mask bit for DisCH1.

| DisCH1   | Meaning                           |
|----------|-----------------------------------|
| 0b0      | TCR2_EL1.DisCH1 is writeable.     |
| 0b1      | TCR2_EL1.DisCH1 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

| A2   | Meaning                       |
|------|-------------------------------|
| 0b0  | TCR2_EL1.A2 is writeable.     |
| 0b1  | TCR2_EL1.A2 is not writeable. |

## DisCH0, bit [14]

## When FEAT\_D128 is implemented:

Mask bit for DisCH0.

| DisCH0   | Meaning                           |
|----------|-----------------------------------|
| 0b0      | TCR2_EL1.DisCH0 is writeable.     |
| 0b1      | TCR2_EL1.DisCH0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [13:12]

Reserved, RES0.

## HAFT, bit [11]

## When FEAT\_HAFT is implemented:

Mask bit for HAFT.

| HAFT   | Meaning                         |
|--------|---------------------------------|
| 0b0    | TCR2_EL1.HAFT is writeable.     |
| 0b1    | TCR2_EL1.HAFT is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PTTWI, bit [10]

## When FEAT\_THE is implemented:

Mask bit for PTTWI.

| PTTWI   | Meaning                          |
|---------|----------------------------------|
| 0b0     | TCR2_EL1.PTTWI is writeable.     |
| 0b1     | TCR2_EL1.PTTWI is not writeable. |

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

Mask bit for D128.

| D128   | Meaning                         |
|--------|---------------------------------|
| 0b0    | TCR2_EL1.D128 is writeable.     |
| 0b1    | TCR2_EL1.D128 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AIE, bit [4]

## When FEAT\_AIE is implemented:

Mask bit for AIE.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .

| AIE   | Meaning                        |
|-------|--------------------------------|
| 0b0   | TCR2_EL1.AIE is writeable.     |
| 0b1   | TCR2_EL1.AIE is not writeable. |

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

POE, bit [3]

## When FEAT\_S1POE is implemented:

Mask bit for POE.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

E0POE, bit [2]

## When FEAT\_S1POE is implemented:

Mask bit for E0POE.

| E0POE   | Meaning                          |
|---------|----------------------------------|
| 0b0     | TCR2_EL1.E0POE is writeable.     |
| 0b1     | TCR2_EL1.E0POE is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PIE, bit [1]

## When FEAT\_S1PIE is implemented:

Mask bit for PIE.

| POE   | Meaning                        |
|-------|--------------------------------|
| 0b0   | TCR2_EL1.POE is writeable.     |
| 0b1   | TCR2_EL1.POE is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PnCH, bit [0]

## When FEAT\_THE is implemented:

Mask bit for PnCH.

| PIE   | Meaning                        |
|-------|--------------------------------|
| 0b0   | TCR2_EL1.PIE is writeable.     |
| 0b1   | TCR2_EL1.PIE is not writeable. |

| PnCH   | Meaning                         |
|--------|---------------------------------|
| 0b0    | TCR2_EL1.PnCH is writeable.     |
| 0b1    | TCR2_EL1.PnCH is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TCR2MASK\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name TCR2MASK\_EL1 or TCR2MASK\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TCR2MASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nTCR2MASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x338]; else X[t, 64] = TCR2MASK_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = TCR2MASK_EL2; else X[t, 64] = TCR2MASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = TCR2MASK_EL1;
```

MSR TCR2MASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0111 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nTCR2MASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x338] = X[t, 64]; elsif !IsZero(EffectiveTCR2MASK_EL1()) then UNDEFINED; else TCR2MASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then
```

```
UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if !IsZero(EffectiveTCR2MASK_EL2()) then UNDEFINED; else TCR2MASK_EL2 = X[t, 64]; else TCR2MASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then TCR2MASK_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, TCR2MASK\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0111 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x338]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = TCR2MASK_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = TCR2MASK_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR TCR2MASK\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0111 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x338] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else TCR2MASK_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then TCR2MASK_EL1 = X[t, 64]; else UNDEFINED;
```