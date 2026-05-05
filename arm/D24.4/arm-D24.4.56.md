## D24.4.56 TRCSEQEVR&lt;n&gt;, Trace Sequencer State Transition Control Register &lt;n&gt;, n = 0 - 2

The TRCSEQEVR&lt;n&gt; characteristics are:

## Purpose

Moves the Sequencer state:

- Backwards, from state n+1 to state n when a programmed resource event occurs.
- Forwards, from state n to state n+1 when a programmed resource event occurs.

## Configuration

AArch64 System register TRCSEQEVR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSEQEVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQEVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSEQEVR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## B\_TYPE, bit [15]

Backward field. Selects an event that causes the Sequencer to move from state n+1 to state n. For example, if TRCSEQEVR2.B.SEL == 0x14 , then when event 0x14 occurs, the Sequencer moves from state 3 to state 2.

Chooses the type of Resource Selector.

| B_TYPE   | Meaning                                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Asingle Resource Selector. TRCSEQEVR.B.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                |
| 0b1      | ABoolean-combined pair of Resource Selectors. TRCSEQEVR.B.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQEVR.B.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [14:13]

Reserved, RES0.

## B\_SEL, bits [12:8]

Backward field. Selects an event that causes the Sequencer to move from state n+1 to state n. For example, if TRCSEQEVR2.B.SEL == 0x14 , then when event 0x14 occurs, the Sequencer moves from state 3 to state 2.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQEVR.B.TYPE controls whether TRCSEQEVR.B.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## F\_TYPE, bit [7]

Forward field. Selects an event that causes the Sequencer to move from state n to state n+1. For example, if TRCSEQEVR1.F.SEL == 0x12 , then when event 0x12 occurs, the Sequencer moves from state 1 to state 2.

Chooses the type of Resource Selector.

| F_TYPE   | Meaning                                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Asingle Resource Selector. TRCSEQEVR.F.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                |
| 0b1      | ABoolean-combined pair of Resource Selectors. TRCSEQEVR.F.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQEVR.F.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## F\_SEL, bits [4:0]

Forward field. Selects an event that causes the Sequencer to move from state n to state n+1. For example, if TRCSEQEVR1.F.SEL == 0x12 , then when event 0x12 occurs, the Sequencer moves from state 1 to state 2.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQEVR.F.TYPE controls whether TRCSEQEVR.F.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQEVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCSEQEVR<m> ; Where m = 0-2
```

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b00 :m[1:0] | 0b100 |

```
integer m = UInt(CRm<1:0>); if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQEVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQEVR[m];
```

```
elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSEQEVR[m];
```

MSR TRCSEQEVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-2

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b00 :m[1:0] | 0b100 |

```
integer m = UInt(CRm<1:0>); if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQEVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSEQEVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else
```
