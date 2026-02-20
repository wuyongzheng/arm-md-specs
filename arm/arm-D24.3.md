## D24.3 Debug registers

This section lists the Debug System registers in AArch64 state, in alphabetic order:

- The principal encoding space for debug registers is op0 == 0b10 , op1 == {0, 3, 4}. Instructions for accessing debug System registers summarizes the registers in this encoding space and lists them in order of their encodings.
- In addition, the following registers in the op0 == 0b11 encoding space are classified as Debug registers:
- -DLR\_EL0.
- -DSPSR\_EL0.
- -MDCR\_EL2.
- -MDCR\_EL3.
- -SDER32\_EL3.

## D24.3.1 DBGAUTHSTATUS\_EL1, Debug Authentication Status Register

The DBGAUTHSTATUS\_EL1 characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for debug.

## Configuration

AArch64 System register DBGAUTHSTATUS\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGAUTHSTATUS[31:0].

AArch64 System register DBGAUTHSTATUS\_EL1 bits [31:0] are architecturally mapped to External register DBGAUTHSTATUS\_EL1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGAUTHSTATUS\_EL1 are UNDEFINED.

## Attributes

DBGAUTHSTATUS\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |       |             |      |       |       |      |      |      |       | 32   |      |      |      |
|------|-------|-------------|------|-------|-------|------|------|------|-------|------|------|------|------|
|      |       |             | RES0 | RES0  | RES0  | RES0 | RES0 | RES0 | RES0  | RES0 | RES0 | RES0 | RES0 |
| 31   | 28    | 27 26 25 24 | 16   | 15 14 | 13 12 |      | 7 6  | 5 4  | 3 2   | 1 0  |      |      |      |
| RES0 | RTNID | RTID        |      | RLNID | RLID  | RES0 | SNID | SID  | NSNID | NSID |      |      |      |

## Bits [63:28]

Reserved, RES0.

## RTNID, bits [27:26]

Root non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RTID.

## RTID, bits [25:24]

Root invasive debug.

All other values are reserved.

If FEAT\_RME is not implemented, the only permitted value is 0b00 .

| RTID   | Meaning                                                                |
|--------|------------------------------------------------------------------------|
| 0b00   | Not implemented.                                                       |
| 0b10   | Implemented and disabled. ExternalRootInvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalRootInvasiveDebugEnabled() == TRUE.   |

## Bits [23:16]

Reserved, RES0.

## RLNID, bits [15:14]

Realm non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RLID.

## RLID, bits [13:12]

Realm invasive debug.

| RLID   | Meaning                                                                 |
|--------|-------------------------------------------------------------------------|
| 0b00   | Not implemented.                                                        |
| 0b10   | Implemented and disabled. ExternalRealmInvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalRealmInvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

If FEAT\_RME is not implemented, the only permitted value is 0b00 .

## Bits [11:8]

Reserved, RES0.

## SNID, bits [7:6]

## When FEAT\_Debugv8p4 is implemented:

Secure non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.SID.

## Otherwise:

Secure non-invasive debug.

| SNID   | Meaning                                                                     |
|--------|-----------------------------------------------------------------------------|
| 0b00   | Secure state is not implemented.                                            |
| 0b10   | Implemented and disabled. ExternalSecureNoninvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalSecureNoninvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## SID, bits [5:4]

Secure invasive debug.

| SID   | Meaning                                                                  |
|-------|--------------------------------------------------------------------------|
| 0b00  | Secure state is not implemented.                                         |
| 0b10  | Implemented and disabled. ExternalSecureInvasiveDebugEnabled() == FALSE. |
| 0b11  | Implemented and enabled. ExternalSecureInvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## NSNID, bits [3:2]

## When FEAT\_Debugv8p4 is implemented:

Non-secure non-invasive debug.

| NSNID   | Meaning                                                                                |
|---------|----------------------------------------------------------------------------------------|
| 0b00    | Non-secure state is not implemented.                                                   |
| 0b11    | Implemented and enabled. EL3 is implemented or the Effective value of SCR_EL3.NS is 1. |

All other values are reserved.

## Otherwise:

Non-secure non-invasive debug.

| NSNID   | Meaning                                                               |
|---------|-----------------------------------------------------------------------|
| 0b00    | Non-secure state is not implemented.                                  |
| 0b10    | Implemented and disabled. ExternalNoninvasiveDebugEnabled() == FALSE. |
| 0b11    | Implemented and enabled. ExternalNoninvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## NSID, bits [1:0]

Non-secure invasive debug.

| NSID   | Meaning                                                            |
|--------|--------------------------------------------------------------------|
| 0b00   | Non-secure state is not implemented.                               |
| 0b10   | Implemented and disabled. ExternalInvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalInvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## Accessing DBGAUTHSTATUS\_EL1

Accesses to this register use the following encodings in the System register encoding space:

## MRS &lt;Xt&gt;, DBGAUTHSTATUS\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0111 | 0b1110 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGAUTHSTATUS_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGAUTHSTATUS_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGAUTHSTATUS_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DBGAUTHSTATUS_EL1;
```

## D24.3.2 DBGBCR&lt;n&gt;\_EL1, Debug Breakpoint Control Registers, n = 0 - 63

The DBGBCR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds control information for a breakpoint. Forms breakpoint n together with value register DBGBVR&lt;n&gt;\_EL1.

## Configuration

If breakpoint n is not implemented, accesses to this register are UNDEFINED.

AArch64 System register DBGBCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGBCR&lt;n&gt;[31:0].

AArch64 System register DBGBCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to External register DBGBCR&lt;n&gt;\_EL1[31:0].

When FEAT\_Debugv8p9 is implemented, AArch64 System register DBGBCR&lt;n&gt;\_EL1 bits [63:32] are architecturally mapped to External register DBGBCR&lt;n&gt;\_EL1[63:32].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGBCR&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

DBGBCR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

SSCE

## Bits [63:32]

Reserved, RES0.

## LBNX, bits [31:30]

## When FEAT\_Debugv8p9 is implemented:

Linked Breakpoint Number.

For Linked address matching breakpoints, with DBGBCR&lt;n&gt;\_EL1.LBN, specifies the index of the breakpoint linked to.

For all other breakpoint types, this field is ignored and reads of the register return an UNKNOWN value.

This field extends DBGBCR&lt;n&gt;\_EL1.LBN to support up to 64 implemented breakpoints.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

SSCE, bit [29]

RES0

## When FEAT\_RME is implemented:

Security State Control Extended.

The fields that indicate when the breakpoint can be generated are: HMC, PMC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MASK, bits [28:24]

## When FEAT\_BWE is implemented:

Address Mask. Only address ranges up to 2GB can be watched using a single mask.

| MASK               | Meaning                        |
|--------------------|--------------------------------|
| 0b00000            | No mask.                       |
| 0b00011 .. 0b11111 | Number of address bits masked. |

## All other values are reserved.

Indicates the number of masked address bits, from 0b00011 masking 3 address bits ( 0x00000007 mask for address) to 0b11111 masking 31 address bits ( 0x7FFFFFFF mask for address).

If any of the following apply, then the behavior of the breakpoint is CONSTRAINED UNPREDICTABLE:

- DBGBCR&lt;n&gt;\_EL1.MASK is a reserved value.
- DBGBCR&lt;n&gt;\_EL1.MASK is zero, DBGBCR&lt;n&gt;\_EL1.{BT2, BT} is {0, 0b010x } (address mismatch breakpoint without linking enabled), and AArch32 is not supported at EL1.
- DBGBCR&lt;n&gt;\_EL1.MASK is a valid nonzero value and any of the following apply:
- DBGBCR&lt;n&gt;\_EL1.BAS is not 0b1111 , and AArch32 is supported at EL0.
- DBGBVR&lt;n&gt;\_EL1[(MASK-1):0] is nonzero.
- DBGBCR&lt;n&gt;\_EL1.{BT2, BT} is {0, 0b0x1x } or {0, 0b1xxx } (Context matching breakpoint).

When any of these conditions apply, the breakpoint behaves as if one of the following:

- DBGBCR&lt;n&gt;\_EL1.MASK has been programmed with a defined value, which might be 0b00000 (no mask), other than for a direct read of DBGBCR&lt;n&gt;\_EL1.
- The breakpoint is disabled.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BT, bits [23:20]

Breakpoint Type.

With DBGBCR&lt;n&gt;\_EL1.BT2 when implemented, specifies breakpoint type.

| BT     | Meaning                                                                                                                                                                                                                                                                                                       | Applies when                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| 0b0000 | Unlinked instruction address match. DBGBVR<n>_EL1 is the address of an instruction.                                                                                                                                                                                                                           |                                                                                      |
| 0b0001 | Linked instruction address match. As 0b0000 , but linked to a breakpoint that has linking enabled.                                                                                                                                                                                                            |                                                                                      |
| 0b0010 | Unlinked Context ID match. If the Effective value of HCR_EL2.E2H is 1, and either the PE is executing at EL0 with HCR_EL2.TGE set to 1 or the PE is executing at EL2, then DBGBVR<n>_EL1.ContextID is compared against CONTEXTIDR_EL2. Otherwise, DBGBVR<n>_EL1.ContextID is compared against CONTEXTIDR_EL1. | breakpoint n is context-aware                                                        |
| 0b0011 | As 0b0010 , with linking enabled.                                                                                                                                                                                                                                                                             | breakpoint n is context-aware                                                        |
| 0b0100 | Unlinked instruction address mismatch. DBGBVR<n>_EL1 is the address of an instruction.                                                                                                                                                                                                                        | FEAT_BWE is implemented                                                              |
| 0b0101 | Linked instruction address mismatch. As 0b0100 , but linked to a breakpoint that has linking enabled.                                                                                                                                                                                                         | FEAT_BWE is implemented                                                              |
| 0b0110 | Unlinked CONTEXTIDR_EL1 match. DBGBVR<n>_EL1.ContextID is a Context ID compared against CONTEXTIDR_EL1.                                                                                                                                                                                                       | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b0111 | As 0b0110 , with linking enabled.                                                                                                                                                                                                                                                                             | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1000 | Unlinked VMIDmatch. DBGBVR<n>_EL1.VMID isaVMID compared against VTTBR_EL2.VMID.                                                                                                                                                                                                                               | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1001 | As 0b1000 , with linking enabled.                                                                                                                                                                                                                                                                             | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1010 | Unlinked VMIDand Context ID match. DBGBVR<n>_EL1.ContextID is a Context ID compared against CONTEXTIDR_EL1, and DBGBVR<n>_EL1.VMID isaVMID compared against VTTBR_EL2.VMID.                                                                                                                                   | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1011 | As 0b1010 , with linking enabled.                                                                                                                                                                                                                                                                             | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1100 | Unlinked CONTEXTIDR_EL2 match. DBGBVR<n>_EL1.ContextID2 is a Context ID compared against CONTEXTIDR_EL2.                                                                                                                                                                                                      | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1101 | As 0b1100 , with linking enabled.                                                                                                                                                                                                                                                                             | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1110 | Unlinked Full Context ID match. DBGBVR<n>_EL1.ContextID is compared against CONTEXTIDR_EL1, and DBGBVR<n>_EL1.ContextID2 is compared against CONTEXTIDR_EL2.                                                                                                                                                  | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1111 | As 0b1110 , with linking enabled.                                                                                                                                                                                                                                                                             | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |

The reset behavior of this field is:

· On a Cold reset, this field resets to an architecturally UNKNOWN value.

## LBN, bits [19:16]

Linked Breakpoint Number.

For Linked address matching breakpoints, with DBGBCR&lt;n&gt;\_EL1.LBNX when implemented, specifies the index of the breakpoint linked to.

For all other breakpoint types, this field is ignored and reads of the register return an UNKNOWN value.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## SSC, bits [15:14]

Security state control. Determines the Security states under which a Breakpoint debug event for breakpoint n is generated.

The fields that indicate when the breakpoint can be generated are: HMC, PMC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

For more information on the operation of these fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

For more information on the effect of programming the fields to a reserved set of values, see 'Reserved DBGBCR&lt;n&gt;\_EL1.{SSC, HMC, PMC} values'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## HMC,bit [13]

Higher mode control. Determines the debug perspective for deciding when a Breakpoint debug event for breakpoint n is generated.

The fields that indicate when the breakpoint can be generated are: HMC, PMC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

For more information on the operation of these fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

For more information, see DBGBCR&lt;n&gt;\_EL1.SSC.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [12:9]

Reserved, RES0.

## BAS, bits [8:5]

## When FEAT\_AA32 is implemented:

Byte address select. Defines which half-words an address-matching breakpoint matches, regardless of the instruction set and Execution state.

The permitted values depend on the breakpoint type.

For Address match breakpoints, the permitted values are:

| BAS    | Match instruction at   | Constraint for debuggers   |
|--------|------------------------|----------------------------|
| 0b0011 | DBGBVR<n>_EL1          | Use for T32 instructions.  |

| BAS    | Match instruction at   | Constraint for debuggers          |
|--------|------------------------|-----------------------------------|
| 0b1100 | DBGBVR<n>_EL1 + 2      | Use for T32 instructions.         |
| 0b1111 | DBGBVR<n>_EL1          | Use for A64 and A32 instructions. |

All other values are reserved. For more information, see 'Reserved DBGBCR&lt;n&gt;\_EL1.BAS values'.

For more information on using the BAS field in address match breakpoints, see 'Using the BAS field in Address Match breakpoints'.

For Context matching breakpoints, this field is RES1 and ignored.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## Bit [4]

Reserved, RES0.

## BT2, bit [3]

## When FEAT\_ABLE is implemented and breakpoint n supports address breakpoint linking:

Breakpoint Type 2. With DBGBCR&lt;n&gt;\_EL1.BT, specifies breakpoint type.

| BT2   | Meaning                                                                                                                                                                                     |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | As DBGBCR<n>_EL1.BT.                                                                                                                                                                        |
| 0b1   | As DBGBCR<n>_EL1.BT, but with linking enabled. This value is only defined for the following DBGBCR<n>_EL1.BT values: 0b0000 , 0b0001 , 0b0100 , and 0b0101 . All other values are reserved. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMC, bits [2:1]

Privilege mode control. Determines the Exception level or levels at which a Breakpoint debug event for breakpoint n is generated.

The fields that indicate when the breakpoint can be generated are: HMC, PMC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

For more information on the operation of these fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

For more information, see DBGBCR&lt;n&gt;\_EL1.SSC.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E, bit [0]

Enable breakpoint n.

| E   | Meaning                |
|-----|------------------------|
| 0b0 | Breakpoint n disabled. |
| 0b1 | Breakpoint n enabled.  |

This field is ignored by the PE and treated as zero when all of the following are true:

- Any of the following are true:
- HaltOnBreakpointOrWatchpoint() is FALSE and the Effective value of MDSCR\_EL1.EMBWE is 0.
- HaltOnBreakpointOrWatchpoint() is TRUE and the Effective value of EDSCR2.EHBWE is 0.
- FEAT\_Debugv8p9 is implemented.
- n &gt;= 16.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGBCR&lt;n&gt;\_EL1

When FEAT\_Debugv8p9 is implemented, a PE is permitted to support up to 64 implemented breakpoints.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, DBGBCR<m>_EL1 ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b101 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_BREAKPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16) >= ↪ → NUM_BREAKPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGBCRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18);
```

```
elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGBCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGBCR_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGBCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGBCR_EL1[m]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGBCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGBCR_EL1[m];
```

MSR DBGBCR&lt;m&gt;\_EL1, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b101 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_BREAKPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16) >= ↪ → NUM_BREAKPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGBCRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then
```

```
Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGBCR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGBCR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGBCR_EL1[m] = X[t, 64];
```

## D24.3.3 DBGBVR&lt;n&gt;\_EL1, Debug Breakpoint Value Registers, n = 0 - 63

The DBGBVR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds a virtual address, or a VMID and/or a context ID, for use in breakpoint matching. Forms breakpoint n together with control register DBGBCR&lt;n&gt;\_EL1.

## Configuration

How this register is interpreted depends on the value of DBGBCR&lt;n&gt;\_EL1.BT.

- When DBGBCR&lt;n&gt;\_EL1.BT is 0b000x , this register holds a virtual address.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b001x , 0b011x , or 0b110x , this register holds a Context ID.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b100x , this register holds a VMID.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b101x , this register holds a VMID and a Context ID.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b111x , this register holds two Context ID values.

For other values of DBGBCR&lt;n&gt;\_EL1.BT, this register is RES0.

If breakpoint n is not implemented then accesses to this register are UNDEFINED.

AArch64 System register DBGBVR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGBVR&lt;n&gt;[31:0].

AArch64 System register DBGBVR&lt;n&gt;\_EL1 bits [63:32] are architecturally mapped to AArch32 System register DBGBXVR&lt;n&gt;[31:0].

AArch64 System register DBGBVR&lt;n&gt;\_EL1 bits [63:0] are architecturally mapped to External register DBGBVR&lt;n&gt;\_EL1[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGBVR&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

DBGBVR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

When DBGBCR&lt;n&gt;\_EL1.BT IN {'000x'}:

<!-- image -->

## RESS[14:8], bits [63:57]

Reserved, Sign extended. Software must set all bits in this field to the same value as the most significant bit of the VA field. If all bits in this field are not the same value as the most significant bit of the V A field, then all of the following apply:

- It is CONSTRAINED UNPREDICTABLE whether the PE ignores this field when comparing an address.
- If the breakpoint is not context-aware, it is IMPLEMENTATION DEFINED whether the value read back in each bit of this field is a copy of the most significant bit of the V A field or the value written.

Bits [56:53]

When FEAT\_LVA3 is implemented:

## VA[56:53], bits [56:53]

Extension to VA[48:2]. For more information, see V A[48:2].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

## RESS[7:4], bits [56:53]

Extension to RESS[14:8]. For more information, see RESS[14:8].

## Bits [52:49]

## When FEAT\_LVA is implemented:

## VA[52:49], bits [52:49]

Extension to VA[48:2]. For more information, see V A[48:2].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

## RESS[3:0], bits [52:49]

Extension to RESS[14:8]. For more information, see RESS[14:8].

## VA[48:2], bits [48:2]

Bits[48:2] of the address value for comparison.

When FEAT\_LVA3 is implemented, (VA[56:53]:VA[52:49]) forms the upper part of the address value. If FEAT\_LVA3 is not implemented, bits VA[56:53] are part of the RESS field.

When FEAT\_LVA is implemented, VA[52:49] forms the upper part of the address value. If FEAT\_LVA is not implemented, bits [52:49] are part of the RESS field.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## When DBGBCR&lt;n&gt;\_EL1.BT IN {'001x'}:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ContextID, bits [31:0]

Context ID value for comparison.

The value is compared against CONTEXTIDR\_EL2 when the Effective value of HCR\_EL2.E2H is 1, and either:

- The PE is executing at EL2.
- HCR\_EL2.TGE is 1, the PE is executing at EL0, and EL2 is enabled in the current Security state.

Otherwise, the value is compared against CONTEXTIDR\_EL1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## When DBGBCR&lt;n&gt;\_EL1.BT IN {'011x'}, EL2 is implemented, and FEAT\_Debugv8p1 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ContextID, bits [31:0]

Context ID value for comparison against CONTEXTIDR\_EL1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## When DBGBCR&lt;n&gt;\_EL1.BT IN {'100x'} and EL2 is implemented:

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## VMID[15:8], bits [47:40]

## When FEAT\_VMID16 is implemented, VTCR\_EL2.VS == '1', and EL2 is using AArch64:

Extension to VMID[7:0]. For more information, see DBGBVR&lt;n&gt;\_EL1.VMID[7:0].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VMID[7:0], bits [39:32]

VMIDvalue for comparison.

The VMID is 8 bits when any of the following are true:

- EL2 is using AArch32.
- VTCR\_EL2.VS is 0.
- FEAT\_VMID16 is not implemented.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [31:0]

Reserved, RES0.

## When DBGBCR&lt;n&gt;\_EL1.BT IN {'101x'} and EL2 is implemented:

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## VMID[15:8], bits [47:40]

## When FEAT\_VMID16 is implemented, VTCR\_EL2.VS == '1', and EL2 is using AArch64:

Extension to VMID[7:0]. For more information, see DBGBVR&lt;n&gt;\_EL1.VMID[7:0].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VMID[7:0], bits [39:32]

VMIDvalue for comparison.

The VMID is 8 bits when any of the following are true:

- EL2 is using AArch32.
- VTCR\_EL2.VS is 0.
- FEAT\_VMID16 is not implemented.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## ContextID, bits [31:0]

Context ID value for comparison against CONTEXTIDR\_EL1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## When DBGBCR&lt;n&gt;\_EL1.BT IN {'110x'}, EL2 is implemented, and FEAT\_Debugv8p1 is implemented:

<!-- image -->

| 63         | 32         |
|------------|------------|
| ContextID2 | ContextID2 |
| 31         | 0          |
| RES0       | RES0       |

## ContextID2, bits [63:32]

Context ID value for comparison against CONTEXTIDR\_EL2.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [31:0]

Reserved, RES0.

When DBGBCR&lt;n&gt;\_EL1.BT IN {'111x'}, EL2 is implemented, and FEAT\_Debugv8p1 is implemented:

ContextID2

63

32

ContextID

31

0

## ContextID2, bits [63:32]

Context ID value for comparison against CONTEXTIDR\_EL2.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## ContextID, bits [31:0]

Context ID value for comparison against CONTEXTIDR\_EL1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGBVR&lt;n&gt;\_EL1

When FEAT\_Debugv8p9 is implemented, a PE is permitted to support up to 64 implemented breakpoints.

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b100 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_BREAKPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16) >= ↪ → NUM_BREAKPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGBVRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGBVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGBVR_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGBVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGBVR_EL1[m]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGBVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGBVR_EL1[m];
```

MSR DBGBVR&lt;m&gt;\_EL1, &lt;Xt&gt; ; Where m = 0-15

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b100 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_BREAKPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16) >= ↪ → NUM_BREAKPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGBVRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGBVR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGBVR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGBVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGBVR_EL1[m] = X[t, 64];
```

## D24.3.4 DBGCLAIMCLR\_EL1, Debug CLAIM Tag Clear Register

The DBGCLAIMCLR\_EL1 characteristics are:

## Purpose

Used by software to read the values of the CLAIM tag bits, and to clear CLAIM tag bits to 0.

The architecture does not define any functionality for the CLAIM tag bits.

Note

CLAIM tags are typically used for communication between the debugger and target software.

Used in conjunction with the DBGCLAIMSET\_EL1 register.

## Configuration

An implementation must include eight CLAIM tag bits.

AArch64 System register DBGCLAIMCLR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register DBGCLAIMSET\_EL1[63:0].

AArch64 System register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMCLR[31:0].

AArch64 System register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMSET[31:0].

AArch64 System register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to External register DBGCLAIMCLR\_EL1[31:0].

AArch64 System register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to External register DBGCLAIMSET\_EL1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGCLAIMCLR\_EL1 are UNDEFINED.

## Attributes

DBGCLAIMCLR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## Bits [31:8]

Reserved, RAZ/WI.

## CLAIM&lt;m&gt;, bits [m], for m = 7 to 0

Claim Tag Clear. Indicates the current status of Claim Tag bit &lt;m&gt;, and is used to clear Claim Tag bit &lt;m&gt; to 0.

| CLAIM<m>   | Meaning                                                                        |
|------------|--------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not set. On a write: Ignored.                  |
| 0b1        | On a read: Claim Tag bit <m> is set. On a write: Clear Claim tag bit <m> to 0. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is W1C.

## Accessing DBGCLAIMCLR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DBGCLAIMCLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0111 | 0b1001 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGCLAIMCLR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else
```

