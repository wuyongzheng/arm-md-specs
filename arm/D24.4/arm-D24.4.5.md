## D24.4.5 TRBMPAM\_EL1, Trace Buffer MPAM Configuration Register

The TRBMPAM\_EL1 characteristics are:

## Purpose

Defines the PARTID, PMG, and MPAM\_SP values used by the trace buffer unit in external mode.

## Configuration

AArch64 System register TRBMPAM\_EL1 bits [63:0] are architecturally mapped to External register TRBMPAM\_EL1[63:0].

This register is present only when FEAT\_TRBE\_MPAM is implemented. Otherwise, direct accesses to TRBMPAM\_EL1 are UNDEFINED.

## Attributes

TRBMPAM\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:27]

Reserved, RES0.

## EN, bit [26]

Enable. Enables use of non-default MPAM values.

| EN   | Meaning                                 |
|------|-----------------------------------------|
| 0b0  | Use default MPAMvalues.                 |
| 0b1  | Use TRBMPAM_EL1.{PARTID, PMG, MPAM_SP}. |

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## MPAM\_SP, bits [25:24]

Partition Identifier space. Selects the PARTID space.

| MPAM_SP   | Meaning                                   | Applies when               |
|-----------|-------------------------------------------|----------------------------|
| 0b00      | PARTID is in the Secure PARTID space.     | FEAT_Secure is implemented |
| 0b01      | PARTID is in the Non-secure PARTID space. |                            |
| 0b10      | PARTID is in the Root PARTID space.       | FEAT_RME is implemented    |
| 0b11      | PARTID is in the Realm PARTID space.      | FEAT_RME is implemented    |

If the Trace Buffer Unit is using external mode and either TRBMPAM\_EL1.MPAM\_SP is set to reserved value, or the IMPLEMENTATION DEFINED authentication interface prohibits invasive debug of the Security state corresponding to the Partition Identifier space selected by TRBMPAM\_EL1.MPAM\_SP, then when the Trace Buffer Unit receives trace data from the trace unit, it does not write the trace data to memory and generates a trace buffer management event.

The interface prohibits invasive debug of the Security state if any of the following apply:

- ExternalInvasiveDebugEnabled() == FALSE.
- Secure state is implemented, ExternalSecureInvasiveDebugEnabled() == FALSE and TRBMPAM\_EL1.MPAM\_SP is 0b00 .
- FEAT\_RME is implemented, ExternalRootInvasiveDebugEnabled() == FALSE, and TRBMPAM\_EL1.MPAM\_SP is 0b10 .
- FEAT\_RME is implemented, ExternalRealmInvasiveDebugEnabled() == FALSE, and TRBMPAM\_EL1.MPAM\_SP is 0b11 .

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## PMG, bits [23:16]

Performance Monitoring Group. Selects the PMG.

Only sufficient low-order bits are required to represent the TRBDEVID1.PMG\_MAX. Higher-order bits are RES0.

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## PARTID, bits [15:0]

Partition Identifier. Selects the PARTID.

Only sufficient low-order bits are required to represent the TRBDEVID1.PARTID\_MAX. Higher-order bits are RES0.

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBMPAM\_EL1

The PE might ignore a write to TRBMPAM\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBMPAM\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b101 |

```
if !IsFeatureImplemented(FEAT_TRBE_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nTRBMPAM_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMPAM_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMPAM_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBMPAM_EL1;
```

MSR TRBMPAM\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b101 |

```
if !IsFeatureImplemented(FEAT_TRBE_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nTRBMPAM_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBMPAM_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnTB2 == '0' then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnTB2 == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBMPAM_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBMPAM_EL1 = X[t, 64];
```
