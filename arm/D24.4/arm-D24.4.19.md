## D24.4.19 TRCCIDCVR&lt;n&gt;, Trace Context Identifier Comparator Value Registers &lt;n&gt;, n = 0 - 7

The TRCCIDCVR&lt;n&gt; characteristics are:

## Purpose

Contains a Context identifier value.

## Configuration

AArch64 System register TRCCIDCVR&lt;n&gt; bits [63:0] are architecturally mapped to External register TRCCIDCVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, and UInt(TRCIDR4.NUMCIDC) &gt; n. Otherwise, direct accesses to TRCCIDCVR&lt;n&gt; are UNDEFINED.

## Attributes

TRCCIDCVR&lt;n&gt; is a 64-bit register.

## Field descriptions

VALUE

63

32

VALUE

31

0

<!-- image -->

## VALUE, bits [63:0]

Context identifier value. The width of this field is indicated by TRCIDR2.CIDSIZE. Unimplemented bits are RES0. After a PE Reset, the trace unit assumes that the Context identifier is zero until the PE updates the Context identifier.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCIDCVR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCRSCTLR&lt;a&gt;.GROUP == 0b0110 and TRCRSCTLR&lt;a&gt;.CID[n] == 1. · TRCACATR&lt;a&gt;.CONTEXTTYPE == 0b01 or 0b11 and TRCACATR&lt;a&gt;.CONTEXT == n.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, TRCCIDCVR<m> ; Where m = 0-7
```

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0011 | m[2:0]: 0b0 | 0b000 |

```
integer m = UInt(CRm<3:1>); if m >= NUM_TRACE_CONTEXT_IDENTIFIER_COMPARATORS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCVR[m]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCVR[m];
```

MSR TRCCIDCVR&lt;m&gt;, &lt;Xt&gt; ; Where m = 0-7

| op0   | op1   | CRn    | CRm         | op2   |
|-------|-------|--------|-------------|-------|
| 0b10  | 0b001 | 0b0011 | m[2:0]: 0b0 | 0b000 |

```
integer m = UInt(CRm<3:1>); if m >= NUM_TRACE_CONTEXT_IDENTIFIER_COMPARATORS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCVR[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCVR[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCVR[m] = X[t, 64];
```