```
X[t, 64] = DBGCLAIMCLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DBGCLAIMCLR_EL1;
```

MSR DBGCLAIMCLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0111 | 0b1001 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGCLAIMCLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGCLAIMCLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then DBGCLAIMCLR_EL1 = X[t, 64];
```

## D24.3.5 DBGCLAIMSET\_EL1, Debug CLAIM Tag Set Register

The DBGCLAIMSET\_EL1 characteristics are:

## Purpose

Used by software to set the CLAIM tag bits to 1.

The architecture does not define any functionality for the CLAIM tag bits.

Note

CLAIM tags are typically used for communication between the debugger and target software.

Used in conjunction with the DBGCLAIMCLR\_EL1 register.

## Configuration

An implementation must include eight CLAIM tag bits.

AArch64 System register DBGCLAIMSET\_EL1 bits [63:0] are architecturally mapped to AArch64 System register DBGCLAIMCLR\_EL1[63:0].

AArch64 System register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMSET[31:0].

AArch64 System register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMCLR[31:0].

AArch64 System register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to External register DBGCLAIMSET\_EL1[31:0].

AArch64 System register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to External register DBGCLAIMCLR\_EL1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGCLAIMSET\_EL1 are UNDEFINED.

## Attributes

DBGCLAIMSET\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## Bits [31:8]

Reserved, RAZ/WI.

## CLAIM&lt;m&gt;, bits [m], for m = 7 to 0

Claim Tag Set. Used to set Claim Tag bit &lt;m&gt; to 1.

| CLAIM<m>   | Meaning                                 |
|------------|-----------------------------------------|
| 0b0        | On a write: Ignored.                    |
| 0b1        | On a write: Set Claim Tag bit <m> to 1. |

Access to this field is RAO/W1S.

## Accessing DBGCLAIMSET\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DBGCLAIMSET\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0111 | 0b1000 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGCLAIMSET_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGCLAIMSET_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DBGCLAIMSET_EL1;
```

MSR DBGCLAIMSET\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0111 | 0b1000 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGCLAIM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGCLAIMSET_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGCLAIMSET_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then DBGCLAIMSET_EL1 = X[t, 64];
```

## D24.3.6 DBGDTR\_EL0, Debug Data Transfer Register, half-duplex

The DBGDTR\_EL0 characteristics are:

## Purpose

Transfers 64 bits of data between the PE and an external debugger. Can transfer both ways using only a single register.

## Configuration

When written, AArch64 System register DBGDTR\_EL0 bits [63:32] are architecturally mapped to AArch32 System register DBGDTRRXint[31:0].

When written, AArch64 System register DBGDTR\_EL0 bits [63:32] are architecturally mapped to External register DBGDTRRX\_EL0[31:0].

When written, AArch64 System register DBGDTR\_EL0 bits [63:32] are architecturally mapped to AArch64 System register DBGDTRRX\_EL0[31:0].

When written, AArch64 System register DBGDTR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRTXint[31:0].

When written, AArch64 System register DBGDTR\_EL0 bits [31:0] are architecturally mapped to External register DBGDTRTX\_EL0[31:0].

When written, AArch64 System register DBGDTR\_EL0 bits [31:0] are architecturally mapped to AArch64 System register DBGDTRTX\_EL0[31:0].

When read, AArch64 System register DBGDTR\_EL0 bits [63:32] are architecturally mapped to AArch32 System register DBGDTRTXint[31:0].

When read, AArch64 System register DBGDTR\_EL0 bits [63:32] are architecturally mapped to External register DBGDTRTX\_EL0[31:0].

When read, AArch64 System register DBGDTR\_EL0 bits [63:32] are architecturally mapped to AArch64 System register DBGDTRTX\_EL0[31:0].

When read, AArch64 System register DBGDTR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRRXint[31:0].

When read, AArch64 System register DBGDTR\_EL0 bits [31:0] are architecturally mapped to External register DBGDTRRX\_EL0[31:0].

When read, AArch64 System register DBGDTR\_EL0 bits [31:0] are architecturally mapped to AArch64 System register DBGDTRRX\_EL0[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGDTR\_EL0 are UNDEFINED.

## Attributes

DBGDTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

HighWord, bits [63:32]

Writes to this register set DTRRX to the value in this field and do not change RXfull.

Reads of this register:

- If RXfull is 1, return the last value written to DTRTX.
- If RXfull is 0, return an UNKNOWN value.

After the read, RXfull is cleared to 0.

## LowWord, bits [31:0]

Writes to this register set DTRTX to the value in this field and set TXfull to 1.

Reads of this register:

- If RXfull is 1, return the last value written to DTRRX.
- If RXfull is 0, return an UNKNOWN value.

After the read, RXfull is cleared to 0.

## Accessing DBGDTR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, DBGDTR_EL0
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b0000 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif Halted() then X[t, 64] = Read_DBGDTR_EL0(64); elsif PSTATE.EL == EL0 then if MDSCR_EL1.TDCC == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = Read_DBGDTR_EL0(64); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = Read_DBGDTR_EL0(64); elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = Read_DBGDTR_EL0(64); elsif PSTATE.EL == EL3 then X[t, 64] = Read_DBGDTR_EL0(64);
```

MSR DBGDTR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b0000 | 0b0100 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif Halted() then Write_DBGDTR_EL0(X[t, 64]); elsif PSTATE.EL == EL0 then if MDSCR_EL1.TDCC == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else Write_DBGDTR_EL0(X[t, 64]); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else Write_DBGDTR_EL0(X[t, 64]); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else Write_DBGDTR_EL0(X[t, 64]); elsif PSTATE.EL == EL3 then Write_DBGDTR_EL0(X[t, 64]);
```

## D24.3.7 DBGDTRRX\_EL0, Debug Data Transfer Register, Receive

The DBGDTRRX\_EL0 characteristics are:

## Purpose

Transfers data from an external debugger to the PE. For example, it is used by a debugger transferring commands and data to a debug target. See DBGDTR\_EL0 for additional architectural mappings. It is a component of the Debug Communications Channel.

## Configuration

AArch64 System register DBGDTRRX\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRRXint[31:0].

AArch64 System register DBGDTRRX\_EL0 bits [31:0] are architecturally mapped to External register DBGDTRRX\_EL0[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGDTRRX\_EL0 are UNDEFINED.

## Attributes

DBGDTRRX\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## DTRRX, bits [31:0]

DTRRX. Reads of this register:

- If RXfull is 1, return the last value written to DTRRX.
- If RXfull is 0, return an UNKNOWN value.

After the read, RXfull is cleared to 0.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRRX\_EL0

Accesses to this register use the following encodings in the System register encoding space:

## MRS &lt;Xt&gt;, DBGDTRRX\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b0000 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif Halted() then X[t, 32] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL0 then if MDSCR_EL1.TDCC == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 32] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 32] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 32] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL3 then X[t, 32] = Read_DBGDTR_EL0(32);
```

## D24.3.8 DBGDTRTX\_EL0, Debug Data Transfer Register, Transmit

The DBGDTRTX\_EL0 characteristics are:

## Purpose

Transfers data from the PE to an external debugger. For example, it is used by a debug target to transfer data to the debugger. See DBGDTR\_EL0 for additional architectural mappings. It is a component of the Debug Communication Channel.

## Configuration

AArch64 System register DBGDTRTX\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRTXint[31:0].

AArch64 System register DBGDTRTX\_EL0 bits [31:0] are architecturally mapped to External register DBGDTRTX\_EL0[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGDTRTX\_EL0 are UNDEFINED.

## Attributes

DBGDTRTX\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## DTRTX, bits [31:0]

DTRTX. Writes to this register:

- If TXfull is 1, DTRTX is set to an UNKNOWN value.
- If TXfull is 0, update the value in DTRTX.

After the write, TXfull is set to 1.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRTX\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MSR DBGDTRTX\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b0000 | 0b0101 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif Halted() then Write_DBGDTR_EL0(X[t, 32]); elsif PSTATE.EL == EL0 then if MDSCR_EL1.TDCC == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else Write_DBGDTR_EL0(X[t, 32]); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else Write_DBGDTR_EL0(X[t, 32]); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else Write_DBGDTR_EL0(X[t, 32]); elsif PSTATE.EL == EL3 then Write_DBGDTR_EL0(X[t, 32]);
```

## D24.3.9 DBGPRCR\_EL1, Debug Power Control Register

The DBGPRCR\_EL1 characteristics are:

## Purpose

Controls behavior of the PE on powerdown request.

## Configuration

AArch64 System register DBGPRCR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGPRCR[31:0].

AArch64 System register DBGPRCR\_EL1 bit [0] is architecturally mapped to External register EDPRCR[0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGPRCR\_EL1 are UNDEFINED.

## Attributes

DBGPRCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:1]

Reserved, RES0.

## CORENPDRQ,bit [0]

## When FEAT\_DoPD is implemented:

Core no powerdown request. Requests emulation of powerdown.

This request is typically passed to an external power controller. This means that whether a request causes power up is dependent on the IMPLEMENTATION DEFINED nature of the system. The power controller must not allow the Core power domain to switch off while this bit is 1.

| CORENPDRQ   | Meaning                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If the system responds to a powerdown request, it powers down Core power domain.                                                             |
| 0b1         | If the system responds to a powerdown request, it does not powerdown the Core power domain, but instead emulates a powerdown of that domain. |

In an implementation that includes the recommended external debug interface, this bit drives the DBGNOPWRDWN signal.

It is IMPLEMENTATION DEFINED whether this bit is reset to its Cold reset value on exit from an IMPLEMENTATION DEFINED software-visible retention state. For more information about retention states see 'Core power domain power states'.

Note

Writes to this bit are not prohibited by the IMPLEMENTATION DEFINED authentication interface. This means that a debugger can request emulation of powerdown regardless of whether invasive debug is permitted.

On a Cold reset, if the powerup request is implemented and the powerup request has been asserted, this field is set to an IMPLEMENTATION DEFINED choice of 0 or 1. If the powerup request is not asserted, this field is set to 0.

## Otherwise:

Core no powerdown request. Requests emulation of powerdown.

This request is typically passed to an external power controller. This means that whether a request causes power up is dependent on the IMPLEMENTATION DEFINED nature of the system. The power controller must not allow the Core power domain to switch off while this bit is 1.

| CORENPDRQ   | Meaning                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If the system responds to a powerdown request, it powers down Core power domain.                                                             |
| 0b1         | If the system responds to a powerdown request, it does not powerdown the Core power domain, but instead emulates a powerdown of that domain. |

In an implementation that includes the recommended external debug interface, this bit drives the DBGNOPWRDWN signal.

It is IMPLEMENTATION DEFINED whether this bit is reset to the value of EDPRCR.COREPURQ on exit from an IMPLEMENTATION DEFINED software-visible retention state. For more information about retention states see 'Core power domain power states'.

Note

Writes to this bit are not prohibited by the IMPLEMENTATION DEFINED authentication interface. This means that a debugger can request emulation of powerdown regardless of whether invasive debug is permitted.

The reset behavior of this field is:

- On a Cold reset, this field resets to the value in EDPRCR.COREPURQ.

## Accessing DBGPRCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DBGPRCR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0100 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGPRCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGPRCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGPRCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = DBGPRCR_EL1;
```

MSR DBGPRCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0100 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGPRCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGPRCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGPRCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then DBGPRCR_EL1 = X[t, 64];
```

## D24.3.10 DBGVCR32\_EL2, Debug Vector Catch Register

The DBGVCR32\_EL2 characteristics are:

## Purpose

Allows access to the AArch32 register DBGVCR from AArch64 state only. Its value has no effect on execution in AArch64 state.

## Configuration

If EL2 is not implemented but EL3 is implemented, and EL1 is capable of using AArch32, then this register is not RES0.

AArch64 System register DBGVCR32\_EL2 bits [31:0] are architecturally mapped to AArch32 System register DBGVCR[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGVCR32\_EL2 are UNDEFINED.

## Attributes

DBGVCR32\_EL2 is a 64-bit register.

## Field descriptions

When EL3 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NSF, bit [31]

FIQ vector catch enable in Non-secure state.

The exception vector offset is 0x1C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSI, bit [30]

IRQ vector catch enable in Non-secure state.

The exception vector offset is 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [29]

Reserved, RES0.

## NSD, bit [28]

Data Abort exception vector catch enable in Non-secure state.

The exception vector offset is 0x10 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSP, bit [27]

Prefetch Abort vector catch enable in Non-secure state.

The exception vector offset is 0x0C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSS, bit [26]

Supervisor Call (SVC) vector catch enable in Non-secure state.

The exception vector offset is 0x08 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NSU, bit [25]

Undefined Instruction vector catch enable in Non-secure state.

The exception vector offset is 0x04 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [24:8]

Reserved, RES0.

## SF, bit [7]

FIQ vector catch enable in Secure state.

The exception vector offset is 0x1C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SI, bit [6]

IRQ vector catch enable in Secure state.

The exception vector offset is 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## SD, bit [4]

Data Abort exception vector catch enable in Secure state.

The exception vector offset is 0x10 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SP, bit [3]

Prefetch Abort vector catch enable in Secure state.

The exception vector offset is 0x0C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SS, bit [2]

Supervisor Call (SVC) vector catch enable in Secure state.

The exception vector offset is 0x08 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SU, bit [1]

Undefined Instruction vector catch enable in Secure state.

The exception vector offset is 0x04 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [0]

Reserved, RES0.

## When EL3 is not implemented:

<!-- image -->

## Bits [63:8]

Reserved, RES0.

## F, bit [7]

FIQ vector catch enable.

The exception vector offset is 0x1C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [6]

IRQ vector catch enable.

The exception vector offset is 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## D, bit [4]

Data Abort exception vector catch enable.

The exception vector offset is 0x10 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## P, bit [3]

Prefetch Abort vector catch enable.

The exception vector offset 0x0C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S, bit [2]

Supervisor Call (SVC) vector catch enable.

The exception vector offset is 0x08 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## U, bit [1]

Undefined Instruction vector catch enable.

The exception vector offset is 0x04 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [0]

Reserved, RES0.

## Accessing DBGVCR32\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DBGVCR32\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b100 | 0b0000 | 0b0111 | 0b000 |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && UNDEFINED; elsif !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = DBGVCR32_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = DBGVCR32_EL2;
```

MSR DBGVCR32\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b100 | 0b0000 | 0b0111 | 0b000 |

```
IsFeatureImplemented(FEAT_AA64)) then
```

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && UNDEFINED; elsif !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else DBGVCR32_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then DBGVCR32_EL2 = X[t, 64];
```

## D24.3.11 DBGWCR&lt;n&gt;\_EL1, Debug Watchpoint Control Registers, n = 0 - 63

The DBGWCR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds control information for a watchpoint. Forms watchpoint n together with value register DBGWVR&lt;n&gt;\_EL1.

## Configuration

If watchpoint n is not implemented then accesses to this register are UNDEFINED.

AArch64 System register DBGWCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGWCR&lt;n&gt;[31:0].

AArch64 System register DBGWCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to External register DBGWCR&lt;n&gt;\_EL1[31:0].

When FEAT\_Debugv8p9 is implemented, AArch64 System register DBGWCR&lt;n&gt;\_EL1 bits [63:32] are architecturally mapped to External register DBGWCR&lt;n&gt;\_EL1[63:32].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGWCR&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

DBGWCR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## LBNX, bits [31:30]

## When FEAT\_Debugv8p9 is implemented:

Linked Breakpoint Number.

For Linked data address watchpoints, with DBGWCR&lt;n&gt;\_EL1.LBN, specifies the index of the breakpoint linked to.

For all other watchpoint types, this field is ignored and reads of the register return an UNKNOWN value.

This field extends DBGWCR&lt;n&gt;\_EL1.LBN to support up to 64 implemented breakpoints.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

SSCE, bit [29]

## When FEAT\_RME is implemented:

Security State Control Extended.

The fields that indicate when the watchpoint can be generated are: HMC, PAC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MASK, bits [28:24]

Address Mask. Only address ranges up to 2GB can be watched using a single mask.

| MASK               | Meaning                        |
|--------------------|--------------------------------|
| 0b00000            | No mask.                       |
| 0b00011 .. 0b11111 | Number of address bits masked. |

## All other values are reserved.

Indicates the number of masked address bits, from 0b00011 masking 3 address bits ( 0x00000007 mask for address) to 0b11111 masking 31 address bits ( 0x7FFFFFFF mask for address).

If programmed with a reserved value, the watchpoint behaves as if one of the following:

- DBGWCR&lt;n&gt;\_EL1.MASK has been programmed with a defined value, which might be 0b00000 (no mask), other than for a direct read of DBGWCR&lt;n&gt;\_EL1.
- The watchpoint is disabled.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bit [23]

Reserved, RES0.

## WT2, bit [22]

## When FEAT\_BWE2 is implemented:

Watchpoint Type 2. With DBGWCR&lt;n&gt;\_EL1.WT, specifies watchpoint type.

| WT2   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Watchpoint n is an address match watchpoint.    |
| 0b1   | Watchpoint n is an address mismatch watchpoint. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [21]

Reserved, RES0.

## WT, bit [20]

Watchpoint type. Possible values are:

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## LBN, bits [19:16]

Linked Breakpoint Number.

For Linked data address watchpoints, with DBGWCR&lt;n&gt;\_EL1.LBNX when implemented, specifies the index of the breakpoint linked to.

For all other watchpoint types, this field is ignored and reads of the register return an UNKNOWN value.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## SSC, bits [15:14]

Security state control. Determines the Security states under which a Watchpoint debug event for watchpoint n is generated.

The fields that indicate when the watchpoint can be generated are: HMC, PAC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

For more information on the operation of these fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

For more information on the effect of programming the fields to a reserved value, see 'Reserved DBGWCR&lt;n&gt;\_EL1.{SSC, HMC, PAC} values'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## HMC,bit [13]

Higher mode control. Determines the debug perspective for deciding when a Watchpoint debug event for watchpoint n is generated.

The fields that indicate when the watchpoint can be generated are: HMC, PAC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

For more information on the operation of these fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

The reset behavior of this field is:

| WT   | Meaning              |
|------|----------------------|
| 0b0  | Unlinked watchpoint. |
| 0b1  | Linked watchpoint.   |

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## BAS, bits [12:5]

Byte address select. Each bit of this field selects whether a byte from within the word or double-word addressed by DBGWVR&lt;n&gt;\_EL1 is being watched.

| BAS      | Description                     |
|----------|---------------------------------|
| xxxxxxx1 | Match byte at DBGWVR<n>_EL1     |
| xxxxxx1x | Match byte at DBGWVR<n>_EL1 + 1 |
| xxxxx1xx | Match byte at DBGWVR<n>_EL1 + 2 |
| xxxx1xxx | Match byte at DBGWVR<n>_EL1 + 3 |

In cases where DBGWVR&lt;n&gt;\_EL1 addresses a double-word:

| BAS      | Description, if DBGWVR<n>_EL1[2] == 0   |
|----------|-----------------------------------------|
| xxx1xxxx | Match byte at DBGWVR<n>_EL1 + 4         |
| xx1xxxxx | Match byte at DBGWVR<n>_EL1 + 5         |
| x1xxxxxx | Match byte at DBGWVR<n>_EL1 + 6         |
| 1xxxxxxx | Match byte at DBGWVR<n>_EL1 + 7         |

If DBGWVR&lt;n&gt;\_EL1[2] == 1, only BAS[3:0] are used and BAS[7:4] are ignored. Arm deprecates setting DBGWVR&lt;n&gt;\_EL1[2] == 1.

The valid values for BAS are nonzero binary numbers all of whose set bits are contiguous. All other values are reserved and must not be used by software. See 'Reserved DBGWCR&lt;n&gt;\_EL1.BAS values'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## LSC, bits [4:3]

Load/store control. This field enables watchpoint matching on the type of access being made. Possible values of this field are:

| LSC   | Meaning                                                               |
|-------|-----------------------------------------------------------------------|
| 0b01  | Match instructions that load from a watchpointed address.             |
| 0b10  | Match instructions that store to a watchpointed address.              |
| 0b11  | Match instructions that load from or store to a watchpointed address. |

All other values are reserved, but must behave as if the watchpoint is disabled. Software must not rely on this property as the behavior of reserved values might change in a future revision of the architecture.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## PAC, bits [2:1]

Privilege of access control. Determines the Exception level or levels at which a Watchpoint debug event for watchpoint n is generated.

The fields that indicate when the watchpoint can be generated are: HMC, PAC, SSC, and SSCE. These fields must be considered in combination, and the values that are permitted for these fields are constrained.

For more information on the operation of these fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E, bit [0]

Enable watchpoint n.

| E   | Meaning                |
|-----|------------------------|
| 0b0 | Watchpoint n disabled. |
| 0b1 | Watchpoint n enabled.  |

This field is ignored by the PE and treated as zero when all of the following are true:

- Any of the following are true:
- HaltOnBreakpointOrWatchpoint() is FALSE and the Effective value of MDSCR\_EL1.EMBWE is 0.
- HaltOnBreakpointOrWatchpoint() is TRUE and the Effective value of EDSCR2.EHBWE is 0.
- FEAT\_Debugv8p9 is implemented.
- n &gt;= 16.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGWCR&lt;n&gt;\_EL1

When FEAT\_Debugv8p9 is implemented, a PE is permitted to support up to 64 implemented watchpoints.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, DBGWCR<m>_EL1 ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b111 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_WATCHPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(MDSELR_EL1.BANK) * 16) >= NUM_WATCHPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGWCRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGWCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGWCR_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGWCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGWCR_EL1[m]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGWCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGWCR_EL1[m];
```

```
MSR DBGWCR<m>_EL1, <Xt> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b111 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_WATCHPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(MDSELR_EL1.BANK) * 16) >= NUM_WATCHPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGWCRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGWCR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGWCR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWCR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGWCR_EL1[m] = X[t, 64];
```

## D24.3.12 DBGWVR&lt;n&gt;\_EL1, Debug Watchpoint Value Registers, n = 0 - 63

The DBGWVR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds a data address value for use in watchpoint matching. Forms watchpoint n together with control register DBGWCR&lt;n&gt;\_EL1.

## Configuration

If watchpoint n is not implemented then accesses to this register are UNDEFINED.

AArch64 System register DBGWVR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGWVR&lt;n&gt;[31:0].

AArch64 System register DBGWVR&lt;n&gt;\_EL1 bits [63:0] are architecturally mapped to External register DBGWVR&lt;n&gt;\_EL1[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DBGWVR&lt;n&gt;\_EL1 are UNDEFINED.

## Attributes

DBGWVR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## RESS[14:8], bits [63:57]

Reserved, Sign extended. Software must set all bits in this field to the same value as the most significant bit of the VA field. If all bits in this field are not the same value as the most significant bit of the V A field, then all of the following apply:

- It is CONSTRAINED UNPREDICTABLE whether the PE ignores this field when comparing an address.
- It is IMPLEMENTATION DEFINED whether the value read back in each bit of this field is a copy of the most significant bit of the V A field or the value written.

## Bits [56:53]

## When FEAT\_LVA3 is implemented:

## VA[56:53], bits [56:53]

Extension to VA[48:2]. For more information, see V A[48:2].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

## RESS[7:4], bits [56:53]

Extension to RESS[14:8]. For more information, see RESS[14:8].

## Bits [52:49]

## When FEAT\_LVA is implemented:

## VA[52:49], bits [52:49]

Extension to VA[48:2]. For more information, see V A[48:2].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

## RESS[3:0], bits [52:49]

Extension to RESS[14:8]. For more information, see RESS[14:8].

## VA[48:2], bits [48:2]

Bits[48:2] of the address value for comparison.

When FEAT\_LVA3 is implemented, (VA[56:53]:VA[52:49]) forms the upper part of the address value. If FEAT\_LVA3 is not implemented, bits VA[56:53] are part of the RESS field.

When FEAT\_LVA is implemented, VA[52:49] forms the upper part of the address value. If FEAT\_LVA is not implemented, bits [52:49] are part of the RESS field.

Arm deprecates setting DBGWVR&lt;n&gt;\_EL1[2] == 1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## Accessing DBGWVR&lt;n&gt;\_EL1

When FEAT\_Debugv8p9 is implemented, a PE is permitted to support up to 64 implemented watchpoints.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DBGWVR&lt;m&gt;\_EL1 ; Where m = 0-15

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b110 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_WATCHPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(MDSELR_EL1.BANK) * 16) >= NUM_WATCHPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.DBGWVRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGWVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGWVR_EL1[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGWVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGWVR_EL1[m]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then X[t, 64] = DBGWVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)]; else X[t, 64] = DBGWVR_EL1[m];
```

```
MSR DBGWVR<m>_EL1, <Xt> ; Where m = 0-15
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | m[3:0] | 0b110 |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif (!IsFeatureImplemented(FEAT_Debugv8p9) && m >= NUM_WATCHPOINTS) || ↪ → (IsFeatureImplemented(FEAT_Debugv8p9) && m + (UInt(MDSELR_EL1.BANK) * 16) >= NUM_WATCHPOINTS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.DBGWVRn_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGWVR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGWVR_EL1[m] = X[t, 64]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else if IsFeatureImplemented(FEAT_Debugv8p9) then DBGWVR_EL1[m + (UInt(EffectiveMDSELR_EL1_BANK()) * 16)] = X[t, 64]; else DBGWVR_EL1[m] = X[t, 64];
```

## D24.3.13 DLR\_EL0, Debug Link Register

The DLR\_EL0 characteristics are:

## Purpose

In Debug state, holds the address to restart from.

## Configuration

AArch64 System register DLR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DLR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DLR\_EL0 are UNDEFINED.

## Attributes

DLR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63              | 32   |
|-----------------|------|
|                 | 0    |
| 31              |      |
| Restart address |      |

## ADDR, bits [63:0]

Restart address.

## Accessing DLR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0101 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif !Halted() then UNDEFINED; else X[t, 64] = DLR_EL0;
```

MSR DLR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0101 | 0b001 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED;

elsif

!Halted() then

UNDEFINED;

else

DLR\_EL0 = X[t, 64];

## D24.3.14 DSPSR\_EL0, Debug Saved Program Status Register

The DSPSR\_EL0 characteristics are:

## Purpose

Holds the saved process state for Debug state. On entering Debug state, PSTATE information is written to this register. On exiting Debug state, values are copied from this register to PSTATE.

## Configuration

AArch64 System register DSPSR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DSPSR[31:0].

When FEAT\_Debugv8p9 is implemented, AArch64 System register DSPSR\_EL0 bits [63:32] are architecturally mapped to AArch32 System register DSPSR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to DSPSR\_EL0 are UNDEFINED.

## Attributes

DSPSR\_EL0 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented and exiting Debug state to AArch32 state:

<!-- image -->

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Copied to PSTATE.UINJ on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [35:34]

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Copied to PSTATE.PPEND on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [32]

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Copied to PSTATE.N on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Copied to PSTATE.Z on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Copied to PSTATE.C on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Copied to PSTATE.V on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Q, bit [27]

Overflow or saturation flag. Copied to PSTATE.Q on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Copied to PSTATE.IT on exiting Debug state.

On exiting Debug state, DSPSR\_EL0.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Copied to PSTATE.DIT on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Copied to PSTATE.SSBS on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Copied to PSTATE.PAN on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Copied to PSTATE.SS on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Copied to PSTATE.IL on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## GE, bits [19:16]

Greater than or Equal flags. Copied to PSTATE.GE on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Copied to PSTATE.E on exiting Debug state.

If the implementation does not support big-endian operation, DSPSR\_EL0.E is RES0. If the implementation does not support little-endian operation, DSPSR\_EL0.E is RES1. On exiting Debug state, if the implementation does not

support big-endian operation at the Exception level being returned to, DSPSR\_EL0.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, DSPSR\_EL0.E is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Copied to PSTATE.A on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Copied to PSTATE.I on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Copied to PSTATE.F on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## T, bit [5]

T32 Instruction set state. Copied to PSTATE.T on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4], bit [4]

