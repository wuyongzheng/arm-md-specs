## D24.4.71 TRCVMIDCCTLR0, Trace Virtual Context Identifier Comparator Control Register 0

The TRCVMIDCCTLR0 characteristics are:

## Purpose

Virtual Context Identifier Comparator mask values for the TRCVMIDCVR&lt;n&gt; registers, where n=0-3.

## Configuration

AArch64 System register TRCVMIDCCTLR0 bits [31:0] are architecturally mapped to External register TRCVMIDCCTLR0[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMVMIDC) &gt; 0x0 , and UInt(TRCIDR2.VMIDSIZE) &gt; 0. Otherwise, direct accesses to TRCVMIDCCTLR0 are UNDEFINED.

## Attributes

TRCVMIDCCTLR0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP3[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 3:

TRCVMIDCVR3 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR3. Each bit in this field corresponds to a byte in TRCVMIDCVR3.

| COMP3[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR3[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR3[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP2[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 2:

TRCVMIDCVR2 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR2. Each bit in this field corresponds to a byte in TRCVMIDCVR2.

| COMP2[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR2[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR2[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP1[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 1:

TRCVMIDCVR1 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR1. Each bit in this field corresponds to a byte in TRCVMIDCVR1.

| COMP1[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR1[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR1[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP0[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 0:

TRCVMIDCVR0 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR0. Each bit in this field corresponds to a byte in TRCVMIDCVR0.

| COMP0[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR0[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR0[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCVMIDCCTLR0

If software uses the TRCVMIDCVR&lt;n&gt; registers, where n=0-3, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCVMIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCVMIDCVR&lt;n&gt; is not 0x00 , the behavior of the Virtual Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVMIDCCTLR0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x0 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR0;
```

MSR TRCVMIDCCTLR0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0010 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x0 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR0 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR0 = X[t, 64];
```
