## D24.4.26 TRCDEVARCH, Trace Device Architecture Register

The TRCDEVARCH characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

AArch64 System register TRCDEVARCH bits [31:0] are architecturally mapped to External register TRCDEVARCH[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCDEVARCH are UNDEFINED.

## Attributes

TRCDEVARCHis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ARCHITECT, bits [31:21]

Defines the architect of the component. For Trace, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as 0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the TRCDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Revision. Defines the architecture revision of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

Access to this field is RO.

## ARCHVER,bits [15:12]

Architecture Version. Defines the architecture version of the component.

| ARCHVER   | Meaning   |
|-----------|-----------|
| 0b0101    | ETEv1.    |

ARCHVERand ARCHPART are also defined as a single field, ARCHID, so that ARCHVER is ARCHID[15:12]. This field reads as 0x5 .

Access to this field is RO.

## ARCHPART, bits [11:0]

Architecture Part. Defines the architecture of the component.

| ARCHPART   | Meaning                    |
|------------|----------------------------|
| 0xA13      | Arm PE trace architecture. |

ARCHVERand ARCHPART are also defined as a single field, ARCHID, so that ARCHPART is ARCHID[11:0]. This field reads as 0xA13 .

Access to this field is RO.

## Accessing TRCDEVARCH

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCDEVARCH

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0111 | 0b1111 | 0b110 |

| REVISION   | Meaning                |
|------------|------------------------|
| 0b0000     | ETEv1.0, FEAT_ETE.     |
| 0b0001     | ETEv1.1, FEAT_ETEv1p1. |
| 0b0010     | ETEv1.2, FEAT_ETEv1p2. |
| 0b0011     | ETEv1.3, FEAT_ETEv1p3. |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVARCH; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVARCH; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCDEVARCH;
```