Execution state. Copied to PSTATE.nRW on exiting Debug state.

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b1    | AArch32 execution state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch32 Mode. Copied to PSTATE.M[3:0] on exiting Debug state.

| M[3:0]   | Meaning   | Applies when   |
|----------|-----------|----------------|
| 0b0000   | User.     |                |

| M[3:0]   | Meaning     | Applies when            |
|----------|-------------|-------------------------|
| 0b0001   | FIQ.        |                         |
| 0b0010   | IRQ.        |                         |
| 0b0011   | Supervisor. |                         |
| 0b0110   | Monitor.    | FEAT_EL3 is implemented |
| 0b0111   | Abort.      |                         |
| 0b1010   | Hyp.        |                         |
| 0b1011   | Undefined.  |                         |
| 0b1111   | System.     |                         |

Other values are reserved. If DSPSR\_EL0.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, exiting Debug state is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_AA64 is implemented and entering or exiting Debug state from or to AArch64 state:

<!-- image -->

## Bits [63:37]

Reserved, RES0.

## UINJ, bit [36]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to the value of PSTATE.UINJ on entering Debug state, and copied to PSTATE.UINJ on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PACM, bit [35]

## When FEAT\_PAuth\_LR is implemented:

PACM. Set to the value of PSTATE.PACM on entering Debug state, and copied to PSTATE.PACM on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLOCK, bit [34]

## When FEAT\_GCS is implemented:

Exception return state lock. Set to the value of PSTATE.EXLOCK on entering Debug state, and copied to PSTATE.EXLOCK on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PPEND, bit [33]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on entering Debug state, and conditionally copied to PSTATE.PPEND on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PM, bit [32]

## When FEAT\_EBEP is implemented:

Profiling exception mask bit. Set to the value of PSTATE.PM on entering Debug state, and copied to PSTATE.PM on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## N, bit [31]

Negative Condition flag. Set to the value of PSTATE.N on entering Debug state, and copied to PSTATE.N on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Z, bit [30]

Zero Condition flag. Set to the value of PSTATE.Z on entering Debug state, and copied to PSTATE.Z on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [29]

Carry Condition flag. Set to the value of PSTATE.C on entering Debug state, and copied to PSTATE.C on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## V, bit [28]

Overflow Condition flag. Set to the value of PSTATE.V on entering Debug state, and copied to PSTATE.V on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:26]

Reserved, RES0.

## TCO, bit [25]

## When FEAT\_MTE is implemented:

Tag Check Override. Set to the value of PSTATE.TCO on entering Debug state, and copied to PSTATE.TCO on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on entering Debug state, and copied to PSTATE.DIT on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UAO, bit [23]

## When FEAT\_UAO is implemented:

User Access Override. Set to the value of PSTATE.UAO on entering Debug state, and copied to PSTATE.UAO on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PAN, bit [22]

## When FEAT\_PAN is implemented:

Privileged Access Never. Set to the value of PSTATE.PAN on entering Debug state, and copied to PSTATE.PAN on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SS, bit [21]

Software Step. Set to the value of PSTATE.SS on entering Debug state, and conditionally copied to PSTATE.SS on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IL, bit [20]

Illegal Execution state. Set to the value of PSTATE.IL on entering Debug state, and copied to PSTATE.IL on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:14]

Reserved, RES0.

## ALLINT, bit [13]

## When FEAT\_NMI is implemented:

All IRQ or FIQ interrupts mask. Set to the value of PSTATE.ALLINT on entering Debug state, and copied to PSTATE.ALLINT on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [12]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on entering Debug state, and copied to PSTATE.SSBS on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BTYPE, bits [11:10]

When FEAT\_BTI is implemented:

Branch Type Indicator. Set to the value of PSTATE.BTYPE on entering Debug state, and copied to PSTATE.BTYPE on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## D, bit [9]

Debug exception mask. Set to the value of PSTATE.D on entering Debug state, and copied to PSTATE.D on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## A, bit [8]

SError exception mask. Set to the value of PSTATE.A on entering Debug state, and copied to PSTATE.A on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## I, bit [7]

IRQ interrupt mask. Set to the value of PSTATE.I on entering Debug state, and copied to PSTATE.I on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## F, bit [6]

FIQ interrupt mask. Set to the value of PSTATE.F on entering Debug state, and copied to PSTATE.F on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [5]

Reserved, RES0.

## M[4], bit [4]

Execution state. Set to 0b0 , the value of PSTATE.nRW, on entering Debug state from AArch64 state, and copied to PSTATE.nRW on exiting Debug state.

| M[4]   | Meaning                  |
|--------|--------------------------|
| 0b0    | AArch64 execution state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[3:0], bits [3:0]

AArch64 Exception level and selected Stack Pointer.

| M[3:0]   | Meaning                 | Applies when            |
|----------|-------------------------|-------------------------|
| 0b0000   | EL0.                    |                         |
| 0b0100   | EL1 with SP_EL0 (EL1t). |                         |
| 0b0101   | EL1 with SP_EL1 (EL1h). |                         |
| 0b1000   | EL2 with SP_EL0 (EL2t). |                         |
| 0b1001   | EL2 with SP_EL2 (EL2h). |                         |
| 0b1100   | EL3 with SP_EL0 (EL3t). | FEAT_EL3 is implemented |
| 0b1101   | EL3 with SP_EL3 (EL3h). | FEAT_EL3 is implemented |

Other values are reserved. If DSPSR\_EL0.M[3:0] has a Reserved value, or a value for an unimplemented Exception level, exiting Debug state is an illegal return event, as described in 'Illegal return events from AArch64 state'.

The bits in this field are interpreted as follows:

- M[3:2] is set to the value of PSTATE.EL on entering Debug state and copied to PSTATE.EL on exiting Debug state.
- M[1] is unused and is 0 for all non-reserved values.
- M[0] is set to the value of PSTATE.SP on entering Debug state and copied to PSTATE.SP on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DSPSR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0101 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

```
UNDEFINED; elsif !Halted() then UNDEFINED; else X[t, 64] = DSPSR_EL0;
```

MSR DSPSR\_EL0, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0100 | 0b0101 | 0b000 |

if !IsFeatureImplemented(FEAT\_AA64) then

UNDEFINED; elsif !Halted() then UNDEFINED; else DSPSR\_EL0 = X[t, 64];

## D24.3.15 MDCCINT\_EL1, Monitor DCC Interrupt Enable Register

The MDCCINT\_EL1 characteristics are:

## Purpose

Enables interrupt requests to be signaled based on the DCC status flags.

## Configuration

AArch64 System register MDCCINT\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGDCCINT[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MDCCINT\_EL1 are UNDEFINED.

## Attributes

MDCCINT\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:31]

Reserved, RES0.

## RX, bit [30]

DCCinterrupt request enable control for DTRRX. Enables a common COMMIRQ interrupt request to be signaled based on the DCC status flags.

| RX   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | No interrupt request generated by DTRRX.            |
| 0b1  | Interrupt request will be generated on RXfull == 1. |

If legacy COMMRX and COMMTX signals are implemented, then these are not affected by the value of this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## TX, bit [29]

DCCinterrupt request enable control for DTRTX. Enables a common COMMIRQ interrupt request to be signaled based on the DCC status flags.

| TX   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | No interrupt request generated by DTRTX.            |
| 0b1  | Interrupt request will be generated on TXfull == 0. |

If legacy COMMRX and COMMTX signals are implemented, then these are not affected by the value of this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [28:0]

Reserved, RES0.

## Accessing MDCCINT\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MDCCINT_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then X[t, 64] = MDCCINT_EL1; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDCCINT_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDCCINT_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MDCCINT_EL1;
```

MSR MDCCINT\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then MDCCINT_EL1 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MDCCINT_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MDCCINT_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MDCCINT_EL1 = X[t, 64];
```

## D24.3.16 MDCCSR\_EL0, Monitor DCC Status Register

The MDCCSR\_EL0 characteristics are:

## Purpose

Read-only register containing control status flags for the DCC.

## Configuration

AArch64 System register MDCCSR\_EL0 bits [30:29] are architecturally mapped to External register EDSCR[30:29].

AArch64 System register MDCCSR\_EL0 bits [30:29] are architecturally mapped to AArch32 System register DBGDSCRint[30:29].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MDCCSR\_EL0 are UNDEFINED.

## Attributes

MDCCSR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:31]

Reserved, RES0.

## RXfull, bit [30]

DTRRXfull. Read-only view of the equivalent bit in the EDSCR.

## TXfull, bit [29]

DTRTX full. Read-only view of the equivalent bit in the EDSCR.

## Bits [28:19]

Reserved, RES0.

## Bits [18:15]

Reserved, RAZ.

## Bits [14:13]

Reserved, RES0.

## Bit [12]

Reserved, RAZ.

## Bits [11:6]

Reserved, RES0.

## Bits [5:2]

Reserved, RAZ.

## Bits [1:0]

Reserved, RES0.

