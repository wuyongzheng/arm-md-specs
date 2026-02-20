## D24.12 MPAM registers

This section lists the MPAM registers in AArch64.

## D24.12.1 MPAM0\_EL1, MPAM0 Register (EL1)

The MPAM0\_EL1 characteristics are:

## Purpose

Holds information to generate MPAM labels for memory requests when executing at EL0.

## Configuration

If FEAT\_MPAM is implemented, EL2 is implemented and enabled in the current Security state, and the MPAM virtualization option is present, then:

- If MPAMHCR\_EL2.GSTAPP\_PLK == 1 and HCR\_EL2.TGE == 0, MPAM1\_EL1 is used instead of MPAM0\_EL1 to generate MPAM information to label memory requests.
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1} and MPAMHCR\_EL2.EL0\_VPMEN == 1, then MPAM PARTIDs in MPAM0\_EL1 are virtual and mapped into physical PARTIDs for the current Security state.

This register is present only when FEAT\_MPAM is implemented. Otherwise, direct accesses to MPAM0\_EL1 are UNDEFINED.

## Attributes

MPAM0\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## PMG\_D, bits [47:40]

Performance monitoring group property for PARTID\_D.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PMG\_I, bits [39:32]

Performance monitoring group property for PARTID\_I.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_D, bits [31:16]

Partition ID for data accesses, including load and store accesses, made from EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_I, bits [15:0]

Partition ID for instruction accesses made from EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAM0\_EL1

None of the fields in this register are permitted to be cached in a TLB.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAM0\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.TRAPMPAM0EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = MPAM0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAM0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAM0_EL1;
```

MSR MPAM0\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.TRAPMPAM0EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else MPAM0_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAM0_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAM0_EL1 = X[t, 64];
```

## D24.12.2 MPAM1\_EL1, MPAM1 Register (EL1)

The MPAM1\_EL1 characteristics are:

## Purpose

Holds information to generate MPAM labels for memory requests when executing at EL1.

## Configuration

If FEAT\_MPAMv1p0 or FEAT\_MPAMv0p1 is implemented, EL2 is implemented and enabled in the current Security state, and the MPAM virtualization option is present, then:

- If MPAMHCR\_EL2.GSTAPP\_PLK == 1 and HCR\_EL2.TGE == 0, MPAM1\_EL1 is used instead of MPAM0\_EL1 to generate MPAM labels for memory requests when executing at EL0.
- If MPAMHCR\_EL2.EL1\_VPMEN == 1, MPAM PARTIDs in MPAM1\_EL1 are virtual and mapped into physical PARTIDs for the current Security state. This mapping of MPAM1\_EL1 virtual PARTIDs to physical PARTIDs when EL1\_VPMEN is 1 also applies when MPAM1\_EL1 is used at EL0 due to MPAMHCR\_EL2.GSTAPP\_PLK.

When (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented) and EL3 is implemented, AArch64 System register MPAM1\_EL1 bit [63] is architecturally mapped to AArch64 System register MPAM3\_EL3[63].

When ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (!HaveEL(EL3))) &amp;&amp; HaveEL(EL2), AArch64 System register MPAM1\_EL1 bit [63] is architecturally mapped to AArch64 System register MPAM2\_EL2[63].

This register is present only when FEAT\_MPAM is implemented. Otherwise, direct accesses to MPAM1\_EL1 are UNDEFINED.

## Attributes

MPAM1\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## MPAMEN,bit [63]

MPAMEnable. MPAM is enabled when MPAMEN == 1. When disabled, all PARTIDs and PMGs are output as their default value in the corresponding ID space.

| MPAMEN   | Meaning                                                                                            |
|----------|----------------------------------------------------------------------------------------------------|
| 0b0      | The default PARTID and default PMGare output in MPAMinformation.                                   |
| 0b1      | MPAMinformation is output based on the MPAMn_ELx register for ELn according the MPAMconfiguration. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- MPAM3\_EL3.MPAMEN == '0'
- Access to this field is RAO/WI if all of the following are true:
- EL3 is implemented
- MPAM3\_EL3.MPAMEN == '1'
- Access to this field is RAZ/WI if all of the following are true:
- EL3 is not implemented
- EL2 is implemented
- MPAM2\_EL2.MPAMEN == '0'
- Access to this field is RAO/WI if all of the following are true:
- EL3 is not implemented
- EL2 is implemented
- MPAM2\_EL2.MPAMEN == '1'

## Bits [62:61]

Reserved, RES0.

## FORCED\_NS, bit [60]

## When FEAT\_MPAMv0p1 is implemented:

In the Secure state, FORCED\_NS indicates the state of MPAM3\_EL3.FORCE\_NS.

| FORCED_NS   | Meaning                                                                                                  |
|-------------|----------------------------------------------------------------------------------------------------------|
| 0b0         | In the Non-secure state, always reads as 0. In the Secure state, indicates that MPAM3_EL3.FORCE_NS == 0. |
| 0b1         | In the Secure state, indicates that MPAM3_EL3.FORCE_NS == 1.                                             |

Always reads as 0 in the Non-secure state.

Writes are ignored.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Bits [59:55]

Reserved, RES0.

## ALTSP\_FRCD, bit [54]

When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Alternative PARTID forced for PARTIDs in this register.

| ALTSP_FRCD   | Meaning                                                                        |
|--------------|--------------------------------------------------------------------------------|
| 0b0          | The PARTIDs in MPAM1_EL1 and MPAM0_EL1 are using the primary PARTID space.     |
| 0b1          | The PARTIDs in MPAM1_EL1 and MPAM0_EL1 are using the alternative PARTID space. |

This bit indicates that a higher Exception level has forced the PARTIDs in this register to use the alternative PARTID space defined for the current Security state.

In MPAM1\_EL1, it also indicates that MPAM0\_EL1 is forced to use alternative PARTID space.

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

Accessing this field has the following behavior:

- When !UsePrimarySpaceEL10(), access to this field is RAO/WI.
- Otherwise, access to this field is RAZ/WI.

## Otherwise:

Reserved, RES0.

## Bits [53:48]

Reserved, RES0.

## PMG\_D, bits [47:40]

Performance monitoring group property for PARTID\_D.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PMG\_I, bits [39:32]

Performance monitoring group property for PARTID\_I.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_D, bits [31:16]

Partition ID for data accesses, including load and store accesses, made from EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_I, bits [15:0]

Partition ID for instruction accesses made from EL1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAM1\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name MPAM1\_EL1 or MPAM1\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

None of the fields in this register are permitted to be cached in a TLB.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAM1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.TRAPMPAM1EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x900]; else X[t, 64] = MPAM1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = MPAM2_EL2; else X[t, 64] = MPAM1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAM1_EL1;
```

MSR MPAM1\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.TRAPMPAM1EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x900] = X[t, 64]; else MPAM1_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then MPAM2_EL2 = X[t, 64]; else MPAM1_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAM1_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, MPAM1\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x900]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAM1_EL1; else
```

