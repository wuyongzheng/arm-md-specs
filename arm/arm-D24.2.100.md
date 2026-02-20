## D24.2.100 ID\_DFR1\_EL1, AArch32 Debug Feature Register 1

The ID\_DFR1\_EL1 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch32.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

AArch64 System register ID\_DFR1\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_DFR1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_DFR1\_EL1 are UNDEFINED.

## Attributes

ID\_DFR1\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## HPMN0, bits [7:4]

Zero PMU event counters for a Guest operating system.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HPMN0   | Meaning                                                           |
|---------|-------------------------------------------------------------------|
| 0b0000  | Setting HDCR.HPMN to zero has CONSTRAINED UNPREDICTABLE behavior. |
| 0b0001  | Setting HDCR.HPMN to zero has defined behavior.                   |

All other values are reserved.

If FEAT\_PMUv3 is not implemented, FEAT\_FGT is not implemented, or EL2 is not implemented, the only permitted value is 0b0000 .

FEAT\_HPMN0 implements the functionality identified by the value 0b0001 .

From Armv8.8, in an implementation that includes FEAT\_PMUv3, FEAT\_FGT, and EL2, the value 0b0000 is not permitted.

Access to this field is RO.

## MTPMU,bits [3:0]

Multi-threaded PMU extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MTPMU   | Meaning                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | FEAT_MTPMU not implemented. If FEAT_PMUv3 is implemented, it is IMPLEMENTATION DEFINED whether PMEVTYPER<n>.MT are read/write or RES0.             |
| 0b0001  | FEAT_MTPMU and FEAT_PMUv3 implemented. PMEVTYPER<n>.MT are read/write. When FEAT_MTPMU is disabled, the Effective values of PMEVTYPER<n>.MT are 0. |
| 0b1111  | FEAT_MTPMU not implemented. If FEAT_PMUv3 is implemented, PMEVTYPER<n>.MT are RES0.                                                                |

All other values are reserved.

FEAT\_MTPMU implements the functionality identified by the value 0b0001 .

From Armv8.6, in an implementation that includes FEAT\_PMUv3, the value 0b0000 is not permitted.

In an implementation that does not include FEAT\_PMUv3, the value 0b0001 is not permitted.

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_DFR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0011 | 0b101 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_DFR1_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_DFR1_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_DFR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_DFR1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_DFR1_EL1;
```