## Accessing MDCCSR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MDCCSR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b011 | 0b0000 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then X[t, 64] = MDCCSR_EL0; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif MDSCR_EL1.TDCC == '1' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && (HCR_EL2.TGE == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDCCSR_EL0; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then
```

```
AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDCCSR_EL0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDCCSR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = MDCCSR_EL0;
```

## D24.3.17 MDCR\_EL2, Monitor Debug Configuration Register (EL2)

The MDCR\_EL2 characteristics are:

## Purpose

Provides EL2 configuration options for self-hosted debug and the Performance Monitors Extension.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register MDCR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HDCR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MDCR\_EL2 are UNDEFINED.

## Attributes

MDCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:51]

Reserved, RES0.

## EnSTEPOP, bit [50]

When FEAT\_STEP2 is implemented:

| EnSTEPOP   | Meaning                                                      |
|------------|--------------------------------------------------------------|
| 0b0        | Execution from MDSTEPOP_EL1 is disabled.                     |
| 0b1        | Execution from MDSTEPOP_EL1 is not disabled by this control. |

If EL2 is not implemented or EL2 is disabled in the current Security state, then the Effective value of this field is 0b1 , other than for a direct read of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [49:44]

Reserved, RES0.

## EBWE, bit [43]

## When FEAT\_Debugv8p9 is implemented:

Extended Breakpoint and Watchpoint Enable. Enables use of additional breakpoints or watchpoints.

| EBWE   | Meaning                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------|
| 0b0    | The Effective value of MDSCR_EL1.EMBWE is 0. The Effective value of MDSELR_EL1.BANK is zero at EL2. |
| 0b1    | The Effective values of MDSCR_EL1.EMBWE and MDSELR_EL1.BANK are not affected by this field.         |

It is IMPLEMENTATION DEFINED whether this field is implemented or is RES0 when 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI.

If EL2 is not implemented or EL2 is disabled in the current Security state, then the Effective value of this field is 1, other than for a direct read of the register.

This field is ignored by the PE and treated as 0 when EL3 is implemented and MDCR\_EL3.EBWE is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [42]

Reserved, RES0.

## PMEE, bits [41:40]

## When FEAT\_EBEP is implemented:

Performance Monitors Exception Enable. Controls the generation of the PMUIRQ signal and the PMU Profiling exception at EL0, EL1, and EL2.

| PMEE   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b00   | The PMUIRQ signal is asserted on a PMUoverflow, and the PMUProfiling exception is disabled. |
| 0b01   | The PMUIRQ signal and the PMUProfiling exception are both controlled by PMECR_EL1.PMEE.     |
| 0b11   | The PMUIRQ signal is deasserted, and the PMUProfiling exception is enabled.                 |

All other values are reserved.

If EL2 is not implemented or EL2 is disabled in the current Security state, then the Effective value of this field is 0b01 , other than for a direct read of the register.

This field is ignored by the PE when all of the following are true:

- EL3 is implemented.
- MDCR\_EL3.PMEE != 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [39:37]

Reserved, RES0.

## HPMFZS, bit [36]

## When FEAT\_SPEv1p2 is implemented:

Hyp Performance Monitors Freeze-on-SPE event. Stop counters when PMBLIMITR\_EL1.{PMFZ,E} is {1,1} and profiling is stopped.

| HPMFZS   | Meaning                                                                                   |
|----------|-------------------------------------------------------------------------------------------|
| 0b0      | Do not freeze on a Statistical Profiling Buffer Management event.                         |
| 0b1      | Affected counters do not count following a Statistical Profiling Buffer Management event. |

The pseudocode function SPEProfilingStopped describes when profiling is stopped.

The counters affected by this field are the event counters in the second range. This applies even when EL2 is disabled in the current Security state.

Other event counters and PMCCNTR\_EL0 are not affected by this field.

When FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0 is not affected by this field.

If MDCR\_EL2.HPMN is equal to GetNumEventCountersSelfHosted() , then this field has no effect.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [35:32]

Reserved, RES0.

PMSSE, bits [31:30]

When FEAT\_PMUv3\_SS is implemented:

Performance Monitors Snapshot Enable. Controls the generation of Capture events.

| PMSSE   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b00    | Capture events are disabled.                    |
| 0b01    | Capture events are controlled by PMECR_EL1.SSE. |
| 0b10    | Capture events are enabled and prohibited.      |
| 0b11    | Capture events are enabled and allowed.         |

If EL2 is not implemented, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Cold reset:
- When the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPMFZO,bit [29]

## When FEAT\_PMUv3p7 is implemented:

Hyp Performance Monitors Freeze-on-overflow. Stop event counters on overflow.

| HPMFZO   | Meaning                                                                                                                                                                                                                    |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Do not freeze on overflow.                                                                                                                                                                                                 |
| 0b1      | Affected counters do not count when all of the following are true for any event counter PMEVCNTR<m>_EL0 in the second range: • PMOVSCLR_EL0[m] is 1. • Either FEAT_SEBEP is not implemented or PMEVTYPER<m>_EL0.SYNC is 0. |

The counters affected by this field are the event counters in the second range. This applies even when EL2 is disabled in the current Security state.

Other event counters and PMCCNTR\_EL0 are not affected by this field.

When FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0 is not affected by this field.

If MDCR\_EL2.HPMN is equal to GetNumEventCountersSelfHosted() , then this field has no effect.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MTPME,bit [28]

## When FEAT\_MTPMU is implemented and EL3 is not implemented:

Multi-threaded PMU Enable. Enables use of the PMEVTYPER&lt;n&gt;\_EL0.MT bits.

| MTPME   | Meaning                                                                  |
|---------|--------------------------------------------------------------------------|
| 0b0     | FEAT_MTPMU is disabled. The Effective value of PMEVTYPER<n>_EL0.MT is 0. |
| 0b1     | PMEVTYPER<n>_EL0.MT bits not affected by this field.                     |

If FEAT\_MTPMU is disabled for any other PE in the system that has the same level 1 Affinity as the PE, it is IMPLEMENTATION DEFINED whether the PE behaves as if this field is 0.

The reset behavior of this field is:

- On a Cold reset, this field resets to '1' .

## Otherwise:

Reserved, RES0.

TDCC, bit [27]

## When FEAT\_FGT is implemented:

Trap DCC. Traps use of the Debug Comms Channel at EL1 and EL0 to EL2.

| TDCC   | Meaning                                                                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any register accesses to be trapped.                                                                                                                                                                                                                                |
| 0b1    | If EL2 is implemented and enabled in the current Security state, accesses to the DCCregisters at EL1 and EL0 generate a Trap exception to EL2, unless the access also generates a higher priority exception. Traps on the DCCdata transfer registers are ignored when the PE is in Debug state. |

The DCC registers trapped by this control are:

AArch64: OSDTRRX\_EL1, OSDTRTX\_EL1, MDCCSR\_EL0, MDCCINT\_EL1, and, when the PE is in Non-debug state, DBGDTR\_EL0, DBGDTRRX\_EL0, and DBGDTRTX\_EL0.

AArch32: DBGDTRRXext, DBGDTRTXext, DBGDSCRint, DBGDCCINT, and, when the PE is in Non-debug state, DBGDTRRXint and DBGDTRTXint.

The traps are reported with EC syndrome value:

- 0x05 for trapped AArch32 MRC and MCR accesses with coproc == 0b1110 .
- 0x06 for trapped AArch32 LDC to DBGDTRTXint and STC from DBGDTRRXint.
- 0x18 for trapped AArch64 MRS and MSR accesses.

When the PE is in Debug state, MDCR\_EL2.TDCC does not trap any accesses to:

AArch64: DBGDTR\_EL0, DBGDTRRX\_EL0, and DBGDTRTX\_EL0.

AArch32: DBGDTRRXint and DBGDTRTXint.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

HLP, bit [26]

## When FEAT\_PMUv3p5 is implemented:

Hypervisor Long Event Counter Enable. Determines which event counter bit generates an overflow recorded by PMOVSR[n].

| HLP   | Meaning                                                                                         |
|-------|-------------------------------------------------------------------------------------------------|
| 0b0   | Affected counters overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[31:0]. |
| 0b1   | Affected counters overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

The counters affected by this field are the event counters in the second range. This applies even when EL2 is disabled in the current Security state.

The following are not affected by this field:

- Other event counters.
- PMCCNTR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0.

If MDCR\_EL2.HPMN is equal to GetNumEventCountersSelfHosted() , then this field has no effect.

For more information see the description of MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E2TB, bits [25:24]

## When FEAT\_TRBE is implemented:

EL2 Trace Buffer.

If EL2 is implemented and enabled in the trace buffer owning Security state, then this field controls the trace buffer owning translation regime.

If EL2 is implemented and enabled in the current Security state, then this field controls access to trace buffer System registers from EL1.

| E2TB   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | If EL2 is implemented and enabled in the trace buffer owning Security state, then the trace buffer owning Exception level is EL2. Otherwise, the trace buffer owning Exception level is EL1 and, if TraceBufferEnabled() == TRUE, tracing is prohibited at EL2. If EL2 is implemented and enabled in the current Security state, then accesses to trace buffer System registers at EL1 are trapped to EL2, unless the access generates a higher priority exception. |
| 0b10   | Trace buffer owning Exception level is EL1. If TraceBufferEnabled() == TRUE, then tracing is prohibited at EL2. If EL2 is implemented and enabled in the current Security state, then accesses to trace buffer System registers at EL1 are trapped to EL2, unless the access generates a higher priority exception.                                                                                                                                                 |

| E2TB   | Meaning                                                                                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b11   | Trace buffer owning Exception level is EL1. If TraceBufferEnabled() == TRUE, then tracing is prohibited at EL2. Accesses to trace buffer System registers at EL1 are not trapped by this mechanism. |

All other values are reserved.

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to TRBBASER\_EL1, TRBLIMITR\_EL1, TRBMAR\_EL1, TRBPTR\_EL1, TRBSR\_EL1, and TRBTRG\_EL1.
- If FEAT\_TRBE\_MPAM is implemented, MRS and MSR accesses to TRBMPAM\_EL1.
- If FEAT\_TRBE\_EXC is implemented, MRS and MSR accesses to TRBSR\_EL2 and TRBSR\_EL12.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL2, reported using EC syndrome value 0x18 .

When TraceBufferEnabled() ==FALSE, this field has no effect on whether tracing is prohibited.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HCCD, bit [23]

## When FEAT\_PMUv3p5 is implemented:

Hypervisor Cycle Counter Disable. Prohibits PMCCNTR\_EL0 from counting at EL2.

| HCCD   | Meaning                                                          |
|--------|------------------------------------------------------------------|
| 0b0    | Cycle counting by PMCCNTR_EL0 is not affected by this mechanism. |
| 0b1    | Cycle counting by PMCCNTR_EL0 is prohibited at EL2.              |

This field does not affect the CPU\_CYCLES event or any other event that counts cycles.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bits [22:20]

Reserved, RES0.

## TTRF, bit [19]

## When FEAT\_TRF is implemented:

Traps use of the Trace Filter Control registers at EL1 to EL2, as follows:

- Access to TRFCR\_EL1 is trapped to EL2, reported using EC syndrome value 0x18 .
- Access to TRFCR is trapped to EL2, reported using EC syndrome value 0x03 .

| TTRF   | Meaning                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses to the specified registers at EL1 are not affected by this control.                                                   |
| 0b1    | Accesses to the specified registers at EL1 generate a trap exception to EL2 when EL2 is enabled in the current Security state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [18]

Reserved, RES0.

## HPMD,bit [17]

## When FEAT\_PMUv3p1 is implemented and FEAT\_Debugv8p2 is implemented:

Guest Performance Monitors Disable. Controls PMU operation at EL2.

| HPMD   | Meaning                                                                                                                                                                    |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Counters are not affected by this mechanism.                                                                                                                               |
| 0b1    | Affected counters are prohibited from counting at EL2. If PMCR_EL0.DP is 1, then PMCCNTR_EL0 is disabled at EL2. Otherwise, PMCCNTR_EL0 is not affected by this mechanism. |

The counters affected by this field are:

- Event counters in the first range.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- If PMCR\_EL0.DP is 1, the cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_PMUv3p1 is implemented:

Guest Performance Monitors Disable. Controls PMU operation at EL2 when

ExternalSecureNoninvasiveDebugEnabled() is FALSE.

| HPMD   | Meaning                                      |
|--------|----------------------------------------------|
| 0b0    | Counters are not affected by this mechanism. |

| HPMD   | Meaning                                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1    | If ExternalSecureNoninvasiveDebugEnabled() is FALSE, then all the following apply:                                                                                                   |
|        | • Affected event counters are prohibited from counting at EL2. • If PMCR_EL0.DP is 1, then PMCCNTR_EL0 is disabled at EL2. Otherwise, PMCCNTR_EL0 is not affected by this mechanism. |

If ExternalSecureNoninvasiveDebugEnabled() is TRUE, then the event counters and PMCCNTR\_EL0 are not affected by this field.

Otherwise, the counters affected by this field are:

- Event counters in the first range.
- If PMCR\_EL0.DP is 1, the cycle counter, PMCCNTR\_EL0.

Other event counters are not affected by this field. When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [16]

Reserved, RES0.

## EnSPM, bit [15]

## When FEAT\_SPMU is implemented:

Enable access to System PMU registers. When disabled, accesses to System PMU registers generate a trap to EL2.

| EnSPM   | Meaning                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Accesses of the specified System PMUregisters at EL1 and EL0 are trapped to EL2, unless the instruction generates a higher priority exception. |
| 0b1     | Accesses of the specified System PMUregisters are not trapped by this mechanism.                                                               |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to SPMACCESSR\_EL1, SPMCFGR\_EL1, SPMCGCR&lt;n&gt;\_EL1, SPMCNTENCLR\_EL0, SPMCNTENSET\_EL0, SPMCR\_EL0, SPMDEVAFF\_EL1, SPMDEVARCH\_EL1, SPMEVCNTR&lt;n&gt;\_EL0, SPMEVFILT2R&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, SPMEVTYPER&lt;n&gt;\_EL0, SPMIIDR\_EL1, SPMINTENCLR\_EL1, SPMINTENSET\_EL1, SPMOVSCLR\_EL0, SPMOVSSET\_EL0, SPMSCR\_EL1, and SPMSELR\_EL0.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TPMS, bit [14]

## When FEAT\_SPE is implemented:

Trap Performance Monitor Sampling. Enables a trap to EL2 on accesses of SPE registers.

| TPMS   | Meaning                                                                                                                          |
|--------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses of the specified SPE registers are not trapped by this mechanism.                                                       |
| 0b1    | Accesses of the specified SPE registers at EL1 are trapped to EL2, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMSCR\_EL1, PMSEVFR\_EL1, PMSFCR\_EL1, PMSICR\_EL1, PMSIRR\_EL1, and PMSLATFR\_EL1.
- MRS accesses to PMSIDR\_EL1.
- If FEAT\_SPE\_FnE is implemented, MRS and MSR accesses to PMSNEVFR\_EL1.
- If FEAT\_SPE\_FDS is implemented, MRS and MSR accesses to PMSDSFR\_EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E2PB, bits [13:12]

## When FEAT\_SPE is implemented:

EL2 Profiling Buffer.

If EL2 is implemented and enabled in the Profiling Buffer owning Security state, then this field controls the Profiling Buffer owning translation regime.

If EL2 is implemented and enabled in the current Security state, then this field controls access to Profiling Buffer System registers from EL1.

| E2PB   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | If EL2 is implemented and enabled in the Profiling Buffer owning Security state, then the Profiling Buffer owning Exception level is EL2. Otherwise, the Profiling Buffer owning Exception level is EL1 and, Profiling is prohibited at EL2. If EL2 is implemented and enabled in the current Security state, then accesses to Profiling Buffer System registers at EL1 are trapped to EL2, unless the access generates a higher priority exception. |
| 0b10   | Profiling Buffer owning Exception level is EL1. Profiling is prohibited at EL2. If EL2 is implemented and enabled in the current Security state, then accesses to Profiling Buffer System registers at EL1 are trapped to EL2, unless the access generates a higher priority exception.                                                                                                                                                              |
| 0b11   | Profiling Buffer owning Exception level is EL1. Profiling is prohibited at EL2. Accesses to Profiling Buffer System registers at EL1 are not trapped by this mechanism.                                                                                                                                                                                                                                                                              |

All other values are reserved.

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMBLIMITR\_EL1, PMBPTR\_EL1, and PMBSR\_EL1.
- If FEAT\_SPE\_nVM is implemented, MRS and MSR accesses to PMBMAR\_EL1.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL2, reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TDRA, bit [11]

Trap Debug ROM Address register access. Traps System register accesses to the Debug ROM registers to EL2 when EL2 is enabled in the current Security state as follows:

- If EL1 is using AArch64, accesses to MDRAR\_EL1 are trapped to EL2, reported using EC syndrome value 0x18 .
- If EL0 or EL1 is using AArch32 state, MRC or MCR accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x05 and MRRC or MCRR accesses are trapped to EL2, reported using EC syndrome value 0x0C :
- DBGDRAR, DBGDSAR.

| TDRA   | Meaning                                                                                                                                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                                                                                         |
| 0b1    | EL0 and EL1 System register accesses to the Debug ROMregisters are trapped to EL2 when EL2 is enabled in the current Security state, unless it is trapped by the following: • DBGDSCRext.UDCCdis. • MDSCR_EL1.TDCC. |

This field is treated as being 1 for all purposes other than a direct read when one or more of the following are true:

- MDCR\_EL2.TDE == 1.
- HCR\_EL2.TGE == 1.

Note

EL2 does not provide traps on debug register accesses through the optional memory-mapped external debug interfaces.

System register accesses to the debug registers might have side-effects. When a System register access is trapped to EL2, no side-effects occur before the exception is taken to EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TDOSA, bit [10]

## When FEAT\_DoubleLock is implemented:

Trap debug OS-related register access. Traps EL1 System register accesses to the powerdown debug registers to EL2, from both Execution states as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x18 :
- OSLAR\_EL1, OSLSR\_EL1, OSDLR\_EL1, and DBGPRCR\_EL1.

- Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this bit.
- In AArch32 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x05 :
- DBGOSLSR, DBGOSLAR, DBGOSDLR, and DBGPRCR.
- Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this bit.

| TDOSA   | Meaning                                                                                                                             |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                         |
| 0b1     | EL1 System register accesses to the powerdown debug registers are trapped to EL2 when EL2 is enabled in the current Security state. |

Note

These registers are not accessible at EL0.

This field is treated as being 1 for all purposes other than a direct read when one or more of the following are true:

- MDCR\_EL2.TDE == 1.
- HCR\_EL2.TGE == 1.

System register accesses to the debug registers might have side-effects. When a System register access is trapped to EL2, no side-effects occur before the exception is taken to EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Trap debug OS-related register access. Traps EL1 System register accesses to the powerdown debug registers to EL2, from both Execution states as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x18 :
- OSLAR\_EL1, OSLSR\_EL1, and DBGPRCR\_EL1.
- Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this bit.
- In AArch32 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x05 :
- DBGOSLSR, DBGOSLAR, and DBGPRCR.
- Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this bit.

It is IMPLEMENTATION DEFINED whether accesses to OSDLR\_EL1 are trapped.

It is IMPLEMENTATION DEFINED whether accesses to DBGOSDLR are trapped.

| TDOSA   | Meaning                                                                                                                             |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                         |
| 0b1     | EL1 System register accesses to the powerdown debug registers are trapped to EL2 when EL2 is enabled in the current Security state. |

Note

These registers are not accessible at EL0.

This field is treated as being 1 for all purposes other than a direct read when one or more of the following are true:

- MDCR\_EL2.TDE == 1.
- HCR\_EL2.TGE == 1.

## Note

EL2 does not provide traps on debug register accesses through the optional memory-mapped external debug interfaces.

System register accesses to the debug registers might have side-effects. When a System register access is trapped to EL2, no side-effects occur before the exception is taken to EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TDA, bit [9]

Trap accesses of debug System registers. Enables a trap to EL2 on accesses of debug System registers.

| TDA   | Meaning                                                                                                                                           |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses of the specified debug System registers are not trapped by this mechanism.                                                               |
| 0b1   | Accesses of the specified debug System registers at EL1 and EL0 are trapped to EL2, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to DBGAUTHSTATUS\_EL1, DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGCLAIMCLR\_EL1, DBGCLAIMSET\_EL1, DBGWCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, MDCCINT\_EL1, MDCCSR\_EL0, MDSCR\_EL1, OSDTRRX\_EL1, OSDTRTX\_EL1, and OSECCR\_EL1.
- If FEAT\_Debugv8p9 is implemented, MRS and MSR accesses to MDSELR\_EL1.
- If FEAT\_STEP2 is implemented, MRS and MSR accesses to MDSTEPOP\_EL1.
- In Non-debug state, MRS accesses to DBGDTRRX\_EL0 and DBGDTR\_EL0 and MSR accesses to DBGDTRTX\_EL0 and DBGDTR\_EL0.

In AArch32 state, the instructions affected by this control are:

- MRC and MCR accesses to DBGAUTHSTATUS, DBGBCR&lt;n&gt;, DBGBVR&lt;n&gt;, DBGBXVR&lt;n&gt;, DBGCLAIMCLR, DBGCLAIMSET, DBGDCCINT, DBGDEVID, DBGDEVID1, DBGDEVID2, DBGDIDR, DBGDSCRext, DBGDSCRint, DBGDTRRXext, DBGDTRTXext, DBGOSECCR, DBGVCR, DBGWCR&lt;n&gt;, DBGWFAR, and DBGWVR&lt;n&gt;.
- STC accesses to DBGDTRRXint and LDC accesses to DBGDTRTXint.
- In Non-debug state, MRC accesses to DBGDTRRXint and MCR accesses to DBGDTRTXint.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x05 for MRC and MCR accesses, and 0x06 for LDC and STC accesses.

The following instructions are not trapped in Debug state:

- AArch64 MRS accesses to DBGDTRRX\_EL0 and DBGDTR\_EL0 and MSR accesses to DBGDTRTX\_EL0 and DBGDTR\_EL0.
- AArch32 MRC accesses to DBGDTRRXint and MCR accesses to DBGDTRTXint.

If 16 or fewer breakpoints and 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI, then it is IMPLEMENTATION DEFINED whether AArch64 accesses to MDSELR\_EL1 are trapped to EL2 when MDCR\_EL2.TDA is 1.

This field is ignored by the PE and treated as one when any of the following are true:

- MDCR\_EL2.TDE == 1.
- HCR\_EL2.TGE == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TDE, bit [8]

Trap Debug Exceptions. Controls routing of Debug exceptions, and defines the debug target Exception level, ELD.

| TDE   | Meaning                                                                                                                                                                                                                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The debug target Exception level is EL1.                                                                                                                                                                                                                                                                      |
| 0b1   | If EL2 is enabled for the current Effective value of SCR_EL3.NS, the debug target Exception level is EL2, otherwise the debug target Exception level is EL1. The MDCR_EL2.{TDRA, TDOSA, TDA} fields are treated as being 1 for all purposes other than returning the result of a direct read of the register. |

For more information, see 'Routing debug exceptions'.

This field is treated as being 1 for all purposes other than a direct read when HCR\_EL2.TGE == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## HPME, bit [7]

## When FEAT\_PMUv3 is implemented:

Hyp Enable.

| HPME   | Meaning                                          |
|--------|--------------------------------------------------|
| 0b0    | Affected counters are disabled and do not count. |
| 0b1    | Affected counters are enabled by PMCNTENSET_EL0. |

The counters affected by this field are the event counters in the second range. This applies even when EL2 is disabled in the current Security state.

The following counters are not affected by this field:

- Other event counters.

- PMCCNTR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0.

If MDCR\_EL2.HPMN is equal to GetNumEventCountersSelfHosted() , then this field has no effect.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TPM, bit [6]

## When FEAT\_PMUv3 is implemented:

Trap accesses of PMU registers. Enables a trap to EL2 on accesses of PMU registers.

| TPM   | Meaning                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses of the specified PMUregisters are not trapped by this mechanism.                                                               |
| 0b1   | Accesses of the specified PMUregisters at EL1 and EL0 are trapped to EL2, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMCR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMINTENCLR\_EL1, PMINTENSET\_EL1, PMOVSCLR\_EL0, PMOVSSET\_EL0, PMSELR\_EL0, PMSWINC\_EL0, PMUSERENR\_EL0, PMXEVCNTR\_EL0, and PMXEVTYPER\_EL0.
- MRS accesses to PMCEID0\_EL0 and PMCEID1\_EL0.
- If FEAT\_PMUv3p4 is implemented, MRS accesses to PMMIR\_EL1.
- If FEAT\_PMUv3p9 is implemented, MSR accesses to PMZR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, MRS accesses to PMICFILTR\_EL0 and PMICNTR\_EL0.
- If FEAT\_EBEP is implemented or FEAT\_PMUv3\_SS is implemented, MRS and MSR accesses to PMECR\_EL1.
- If FEAT\_SEBEP is implemented, MRS and MSR accesses to PMIAR\_EL1.

In AArch32 state, the instructions affected by this control are:

- MRC and MCR accesses to PMCCFILTR, PMCCNTR, PMCNTENCLR, PMCNTENSET, PMCR, PMEVCNTR&lt;n&gt;, PMEVTYPER&lt;n&gt;, PMINTENCLR, PMINTENSET, PMOVSR, PMOVSSET, PMSELR, PMSWINC, PMUSERENR, PMXEVCNTR, and PMXEVTYPER.
- MRC accesses to PMCEID0 and PMCEID1.
- MRRC and MCRR accesses to PMCCNTR.
- If FEAT\_PMUv3p1 is implemented, MRC accesses to PMCEID2 and PMCEID3.
- If FEAT\_PMUv3p4 is implemented, MRC accesses to PMMIR.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x03 for MRC and MCR accesses, and 0x04 for MRRC and MCRR accesses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TPMCR, bit [5]

## When FEAT\_PMUv3 is implemented:

Trap PMCR\_EL0 or PMCR accesses. Traps EL0 and EL1 accesses to EL2, when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to PMCR\_EL0 are trapped to EL2, reported using EC syndrome value 0x18 .
- In AArch32 state, accesses to PMCR are trapped to EL2, reported using EC syndrome value 0x03 .

| TPMCR   | Meaning                                                                                                                                                                                             |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                                                                                         |
| 0b1     | EL0 and EL1 accesses to the specified registers are trapped to EL2 when EL2 is enabled in the current Security state, unless they are trapped by the following: • PMUSERENR.EN. • PMUSERENR_EL0.EN. |

Note

EL2 does not provide traps on Performance Monitor register accesses through the optional memory-mapped external debug interface.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPMN,bits [4:0]

## When FEAT\_PMUv3 is implemented:

Defines the number of event counters PMEVCNTR&lt;n&gt;\_EL0 and, if FEAT\_PMUv3\_SS is implemented, event counter snapshot registers PMEVCNTSVR&lt;n&gt;\_EL1, that are accessible from EL1 and, if permitted, from EL0.

MDCR\_EL2.HPMN divides the event counters accessible from self-hosted software into a first range and a second range.

When FEAT\_PMUv3\_EXTPMN is implemented, all of the following apply:

- PMCCR.EPMN divides the NUM\_PMU\_COUNTERS event counters implemented by the PE into the event counters that MDCR\_EL2.HPMN divides into the first and second ranges, and a third range that is inaccessible from self-hosted software.
- If MDCR\_EL2.HPMN is not 0 and is less than the Effective value of PMCCR.EPMN, then event counters [0..(MDCR\_EL2.HPMN-1)] are in the first range, and the remaining event counters [MDCR\_EL2.HPMN..(PMCCR.EPMN-1)] are in the second range.
- The pseudcode function GetNumEventCountersSelfHosted() returns the Effective value of PMCCR.EPMN.

When FEAT\_PMUv3\_EXTPMN is not implemented, all of the following apply:

- All of the NUM\_PMU\_COUNTERS event counters are accessible to self-hosted software and no counters are in the third range.
- If MDCR\_EL2.HPMN is not 0 and is less than NUM\_PMU\_COUNTERS , then event counters [0..(MDCR\_EL2.HPMN-1)] are in the first range, and the remaining event counters [MDCR\_EL2.HPMN..( NUM\_PMU\_COUNTERS -1)] are in the second range.
- The pseudocode function GetNumEventCountersSelfHosted() returns NUM\_PMU\_COUNTERS .

If FEAT\_HPMN0 is implemented and MDCR\_EL2.HPMN is 0, then all of the following apply:

- No event counters are in the first range.
- If FEAT\_PMUv3\_EXTPMN is implemented, then event counters [0..(PMCCR.EPMN-1)] are in the second range.
- If FEAT\_PMUv3\_EXTPMN is not implemented, then all event counters are in the second range.

If MDCR\_EL2.HPMN is equal to GetNumEventCountersSelfHosted() , or EL2 is not implemented, then all of the following apply:

- If FEAT\_PMUv3\_EXTPMN is implemented, then event counters [0..(PMCCR.EPMN-1)] are in the first range.
- If FEAT\_PMUv3\_EXTPMN is not implemented, then all event counters are in the first range.
- No event counters are in the second range.

All of the following apply for an event counter PMEVCNTR&lt;n&gt;\_EL0 in the first range:

- The counter is accessible from EL1, EL2, and EL3.
- The counter is accessible from EL0 if permitted by PMUSERENR\_EL0 and PMUACR\_EL1, or by PMUSERENR.
- If FEAT\_PMUv3p5 is implemented, then PMCR\_EL0.LP or PMCR.LP determines whether the counter overflow flag PMOVSSET\_EL0[n] is set on unsigned overflow of PMEVCNTR&lt;n&gt;\_EL0[31:0] or PMEVCNTR&lt;n&gt;\_EL0[63:0].
- PMCR\_EL0.E and PMCNTENSET\_EL0[n] enable the operation of the event counter.

All of the following apply for an event counter PMEVCNTR&lt;n&gt;\_EL0 in the second range:

- The counter is accessible from EL2 and EL3.
- If EL2 is disabled in the current Security state, then the event counter is accessible from EL1, and from EL0 if permitted by PMUSERENR\_EL0 and PMUACR\_EL1, or by PMUSERENR.
- If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP determines whether the counter overflow flag PMOVSSET\_EL0[n] is set on unsigned overflow of PMEVCNTR&lt;n&gt;\_EL0[31:0] or PMEVCNTR&lt;n&gt;\_EL0[63:0].
- MDCR\_EL2.HPME and PMCNTENSET\_EL0[n] enable the operation of the event counter.

If FEAT\_PMUv3\_SS is implemented, then all of the following apply:

- For an event counter snapshot register PMEVCNTSVR&lt;n&gt;\_EL1 in the first range, the register is accessible from EL1, EL2, and EL3.
- For an event counter snapshot register PMEVCNTSVR&lt;n&gt;\_EL1 in the second range, the register is accessible from EL2 and EL3. If EL2 is disabled in the current Security state, the event counter is also accessible from EL1.

For information about counters in the third range, see the description of PMCCR.EPMN.

Values greater than GetNumEventCountersSelfHosted() are reserved. If FEAT\_HPMN0 is not implemented, then the value 0 is reserved.

When FEAT\_PMUv3\_EXTPMN is not implemented and this field is set to a reserved value, the following CONSTRAINED UNPREDICTABLE behaviors apply:

- The value returned by a direct read of MDCR\_EL2.HPMN is UNKNOWN.
- The number of event counters in each of the first and second ranges is UNKNOWN. That is, either:
- The PE behaves as if MDCR\_EL2.HPMN is set to an UNKNOWN nonzero value less than or equal to NUM\_PMU\_COUNTERS .
- All counters are in the second range and none are in the first range.

When FEAT\_PMUv3\_EXTPMN is implemented and this field is set to a reserved value, the following behaviors apply:

- The value returned by a direct read of MDCR\_EL2.HPMN is the Effective value of PMCCR.EPMN.
- No event counters are in the second range.
- The value returned by an indirect read of MDCR\_EL2.HPMN as a result of direct reads of PMCR\_EL0.N or PMCR.N is the Effective value of PMCCR.EPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to the expression NUM\_PMU\_COUNTERS .

## Otherwise:

Reserved, RES0.

## Accessing MDCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MDCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MDCR_EL2;
```