```
UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = MPAM1_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR MPAM1\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x900] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAM1_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then MPAM1_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.12.3 MPAM2\_EL2, MPAM2 Register (EL2)

The MPAM2\_EL2 characteristics are:

## Purpose

Holds information to generate MPAM labels for memory requests when executing at EL2.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

When (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented) and EL3 is implemented, AArch64 System register MPAM2\_EL2 bit [63] is architecturally mapped to AArch64 System register MPAM3\_EL3[63].

When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented, AArch64 System register MPAM2\_EL2 bit [63] is architecturally mapped to AArch64 System register MPAM1\_EL1[63].

This register is present only when FEAT\_MPAM is implemented. Otherwise, direct accesses to MPAM2\_EL2 are UNDEFINED.

## Attributes

MPAM2\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## MPAMEN,bit [63]

MPAMEnable. MPAM is enabled when MPAMEN == 1. When disabled, all PARTIDs and PMGs are output as their default value in the corresponding ID space.

| MPAMEN   | Meaning                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------|
| 0b0      | The default PARTID and default PMGare output in MPAMinformation from all Exception levels.            |
| 0b1      | MPAMinformation is output based on the MPAMn_ELx register for ELn according to the MPAMconfiguration. |

If EL3 is implemented, this field is read-only and reads the current value of the read/write MPAM3\_EL3.MPAMEN bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- EL3 is implemented
- MPAM3\_EL3.MPAMEN == '0'
- Access to this field is RAO/WI if all of the following are true:
- EL3 is implemented
- MPAM3\_EL3.MPAMEN == '1'
- When EL3 is not implemented, access to this field is RW.

## Bits [62:59]

Reserved, RES0.

## TIDR, bit [58]

## When (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p1 is implemented) and MPAMIDR\_EL1.HAS\_TIDR == '1':

TIDR traps accesses to MPAMIDR\_EL1 from EL1 to EL2.

| TIDR   | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped. |
| 0b1    | Trap accesses to MPAMIDR_EL1 from EL1 to EL2.               |

MPAMHCR\_EL2.TRAP\_MPAMIDR\_EL1 == 1 also traps MPAMIDR\_EL1 accesses from EL1 to EL2. If either TIDR or TRAP\_MPAMIDR\_EL1 are 1, accesses are trapped.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [57]

Reserved, RES0.

## ALTSP\_HFC, bit [56]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Hierarchical force of alternative PARTID space controls. When MPAM3\_EL3.ALTSP\_HEN is 0, ALTSP controls in MPAM2\_EL2 have no effect. When MPAM3\_EL3.ALTSP\_HEN is 1, this bit selects whether the PARTIDs in MPAM1\_EL1 and MPAM0\_EL1 are in the primary (0) or alternative (1) PARTID space for the security state.

| ALTSP_HFC   | Meaning                                                                                                                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | When MPAM3_EL3.ALTSP_HEN is 1, the PARTID space of MPAM1_EL1.PARTID_I, MPAM1_EL1.PARTID_D, MPAM0_EL1.PARTID_I, and MPAM0_EL1.PARTID_D are in the primary PARTID space for the Security state. |

| ALTSP_HFC   | Meaning                                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1         | When MPAM3_EL3.ALTSP_HEN is 1, the PARTID space of MPAM1_EL1.PARTID_I, MPAM1_EL1.PARTID_D, MPAM0_EL1.PARTID_I, and MPAM0_EL1.PARTID_D are in the alternative PARTID space for the Security state. |

This control has no effect when MPAM3\_EL3.ALTSP\_HEN is 0.

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ALTSP\_EL2, bit [55]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Select alternative PARTID space for PARTIDs in MPAM2\_EL2 when MPAM3\_EL3.ALTSP\_HEN is 1.

| ALTSP_EL2   | Meaning                                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0         | When MPAM3_EL3.ALTSP_HEN is 1, selects the primary PARTID space for MPAM2_EL2.PARTID_I and MPAM2_EL2.PARTID_D.     |
| 0b1         | When MPAM3_EL3.ALTSP_HEN is 1, selects the alternative PARTID space for MPAM2_EL2.PARTID_I and MPAM2_EL2.PARTID_D. |

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ALTSP\_FRCD, bit [54]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Alternative PARTID forced for PARTIDs in this register.

| ALTSP_FRCD   | Meaning                                                              |
|--------------|----------------------------------------------------------------------|
| 0b0          | The PARTIDs in this register are using the primary PARTID space.     |
| 0b1          | The PARTIDs in this register are using the alternative PARTID space. |

This bit indicates that a higher Exception level has forced the PARTIDs in this register to use the alternative PARTID space defined for the current Security state. In EL2, it is also 1 when MPAM2\_EL2.ALTSP\_EL2 is 1.

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When !UsePrimarySpaceEL2(), access to this field is RAO/WI.
- Otherwise, access to this field is RAZ/WI.

## Otherwise:

Reserved, RES0.

## Bits [53:51]

Reserved, RES0.

## EnMPAMSM,bit [50]

## When FEAT\_SME is implemented:

Traps execution at EL1 of instructions that directly access the MPAMSM\_EL1 register to EL2. The exception is reported using ESR\_ELx.EC syndrome value 0x18 .

| EnMPAMSM   | Meaning                                                                   |
|------------|---------------------------------------------------------------------------|
| 0b0        | This control causes execution of these instructions at EL1 to be trapped. |
| 0b1        | This control does not cause execution of any instructions to be trapped.  |

This field has no effect on accesses to MPAMSM\_EL1 from EL2 or EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRAPMPAM0EL1, bit [49]

Trap accesses from EL1 to the MPAM0\_EL1 register trap to EL2.

| TRAPMPAM0EL1   | Meaning                                            |
|----------------|----------------------------------------------------|
| 0b0            | Accesses to MPAM0_EL1 from EL1 are not trapped.    |
| 0b1            | Accesses to MPAM0_EL1 from EL1 are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When EL3 is not implemented, this field resets to '1' .
- When EL3 is implemented, this field resets to an architecturally UNKNOWN value.

## TRAPMPAM1EL1, bit [48]

Trap accesses from EL1 to the MPAM1\_EL1 register trap to EL2.

| TRAPMPAM1EL1   | Meaning                                            |
|----------------|----------------------------------------------------|
| 0b0            | Accesses to MPAM1_EL1 from EL1 are not trapped.    |
| 0b1            | Accesses to MPAM1_EL1 from EL1 are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When EL3 is not implemented, this field resets to '1' .
- When EL3 is implemented, this field resets to an architecturally UNKNOWN value.

## PMG\_D, bits [47:40]

Performance monitoring group for data accesses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PMG\_I, bits [39:32]

Performance monitoring group for instruction accesses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_D, bits [31:16]

Partition ID for data accesses, including load and store accesses, made from EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_I, bits [15:0]

Partition ID for instruction accesses made from EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAM2\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name MPAM2\_EL2 or MPAM1\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

None of the fields in this register are permitted to be cached in a TLB.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAM2\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAM2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAM2_EL2;
```

MSR MPAM2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then
```

AArch64.SystemAccessTrap(EL3, 0x18);

```
UNDEFINED; else else MPAM2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAM2_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, MPAM1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.TRAPMPAM1EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x900]; else X[t, 64] = MPAM1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = MPAM2_EL2; else X[t, 64] = MPAM1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAM1_EL1;
```

MSR MPAM1\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.TRAPMPAM1EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x900] = X[t, 64]; else MPAM1_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then MPAM2_EL2 = X[t, 64]; else MPAM1_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAM1_EL1 = X[t, 64];
```

## D24.12.4 MPAM3\_EL3, MPAM3 Register (EL3)

The MPAM3\_EL3 characteristics are:

## Purpose

Holds information to generate MPAM labels for memory requests when executing at EL3.

## Configuration

When (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented) and EL2 is implemented, AArch64 System register MPAM3\_EL3 bit [63] is architecturally mapped to AArch64 System register MPAM2\_EL2[63].

When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented, AArch64 System register MPAM3\_EL3 bit [63] is architecturally mapped to AArch64 System register MPAM1\_EL1[63].

This register is present only when FEAT\_MPAM is implemented. Otherwise, direct accesses to MPAM3\_EL3 are UNDEFINED.

## Attributes

MPAM3\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## MPAMEN,bit [63]

MPAMEnable. MPAM is enabled when MPAMEN == 1. When disabled, all PARTIDs and PMGs are output as their default value in the corresponding ID space.

Values of this field are:

| MPAMEN   | Meaning                                                                                            |
|----------|----------------------------------------------------------------------------------------------------|
| 0b0      | The default PARTID and default PMGare output in MPAMinformation when executing at any ELn.         |
| 0b1      | MPAMinformation is output based on the MPAMn_ELx register for ELn according the MPAMconfiguration. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is RW.

## TRAPLOWER,bit [62]

Trap direct accesses to MPAM System registers that are not UNDEFINED from all ELn lower than EL3.

| TRAPLOWER   | Meaning                                                                  |
|-------------|--------------------------------------------------------------------------|
| 0b0         | Do not force trapping of direct accesses of MPAMSystem registers to EL3. |
| 0b1         | Force direct accesses of MPAMSystem registers to trap to EL3.            |

Note

This trap is higher priority than any of the traps controlled by MPAM \_EL2 registers.

The reset behavior of this field is:

· On a Warm reset, this field resets to '1' .

## SDEFLT, bit [61]

## When (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p1 is implemented) and MPAMIDR\_EL1.HAS\_SDEFLT == '1':

SDEFLT overrides the PARTID and PMG with the default PARTID and default PMG when executing in the Secure state.

| SDEFLT   | Meaning                                                                                       |
|----------|-----------------------------------------------------------------------------------------------|
| 0b0      | The PARTID and PMGare determined normally in the Secure state.                                |
| 0b1      | When executing in the Secure state, the PARTID is always PARTID 0, and the PMGis always PMG0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

FORCE\_NS, bit [60]

## When FEAT\_MPAMv0p1 is implemented and MPAMIDR\_EL1.HAS\_FORCE\_NS == '1':

FORCE\_NS forces MPAM\_NS to always be 1 in the Secure state.

| FORCE_NS   | Meaning                                         |
|------------|-------------------------------------------------|
| 0b0        | MPAM_NSis 0 when executing in the Secure state. |
| 0b1        | MPAM_NSis 1 when executing in the Secure state. |

An implementation is permitted to have this field as RAO if the implementation does not support generating MPAM\_NSas 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [59:58]

Reserved, RES0.

## ALTSP\_HEN, bit [57]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Hierarchical enable for alternative PARTID space controls. Alternative PARTID space controls in MPAM2\_EL2 have no effect when this field is zero.

| ALTSP_HEN   | Meaning                                                                                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Disable alternative PARTID space controls in MPAM2_EL2. The PARTID space for PARTIDs in MPAM2_EL2, MPAM1_EL1, and MPAM0_EL1 is selected by MPAM3_EL3.ALTSP_HFC. |
| 0b1         | Enable alternative PARTID space controls in MPAM2_EL2 to control the PARTID space used for PARTIDs in MPAM2_EL2, MPAM1_EL1, and MPAM0_EL1.                      |

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ALTSP\_HFC, bit [56]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Hierarchical force of alternative PARTID space controls. When MPAM3\_EL3.ALTSP\_HEN is 0, the PARTID space for PARTIDs in MPAM2\_EL2, MPAM1\_EL1, and MPAM0\_EL1 is selected by the value of this bit.

