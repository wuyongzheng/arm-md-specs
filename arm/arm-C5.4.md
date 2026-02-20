## C5.4 A64 System instructions for address translation

This section lists the A64 System instructions for address translation.

## C5.4.1 AT S12E0R, Address Translate Stages 1 and 2 EL0 Read

The AT S12E0R characteristics are:

## Purpose

Performs stage 1 and 2 address translation, with permissions as if reading from the given virtual address from EL0, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime.
- Otherwise, the EL1&amp;0 translation regime.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S12E0R are UNDEFINED.

## Attributes

AT S12E0R is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S12E0R

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S12E0R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00' then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Read); else AArch64.AT(X[t, 64], TranslationStage_12, EL0, ATAccess_Read); elsif PSTATE.EL == EL3 then if !EL2Enabled() then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Read); elsif EL2Enabled() && (ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00') then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Read); else AArch64.AT(X[t, 64], TranslationStage_12, EL0, ATAccess_Read);
```

## C5.4.2 AT S12E0W, Address Translate Stages 1 and 2 EL0 Write

The AT S12E0W characteristics are:

## Purpose

Performs stage 1 and 2 address translation, with permissions as if writing to the given virtual address from EL0, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime.
- Otherwise, the EL1&amp;0 translation regime.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S12E0W are UNDEFINED.

## Attributes

AT S12E0W is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S12E0W

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S12E0W, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b111 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00' then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Write); else AArch64.AT(X[t, 64], TranslationStage_12, EL0, ATAccess_Write); elsif PSTATE.EL == EL3 then if !EL2Enabled() then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Write); elsif EL2Enabled() && (ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00') then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Write); else AArch64.AT(X[t, 64], TranslationStage_12, EL0, ATAccess_Write);
```

## C5.4.3 AT S12E1R, Address Translate Stages 1 and 2 EL1 Read

The AT S12E1R characteristics are:

## Purpose

Performs stage 1 and 2 address translation, with permissions as if reading from the given virtual address from EL1, or from EL2 if the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S12E1R are UNDEFINED.

## Attributes

AT S12E1R is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S12E1R

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S12E1R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00' then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Read); else AArch64.AT(X[t, 64], TranslationStage_12, EL1, ATAccess_Read); elsif PSTATE.EL == EL3 then if !EL2Enabled() then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Read); elsif EL2Enabled() && (ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00') then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Read); else AArch64.AT(X[t, 64], TranslationStage_12, EL1, ATAccess_Read);
```

## C5.4.4 AT S12E1W, Address Translate Stages 1 and 2 EL1 Write

The AT S12E1W characteristics are:

## Purpose

Performs stage 1 and 2 address translation, with permissions as if writing to the given virtual address from EL1, or from EL2 if the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S12E1W are UNDEFINED.

## Attributes

AT S12E1W is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S12E1W

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S12E1W, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00' then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Write); else AArch64.AT(X[t, 64], TranslationStage_12, EL1, ATAccess_Write); elsif PSTATE.EL == EL3 then if !EL2Enabled() then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Write); elsif EL2Enabled() && (ELIsInHost(EL0) || HCR_EL2.<DC,VM> == '00') then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Write); else AArch64.AT(X[t, 64], TranslationStage_12, EL1, ATAccess_Write);
```

## C5.4.5 AT S1E0R, Address Translate Stage 1 EL0 Read

The AT S1E0R characteristics are:

## Purpose

Performs stage 1 address translation, with permissions as if reading from the given virtual address from EL0, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime.
- Otherwise, the EL1&amp;0 translation regime.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E0R are UNDEFINED.

## Attributes

AT S1E0R is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E0R

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E0R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E0R == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Read); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Read); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Read);
```

## C5.4.6 AT S1E0W, Address Translate Stage 1 EL0 Write

The AT S1E0W characteristics are:

## Purpose

Performs stage 1 address translation, with permissions as if writing to the given virtual address from EL0, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime.
- Otherwise, the EL1&amp;0 translation regime.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E0W are UNDEFINED.

## Attributes

AT S1E0W is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E0W

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E0W, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b011 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E0W == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Write); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Write); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL0, ATAccess_Write);
```

## C5.4.7 AT S1E1A, Address Translate Stage 1 EL1 Without Permission checks

The AT S1E1A characteristics are:

## Purpose

Performs a stage 1 address translation, while ignoring the permission checks using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_ATS1A is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E1A are UNDEFINED.

## Attributes

AT S1E1A is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

## Executing AT S1E1A

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E1A, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ATS1A) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E1A == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Any); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Any); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Any);
```

## C5.4.8 AT S1E1R, Address Translate Stage 1 EL1 Read

The AT S1E1R characteristics are:

## Purpose

Performs stage 1 address translation, with permissions as if reading from the given virtual address from EL1, or from EL2 if the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E1R are UNDEFINED.

## Attributes

AT S1E1R is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E1R

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E1R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E1R == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Read); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Read); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Read);
```

## C5.4.9 AT S1E1RP, Address Translate Stage 1 EL1 Read PAN

The AT S1E1RP characteristics are:

## Purpose

Performs a stage 1 address translation, where the value of PSTATE.PAN determines if a read from a location will generate a Permission fault for a privileged access, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_PAN2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E1RP are UNDEFINED.

## Attributes