MSR MDCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then
```

```
then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MDCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then MDCR_EL2 = X[t, 64];
```

## D24.3.18 MDCR\_EL3, Monitor Debug Configuration Register (EL3)

The MDCR\_EL3 characteristics are:

## Purpose

Provides EL3 configuration options for self-hosted debug and the Performance Monitors Extension.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MDCR\_EL3 are UNDEFINED.

## Attributes

MDCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## EnPMS4, bit [55]

## When FEAT\_SPE\_nVM is implemented:

Enable access to SPE registers. When disabled, accesses to SPE registers generate a trap to EL3.

| EnPMS4   | Meaning                                                                                                                                  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Accesses of the specified SPE registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1      | Accesses of the specified SPE registers are not trapped by this mechanism.                                                               |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to PMBMAR\_EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRBEE, bits [54:53]

## When FEAT\_TRBE\_EXC is implemented:

Trace buffer management event Exception Enable.

| TRBEE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | Disabled. TRBE Profiling exceptions for all Exception levels are disabled. All of the following apply: • No trace buffer management events are recorded in TRBSR_EL3. • TRBE Profiling exceptions are not generated. • TRBSR_EL1.IRQ drives the interrupt request signal TRBIRQ . • Accesses to TRBSR_EL2 at EL2 are trapped to EL3. • Accesses to TRBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1 and accesses to TRBSR_EL1 at EL2 ignore the value of HCR_EL2.E2H. |
| 0b01    | Delegated. TRBE Profiling exceptions for EL3 are disabled, but might be enabled for EL2 or EL1 by TRFCR_EL2.EE or TRFCR_EL1.EE. All of the following apply: • No trace buffer management events are recorded in TRBSR_EL3. • TRBSR_EL3.IRQ is ignored and TRBE Profiling exceptions are not taken to EL3.                                                                                                                                                             |
| 0b10    | Enabled. TRBE Profiling exceptions for EL3 are enabled for trace buffer management events targeting EL3, as follows:                                                                                                                                                                                                                                                                                                                                                  |
| 0b11    | Trap all. TRBE Profiling exceptions for EL3 are enabled for all trace buffer management events, as follows: • All trace buffer management events are recorded in TRBSR_EL3. • TRBE Profiling exceptions are generated and taken to EL3 when unmasked and TRBSR_EL3.IRQ is 1.                                                                                                                                                                                          |

If EL3 is not implemented, then the Effective value of MDCR\_EL3.TRBEE is 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMSEE, bits [52:51]

## When FEAT\_SPE\_EXC is implemented:

Profiling Buffer management event Exception Enable.

| PMSEE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | Disabled. SPE Profiling exceptions for all Exception levels are disabled. All of the following apply: • No Profiling Buffer management events are recorded in PMBSR_EL3. • SPE Profiling exceptions are not generated. • PMBSR_EL1.S drives the interrupt request signal PMBIRQ . • Accesses to PMBSR_EL2 at EL2 are trapped to EL3. • Accesses to PMBSR_EL1 at EL1 ignore the value of HCR_EL2.NV1 and accesses to PMBSR_EL1 at EL2 ignore the value of HCR_EL2.E2H. |
| 0b01    | Delegated. SPE Profiling exceptions for EL3 are disabled, but might be enabled for EL2 or EL1 by PMSCR_EL2.EE or PMSCR_EL1.EE. All of the following apply: • No Profiling Buffer management events are recorded in PMBSR_EL3. • PMBSR_EL3.S is ignored and SPE Profiling exceptions are not taken to EL3.                                                                                                                                                             |
| 0b10    | Enabled. SPE Profiling exceptions for EL3 are enabled for Profiling Buffer management events targeting EL3, as follows: • Profiling Buffer management events due to a fault on a write to the Profiling Buffer that would                                                                                                                                                                                                                                             |
| 0b11    | Trap all. SPE Profiling exceptions for EL3 are enabled for all Profiling Buffer management events, as follows: • All Profiling Buffer management events are recorded in PMBSR_EL3. • SPE Profiling exceptions are generated and taken to EL3 when unmasked and PMBSR_EL3.S is 1.                                                                                                                                                                                      |

If EL3 is not implemented, then the Effective value of MDCR\_EL3.PMSEE is 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnSTEPOP, bit [50]

When FEAT\_STEP2 is implemented:

| EnSTEPOP   | Meaning                                                                                                                                                                         |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Execution from MDSTEPOP_EL1 is disabled. EL2, EL1 and EL0 System register accesses to MDSTEPOP_EL1 are trapped to EL3, unless the access generates a higher priority exception. |
| 0b1        | Execution from MDSTEPOP_EL1 is not disabled by this control. System register accesses to MDSTEPOP_EL1 are not trapped by this mechanism.                                        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ETBAD, bits [49:48]

## When FEAT\_TRBE\_EXT is implemented:

External Trace Buffer Access Disable. Controls access to the Trace Buffer registers from an external debugger.

| ETBAD   | Meaning                                                                                                                                                                                                                                                                                                                                                          | Applies when            |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b00    | Non-secure accesses from an external debugger to Trace Buffer registers are prohibited. If FEAT_RME is implemented, Secure and Realm accesses from an external debugger to Trace Buffer registers are prohibited and Root accesses to Trace Buffer registers are allowed. If FEAT_RME is not implemented, Secure accesses to Trace Buffer registers are allowed. |                         |
| 0b01    | Secure and Non-secure accesses from an external debugger to Trace Buffer registers are prohibited. Root and Realm accesses to Trace Buffer registers are allowed.                                                                                                                                                                                                | FEAT_RME is implemented |
| 0b10    | Realm and Non-secure accesses from an external debugger to Trace Buffer registers are prohibited. Root and Secure accesses to Trace Buffer registers are allowed.                                                                                                                                                                                                | FEAT_RME is implemented |
| 0b11    | All accesses from an external debugger to Trace Buffer registers are allowed.                                                                                                                                                                                                                                                                                    |                         |

If EL3 is not implemented, then the Effective value of this field is 0b11 .

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## Otherwise:

Reserved, RES0.

## EnITE, bit [47]

## When FEAT\_ITE is implemented:

Enable access to Instrumentation trace registers. When disabled, accesses to Instrumentation trace registers generate a trap to EL3.

| EnITE   | Meaning                                                                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Accesses of the specified Instrumentation trace registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1     | Accesses of the specified Instrumentation trace registers are not trapped by this mechanism.                                                               |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to TRCITECR\_EL1, TRCITECR\_EL2, and TRCITECR\_EL12.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EPMSSAD, bits [46:45]

## When FEAT\_PMUv3\_SS is implemented:

External PMU Snapshot Access Disable. Controls access to the PMU Snapshot registers from an external debugger.

External accesses of the following registers are affected by this control:

- PMCCNTSVR\_EL1, PMEVCNTSVR&lt;n&gt;\_EL1, and PMSSCR\_EL1.
- If FEAT\_PMUv3\_ICNTR is implemented, PMICNTSVR\_EL1.

| EPMSSAD   | Meaning                                                                                                                                                                                                                                                                                                                                         | Applies when            |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b00      | Non-secure accesses from an external debugger to the affected PMUSnapshot registers are prohibited. If FEAT_RME is implemented, Secure and Realm accesses from an external debugger to the affected PMUSnapshot registers are prohibited. Other accesses from an external debugger to the specified registers are not affected by this control. |                         |
| 0b01      | Secure and Non-secure accesses from an external debugger to the affected PMUSnapshot registers are prohibited. Other accesses from an external debugger to the specified registers are not affected by this control.                                                                                                                            | FEAT_RME is implemented |
| 0b10      | Realm and Non-secure accesses from an external debugger to the affected PMUSnapshot registers are prohibited. Other accesses from an external debugger to the specified registers are not affected by this control.                                                                                                                             | FEAT_RME is implemented |
| 0b11      | No accesses from an external debugger to the affected PMUSnapshot registers are prohibited by this control.                                                                                                                                                                                                                                     |                         |

If EL3 is not implemented, then the Effective value of this field is 0b11 .

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## Otherwise:

Reserved, RES0.

## EnPMSS, bit [44]

## When FEAT\_PMUv3\_SS is implemented:

Enable access to PMU Snapshot registers. When disabled, accesses to PMU Snapshot registers generate a trap to EL3.

| EnPMSS   | Meaning                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Accesses of the specified PMUSnapshot registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1      | Accesses of the specified PMUSnapshot registers are not trapped by this mechanism.                                                               |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMCCNTSVR\_EL1, PMEVCNTSVR&lt;n&gt;\_EL1, and PMSSCR\_EL1.
- If FEAT\_PMUv3\_ICNTR is implemented, MRS and MSR accesses to PMICNTSVR\_EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EBWE, bit [43]

## When FEAT\_Debugv8p9 is implemented:

Extended Breakpoint and Watchpoint Enable. Enables use of additional breakpoints or watchpoints, and enables a trap to EL3 on accesses to debug registers.

| EBWE   | Meaning                                                                                                                                                                                                                                         |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | The Effective values of MDSCR_EL1.EMBWE and MDCR_EL2.EBWE are 0. The Effective value of MDSELR_EL1.BANK is zero at EL3. Accesses of MDSELR_EL1 at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1    | The Effective values of MDSCR_EL1.EMBWE, MDCR_EL2.EBWE, and MDSELR_EL1.BANK are not affected by this field. Accesses of MDSELR_EL1 are not trapped by this mechanism.                                                                           |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to MDSELR\_EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

It is IMPLEMENTATION DEFINED whether this field is implemented or is RES0 when 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI.

If EL3 is not implemented, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EnPMS3, bit [42]

## When FEAT\_SPE\_FDS is implemented:

Enable access to SPE registers. When disabled, accesses to SPE registers generate a trap to EL3.

| EnPMS3   | Meaning                                                                                                                                  |
|----------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Accesses of the specified SPE registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1      | Accesses of the specified SPE registers are not trapped by this mechanism.                                                               |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to PMSDSFR\_EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PMEE, bits [41:40]

## When FEAT\_EBEP is implemented:

Performance Monitors Exception Enable. Controls the generation of the PMUIRQ signal and the PMU Profiling exception at all Exception levels.

| PMEE   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b00   | The PMUIRQ signal is asserted on a PMUoverflow, and the PMUProfiling exception is disabled. |
| 0b01   | The PMUIRQ signal and the PMUProfiling exception are both controlled by MDCR_EL2.PMEE.      |
| 0b11   | The PMUIRQ signal is deasserted, and the PMUProfiling exception is enabled.                 |

All other values are reserved.

If EL3 is not implemented, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnTB2, bit [39]

## When FEAT\_TRBE\_MPAM is implemented:

Enable access to Trace Buffer registers. When disabled, accesses to Trace Buffer registers generate a trap to EL3.

| EnTB2   | Meaning                                                                                                                                           |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Accesses of the specified Trace Buffer registers at EL2 and EL1 are trapped to EL3, unless the instruction generates a higher priority exception. |
| 0b1     | Accesses of the specified Trace Buffer registers are not trapped by this mechanism.                                                               |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to TRBMPAM\_EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E3BREC, bit [38]

## When FEAT\_BRBEv1p1 is implemented:

Branch Record Buffer EL3 Cold Reset Enable. With MDCR\_EL3.E3BREW, controls branch recording at EL3.

| E3BREC   | Meaning                                                                                                                        |
|----------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | When MDCR_EL3.E3BREW == 0: Branch recording at EL3 is disabled. When MDCR_EL3.E3BREW == 1: Branch recording at EL3 is enabled. |
| 0b1      | When MDCR_EL3.E3BREW == 0: Branch recording at EL3 is enabled. When MDCR_EL3.E3BREW == 1: Branch recording at EL3 is disabled. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## E3BREW, bit [37]

## When FEAT\_BRBEv1p1 is implemented:

Branch Record Buffer EL3 Warm Reset Enable. With MDCR\_EL3.E3BREC, controls branch recording at EL3.

For a description of the values derived by evaluating MDCR\_EL3.E3BREC and MDCR\_EL3.E3BREW together, see MDCR\_EL3.E3BREC.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EnPMSN, bit [36]

## When FEAT\_SPE\_FnE is implemented:

Trap accesses to PMSNEVFR\_EL1. Controls access to Statistical Profiling PMSNEVFR\_EL1 System register from EL2 and EL1.

| EnPMSN   | Meaning                                                                   |
|----------|---------------------------------------------------------------------------|
| 0b0      | Accesses to PMSNEVFR_EL1 at EL2 and EL1 generate a Trap exception to EL3. |
| 0b1      | Do not trap PMSNEVFR_EL1 to EL3.                                          |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MPMX,bit [35]

## When FEAT\_PMUv3p7 is implemented:

Monitor Performance Monitors Extended control. With MDCR\_EL3.SPME, controls PMU operation at EL3.

| MPMX   | Meaning                                                                                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Counters are not affected by this mechanism.                                                                                                                          |
| 0b1    | Affected counters are prohibited from counting at EL3. If PMCR_EL0.DP is 1, PMCCNTR_EL0 is disabled at EL3. Otherwise, PMCCNTR_EL0 is not affected by this mechanism. |

The counters affected by this field are:

- If EL2 is implemented and MDCR\_EL3.SPME is 1, event counters PMEVCNTR&lt;n&gt;\_EL0 in the first range.
- If EL2 is not implemented or MDCR\_EL3.SPME is 0, event counters in the first and second ranges.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter, PMICNTR\_EL0.
- If PMCR\_EL0.DP is 1, the cycle counter, PMCCNTR\_EL0.

Other event counters are not affected by this field. When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## MCCD,bit [34]

## When FEAT\_PMUv3p7 is implemented:

Monitor Cycle Counter Disable. Prohibits the Cycle Counter, PMCCNTR\_EL0, from counting at EL3.

| MCCD   | Meaning                                                          |
|--------|------------------------------------------------------------------|
| 0b0    | Cycle counting by PMCCNTR_EL0 is not affected by this mechanism. |
| 0b1    | Cycle counting by PMCCNTR_EL0 is prohibited at EL3.              |

This field does not affect the CPU\_CYCLES event or any other event that counts cycles.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SBRBE, bits [33:32]

## When FEAT\_BRBE is implemented:

Secure Branch Record Buffer Enable. Controls branch recording by the BRBE, and access to BRBE registers and instructions at EL2 and EL1.

| SBRBE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00    | Direct accesses to BRBE registers and instructions, except when in EL3, generate a Trap exception to EL3. EL0, EL1, and EL2 are prohibited regions.                                                                                                                                                                                                                                       |
| 0b01    | Direct accesses to BRBE registers and instructions in Secure state, except when in EL3, generate a Trap exception to EL3. EL0, EL1, and EL2 in Secure state are prohibited regions. This control does not cause any direct accesses to BRBE registers when not in Secure state to be trapped, and does not cause any Exception levels when not in Secure state to be a prohibited region. |
| 0b10    | Direct accesses to BRBE registers and instructions, except when in EL3, generate a Trap exception to EL3. This control does not cause any Exception levels to be prohibited regions.                                                                                                                                                                                                      |
| 0b11    | This control does not cause any direct accesses to BRBE registers or instruction to be trapped, and does not cause any Exception levels to be a prohibited region.                                                                                                                                                                                                                        |

The Branch Record Buffer registers trapped by this control are: BRBCR\_EL1, BRBCR\_EL2, BRBCR\_EL12, BRBFCR\_EL1, BRBIDR0\_EL1, BRBINF&lt;n&gt;\_EL1, BRBINFINJ\_EL1, BRBSRC&lt;n&gt;\_EL1, BRBSRCINJ\_EL1, BRBTGT&lt;n&gt;\_EL1, BRBTGTINJ\_EL1, and BRBTS\_EL1.

The Branch Record Buffer instructions trapped by this control are:

- BRBIALL.
- BRBINJ.

Note

If FEAT\_BRBEv1p1 is not implemented, EL3 is a prohibited region.

If EL3 is not implemented, then the Effective value of this field is 0b11 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

PMSSE, bits [31:30]

## When FEAT\_PMUv3\_SS is implemented:

Performance Monitors Snapshot Enable. Controls the generation of Capture events.

| PMSSE   | Meaning                                          |
|---------|--------------------------------------------------|
| 0b00    | Capture events are disabled.                     |
| 0b01    | Capture events are controlled by MDCR_EL2.PMSSE. |
| 0b10    | Capture events are enabled and prohibited.       |
| 0b11    | Capture events are enabled and allowed.          |

If EL3 is not implemented, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Cold reset, this field resets to '00' .

## Otherwise:

Reserved, RES0.

Bit [29]

Reserved, RES0.

## MTPME,bit [28]

## When FEAT\_MTPMU is implemented:

Multi-threaded PMU Enable. Enables use of the PMEVTYPER&lt;n&gt;\_EL0.MT bits.

| MTPME   | Meaning                                                                  |
|---------|--------------------------------------------------------------------------|
| 0b0     | FEAT_MTPMU is disabled. The Effective value of PMEVTYPER<n>_EL0.MT is 0. |
| 0b1     | PMEVTYPER<n>_EL0.MT bits not affected by this field.                     |

If FEAT\_MTPMU is disabled for any other PE in the system that has the same level 1 Affinity as the PE, it is IMPLEMENTATION DEFINED whether the PE behaves as if this field is 0.

The reset behavior of this field is:

- On a Cold reset, this field resets to '1' .

## Otherwise:

Reserved, RES0.

## TDCC, bit [27]

## When FEAT\_FGT is implemented:

Trap DCC. Traps use of the Debug Comms Channel at EL2, EL1, and EL0 to EL3.

| TDCC   | Meaning                                                                                                                                                                                                                              |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any register accesses to be trapped.                                                                                                                                                                     |
| 0b1    | Accesses to the DCCregisters at EL2, EL1, and EL0 generate a Trap exception to EL3, unless the access also generates a higher priority exception. Traps on the DCCdata transfer registers are ignored when the PE is in Debug state. |

The DCC registers trapped by this control are:

AArch64: OSDTRRX\_EL1, OSDTRTX\_EL1, MDCCSR\_EL0, MDCCINT\_EL1, and, when the PE is in Non-debug state, DBGDTR\_EL0, DBGDTRRX\_EL0, and DBGDTRTX\_EL0.

AArch32: DBGDTRRXext, DBGDTRTXext, DBGDSCRint, DBGDCCINT, and, when the PE is in Non-debug state, DBGDTRRXint and DBGDTRTXint.

The traps are reported with EC syndrome value:

- 0x05 for trapped AArch32 MRC and MCR accesses with coproc == 0b1110 .
- 0x06 for trapped AArch32 LDC to DBGDTRTXint and STC from DBGDTRRXint.
- 0x18 for trapped AArch64 MRS and MSR accesses.

When the PE is in Debug state, MDCR\_EL3.TDCC does not trap any accesses to:

AArch64: DBGDTR\_EL0, DBGDTRRX\_EL0, and DBGDTRTX\_EL0.

AArch32: DBGDTRRXint and DBGDTRTXint.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSTBE, bit [26]

## When FEAT\_TRBE is implemented and FEAT\_RME is implemented:

Non-secure Trace Buffer Extended. Together with MDCR\_EL3.NSTB, controls the trace buffer owning Security state and accesses to trace buffer System registers from EL2 and EL1.

For a description of the values derived by evaluating NSTB and NSTBE together, see MDCR\_EL3.NSTB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSTB, bits [25:24]

## When FEAT\_TRBE is implemented and FEAT\_RME is implemented:

Non-secure Trace Buffer. Together with MDCR\_EL3.NSTBE, controls the trace buffer owning Security state and accesses to trace buffer System registers from EL2 and EL1.

| NSTBE   | NSTB   | Meaning                                                                                                                                                                                                                                                                                                                                                                                       |
|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | 0b00   | Trace buffer owning Security state is Secure state. When TraceBufferEnabled()==TRUE, tracing is prohibited in Realm and Non-secure states. Accesses to trace buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception. When Secure state is not implemented, this encoding is reserved.                                             |
| 0b0     | 0b01   | Trace buffer owning Security state is Secure state. When TraceBufferEnabled()==TRUE, tracing is prohibited in Realm and Non-secure states. Accesses to trace buffer System registers at Realm and Non-secure EL2, and Realm and Non-secure EL1, are trapped to EL3, unless the access generates a higher priority exception. When Secure state is not implemented, this encoding is reserved. |
| 0b0     | 0b10   | Trace buffer owning Security state is Non-secure state. When TraceBufferEnabled()==TRUE, tracing is prohibited in Secure and Realm states. Accesses to trace buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception.                                                                                                              |
| 0b0     | 0b11   | Trace buffer owning Security state is Non-secure state. When TraceBufferEnabled()==TRUE, tracing is prohibited in Secure and Realm states. Accesses to trace buffer System registers at Secure and Realm EL2, and Secure and Realm EL1, are trapped to EL3, unless the access generates a higher priority exception.                                                                          |
| 0b1     | 0b10   | Trace buffer owning Security state is Realm state. When TraceBufferEnabled()==TRUE, tracing is prohibited in Secure and Non-secure states. Accesses to trace buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a highe priority exception.                                                                                                               |
| 0b1     | 0b11   | Trace buffer owning Security state is Realm state. When TraceBufferEnabled()==TRUE, tracing is prohibited in Secure and Non-secure states. Accesses to trace buffer System registers at Secure and Non-secure EL2, and Secure and Non-secure EL1, are trapped to EL3, unless the access generates a higher priority exception.                                                                |

All other combinations of MDCR\_EL3.NSTBE and MDCR\_EL3.NSTB are reserved.

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to TRBBASER\_EL1, TRBLIMITR\_EL1, TRBMAR\_EL1, TRBPTR\_EL1, TRBSR\_EL1, and TRBTRG\_EL1.
- If FEAT\_TRBE\_MPAM is implemented, MRS and MSR accesses to TRBMPAM\_EL1.
- If FEAT\_TRBE\_EXC is implemented, MRS and MSR accesses to TRBSR\_EL2 and TRBSR\_EL12.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3, reported using EC syndrome value 0x18 .

When TraceBufferEnabled() ==FALSE, these controls have no effect on whether tracing is prohibited.

If the Trace Buffer Unit is enabled and using Self-hosted mode, and MDCR\_EL3.{NSTB, NSTBE} selects a reserved value, then the behavior is CONSTRAINED UNPREDICTABLE, and the Trace Buffer Unit does one of:

- Behaves as if the Trace Buffer Unit is disabled.
- Selects an implemented Security state as the owning Security state.
- When trace data is received from the trace unit, it is not written to memory and the Trace Buffer Unit generates a trace buffer management event, as follows:
- TRBSR\_ELx.IRQ is set to 1.
- If TRBSR\_ELx.S is 0, then all of the following occur:
- TRBSR\_ELx.S is set to 1, Collection is stopped.
- TRBSR\_ELx.EC is set to 0x00 , Other buffer management event.
- TRBSR\_ELx.BSC is set to 0b000000 , Access not allowed.
- The other fields in TRBSR\_ELx are unchanged.

If the Trace Buffer Unit is enabled and using Self-hosted mode, and MDCR\_EL3.{NSTB, NSTBE} selects a reserved value, then it is CONSTRAINED UNPREDICTABLE whether or not accesses to trace buffer System registers at EL2 and EL1 generate Trap exceptions to EL3.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 1, then the Effective value of this field is 0b11 .

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_TRBE is implemented:

Non-secure Trace Buffer. Controls the trace buffer owning Security state and accesses to trace buffer System registers from EL2 and EL1.

| NSTB   | Meaning                                                                                                                                                                                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | Trace buffer owning Security state is Secure state. When TraceBufferEnabled() ==TRUE, tracing is prohibited in Non-secure state. Accesses to trace buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception.                     |
| 0b01   | Trace buffer owning Security state is Secure state. When TraceBufferEnabled() ==TRUE, tracing is prohibited in Non-secure state. Accesses to trace buffer System registers at EL2 and EL1 in Non-secure state are trapped to EL3, unless the access generates a higher priority exception. |
| 0b10   | Trace buffer owning Security state is Non-secure state. When TraceBufferEnabled() ==TRUE, tracing is prohibited in Secure state. Accesses to trace buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception.                     |
| 0b11   | Trace buffer owning Security state is Non-secure state. When TraceBufferEnabled() ==TRUE, tracing is prohibited in Secure state. Accesses to trace buffer System registers at EL2 and EL1 in Secure state are trapped to EL3, unless the access generates a higher priority exception.     |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to TRBBASER\_EL1, TRBLIMITR\_EL1, TRBMAR\_EL1, TRBPTR\_EL1, TRBSR\_EL1, and TRBTRG\_EL1.
- If FEAT\_TRBE\_MPAM is implemented, MRS and MSR accesses to TRBMPAM\_EL1.
- If FEAT\_TRBE\_EXC is implemented, MRS and MSR accesses to TRBSR\_EL2 and TRBSR\_EL12.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3, reported using EC syndrome value 0x18 .

When TraceBufferEnabled() ==FALSE, this control has no effect on whether tracing is prohibited.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 1, then the Effective value of this field is 0b11 .

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SCCD, bit [23]

## When FEAT\_PMUv3p5 is implemented:

Secure Cycle Counter Disable. Prohibits PMCCNTR\_EL0 from counting in Secure state and EL3.

| SCCD   | Meaning                                                              |
|--------|----------------------------------------------------------------------|
| 0b0    | Cycle counting by PMCCNTR_EL0 is not affected by this mechanism.     |
| 0b1    | Cycle counting by PMCCNTR_EL0 is prohibited in Secure state and EL3. |

This field does not affect the CPU\_CYCLES event or any other event that counts cycles.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## ETAD, bit [22]

## When FEAT\_RME is implemented, FEAT\_TRC\_EXT is implemented, and FEAT\_TRBE is implemented:

External Trace Access Disable. Together with MDCR\_EL3.ETADE, controls access to trace unit registers by an external debugger.

| ETADE   | ETAD   | Meaning                                                                                                                                                                                                     |
|---------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | 0b0    | No accesses from an external debugger to trace unit registers are prohibited by this control.                                                                                                               |
| 0b0     | 0b1    | Realm and Non-secure accesses from an external debugger to trace unit registers are prohibited. Other accesses from an external debugger to trace unit registers are not affected by this control.          |
| 0b1     | 0b0    | Secure and Non-secure accesses from an external debugger to trace unit registers are prohibited. Other accesses from an external debugger to trace unit registers are not affected by this control.         |
| 0b1     | 0b1    | Secure, Non-secure, and Realm accesses from an external debugger to trace unit registers are prohibited. Other accesses from an external debugger to trace unit registers are not affected by this control. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_TRC\_EXT is implemented and FEAT\_TRBE is implemented:

External Trace Access Disable. Controls Non-secure access to trace unit registers by an external debugger.

| ETAD   | Meaning                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the trace unit registers are prohibited by this control.                                                 |
| 0b1    | Non-secure accesses from an external debugger to some trace unit registers are prohibited. See individual registers for the effect of this field. |

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EPMAD, bit [21]

## When FEAT\_RME is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable. Together with MDCR\_EL3.EPMADE, controls access to Performance Monitor registers by an external debugger.

External accesses of the following Performance Monitor registers are affected by this control:

- PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCFGR, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMCR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMINTENCLR\_EL1, PMINTENSET\_EL1, PMOVSCLR\_EL0, and PMOVSSET\_EL0.
- If PMEVFILT2R&lt;n&gt; is implemented, PMEVFILT2R&lt;n&gt;.
- If implemented, PMIIDR.
- If PMSWINC\_EL0 is implemented in the external view, PMSWINC\_EL0.
- If FEAT\_PMUv3p4 is implemented, PMMIR.
- If FEAT\_PMUv3\_EXT64 is implemented, PMCNTEN, PMINTEN, and PMOVS.
- If FEAT\_PMUv3p9 is implemented, PMZR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, PMCGCR0, PMICFILTR\_EL0, and PMICNTR\_EL0.
- If FEAT\_PCSRv8p9 is implemented, PMPCSCTL.

| EPMADE   | EPMAD   | Meaning                                                                                                                                                                                                                                         |
|----------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | 0b0     | No accesses from an external debugger to affected Performance Monitor registers are prohibited by this control.                                                                                                                                 |
| 0b0      | 0b1     | Realm and Non-secure accesses from an external debugger to affected Performance Monitor registers are prohibited. Other accesses from an external debugger to affected Performance Monitor registers are not affected by this control.          |
| 0b1      | 0b0     | Secure and Non-secure accesses from an external debugger to affected Performance Monitor registers are prohibited. Other accesses from an external debugger to affected Performance Monitor registers are not affected by this control.         |
| 0b1      | 0b1     | Secure, Non-secure, and Realm accesses from an external debugger to affected Performance Monitor registers are prohibited. Other accesses from an external debugger to affected Performance Monitor registers are not affected by this control. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_Debugv8p4 is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable. Controls Non-secure access to Performance Monitor registers by an external debugger.

External accesses of the following Performance Monitor registers are affected by this control:

- PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCFGR, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMCR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMINTENCLR\_EL1, PMINTENSET\_EL1, PMOVSCLR\_EL0, and PMOVSSET\_EL0.
- If PMEVFILT2R&lt;n&gt; is implemented, PMEVFILT2R&lt;n&gt;.
- If implemented, PMIIDR.
- If PMSWINC\_EL0 is implemented in the external view, PMSWINC\_EL0.
- If FEAT\_PMUv3p4 is implemented, PMMIR.
- If FEAT\_PMUv3\_EXT64 is implemented, PMCNTEN, PMINTEN, and PMOVS.
- If FEAT\_PMUv3p9 is implemented, PMZR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, PMCGCR0, PMICFILTR\_EL0, and PMICNTR\_EL0.
- If FEAT\_PCSRv8p9 is implemented, PMPCSCTL.

| EPMAD   | Meaning                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------|
| 0b0     | No accesses from an external debugger to the Performance Monitor registers are prohibited by this control.  |
| 0b1     | Non-secure accesses from an external debugger to the affected Performance Monitor registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable. Controls access to Performance Monitor registers by an external debugger.

External accesses of the following Performance Monitor registers are affected by this control:

- PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCFGR, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMCR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMINTENCLR\_EL1, PMINTENSET\_EL1, PMOVSCLR\_EL0, and PMOVSSET\_EL0.
- If PMEVFILT2R&lt;n&gt; is implemented, PMEVFILT2R&lt;n&gt;.
- If implemented, PMIIDR.
- If PMSWINC\_EL0 is implemented in the external view, PMSWINC\_EL0.
- If FEAT\_PMUv3p4 is implemented, PMMIR.

| EPMAD   | Meaning                                                                                                                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | No accesses from an external debugger to the Performance Monitor registers are prohibited by this control.                                                                                                                |
| 0b1     | If the IMPLEMENTATION DEFINED authentication interface function ExternalSecureInvasiveDebugEnabled() returns FALSE, then accesses from an external debugger to the affected Performance Monitor registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EDAD, bit [20]

## When FEAT\_RME is implemented:

External Debug Access Disable. Together with MDCR\_EL3.EDADE, controls access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger.

External accesses of the following debug registers are affected by this control:

- DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGWCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, and OSLAR\_EL1.

| EDADE   | EDAD   | Meaning                                                                                                                                                                                                             |
|---------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | 0b0    | No accesses from an external debugger to affected debug registers are prohibited by this control.                                                                                                                   |
| 0b0     | 0b1    | Realm and Non-secure accesses from an external debugger to affected debug registers are prohibited. Other accesses from an external debugger to affected debug registers are not affected by this control.          |
| 0b1     | 0b0    | Secure and Non-secure accesses from an external debugger to affected debug registers are prohibited. Other accesses from an external debugger to affected debug registers are not affected by this control.         |
| 0b1     | 0b1    | Secure, Non-secure, and Realm accesses from an external debugger to affected debug registers are prohibited. Other accesses from an external debugger to affected debug registers are not affected by this control. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_Debugv8p4 is implemented:

External Debug Access Disable. Controls Non-secure access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger.

External accesses of the following debug registers are affected by this control:

- DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGWCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, and OSLAR\_EL1.

| EDAD   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the debug registers are prohibited by this control.  |
| 0b1    | Non-secure accesses from an external debugger to the affected debug registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_Debugv8p2 is implemented:

External Debug Access Disable. Controls access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger.

External accesses of the following debug registers are affected by this control:

- DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGWCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, and OSLAR\_EL1.

| EDAD   | Meaning                                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the debug registers are prohibited by this control.                                                                                                                |
| 0b1    | If the IMPLEMENTATION DEFINED authentication interface function ExternalSecureInvasiveDebugEnabled() returns FALSE, then accesses from an external debugger to the affected debug registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

External Debug Access Disable. Controls access to breakpoint registers, watchpoint registers, and optionally OSLAR\_EL1 by an external debugger.

External accesses of the following debug registers are affected by this control:

- DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGWCR&lt;n&gt;\_EL1, and DBGWVR&lt;n&gt;\_EL1.
- It is IMPLEMENTATION DEFINED whether this control affects OSLAR\_EL1.

| EDAD   | Meaning                                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the debug registers are prohibited by this control.                                                                                                                |
| 0b1    | If the IMPLEMENTATION DEFINED authentication interface function ExternalSecureInvasiveDebugEnabled() returns FALSE, then accesses from an external debugger to the affected debug registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## TTRF, bit [19]

## When FEAT\_TRF is implemented:

Trap Trace Filter controls. Traps use of the Trace Filter control registers at EL2 and EL1 to EL3.

The Trace Filter registers trapped by this control are:

- TRFCR\_EL2, TRFCR\_EL12, TRFCR\_EL1, reported using EC syndrome value 0x18 .
- HTRFCR and TRFCR, reported using EC syndrome value 0x03 .

| TTRF   | Meaning                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses to Trace Filter registers at EL2 and EL1 are not affected by this field.                                                            |
| 0b1    | Accesses to Trace Filter registers at EL2 and EL1 generate a Trap exception to EL3, unless the access generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

STE, bit [18]

## When FEAT\_TRF is implemented and Secure state is implemented:

Secure Trace enable. Enables tracing in Secure state.

| STE   | Meaning                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------|
| 0b0   | Trace prohibited in Secure state unless overridden by the IMPLEMENTATION DEFINED authentication interface. |
| 0b1   | Trace in Secure state is not affected by this field.                                                       |

This field also controls the level of authentication required by an external debugger to enable external tracing. See 'Register controls to enable self-hosted trace'.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SPME, bit [17]

## When FEAT\_PMUv3 is implemented and FEAT\_PMUv3p7 is implemented:

Secure Performance Monitors Enable. Controls PMU operation in Secure state and at EL3 when MDCR\_EL3.MPMX is 0.

| SPME   | Meaning                                                                                                                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Affected counters are prohibited from counting in Secure state and at EL3. If PMCR_EL0.DP is 1, PMCCNTR_EL0 is disabled in Secure state and at EL3. Otherwise, PMCCNTR_EL0 is not affected by this mechanism. |
| 0b1    | Counters are not affected by this mechanism.                                                                                                                                                                  |

When MDCR\_EL3.MPMX is 0, the counters affected by this field are:

- Event counters in the first and second ranges. For more information about event counter ranges, see MDCR\_EL2.HPMN.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter, PMICNTR\_EL0.
- If PMCR\_EL0.DP is 1, the cycle counter, PMCCNTR\_EL0.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

When MDCR\_EL3.MPMX is 1, this field controls which event counters are affected by MDCR\_EL3.MPMX at EL3. See MDCR\_EL3.MPMX for more information.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_PMUv3 is implemented and FEAT\_Debugv8p2 is implemented:

Secure Performance Monitors Enable. Controls PMU operation in Secure state.

| SPME   | Meaning                                                                                                                                                               |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Event counting is prohibited in Secure state. If PMCR_EL0.DP is 1, PMCCNTR_EL0 is disabled in Secure state. Otherwise, PMCCNTR_EL0 is not affected by this mechanism. |
| 0b1    | Event counting and PMCCNTR_EL0 are not affected by this mechanism.                                                                                                    |

The counters affected by this field are:

- All event counters.
- If PMCR\_EL0.DP is 1, the cycle counter, PMCCNTR\_EL0.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## When FEAT\_PMUv3 is implemented:

Secure Performance Monitors Enable. Controls PMU operation in Secure state.

| SPME   | Meaning                                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If ExternalSecureNoninvasiveDebugEnabled() is FALSE, then all the following apply: • Event counting is prohibited in Secure state. • If PMCR_EL0.DP is 1, PMCCNTR_EL0 is disabled in Secure state. Otherwise, PMCCNTR_EL0 is not affected by this mechanism. |
| 0b1    | Event counting and PMCCNTR_EL0 are not affected by this mechanism.                                                                                                                                                                                           |

If ExternalSecureNoninvasiveDebugEnabled() is TRUE, then the event counters and PMCCNTR\_EL0 are not affected by this field.

Otherwise, the counters affected by this field are:

- All event counters.
- If PMCR\_EL0.DP is 1, the cycle counter, PMCCNTR\_EL0.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SDD, bit [16]

When Secure state is implemented:

AArch64 Secure Self-hosted invasive debug disable. Disables Software debug exceptions in Secure state, other than Breakpoint Instruction exceptions.

| SDD   | Meaning                                                                                                                 |
|-------|-------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Debug exceptions in Secure state are not affected by this field.                                                        |
| 0b1   | Debug exceptions, other than Breakpoint Instruction exceptions, are disabled from all Exception levels in Secure state. |

The SDD bit is ignored unless both of the following are true:

- The PE is in Secure state.
- The Effective value of SCR\_EL3.RW is 0.

If Secure EL2 is implemented and enabled, and Secure EL1 is using AArch32, then:

- If debug exceptions from Secure EL1 are enabled, debug exceptions from Secure EL0 are also enabled.
- Otherwise, debug exceptions from Secure EL0 are enabled only if the value of SDER32\_EL3.SUIDEN is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SPD32, bits [15:14]

## When FEAT\_AA32EL1 is implemented:

AArch32 Secure self-hosted privileged debug. Enables or disables debug exceptions from Secure EL1 using AArch32, other than Breakpoint Instruction exceptions.

| SPD32   | Meaning                                                                                                           |
|---------|-------------------------------------------------------------------------------------------------------------------|
| 0b00    | Legacy mode. Debug exceptions from Secure EL1 are enabled by the IMPLEMENTATION DEFINED authentication interface. |
| 0b10    | Secure privileged debug disabled. Debug exceptions from Secure EL1 are disabled.                                  |
| 0b11    | Secure privileged debug enabled. Debug exceptions from Secure EL1 are enabled.                                    |

Other values are reserved, and have the CONSTRAINED UNPREDICTABLE behavior that they must have the same behavior as 0b00 . Software must not rely on this property as the behavior of reserved values might change in a future revision of the architecture.

This field has no effect on Breakpoint Instruction exceptions. These are always enabled.

This field is ignored unless both of the following are true:

- The PE is in Secure state.
- The Effective value of SCR\_EL3.RW is 0.

If Secure EL1 is using AArch32, then:

- If debug exceptions from Secure EL1 are enabled, then debug exceptions from Secure EL0 are also enabled.

- Otherwise, debug exceptions from Secure EL0 are enabled only if the value of SDER32\_EL3.SUIDEN is 1.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 0b11 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSPB, bits [13:12]

## When FEAT\_SPE is implemented and FEAT\_RME is implemented:

Non-secure Profiling Buffer. Together with MDCR\_EL3.NSPBE, controls the Profiling Buffer owning Security state and accesses to Statistical Profiling and Profiling Buffer System registers from EL2 and EL1.

| NSPBE   | NSPB   | Meaning                                                                                                                                                                                                                                                                                                                                                                                        |
|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | 0b00   | Profiling Buffer owning Security state is Secure state. Profiling is disabled in Realm and Non-secure states. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception. When Secure state is not implemented, this encoding is reserved.                                             |
| 0b0     | 0b01   | Profiling Buffer owning Security state is Secure state. Profiling is disabled in Realm and Non-secure states. Accesses to Statistical Profiling and Profiling Buffer System registers at Realm and Non-secure EL2, and Realm and Non-secure EL1, are trapped to EL3, unless the access generates a higher priority exception. When Secure state is not implemented, this encoding is reserved. |
| 0b0     | 0b10   | Profiling Buffer owning Security state is Non-secure state. Profiling is disabled in Secure and Realm states. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception.                                                                                                              |
| 0b0     | 0b11   | Profiling Buffer owning Security state is Non-secure state. Profiling is disabled in Secure and Realm states. Accesses to Statistical Profiling and Profiling Buffer System registers at Secure and Realm EL2, and Secure and Realm EL1, are trapped to EL3, unless the access generates a higher priority exception.                                                                          |
| 0b1     | 0b10   | Profiling Buffer owning Security state is Realm state. Profiling is disabled in Secure and Non-secure states. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a highe priority exception.                                                                                                               |
| 0b1     | 0b11   | Profiling Buffer owning Security state is Realm state. Profiling is disabled in Secure and Non-secure states. Accesses to Statistical Profiling and Profiling Buffer System registers at Secure and Non-secure EL2, and Secure and Non-secure EL1, are trapped to EL3, unless the access generates a higher priority exception.                                                                |

All other combinations of MDCR\_EL3.NSPBE and MDCR\_EL3.NSPB are reserved.

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMBLIMITR\_EL1, PMBPTR\_EL1, PMBSR\_EL1, PMSCR\_EL1, PMSCR\_EL2, PMSCR\_EL12, PMSEVFR\_EL1, PMSFCR\_EL1, PMSICR\_EL1, PMSIRR\_EL1, and PMSLATFR\_EL1.
- MRS accesses to PMSIDR\_EL1.
- If FEAT\_SPE\_FnE is implemented, MRS and MSR accesses to PMSNEVFR\_EL1.
- If FEAT\_SPE\_FDS is implemented, MRS and MSR accesses to PMSDSFR\_EL1.
- If FEAT\_SPE\_EXC is implemented, MRS and MSR accesses to PMBSR\_EL2 and PMBSR\_EL12.
- If FEAT\_SPE\_nVM is implemented, MRS and MSR accesses to PMBMAR\_EL1.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3, reported using EC syndrome value 0x18 .

If profiling is enabled and MDCR\_EL3.{NSPB, NSPBE} selects a reserved value, then the behavior is CONSTRAINED UNPREDICTABLE, and the Statistical Profiling Unit does one of:

- Behaves as if profiling is disabled.
- Selects an implemented Security state as the owning Security state.
- When profiling data is generated, it is not written to memory and the Statistical Profiling Unit generates a Profiling Buffer management event, as follows:
- If PMBSR\_ELx.S is 0, then all of the following occur:
- PMBSR\_ELx.S is set to 1.
- PMBSR\_ELx.DL is set to 1.
- PMBSR\_ELx.EC is set to 0b000000 , Other buffer management event.
- PMBSR\_ELx.BSC is set to 0b000000 , Access not allowed.
- The other fields in PMBSR\_ELx are unchanged.

If profiling is enabled and MDCR\_EL3.{NSPB, NSPBE} selects a reserved value, then it is CONSTRAINED UNPREDICTABLE whether or not accesses to the Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 generate Trap exceptions to EL3.

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 1, then the Effective value of this field is 0b11 .

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_SPE is implemented:

Non-secure Profiling Buffer. Controls the Profiling Buffer owning Security state and accesses to Statistical Profiling and Profiling Buffer System registers from EL2 and EL1.

| NSPB   | Meaning                                                                                                                                                                                                                                                                                    |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | Profiling Buffer owning Security state is Secure state. Profiling is disabled in Non-secure state. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception.                     |
| 0b01   | Profiling Buffer owning Security state is Secure state. Profiling is disabled in Non-secure state. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 in Non-secure state are trapped to EL3, unless the access generates a higher priority exception. |
| 0b10   | Profiling Buffer owning Security state is Non-secure state. Profiling is disabled in Secure state. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 are trapped to EL3, unless the access generates a higher priority exception.                     |
| 0b11   | Profiling Buffer owning Security state is Non-secure state. Profiling is disabled in Secure state. Accesses to Statistical Profiling and Profiling Buffer System registers at EL2 and EL1 in Secure state are trapped to EL3, unless the access generates a higher priority exception.     |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMBLIMITR\_EL1, PMBPTR\_EL1, PMBSR\_EL1, PMSCR\_EL1, PMSCR\_EL2, PMSCR\_EL12, PMSEVFR\_EL1, PMSFCR\_EL1, PMSICR\_EL1, PMSIRR\_EL1, and PMSLATFR\_EL1.
- MRS accesses to PMSIDR\_EL1.
- If FEAT\_SPE\_FnE is implemented, MRS and MSR accesses to PMSNEVFR\_EL1.
- If FEAT\_SPE\_FDS is implemented, MRS and MSR accesses to PMSDSFR\_EL1.
- If FEAT\_SPE\_EXC is implemented, MRS and MSR accesses to PMBSR\_EL2 and PMBSR\_EL12.
- If FEAT\_SPE\_nVM is implemented, MRS and MSR accesses to PMBMAR\_EL1.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL3, reported using EC syndrome value 0x18 .

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 1, then the Effective value of this field is 0b11 .

If EL3 is not implemented and the Effective value of SCR\_EL3.NS is 0, then the Effective value of this field is 0b01 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSPBE, bit [11]

## When FEAT\_SPE is implemented and FEAT\_RME is implemented:

Non-secure Profiling Buffer Extended. Together with MDCR\_EL3.NSPB, controls the Profiling Buffer owning Security state and accesses to Statistical Profiling and Profiling Buffer System registers from EL2 and EL1.

For a description of the values derived by evaluating NSPB and NSPBE together, see MDCR\_EL3.NSPB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TDOSA, bit [10]

## When FEAT\_DoubleLock is implemented:

Trap debug OS-related register access. Traps EL2 and EL1 System register accesses to the powerdown debug registers to EL3.

Accesses to the registers are trapped as follows:

- Accesses from AArch64 state, OSLAR\_EL1, OSLSR\_EL1, OSDLR\_EL1, DBGPRCR\_EL1, and any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this field, are trapped to EL3 and reported using EC syndrome value 0x18 .
- Accesses using MCR or MRC to DBGOSLAR, DBGOSLSR, DBGOSDLR, and DBGPRCR, are trapped to EL3 and reported using EC syndrome value 0x05 .
- Accesses to any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this field.

| TDOSA   | Meaning                                                                                                                                         |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                                     |
| 0b1     | EL2 and EL1 System register accesses to the powerdown debug registers are trapped to EL3, unless it is trapped by HDCR.TDOSA or MDCR_EL2.TDOSA. |

| Note                                                     |
|----------------------------------------------------------|
| The powerdown debug registers are not accessible at EL0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Trap debug OS-related register access. Traps EL2 and EL1 System register accesses to the powerdown debug registers to EL3.

The following registers are affected by this trap:

- AArch64: OSLAR\_EL1, OSLSR\_EL1, and DBGPRCR\_EL1.
- AArch32: DBGOSLAR, DBGOSLSR, and DBGPRCR.
- AArch64 and AArch32: Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this field.
- It is IMPLEMENTATION DEFINED whether accesses to OSDLR\_EL1 and DBGOSDLR are trapped.

| TDOSA   | Meaning                                                                                                                                         |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                                     |
| 0b1     | EL2 and EL1 System register accesses to the powerdown debug registers are trapped to EL3, unless it is trapped by HDCR.TDOSA or MDCR_EL2.TDOSA. |

Note

The powerdown debug registers are not accessible at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TDA, bit [9]

Trap accesses of debug System registers. Enables a trap to EL3 on accesses of debug System registers.

| TDA   | Meaning                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses of the specified debug System registers are not trapped by this mechanism.                                                                     |
| 0b1   | Accesses of the specified debug System registers at EL2, EL1, and EL0 are trapped to EL3, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to DBGAUTHSTATUS\_EL1, DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGCLAIMCLR\_EL1, DBGCLAIMSET\_EL1, DBGVCR32\_EL2, DBGWCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, MDCCINT\_EL1, MDCCSR\_EL0, MDCR\_EL2, MDRAR\_EL1, MDSCR\_EL1, OSDTRRX\_EL1, OSDTRTX\_EL1, and OSECCR\_EL1.
- If FEAT\_Debugv8p9 is implemented, MRS and MSR accesses to MDSELR\_EL1.
- If FEAT\_STEP2 is implemented, MRS and MSR accesses to MDSTEPOP\_EL1.
- In Non-debug state, MRS accesses to DBGDTRRX\_EL0 and DBGDTR\_EL0 and MSR accesses to DBGDTRTX\_EL0 and DBGDTR\_EL0.

In AArch32 state, the instructions affected by this control are:

- MRC and MCR accesses to DBGAUTHSTATUS, DBGBCR&lt;n&gt;, DBGBVR&lt;n&gt;, DBGBXVR&lt;n&gt;, DBGCLAIMCLR, DBGCLAIMSET, DBGDCCINT, DBGDEVID, DBGDEVID1, DBGDEVID2, DBGDIDR, DBGDRAR, DBGDSAR, DBGDSCRext, DBGDSCRint, DBGDTRRXext, DBGDTRTXext, DBGOSECCR, DBGVCR, DBGWCR&lt;n&gt;, DBGWFAR, DBGWVR&lt;n&gt;, HDCR, and SDER.
- MRRC accesses to DBGDRAR and DBGDSAR.
- STC accesses to DBGDTRRXint and LDC accesses to DBGDTRTXint.

- In Non-debug state, MRC accesses to DBGDTRRXint and MCR accesses to DBGDTRTXint.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x03 for MRC and MCR accesses with coproc == 0b1111 , 0x05 for MCR and MCR accesses with coproc == 0b1110 , 0x06 for LDC and STC accesses, and 0x0C for MRRC accesses.

The following instructions are not trapped in Debug state:

- AArch64 MRS accesses to DBGDTRRX\_EL0 and DBGDTR\_EL0 and MSR accesses to DBGDTRTX\_EL0 and DBGDTR\_EL0.
- AArch32 MRC accesses to DBGDTRRXint and MCR accesses to DBGDTRTXint.

If 16 or fewer breakpoints and 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI, then it is IMPLEMENTATION DEFINED whether AArch64 accesses to MDSELR\_EL1 are trapped to EL3 when MDCR\_EL3.TDA is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [8]

Reserved, RES0.

## EnPM2, bit [7]

When FEAT\_PMUv3p9 is implemented, or FEAT\_SPMU is implemented, or FEAT\_EBEP is implemented, or FEAT\_PMUv3\_SS is implemented, or FEAT\_SPMU2 is implemented:

Enable access to PMU registers. When disabled, accesses to PMU registers generate a trap to EL3.

| EnPM2   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Accesses of the specified PMUregisters at EL2, EL1, and EL0 are trapped to EL3, unless the instruction generates a higher priority exception. If FEAT_PMUv3_ICNTR is implemented, then: • PMCNTENCLR_EL0.F0, PMCNTENSET_EL0.F0, PMOVSCLR_EL0.F0, PMOVSSET_EL0.F0, and PMZR_EL0.F0 read-as-zero and ignore writes at EL2, EL1, and EL0. • PMINTENCLR_EL1.F0 and PMINTENSET_EL1.F0 read-as-zero and ignore writes at EL2 and EL1. |
| 0b1     | Accesses of the specified PMUregisters are not trapped by this mechanism.                                                                                                                                                                                                                                                                                                                                                       |

In AArch64 state, the instructions affected by this control are:

- If FEAT\_EBEP is implemented or FEAT\_PMUv3\_SS is implemented, MRS and MSR accesses to PMECR\_EL1.
- If FEAT\_PMUv3\_ICNTR is implemented, MRS and MSR accesses to PMICFILTR\_EL0 and PMICNTR\_EL0.
- If FEAT\_PMUv3p9 is implemented, MRS and MSR accesses to PMUACR\_EL1.
- If FEAT\_SEBEP is implemented, MRS and MSR accesses to PMIAR\_EL1.
- If FEAT\_SPMU is implemented, MRS and MSR accesses to SPMACCESSR\_EL1, SPMACCESSR\_EL2, SPMACCESSR\_EL12, SPMCFGR\_EL1, SPMCGCR&lt;n&gt;\_EL1, SPMCNTENCLR\_EL0, SPMCNTENSET\_EL0, SPMCR\_EL0, SPMDEVAFF\_EL1, SPMDEVARCH\_EL1, SPMEVCNTR&lt;n&gt;\_EL0, SPMEVFILT2R&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, SPMEVTYPER&lt;n&gt;\_EL0, SPMIIDR\_EL1, SPMINTENCLR\_EL1, SPMINTENSET\_EL1, SPMOVSCLR\_EL0, SPMOVSSET\_EL0, SPMSCR\_EL1, and SPMSELR\_EL0.
- If FEAT\_SPMU2 is implemented, MSR writes to SPMZR\_EL0.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TPM, bit [6]

## When FEAT\_PMUv3 is implemented:

Trap accesses of PMU registers. Enables a trap to EL3 on accesses of PMU registers.

| TPM   | Meaning                                                                                                                                       |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses of the specified PMUregisters are not trapped by this mechanism.                                                                     |
| 0b1   | Accesses of the specified PMUregisters at EL2, EL1, and EL0 are trapped to EL3, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to PMCCFILTR\_EL0, PMCCNTR\_EL0, PMCNTENCLR\_EL0, PMCNTENSET\_EL0, PMCR\_EL0, PMEVCNTR&lt;n&gt;\_EL0, PMEVTYPER&lt;n&gt;\_EL0, PMINTENCLR\_EL1, PMINTENSET\_EL1, PMOVSCLR\_EL0, PMOVSSET\_EL0, PMSELR\_EL0, PMSWINC\_EL0, PMUSERENR\_EL0, PMXEVCNTR\_EL0, and PMXEVTYPER\_EL0.
- MRS accesses to PMCEID0\_EL0 and PMCEID1\_EL0.
- If FEAT\_PMUv3p4 is implemented, MRS accesses to PMMIR\_EL1.
- If FEAT\_PMUv3p9 is implemented, MSR accesses to PMZR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, MRS and MSR accesses to PMICFILTR\_EL0 and PMICNTR\_EL0.
- If FEAT\_EBEP is implemented or FEAT\_PMUv3\_SS is implemented, MRS and MSR accesses to PMECR\_EL1.
- If FEAT\_SEBEP is implemented, MRS and MSR accesses to PMIAR\_EL1.

In AArch32 state, the instructions affected by this control are:

- MRC and MCR accesses to PMCCFILTR, PMCCNTR, PMCEID0, PMCEID1, PMCNTENCLR, PMCNTENSET, PMCR, PMEVCNTR&lt;n&gt;, PMEVTYPER&lt;n&gt;, PMINTENCLR, PMINTENSET, PMOVSR, PMOVSSET, PMSELR, PMSWINC, PMUSERENR, PMXEVCNTR, and PMXEVTYPER.
- MRRC and MCRR accesses to PMCCNTR.
- If FEAT\_PMUv3p1 is implemented, MRC accesses to PMCEID2 and PMCEID3.
- If FEAT\_PMUv3p4 is implemented, MRC accesses to PMMIR.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x03 for MRC and MCR accesses, and 0x04 for MRRC and MCRR accesses.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [5]

Reserved, RES0.

## EDADE, bit [4]

## When FEAT\_RME is implemented:

External Debug Access Disable Extended. Together with MDCR\_EL3.EDAD, controls access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger.

For a description of the values derived by evaluating MDCR\_EL3.EDAD and MDCR\_EL3.EDADE together, see MDCR\_EL3.EDAD.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## ETADE, bit [3]

## When FEAT\_RME is implemented, FEAT\_TRC\_EXT is implemented, and FEAT\_TRBE is implemented:

External Trace Access Disable Extended. Together with MDCR\_EL3.ETAD, controls access to trace unit registers by an external debugger.

For a description of the values derived by evaluating MDCR\_EL3.ETAD and MDCR\_EL3.ETADE together, see MDCR\_EL3.ETAD.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EPMADE, bit [2]

## When FEAT\_RME is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable Extended. Together with MDCR\_EL3.EPMAD, controls access to Performance Monitor registers by an external debugger.

For a description of the values derived by evaluating MDCR\_EL3.EPMAD and MDCR\_EL3.EPMADE together, see MDCR\_EL3.EPMAD.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [1]

Reserved, RES0.

## RLTE, bit [0]

## When FEAT\_RME is implemented and FEAT\_TRF is implemented:

Realm Trace enable. Enables tracing in Realm state.

| RLTE   | Meaning                                                                                                    |
|--------|------------------------------------------------------------------------------------------------------------|
| 0b0    | Trace prohibited in Realm state, unless overridden by the IMPLEMENTATION DEFINED authentication interface. |
| 0b1    | Trace in Realm state is not affected by this field.                                                        |

This field also controls the level of authentication that is required by an external debugger to enable external tracing.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Accessing MDCR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0011 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = MDCR_EL3;
```