| ALTSP_HFC   | Meaning                                                                                                                                                                |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | When MPAM3_EL3.ALTSP_HEN is 0, the PARTID space of MPAM2_EL2.PARTID, MPAM1_EL1.PARTID and MPAM0_EL1.PARTID are the primary PARTID space for the security state.        |
| 0b1         | When MPAM3_EL3.ALTSP_HEN is 0, the PARTID space of MPAM2_EL2.PARTID and MPAM1_EL1.PARTID and MPAM0_EL1.PARTID are the alternative PARTID space for the security state. |

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ALTSP\_EL3, bit [55]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Select alternative PARTID space for PARTIDs in MPAM3\_EL3.

| ALTSP_EL3   | Meaning                                                                            |
|-------------|------------------------------------------------------------------------------------|
| 0b0         | Selects the primary PARTID space of MPAM3_EL3.PARTID_I and MPAM3_EL3.PARTID_D.     |
| 0b1         | Selects the alternative PARTID space of MPAM3_EL3.PARTID_I and MPAM3_EL3.PARTID_D. |

For more information, see In a PE with FEAT\_RME, selection of primary or alternative PARTID space.

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Otherwise:

Reserved, RES0.

## Bits [54:53]

Reserved, RES0.

## RT\_ALTSP\_NS, bit [52]

## When FEAT\_RME is implemented and MPAMIDR\_EL1.HAS\_ALTSP == '1':

Selects whether the alternative PARTID space for the Root security state is the Secure PARTID space or the Non-secure PARTID space. MPAM3\_EL3.RT\_ALTSP\_NS selects the alternative PARTID space for the Root Security state when MPAM3\_EL3.ALTSP\_EL3 == 1.

| RT_ALTSP_NS   | Meaning                                                                                 |
|---------------|-----------------------------------------------------------------------------------------|
| 0b0           | The alternative PARTID space in the Root security state is the Secure PARTID space.     |
| 0b1           | The alternative PARTID space in the Root security state is the Non-secure PARTID space. |

This field has no effect except in the Root security state (EL3).

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Otherwise:

Reserved, RES0.

## Bits [51:48]

Reserved, RES0.

## PMG\_D, bits [47:40]

Performance monitoring group for data accesses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PMG\_I, bits [39:32]

Performance monitoring group for instruction accesses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_D, bits [31:16]

Partition ID for data accesses, including load and store accesses, made from EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PARTID\_I, bits [15:0]

Partition ID for instruction accesses made from EL3.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAM3\_EL3

None of the fields in this register are permitted to be cached in a TLB.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = MPAM3_EL3;
```

MSR MPAM3\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.MPAM3_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else MPAM3_EL3 = X[t, 64];
```

## D24.12.5 MPAMBW0\_EL1, MPAM PE-side Maximum-bandwidth Control Register (EL0)

The MPAMBW0\_EL1 characteristics are:

## Purpose

Enables software to configure a maximum fraction of memory bandwidth that the PE is permitted to use when executing at EL0 with its current PARTID.

## Configuration

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented. Otherwise, direct accesses to MPAMBW0\_EL1are UNDEFINED.

## Attributes

MPAMBW0\_EL1is a 64-bit register.

## Field descriptions

<!-- image -->

HW\_SCALE\_ENABLE, bit [63]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1':

Enables hardware bandwidth scaling of the MPAMBW0\_EL1.MAX value.

| HW_SCALE_ENABLE   | Meaning                                                               |
|-------------------|-----------------------------------------------------------------------|
| 0b0               | PE-side memory bandwidth control hardware scaling in EL0 is disabled. |
| 0b1               | PE-side memory bandwidth control hardware scaling in EL0 is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ENABLED, bit [62]

Enables the PE-side memory bandwidth control when in EL0.

| ENABLED   | Meaning                                                  |
|-----------|----------------------------------------------------------|
| 0b0       | The PE-side memory bandwidth control in EL0 is disabled. |
| 0b1       | The PE-side memory bandwidth control in EL0 is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## HARDLIM, bit [61]

PE-side Maximum Bandwidth Limit Behavior Selection.

| HARDLIM   | Meaning                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Soft limit: when MPAMBW0_EL1.MAX bandwidth is exceeded, the PE is unregulated unless the downstream memory path is saturated. It is IMPLEMENTATION DEFINED how hardware determines when the downstream memory path is saturated. |
| 0b1       | Hard limit: when MPAMBW0_EL1.MAX bandwidth is exceeded, the PE does not use any more bandwidth until the memory bandwidth for the PE falls below MPAMBW0_EL1.MAX.                                                                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MPAMBWIDR\_EL1.MAX\_LIM == '00', access to this field is RW.
- When MPAMBWIDR\_EL1.MAX\_LIM == '01', access to this field is RAZ/WI.
- When MPAMBWIDR\_EL1.MAX\_LIM == '10', access to this field is RAO/WI.

## Bits [60:32]

Reserved, RES0.

## MAX,bits [31:0]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1' and MPAMBW0\_EL1.HW\_SCALE\_ENABLE == '1':

| 31   | 0   |
|------|-----|

## MAX,bits [31:0]

Maximum memory bandwidth allocated to the PE when executing at EL0 with its current PARTID.

The value is represented as a multiplier of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [31:16] represent the integer part of the value.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '0' or MPAMBW0\_EL1.HW\_SCALE\_ENABLE == '0':

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## MAX,bits [15:0]

Maximum memory bandwidth allocated to the PE when executing at EL0 with its current PARTID.

The value is represented as a fraction of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMBW0\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMBW0_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b101 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBW0_EL1 == '0' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = MPAMBW0_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMBW0_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBW0_EL1;
```

MSR MPAMBW0\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b101 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBW0_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else MPAMBW0_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMBW0_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMBW0_EL1 = X[t, 64];
```

## D24.12.6 MPAMBW1\_EL1, MPAM PE-side Maximum-bandwidth Control Register (EL1)

The MPAMBW1\_EL1 characteristics are:

## Purpose

Enables software to configure a maximum fraction of memory bandwidth that the PE is permitted to use when executing at EL1 with its current PARTID.

## Configuration

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented. Otherwise, direct accesses to MPAMBW1\_EL1are UNDEFINED.

## Attributes

MPAMBW1\_EL1is a 64-bit register.

## Field descriptions

<!-- image -->

HW\_SCALE\_ENABLE, bit [63]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1':

Enables hardware bandwidth scaling of the MPAMBW1\_EL1.MAX value.

| HW_SCALE_ENABLE   | Meaning                                                               |
|-------------------|-----------------------------------------------------------------------|
| 0b0               | PE-side memory bandwidth control hardware scaling in EL1 is disabled. |
| 0b1               | PE-side memory bandwidth control hardware scaling in EL1 is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ENABLED, bit [62]

Enables the PE-side memory bandwidth control when in EL1.

| ENABLED   | Meaning                                                  |
|-----------|----------------------------------------------------------|
| 0b0       | The PE-side memory bandwidth control in EL1 is disabled. |
| 0b1       | The PE-side memory bandwidth control in EL1 is enabled.  |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## HARDLIM, bit [61]

PE-side Maximum Bandwidth Limit Behavior Selection.

| HARDLIM   | Meaning                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Soft limit: when MPAMBW1_EL1.MAX bandwidth is exceeded, the PE is unregulated unless the downstream memory path is saturated. It is IMPLEMENTATION DEFINED how hardware determines when the downstream memory path is saturated. |
| 0b1       | Hard limit: when MPAMBW1_EL1.MAX bandwidth is exceeded, the PE does not use any more bandwidth until the memory bandwidth for the PE falls below MPAMBW1_EL1.MAX.                                                                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MPAMBWIDR\_EL1.MAX\_LIM == '00', access to this field is RW.
- When MPAMBWIDR\_EL1.MAX\_LIM == '01', access to this field is RAZ/WI.
- When MPAMBWIDR\_EL1.MAX\_LIM == '10', access to this field is RAO/WI.

Bits [60:32]

Reserved, RES0.

MAX,bits [31:0]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1' and MPAMBW1\_EL1.HW\_SCALE\_ENABLE == '1':

| 31   | 0   |
|------|-----|

## MAX,bits [31:0]

Maximum memory bandwidth allocated to the PE when executing at EL1 with its current PARTID.

The value is represented as a multiplier of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [31:16] represent the integer part of the value.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '0' or MPAMBW1\_EL1.HW\_SCALE\_ENABLE == '0':

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## MAX,bits [15:0]

Maximum memory bandwidth allocated to the PE when executing at EL1 with its current PARTID.

The value is represented as a fraction of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMBW1\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name MPAMBW1\_EL1 or MPAMBW1\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMBW1_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBW1_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x908]; else X[t, 64] = MPAMBW1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = MPAMBW2_EL2; else X[t, 64] = MPAMBW1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBW1_EL1;
```

MSR MPAMBW1\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBW1_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x908] = X[t, 64]; else MPAMBW1_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then MPAMBW2_EL2 = X[t, 64]; else MPAMBW1_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMBW1_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, MPAMBW1\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x908]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMBW1_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = MPAMBW1_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR MPAMBW1\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x908] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMBW1_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then MPAMBW1_EL1 = X[t, 64]; else UNDEFINED;
```

