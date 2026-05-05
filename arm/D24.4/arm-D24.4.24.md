## D24.4.24 TRCCNTVR&lt;n&gt;, Trace Counter Value Register &lt;n&gt;, n = 0 - 3

The TRCCNTVR&lt;n&gt; characteristics are:

## Purpose

This sets or returns the value of Counter &lt;n&gt;.

## Configuration

AArch64 System register TRCCNTVR&lt;n&gt; bits [31:0] are architecturally mapped to External register TRCCNTVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCNTVR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## VALUE, bits [15:0]

Contains the count value of Counter.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCNTVR&lt;m&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b10 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCCNTVRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCNTVR[m];
```

MSR TRCCNTVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-3

| op0   | op1   | CRn    | CRm          | op2   |
|-------|-------|--------|--------------|-------|
| 0b10  | 0b001 | 0b0000 | 0b10 :m[1:0] | 0b101 |

```
integer m = UInt(CRm<1:0>); if m >= NUM_TRACE_COUNTERS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCCNTVRn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCNTVR[m] = X[t, 64];
```