MSR MDCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0011 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.MDCR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else MDCR_EL3 = X[t, 64];
```

## D24.3.19 MDRAR\_EL1, Monitor Debug ROM Address Register

The MDRAR\_EL1 characteristics are:

## Purpose

Defines the base physical address of a 4KB-aligned memory-mapped debug component, usually a ROM table that locates and describes the memory-mapped debug components in the system. Use of this register is deprecated.

## Configuration

AArch64 System register MDRAR\_EL1 bits [63:0] are architecturally mapped to AArch32 System register DBGDRAR[63:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MDRAR\_EL1 are UNDEFINED.

## Attributes

MDRAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

ROMADDR,bits [55:12]

When FEAT\_D128 is implemented and MDRAR\_EL1.Valid != '00':

<!-- image -->

## ROMADDR,bits [43:0]

Bits [55:12] of the ROM table physical address.

Bits [11:0] of the ROM table physical address are zero.

This field has an IMPLEMENTATION DEFINED value.

For implementations with fewer than 56 physical address bits, the corresponding upper bits of this field are RES0

In an implementation that includes EL3, ROMADDR is an address in Non-secure PA space. It is IMPLEMENTATION DEFINED whether the ROM table is also accessible in Secure PA space. If FEAT\_RME is

implemented, it is IMPLEMENTATION DEFINED whether the ROM table is also accessible in the Root or Realm PA spaces.

Arm strongly recommends that bits ROMADDR[(PAsize-1):32] are zero in any system where the implementation only supports execution in AArch32 state.

Access to this field is RO.

## When FEAT\_D128 is not implemented, FEAT\_LPA is implemented, and MDRAR\_EL1.Valid != '00':

<!-- image -->

## Bits [43:40]

Reserved, RES0.

## ROMADDR,bits [39:0]

Bits [51:12] of the ROM table physical address.

Bits [11:0] of the ROM table physical address are zero.

This field has an IMPLEMENTATION DEFINED value.

For implementations with fewer than 52 physical address bits, the corresponding upper bits of this field are RES0

In an implementation that includes EL3, ROMADDR is an address in Non-secure PA space. It is IMPLEMENTATION DEFINED whether the ROM table is also accessible in Secure PA space. If FEAT\_RME is implemented, it is IMPLEMENTATION DEFINED whether the ROM table is also accessible in the Root or Realm PA spaces.

Arm strongly recommends that bits ROMADDR[(PAsize-1):32] are zero in any system where the implementation only supports execution in AArch32 state.

Access to this field is RO.

## When FEAT\_D128 is not implemented, FEAT\_LPA is not implemented, and MDRAR\_EL1.Valid != '00':

<!-- image -->

## Bits [43:36]

Reserved, RES0.

## ROMADDR,bits [35:0]

Bits [39:12] of the ROM table physical address.

Bits [11:0] of the ROM table physical address are zero.

This field has an IMPLEMENTATION DEFINED value.

For implementations with fewer than 48 physical address bits, the corresponding upper bits of this field are RES0

In an implementation that includes EL3, ROMADDR is an address in Non-secure PA space. It is IMPLEMENTATION DEFINED whether the ROM table is also accessible in Secure PA space. If FEAT\_RME is implemented, it is IMPLEMENTATION DEFINED whether the ROM table is also accessible in Root or Realm PA spaces.

Arm strongly recommends that bits ROMADDR[(PAsize-1):32] are zero in any system where the implementation only supports execution in AArch32 state.

Access to this field is RO.

## When MDRAR\_EL1.Valid == '00':

<!-- image -->

## Bits [43:0]

Reserved, UNKNOWN.

## Bits [11:2]

Reserved, RES0.

## Valid, bits [1:0]

This field indicates whether the ROM Table address is valid.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Valid   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b00    | ROMTable address is not valid. Software must ignore ROMADDR. |
| 0b11    | ROMTable address is valid.                                   |

Other values are reserved.

Arm recommends implementations set this field to zero.

Access to this field is RO.

## Accessing MDRAR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MDRAR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && MDCR_EL2.<TDE,TDRA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDRAR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDRAR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MDRAR_EL1;
```