## D24.12.7 MPAMBW2\_EL2, MPAM PE-side Maximum-bandwidth Control Register (EL2)

The MPAMBW2\_EL2 characteristics are:

## Purpose

Enables software to configure a maximum fraction of memory bandwidth that the PE is permitted to use when executing at EL2 with its current PARTID.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented. Otherwise, direct accesses to MPAMBW2\_EL2are UNDEFINED.

## Attributes

MPAMBW2\_EL2is a 64-bit register.

## Field descriptions

<!-- image -->

## HW\_SCALE\_ENABLE, bit [63]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1':

Enables hardware bandwidth scaling of the MPAMBW2\_EL2.MAX value.

| HW_SCALE_ENABLE   | Meaning                                                               |
|-------------------|-----------------------------------------------------------------------|
| 0b0               | PE-side memory bandwidth control hardware scaling in EL2 is disabled. |
| 0b1               | PE-side memory bandwidth control hardware scaling in EL2 is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ENABLED, bit [62]

Enables the PE-side memory bandwidth control when in EL2.

| ENABLED   | Meaning                                                  |
|-----------|----------------------------------------------------------|
| 0b0       | The PE-side memory bandwidth control in EL2 is disabled. |
| 0b1       | The PE-side memory bandwidth control in EL2 is enabled.  |

## The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## HARDLIM, bit [61]

PE-side Maximum Bandwidth Limit Behavior Selection.

| HARDLIM   | Meaning                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Soft limit: when MPAMBW2_EL2.MAX bandwidth is exceeded, the PE is unregulated unless the downstream memory path is saturated. It is IMPLEMENTATION DEFINED how hardware determines when the downstream memory path is saturated. |
| 0b1       | Hard limit: when MPAMBW2_EL2.MAX bandwidth is exceeded, the PE does not use any more bandwidth until the memory bandwidth for the PE falls below MPAMBW2_EL2.MAX.                                                                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MPAMBWIDR\_EL1.MAX\_LIM == '00', access to this field is RW.
- When MPAMBWIDR\_EL1.MAX\_LIM == '01', access to this field is RAZ/WI.
- When MPAMBWIDR\_EL1.MAX\_LIM == '10', access to this field is RAO/WI.

## Bits [60:53]

Reserved, RES0.

## nTRAP\_MPAMBWIDR\_EL1, bit [52]

Traps accesses to MPAMBWIDR\_EL1 from EL1 to EL2.

| nTRAP_MPAMBWIDR_EL1   | Meaning                                                                             |
|-----------------------|-------------------------------------------------------------------------------------|
| 0b0                   | Accesses to MPAMBWIDR_EL1 from EL1 are trapped to EL2 with EC syndrome value 0x18 . |
| 0b1                   | Accesses to MPAMBWIDR_EL1 from EL1 are not trapped by this mechanism.               |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## nTRAP\_MPAMBW0\_EL1, bit [51]

Traps accesses to MPAMBW0\_EL1 from EL1 to EL2.

| nTRAP_MPAMBW0_EL1   | Meaning                                                                           |
|---------------------|-----------------------------------------------------------------------------------|
| 0b0                 | Accesses to MPAMBW0_EL1 from EL1 are trapped to EL2 with EC syndrome value 0x18 . |
| 0b1                 | Accesses to MPAMBW0_EL1 from EL1 are not trapped by this mechanism.               |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## nTRAP\_MPAMBW1\_EL1, bit [50]

Traps accesses to MPAMBW1\_EL1 from EL1 to EL2.

| nTRAP_MPAMBW1_EL1   | Meaning                                                                           |
|---------------------|-----------------------------------------------------------------------------------|
| 0b0                 | Accesses to MPAMBW1_EL1 from EL1 are trapped to EL2 with EC syndrome value 0x18 . |
| 0b1                 | Accesses to MPAMBW1_EL1 from EL1 are not trapped by this mechanism.               |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## nTRAP\_MPAMBWSM\_EL1,bit [49]

## When FEAT\_SME is implemented:

Traps accesses to MPAMBWSM\_EL1 from EL1 to EL2.

| nTRAP_MPAMBWSM_EL1   | Meaning                                                                           |
|----------------------|-----------------------------------------------------------------------------------|
| 0b0                  | Accesses to MPAMBWSM_EL1from EL1 are trapped to EL2 with EC syndrome value 0x18 . |
| 0b1                  | Accesses to MPAMBWSM_EL1from EL1 are not trapped by this mechanism.               |

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL2, this field resets to '0' .

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [48:32]

Reserved, RES0.

MAX,bits [31:0]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1' and MPAMBW2\_EL2.HW\_SCALE\_ENABLE == '1':

MAX

31

0

## MAX,bits [31:0]

Maximum memory bandwidth allocated to the PE when executing at EL2 with its current PARTID.

The value is represented as a multiplier of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [31:16] represent the integer part of the value.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '0' or MPAMBW2\_EL2.HW\_SCALE\_ENABLE == '0':

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## MAX,bits [15:0]

Maximum memory bandwidth allocated to the PE when executing at EL2 with its current PARTID.

The value is represented as a fraction of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMBW2\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name MPAMBW2\_EL2 or MPAMBW1\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMBW2\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMBW2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBW2_EL2;
```

MSR MPAMBW2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMBW2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMBW2_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, MPAMBW1\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then
```

```
UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBW1_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x908]; else X[t, 64] = MPAMBW1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = MPAMBW2_EL2; else X[t, 64] = MPAMBW1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBW1_EL1;
```

