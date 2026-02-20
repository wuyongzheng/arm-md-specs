## D24.11 Guarded Control Stack registers

This section lists the Guarded Control Stack registers in AArch64.

## D24.11.1 GCSCR\_EL1, Guarded Control Stack Control Register (EL1)

The GCSCR\_EL1 characteristics are:

## Purpose

Controls the Guarded Control Stack at EL1.

## Configuration

This register is present only when FEAT\_GCS is implemented. Otherwise, direct accesses to GCSCR\_EL1 are UNDEFINED.

## Attributes

GCSCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## STREn, bit [9]

Execution of the following instructions are trapped:

- GCSSTR.
- GCSSTTR if any of the following are true.
- PSTATE.UAO is 1.
- If EL2 is implemented and enabled in the current Security state and the Effective value of HCR\_EL2.{NV,NV1} is {1,1}.

| STREn   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b0     | Execution of any of the specified instructions at EL1 causes a GCS exception. |
| 0b1     | This control does not cause any instructions to be trapped.                   |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## PUSHMEn, bit [8]

Trap GCSPUSHM instruction.

| PUSHMEn   | Meaning                                                            |
|-----------|--------------------------------------------------------------------|
| 0b0       | Execution of a GCSPUSHMinstruction at EL1 causes a Trap exception. |
| 0b1       | This control does not cause any instructions to be trapped.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [7]

Reserved, RES0.

## EXLOCKEN,bit [6]

Exception state lock.

Prevents MSR instructions from writing to ELR\_EL1 or SPSR\_EL1.

| EXLOCKEN   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | EL1 exception state locking disabled. |
| 0b1        | EL1 exception state locking enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## RVCHKEN,bit [5]

Return value check enable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:1]

Reserved, RES0.

## PCRSEL, bit [0]

Guarded Control Stack procedure call return enable selection.

| RVCHKEN   | Meaning                                |
|-----------|----------------------------------------|
| 0b0       | Return value checking disabled at EL1. |
| 0b1       | Return value checking enabled at EL1.  |

| PCRSEL   | Meaning                                           |
|----------|---------------------------------------------------|
| 0b0      | Guarded Control Stack at EL1 is not PCR Selected. |
| 0b1      | Guarded Control Stack at EL1 is PCR Selected.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing GCSCR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name GCSCR\_EL1 or GCSCR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GCSCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8D0]; else X[t, 64] = GCSCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = GCSCR_EL2; else X[t, 64] = GCSCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GCSCR_EL1;
```

MSR GCSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8D0] = X[t, 64]; else GCSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then GCSCR_EL2 = X[t, 64]; else GCSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSCR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, GCSCR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x8D0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED;
```

```
elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSCR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = GCSCR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR GCSCR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x8D0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSCR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then GCSCR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.11.2 GCSCR\_EL2, Guarded Control Stack Control Register (EL2)

The GCSCR\_EL2 characteristics are:

## Purpose

Controls the Guarded Control Stack at EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_GCS is implemented. Otherwise, direct accesses to GCSCR\_EL2 are UNDEFINED.

## Attributes

GCSCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## STREn, bit [9]

Execution of the following instructions are trapped:

- GCSSTR.
- GCSSTTR if any of the following are true.
- The Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.
- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, and PSTATE.UAO is 1.

| STREn   | Meaning                                                                      |
|---------|------------------------------------------------------------------------------|
| 0b0     | Execution of any of the specified instructions at EL2 cause a GCS exception. |
| 0b1     | This control does not cause any instructions to be trapped.                  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## PUSHMEn, bit [8]

Trap GCSPUSHM instruction.

| PUSHMEn   | Meaning                                                            |
|-----------|--------------------------------------------------------------------|
| 0b0       | Execution of a GCSPUSHMinstruction at EL2 causes a Trap exception. |
| 0b1       | This control does not cause any instructions to be trapped.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [7]

Reserved, RES0.

## EXLOCKEN,bit [6]

Exception state lock.

Prevents MSR instructions from writing to ELR\_EL2 or SPSR\_EL2.

| EXLOCKEN   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | EL2 exception state locking disabled. |
| 0b1        | EL2 exception state locking enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## RVCHKEN,bit [5]

Return value check enable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:1]

Reserved, RES0.

## PCRSEL, bit [0]

Guarded Control Stack procedure call return enable selection.

| RVCHKEN   | Meaning                                |
|-----------|----------------------------------------|
| 0b0       | Return value checking disabled at EL2. |
| 0b1       | Return value checking enabled at EL2.  |

| PCRSEL   | Meaning                                           |
|----------|---------------------------------------------------|
| 0b0      | Guarded Control Stack at EL2 is not PCR Selected. |
| 0b1      | Guarded Control Stack at EL2 is PCR Selected.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing GCSCR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name GCSCR\_EL2 or GCSCR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GCSCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = GCSCR_EL2;
```

