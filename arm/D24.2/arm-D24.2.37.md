## D24.2.37 CPACRMASK\_EL1, Architectural Feature Access Control Masking Register

The CPACRMASK\_EL1 characteristics are:

## Purpose

Mask register to prevent updates of fields in CPACR\_EL1 on writes to CPACR\_EL1 or CPACRALIAS\_EL1.

## Configuration

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CPACRMASK\_EL1 are UNDEFINED.

## Attributes

CPACRMASK\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

## When FEAT\_NV2p1 is implemented:

Mask bit for TCPAC.

| TCPAC   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | CPACR_EL1.TCPAC is writeable.     |
| 0b1     | CPACR_EL1.TCPAC is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TAM, bit [30]

## When FEAT\_AMUv1 is implemented and FEAT\_NV2p1 is implemented:

Mask bit for TAM.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0POE, bit [29]

## When FEAT\_S1POE is implemented:

Mask bit for E0POE.

| E0POE   | Meaning                           |
|---------|-----------------------------------|
| 0b0     | CPACR_EL1.E0POE is writeable.     |
| 0b1     | CPACR_EL1.E0POE is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTA, bit [28]

## When System register access to the trace unit registers is implemented:

Mask bit for TTA.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

| TAM   | Meaning                         |
|-------|---------------------------------|
| 0b0   | CPACR_EL1.TAM is writeable.     |
| 0b1   | CPACR_EL1.TAM is not writeable. |

| TTA   | Meaning                         |
|-------|---------------------------------|
| 0b0   | CPACR_EL1.TTA is writeable.     |
| 0b1   | CPACR_EL1.TTA is not writeable. |

## Otherwise:

Reserved, RES0.

Bits [27:25]

Reserved, RES0.

## SMEN, bit [24]

## When FEAT\_SME is implemented:

Mask bit for SMEN.

| SMEN   | Meaning                          |
|--------|----------------------------------|
| 0b0    | CPACR_EL1.SMEN is writeable.     |
| 0b1    | CPACR_EL1.SMEN is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [23:21]

Reserved, RES0.

## FPEN, bit [20]

Mask bit for FPEN.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [19:17]

Reserved, RES0.

## ZEN, bit [16]

## When FEAT\_SVE is implemented:

Mask bit for ZEN.

| FPEN   | Meaning                          |
|--------|----------------------------------|
| 0b0    | CPACR_EL1.FPEN is writeable.     |
| 0b1    | CPACR_EL1.FPEN is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:0]

Reserved, RES0.

## Accessing CPACRMASK\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CPACRMASK\_EL1 or CPACRMASK\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CPACRMASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nCPACRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x320]; else X[t, 64] = CPACRMASK_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED;
```

| ZEN   | Meaning                         |
|-------|---------------------------------|
| 0b0   | CPACR_EL1.ZEN is writeable.     |
| 0b1   | CPACR_EL1.ZEN is not writeable. |

```
elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = CPTRMASK_EL2; else X[t, 64] = CPACRMASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CPACRMASK_EL1;
```

MSR CPACRMASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nCPACRMASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x320] = X[t, 64]; elsif !IsZero(EffectiveCPACRMASK_EL1()) then UNDEFINED; else CPACRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if !IsZero(EffectiveCPTRMASK_EL2()) then UNDEFINED; else CPTRMASK_EL2 = X[t, 64]; else CPACRMASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CPACRMASK_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CPACRMASK\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x320]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CPACRMASK_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CPACRMASK_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CPACRMASK\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x320] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED;
```

```
elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else CPACRMASK_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CPACRMASK_EL1 = X[t, 64]; else UNDEFINED;
```