When FEAT\_VHE is implemented MSR MPAMBW1\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBW1_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x908] = X[t, 64]; else MPAMBW1_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && ↪ → MPAM3_EL3.TRAPLOWER == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then MPAMBW2_EL2 = X[t, 64]; else MPAMBW1_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMBW1_EL1 = X[t, 64];
```

## D24.12.8 MPAMBW3\_EL3, MPAM PE-side Maximum-bandwidth Control Register (EL3)

The MPAMBW3\_EL3 characteristics are:

## Purpose

Enables software to configure a maximum fraction of memory bandwidth that the PE is permitted to use when executing at EL3 with its current PARTID.

## Configuration

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented. Otherwise, direct accesses to MPAMBW3\_EL3are UNDEFINED.

## Attributes

MPAMBW3\_EL3is a 64-bit register.

## Field descriptions

<!-- image -->

HW\_SCALE\_ENABLE, bit [63]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1':

Enables hardware bandwidth scaling of the MPAMBW3\_EL3.MAX value.

| HW_SCALE_ENABLE   | Meaning                                                               |
|-------------------|-----------------------------------------------------------------------|
| 0b0               | PE-side memory bandwidth control hardware scaling in EL3 is disabled. |
| 0b1               | PE-side memory bandwidth control hardware scaling in EL3 is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ENABLED, bit [62]

Enables the PE-side memory bandwidth control when in EL3.

| ENABLED   | Meaning                                                  |
|-----------|----------------------------------------------------------|
| 0b0       | The PE-side memory bandwidth control in EL3 is disabled. |
| 0b1       | The PE-side memory bandwidth control in EL3 is enabled.  |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## HARDLIM, bit [61]

PE-side Maximum Bandwidth Limit Behavior Selection.

| HARDLIM   | Meaning                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Soft limit: when MPAMBW3_EL3.MAX bandwidth is exceeded, the PE is unregulated unless the downstream memory path is saturated. It is IMPLEMENTATION DEFINED how hardware determines when the downstream memory path is saturated. |
| 0b1       | Hard limit: when MPAMBW3_EL3.MAX bandwidth is exceeded, the PE does not use any more bandwidth until the memory bandwidth for the PE falls below MPAMBW3_EL3.MAX.                                                                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MPAMBWIDR\_EL1.MAX\_LIM == '00', access to this field is RW.
- When MPAMBWIDR\_EL1.MAX\_LIM == '01', access to this field is RAZ/WI.
- When MPAMBWIDR\_EL1.MAX\_LIM == '10', access to this field is RAO/WI.

## Bits [60:50]

Reserved, RES0.

## nTRAPLOWER,bit [49]

Traps accesses to MPAMBW2\_EL2, MPAMBWCAP\_EL2, MPAMBW1\_EL1, MPAMBW0\_EL1, MPAMBWSM\_EL1, MPAMBWIDR\_EL1 from any lower EL to EL3.

| nTRAPLOWER   | Meaning                                                                                                                                                 |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Accesses to MPAMBW2_EL2, MPAMBWCAP_EL2, MPAMBW1_EL1, MPAMBW0_EL1, MPAMBWSM_EL1, MPAMBWIDR_EL1 from EL1 are trapped to EL3 with EC syndrome value 0x18 . |
| 0b1          | Accesses to MPAMBW2_EL2, MPAMBWCAP_EL2, MPAMBW1_EL1, MPAMBW0_EL1, MPAMBWSM_EL1, MPAMBWIDR_EL1 from EL1 are not trapped by this mechanism.               |

Note

This trap is higher priority than any of the traps controlled by MPAM \_EL2 registers.

The reset behavior of this field is:

- On a Warm reset:

- When the highest implemented Exception level is EL3, this field resets to '0' .

Bits [48:32]

Reserved, RES0.

MAX,bits [31:0]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1' and MPAMBW3\_EL3.HW\_SCALE\_ENABLE == '1':

MAX

31

0

## MAX,bits [31:0]

Maximum memory bandwidth allocated to the PE when executing at EL3 with its current PARTID.

The value is represented as a multiplier of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [31:16] represent the integer part of the value.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '0' or MPAMBW3\_EL3.HW\_SCALE\_ENABLE == '0':

RES0

31

16 15

MAX

0

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## MAX,bits [15:0]

Maximum memory bandwidth allocated to the PE when executing at EL3 with its current PARTID.

The value is represented as a fraction of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMBW3\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMBW3\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0101 | 0b100 |

if !IsFeatureImplemented(FEAT\_MPAM\_PE\_BW\_CTRL) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

X[t, 64] = MPAMBW3\_EL3;

MSR MPAMBW3\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0101 | 0b100 |

if !IsFeatureImplemented(FEAT\_MPAM\_PE\_BW\_CTRL) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then UNDEFINED;

elsif PSTATE.EL == EL2 then UNDEFINED;

elsif PSTATE.EL == EL3 then MPAMBW3\_EL3 = X[t, 64];

## D24.12.9 MPAMBWCAP\_EL2, MPAM PE-side Maximum-bandwidth Limit Virtualization Register

The MPAMBWCAP\_EL2 characteristics are:

## Purpose

Allows software executing at EL2 to provide MPAMBWCAP\_EL2.CAP as an upper bound to MPAMBW1\_EL1.MAX.

If FEAT\_SME is implemented, the upper bound also applies to MPAMBWSM\_EL1.MAX when executing at EL1: the maximum bandwidth allowed for the PE is MIN(MPAMBWSM\_EL1.MAX, MPAMBWCAP\_EL2.CAP).

If the Effective value of HCR\_EL2.{E2H,TGE} is not {1,1}:

- The upper bound also applies to MPAMBW0\_EL1.MAX: the maximum bandwidth allowed for the PE is MIN(MPAMBW0\_EL1.MAX, MPAMBWCAP\_EL2.CAP).
- If FEAT\_SME is implemented, the upper bound also applies to MPAMBWSM\_EL1.MAX when executing at EL0: the maximum bandwidth allowed for the PE is MIN(MPAMBWSM\_EL1.MAX, MPAMBWCAP\_EL2.CAP).

If MPAMBWCAP\_EL2.ENABLED is 1, a PARTID that has used more than min(CAP,MAX) is given no access to additional bandwidth.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented and MPAMIDR\_EL1.HAS\_HCR == '1'. Otherwise, direct accesses to MPAMBWCAP\_EL2 are UNDEFINED.

## Attributes

MPAMBWCAP\_EL2is a 64-bit register.

## Field descriptions

<!-- image -->

HW\_SCALE\_ENABLE, bit [63]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1':

Enables hardware bandwidth scaling of the MPAMBWCAP\_EL2.CAP value.

| HW_SCALE_ENABLE   | Meaning                                                                        |
|-------------------|--------------------------------------------------------------------------------|
| 0b0               | PE-side memory bandwidth control hardware scaling for EL2 capping is disabled. |

| HW_SCALE_ENABLE   | Meaning                                                                       |
|-------------------|-------------------------------------------------------------------------------|
| 0b1               | PE-side memory bandwidth control hardware scaling for EL2 capping is enabled. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ENABLED, bit [62]

Enables the PE-side memory bandwidth control capping by EL2.

| ENABLED   | Meaning                                                          |
|-----------|------------------------------------------------------------------|
| 0b0       | The PE-side memory bandwidth control capping by EL2 is disabled. |
| 0b1       | The PE-side memory bandwidth control capping by EL2 is enabled.  |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bits [61:32]

Reserved, RES0.

## CAP, bits [31:0]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1' and MPAMBWCAP\_EL2.HW\_SCALE\_ENABLE == '1':

0

31

## CAP, bits [31:0]

Upper bound to the maximum memory bandwidth allocated to the current PARTID in MPAMBW1\_EL1.MAX, MPAMBW0\_EL1.MAX and MPAMBWSM\_EL1.MAX.

The value is represented as a multiplier of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [31:16] represent the integer part of the value.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The value set in the MAX field must be less than or equal to this upper bound.

CAP

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '0' or MPAMBWCAP\_EL2.HW\_SCALE\_ENABLE == '0':

<!-- image -->

| 31   | 16 15   |
|------|---------|
| RES0 | CAP     |

## Bits [31:16]

Reserved, RES0.

## CAP, bits [15:0]

Upper bound to the maximum memory bandwidth allocated to the current PARTID in MPAMBW1\_EL1.MAX, MPAMBW0\_EL1.MAX and MPAMBWSM\_EL1.MAX.

The value is represented as a fraction of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The value set in the MAX field must be less than or equal to this upper bound.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMBWCAP\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMBWCAP_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0101 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) && MPAMIDR_EL1.HAS_HCR == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x910]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMBWCAP_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBWCAP_EL2;
```

MSR MPAMBWCAP\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0101 | 0b110 |

```
if !(IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) && MPAMIDR_EL1.HAS_HCR == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x910] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMBWCAP_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMBWCAP_EL2 = X[t, 64];
```

## D24.12.10 MPAMBWIDR\_EL1, MPAM PE-side Bandwidth Controls ID Register

The MPAMBWIDR\_EL1 characteristics are:

## Purpose

Indicates the supported PE-side memory bandwidth parameter values.

## Configuration

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented. Otherwise, direct accesses to MPAMBWIDR\_EL1 are UNDEFINED.

## Attributes

MPAMBWIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## HAS\_HW\_SCALE, bit [63]

Indicates whether hardware support for auto-scaling of MPAMBWn\_ELx.MAX, MPAMBWSM\_EL1.MAX and MPAMBWCAP\_EL2.CAP limits is available.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAS_HW_SCALE   | Meaning                                               |
|----------------|-------------------------------------------------------|
| 0b0            | Hardware support for auto-scaling is not implemented. |
| 0b1            | Hardware support for auto-scaling is implemented.     |

Access to this field is RO.

## Bits [62:32]

Reserved, RES0.

## MAX\_LIM, bits [31:30]

Indicates the implemented maximum-bandwidth limit partitioning behaviors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MAX_LIM   | Meaning                                                   |
|-----------|-----------------------------------------------------------|
| 0b00      | Both soft limit and hard limit behaviors are implemented. |
| 0b01      | Soft limit behavior is implemented.                       |
| 0b10      | Hard limit behavior is implemented.                       |
| 0b11      | Reserved.                                                 |

Access to this field is RO.

## Bits [29:6]

Reserved, RES0.

## BWA\_WD,bits [5:0]

Indicates the number of implemented bits in the bandwidth allocation fields MPAMBWn\_ELx.MAX, MPAMBWSM\_EL1.MAXand MPAMBWCAP\_EL2.CAP.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BWA_WD               | Meaning                                                        |
|----------------------|----------------------------------------------------------------|
| 0b000001 .. 0b010000 | Number of implemented bits in the bandwidth allocation fields. |

Access to this field is RO.

## Accessing MPAMBWIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMBWIDR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b101 |

```
if !IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBWIDR_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = MPAMBWIDR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMBWIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBWIDR_EL1;
```

## D24.12.11 MPAMBWSM\_EL1, MPAM Streaming Mode Bandwidth Control Register (EL1)

The MPAMBWSM\_EL1 characteristics are:

## Purpose

Enables software to configure a maximum fraction of memory bandwidth that the PE is permitted for SME memory accesses labelled with values from MPAMSM\_EL1.

## Configuration

This register is present only when FEAT\_MPAM\_PE\_BW\_CTRL is implemented and FEAT\_SME is implemented. Otherwise, direct accesses to MPAMBWSM\_EL1 are UNDEFINED.

## Attributes

MPAMBWSM\_EL1is a 64-bit register.

## Field descriptions

<!-- image -->

HW\_SCALE\_ENABLE, bit [63]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1':

Enables hardware bandwidth scaling of the MPAMBWSM\_EL1.MAX value.

| HW_SCALE_ENABLE   | Meaning                                                                              |
|-------------------|--------------------------------------------------------------------------------------|
| 0b0               | PE-side memory bandwidth control hardware scaling for streaming PARTIDs is disabled. |
| 0b1               | PE-side memory bandwidth control hardware scaling for streaming PARTIDs is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ENABLED, bit [62]

Enables the PE-side memory bandwidth control for streaming PARTIDs.

| ENABLED   | Meaning                                                             |
|-----------|---------------------------------------------------------------------|
| 0b0       | PE-side memory bandwidth control for streaming PARTIDs is disabled. |
| 0b1       | PE-side memory bandwidth control for streaming PARTIDs is enabled.  |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## HARDLIM, bit [61]

PE-side Maximum-bandwidth Limit Behavior Selection.

