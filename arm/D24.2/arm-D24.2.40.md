## D24.2.40 CPTRMASK\_EL2, Architectural Feature Trap Masking Register

The CPTRMASK\_EL2 characteristics are:

## Purpose

Mask register to prevent updates of fields in CPTR\_EL2 on writes.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CPTRMASK\_EL2 are UNDEFINED.

## Attributes

CPTRMASK\_EL2 is a 64-bit register.

## Field descriptions

When ELIsInHost(EL2):

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

Mask bit for TCPAC.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TAM, bit [30]

## When FEAT\_AMUv1 is implemented:

Mask bit for TAM.

| TCPAC   | Meaning                          |
|---------|----------------------------------|
| 0b0     | CPTR_EL2.TCPAC is writeable.     |
| 0b1     | CPTR_EL2.TCPAC is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0POE, bit [29]

## When FEAT\_S1POE is implemented:

Mask bit for E0POE.

| E0POE   | Meaning                          |
|---------|----------------------------------|
| 0b0     | CPTR_EL2.E0POE is writeable.     |
| 0b1     | CPTR_EL2.E0POE is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTA, bit [28]

## When System register access to the trace unit registers is implemented:

Mask bit for TTA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| TAM   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.TAM is writeable.     |
| 0b1   | CPTR_EL2.TAM is not writeable. |

| TTA   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.TTA is writeable.     |
| 0b1   | CPTR_EL2.TTA is not writeable. |

## Otherwise:

Reserved, RES0.

Bits [27:25]

Reserved, RES0.

## SMEN, bit [24]

## When FEAT\_SME is implemented:

Mask bit for SMEN.

| SMEN   | Meaning                         |
|--------|---------------------------------|
| 0b0    | CPTR_EL2.SMEN is writeable.     |
| 0b1    | CPTR_EL2.SMEN is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [23:21]

Reserved, RES0.

## FPEN, bit [20]

Mask bit for FPEN.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [19:17]

Reserved, RES0.

## ZEN, bit [16]

## When FEAT\_SVE is implemented:

Mask bit for ZEN.

| FPEN   | Meaning                         |
|--------|---------------------------------|
| 0b0    | CPTR_EL2.FPEN is writeable.     |
| 0b1    | CPTR_EL2.FPEN is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

This format applies in all Armv8.0 implementations.

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

Mask bit for TCPAC.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

TAM, bit [30]

| ZEN   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.ZEN is writeable.     |
| 0b1   | CPTR_EL2.ZEN is not writeable. |

| TCPAC   | Meaning                          |
|---------|----------------------------------|
| 0b0     | CPTR_EL2.TCPAC is writeable.     |
| 0b1     | CPTR_EL2.TCPAC is not writeable. |

## When FEAT\_AMUv1 is implemented:

Mask bit for TAM.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [29:21]

Reserved, RES0.

## TTA, bit [20]

Mask bit for TTA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [19:13]

Reserved, RES0.

## TSM, bit [12]

## When FEAT\_SME is implemented:

Mask bit for TSM.

The reset behavior of this field is:

| TAM   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.TAM is writeable.     |
| 0b1   | CPTR_EL2.TAM is not writeable. |

| TTA   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.TTA is writeable.     |
| 0b1   | CPTR_EL2.TTA is not writeable. |

| TSM   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.TSM is writeable.     |
| 0b1   | CPTR_EL2.TSM is not writeable. |

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [11]

Reserved, RES0.

## TFP, bit [10]

Mask bit for TFP.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## TZ, bit [8]

## When FEAT\_SVE is implemented:

Mask bit for TZ.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [7:0]

Reserved, RES0.

| TFP   | Meaning                        |
|-------|--------------------------------|
| 0b0   | CPTR_EL2.TFP is writeable.     |
| 0b1   | CPTR_EL2.TFP is not writeable. |

| TZ   | Meaning                       |
|------|-------------------------------|
| 0b0  | CPTR_EL2.TZ is writeable.     |
| 0b1  | CPTR_EL2.TZ is not writeable. |

## Accessing CPTRMASK\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CPTRMASK\_EL2 or CPTRMASK\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CPTRMASK\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CPTRMASK_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CPTRMASK_EL2;
```

MSR CPTRMASK\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED;
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsZero(EffectiveCPTRMASK_EL2()) then UNDEFINED; else CPTRMASK_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CPTRMASK_EL2 = X[t, 64];
```

MRS

```
else <Xt>, CPACRMASK_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nCPACRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x320]; else X[t, 64] = CPACRMASK_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = CPTRMASK_EL2; else X[t, 64] = CPACRMASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CPACRMASK_EL1;
```

MSR CPACRMASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nCPACRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x320] = X[t, 64]; elsif !IsZero(EffectiveCPACRMASK_EL1()) then UNDEFINED; else CPACRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if !IsZero(EffectiveCPTRMASK_EL2()) then UNDEFINED; else CPTRMASK_EL2 = X[t, 64]; else CPACRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CPACRMASK_EL1 = X[t, 64];
```