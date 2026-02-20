## G8.2.85 ID\_DFR1, Debug Feature Register 1

The ID\_DFR1 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch32.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

AArch32 System register ID\_DFR1 bits [31:0] are architecturally mapped to AArch64 System register ID\_DFR1\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_DFR1 are UNDEFINED.

## Attributes

ID\_DFR1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7   | 4 3   |
|------|-------|-------|
| RES0 | HPMN0 | MTPMU |

## Bits [31:8]

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

## Accessing ID\_DFR1

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0011 | 0b101  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_DFR1) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_DFR1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_DFR1) || boolean IMPLEMENTATION_DEFINED ↪ → "ID_DFR1 trapped by HCR.TID3") && HCR.TID3 == '1' then AArch32.TakeHypTrapException(0x03); else R[t] = ID_DFR1; elsif PSTATE.EL == EL2 then R[t] = ID_DFR1;
```

```
elsif PSTATE.EL == EL3 then R[t] = ID_DFR1;
```