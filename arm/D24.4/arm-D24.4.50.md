## D24.4.50 TRCITEEDCR, Instrumentation Trace Extension External Debug Control Register

The TRCITEEDCR characteristics are:

## Purpose

Controls instrumentation trace filtering.

## Configuration

AArch64 System register TRCITEEDCR bits [31:0] are architecturally mapped to External register TRCITEEDCR[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and FEAT\_ITE is implemented. Otherwise, direct accesses to TRCITEEDCR are UNDEFINED.

## Attributes

TRCITEEDCR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      | 32    |
|---------|-------|
| RES0 31 | 1 0   |
| RES0    | E1 E0 |

## Bits [63:7]

Reserved, RES0.

## RL, bit [6]

## When FEAT\_RME is implemented:

Instrumentation Trace in Realm state.

| RL   | Meaning                                          |
|------|--------------------------------------------------|
| 0b0  | Instrumentation trace prohibited in Realm state. |
| 0b1  | Instrumentation trace permitted in Realm state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Realm state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## S, bit [5]

## When Secure state is implemented:

Instrumentation Trace in Secure state.

<!-- image -->

| S   | Meaning                                           |
|-----|---------------------------------------------------|
| 0b0 | Instrumentation trace prohibited in Secure state. |
| 0b1 | Instrumentation trace permitted in Secure state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

When FEAT\_RME is not implemented, this field is used in conjunction with TRCCONFIGR.ITO, TRCITEEDCR.E3, and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Secure state.

When FEAT\_RME is implemented, this field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Secure state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NS, bit [4]

## When Any of Non-secure EL2, EL1, or EL0 are implemented:

Instrumentation Trace in Non-secure state.

| NS   | Meaning                                               |
|------|-------------------------------------------------------|
| 0b0  | Instrumentation trace prohibited in Non-secure state. |
| 0b1  | Instrumentation trace permitted in Non-secure state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Non-secure state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E3, bit [3]

## When EL3 is implemented:

Instrumentation Trace Enable at EL3.

| E3   | Meaning                                  |
|------|------------------------------------------|
| 0b0  | Instrumentation trace prohibited at EL3. |
| 0b1  | Instrumentation trace permitted at EL3.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

When FEAT\_RME is not implemented, TRCITEEDCR.E3 is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.S to control whether Instrumentation trace is permitted or prohibited at EL3.

When FEAT\_RME is implemented, TRCITEEDCR.E3 is used in conjunction with TRCCONFIGR.ITO to control whether Instrumentation trace is permitted or prohibited at EL3.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E&lt;m&gt;, bits [m], for m = 2 to 0

Instrumentation Trace Enable at EL&lt;m&gt;.

| E<m>   | Meaning                                    |
|--------|--------------------------------------------|
| 0b0    | Instrumentation trace prohibited at EL<m>. |
| 0b1    | Instrumentation trace permitted at EL<m>.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This bit is used in conjunction with TRCCONFIGR.ITO, TRCITEEDCR.NS, TRCITEEDCR.S, and TRCITEEDCR.RL to control whether Instrumentation trace is permitted or prohibited at EL&lt;m&gt; in the specified Security states.

TRCITEEDCR.E&lt;2&gt; is RES0 if EL2 is not implemented in any Security states.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCITEEDCR

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCITEEDCR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_ITE)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCITEEDCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCITEEDCR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCITEEDCR;
```

MSR TRCITEEDCR, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && ↪ → IsFeatureImplemented(FEAT_ITE)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCITEEDCR = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCITEEDCR = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCITEEDCR = X[t, 64];
```
