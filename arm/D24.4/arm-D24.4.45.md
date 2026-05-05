## D24.4.45 TRCIMSPEC0, Trace IMP DEF Register 0

The TRCIMSPEC0 characteristics are:

## Purpose

TRCIMSPEC0 shows the presence of any IMPLEMENTATION DEFINED features, and provides an interface to enable the features that are provided.

## Configuration

AArch64 System register TRCIMSPEC0 bits [31:0] are architecturally mapped to External register TRCIMSPEC0[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIMSPEC0 are UNDEFINED.

## Attributes

TRCIMSPEC0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## EN, bits [7:4]

## When TRCIMSPEC0.SUPPORT != '0000':

Enable. Controls whether the IMPLEMENTATION DEFINED features are enabled.

| EN     | Meaning                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | The IMPLEMENTATION DEFINED features are not enabled. The trace unit must behave as if the IMPLEMENTATION DEFINED features are not supported. |
| 0b0001 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0010 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0011 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0100 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0101 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0110 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b0111 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b1000 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b1001 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |

| EN     | Meaning                                            |
|--------|----------------------------------------------------|
| 0b1010 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1011 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1100 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1101 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1110 | The trace unit behavior is IMPLEMENTATION DEFINED. |
| 0b1111 | The trace unit behavior is IMPLEMENTATION DEFINED. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0000' .

## Otherwise:

Reserved, RES0.

## SUPPORT, bits [3:0]

Indicates whether the implementation supports IMPLEMENTATION DEFINED features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SUPPORT   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0000    | No IMPLEMENTATION DEFINED features are supported. |
| 0b0001    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0010    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0011    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0100    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0101    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0110    | IMPLEMENTATION DEFINED features are supported.    |
| 0b0111    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1000    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1001    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1010    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1011    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1100    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1101    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1110    | IMPLEMENTATION DEFINED features are supported.    |
| 0b1111    | IMPLEMENTATION DEFINED features are supported.    |

Use of nonzero values requires written permission from Arm.

Access to this field is RO.

## Accessing TRCIMSPEC0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIMSPEC0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCIMSPECn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC0; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIMSPEC0;
```

MSR TRCIMSPEC0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b0000 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRCIMSPECn == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC0 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC0 = X[t, 64]; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRCIMSPEC0 = X[t, 64];
```
