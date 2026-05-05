## D24.4.51 TRCOSLSR, Trace OS Lock Status Register

The TRCOSLSR characteristics are:

## Purpose

Returns the status of the Trace OS Lock.

## Configuration

AArch64 System register TRCOSLSR bits [31:0] are architecturally mapped to External register TRCOSLSR[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCOSLSR are UNDEFINED.

## Attributes

TRCOSLSR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:5]

Reserved, RES0.

## OSLM, bits [4:3, 0]

OS Lock model.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OSLM   | Meaning                                                                               |
|--------|---------------------------------------------------------------------------------------|
| 0b000  | Trace OS Lock is not implemented.                                                     |
| 0b010  | Trace OS Lock is implemented.                                                         |
| 0b100  | Trace OS Lock is not implemented, and the trace unit is controlled by the PE OS Lock. |

All other values are reserved.

When FEAT\_ETE is implemented, the values 0b000 and 0b010 are not permitted.

Access to this field is RO.

## Bit [2]

Reserved, RES0.

## OSLK, bit [1]

OS Lock status.

| OSLK   | Meaning                  |
|--------|--------------------------|
| 0b0    | The OS Lock is unlocked. |
| 0b1    | The OS Lock is locked.   |

When FEAT\_ETE is implemented, this field indicates the state of the PE OS Lock.

When FEAT\_ETMv4 is implemented, this field indicates the state of the Trace OS Lock.

## Accessing TRCOSLSR

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCOSLSR

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0001 | 0b0001 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCOSLSR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCOSLSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCOSLSR; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCOSLSR;
```
