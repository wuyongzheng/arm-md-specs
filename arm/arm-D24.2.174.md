## D24.2.174 SCTLR2MASK\_EL2, Extended System Control Masking Register (EL2)

The SCTLR2MASK\_EL2 characteristics are:

## Purpose

Mask register to prevent updates of fields in SCTLR2\_EL2 on writes.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_SRMASK is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to SCTLR2MASK\_EL2 are UNDEFINED.

## Attributes

SCTLR2MASK\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:13]

Reserved, RES0.

## CPTM0, bit [12]

## When FEAT\_CPA2 is implemented:

Mask bit for CPTM0.

| CPTM0   | Meaning                            |
|---------|------------------------------------|
| 0b0     | SCTLR2_EL2.CPTM0 is writeable.     |
| 0b1     | SCTLR2_EL2.CPTM0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CPTM, bit [11]

## When FEAT\_CPA2 is implemented:

Mask bit for CPTM.

| CPTM   | Meaning                           |
|--------|-----------------------------------|
| 0b0    | SCTLR2_EL2.CPTM is writeable.     |
| 0b1    | SCTLR2_EL2.CPTM is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CPTA0, bit [10]

## When FEAT\_CPA2 is implemented:

Mask bit for CPTA0.

| CPTA0   | Meaning                            |
|---------|------------------------------------|
| 0b0     | SCTLR2_EL2.CPTA0 is writeable.     |
| 0b1     | SCTLR2_EL2.CPTA0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

CPTA, bit [9]

## When FEAT\_CPA2 is implemented:

Mask bit for CPTA.

| CPTA   | Meaning                           |
|--------|-----------------------------------|
| 0b0    | SCTLR2_EL2.CPTA is writeable.     |
| 0b1    | SCTLR2_EL2.CPTA is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnPACM0, bit [8]

## When FEAT\_PAuth\_LR is implemented:

Mask bit for EnPACM0.

| EnPACM0   | Meaning                              |
|-----------|--------------------------------------|
| 0b0       | SCTLR2_EL2.EnPACM0 is writeable.     |
| 0b1       | SCTLR2_EL2.EnPACM0 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EnPACM, bit [7]

## When FEAT\_PAuth\_LR is implemented:

Mask bit for EnPACM.

| EnPACM   | Meaning                             |
|----------|-------------------------------------|
| 0b0      | SCTLR2_EL2.EnPACM is writeable.     |
| 0b1      | SCTLR2_EL2.EnPACM is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnIDCP128, bit [6]

## When FEAT\_SYSREG128 is implemented:

Mask bit for EnIDCP128.

| EnIDCP128   | Meaning                                |
|-------------|----------------------------------------|
| 0b0         | SCTLR2_EL2.EnIDCP128 is writeable.     |
| 0b1         | SCTLR2_EL2.EnIDCP128 is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EASE, bit [5]

## When FEAT\_DoubleFault2 is implemented:

Mask bit for EASE.

| EASE   | Meaning                           |
|--------|-----------------------------------|
| 0b0    | SCTLR2_EL2.EASE is writeable.     |
| 0b1    | SCTLR2_EL2.EASE is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnANERR, bit [4]

## When FEAT\_ANERR is implemented:

Mask bit for EnANERR.

| EnANERR   | Meaning                              |
|-----------|--------------------------------------|
| 0b0       | SCTLR2_EL2.EnANERR is writeable.     |
| 0b1       | SCTLR2_EL2.EnANERR is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnADERR, bit [3]

## When FEAT\_ADERR is implemented:

Mask bit for EnADERR.

| EnADERR   | Meaning                              |
|-----------|--------------------------------------|
| 0b0       | SCTLR2_EL2.EnADERR is writeable.     |
| 0b1       | SCTLR2_EL2.EnADERR is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NMEA,bit [2]

## When FEAT\_DoubleFault2 is implemented:

Mask bit for NMEA.

| NMEA   | Meaning                           |
|--------|-----------------------------------|
| 0b0    | SCTLR2_EL2.NMEA is writeable.     |
| 0b1    | SCTLR2_EL2.NMEA is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EMEC, bit [1]

## When FEAT\_MEC is implemented:

Mask bit for EMEC.

| EMEC   | Meaning                           |
|--------|-----------------------------------|
| 0b0    | SCTLR2_EL2.EMEC is writeable.     |
| 0b1    | SCTLR2_EL2.EMEC is not writeable. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [0]

Reserved, RES0.

## Accessing SCTLR2MASK\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name SCTLR2MASK\_EL2 or SCTLR2MASK\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SCTLR2MASK_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SCTLR2MASK_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLR2MASK_EL2;
```

MSR SCTLR2MASK\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsZero(EffectiveSCTLR2MASK_EL2()) then UNDEFINED; else SCTLR2MASK_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLR2MASK_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, SCTLR2MASK\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGRTR2_EL2.nSCTLR2MASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x328]; else X[t, 64] = SCTLR2MASK_EL1;
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = SCTLR2MASK_EL2; else X[t, 64] = SCTLR2MASK_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLR2MASK_EL1;
```

MSR SCTLR2MASK\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_SRMASK) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HFGWTR2_EL2.nSCTLR2MASK_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (!IsHCRXEL2Enabled() || HCRX_EL2.SRMASKEn == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x328] = X[t, 64]; elsif !IsZero(EffectiveSCTLR2MASK_EL1()) then UNDEFINED; else SCTLR2MASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.SRMASKEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.SRMASKEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if !IsZero(EffectiveSCTLR2MASK_EL2()) then UNDEFINED; else SCTLR2MASK_EL2 = X[t, 64]; else SCTLR2MASK_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLR2MASK_EL1 = X[t, 64];
```