## D24.3.20 MDSCR\_EL1, Monitor Debug System Control Register

The MDSCR\_EL1 characteristics are:

## Purpose

Main control register for the debug implementation.

## Configuration

AArch64 System register MDSCR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGDSCRext[31:0].

AArch64 System register MDSCR\_EL1 bit [15] is architecturally mapped to AArch32 System register DBGDSCRint[15].

AArch64 System register MDSCR\_EL1 bit [12] is architecturally mapped to AArch32 System register DBGDSCRint[12].

AArch64 System register MDSCR\_EL1 bits [5:2] are architecturally mapped to AArch32 System register DBGDSCRint[5:2].

AArch64 System register MDSCR\_EL1 bits [31:29, 27:26, 23:21, 19, 14, 6] are architecturally mapped to External register EDSCR[31:29, 27:26, 23:21, 19, 14, 6].

AArch64 System register MDSCR\_EL1 bits [35, 33] are architecturally mapped to External register EDSCR2[3, 1].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MDSCR\_EL1 are UNDEFINED.

## Attributes

MDSCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:51]

Reserved, RES0.

## EnSTEPOP, bit [50]

## When FEAT\_STEP2 is implemented:

Software step control bit. Enable execution from MDSTEPOP\_EL1. Permitted values are:

| EnSTEPOP   | Meaning                                                      |
|------------|--------------------------------------------------------------|
| 0b0        | Execution from MDSTEPOP_EL1 is disabled.                     |
| 0b1        | Execution from MDSTEPOP_EL1 is not disabled by this control. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [49:36]

Reserved, RES0.

## EHBWE,bit [35]

## When FEAT\_Debugv8p9 is implemented:

Extended Halting Breakpoint and Watchpoint Enable. Used for save/restore of EDSCR2.EHBWE.

When OSLSR\_EL1.OSLK is 0, software must treat this field as UNK/SBZP.

When OSLSR\_EL1.OSLK is 1, this field holds the value of EDSCR2.EHBWE. Reads and writes of this field are indirect accesses to EDSCR2.EHBWE.

It is IMPLEMENTATION DEFINED whether this field is implemented or is RES0 when 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '0', access to this field is RO.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## EnSPM, bit [34]

## When FEAT\_SPMU is implemented:

Enable access to System PMU registers. When disabled, accesses to System PMU registers generate a trap to EL1.

| EnSPM   | Meaning                                                                                                                                |
|---------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Accesses of the specified System PMUregisters at EL0 are trapped to EL1, unless the instruction generates a higher priority exception. |
| 0b1     | Accesses of the specified System PMUregisters are not trapped by this mechanism.                                                       |

In AArch64 state, the instructions affected by this control are: MRS and MSR accesses to

SPMCNTENCLR\_EL0, SPMCNTENSET\_EL0, SPMCR\_EL0, SPMEVCNTR&lt;n&gt;\_EL0, SPMEVFILT2R&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, SPMEVTYPER&lt;n&gt;\_EL0, SPMOVSCLR\_EL0, SPMOVSSET\_EL0, and SPMSELR\_EL0.

Unless the instruction generates a higher priority exception:

- If EL2 is implemented and enabled in the current Security state, and HCR\_EL2.TGE is 1, then trapped instructions generate an exception to EL2.
- Otherwise, trapped instructions generate an exception to EL1.

Trapped instructions are reported using EC syndrome value 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTA, bit [33]

## When FEAT\_TRBE\_EXT is implemented or FEAT\_ETEv1p3 is implemented:

Trap Trace Accesses. Used for save/restore of EDSCR2.TTA.

When OSLSR\_EL1.OSLK is 0, software must treat this field as UNK/SBZP.

When OSLSR\_EL1.OSLK is 1, this field holds the value of EDSCR2.TTA. Reads and writes of this field are indirect accesses to EDSCR2.TTA.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '0', access to this field is RO.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## EMBWE,bit [32]

## When FEAT\_Debugv8p9 is implemented:

Extended Monitor Breakpoint and Watchpoint Enable. Enables use of additional breakpoints or watchpoints.

| EMBWE   | Meaning                                                                                                                                                                                      |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Breakpoint and Watchpoint exceptions are disabled for each breakpoint <n> and watchpoint <n>, where n is greater than or equal to 16. The Effective value of MDSELR_EL1.BANK is zero at EL1. |
| 0b1     | Breakpoint and Watchpoint exceptions are not affected by this mechanism. The Effective value of MDSELR_EL1.BANK is not affected by this field.                                               |

It is IMPLEMENTATION DEFINED whether this field is implemented or is RES0 when 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI.

This field is ignored by the PE and treated as zero when any of the following are true:

- EL3 is implemented and MDCR\_EL3.EBWE is 0.
- EL2 is implemented and enabled in the current Security state, and MDCR\_EL2.EBWE is 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL1, this field resets to '0' .

- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TFO, bit [31]

## When FEAT\_TRF is implemented:

Trace Filter override. Used for save/restore of EDSCR.TFO.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.TFO. Reads and writes of this bit are indirect accesses to EDSCR.TFO.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## Otherwise:

Reserved, RES0.

## RXfull, bit [30]

Used for save/restore of EDSCR.RXfull.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.RXfull. Reads and writes of this bit are indirect accesses to EDSCR.RXfull.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## TXfull, bit [29]