| HARDLIM   | Meaning                                                                                                                                                                                                                          |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0       | Soft limit: when MPAMBWSM_EL1.MAXbandwidth is exceeded, the PE is unregulated unless the downstream memory path is saturated. It is IMPLEMENTATION DEFINED how hardware determines when the downstream memory path is saturated. |
| 0b1       | Hard limit: when MPAMBWSM_EL1.MAXbandwidth is exceeded, the PE does not use any more bandwidth until the memory bandwidth for the PE falls below MPAMBWSM_EL1.MAX.                                                               |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When MPAMBWIDR\_EL1.MAX\_LIM == '00', access to this field is RW.
- When MPAMBWIDR\_EL1.MAX\_LIM == '01', access to this field is RAZ/WI.
- When MPAMBWIDR\_EL1.MAX\_LIM == '10', access to this field is RAO/WI.

Bits [60:32]

Reserved, RES0.

## MAX,bits [31:0]

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '1' and MPAMBWSM\_EL1.HW\_SCALE\_ENABLE == '1':

MAX

31

0

## MAX,bits [31:0]

Maximum memory bandwidth allocated to the partition selected by MPAMSM\_EL1.PARTID\_D.

The value is represented as a multiplier of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [31:16] represent the integer part of the value.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When MPAMBWIDR\_EL1.HAS\_HW\_SCALE == '0' or MPAMBWSM\_EL1.HW\_SCALE\_ENABLE == '0':

<!-- image -->

| 31   | 16 15   |
|------|---------|
| RES0 | MAX     |

## Bits [31:16]

Reserved, RES0.

## MAX,bits [15:0]

Maximum memory bandwidth allocated to the partition selected by MPAMSM\_EL1.PARTID\_D.

The value is represented as a fraction of the available bandwidth for the PE. The value is represented in base-2 fixed-point format.

Bits [15:(16 - MPAMBWIDR\_EL1.BWA\_WD)] represent the fractional part of the value. When MPAMBWIDR\_EL1.BWA\_WD indicates a width less than 16 bits, bits [(15 -MPAMBWIDR\_EL1.BWA\_WD):0] are RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMBWSM\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMBWSM_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) && IsFeatureImplemented(FEAT_SME)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBWSM_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = MPAMBWSM_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMBWSM_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMBWSM_EL1;
```

MSR MPAMBWSM\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_MPAM_PE_BW_CTRL) && IsFeatureImplemented(FEAT_SME)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && MPAMBW2_EL2.nTRAP_MPAMBWSM_EL1 == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else MPAMBWSM_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MPAMBW3_EL3.nTRAPLOWER == '0' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MPAMBW3_EL3.nTRAPLOWER == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMBWSM_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMBWSM_EL1 = X[t, 64];
```

## D24.12.12 MPAMHCR\_EL2, MPAM Hypervisor Control Register (EL2)

The MPAMHCR\_EL2 characteristics are:

## Purpose

Controls the PARTID virtualization features of MPAM.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when FEAT\_MPAM is implemented and MPAMIDR\_EL1.HAS\_HCR == '1'. Otherwise, direct accesses to MPAMHCR\_EL2 are UNDEFINED.

## Attributes

MPAMHCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TRAP\_MPAMIDR\_EL1, bit [31]

When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented:

Trap accesses from EL1 to MPAMIDR\_EL1 to EL2.

| TRAP_MPAMIDR_EL1   | Meaning                                                     |
|--------------------|-------------------------------------------------------------|
| 0b0                | This control does not cause any instructions to be trapped. |
| 0b1                | Direct accesses to MPAMIDR_EL1 from EL1 are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When EL3 is not implemented, this field resets to '1' .
- When EL3 is implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [30:9]

Reserved, RES0.

## GSTAPP\_PLK, bit [8]

## When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented:

Make the PARTIDs at EL0 the same as the PARTIDs at EL1. When executing at EL0, EL2 is enabled, HCR\_EL2.TGE == 0 and GSTAPP\_PLK = 1, MPAM1\_EL1 is used instead of MPAM0\_EL1 to generate MPAMlabels for memory requests.

| GSTAPP_PLK   | Meaning                                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | MPAM0_EL1 is used to generate MPAMlabels when executing at EL0.                                                                    |
| 0b1          | MPAM1_EL1 is used to generate MPAMlabels when executing at EL0 with EL2 enabled and HCR_EL2.TGE == 0. Otherwise MPAM0_EL1 is used. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [7:2]

Reserved, RES0.

## EL1\_VPMEN, bit [1]

## When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented:

Enable virtualized identifiers in MPAM1\_EL1 when executing at EL1. This bit also enables virtualized identifiers when MPAM1\_EL1 is used to generate MPAM identifiers for memory requests at EL0 due to GSTAPP\_PLK == 1.

| EL1_VPMEN   | Meaning                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MPAM1_EL1.PARTID_I and MPAM1_EL1.PARTID_D are physical PARTIDs used to label memory system requests.                                                                                            |
| 0b1         | MPAM1_EL1.PARTID_I and MPAM1_EL1.PARTID_D are virtual PARTIDs used to index the MPAMVPMn_EL2.PhyPARTID fields to map the virtual PARTID into a physical PARTID to label memory system requests. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EL0\_VPMEN, bit [0]

## When FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented:

Enable virtualized identifiers in MPAM0\_EL1 unless the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, EL0\_VPMEN is ignored and MPAM0\_EL1 identifiers are not virtualized.

When MPAMHCR\_EL2.GSTAPP\_PLK == 1 and HCR\_EL2.TGE == 0, MPAM1\_EL1 is used as the source of identifiers and the virtualization of identifiers in MPAM1\_EL1 is controlled by MPAMHCR\_EL2.EL1\_VPMEN.

| EL0_VPMEN   | Meaning                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | MPAM0_EL1.PARTID_I and MPAM0_EL1.PARTID_D are physical PARTIDs used to label memory system requests.                                                                                            |
| 0b1         | MPAM0_EL1.PARTID_I and MPAM0_EL1.PARTID_D are virtual PARTIDs used to index the MPAMVPMn_EL2.PhyPARTID fields to map the virtual PARTID into a physical PARTID to label memory system requests. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing MPAMHCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMHCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_MPAM) && MPAMIDR_EL1.HAS_HCR == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x930]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = MPAMHCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMHCR_EL2;
```

MSR MPAMHCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0100 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_MPAM) && MPAMIDR_EL1.HAS_HCR == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x930] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMHCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMHCR_EL2 = X[t, 64];
```

## D24.12.13 MPAMIDR\_EL1, MPAM ID Register (EL1)

The MPAMIDR\_EL1 characteristics are:

## Purpose

Indicates the maximum PARTID and PMG values supported in the implementation and the support for other optional features.

## Configuration

This register is present only when FEAT\_MPAM is implemented. Otherwise, direct accesses to MPAMIDR\_EL1 are UNDEFINED.

## Attributes

MPAMIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:62]

Reserved, RES0.

## HAS\_SDEFLT, bit [61]

HAS\_SDEFLT indicates support for MPAM3\_EL3.SDEFLT bit.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAS_SDEFLT   | Meaning                                         |
|--------------|-------------------------------------------------|
| 0b0          | The SDEFLT bit is not implemented in MPAM3_EL3. |
| 0b1          | The SDEFLT bit is implemented in MPAM3_EL3.     |

When MPAM3\_EL3.SDEFLT == 1, accesses from the Secure Execution state use the default PARTID, PARTID == 0.

Access to this field is RO.

## HAS\_FORCE\_NS, bit [60]

HAS\_FORCE\_NS indicates support for MPAM3\_EL3.FORCE\_NS bit.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAS_FORCE_NS   | Meaning                                           |
|----------------|---------------------------------------------------|
| 0b0            | The FORCE_NS bit is not implemented in MPAM3_EL3. |
| 0b1            | The FORCE_NS bit is implemented in MPAM3_EL3.     |

When MPAM3\_EL3.FORCE\_NS == 1, accesses from the Secure Execution state have MPAM\_NS == 1.

Access to this field is RO.

## SP4, bit [59]

Supports 4 MPAM PARTID spaces.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SP4   | Meaning                       |
|-------|-------------------------------|
| 0b0   | MPAMsupports 2 PARTID spaces. |
| 0b1   | MPAMsupports 4 PARTID spaces. |

Access to this field is RO.

## HAS\_TIDR, bit [58]

HAS\_TIDR indicates support for MPAM2\_EL2.TIDR bit.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAS_TIDR   | Meaning                                       |
|------------|-----------------------------------------------|
| 0b0        | The TIDR bit is not implemented in MPAM2_EL2. |
| 0b1        | The TIDR bit is implemented in MPAM2_EL2.     |

Note

Arm recommends that when the MPAM version is MPAM v0.1 or MPAM v1.1, MPAMIDR\_EL1.HAS\_TIDR is 1 and that the MPAM2\_EL2.TIDR field is implemented.

Access to this field is RO.

## HAS\_ALTSP, bit [57]

HAS\_ALTSP indicates support for alternative PARTID spaces.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAS_ALTSP   | Meaning                                                                                 |
|-------------|-----------------------------------------------------------------------------------------|
| 0b0         | Alternative PARTID spaces are not implemented.                                          |
| 0b1         | Alternative PARTID spaces are implemented with control bits in MPAM3_EL3 and MPAM2_EL2. |

Access to this field is RO.

## HAS\_BW\_CTRL, bit [56]

