## D24.4.33 TRCIDR10, Trace ID Register 10

The TRCIDR10 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR10 bits [31:0] are architecturally mapped to External register TRCIDR10[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR10 are UNDEFINED.

## Attributes

TRCIDR10 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NUMP1KEY, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of P1 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR10

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR10

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0010 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR10; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR10; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR10;
```
