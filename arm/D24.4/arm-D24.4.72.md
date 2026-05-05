## D24.4.72 TRCVMIDCCTLR1, Trace Virtual Context Identifier Comparator Control Register 1

The TRCVMIDCCTLR1 characteristics are:

## Purpose

Virtual Context Identifier Comparator mask values for the TRCVMIDCVR&lt;n&gt; registers, where n=4-7.

## Configuration

AArch64 System register TRCVMIDCCTLR1 bits [31:0] are architecturally mapped to External register TRCVMIDCCTLR1[31:0].

This register is present only when FEAT\_ETE is implemented, System register access to the trace unit registers is implemented, UInt(TRCIDR4.NUMVMIDC) &gt; 0x4 , and UInt(TRCIDR2.VMIDSIZE) &gt; 0. Otherwise, direct accesses to TRCVMIDCCTLR1 are UNDEFINED.

## Attributes

TRCVMIDCCTLR1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

COMP7[&lt;m&gt;] , bits [m+24], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 7:

TRCVMIDCVR7 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR7. Each bit in this field corresponds to a byte in TRCVMIDCVR7.

| COMP7[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR7[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR7[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP6[&lt;m&gt;] , bits [m+16], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 6:

TRCVMIDCVR6 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR6. Each bit in this field corresponds to a byte in TRCVMIDCVR6.

| COMP6[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR6[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR6[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP5[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 5:

TRCVMIDCVR5 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR5. Each bit in this field corresponds to a byte in TRCVMIDCVR5.

| COMP5[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR5[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR5[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP4[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 4:

TRCVMIDCVR4 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR4. Each bit in this field corresponds to a byte in TRCVMIDCVR4.

| COMP4[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR4[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR4[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCVMIDCCTLR1

If software uses the TRCVMIDCVR&lt;n&gt; registers, where n=4-7, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCVMIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCVMIDCVR&lt;n&gt; is not 0x00 , the behavior of the Virtual Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCVMIDCCTLR1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x4 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR1; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCVMIDCCTLR1;
```

MSR TRCVMIDCCTLR1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0011 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR) && UInt(TRCIDR4.NUMVMIDC) > 0x4 ↪ → && UInt(TRCIDR2.VMIDSIZE) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR1 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCVMIDCCTLR1 = X[t, 64];
```