HAS\_BW\_CTRL indicates support for PE-side bandwidth controls.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAS_BW_CTRL   | Meaning                                         |
|---------------|-------------------------------------------------|
| 0b0           | PE-side bandwidth controls are not implemented. |
| 0b1           | PE-side bandwidth controls are implemented.     |

FEAT\_MPAM\_PE\_BW\_CTRL implements the functionality identified by the value 0b1 .

Access to this field is RO.

## Bits [55:40]

Reserved, RES0.

## PMG\_MAX,bits [39:32]

The largest value of PMG that the implementation can generate. The PMG\_I and PMG\_D fields of every MPAMn\_ELx must implement at least enough bits to represent PMG\_MAX.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bits [31:21]

Reserved, RES0.

## VPMR\_MAX,bits [20:18]

## When MPAMIDR\_EL1.HAS\_HCR == '1':

Indicates the maximum register index n for the MPAMVPM&lt;n&gt;\_EL2 registers.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RAZ.

## HAS\_HCR, bit [17]

HAS\_HCR indicates that the PE implementation supports MPAM virtualization, including MPAMHCR\_EL2, MPAMVPMV\_EL2, and MPAMVPM&lt;n&gt;\_EL2 with n in the range 0 to VPMR\_MAX. Must be 0 if EL2 is not implemented in either Security state.

Access to this field is RO.

## Bit [16]

Reserved, RES0.

## PARTID\_MAX, bits [15:0]

The largest value of PARTID that the implementation can generate. The PARTID\_I and PARTID\_D fields of every MPAMn\_ELx must implement at least enough bits to represent PARTID\_MAX.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing MPAMIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0100 | 0b100 |

```
if !IsFeatureImplemented(FEAT_MPAM) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAMIDR_EL1.HAS_HCR == '1' && ↪ → MPAMHCR_EL2.TRAP_MPAMIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAMIDR_EL1.HAS_TIDR == '1' && ↪ → MPAM2_EL2.TIDR == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = MPAMIDR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED;
```

| HAS_HCR   | Meaning                              |
|-----------|--------------------------------------|
| 0b0       | MPAMvirtualization is not supported. |
| 0b1       | MPAMvirtualization is supported.     |

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMIDR_EL1;
```

## D24.12.14 MPAMSM\_EL1, MPAM Streaming Mode Register

The MPAMSM\_EL1 characteristics are:

## Purpose

Holds information to generate MPAM labels for memory requests that are:

- Issued due to the execution of SME load and store instructions.
- Issued when the PE is in Streaming SVE mode due to the execution of SVE and SIMD&amp;FP load and store instructions and SVE prefetch instructions.

If an implementation uses a shared SMCU, then the MPAM labels in this register have precedence over the labels in MPAM0\_EL1, MPAM1\_EL1, MPAM2\_EL2, and MPAM3\_EL3.

If an implementation includes an SMCU that is not shared with other PEs, then it is IMPLEMENTATION DEFINED whether the MPAM labels in this register have precedence over the labels in MPAM0\_EL1, MPAM1\_EL1, MPAM2\_EL2, and MPAM3\_EL3.

The MPAM labels in this register are only used if MPAM1\_EL1.MPAMEN (MPAM 1.0) or MPAMCTL\_EL1.MPAMEN (MPAM 2.0) is 1.

For memory requests issued from EL0, the MPAM PARTID in this register is virtual and mapped into a physical PARTID when all of the following are true:

- EL2 is implemented and enabled in the current Security state, and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.
- The MPAM virtualization option is implemented and MPAMHCR\_EL2.EL0\_VPMEN is 1.

For memory requests issued from EL1, the MPAM PARTID in this register is virtual and mapped into a physical PARTID when all of the following are true:

- EL2 is implemented and enabled in the current Security state.
- The MPAM virtualization option is implemented and MPAMHCR\_EL2.EL1\_VPMEN is 1.

## Configuration

This register is present only when FEAT\_MPAM is implemented and FEAT\_SME is implemented. Otherwise, direct accesses to MPAMSM\_EL1 are UNDEFINED.

## Attributes

MPAMSM\_EL1is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## PMG\_D, bits [47:40]

Performance monitoring group property for PARTID\_D.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [39:32]

Reserved, RES0.

## PARTID\_D, bits [31:16]

Partition ID for requests issued due to the execution at any Exception level of SME load and store instructions and, when the PE is in Streaming SVE mode, SVE and SIMD&amp;FP load and store instructions and SVE prefetch instructions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [15:0]

Reserved, RES0.

## Accessing MPAMSM\_EL1

None of the fields in this register are permitted to be cached in a TLB.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMSM\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_MPAM) && IsFeatureImplemented(FEAT_SME)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.EnMPAMSM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = MPAMSM_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMSM_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMSM_EL1;
```

MSR MPAMSM\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1010 | 0b0101 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_MPAM) && IsFeatureImplemented(FEAT_SME)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_MPAM) && MPAM2_EL2.EnMPAMSM == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else MPAMSM_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMSM_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMSM_EL1 = X[t, 64];
```

## D24.12.15 MPAMVPM0\_EL2, MPAM Virtual PARTID Mapping Register 0

The MPAMVPM0\_EL2 characteristics are:

## Purpose

MPAMVPM0\_EL2 provides mappings from virtual PARTIDs 0 - 3 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM&lt;n&gt;\_EL2 register. VPMR\_MAXcan be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented) and MPAMIDR\_EL1.HAS\_HCR == '1'. Otherwise, direct accesses to MPAMVPM0\_EL2 are UNDEFINED.

## Attributes

MPAMVPM0\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 48 47      | 32         |
|------------|------------|------------|
| PhyPARTID3 | PhyPARTID2 |            |
| 31         | 16 15      | 0          |
| PhyPARTID1 |            | PhyPARTID0 |

## PhyPARTID3, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 3. PhyPARTID3 gives the mapping of virtual PARTID 3 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID2, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 2. PhyPARTID2 gives the mapping of virtual PARTID 2 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID1, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 1. PhyPARTID1 gives the mapping of virtual PARTID 1 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID0, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 0. PhyPARTID0 gives the mapping of virtual PARTID 0 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM0\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMVPM0\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b000 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x940]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM0_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM0_EL2;
```

MSR MPAMVPM0\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b000 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x940] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM0_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM0_EL2 = X[t, 64];
```

## D24.12.16 MPAMVPM1\_EL2, MPAM Virtual PARTID Mapping Register 1

The MPAMVPM1\_EL2 characteristics are:

## Purpose

MPAMVPM1\_EL2 provides mappings from virtual PARTIDs 4 - 7 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM0\_EL2 to MPAMVPM7\_EL2 registers. VPMR\_MAX can be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) &gt; 0). Otherwise, direct accesses to MPAMVPM1\_EL2 are UNDEFINED.

## Attributes

MPAMVPM1\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 48 47      | 32   |
|------------|------------|------|
| PhyPARTID7 | PhyPARTID6 |      |
| 31         | 16 15      | 0    |
| PhyPARTID5 | PhyPARTID4 |      |

## PhyPARTID7, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 7. PhyPARTID7 gives the mapping of virtual PARTID 7 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID6, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 6. PhyPARTID6 gives the mapping of virtual PARTID 6 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID5, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 5. PhyPARTID5 gives the mapping of virtual PARTID 5 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID4, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 4. PhyPARTID4 gives the mapping of virtual PARTID 4 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM1\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM1_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b001 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x948]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM1_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM1_EL2;
```

MSR MPAMVPM1\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b001 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 0) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x948] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM1_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM1_EL2 = X[t, 64];
```

## D24.12.17 MPAMVPM2\_EL2, MPAM Virtual PARTID Mapping Register 2

The MPAMVPM2\_EL2 characteristics are:

## Purpose

MPAMVPM2\_EL2 provides mappings from virtual PARTIDs 8 - 11 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM0\_EL2 to MPAMVPM7\_EL2 registers. VPMR\_MAX can be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) &gt; 1). Otherwise, direct accesses to MPAMVPM2\_EL2 are UNDEFINED.

## Attributes

MPAMVPM2\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63          | 48 47       | 32   |
|-------------|-------------|------|
| PhyPARTID11 | PhyPARTID10 |      |
| 31          | 16 15       | 0    |
| PhyPARTID9  | PhyPARTID8  |      |

## PhyPARTID11, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 11. PhyPARTID11 gives the mapping of virtual PARTID 11 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID10, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 10. PhyPARTID10 gives the mapping of virtual PARTID 10 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID9, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 9. PhyPARTID9 gives the mapping of virtual PARTID 9 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID8, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 8. PhyPARTID8 gives the mapping of virtual PARTID 8 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM2\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM2_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b010 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x950]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM2_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM2_EL2;
```

