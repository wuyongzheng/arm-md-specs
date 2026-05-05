## D24.4.17 TRCCIDCCTLR0, Trace Context Identifier Comparator Control Register 0

The TRCCIDCCTLR0 characteristics are:

## Purpose

Contains Context identifier mask values for the TRCCIDCVR&lt;n&gt; registers, for n = 0 to 3.

## Configuration

AArch64 System register TRCCIDCCTLR0 bits [31:0] are architecturally mapped to External register TRCCIDCCTLR0[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMCIDC) &gt; 0x0 , and UInt(TRCIDR2.CIDSIZE) &gt; 0. Otherwise, direct accesses to TRCCIDCCTLR0 are UNDEFINED.

## Attributes

TRCCIDCCTLR0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP3[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 3:

TRCCIDCVR3 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR3. Each bit in this field corresponds to a byte in TRCCIDCVR3.

| COMP3[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR3[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR3[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP2[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMCIDC) &gt; 2:

TRCCIDCVR2 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR2. Each bit in this field corresponds to a byte in TRCCIDCVR2.

| COMP2[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR2[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR2[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP1[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 1:

TRCCIDCVR1 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR1. Each bit in this field corresponds to a byte in TRCCIDCVR1.

| COMP1[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR1[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR1[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP0[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 0:

TRCCIDCVR0 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR0. Each bit in this field corresponds to a byte in TRCCIDCVR0.

| COMP0[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR0[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR0[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCCIDCCTLR0

If software uses the TRCCIDCVR&lt;n&gt; registers, for n = 0 to 3, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCCIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCCIDCVR&lt;n&gt; is not 0x00 , the behavior of the Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCCIDCCTLR0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMCIDC) > 0x0 ↪ → && UInt(TRCIDR2.CIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCCIDCCTLR0;
```

MSR TRCCIDCCTLR0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMCIDC) > 0x0 ↪ → && UInt(TRCIDR2.CIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCCIDCCTLR0 = X[t, 64];
```
