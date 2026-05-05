## D24.4.60 TRCSSCSR&lt;n&gt;, Trace Single-shot Comparator Control Status Register &lt;n&gt;, n = 0 - 7

The TRCSSCSR&lt;n&gt; characteristics are:

## Purpose

Returns the status of the corresponding Single-shot Comparator Control.

## Configuration

AArch64 System register TRCSSCSR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSSCSR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMSSCC) &gt; n. Otherwise, direct accesses to TRCSSCSR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSSCSR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## STATUS, bit [31]

Single-shot Comparator Control status. Indicates if any of the comparators selected by this Single-shot Comparator control have matched. The selected comparators are defined by TRCSSCCR&lt;n&gt;.ARC, TRCSSCCR&lt;n&gt;.SAC, and TRCSSPCICR&lt;n&gt;.PC.

| STATUS   | Meaning                                                                                                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | No match has occurred. When the first match occurs, this field takes a value of 1. It remains at 1 until explicitly modified by a write to this register.                                                          |
| 0b1      | One or more matches has occurred. If TRCSSCCR<n>.RST == 0 then: • There is only one match and no more matches are possible. • Software must reset this field to 0 to re-enable the Single-shot Comparator Control. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## PENDING, bit [30]

Single-shot pending status. The Single-shot Comparator Control fired while the resources were in the Paused state.

The reset behavior of this field is:

· On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [29:4]

Reserved, RES0.

## PC, bit [3]

PE Comparator Input support. Indicates if the Single-shot Comparator Control supports PE Comparator Inputs.

| PC   | Meaning                                                                                                                                                                                                                                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support PE Comparator Inputs. Selecting any PE Comparator Inputs using the associated TRCSSPCICR<n> results in CONSTRAINED UNPREDICTABLE behavior of the Single-shot Comparator Control resource. The Single-shot Comparator Control might match unexpectedly or might not match. |
| 0b1  | This Single-shot Comparator Control supports PE Comparator Inputs.                                                                                                                                                                                                                                                             |

Access to this field is RO.

## DV, bit [2]

Data value comparator support. Data value comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

| DV   | Meaning                                                                      |
|------|------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support data value comparisons. |
| 0b1  | This Single-shot Comparator Control supports data value comparisons.         |

This field reads as 0.

Access to this field is RO.

## DA, bit [1]

Data Address Comparator support. Data address comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

| PENDING   | Meaning                           |
|-----------|-----------------------------------|
| 0b0       | No match has occurred.            |
| 0b1       | One or more matches has occurred. |

| DA   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support data address comparisons. |
| 0b1  | This Single-shot Comparator Control supports data address comparisons.         |

This field reads as 0.

Access to this field is RO.

## INST, bit [0]

Instruction Address Comparator support. Indicates if the Single-shot Comparator Control supports instruction address comparisons.

| INST   | Meaning                                                                               |
|--------|---------------------------------------------------------------------------------------|
| 0b0    | This Single-shot Comparator Control does not support instruction address comparisons. |
| 0b1    | This Single-shot Comparator Control supports instruction address comparisons.         |

This field reads as 1.

Access to this field is RO.

## Accessing TRCSSCSR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSSCSR&lt;m&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b1 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCSSCSRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCSR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCSR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCSR[m];
```

MSR TRCSSCSR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b1 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCSSCSRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCSR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCSR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCSR[m] = X[t, 64];
```