MSR GCSCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSCR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, GCSCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8D0]; else X[t, 64] = GCSCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = GCSCR_EL2; else X[t, 64] = GCSCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GCSCR_EL1;
```

MSR GCSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8D0] = X[t, 64]; else GCSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then GCSCR_EL2 = X[t, 64]; else GCSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSCR_EL1 = X[t, 64];
```

## D24.11.3 GCSCR\_EL3, Guarded Control Stack Control Register (EL3)

The GCSCR\_EL3 characteristics are:

## Purpose

Controls the Guarded Control Stack at EL3.

## Configuration

This register is present only when FEAT\_GCS is implemented and EL3 is implemented. Otherwise, direct accesses to GCSCR\_EL3 are UNDEFINED.

## Attributes

GCSCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:10]

Reserved, RES0.

## STREn, bit [9]

Execution of the following instructions are trapped:

- GCSSTR.
- GCSSTTR.

| STREn   | Meaning                                                                      |
|---------|------------------------------------------------------------------------------|
| 0b0     | Execution of any of the specified instructions at EL3 cause a GCS exception. |
| 0b1     | This control does not cause any instructions to be trapped.                  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## PUSHMEn, bit [8]

Trap GCSPUSHM instruction.

| PUSHMEn   | Meaning                                                            |
|-----------|--------------------------------------------------------------------|
| 0b0       | Execution of a GCSPUSHMinstruction at EL3 causes a Trap exception. |
| 0b1       | This control does not cause any instructions to be trapped.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [7]

Reserved, RES0.

## EXLOCKEN,bit [6]

Exception state lock.

Prevents MSR instructions from writing to ELR\_EL3 or SPSR\_EL3.

| EXLOCKEN   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | EL3 exception state locking disabled. |
| 0b1        | EL3 exception state locking enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## RVCHKEN,bit [5]

Return value check enable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:1]

Reserved, RES0.

## PCRSEL, bit [0]

Guarded Control Stack procedure call return enable selection.

| RVCHKEN   | Meaning                                |
|-----------|----------------------------------------|
| 0b0       | Return value checking disabled at EL3. |
| 0b1       | Return value checking enabled at EL3.  |

| PCRSEL   | Meaning                                           |
|----------|---------------------------------------------------|
| 0b0      | Guarded Control Stack at EL3 is not PCR Selected. |
| 0b1      | Guarded Control Stack at EL3 is PCR Selected.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing GCSCR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GCSCR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0101 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_GCS) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = GCSCR_EL3;
```

MSR GCSCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0101 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_GCS) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.GCSCR_EL3 == '1' AArch64.SystemAccessTrap(EL3, 0x18); else GCSCR_EL3 = X[t, 64];
```

```
then
```

## D24.11.4 GCSCRE0\_EL1, Guarded Control Stack Control Register (EL0)

The GCSCRE0\_EL1 characteristics are:

## Purpose

Controls the Guarded Control Stack at EL0.

## Configuration

This register is present only when FEAT\_GCS is implemented. Otherwise, direct accesses to GCSCRE0\_EL1 are UNDEFINED.

## Attributes

GCSCRE0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:11]

Reserved, RES0.

## nTR, bit [10]

Trap GCS register accesses from EL0.

| nTR   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | Read accesses to GCSPR_EL0 at EL0 cause a Trap exception.   |
| 0b1   | This control does not cause any instructions to be trapped. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## STREn, bit [9]

Execution of the following instructions are trapped:

- GCSSTR.
- GCSSTTR.

| STREn   | Meaning                                                                      |
|---------|------------------------------------------------------------------------------|
| 0b0     | Execution of any of the specified instructions at EL0 cause a GCS exception. |
| 0b1     | This control does not cause any instructions to be trapped.                  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## PUSHMEn, bit [8]

Trap GCSPUSHM instruction.

| PUSHMEn   | Meaning                                                            |
|-----------|--------------------------------------------------------------------|
| 0b0       | Execution of a GCSPUSHMinstruction at EL0 causes a Trap exception. |
| 0b1       | This control does not cause any instructions to be trapped.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [7:6]

Reserved, RES0.

## RVCHKEN,bit [5]

Return value check enable.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:1]

Reserved, RES0.

## PCRSEL, bit [0]

Guarded Control Stack procedure call return enable selection.

| RVCHKEN   | Meaning                                |
|-----------|----------------------------------------|
| 0b0       | Return value checking disabled at EL0. |
| 0b1       | Return value checking enabled at EL0.  |

| PCRSEL   | Meaning                                           |
|----------|---------------------------------------------------|
| 0b0      | Guarded Control Stack at EL0 is not PCR Selected. |
| 0b1      | Guarded Control Stack at EL0 is PCR Selected.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing GCSCRE0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GCSCRE0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b010 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nGCS_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSCRE0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSCRE0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GCSCRE0_EL1;
```

MSR GCSCRE0\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b010 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nGCS_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSCRE0_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSCRE0_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSCRE0_EL1 = X[t, 64];
```