MSR MPAMVPM2\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b010 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x950] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM2_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM2_EL2 = X[t, 64];
```

## D24.12.18 MPAMVPM3\_EL2, MPAM Virtual PARTID Mapping Register 3

The MPAMVPM3\_EL2 characteristics are:

## Purpose

MPAMVPM3\_EL2 provides mappings from virtual PARTIDs 12 - 15 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM&lt;n&gt;\_EL2 registers. VPMR\_MAXcan be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) &gt; 2). Otherwise, direct accesses to MPAMVPM3\_EL2 are UNDEFINED.

## Attributes

MPAMVPM3\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63          | 48 47       | 32   |
|-------------|-------------|------|
| PhyPARTID15 | PhyPARTID14 |      |
| 31          | 16 15       | 0    |
| PhyPARTID13 | PhyPARTID12 |      |

## PhyPARTID15, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 15. PhyPARTID15 gives the mapping of virtual PARTID 15 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID14, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 14. PhyPARTID14 gives the mapping of virtual PARTID 14 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID13, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 13. PhyPARTID13 gives the mapping of virtual PARTID 13 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID12, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 12. PhyPARTID12 gives the mapping of virtual PARTID 12 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM3\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM3_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b011 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x958]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM3_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM3_EL2;
```

MSR MPAMVPM3\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b011 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x958] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM3_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM3_EL2 = X[t, 64];
```

## D24.12.19 MPAMVPM4\_EL2, MPAM Virtual PARTID Mapping Register 4

The MPAMVPM4\_EL2 characteristics are:

## Purpose

MPAMVPM4\_EL2 provides mappings from virtual PARTIDs 16 - 19 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM&lt;n&gt;\_EL2 registers. VPMR\_MAXcan be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) &gt; 3). Otherwise, direct accesses to MPAMVPM4\_EL2 are UNDEFINED.

## Attributes

MPAMVPM4\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63          | 48 47       | 32   |
|-------------|-------------|------|
| PhyPARTID19 | PhyPARTID18 |      |
| 31          | 16 15       | 0    |
| PhyPARTID17 | PhyPARTID16 |      |

## PhyPARTID19, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 19. PhyPARTID19 gives the mapping of virtual PARTID 19 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID18, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 18. PhyPARTID18 gives the mapping of virtual PARTID 18 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID17, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 17. PhyPARTID17 gives the mapping of virtual PARTID 17 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID16, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 16. PhyPARTID16 gives the mapping of virtual PARTID 16 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM4\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM4_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b100 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 3) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x960]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM4_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM4_EL2;
```

MSR MPAMVPM4\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b100 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 3) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x960] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM4_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM4_EL2 = X[t, 64];
```

## D24.12.20 MPAMVPM5\_EL2, MPAM Virtual PARTID Mapping Register 5

The MPAMVPM5\_EL2 characteristics are:

## Purpose

MPAMVPM5\_EL2 provides mappings from virtual PARTIDs 20 - 23 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM&lt;n&gt;\_EL2 registers. VPMR\_MAXcan be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) &gt; 4). Otherwise, direct accesses to MPAMVPM5\_EL2 are UNDEFINED.

## Attributes

MPAMVPM5\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63          | 48 47       | 32   |
|-------------|-------------|------|
| PhyPARTID23 | PhyPARTID22 |      |
| 31          | 16 15       | 0    |
| PhyPARTID21 | PhyPARTID20 |      |

## PhyPARTID23, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 23. PhyPARTID23 gives the mapping of virtual PARTID 23 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID22, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 22. PhyPARTID22 gives the mapping of virtual PARTID 22 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID21, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 21. PhyPARTID21 gives the mapping of virtual PARTID 21 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID20, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 20. PhyPARTID20 gives the mapping of virtual PARTID 20 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM5\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM5_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b101 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 4) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x968]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM5_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM5_EL2;
```

MSR MPAMVPM5\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b101 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 4) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x968] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM5_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM5_EL2 = X[t, 64];
```

## D24.12.21 MPAMVPM6\_EL2, MPAM Virtual PARTID Mapping Register 6

The MPAMVPM6\_EL2 characteristics are:

## Purpose

MPAMVPM6\_EL2 provides mappings from virtual PARTIDs 24 - 27 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM&lt;n&gt;\_EL2 registers. VPMR\_MAXcan be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for the PARTID in MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) &gt; 5). Otherwise, direct accesses to MPAMVPM6\_EL2 are UNDEFINED.

## Attributes

MPAMVPM6\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63          | 48 47       | 32   |
|-------------|-------------|------|
| PhyPARTID27 | PhyPARTID26 |      |
| 31          | 16 15       | 0    |
| PhyPARTID25 | PhyPARTID24 |      |

## PhyPARTID27, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 27. PhyPARTID27 gives the mapping of virtual PARTID 27 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID26, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 26. PhyPARTID26 gives the mapping of virtual PARTID 26 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID25, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 25. PhyPARTID25 gives the mapping of virtual PARTID 25 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID24, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 24. PhyPARTID24 gives the mapping of virtual PARTID 24 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM6\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM6_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b110 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 5) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x970]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM6_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM6_EL2;
```

MSR MPAMVPM6\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b110 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) > 5) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x970] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM6_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM6_EL2 = X[t, 64];
```

## D24.12.22 MPAMVPM7\_EL2, MPAM Virtual PARTID Mapping Register 7

The MPAMVPM7\_EL2 characteristics are:

## Purpose

MPAMVPM7\_EL2 provides mappings from virtual PARTIDs 28 - 31 to physical PARTIDs.

MPAMIDR\_EL1.VPMR\_MAX field gives the index of the highest implemented MPAMVPM&lt;n&gt;\_EL2 registers. VPMR\_MAXcan be as large as 7 (8 registers) or 32 virtual PARTIDs. If MPAMIDR\_EL1.VPMR\_MAX == 0, there is only a single MPAMVPM&lt;n&gt;\_EL2 register, MPAMVPM0\_EL2.

Virtual PARTID mapping is enabled by MPAMHCR\_EL2.EL1\_VPMEN for the PARTID in MPAM1\_EL1 and by MPAMHCR\_EL2.EL0\_VPMEN for MPAM0\_EL1.

Avirtual-to-physical PARTID mapping entry, PhyPARTID&lt;n&gt;, is valid only when the MPAMVPMV\_EL2.VPM\_V bit in bit position n is set to 1.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when ((IsFeatureImplemented(FEAT\_MPAMv0p1) || IsFeatureImplemented(FEAT\_MPAMv1p0)) &amp;&amp; (MPAMIDR\_EL1.HAS\_HCR == '1')) &amp;&amp; (UInt(MPAMIDR\_EL1.VPMR\_MAX) == 7). Otherwise, direct accesses to MPAMVPM7\_EL2 are UNDEFINED.

## Attributes

MPAMVPM7\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63          | 48 47       | 32   |
|-------------|-------------|------|
| PhyPARTID31 | PhyPARTID30 |      |
| 31          | 16 15       | 0    |
| PhyPARTID29 | PhyPARTID28 |      |

## PhyPARTID31, bits [63:48]

Virtual PARTID Mapping Entry for virtual PARTID 31. PhyPARTID31 gives the mapping of virtual PARTID 31 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID30, bits [47:32]

Virtual PARTID Mapping Entry for virtual PARTID 30. PhyPARTID30 gives the mapping of virtual PARTID 30 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID29, bits [31:16]

Virtual PARTID Mapping Entry for virtual PARTID 29. PhyPARTID29 gives the mapping of virtual PARTID 29 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PhyPARTID28, bits [15:0]

Virtual PARTID Mapping Entry for virtual PARTID 28. PhyPARTID28 gives the mapping of virtual PARTID 28 to a physical PARTID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPM7\_EL2

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MPAMVPM7_EL2
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) == 7) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x978]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPM7_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPM7_EL2;
```

MSR MPAMVPM7\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0110 | 0b111 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1' && UInt(MPAMIDR_EL1.VPMR_MAX) == 7) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x978] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPM7_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPM7_EL2 = X[t, 64];
```

## D24.12.23 MPAMVPMV\_EL2, MPAM Virtual Partition Mapping Valid Register

The MPAMVPMV\_EL2 characteristics are:

## Purpose

Valid bits for virtual PARTID mapping entries. Each bit m corresponds to virtual PARTID mapping entry m in the MPAMVPM&lt;n&gt;\_EL2 registers where n = m » 2.

## Configuration

This register has no effect if EL2 is not enabled in the current Security state.

This register is present only when (FEAT\_MPAMv0p1 is implemented or FEAT\_MPAMv1p0 is implemented) and MPAMIDR\_EL1.HAS\_HCR == '1'. Otherwise, direct accesses to MPAMVPMV\_EL2 are UNDEFINED.

## Attributes

MPAMVPMV\_EL2is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## VPM\_V&lt;m&gt;, bits [m], for m = 31 to 0

Contains valid bit for virtual PARTID mapping entry corresponding to virtual PARTID&lt;m&gt;.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MPAMVPMV\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MPAMVPMV\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0100 | 0b001 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x938]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MPAMVPMV_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MPAMVPMV_EL2;
```

MSR MPAMVPMV\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b0100 | 0b001 |

```
if !((IsFeatureImplemented(FEAT_MPAMv0p1) || IsFeatureImplemented(FEAT_MPAMv1p0)) && MPAMIDR_EL1.HAS_HCR ↪ → == '1') then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x938] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then if HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); else AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == ↪ → '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_MPAM) && MPAM3_EL3.TRAPLOWER == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MPAMVPMV_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MPAMVPMV_EL2 = X[t, 64];
```