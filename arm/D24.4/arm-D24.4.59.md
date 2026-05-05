## D24.4.59 TRCSSCCR&lt;n&gt;, Trace Single-shot Comparator Control Register &lt;n&gt;, n = 0 - 7

The TRCSSCCR&lt;n&gt; characteristics are:

## Purpose

Controls the corresponding Single-shot Comparator Control resource.

## Configuration

AArch64 System register TRCSSCCR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCSSCCR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMSSCC) &gt; n. Otherwise, direct accesses to TRCSSCCR&lt;n&gt; are UNDEFINED.

## Attributes

TRCSSCCR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:25]

Reserved, RES0.

## RST, bit [24]

Selects the Single-shot Comparator Control mode.

| RST   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | The Single-shot Comparator Control is in single-shot mode. |
| 0b1   | The Single-shot Comparator Control is in multi-shot mode.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## ARC[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Selects one or more Address Range Comparators for Single-shot control.

| ARC[<m>]   | Meaning                                                                    |
|------------|----------------------------------------------------------------------------|
| 0b0        | The Address Range Comparator <m>, is not selected for Single-shot control. |
| 0b1        | The Address Range Comparator <m>, is selected for Single-shot control.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## SAC[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects one or more Single Address Comparators for Single-shot control.

| SAC[<m>]   | Meaning                                                                     |
|------------|-----------------------------------------------------------------------------|
| 0b0        | The Single Address Comparator <m>, is not selected for Single-shot control. |
| 0b1        | The Single Address Comparator <m>, is selected for Single-shot control.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCSSCCR&lt;n&gt;

Must be programmed if any TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCSSCCR&lt;m&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCCR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCCR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCSSCCR[m];
```

MSR TRCSSCCR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0 :m[2:0] | 0b010 |

```
integer m = UInt(CRm<2:0>); if m >= NUM_TRACE_SINGLE_SHOT_COMPARATOR_CONTROLS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCCR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCCR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCSSCCR[m] = X[t, 64];
```