## D24.11.5 GCSPR\_EL0, Guarded Control Stack Pointer Register (EL0)

The GCSPR\_EL0 characteristics are:

## Purpose

Contains the Guarded Control Stack Pointer at EL0.

## Configuration

This register is present only when FEAT\_GCS is implemented. Otherwise, direct accesses to GCSPR\_EL0 are UNDEFINED.

## Attributes

GCSPR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| PTR[63:3]      | PTR[63:3]      | PTR[63:3]      |
| 31             | 0              |                |
| PTR[63:3] RES0 | PTR[63:3] RES0 | PTR[63:3] RES0 |

## PTR[63:3], bits [63:3]

EL0 Guarded Control Stack Pointer bits [63:3].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [2:0]

Reserved, RES0.

## Accessing GCSPR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, GCSPR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif (!EL2Enabled() || HCR_EL2.TGE != '1') && GCSCRE0_EL1.nTR == '0' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && HCR_EL2.TGE == '1' && GCSCRE0_EL1.nTR == '0' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGRTR_EL2.nGCS_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSPR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nGCS_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSPR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSPR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = GCSPR_EL0;
```

MSR GCSPR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nGCS_EL0 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSPR_EL0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then
```

```
UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSPR_EL0 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSPR_EL0 = X[t, 64];
```

## D24.11.6 GCSPR\_EL1, Guarded Control Stack Pointer Register (EL1)

The GCSPR\_EL1 characteristics are:

## Purpose

Contains the Guarded Control Stack Pointer at EL1.

## Configuration

This register is present only when FEAT\_GCS is implemented. Otherwise, direct accesses to GCSPR\_EL1 are UNDEFINED.

## Attributes

GCSPR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| PTR[63:3]      | PTR[63:3]      | PTR[63:3]      |
| 31             | 0              |                |
| PTR[63:3] RES0 | PTR[63:3] RES0 | PTR[63:3] RES0 |

## PTR[63:3], bits [63:3]

EL1 Guarded Control Stack Pointer bits [63:3].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [2:0]

Reserved, RES0.

## Accessing GCSPR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name GCSPR\_EL1 or GCSPR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, GCSPR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8C0]; else X[t, 64] = GCSPR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = GCSPR_EL2; else X[t, 64] = GCSPR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GCSPR_EL1;
```

MSR GCSPR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8C0] = X[t, 64]; else GCSPR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif ELIsInHost(EL2) then GCSPR_EL2 = X[t, 64]; else GCSPR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSPR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, GCSPR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x8C0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSPR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = GCSPR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR GCSPR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x8C0] = X[t, 64];
```

```
elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSPR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then GCSPR_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.11.7 GCSPR\_EL2, Guarded Control Stack Pointer Register (EL2)

The GCSPR\_EL2 characteristics are:

## Purpose

Contains the Guarded Control Stack Pointer at EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_GCS is implemented. Otherwise, direct accesses to GCSPR\_EL2 are UNDEFINED.

## Attributes

GCSPR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| PTR[63:3]      | PTR[63:3]      | PTR[63:3]      |
| 31             | 2 0            |                |
| PTR[63:3] RES0 | PTR[63:3] RES0 | PTR[63:3] RES0 |

## PTR[63:3], bits [63:3]

EL2 Guarded Control Stack Pointer bits [63:3].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [2:0]

Reserved, RES0.

## Accessing GCSPR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name GCSPR\_EL2 or GCSPR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = GCSPR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = GCSPR_EL2;
```

MSR GCSPR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else GCSPR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSPR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, GCSPR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x8C0]; else X[t, 64] = GCSPR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = GCSPR_EL2; else X[t, 64] = GCSPR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = GCSPR_EL1;
```

MSR GCSPR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_GCS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.nGCS_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x8C0] = X[t, 64]; else GCSPR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.GCSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.GCSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then GCSPR_EL2 = X[t, 64]; else GCSPR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then GCSPR_EL1 = X[t, 64];
```

## D24.11.8 GCSPR\_EL3, Guarded Control Stack Pointer Register (EL3)

The GCSPR\_EL3 characteristics are:

## Purpose

Contains the Guarded Control Stack Pointer at EL3.

## Configuration

This register is present only when FEAT\_GCS is implemented and EL3 is implemented. Otherwise, direct accesses to GCSPR\_EL3 are UNDEFINED.

## Attributes

GCSPR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| PTR[63:3]      | PTR[63:3]      | PTR[63:3]      |
| 31             | 0              |                |
| PTR[63:3] RES0 | PTR[63:3] RES0 | PTR[63:3] RES0 |

## PTR[63:3], bits [63:3]

EL3 Guarded Control Stack Pointer bits [63:3].

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [2:0]

Reserved, RES0.

## Accessing GCSPR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0101 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_GCS) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = GCSPR_EL3;
```

MSR GCSPR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0010 | 0b0101 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_GCS) && HaveEL(EL3)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.GCSPR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else GCSPR_EL3 = X[t, 64];
```