AT S1E1RP is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E1RP

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E1RP, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_PAN2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E1RP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_ReadPAN); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_ReadPAN); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_ReadPAN);
```

## C5.4.10 AT S1E1W, Address Translate Stage 1 EL1 Write

The AT S1E1W characteristics are:

## Purpose

Performs stage 1 address translation, with permissions as if writing to the given virtual address from EL1, or from EL2 if the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E1W are UNDEFINED.

## Attributes

AT S1E1W is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E1W

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E1W, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E1W == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Write); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Write); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_Write);
```

## C5.4.11 AT S1E1WP, Address Translate Stage 1 EL1 Write PAN

The AT S1E1WP characteristics are:

## Purpose

Performs a stage 1 address translation, where the value of PSTATE.PAN determines if a write to a location will generate a Permission fault for a privileged access, using the following translation regime:

- When EL2 is implemented and enabled in the Security state described by the current Effective value of SCR\_EL3.{NSE, NS}:
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the EL1&amp;0 translation regime, accessed from EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the EL2&amp;0 translation regime, accessed from EL2.
- Otherwise, the EL1&amp;0 translation regime, accessed from EL1.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_PAN2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E1WP are UNDEFINED.

## Attributes

AT S1E1WP is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E1WP

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E1WP, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b000 | 0b0111 | 0b1001 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_PAN2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.AT == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGITR_EL2.ATS1E1WP == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_WritePAN); elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_WritePAN); elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL1, ATAccess_WritePAN);
```

## C5.4.12 AT S1E2A, Address Translate Stage 1 EL2 Without Permission checks

The AT S1E2A characteristics are:

## Purpose

Performs stage 1 address translation as defined for EL2, while ignoring permissions checks from the given virtual address.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_ATS1A is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E2A are UNDEFINED.

## Attributes

AT S1E2A is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

## Executing AT S1E2A

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E2A, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ATS1A) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL2, ATAccess_Any); elsif PSTATE.EL == EL3 then
```

```
if !EL2Enabled() then UNDEFINED; else AArch64.AT(X[t, 64],
```

TranslationStage\_1, EL2, ATAccess\_Any);

## C5.4.13 AT S1E2R, Address Translate Stage 1 EL2 Read

The AT S1E2R characteristics are:

## Purpose

Performs stage 1 address translation as defined for EL2, with permissions as if reading from the given virtual address.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E2R are UNDEFINED.

## Attributes

AT S1E2R is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32                            |
|-------------------------------|-------------------------------|
| 31                            | 0                             |
| Input address for translation | Input address for translation |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E2R

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E2R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED;
```

```
elsif PSTATE.EL == EL2 then AArch64.AT(X[t, 64], TranslationStage_1, EL2, ATAccess_Read); elsif PSTATE.EL == EL3 then if !EL2Enabled() then UNDEFINED; else AArch64.AT(X[t, 64], TranslationStage_1, EL2, ATAccess_Read);
```

## C5.4.14 AT S1E2W, Address Translate Stage 1 EL2 Write

The AT S1E2W characteristics are:

## Purpose

Performs stage 1 address translation as defined for EL2, with permissions as if writing to the given virtual address.

When FEAT\_RME is implemented, if the Effective value of SCR\_EL3.{NSE, NS} is a reserved value, this instruction is UNDEFINED at EL3.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E2W are UNDEFINED.

## Attributes

AT S1E2W is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32                            |
|-------------------------------|-------------------------------|
| Input address for translation |                               |
| 31                            | 0                             |
| Input address for translation | Input address for translation |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E2W

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E2W, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b0111 | 0b1000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

```
AArch64.AT(X[t, 64], TranslationStage_1, EL2, ATAccess_Write); elsif PSTATE.EL == EL3 then if !EL2Enabled() then UNDEFINED; else AArch64.AT(X[t, 64], TranslationStage_1, EL2, ATAccess_Write);
```

## C5.4.15 AT S1E3A, Address Translate Stage 1 EL3 Without Permission checks

The AT S1E3A characteristics are:

## Purpose

Performs stage 1 address translation as defined for EL3, while ignoring permissions checks from the given virtual address.

## Configuration

This system instruction is present only when FEAT\_ATS1A is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E3A are UNDEFINED.

## Attributes

AT S1E3A is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

## Executing AT S1E3A

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E3A, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b0111 | 0b1001 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ATS1A) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL3, ATAccess_Any);
```

## C5.4.16 AT S1E3R, Address Translate Stage 1 EL3 Read

The AT S1E3R characteristics are:

## Purpose

Performs stage 1 address translation as defined for EL3, with permissions as if reading from the given virtual address.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E3R are UNDEFINED.

## Attributes

AT S1E3R is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E3R

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E3R, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b0111 | 0b1000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL3,
```

```
ATAccess_Read);
```

## C5.4.17 AT S1E3W, Address Translate Stage 1 EL3 Write

The AT S1E3W characteristics are:

## Purpose

Performs stage 1 address translation as defined for EL3, with permissions as if writing to the given virtual address.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to AT S1E3W are UNDEFINED.

## Attributes

AT S1E3W is a 64-bit System instruction.

## Field descriptions

<!-- image -->

| 63                            | 32   |
|-------------------------------|------|
| Input address for translation |      |
| 31                            | 0    |
| Input address for translation |      |

## IA, bits [63:0]

Input address for translation. The resulting address can be read from the PAR\_EL1.

If the address translation instructions are targeting a translation regime that is using AArch32, and so has a V A of only 32 bits, then V A[63:32] is RES0.

## Executing AT S1E3W

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

AT S1E3W, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b0111 | 0b1000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then AArch64.AT(X[t, 64], TranslationStage_1, EL3,
```

```
ATAccess_Write);
```