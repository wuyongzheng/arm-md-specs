## D24.4.25 TRCCONFIGR, Trace Configuration Register

The TRCCONFIGR characteristics are:

## Purpose

Controls the tracing options.

## Configuration

AArch64 System register TRCCONFIGR bits [31:0] are architecturally mapped to External register TRCCONFIGR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCCONFIGR are UNDEFINED.

## Attributes

TRCCONFIGR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:19]

Reserved, RES0.

## ITO, bit [18]

When TRCIDR0.ITE == '1':

Instrumentation Trace Override.

| ITO   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Instrumentation Trace Override disabled. |
| 0b1   | Instrumentation Trace Override enabled.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [17:16]

Reserved, RES0.

## VMIDOPT, bit [15]

## When TRCIDR2.VMIDOPT == '01':

Virtual context identifier selection control.

| VMIDOPT   | Meaning                                                          |
|-----------|------------------------------------------------------------------|
| 0b0       | VTTBR_EL2.VMID is used as the Virtual context identifier.        |
| 0b1       | CONTEXTIDR_EL2.PROCID is used as the Virtual context identifier. |

## When TRCIDR2.VMIDOPT == '00':

Reserved, RES0.

Virtual context identifier selection control.

VTTBR\_EL2.VMID is used as the Virtual context identifier.

## When TRCIDR2.VMIDOPT == '10':

Reserved, RES1.

Virtual context identifier selection control.

CONTEXTIDR\_EL2.PROCID is used as the Virtual context identifier.

## Otherwise:

Reserved, RES0.

QE, bits [14:13]

## When TRCIDR0.QSUPP == '01':

Qelement generation control.

| QE   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                           |
| 0b01 | Qelements with instruction counts are enabled. Qelements without instruction counts are disabled. |

All other values are reserved.

## When TRCIDR0.QSUPP == '10':

Qelement generation control.

| QE   | Meaning                                                                                          |
|------|--------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                          |
| 0b11 | Qelements with instruction counts are enabled. Qelements without instruction counts are enabled. |

All other values are reserved.

## When TRCIDR0.QSUPP == '11':

Qelement generation control.

| QE   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                           |
| 0b01 | Qelements with instruction counts are enabled. Qelements without instruction counts are disabled. |
| 0b11 | Qelements with instruction counts are enabled. Qelements without instruction counts are enabled.  |

All other values are reserved.

## Otherwise:

Reserved, RES0.

## RS, bit [12]

## When TRCIDR0.RETSTACK == '1':

Return stack control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TS, bit [11]

## When TRCIDR0.TSSIZE != '00000':

Global timestamp tracing control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

| RS   | Meaning                   |
|------|---------------------------|
| 0b0  | Return stack is disabled. |
| 0b1  | Return stack is enabled.  |

| TS   | Meaning                               |
|------|---------------------------------------|
| 0b0  | Global timestamp tracing is disabled. |
| 0b1  | Global timestamp tracing is enabled.  |

## Otherwise:

Reserved, RES0.

## Bits [10:8]

Reserved, RES0.

## VMID, bit [7]

## When TRCIDR2.VMIDSIZE != '00000':

Virtual context identifier tracing control.

| VMID   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Virtual context identifier tracing is disabled. |
| 0b1    | Virtual context identifier tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

CID, bit [6]

## When TRCIDR2.CIDSIZE != '00000':

Context identifier tracing control.

| CID   | Meaning                                 |
|-------|-----------------------------------------|
| 0b0   | Context identifier tracing is disabled. |
| 0b1   | Context identifier tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [5]

Reserved, RES0.

CCI, bit [4]

When TRCIDR0.TRCCCI == '1':

Cycle counting instruction tracing control.

| CCI   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Cycle counting instruction tracing is disabled. |
| 0b1   | Cycle counting instruction tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BB, bit [3]

## When TRCIDR0.TRCBB == '1':

Branch broadcasting control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [2:1]

Reserved, RES0.

## Bit [0]

Reserved, RES1.

## Accessing TRCCONFIGR

Must always be programmed.

TRCCONFIGR.QE must be set to 0b00 if TRCCONFIGR.BB is not 0.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCONFIGR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0100 | 0b000 |

| BB   | Meaning                          |
|------|----------------------------------|
| 0b0  | Branch broadcasting is disabled. |
| 0b1  | Branch broadcasting is enabled.  |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCONFIGR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCONFIGR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCONFIGR;
```

MSR TRCCONFIGR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then
```

```
UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCONFIGR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCONFIGR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCONFIGR = X[t, 64];
```