Used for save/restore of EDSCR.TXfull.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.TXfull. Reads and writes of this bit are indirect accesses to EDSCR.TXfull.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## Bit [28]

Reserved, RES0.

## RXO, bit [27]

Used for save/restore of EDSCR.RXO.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.RXO. Reads and writes of this bit are indirect accesses to EDSCR.RXO.

When OSLSR\_EL1.OSLK == 1, if bits [27,6] of the value written to MDSCR\_EL1 are {1,0}, that is, the RXO bit is 1 and the ERR bit is 0, the PE sets EDSCR.{RXO,ERR} to UNKNOWN values.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## TXU, bit [26]

Used for save/restore of EDSCR.TXU.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.TXU. Reads and writes of this bit are indirect accesses to EDSCR.TXU.

When OSLSR\_EL1.OSLK == 1, if bits [26,6] of the value written to MDSCR\_EL1 are {1,0}, that is, the TXU bit is 1 and the ERR bit is 0, the PE sets EDSCR.{TXU,ERR} to UNKNOWN values.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## Bits [25:24]

Reserved, RES0.

## INTdis, bits [23:22]

Used for save/restore of EDSCR.INTdis.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this field holds the value of EDSCR.INTdis. Reads and writes of this field are indirect accesses to EDSCR.INTdis.

The reset behavior of this field is:

- On a Cold reset, this field resets to '00' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## TDA, bit [21]

Used for save/restore of EDSCR.TDA.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.TDA. Reads and writes of this bit are indirect accesses to EDSCR.TDA.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## Bit [20]

Reserved, RES0.

## SC2, bit [19]

## When FEAT\_PCSRv8 is implemented, FEAT\_VHE is implemented, and FEAT\_PCSRv8p2 is not implemented:

Used for save/restore of EDSCR.SC2.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.SC2. Reads and writes of this bit are indirect accesses to EDSCR.SC2.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## Otherwise:

Reserved, RES0.

## Bits [18:16]

Reserved, RAZ/WI.

Hardware must implement this field as RAZ/WI. Software must not rely on the register reading as zero, and must use a read-modify-write sequence to write to the register.

## MDE, bit [15]

Monitor debug events. Enable Breakpoint, Watchpoint, and Vector Catch exceptions.

| MDE   | Meaning                                                       |
|-------|---------------------------------------------------------------|
| 0b0   | Breakpoint, Watchpoint, and Vector Catch exceptions disabled. |
| 0b1   | Breakpoint, Watchpoint, and Vector Catch exceptions enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## HDE, bit [14]

Used for save/restore of EDSCR.HDE.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.HDE. Reads and writes of this bit are indirect accesses to EDSCR.HDE.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## KDE, bit [13]

Local (kernel) debug enable. If ELD is using AArch64, enable debug exceptions within ELD. Permitted values are:

| KDE   | Meaning                                                                                |
|-------|----------------------------------------------------------------------------------------|
| 0b0   | Debug exceptions, other than Breakpoint Instruction exceptions, disabled within EL D . |
| 0b1   | All debug exceptions enabled within EL D .                                             |

RES0 if ELD is using AArch32.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TDCC, bit [12]

Traps EL0 accesses to the Debug Communication Channel (DCC) registers to EL1, or to EL2 when it is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1, from both Execution states, as follows:

- In AArch64 state, MRS or MSR accesses to the following DCC registers are trapped, reported using EC syndrome value 0x18 :
- MDCCSR\_EL0.
- If not in Debug state, DBGDTR\_EL0, DBGDTRTX\_EL0, and DBGDTRRX\_EL0.
- In AArch32 state, MRC or MCR accesses to the following registers are trapped, reported using EC syndrome value 0x05 .
- DBGDSCRint, DBGDIDR, DBGDSAR, DBGDRAR.
- If not in Debug state, DBGDTRRXint, and DBGDTRTXint.
- In AArch32 state, LDC access to DBGDTRRXint and STC access to DBGDTRTXint are trapped, reported using EC syndrome value 0x06 .
- In AArch32 state, MRRC accesses to DBGDSAR and DBGDRAR are trapped, reported using EC syndrome value 0x0C .

| TDCC   | Meaning                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                       |
| 0b1    | EL0 using AArch64: EL0 accesses to the AArch64 DCCregisters are trapped. EL0 using AArch32: EL0 accesses to the AArch32 DCCregisters are trapped. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:7]

Reserved, RES0.

## ERR, bit [6]

Used for save/restore of EDSCR.ERR.

When OSLSR\_EL1.OSLK == 0, software must treat this bit as UNK/SBZP.

When OSLSR\_EL1.OSLK == 1, this bit holds the value of EDSCR.ERR. Reads and writes of this bit are indirect accesses to EDSCR.ERR.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When OSLSR\_EL1.OSLK == '1', access to this field is RW.
- When OSLSR\_EL1.OSLK == '0', access to this field is RO.

## Bits [5:1]

Reserved, RES0.

## SS, bit [0]

Software step control bit. If ELD is using AArch64, enable Software step. Permitted values are:

| SS   | Meaning                |
|------|------------------------|
| 0b0  | Software step disabled |
| 0b1  | Software step enabled. |

RES0 if ELD is using AArch32.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MDSCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.MDSCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x158]; else X[t, 64] = MDSCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDSCR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MDSCR_EL1;
```

MSR MDSCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0010 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.MDSCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x158] = X[t, 64]; else MDSCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else
```

AArch64.SystemAccessTrap(EL3, 0x18);

<!-- formula-not-decoded -->

## D24.3.21 MDSELR\_EL1, Breakpoint and Watchpoint Selection Register

The MDSELR\_EL1 characteristics are:

## Purpose

Selects the current breakpoints or watchpoints accessed by System register instructions.

## Configuration

This register is present only when FEAT\_Debugv8p9 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MDSELR\_EL1 are UNDEFINED.

## Attributes

MDSELR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:6]

Reserved, RES0.

## BANK, bits [5:4]

Breakpoint and watchpoint bank select.

| BANK   | Meaning          | Applies when                                 |
|--------|------------------|----------------------------------------------|
| 0b00   | Select 0 to 15.  |                                              |
| 0b01   | Select 16 to 31. | NUM_BREAKPOINTS > 16 or NUM_WATCHPOINTS > 16 |
| 0b10   | Select 32 to 47. | NUM_BREAKPOINTS > 32 or NUM_WATCHPOINTS > 32 |
| 0b11   | Select 48 to 63. | NUM_BREAKPOINTS > 48 or NUM_WATCHPOINTS > 48 |

Each of the following register names accesses a register for breakpoint or watchpoint &lt;n&gt;, where n =

UInt(MDSELR\_EL1.BANK:m[3:0]) :

- DBGBCR&lt;m&gt;\_EL1.
- DBGBVR&lt;m&gt;\_EL1.
- DBGWCR&lt;m&gt;\_EL1.
- DBGWVR&lt;m&gt;\_EL1.

This field is ignored by the PE and treated as zeros when any of the following are true:

- Executing at EL3 and MDCR\_EL3.EBWE is 0.
- Executing at EL2 and the Effective value of MDCR\_EL2.EBWE is 0.

- Executing at EL1 and the Effective value of MDSCR\_EL1.EMBWE is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES0 if all of the following are true:
- NUM\_BREAKPOINTS &lt;= 16
- NUM\_WATCHPOINTS &lt;= 16
- Otherwise, access to this field is RW.

## Bits [3:0]

Reserved, RES0.

## Accessing MDSELR\_EL1

When 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI, it is IMPLEMENTATION DEFINED whether these trap controls have any effect on accesses to MDSELR\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, MDSELR_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_Debugv8p9) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EBWE == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nMDSELR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EBWE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDSELR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EBWE == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED;
```

```
elsif HaveEL(EL3) && MDCR_EL3.EBWE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDSELR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MDSELR_EL1;
```

MSR MDSELR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0100 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_Debugv8p9) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EBWE == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nMDSELR_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EBWE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MDSELR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EBWE == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EBWE == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else
```

AArch64.SystemAccessTrap(EL3, 0x18);

<!-- formula-not-decoded -->

## D24.3.22 MDSTEPOP\_EL1, Monitor Debug Step Opcode Register

The MDSTEPOP\_EL1 characteristics are:

## Purpose

Used to execute instructions while Software Step is in active-not-pending state.

## Configuration

This register is present only when FEAT\_STEP2 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MDSTEPOP\_EL1 are UNDEFINED.

## Attributes

MDSTEPOP\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 32   |
|--------|------|
| RES0   |      |
| 31     | 0    |
| OPCODE |      |

## Bits [63:32]

Reserved, RES0.

## OPCODE, bits [31:0]

A64 instruction to be executed on the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MDSTEPOP\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MDSTEPOP\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0101 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_STEP2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnSTEPOP == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGRTR2_EL2.nMDSTEPOP_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnSTEPOP == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDSTEPOP_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnSTEPOP == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnSTEPOP == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = MDSTEPOP_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MDSTEPOP_EL1;
```

MSR MDSTEPOP\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0101 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_STEP2) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnSTEPOP == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == '0') || ↪ → HDFGWTR2_EL2.nMDSTEPOP_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.EnSTEPOP == '0' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MDSTEPOP_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.EnSTEPOP == '0' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.EnSTEPOP == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else MDSTEPOP_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then MDSTEPOP_EL1 = X[t, 64];
```

## D24.3.23 OSDLR\_EL1, OS Double Lock Register

The OSDLR\_EL1 characteristics are:

## Purpose

Used to control the OS Double Lock.

## Configuration

AArch64 System register OSDLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGOSDLR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to OSDLR\_EL1 are UNDEFINED.

## Attributes

OSDLR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
| RES0 |      |
| 31   | 1 0  |
| RES0 | DLK  |

## Bits [63:1]

Reserved, RES0.

## DLK, bit [0]

## When FEAT\_DoubleLock is implemented:

OS Double Lock control bit.

| DLK   | Meaning                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | OS Double Lock unlocked.                                                                                                      |
| 0b1   | OS Double Lock locked, if DBGPRCR_EL1.CORENPDRQ (Core no powerdown request) bit is set to 0 and the PE is in Non-debug state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RAZ/WI.

## Accessing OSDLR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, OSDLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0011 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' && ↪ → (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → IsFeatureImplemented(FEAT_DoubleLock) && HDFGRTR_EL2.OSDLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDOSA> != '00' && (IsFeatureImplemented(FEAT_DoubleLock) || ↪ → boolean IMPLEMENTATION_DEFINED "Trapped by MDCR_EL2.TDOSA") then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean ↪ → IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSDLR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' && ↪ → (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean ↪ → IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSDLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = OSDLR_EL1;
```

MSR OSDLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0011 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' && ↪ → (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → IsFeatureImplemented(FEAT_DoubleLock) && HDFGWTR_EL2.OSDLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDOSA> != '00' && (IsFeatureImplemented(FEAT_DoubleLock) || ↪ → boolean IMPLEMENTATION_DEFINED "Trapped by MDCR_EL2.TDOSA") then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean ↪ → IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSDLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' && ↪ → (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean ↪ → IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSDLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then OSDLR_EL1 = X[t, 64];
```

## D24.3.24 OSDTRRX\_EL1, OS Lock Data Transfer Register, Receive

The OSDTRRX\_EL1 characteristics are:

## Purpose

Used for save and restore of DBGDTRRX\_EL0. It is a component of the Debug Communications Channel.

## Configuration

AArch64 System register OSDTRRX\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRRXext[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to OSDTRRX\_EL1 are UNDEFINED.

## Attributes

OSDTRRX\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
|      | 0    |
| 31   |      |

## Bits [63:32]

Reserved, RES0.

## DTRRX, bits [31:0]

Update DTRRX without side-effect.

Writes to this register update the value in DTRRX and do not change RXfull.

Reads of this register return the last value written to DTRRX and do not change RXfull.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

## Accessing OSDTRRX\_EL1

Arm deprecates reads and writes of OSDTRRX\_EL1 when the OS Lock is unlocked.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, OSDTRRX\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then X[t, 64] = OSDTRRX_EL1; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSDTRRX_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSDTRRX_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = OSDTRRX_EL1;
```

MSR OSDTRRX\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then
```

```
OSDTRRX_EL1 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSDTRRX_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSDTRRX_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then OSDTRRX_EL1 = X[t, 64];
```

## D24.3.25 OSDTRTX\_EL1, OS Lock Data Transfer Register, Transmit

The OSDTRTX\_EL1 characteristics are:

## Purpose

Used for save/restore of DBGDTRTX\_EL0. It is a component of the Debug Communications Channel.

## Configuration

AArch64 System register OSDTRTX\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRTXext[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to OSDTRTX\_EL1 are UNDEFINED.

## Attributes

OSDTRTX\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63    | 32   |
|-------|------|
|       | 0    |
| 31    |      |
| DTRTX |      |

## Bits [63:32]

Reserved, RES0.

## DTRTX, bits [31:0]

Return DTRTX without side-effect.

Reads of this register return the value in DTRTX and do not change TXfull.

Writes of this register update the value in DTRTX and do not change TXfull.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

## Accessing OSDTRTX\_EL1

Arm deprecates reads and writes of OSDTRTX\_EL1 when the OS Lock is unlocked.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, OSDTRTX\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then X[t, 64] = OSDTRTX_EL1; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSDTRTX_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSDTRTX_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = OSDTRTX_EL1;
```

MSR OSDTRTX\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then
```

```
OSDTRTX_EL1 = X[t, 64]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSDTRTX_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSDTRTX_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then OSDTRTX_EL1 = X[t, 64];
```

## D24.3.26 OSECCR\_EL1, OS Lock Exception Catch Control Register

The OSECCR\_EL1 characteristics are:

## Purpose

Provides a mechanism for an operating system to access the contents of EDECCR that are otherwise invisible to software, so it can save/restore the contents of EDECCR over powerdown on behalf of the external debugger.

## Configuration

If OSLSR\_EL1.OSLK == 0, then OSECCR\_EL1 returns an UNKNOWN value on reads and ignores writes.

AArch64 System register OSECCR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGOSECCR[31:0].

AArch64 System register OSECCR\_EL1 bits [31:0] are architecturally mapped to External register EDECCR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to OSECCR\_EL1 are UNDEFINED.

## Attributes

OSECCR\_EL1 is a 64-bit register.

## Field descriptions

When OSLSR\_EL1.OSLK == '1':

<!-- image -->

| 63   |        | 32   |
|------|--------|------|
|      | RES0   |      |
| 31   |        | 0    |
|      | EDECCR |      |

## Bits [63:32]

Reserved, RES0.

## EDECCR, bits [31:0]

Used for save/restore to EDECCR over powerdown.

Reads or writes to this field are indirect accesses to EDECCR.

The reset behavior of this field is:

- On a Cold reset, this field resets to 0x00000000 .

## Accessing OSECCR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0110 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.OSECCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = OSECCR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = OSECCR_EL1; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' then X[t, 64] = bits(64) UNKNOWN; else X[t, 64] = OSECCR_EL1;
```

MSR OSECCR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0000 | 0b0110 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.OSECCR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED;
```

```
else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' then return; else OSECCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif OSLSR_EL1.OSLK == '0' then return; else OSECCR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if OSLSR_EL1.OSLK == '0' then return; else OSECCR_EL1 = X[t, 64];
```

## D24.3.27 OSLAR\_EL1, OS Lock Access Register

The OSLAR\_EL1 characteristics are:

## Purpose

Used to lock or unlock the OS Lock.

## Configuration

The OS Lock can also be locked or unlocked using DBGOSLAR.

AArch64 System register OSLAR\_EL1 bits [31:0] are architecturally mapped to External register OSLAR\_EL1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to OSLAR\_EL1 are UNDEFINED.

## Attributes

OSLAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:1]

Reserved, RES0.

## OSLK, bit [0]

On writes to OSLAR\_EL1, bit[0] is copied to the OS Lock.

Use OSLSR\_EL1.OSLK to check the current status of the lock.

## Accessing OSLAR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MSR OSLAR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0000 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then
```

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.OSLAR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSLAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else OSLAR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then OSLAR_EL1 = X[t, 64];
```

## D24.3.28 OSLSR\_EL1, OS Lock Status Register

The OSLSR\_EL1 characteristics are:

## Purpose

Provides the status of the OS Lock.

## Configuration

AArch64 System register OSLSR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGOSLSR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to OSLSR\_EL1 are UNDEFINED.

## Attributes

OSLSR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:4]

Reserved, RES0.

## OSLM, bits [3, 0]

OS Lock model implemented. Identifies the form of OS save and restore mechanism implemented. The value of this field is an IMPLEMENTATION DEFINED choice of:

| OSLM   | Meaning                  |
|--------|--------------------------|
| 0b00   | OS Lock not implemented. |
| 0b10   | OS Lock implemented.     |

All other values are reserved. In an Armv8 implementation the value 0b00 is not permitted.

Access to this field is RO.

## nTT, bit [2]

Not 32-bit access. This bit is always RAZ. It indicates that a 32-bit access is needed to write the key to the OS Lock Access Register.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## OSLK, bit [1]

OS Lock Status.

| OSLK   | Meaning           |
|--------|-------------------|
| 0b0    | OS Lock unlocked. |
| 0b1    | OS Lock locked.   |

The OS Lock is locked and unlocked by writing to the OS Lock Access Register.

The reset behavior of this field is:

- On a Cold reset, this field resets to '1' .

## Accessing OSLSR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, OSLSR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b000 | 0b0001 | 0b0001 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.OSLSR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSLSR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDOSA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = OSLSR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = OSLSR_EL1;
```

## D24.3.29 SDER32\_EL2, AArch32 Secure Debug Enable Register

The SDER32\_EL2 characteristics are:

## Purpose

Allows access to the AArch32 register SDER from Secure EL2 and EL3 only.

## Configuration

When EL3 is implemented, AArch64 System register SDER32\_EL2 bits [63:0] are architecturally mapped to AArch64 System register SDER32\_EL3[63:0].

AArch64 System register SDER32\_EL2 bits [31:0] are architecturally mapped to AArch32 System register SDER[31:0].

This register is present only when EL2 is implemented, FEAT\_SEL2 is implemented, FEAT\_AA32EL1 is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to SDER32\_EL2 are UNDEFINED.

## Attributes

SDER32\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## SUNIDEN, bit [1]

Secure User Non-Invasive Debug Enable.

| SUNIDEN   | Meaning                                                    |
|-----------|------------------------------------------------------------|
| 0b0       | This bit has no effect on non-invasive debug.              |
| 0b1       | Non-invasive debug is allowed in Secure EL0 using AArch32. |

When Secure EL1 is using AArch32, the forms of non-invasive debug affected by this control are:

- The PC Sample-based Profiling Extension. See About the PC Sample-based Profiling Extension.
- When SelfHostedTraceEnabled() == FALSE, processor trace.
- When EL3 is implemented, Performance Monitors.

When Secure EL1 is using AArch64, this bit has no effect.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SUIDEN, bit [0]

## When EL3 is implemented:

Secure User Invasive Debug Enable.

| SUIDEN   | Meaning                                                                    |
|----------|----------------------------------------------------------------------------|
| 0b0      | This bit does not affect the generation of debug exceptions at Secure EL0. |
| 0b1      | If EL1 is using AArch32, debug exceptions from Secure EL0 are enabled.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing SDER32\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SDER32\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0011 | 0b001 |

```
if !(HaveEL(EL2) && IsFeatureImplemented(FEAT_SEL2) && IsFeatureImplemented(FEAT_AA32EL1) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !HaveEL(EL2) || !IsFeatureImplemented(FEAT_SEL2) || !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif HaveEL(EL3) && MDCR_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = SDER32_EL2; elsif PSTATE.EL == EL3 then if SCR_EL3.EEL2 == '0' then UNDEFINED; else X[t, 64] = SDER32_EL2;
```

MSR SDER32\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0011 | 0b001 |

- if !(HaveEL(EL2) &amp;&amp; IsFeatureImplemented(FEAT\_SEL2) &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL1) &amp;&amp; ↪ → IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

- elsif !HaveEL(EL2) || !IsFeatureImplemented(FEAT\_SEL2) || !IsFeatureImplemented(FEAT\_AA32EL1) then UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

- if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED;
- elsif EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

- if !IsCurrentSecurityState(SS\_Secure) then UNDEFINED;
- elsif HaveEL(EL3) &amp;&amp; MDCR\_EL3.TDA == '1' then AArch64.SystemAccessTrap(EL3, 0x18);

else

SDER32\_EL2 = X[t, 64];

elsif PSTATE.EL == EL3 then

- if SCR\_EL3.EEL2 == '0' then UNDEFINED;

else

SDER32\_EL2 = X[t, 64];

## D24.3.30 SDER32\_EL3, AArch32 Secure Debug Enable Register

The SDER32\_EL3 characteristics are:

## Purpose

Allows access to the AArch32 register SDER from AArch64 state only. Its value has no effect on execution in AArch64 state.

## Configuration

When EL2 is implemented and FEAT\_SEL2 is implemented, AArch64 System register SDER32\_EL3 bits [63:0] are architecturally mapped to AArch64 System register SDER32\_EL2[63:0].

AArch64 System register SDER32\_EL3 bits [31:0] are architecturally mapped to AArch32 System register SDER[31:0].

This register is present only when EL3 is implemented, FEAT\_AA32EL1 is implemented, and FEAT\_AA64 is implemented. Otherwise, direct accesses to SDER32\_EL3 are UNDEFINED.

## Attributes

SDER32\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## SUNIDEN, bit [1]

Secure User Non-Invasive Debug Enable.

| SUNIDEN   | Meaning                                                    |
|-----------|------------------------------------------------------------|
| 0b0       | This bit has no effect on non-invasive debug.              |
| 0b1       | Non-invasive debug is allowed in Secure EL0 using AArch32. |

When Secure EL1 is using AArch32, the forms of non-invasive debug affected by this control are:

- The PC Sample-based Profiling Extension. See About the PC Sample-based Profiling Extension.
- When SelfHostedTraceEnabled() == FALSE, processor trace.
- Performance Monitors.

When Secure EL1 is using AArch64, this bit has no effect.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SUIDEN, bit [0]

Secure User Invasive Debug Enable.

| SUIDEN   | Meaning                                                                    |
|----------|----------------------------------------------------------------------------|
| 0b0      | This bit does not affect the generation of debug exceptions at Secure EL0. |
| 0b1      | If EL1 is using AArch32, debug exceptions from Secure EL0 are enabled.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SDER32\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SDER32\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !HaveEL(EL3) || !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = SDER32_EL3;
```

MSR SDER32\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b001 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !HaveEL(EL3) || !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then SDER32_EL3 = X[t, 64];
```