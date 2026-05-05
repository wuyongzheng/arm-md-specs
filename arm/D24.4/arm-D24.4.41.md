## D24.4.41 TRCIDR6, Trace ID Register 6

The TRCIDR6 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR6 bits [31:0] are architecturally mapped to External register TRCIDR6[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR6 are UNDEFINED.

## Attributes

TRCIDR6 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:3]

Reserved, RES0.

## EXLEVEL\_RL\_EL2, bit [2]

Indicates if Realm EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_RL_EL2   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL2 is not implemented. |
| 0b1              | Realm EL2 is implemented.     |

Access to this field is RO.

## EXLEVEL\_RL\_EL1, bit [1]

Indicates if Realm EL1 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## EXLEVEL\_RL\_EL0, bit [0]

Indicates if Realm EL0 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_RL_EL0   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL0 is not implemented. |
| 0b1              | Realm EL0 is implemented.     |

Access to this field is RO.

## Accessing TRCIDR6

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR6

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1110 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR6; elsif PSTATE.EL == EL2 then
```

| EXLEVEL_RL_EL1   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL1 is not implemented. |
| 0b1              | Realm EL1 is implemented.     |

```
if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR6; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR6;
```
