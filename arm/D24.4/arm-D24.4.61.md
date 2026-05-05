## D24.4.61 TRCSSPCICR&lt;n&gt;, Trace Single-shot Processing Element Comparator Input Control Register &lt;n&gt;, n = 0 - 7

The TRCSSPCICR&lt;n&gt; characteristics are:

## Purpose

Returns the status of the corresponding Single-shot Comparator Control.

## Configuration

AArch64 System register TRCSSPCICR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSSPCICR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMSSCC) &gt; n, UInt(TRCIDR4.NUMPC) &gt; 0, and TRCSSCSR&lt;n&gt;.PC == '1'. Otherwise, direct accesses to TRCSSPCICR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSSPCICR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## PC[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more PE Comparator Inputs for Single-shot control.

| PC[<m>]   | Meaning                                                                         |
|-----------|---------------------------------------------------------------------------------|
| 0b0       | The single PE Comparator Input <m>, is not selected as for Single-shot control. |
| 0b1       | The single PE Comparator Input <m>, is selected as for Single-shot control.     |

This bit is RES0 if m &gt;= TRCIDR4.NUMPC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSSPCICR&lt;n&gt;

Must be programmed if implemented and any TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSSPCICR&lt;m&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b011 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSPCICR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSPCICR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then
```

```
Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSPCICR[m];
```

MSR TRCSSPCICR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b011 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSPCICR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSPCICR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSPCICR[m] = X[t, 64];
```
