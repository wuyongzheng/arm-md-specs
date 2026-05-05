## D24.4.22 TRCCNTCTLR&lt;n&gt;, Trace Counter Control Register &lt;n&gt;, n = 0 - 3

The TRCCNTCTLR&lt;n&gt; characteristics are:

## Purpose

Controls the operation of Counter &lt;n&gt;.

## Configuration

AArch64 System register TRCCNTCTLR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCCNTCTLR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTCTLR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCNTCTLR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:18]

Reserved, RES0.

## CNTCHAIN, bit [17]

## When (n MOD 2) != 0:

For TRCCNTCTLR3 and TRCCNTCTLR1, this field controls whether the Counter decrements when a reload event occurs for Counter &lt;n-1&gt;.

| CNTCHAIN   | Meaning                                                                                                                                                |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | The Counter does not decrement when a reload event for Counter <n-1> occurs.                                                                           |
| 0b1        | Counter <n> decrements when a reload event for Counter <n-1> occurs. This concatenates Counter <n> and Counter <n-1>, to provide a larger count value. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLDSELF, bit [16]

Controls whether a reload event occurs for the Counter, when the Counter reaches zero.

| RLDSELF   | Meaning                                               |
|-----------|-------------------------------------------------------|
| 0b0       | Normal mode. The Counter is in Normal mode.           |
| 0b1       | Self-reload mode. The Counter is in Self-reload mode. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RLDEVENT\_TYPE, bit [15]

Selects an event, that when it occurs causes a reload event for Counter

Chooses the type of Resource Selector.

| RLDEVENT_TYPE   | Meaning                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Asingle Resource Selector. TRCCNTCTLR.RLDEVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                        |
| 0b1             | ABoolean-combined pair of Resource Selectors. TRCCNTCTLR.RLDEVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCCNTCTLR.RLDEVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [14:13]

Reserved, RES0.

## RLDEVENT\_SEL, bits [12:8]

Selects an event, that when it occurs causes a reload event for Counter

Defines the selected Resource Selector or pair of Resource Selectors. TRCCNTCTLR.RLDEVENT.TYPE controls whether TRCCNTCTLR.RLDEVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## CNTEVENT\_TYPE, bit [7]

Selects an event, that when it occurs causes Counter to decrement.

Chooses the type of Resource Selector.

| CNTEVENT_TYPE   | Meaning                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Asingle Resource Selector. TRCCNTCTLR.CNTEVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                        |
| 0b1             | ABoolean-combined pair of Resource Selectors. TRCCNTCTLR.CNTEVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCCNTCTLR.CNTEVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## CNTEVENT\_SEL, bits [4:0]

Selects an event, that when it occurs causes Counter to decrement.

Defines the selected Resource Selector or pair of Resource Selectors. TRCCNTCTLR.CNTEVENT.TYPE controls whether TRCCNTCTLR.CNTEVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTCTLR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCNTCTLR&lt;m&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b01 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTCTLR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTCTLR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTCTLR[m];
```

MSR TRCCNTCTLR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b01 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTCTLR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTCTLR[m] = X[t, 64];
```
