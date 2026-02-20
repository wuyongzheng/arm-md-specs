## G8.3 Debug registers

This section lists the Debug System registers in AArch32 state, in alphabetic order.

## G8.3.1 DBGAUTHSTATUS, Debug Authentication Status register

The DBGAUTHSTATUS characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for debug.

## Configuration

This register is required in all implementations.

AArch32 System register DBGAUTHSTATUS bits [31:0] are architecturally mapped to AArch64 System register DBGAUTHSTATUS\_EL1[31:0].

AArch32 System register DBGAUTHSTATUS bits [31:0] are architecturally mapped to External register DBGAUTHSTATUS\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGAUTHSTATUS are UNDEFINED.

## Attributes

DBGAUTHSTATUS is a 32-bit register.

## Field descriptions

| 31   | 8 7 6 5 4 3 2 1 0   |
|------|---------------------|
| RES0 | SNID SID NSNID NSID |

## Bits [31:8]

Reserved, RES0.

## SNID, bits [7:6]

## When FEAT\_Debugv8p4 is implemented:

Secure Non-Invasive Debug.

This field has the same value as DBGAUTHSTATUS.SID.

## Otherwise:

Secure Non-Invasive Debug.

| SNID   | Meaning                                                                     |
|--------|-----------------------------------------------------------------------------|
| 0b00   | Secure state is not implemented.                                            |
| 0b10   | Implemented and disabled. ExternalSecureNoninvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalSecureNoninvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## SID, bits [5:4]

Secure Invasive Debug.

| SID   | Meaning                                                                  |
|-------|--------------------------------------------------------------------------|
| 0b00  | Secure state is not implemented.                                         |
| 0b10  | Implemented and disabled. ExternalSecureInvasiveDebugEnabled() == FALSE. |
| 0b11  | Implemented and enabled. ExternalSecureInvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

NSNID, bits [3:2]

## When FEAT\_Debugv8p4 is implemented:

Non-secure Non-invasive debug.

| NSNID   | Meaning                                                                            |
|---------|------------------------------------------------------------------------------------|
| 0b00    | Non-secure state is not implemented.                                               |
| 0b11    | Implemented and enabled. EL3 is implemented or the Effective value of SCR.NS is 1. |

All other values are reserved.

## Otherwise:

Non-secure Non-Invasive Debug.

| NSNID   | Meaning                                                               |
|---------|-----------------------------------------------------------------------|
| 0b00    | Non-secure state is not implemented.                                  |
| 0b10    | Implemented and disabled. ExternalNoninvasiveDebugEnabled() == FALSE. |
| 0b11    | Implemented and enabled. ExternalNoninvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## NSID, bits [1:0]

Non-secure Invasive Debug.

| NSID   | Meaning                                                            |
|--------|--------------------------------------------------------------------|
| 0b00   | Non-secure state is not implemented.                               |
| 0b10   | Implemented and disabled. ExternalInvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalInvasiveDebugEnabled() == TRUE.   |

All other values are reserved.

## Accessing DBGAUTHSTATUS

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b1110 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGAUTHSTATUS; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGAUTHSTATUS; elsif PSTATE.EL == EL3 then R[t] = DBGAUTHSTATUS;
```

## G8.3.2 DBGBCR&lt;n&gt;, Debug Breakpoint Control Registers, n = 0 - 15

The DBGBCR&lt;n&gt; characteristics are:

## Purpose

Holds control information for a breakpoint. Forms breakpoint n together with value register DBGBVR&lt;n&gt;. If EL2 is implemented and this breakpoint supports Context matching, DBGBVR&lt;n&gt; can be associated with a Breakpoint Extended Value Register DBGBXVR&lt;n&gt; for VMID matching.

## Configuration

If breakpoint n is not implemented then accesses to this register are UNDEFINED.

AArch32 System register DBGBCR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register DBGBCR&lt;n&gt;\_EL1[31:0].

AArch32 System register DBGBCR&lt;n&gt; bits [31:0] are architecturally mapped to External register DBGBCR&lt;n&gt;\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGBCR&lt;n&gt; are UNDEFINED.

## Attributes

DBGBCR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

When the E field is zero, all the other fields in the register are ignored.

## Bits [31:24]

Reserved, RES0.

## BT, bits [23:20]

Breakpoint Type. Possible values are:

| BT     | Meaning                                                                                                                                                                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Unlinked instruction address match. DBGBVR<n> is the address of an instruction.                                                                                                                                                                                                                   |
| 0b0001 | As 0b0000 , but linked to a Context matching breakpoint.                                                                                                                                                                                                                                          |
| 0b0010 | Unlinked Context ID match. If the Effective value of HCR_EL2.E2H is 1, and either the PE is executing at EL0 with HCR_EL2.TGE set to 1 or the PE is executing at EL2, then DBGBVR<n>.ContextID is compared against CONTEXTIDR_EL2. Otherwise, DBGBVR<n>.ContextID is compared against CONTEXTIDR. |
| 0b0011 | As 0b0010 with linking enabled.                                                                                                                                                                                                                                                                   |
| 0b0100 | Unlinked instruction address mismatch. DBGBVR<n> is the address of an instruction to be stepped.                                                                                                                                                                                                  |
| 0b0101 | As 0b0100 , but linked to a Context matching breakpoint.                                                                                                                                                                                                                                          |

| BT     | Meaning                                                                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0110 | Unlinked CONTEXTIDR match. DBGBVR<n>.ContextID is a Context ID compared against CONTEXTIDR.                                                                   |
| 0b0111 | As 0b0110 with linking enabled.                                                                                                                               |
| 0b1000 | Unlinked VMIDmatch. DBGBXVR<n>.VMID is a VMIDcompared against VTTBR.VMID.                                                                                     |
| 0b1001 | As 0b1000 with linking enabled.                                                                                                                               |
| 0b1010 | Unlinked VMIDand Context ID match. DBGBVR<n>.ContextID is a Context ID compared against CONTEXTIDR, and DBGBXVR<n>.VMID is a VMIDcompared against VTTBR.VMID. |
| 0b1011 | As 0b1010 with linking enabled.                                                                                                                               |
| 0b1100 | Unlinked CONTEXTIDR_EL2 match. DBGBXVR<n>.ContextID2 is a Context ID compared against CONTEXTIDR_EL2.                                                         |
| 0b1101 | As 0b1100 with linking enabled.                                                                                                                               |
| 0b1110 | Unlinked Full Context ID match. DBGBVR<n>.ContextID is compared against CONTEXTIDR, and DBGBXVR<n>.ContextID2 is compared against CONTEXTIDR_EL2.             |
| 0b1111 | As 0b1110 with linking enabled.                                                                                                                               |

For more information on Breakpoints and their constraints, see 'Breakpoint exceptions' and 'Reserved DBGBCR&lt;n&gt;.BT values'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## LBN, bits [19:16]

Linked Breakpoint Number. For Linked address matching breakpoints, this specifies the index of the Context-matching breakpoint linked to.

For all other breakpoint types, this field is ignored and reads of the register return an UNKNOWN value.

This field is ignored when the value of DBGBCR&lt;n&gt;.E is 0.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## SSC, bits [15:14]

Security state control. Determines the Security states under which a Breakpoint debug event for breakpoint n is generated. This field must be interpreted along with the HMC and PMC fields, and there are constraints on the permitted values of the {HMC, SSC, PMC} fields.

For more information, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions' and 'Reserved DBGBCR&lt;n&gt;.{SSC, HMC, PMC} values'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## HMC,bit [13]

Higher mode control. Determines the debug perspective for deciding when a Breakpoint debug event for breakpoint n is generated. This field must be interpreted along with the SSC and PMC fields, and there are constraints on the permitted values of the {HMC, SSC, PMC} fields. For more information see the SSC, bits [15:14] description.

For more information on the operation of the SSC, HMC, and PMC fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [12:9]

Reserved, RES0.

## BAS, bits [8:5]

Byte address select. Defines which half-words an address-matching breakpoint matches, regardless of the instruction set and Execution state.

The permitted values depend on the breakpoint type.

For Address match breakpoints, the permitted values are:

| BAS    | Match instruction at   | Constraint for debuggers   |
|--------|------------------------|----------------------------|
| 0b0011 | DBGBVR<n>              | Use for T32 instructions   |
| 0b1100 | DBGBVR<n>+2            | Use for T32 instructions   |
| 0b1111 | DBGBVR<n>              | Use for A32 instructions   |

All other values are reserved. For more information, see 'Reserved DBGBCR&lt;n&gt;.BAS values'.

For more information on using the BAS field in Address Match breakpoints, see 'Using the BAS field in Address Match breakpoints'.

For Address mismatch breakpoints in an AArch32 stage 1 translation regime, the permitted values are:

| BAS    | Step instruction at   | Constraint for debuggers            |
|--------|-----------------------|-------------------------------------|
| 0b0000 | •                     | Use for a match anywhere breakpoint |
| 0b0011 | DBGBVR<n>             | Use for T32 instructions            |
| 0b1100 | DBGBVR<n>+2           | Use for T32 instructions            |
| 0b1111 | DBGBVR<n>             | Use for A32 instructions            |

All other values are reserved. For more information, see 'Reserved DBGBCR&lt;n&gt;.BAS values'.

For more information on using the BAS field in address mismatch breakpoints, see 'Using the BAS field in Address Match breakpoints'.

For Context matching breakpoints, this field is RES1 and ignored.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:3]

Reserved, RES0.

## PMC, bits [2:1]

Privilege mode control. Determines the Exception level or levels at which a Breakpoint debug event for breakpoint n is generated. This field must be interpreted along with the SSC and HMC fields, and there are constraints on the permitted values of the {HMC, SSC, PMC} fields. For more information see the DBGBCR&lt;n&gt;.SSC description.

For more information on the operation of the SSC, HMC, and PMC fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E, bit [0]

Enable breakpoint DBGBVR&lt;n&gt;. Possible values are:

| E   | Meaning              |
|-----|----------------------|
| 0b0 | Breakpoint disabled. |
| 0b1 | Breakpoint enabled.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGBCR&lt;n&gt;

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b101  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_BREAKPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else
```

```
R[t] = DBGBCR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBCR[m]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBCR[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b101  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_BREAKPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBCR[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBCR[m] = R[t]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBCR[m] = R[t];
```

## G8.3.3 DBGBVR&lt;n&gt;, Debug Breakpoint Value Registers, n = 0 - 15

The DBGBVR&lt;n&gt; characteristics are:

## Purpose

Holds a value for use in breakpoint matching, either the virtual address of an instruction or a context ID. Forms breakpoint n together with control register DBGBCR&lt;n&gt;. If EL2 is implemented and this breakpoint supports Context matching, DBGBVR&lt;n&gt; can be associated with a Breakpoint Extended Value Register DBGBXVR&lt;n&gt; for VMID matching.

## Configuration

How this register is interpreted depends on the value of DBGBCR&lt;n&gt;.BT.

- When DBGBCR&lt;n&gt;.BT is 0b0x0x , this register holds a virtual address.
- When DBGBCR&lt;n&gt;.BT is 0bxx1x , this register holds a Context ID.

For other values of DBGBCR&lt;n&gt;.BT, this register is RES0.

Some breakpoints might not support Context ID comparison. For more information, see the description of the DBGDIDR.CTX\_CMPs field.

If breakpoint n is not implemented then accesses to this register are UNDEFINED.

AArch32 System register DBGBVR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register DBGBVR&lt;n&gt;\_EL1[31:0].

AArch32 System register DBGBVR&lt;n&gt; bits [31:0] are architecturally mapped to External register DBGBVR&lt;n&gt;\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGBVR&lt;n&gt; are UNDEFINED.

## Attributes

DBGBVR&lt;n&gt; is a 32-bit register.

## Field descriptions

When DBGBCR&lt;n&gt;.BT IN {' 0x0 x'}:

31

VA[31:2]

## VA[31:2], bits [31:2]

Bits[31:2] of the address value for comparison.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

When DBGBCR&lt;n&gt;.BT IN {'001x'}:

2

1

0

RES0

| 31        | 0   |
|-----------|-----|
| ContextID |     |

## ContextID, bits [31:0]

Context ID value for comparison.

The value is compared against CONTEXTIDR\_EL2 when all of the following are true:

- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.
- The PE is executing at EL0.

Otherwise, the value is compared against CONTEXTIDR.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

When DBGBCR&lt;n&gt;.BT IN {'101x'} and EL2 is implemented:

ContextID

31

0

## ContextID, bits [31:0]

Context ID value for comparison against CONTEXTIDR.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

When DBGBCR&lt;n&gt;.BT IN {'x11x'}, EL2 is implemented, and FEAT\_Debugv8p1 is implemented:

ContextID

31

0

## ContextID, bits [31:0]

Context ID value for comparison against CONTEXTIDR.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGBVR&lt;n&gt;

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b100  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_BREAKPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBVR[m]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBVR[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b100  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_BREAKPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBVR[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBVR[m] = R[t]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBVR[m] = R[t];
```

## G8.3.4 DBGBXVR&lt;n&gt;, Debug Breakpoint Extended Value Registers, n = 0 - 15

The DBGBXVR&lt;n&gt; characteristics are:

## Purpose

Holds a value for use in breakpoint matching, to support VMID matching. Used in conjunction with a control register DBGBCR&lt;n&gt; and a value register DBGBVR&lt;n&gt;, where EL2 is implemented and breakpoint n supports Context matching.

## Configuration

How this register is interpreted depends on the value of DBGBCR&lt;n&gt;.BT.

- When DBGBCR&lt;n&gt;.BT is 0b10xx , this register holds a VMID.
- When DBGBCR&lt;n&gt;.BT is 0b11xx , this register holds a Context ID.

For other values of DBGBCR&lt;n&gt;.BT, this register is RES0.

Accesses to this register are UNDEFINED in any of the following cases:

- Breakpoint n is not implemented.
- Breakpoint n does not support Context matching.
- EL2 is not implemented.

For more information, see the description of the DBGDIDR.CTX\_CMPs field.

AArch32 System register DBGBXVR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register DBGBVR&lt;n&gt;\_EL1[63:32].

AArch32 System register DBGBXVR&lt;n&gt; bits [31:0] are architecturally mapped to External register DBGBVR&lt;n&gt;\_EL1[63:32].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGBXVR&lt;n&gt; are UNDEFINED.

## Attributes

DBGBXVR&lt;n&gt; is a 32-bit register.

## Field descriptions

When DBGBCR&lt;n&gt;.BT IN {'10xx'} and EL2 is implemented:

<!-- image -->

| 31   | 16 15      | 8 7       |
|------|------------|-----------|
| RES0 | VMID[15:8] | VMID[7:0] |

## Bits [31:16]

Reserved, RES0.

VMID[15:8], bits [15:8]

## When FEAT\_VMID16 is implemented and VTCR\_EL2.VS == '1':

Extension to VMID[7:0]. For more information, see VMID[7:0].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VMID[7:0], bits [7:0]

VMIDvalue for comparison. The VMID is 8 bits when any of the following are true:

- EL2 is using AArch32.
- VTCR\_EL2.VS is 0.
- FEAT\_VMID16 is not implemented.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## When DBGBCR&lt;n&gt;.BT IN {'11xx'} and EL2 is implemented:

| 31         | 0          |
|------------|------------|
| ContextID2 | ContextID2 |

## ContextID2, bits [31:0]

## When FEAT\_Debugv8p1 is implemented:

Context ID value for comparison against CONTEXTIDR\_EL2.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing DBGBXVR&lt;n&gt;

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>} ; Where m = 0-15
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | m[3:0] | 0b001  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_BREAKPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then
```

```
AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBXVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBXVR[m]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGBXVR[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | m[3:0] | 0b001  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_BREAKPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05);
```

```
elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBXVR[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBXVR[m] = R[t]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGBXVR[m] = R[t];
```

## G8.3.5 DBGCLAIMCLR, Debug CLAIM Tag Clear register

The DBGCLAIMCLR characteristics are:

## Purpose

Used by software to read the values of the CLAIM tag bits, and to clear CLAIM tag bits to 0.

The architecture does not define any functionality for the CLAIM tag bits.

Note

CLAIM tags are typically used for communication between the debugger and target software.

Used in conjunction with the DBGCLAIMSET register.

## Configuration

An implementation must include eight CLAIM tag bits.

AArch32 System register DBGCLAIMCLR bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMCLR\_EL1[31:0].

AArch32 System register DBGCLAIMCLR bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMSET\_EL1[31:0].

AArch32 System register DBGCLAIMCLR bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMSET[31:0].

AArch32 System register DBGCLAIMCLR bits [31:0] are architecturally mapped to External register DBGCLAIMCLR\_EL1[31:0].

AArch32 System register DBGCLAIMCLR bits [31:0] are architecturally mapped to External register DBGCLAIMSET\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGCLAIMCLRare UNDEFINED.

## Attributes

DBGCLAIMCLRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RAZ/WI.

CLAIM&lt;m&gt;, bits [m], for m = 7 to 0

Claim Tag Clear. Indicates the current status of Claim Tag bit &lt;m&gt;, and is used to clear Claim Tag bit &lt;m&gt; to 0.

| CLAIM<m>   | Meaning                                                                        |
|------------|--------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not set. On a write: Ignored.                  |
| 0b1        | On a read: Claim Tag bit <m> is set. On a write: Clear Claim tag bit <m> to 0. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is W1C.

## Accessing DBGCLAIMCLR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b1001 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGCLAIMCLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGCLAIMCLR; elsif PSTATE.EL == EL3 then
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b1001 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGCLAIMCLR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGCLAIMCLR = R[t]; elsif PSTATE.EL == EL3 then DBGCLAIMCLR = R[t];
```

## G8.3.6 DBGCLAIMSET, Debug CLAIM Tag Set register

The DBGCLAIMSET characteristics are:

## Purpose

Used by software to set the CLAIM tag bits to 1.

The architecture does not define any functionality for the CLAIM tag bits.

Note

CLAIM tags are typically used for communication between the debugger and target software.

Used in conjunction with the DBGCLAIMCLR register.

## Configuration

An implementation must include eight CLAIM tag bits.

AArch32 System register DBGCLAIMSET bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMSET\_EL1[31:0].

AArch32 System register DBGCLAIMSET bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMCLR\_EL1[31:0].

AArch32 System register DBGCLAIMSET bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMCLR[31:0].

AArch32 System register DBGCLAIMSET bits [31:0] are architecturally mapped to External register DBGCLAIMSET\_EL1[31:0].

AArch32 System register DBGCLAIMSET bits [31:0] are architecturally mapped to External register DBGCLAIMCLR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGCLAIMSET are UNDEFINED.

## Attributes

DBGCLAIMSET is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RAZ/WI.

CLAIM&lt;m&gt;, bits [m], for m = 7 to 0

Claim Tag Set. Used to set Claim Tag bit &lt;m&gt; to 1.

| CLAIM<m>   | Meaning                                 |
|------------|-----------------------------------------|
| 0b0        | On a write: Ignored.                    |
| 0b1        | On a write: Set Claim Tag bit <m> to 1. |

Access to this field is RAO/W1S.

## Accessing DBGCLAIMSET

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b1000 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGCLAIMSET; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGCLAIMSET; elsif PSTATE.EL == EL3 then R[t] = DBGCLAIMSET;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b1000 | 0b110  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGCLAIMSET = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGCLAIMSET = R[t]; elsif PSTATE.EL == EL3 then DBGCLAIMSET = R[t];
```

## G8.3.7 DBGDCCINT, DCC Interrupt Enable Register

The DBGDCCINT characteristics are:

## Purpose

Enables interrupt requests to be signaled based on the DCC status flags.

## Configuration

AArch32 System register DBGDCCINT bits [31:0] are architecturally mapped to AArch64 System register MDCCINT\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDCCINT are UNDEFINED.

## Attributes

DBGDCCINT is a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

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

## Accessing DBGDCCINT

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then R[t] = DBGDCCINT; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDCCINT; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDCCINT; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else R[t] = DBGDCCINT;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then
```

```
DBGDCCINT = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDCCINT = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA ==
```

```
↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDCCINT = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else DBGDCCINT = R[t];
```

## G8.3.8 DBGDEVID, Debug Device ID register 0

The DBGDEVID characteristics are:

## Purpose

Adds to the information given by the DBGDIDR by describing other features of the debug implementation.

## Configuration

This register is required in all implementations.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDEVID are UNDEFINED.

## Attributes

DBGDEVID is a 32-bit register.

## Field descriptions

| 31      | 28 27   | 24 23      | 20 19     | 16 15       | 12 11      | 8 7        | 4 3   | 0        |
|---------|---------|------------|-----------|-------------|------------|------------|-------|----------|
| CIDMask | AuxRegs | DoubleLock | VirtExtns | VectorCatch | BPAddrMask | WPAddrMask |       | PCSample |

## CIDMask, bits [31:28]

Indicates the level of support for the Context ID matching breakpoint masking capability.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CIDMask   | Meaning                                |
|-----------|----------------------------------------|
| 0b0000    | Context ID masking is not implemented. |
| 0b0001    | Context ID masking is implemented.     |

All other values are reserved. The value of this for Armv8 is 0b0000 .

Access to this field is RO.

## AuxRegs, bits [27:24]

Indicates support for Auxiliary registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AuxRegs   | Meaning                                                       |
|-----------|---------------------------------------------------------------|
| 0b0000    | None supported.                                               |
| 0b0001    | Support for External Debug Auxiliary Control Register, EDACR. |

All other values are reserved.

Access to this field is RO.

## DoubleLock, bits [23:20]

OS Double Lock implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DoubleLock   | Meaning                                               |
|--------------|-------------------------------------------------------|
| 0b0000       | OS Double Lock is not implemented. DBGOSDLRis RAZ/WI. |
| 0b0001       | OS Double Lock is implemented. DBGOSDLRis RW.         |

FEAT\_DoubleLock implements the functionality identified by the value 0b0001 .

All other values are reserved.

Access to this field is RO.

## VirtExtns, bits [19:16]

Indicates whether EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VirtExtns   | Meaning                 |
|-------------|-------------------------|
| 0b0000      | EL2 is not implemented. |
| 0b0001      | EL2 is implemented.     |

All other values are reserved.

Access to this field is RO.

## VectorCatch, bits [15:12]

Defines the form of Vector Catch exception implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VectorCatch   | Meaning                                                |
|---------------|--------------------------------------------------------|
| 0b0000        | Address matching Vector Catch exception implemented.   |
| 0b0001        | Exception matching Vector Catch exception implemented. |

All other values are reserved.

Access to this field is RO.

## BPAddrMask, bits [11:8]

Indicates the level of support for the instruction address matching breakpoint masking capability.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BPAddrMask   | Meaning                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------|
| 0b0000       | Breakpoint address masking might be implemented. If not implemented, DBGBCR<n>[28:24] is RAZ/WI. |
| 0b0001       | Breakpoint address masking is implemented.                                                       |
| 0b1111       | Breakpoint address masking is not implemented. DBGBCR<n>[28:24] is RES0.                         |

All other values are reserved. The value of this for Armv8 is 0b1111 .

Access to this field is RO.

## WPAddrMask, bits [7:4]

Indicates the level of support for the data address matching watchpoint masking capability.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WPAddrMask   | Meaning                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------|
| 0b0000       | Watchpoint address masking might be implemented. If not implemented, DBGWCR<n>.MASK (Address mask) is RAZ/WI. |
| 0b0001       | Watchpoint address masking is implemented.                                                                    |
| 0b1111       | Watchpoint address masking is not implemented. DBGWCR<n>.MASK (Address mask) is RES0.                         |

All other values are reserved. The value of this for Armv8 is 0b0001 .

Access to this field is RO.

## PCSample, bits [3:0]

Indicates the level of PC Sample-based Profiling support using external debug registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PCSample   | Meaning                                                                                                    |
|------------|------------------------------------------------------------------------------------------------------------|
| 0b0000     | PC Sample-based Profiling Extension is not implemented in the external debug registers space.              |
| 0b0010     | Only EDPCSR and EDCIDSR are implemented. This option is only permitted if EL3 and EL2 are not implemented. |
| 0b0011     | EDPCSR, EDCIDSR, and EDVIDSR are implemented.                                                              |

All other values are reserved.

When FEAT\_PCSRv8p2 is implemented, the only permitted value is 0b0000 .

Note

FEAT\_PCSRv8p2 implements the PC Sample-based Profiling Extension in the Performance Monitors register space, as indicated by the value of PMDEVID.PCSample.

Access to this field is RO.

## Accessing DBGDEVID

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b0010 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDEVID; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDEVID; elsif PSTATE.EL == EL3 then R[t] = DBGDEVID;
```

## G8.3.9 DBGDEVID1, Debug Device ID register 1

The DBGDEVID1 characteristics are:

## Purpose

Adds to the information given by the DBGDIDR by describing other features of the debug implementation.

## Configuration

This register is required in all implementations.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDEVID1 are UNDEFINED.

## Attributes

DBGDEVID1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 4 3 0      |
|------|------------|
|      | PCSROffset |

## Bits [31:4]

Reserved, RES0.

## PCSROffset, bits [3:0]

This field indicates the offset applied to PC samples returned by reads of EDPCSR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PCSROffset   | Meaning                                                                                                          |
|--------------|------------------------------------------------------------------------------------------------------------------|
| 0b0000       | EDPCSR is not implemented.                                                                                       |
| 0b0010       | EDPCSR implemented. Samples have no offset applied and do not sample the instruction set state in AArch32 state. |

When FEAT\_PCSRv8p2 is implemented, the only permitted value is 0b0000 .

Note

FEAT\_PCSRv8p2 implements the PC Sample-based Profiling Extension in the Performance Monitors register space, as indicated by the value of PMDEVID.PCSample.

Access to this field is RO.

## Accessing DBGDEVID1

Accesses to this register use the following encodings in the System register encoding space:

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b0001 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDEVID1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDEVID1; elsif PSTATE.EL == EL3 then R[t] = DBGDEVID1;
```

## G8.3.10 DBGDEVID2, Debug Device ID register 2

The DBGDEVID2 characteristics are:

## Purpose

Reserved for future descriptions of features of the debug implementation.

## Configuration

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDEVID2 are UNDEFINED.

## Attributes

DBGDEVID2 is a 32-bit register.

## Field descriptions

## Bits [31:0]

Reserved, RES0.

## Accessing DBGDEVID2

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0111 | 0b0000 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else
```

31

RES0

0

```
R[t] = DBGDEVID2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDEVID2; elsif PSTATE.EL == EL3 then R[t] = DBGDEVID2;
```

## G8.3.11 DBGDIDR, Debug ID Register

The DBGDIDR characteristics are:

## Purpose

Specifies which version of the Debug architecture is implemented, and some features of the debug implementation.

## Configuration

If EL1 cannot use AArch32 then the implementation of this register is OPTIONAL and deprecated.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DBGDIDR are UNDEFINED.

## Attributes

DBGDIDR is a 32-bit register.

## Field descriptions

<!-- image -->

## WRPs, bits [31:28]

Number of watchpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WRPs             | Meaning                             |
|------------------|-------------------------------------|
| 0b0001 .. 0b1111 | The number of watchpoints, minus 1. |

If FEAT\_Debugv8p9 is implemented and 16 or more watchpoints are implemented, this field reads as 0b1111 .

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 watchpoints.

The value

0b0000 is reserved.

Access to this field is RO.

## BRPs, bits [27:24]

Number of breakpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BRPs             | Meaning                             |
|------------------|-------------------------------------|
| 0b0001 .. 0b1111 | The number of breakpoints, minus 1. |

If FEAT\_Debugv8p9 is implemented and 16 or more breakpoints are implemented, this field reads as 0b1111 .

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 breakpoints.

The value

0b0000 is reserved.

Access to this field is RO.

## CTX\_CMPs, bits [23:20]

Number of context-aware breakpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CTX_CMPs         | Meaning                                           |
|------------------|---------------------------------------------------|
| 0b0000 .. 0b1111 | The number of context-aware breakpoints, minus 1. |

The value of this field is never greater than DBGDIDR.BRPs.

If FEAT\_Debugv8p9 is implemented and 16 or more context-aware breakpoints are implemented, this field reads as 0b1111 .

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 breakpoints.

Access to this field is RO.

## Version, bits [19:16]

Debug architecture version. Indicates presence of Armv8 debug architecture.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Version   | Meaning                                                              |
|-----------|----------------------------------------------------------------------|
| 0b0000    | Not supported.                                                       |
| 0b0001    | Armv6, v6 Debug architecture, with System registers access.          |
| 0b0010    | Armv6, v6.1 Debug architecture, with System registers access.        |
| 0b0011    | Armv7, v7 Debug architecture, with only baseline System registers.   |
| 0b0100    | Armv7, v7 Debug architecture, with all System registers implemented. |
| 0b0101    | Armv7, v7.1 Debug architecture, with System registers access.        |
| 0b0110    | Armv8.0 debug architecture.                                          |
| 0b0111    | Armv8.1 debug architecture, FEAT_Debugv8p1.                          |

| Version   | Meaning                                     |
|-----------|---------------------------------------------|
| 0b1000    | Armv8.2 debug architecture, FEAT_Debugv8p2. |
| 0b1001    | Armv8.4 debug architecture, FEAT_Debugv8p4. |
| 0b1010    | Armv8.8 debug architecture, FEAT_Debugv8p8. |
| 0b1011    | Armv8.9 debug architecture, FEAT_Debugv8p9. |

## All other values are reserved.

From Armv8.0, the values 0b0000 , 0b0001 , 0b0010 , 0b0011 , 0b0100 , and 0b0101 are not permitted.

FEAT\_Debugv8p1 implements the functionality identified by the value 0b0111 .

FEAT\_Debugv8p2 implements the functionality identified by the value 0b1000 .

FEAT\_Debugv8p4 implements the functionality identified by the value 0b1001 .

FEAT\_Debugv8p8 implements the functionality identified by the value 0b1010 .

FEAT\_Debugv8p9 implements the functionality identified by the value 0b1011 .

From Armv8.1, when FEAT\_Debugv8p1 is implemented the value 0b0110 is not permitted.

From Armv8.2, the values 0b0110 and 0b0111 are not permitted.

From Armv8.4, the value 0b1000 is not permitted.

From Armv8.8, the value 0b1001 is not permitted.

From Armv8.9, the value 0b1010 is not permitted.

Access to this field is RO.

## Bit [15]

Reserved, RES1.

## nSUHD\_imp, bit [14]

Previously indicated that Secure User Halting Debug is not implemented.

The value of this field must match the value of the SE\_imp field.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bit [13]

Reserved, RES0.

## SE\_imp, bit [12]

EL3 implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SE_imp   | Meaning              |
|----------|----------------------|
| 0b0      | EL3 not implemented. |
| 0b1      | EL3 implemented.     |

The value of this field must match the value of the nSUHD\_imp field.

Access to this field is RO.

## Bits [11:0]

Reserved, RES0.

## Accessing DBGDIDR

Arm deprecates any access to this register from EL0.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then R[t] = DBGDIDR; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); else AArch64.AArch32SystemAccessTrap(EL1, 0x05); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDA> != '00') then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDIDR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDIDR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDIDR; elsif PSTATE.EL == EL3 then R[t] = DBGDIDR;
```

## G8.3.12 DBGDRAR, Debug ROM Address Register

The DBGDRAR characteristics are:

## Purpose

Defines the base physical address of a 4KB-aligned memory-mapped debug component, usually a ROM table that locates and describes the memory-mapped debug components in the system. Use of this register is deprecated.

## Configuration

DBGDRARis a 64-bit register that can also be accessed as a 32-bit value. If it is accessed as a 32-bit register, bits [31:0] are read.

If EL1 cannot use AArch32 then the implementation of this register is OPTIONAL and deprecated.

AArch32 System register DBGDRAR bits [63:0] are architecturally mapped to AArch64 System register MDRAR\_EL1[63:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DBGDRAR are UNDEFINED.

## Attributes

DBGDRARis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## ROMADDR[47:12], bits [47:12]

Bits[47:12] of the ROM table physical address.

If the physical address size in bits (PAsize) is less than 48 then the register bits corresponding to ROMADDR [47:PAsize] are RES0.

Bits [11:0] of the ROM table physical address are zero.

Arm strongly recommends that bits ROMADDR[(PAsize-1):32] are zero in any system where the implementation only supports execution in AArch32 state.

If DBGDRAR.Valid == 0b00 , then this field is UNKNOWN.

In an implementation that includes EL3, ROMADDR is an address in Non-secure memory. It is IMPLEMENTATION DEFINED whether the ROM table is also accessible in Secure memory.

## Bits [11:2]

Reserved, RES0.

## Valid, bits [1:0]

This field indicates whether the ROM Table address is valid.

| Valid   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b00    | ROMTable address is not valid. Software must ignore ROMADDR. |
| 0b11    | ROMTable address is valid.                                   |

Other values are reserved.

Arm recommends implementations set this field to zero.

## Accessing DBGDRAR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then R[t] = DBGDRAR<31:0>; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); else AArch64.AArch32SystemAccessTrap(EL1, 0x05); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDRA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDRA> != '00') then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDRAR<31:0>;
```

```
elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDRA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDRA> ↪ → != '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDRAR<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDRAR<31:0>; elsif PSTATE.EL == EL3 then R[t] = DBGDRAR<31:0>;
```

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1110   | 0b0001 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then R[t, t2] = DBGDRAR; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); else AArch64.AArch32SystemAccessTrap(EL1, 0x0C); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else
```

```
UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDRA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDRA> != '00') then AArch32.TakeHypTrapException(0x0C); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x0C); else R[t, t2] = DBGDRAR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDRA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDRA> ↪ → != '00' then AArch32.TakeHypTrapException(0x0C); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x0C); else R[t, t2] = DBGDRAR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x0C); else R[t, t2] = DBGDRAR; elsif PSTATE.EL == EL3 then R[t, t2] = DBGDRAR;
```

## G8.3.13 DBGDSAR, Debug Self Address Register

The DBGDSAR characteristics are:

## Purpose

In earlier versions of the Arm Architecture, this register defines the offset from the base address defined in DBGDRARofthe physical base address of the debug registers for the PE. Use of this register is deprecated.

## Configuration

DBGDSARis a 64-bit register that can also be accessed as a 32-bit value. If it is accessed as a 32-bit register, bits [31:0] are read.

If EL1 cannot use AArch32 then the implementation of this register is OPTIONAL and deprecated.

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DBGDSAR are UNDEFINED.

## Attributes

DBGDSARis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:2]

Reserved, RES0.

## Bits [1:0]

Reserved, RAZ.

This field indicates whether the debug self address offset is valid. For ARMv8, this field is always 0b00 , the offset is not valid.

## Accessing DBGDSAR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0010 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then R[t] = DBGDSAR<31:0>; elsif PSTATE.EL == EL0 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); else AArch64.AArch32SystemAccessTrap(EL1, 0x05); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDRA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDRA> != '00') then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDSAR<31:0>; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDRA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDRA> ↪ → != '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDSAR<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDSAR<31:0>; elsif PSTATE.EL == EL3 then R[t] = DBGDSAR<31:0>;
```

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1110   | 0b0010 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then R[t, t2] = DBGDSAR; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); else AArch64.AArch32SystemAccessTrap(EL1, 0x0C); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDRA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDRA> != '00') then AArch32.TakeHypTrapException(0x0C); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x0C); else R[t, t2] = DBGDSAR; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDRA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x0C); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDRA> ↪ → != '00' then AArch32.TakeHypTrapException(0x0C); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x0C); else R[t, t2] = DBGDSAR; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x0C); else R[t, t2] = DBGDSAR; elsif PSTATE.EL == EL3 then R[t, t2] = DBGDSAR;
```

## G8.3.14 DBGDSCRext, Debug Status and Control Register, External View

The DBGDSCRext characteristics are:

## Purpose

Main control register for the debug implementation.

## Configuration

This register is required in all implementations.

AArch32 System register DBGDSCRext bits [31:0] are architecturally mapped to AArch64 System register MDSCR\_EL1[31:0].

AArch32 System register DBGDSCRext bits [31:29, 27:26, 23:21, 19, 14, 6] are architecturally mapped to External register EDSCR[31:29, 27:26, 23:21, 19, 14, 6].

AArch32 System register DBGDSCRext bit [15] is architecturally mapped to AArch32 System register DBGDSCRint[15].

AArch32 System register DBGDSCRext bit [12] is architecturally mapped to AArch32 System register DBGDSCRint[12].

AArch32 System register DBGDSCRext bits [5:2] are architecturally mapped to AArch32 System register DBGDSCRint[5:2].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDSCRext are UNDEFINED.

## Attributes

DBGDSCRext is a 32-bit register.

## Field descriptions

<!-- image -->

## TFO, bit [31]

## When FEAT\_TRF is implemented:

Trace Filter override. Used for save/restore of EDSCR.TFO.

When the OS Lock is unlocked, DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When the OS Lock is locked, DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.TFO. Reads and writes of this bit are indirect accesses to EDSCR.TFO.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## Otherwise:

Reserved, RES0.

## RXfull, bit [30]

DTRRXfull. Used for save/restore of EDSCR.RXfull.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.RXfull. Reads and writes of this bit are indirect accesses to EDSCR.RXfull.

Arm deprecates use of this bit other than for save/restore. Use DBGDSCRint to access the DTRRX full status.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## TXfull, bit [29]

DTRTX full. Used for save/restore of EDSCR.TXfull.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.TXfull. Reads and writes of this bit are indirect accesses to EDSCR.TXfull.

Arm deprecates use of this bit other than for save/restore. Use DBGDSCRint to access the DTRTX full status.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## Bit [28]

Reserved, RES0.

## RXO, bit [27]

Used for save/restore of EDSCR.RXO.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.RXO. Reads and writes of this bit are indirect accesses to EDSCR.RXO.

When DBGOSLSR.OSLK == 1, if bits [27,6] of the value written to DBGDSCRext are {1,0}, that is, the RXO bit is 1 and the ERR bit is 0, the PE sets EDSCR.{RXO,ERR} to UNKNOWN values.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## TXU, bit [26]

Used for save/restore of EDSCR.TXU.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.TXU. Reads and writes of this bit are indirect accesses to EDSCR.TXU.

When DBGOSLSR.OSLK == 1, if bits [26,6] of the value written to DBGDSCRext are {1,0}, that is, the TXU bit is 1 and the ERR bit is 0, the PE sets EDSCR.{TXU,ERR} to UNKNOWN values.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## Bits [25:24]

Reserved, RES0.

## INTdis, bits [23:22]

Used for save/restore of EDSCR.INTdis.

When DBGOSLSR.OSLK == 0, software must treat it as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this field holds the value of EDSCR.INTdis. Reads and writes of this field are indirect accesses to EDSCR.INTdis.

The reset behavior of this field is:

- On a Cold reset, this field resets to '00' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## TDA, bit [21]

Used for save/restore of EDSCR.TDA.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.TDA. Reads and writes of this bit are indirect accesses to EDSCR.TDA.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## Bit [20]

Reserved, RES0.

## SC2, bit [19]

## When FEAT\_PCSRv8 is implemented, FEAT\_VHE is implemented, and FEAT\_PCSRv8p2 is not implemented:

Used for save/restore of EDSCR.SC2.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.SC2. Reads and writes of this bit are indirect accesses to EDSCR.SC2.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## Otherwise:

Reserved, RES0.

## NS, bit [18]

Non-secure status.

Arm deprecates use of this field.

Access to this field is RO.

## SPNIDdis, bit [17]

## When EL3 is implemented:

Secure privileged profiling disabled status bit.

| SPNIDdis   | Meaning                                          |
|------------|--------------------------------------------------|
| 0b0        | Profiling allowed in Secure privileged modes.    |
| 0b1        | Profiling prohibited in Secure privileged modes. |

This field reads as 0 if any of the following applies, and reads as 1 otherwise:

- FEAT\_Debugv8p2 is not implemented and ExternalSecureNoninvasiveDebugEnabled() returns TRUE.
- EL3 is using AArch32 and the value of SDCR.SPME is 1.
- EL3 is using AArch64 and the value of MDCR\_EL3.SPME is 1.

Arm deprecates use of this field.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## SPIDdis, bit [16]

## When EL3 is implemented:

Secure privileged AArch32 invasive self-hosted debug disabled status bit. The value of this bit depends on the value of SDCR.SPD and the pseudocode function

AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled() .

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

| SPIDdis   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0       | Self-hosted debug enabled in Secure privileged AArch32 modes.  |
| 0b1       | Self-hosted debug disabled in Secure privileged AArch32 modes. |

This bit reads as 1 if any of the following is true and reads as 0 otherwise:

- EL3 is using AArch32 and SDCR.SPD has the value 0b10 .
- EL3 is using AArch64 and MDCR\_EL3.SPD32 has the value 0b10 .

•

EL3 is using AArch32, SDCR.SPD has the value

0b00

, and

AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled()

returns FALSE.

- EL3 is using AArch64, MDCR\_EL3.SPD32 has the value 0b00 , and AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled() returns FALSE.

Arm deprecates use of this field.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## MDBGen, bit [15]

Monitor debug events enable. Enable Breakpoint, Watchpoint, and Vector Catch exceptions.

| MDBGen   | Meaning                                                       |
|----------|---------------------------------------------------------------|
| 0b0      | Breakpoint, Watchpoint, and Vector Catch exceptions disabled. |
| 0b1      | Breakpoint, Watchpoint, and Vector Catch exceptions enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## HDE, bit [14]

Used for save/restore of EDSCR.HDE.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.HDE. Reads and writes of this bit are indirect accesses to EDSCR.HDE.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## Bit [13]

Reserved, RES0.

## UDCCdis, bit [12]

Traps EL0 accesses to the DCC registers to Undefined mode.

| UDCCdis   | Meaning                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0       | This control does not cause any instructions to be trapped.                                                           |
| 0b1       | EL0 accesses to the DBGDSCRint, DBGDTRRXint, DBGDTRTXint, DBGDIDR, DBGDSAR, and DBGDRARare trapped to Undefined mode. |

Note

All accesses to these registers are trapped, including LDC and STC accesses to DBGDTRTXint and DBGDTRRXint, and MRRC accesses to DBGDSAR and DBGDRAR.

Traps of EL0 accesses to the DBGDTRRXint and DBGDTRTXint are ignored in Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [11:7]

Reserved, RES0.

## ERR, bit [6]

Used for save/restore of EDSCR.ERR.

When DBGOSLSR.OSLK == 0, software must treat this bit as UNK/SBZP.

When DBGOSLSR.OSLK == 1, this bit holds the value of EDSCR.ERR. Reads and writes of this bit are indirect accesses to EDSCR.ERR.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- When DBGOSLSR.OSLK == '1', access to this field is RW.
- When DBGOSLSR.OSLK == '0', access to this field is RO.

## MOE,bits [5:2]

Method of Entry for debug exception. When a debug exception is taken to an Exception level using AArch32, this field is set to indicate the event that caused the exception:

| MOE    | Meaning                                 |
|--------|-----------------------------------------|
| 0b0001 | Breakpoint.                             |
| 0b0011 | Software breakpoint (BKPT) instruction. |
| 0b0101 | Vector catch.                           |
| 0b1010 | Watchpoint.                             |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## Accessing DBGDSCRext

Individual fields within this register might have restricted accessibility when the OS Lock is unlocked, DBGOSLSR.OSLK == 0. See the field descriptions for more detail.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0010 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDSCRext; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDSCRext; elsif PSTATE.EL == EL3 then R[t] = DBGDSCRext;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0010 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDSCRext = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDSCRext = R[t]; elsif PSTATE.EL == EL3 then DBGDSCRext = R[t];
```

## G8.3.15 DBGDSCRint, Debug Status and Control Register, Internal View

The DBGDSCRint characteristics are:

## Purpose

Main control register for the debug implementation. This is an internal, read-only view.

## Configuration

This register is required in all implementations.

DBGDSCRint.{NS, SPNIDdis, SPIDdis, MDBGen, UDCCdis, MOE} are UNKNOWN when the register is accessed at EL0. However, although these values are not accessible at EL0 by instructions that are neither UNPREDICTABLE nor return UNKNOWN values, it is permissible for an implementation to return the values of DBGDSCRext.{NS, SPNIDdis, SPIDdis, MDBGen, UDCCdis, MOE} for these fields at EL0.

It is also permissible for an implementation to return the same values as defined for a read of DBGDSCRint at EL1 or above. (This is the case even if the implementation does not support AArch32 at EL1 or above.)

AArch32 System register DBGDSCRint bits [30:29] are architecturally mapped to AArch64 System register MDCCSR\_EL0[30:29].

AArch32 System register DBGDSCRint bits [30:29] are architecturally mapped to External register EDSCR[30:29].

AArch32 System register DBGDSCRint bit [15] is architecturally mapped to AArch64 System register MDSCR\_EL1[15].

AArch32 System register DBGDSCRint bit [12] is architecturally mapped to AArch64 System register MDSCR\_EL1[12].

AArch32 System register DBGDSCRint bits [5:2] are architecturally mapped to AArch64 System register MDSCR\_EL1[5:2].

AArch32 System register DBGDSCRint bit [15] is architecturally mapped to AArch32 System register DBGDSCRext[15].

AArch32 System register DBGDSCRint bit [12] is architecturally mapped to AArch32 System register DBGDSCRext[12].

AArch32 System register DBGDSCRint bits [5:2] are architecturally mapped to AArch32 System register DBGDSCRext[5:2].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DBGDSCRint are UNDEFINED.

## Attributes

DBGDSCRint is a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES0.

RXfull, bit [30]

DTRRXfull. Read-only view of the equivalent bit in the EDSCR.

## TXfull, bit [29]

DTRTX full. Read-only view of the equivalent bit in the EDSCR.

## Bits [28:19]

Reserved, RES0.

## NS, bit [18]

Non-secure status.

Read-only view of the equivalent bit in the DBGDSCRext. Arm deprecates use of this field.

## SPNIDdis, bit [17]

Secure privileged non-invasive debug disable.

Read-only view of the equivalent bit in the DBGDSCRext. Arm deprecates use of this field.

## SPIDdis, bit [16]

Secure privileged invasive debug disable.

Read-only view of the equivalent bit in the DBGDSCRext. Arm deprecates use of this field.

## MDBGen, bit [15]

Monitor debug events enable.

Read-only view of the equivalent bit in the DBGDSCRext.

## Bits [14:13]

Reserved, RES0.

## UDCCdis, bit [12]

User mode access to Debug Communications Channel disable.

Read-only view of the equivalent bit in the DBGDSCRext. Arm deprecates use of this field.

## Bits [11:6]

Reserved, RES0.

## MOE,bits [5:2]

Method of Entry for debug exception. When a debug exception is taken to an Exception level using AArch32, this field is set to indicate the event that caused the exception:

| MOE    | Meaning                                |
|--------|----------------------------------------|
| 0b0001 | Breakpoint                             |
| 0b0011 | Software breakpoint (BKPT) instruction |
| 0b0101 | Vector catch                           |
| 0b1010 | Watchpoint                             |

Read-only view of the equivalent bit in the DBGDSCRext.

## Bits [1:0]

Reserved, RES0.

## Accessing DBGDSCRint

When &lt;Rt&gt; is APSR\_nzcv, encoded as R15, then instead of reading the entire register, the access copies DBGDSCRint[31:28] into the PSTATE NZCV flags.

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then if t == 15 then ConstrainUnpredictableProcedure(Unpredictable_MRC_APSR_TARGET); else R[t] = DBGDSCRint; elsif PSTATE.EL == EL0 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); else AArch64.AArch32SystemAccessTrap(EL1, 0x05); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && HDCR.TDCC == '1' then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDA> != '00') then AArch32.TakeHypTrapException(0x05);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else if t == 15 then if Halted() then ConstrainUnpredictableProcedure(Unpredictable_MRC_APSR_TARGET); else PSTATE.<N,Z,C,V> = DBGDSCRint<31:28>; else R[t] = DBGDSCRint; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05);
```

```
else if t == 15 then if Halted() then ConstrainUnpredictableProcedure(Unpredictable_MRC_APSR_TARGET); else PSTATE.<N,Z,C,V> = DBGDSCRint<31:28>; else R[t] = DBGDSCRint; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else if t == 15 then if Halted() then ConstrainUnpredictableProcedure(Unpredictable_MRC_APSR_TARGET); else PSTATE.<N,Z,C,V> = DBGDSCRint<31:28>; else R[t] = DBGDSCRint; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else if t == 15 then if Halted() then ConstrainUnpredictableProcedure(Unpredictable_MRC_APSR_TARGET); else PSTATE.<N,Z,C,V> = DBGDSCRint<31:28>; else R[t] = DBGDSCRint;
```

## G8.3.16 DBGDTRRXext, Debug OS Lock Data Transfer Register, Receive, External View

The DBGDTRRXext characteristics are:

## Purpose

Used for save/restore of DBGDTRRXint. It is a component of the Debug Communications Channel.

## Configuration

AArch32 System register DBGDTRRXext bits [31:0] are architecturally mapped to AArch64 System register OSDTRRX\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDTRRXext are UNDEFINED.

## Attributes

DBGDTRRXext is a 32-bit register.

## Field descriptions

```
Update DTRRX without side-effect 31 0
```

## DTRRX, bits [31:0]

Update DTRRX without side-effect.

Writes to this register update the value in DTRRX and do not change RXfull.

Reads of this register return the last value written to DTRRX and do not change RXfull.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRRXext

Arm deprecates reads and writes of DBGDTRRXext through the System register interface when the OS Lock is unlocked, DBGOSLSR.OSLK == 0.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then
```

```
R[t] = DBGDTRRXext; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDTRRXext; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA ==
```

```
↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDTRRXext; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else R[t] = DBGDTRRXext;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then DBGDTRRXext = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDTRRXext = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDTRRXext = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else DBGDTRRXext = R[t];
```

## G8.3.17 DBGDTRRXint, Debug Data Transfer Register, Receive

The DBGDTRRXint characteristics are:

## Purpose

Transfers data from an external debugger to the PE. For example, it is used by a debugger transferring commands and data to a debug target. See DBGDTR\_EL0 for additional architectural mappings. It is a component of the Debug Communications Channel.

## Configuration

AArch32 System register DBGDTRRXint bits [31:0] are architecturally mapped to AArch64 System register DBGDTRRX\_EL0[31:0].

AArch32 System register DBGDTRRXint bits [31:0] are architecturally mapped to External register DBGDTRRX\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DBGDTRRXint are UNDEFINED.

## Attributes

DBGDTRRXint is a 32-bit register.

## Field descriptions

<!-- image -->

## DTRRX, bits [31:0]

Update DTRRX.

Reads of this register:

- If RXfull is 1, return the last value written to DTRRX.
- If RXfull is 0, return an UNKNOWN value.

After the read, RXfull is cleared to 0.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRRXint

Data can be stored to memory from this register using STC.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0101 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() then R[t] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); else AArch64.AArch32SystemAccessTrap(EL1, 0x05); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && HDCR.TDCC == '1' then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDA> != '00') then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then
```

```
AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else R[t] = Read_DBGDTR_EL0(32);
```

STC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, &lt;CRd&gt;, &lt;addressing\_mode&gt;

| coproc   | CRd    |
|----------|--------|
| 0b1110   | 0b0101 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() then MemA[address, 4] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); else AArch64.AArch32SystemAccessTrap(EL1, 0x06); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && HDCR.TDCC == '1' then AArch32.TakeHypTrapException(0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDA> != '00') then
```

```
AArch32.TakeHypTrapException(0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); else MemA[address, 4] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x06); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); else MemA[address, 4] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); else MemA[address, 4] = Read_DBGDTR_EL0(32); elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else MemA[address, 4] = Read_DBGDTR_EL0(32);
```

## G8.3.18 DBGDTRTXext, Debug OS Lock Data Transfer Register, Transmit

The DBGDTRTXext characteristics are:

Purpose

Used for save/restore of DBGDTRTXint. It is a component of the Debug Communication Channel.

## Configuration

AArch32 System register DBGDTRTXext bits [31:0] are architecturally mapped to AArch64 System register OSDTRTX\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGDTRTXext are UNDEFINED.

## Attributes

DBGDTRTXext is a 32-bit register.

## Field descriptions

```
Return DTRTX without side-effect 31 0
```

## DTRTX, bits [31:0]

Return DTRTX without side-effect.

Reads of this register return the value in DTRTX and do not change TXfull.

Writes of this register update the value in DTRTX and do not change TXfull.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRTXext

Arm deprecates reads and writes of DBGDTRTXext through the System register interface when the OS Lock is unlocked, DBGOSLSR.OSLK == 0.

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0011 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then
```

```
R[t] = DBGDTRTXext; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDTRTXext; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA ==
```

```
↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGDTRTXext; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else R[t] = DBGDTRTXext;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0011 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif Halted() && ConstrainUnpredictableBool(Unpredictable_IGNORETRAPINDEBUG) then DBGDTRTXext = R[t]; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDTRTXext = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TDCC == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGDTRTXext = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else DBGDTRTXext = R[t];
```

## G8.3.19 DBGDTRTXint, Debug Data Transfer Register, Transmit

The DBGDTRTXint characteristics are:

## Purpose

Transfers data from the PE to an external debugger. For example, it is used by a debug target to transfer data to the debugger. See DBGDTR\_EL0 for additional architectural mappings. It is a component of the Debug Communication Channel.

## Configuration

AArch32 System register DBGDTRTXint bits [31:0] are architecturally mapped to AArch64 System register DBGDTRTX\_EL0[31:0].

AArch32 System register DBGDTRTXint bits [31:0] are architecturally mapped to External register DBGDTRTX\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DBGDTRTXint are UNDEFINED.

## Attributes

DBGDTRTXint is a 32-bit register.

## Field descriptions

## DTRTX, bits [31:0]

DTRTX. Writes to this register:

- If TXfull is 1, DTRTX is set to an UNKNOWN value.
- If TXfull is 0, update the value in DTRTX.

After the write, TXfull is set to 1.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRTXint

Data can be loaded from memory into this register using 'LDC (immediate)' and 'LDC (literal)'.

Accesses to this register use the following encodings in the System register encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0101 | 0b000  |

31

Return DTRTX

0

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() then Write_DBGDTR_EL0(R[t]); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); else AArch64.AArch32SystemAccessTrap(EL1, 0x05); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && HDCR.TDCC == '1' then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDA> != '00') then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); else Write_DBGDTR_EL0(R[t]); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05);
```

```
else Write_DBGDTR_EL0(R[t]); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x05); else Write_DBGDTR_EL0(R[t]); elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else Write_DBGDTR_EL0(R[t]);
```

LDC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, &lt;CRd&gt;, &lt;addressing\_mode&gt;

| coproc   | CRd    |
|----------|--------|
| 0b1110   | 0b0101 |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif Halted() then Write_DBGDTR_EL0(MemA[address, 4]); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && MDSCR_EL1.TDCC == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); else AArch64.AArch32SystemAccessTrap(EL1, 0x06); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && DBGDSCRext.UDCCdis == '1' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && ↪ → IsFeatureImplemented(FEAT_FGT) && HDCR.TDCC == '1' then AArch32.TakeHypTrapException(0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && (HCR_EL2.TGE ↪ → == '1' || MDCR_EL2.<TDE,TDA> != '00') then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && (HCR.TGE == '1' ↪ → || HDCR.<TDE,TDA> != '00') then AArch32.TakeHypTrapException(0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); else Write_DBGDTR_EL0(MemA[address, 4]); elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL2.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TDCC == '1' ↪ → then AArch32.TakeHypTrapException(0x06); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x06); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); else Write_DBGDTR_EL0(MemA[address, 4]); elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsFeatureImplemented(FEAT_FGT) && MDCR_EL3.TDCC == '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TDCC == '1' ↪ → then AArch32.TakeMonitorTrapException(); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x06); else Write_DBGDTR_EL0(MemA[address, 4]); elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TDCC == '1' then AArch32.TakeMonitorTrapException(); else Write_DBGDTR_EL0(MemA[address, 4]);
```

## G8.3.20 DBGOSDLR, Debug OS Double Lock Register

The DBGOSDLR characteristics are:

## Purpose

Locks out the external debug interface.

## Configuration

AArch32 System register DBGOSDLR bits [31:0] are architecturally mapped to AArch64 System register OSDLR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGOSDLR are UNDEFINED.

## Attributes

DBGOSDLRis a 32-bit register.

## Field descriptions

| 31   | 1 0   |
|------|-------|
|      | DLK   |

## Bits [31:1]

Reserved, RES0.

DLK, bit [0]

## When FEAT\_DoubleLock is implemented:

OS Double Lock control bit.

| DLK   | Meaning                                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------------------|
| 0b0   | OS Double Lock unlocked.                                                                                                  |
| 0b1   | OS Double Lock locked, if DBGPRCR.CORENPDRQ (Core no powerdown request) bit is set to 0 and the PE is in Non-debug state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RAZ/WI.

## Accessing DBGOSDLR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0011 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || ↪ → boolean IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDOSA> != '00' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean ↪ → IMPLEMENTATION_DEFINED "Trapped by MDCR_EL2.TDOSA") then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDOSA> ↪ → != '00' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped ↪ → by HDCR.TDOSA") then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGOSDLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || ↪ → boolean IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGOSDLR; elsif PSTATE.EL == EL3 then R[t] = DBGOSDLR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0011 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || ↪ → boolean IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDOSA> != '00' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean ↪ → IMPLEMENTATION_DEFINED "Trapped by MDCR_EL2.TDOSA") then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDOSA> ↪ → != '00' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped ↪ → by HDCR.TDOSA") then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGOSDLR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' && (IsFeatureImplemented(FEAT_DoubleLock) || ↪ → boolean IMPLEMENTATION_DEFINED "Trapped by MDCR_EL3.TDOSA") then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' && (IsFeatureImplemented(FEAT_DoubleLock) || boolean IMPLEMENTATION_DEFINED "Trapped by ↪ → MDCR_EL3.TDOSA") then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGOSDLR = R[t]; elsif PSTATE.EL == EL3 then DBGOSDLR = R[t];
```

## G8.3.21 DBGOSECCR, Debug OS Lock Exception Catch Control Register

The DBGOSECCR characteristics are:

## Purpose

Provides a mechanism for an operating system to access the contents of EDECCR that are otherwise invisible to software, so it can save/restore the contents of EDECCR over powerdown on behalf of the external debugger.

## Configuration

If DBGOSLSR.OSLK == 0 then DBGOSECCR returns an UNKNOWN value on reads and ignores writes.

AArch32 System register DBGOSECCR bits [31:0] are architecturally mapped to AArch64 System register OSECCR\_EL1[31:0].

AArch32 System register DBGOSECCR bits [31:0] are architecturally mapped to External register EDECCR[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGOSECCR are UNDEFINED.

## Attributes

DBGOSECCRis a 32-bit register.

## Field descriptions

When DBGOSLSR.OSLK == '1':

31

EDECCR

## EDECCR, bits [31:0]

Used for save/restore to EDECCR over powerdown.

Reads or writes to this field are indirect accesses to EDECCR.

The reset behavior of this field is:

- On a Cold reset, this field resets to 0x00000000 .

## Accessing DBGOSECCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0110 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

0

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' then R[t] = bits(32) UNKNOWN; else R[t] = DBGOSECCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' then R[t] = bits(32) UNKNOWN; else R[t] = DBGOSECCR; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' then R[t] = bits(32) UNKNOWN; else R[t] = DBGOSECCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0110 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' then return; else DBGOSECCR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' then return; else DBGOSECCR = R[t]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' then return; else DBGOSECCR = R[t];
```

## G8.3.22 DBGOSLAR, Debug OS Lock Access Register

The DBGOSLAR characteristics are:

## Purpose

Provides a lock for the debug registers. The OS Lock also disables some debug exceptions and debug events.

## Configuration

The OS Lock can also be locked or unlocked using the AArch64 System register OSLAR\_EL1 and External register OSLAR\_EL1.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGOSLAR are UNDEFINED.

## Attributes

DBGOSLARis a 32-bit register.

## Field descriptions

```
OSLA 31 0
```

## OSLA, bits [31:0]

OS Lock Access. Writing the value 0xC5ACCE55 to the DBGOSLAR sets the OS Lock to 1. Writing any other value sets the OS Lock to 0.

Use DBGOSLSR.OSLK to check the current status of the lock.

## Accessing DBGOSLAR

Accesses to this register use the following encodings in the System register encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0000 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDOSA> ↪ → != '00' then AArch32.TakeHypTrapException(0x05);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGOSLAR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGOSLAR = R[t]; elsif PSTATE.EL == EL3 then DBGOSLAR = R[t];
```

## G8.3.23 DBGOSLSR, Debug OS Lock Status Register

The DBGOSLSR characteristics are:

## Purpose

Provides status information for the OS Lock.

## Configuration

The OS Lock status is also visible in the external debug interface through EDPRSR.

AArch32 System register DBGOSLSR bits [31:0] are architecturally mapped to AArch64 System register OSLSR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGOSLSR are UNDEFINED.

## Attributes

DBGOSLSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:4]

Reserved, RES0.

## OSLM, bits [3, 0]

OS Lock model implemented. Identifies the form of OS save and restore mechanism implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

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

## Accessing DBGOSLSR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0001 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDOSA> ↪ → != '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGOSLSR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else
```

```
R[t] = DBGOSLSR; elsif PSTATE.EL == EL3 then R[t] = DBGOSLSR;
```

## G8.3.24 DBGPRCR, Debug Power Control Register

The DBGPRCR characteristics are:

## Purpose

Controls behavior of the PE on powerdown request.

## Configuration

AArch32 System register DBGPRCR bits [31:0] are architecturally mapped to AArch64 System register DBGPRCR\_EL1[31:0].

AArch32 System register DBGPRCR bit [0] is architecturally mapped to External register EDPRCR[0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGPRCR are UNDEFINED.

## Attributes

DBGPRCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:1]

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

It is IMPLEMENTATION DEFINED whether this bit is reset to the Cold reset value on exit from an IMPLEMENTATION DEFINED software-visible retention state. For more information about retention states see 'Core power domain power states'.

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

## Accessing DBGPRCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0100 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDOSA> ↪ → != '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGPRCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGPRCR; elsif PSTATE.EL == EL3 then R[t] = DBGPRCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0001 | 0b0100 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDOSA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDOSA> ↪ → != '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGPRCR = R[t]; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDOSA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGPRCR = R[t]; elsif PSTATE.EL == EL3 then DBGPRCR = R[t];
```

## G8.3.25 DBGVCR, Debug Vector Catch Register

The DBGVCR characteristics are:

## Purpose

Controls Vector Catch debug events.

## Configuration

This register is required in all implementations.

AArch32 System register DBGVCR bits [31:0] are architecturally mapped to AArch64 System register DBGVCR32\_EL2[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGVCR are UNDEFINED.

## Attributes

DBGVCRis a 32-bit register.

## Field descriptions

When EL3 is implemented and EL3 is using AArch32:

<!-- image -->

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

## Bits [24:16]

Reserved, RES0.

## MF, bit [15]

FIQ vector catch enable in Monitor mode.

The exception vector offset is 0x1C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## MI, bit [14]

IRQ vector catch enable in Monitor mode.

The exception vector offset is 0x18 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [13]

Reserved, RES0.

## MD, bit [12]

Data Abort exception vector catch enable in Monitor mode.

The exception vector offset is 0x10 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## MP, bit [11]

Prefetch Abort vector catch enable in Monitor mode.

The exception vector offset is 0x0C .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## MS, bit [10]

Secure Monitor Call (SMC) vector catch enable in Monitor mode.

The exception vector offset is 0x08 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [9:8]

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

When EL3 is implemented and EL3 is using AArch64:

<!-- image -->

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

## Bits [31:8]

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

## Accessing DBGVCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0111 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05);
```

```
else R[t] = DBGVCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGVCR; elsif PSTATE.EL == EL3 then R[t] = DBGVCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0111 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGVCR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGVCR = R[t]; elsif PSTATE.EL == EL3 then DBGVCR = R[t];
```

## G8.3.26 DBGWCR&lt;n&gt;, Debug Watchpoint Control Registers, n = 0 - 15

The DBGWCR&lt;n&gt; characteristics are:

## Purpose

Holds control information for a watchpoint. Forms watchpoint n together with value register DBGWVR&lt;n&gt;.

## Configuration

If watchpoint n is not implemented then accesses to this register are UNDEFINED.

AArch32 System register DBGWCR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register DBGWCR&lt;n&gt;\_EL1[31:0].

AArch32 System register DBGWCR&lt;n&gt; bits [31:0] are architecturally mapped to External register DBGWCR&lt;n&gt;\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGWCR&lt;n&gt; are UNDEFINED.

## Attributes

DBGWCR&lt;n&gt;is a 32-bit register.

## Field descriptions

| 31   | 29 28   | 24 23   | 21 20 19   | 2 1 0   | 16 15 14 13 12 5 4 3   |
|------|---------|---------|------------|---------|------------------------|
| RES0 | MASK    | RES0    | WT         | PAC     | SSC HMC BAS LSC E      |

When the E field is zero, all the other fields in the register are ignored.

## Bits [31:29]

Reserved, RES0.

## MASK, bits [28:24]

Address Mask. Only objects up to 2GB can be watched using a single mask.

| MASK               | Meaning                        |
|--------------------|--------------------------------|
| 0b00000            | No mask.                       |
| 0b00011 .. 0b11111 | Number of address bits masked. |

All other values are reserved.

Indicates the number of masked address bits, from 0b00011 masking 3 address bits ( 0x00000007 mask for address) to 0b11111 masking 31 address bits ( 0x7FFFFFFF mask for address).

If programmed with a reserved value, the watchpoint behaves as if either:

- DBGWCR&lt;n&gt;.MASK has been programmed with a defined value, which might be 0 (no mask), other than for a direct read of DBGWCR&lt;n&gt;.
- The watchpoint is disabled.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [23:21]

Reserved, RES0.

## WT, bit [20]

Watchpoint type. Possible values are:

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## LBN, bits [19:16]

Linked Breakpoint Number. For Linked data address watchpoints, this specifies the index of the Context-matching breakpoint linked to.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## SSC, bits [15:14]

Security state control. Determines the Security states under which a Watchpoint debug event for watchpoint n is generated. This field must be interpreted along with the HMC and PAC fields.

For more information, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions', and 'Reserved DBGWCR&lt;n&gt;.{SSC, HMC, PAC} values'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## HMC,bit [13]

Higher mode control. Determines the debug perspective for deciding when a Watchpoint debug event for watchpoint n is generated. This field must be interpreted along with the SSC and PAC fields.

For more information on the operation of the SSC, HMC, and PAC fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## BAS, bits [12:5]

Byte address select. Each bit of this field selects whether a byte from within the word or double-word addressed by DBGWVR&lt;n&gt;is being watched.

| WT   | Meaning                      |
|------|------------------------------|
| 0b0  | Unlinked data address match. |
| 0b1  | Linked data address match.   |

| BAS        | Description               |
|------------|---------------------------|
| 0bxxxxxxx1 | Match byte atDBGWVR<n>    |
| 0bxxxxxx1x | Match byte at DBGWVR<n>+1 |
| 0bxxxxx1xx | Match byte at DBGWVR<n>+2 |
| 0bxxxx1xxx | Match byte at DBGWVR<n>+3 |

In cases where DBGWVR&lt;n&gt; addresses a double-word:

| BAS        | Description, if DBGWVR<n>[2] == 0   |
|------------|-------------------------------------|
| 0bxxx1xxxx | Match byte at DBGWVR<n>+4           |
| 0bxx1xxxxx | Match byte at DBGWVR<n>+5           |
| 0bx1xxxxxx | Match byte at DBGWVR<n>+6           |
| 0b1xxxxxxx | Match byte at DBGWVR<n>+7           |

If DBGWVR&lt;n&gt;[2] == 1, only BAS[3:0] are used and BAS[7:4] are ignored. Arm deprecates setting DBGWVR&lt;n&gt;[2] == 1.

The valid values for BAS are nonzero binary numbers all of whose set bits are contiguous. All other values are reserved and must not be used by software. See 'Reserved DBGWCR&lt;n&gt;.BAS values'.

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

Privilege of access control. Determines the Exception level or levels at which a Watchpoint debug event for watchpoint n is generated. This field must be interpreted along with the SSC and HMC fields.

For more information on the operation of the SSC, HMC, and PAC fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E, bit [0]

Enable watchpoint n. Possible values are:

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGWCR&lt;n&gt;

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>} ; Where m = 0-15
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b111  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_WATCHPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGWCR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED;
```

| E   | Meaning              |
|-----|----------------------|
| 0b0 | Watchpoint disabled. |
| 0b1 | Watchpoint enabled.  |

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGWCR[m]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGWCR[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b111  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_WATCHPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGWCR[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then
```

```
Halt(DebugHalt_SoftwareAccess); else DBGWCR[m] = R[t]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGWCR[m] = R[t];
```

## G8.3.27 DBGWFAR, Debug Watchpoint Fault Address Register

The DBGWFAR characteristics are:

## Purpose

Previously returned information about the address of the instruction that accessed a watchpointed address. Is now deprecated and RES0.

## Configuration

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGWFAR are UNDEFINED.

## Attributes

DBGWFARis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:0]

Reserved, RES0.

## Accessing DBGWFAR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0110 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else
```

```
AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGWFAR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else R[t] = DBGWFAR; elsif PSTATE.EL == EL3 then R[t] = DBGWFAR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | 0b0110 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGWFAR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); else DBGWFAR = R[t]; elsif PSTATE.EL == EL3 then DBGWFAR = R[t];
```

## G8.3.28 DBGWVR&lt;n&gt;, Debug Watchpoint Value Registers, n = 0 - 15

The DBGWVR&lt;n&gt; characteristics are:

## Purpose

Holds a data address value for use in watchpoint matching. Forms watchpoint n together with control register DBGWCR&lt;n&gt;.

## Configuration

If watchpoint n is not implemented then accesses to this register are UNDEFINED.

AArch32 System register DBGWVR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register DBGWVR&lt;n&gt;\_EL1[31:0].

AArch32 System register DBGWVR&lt;n&gt; bits [31:0] are architecturally mapped to External register DBGWVR&lt;n&gt;\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DBGWVR&lt;n&gt; are UNDEFINED.

## Attributes

DBGWVR&lt;n&gt;is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 2 1 0   |
|------|---------|
|      | RES0    |

## VA, bits [31:2]

Bits[31:2] of the address value for comparison.

Arm deprecates setting DBGWVR&lt;n&gt;[2] == 1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [1:0]

Reserved, RES0.

## Accessing DBGWVR&lt;n&gt;

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b110  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_WATCHPOINTS then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGWVR[m]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGWVR[m]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else R[t] = DBGWVR[m];
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;} ; Where m = 0-15

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1110   | 0b000  | 0b0000 | m[3:0] | 0b110  |

```
integer m = UInt(CRm<3:0>); if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif m >= NUM_WATCHPOINTS then UNDEFINED;
```

```
elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x05); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.<TDE,TDA> != ↪ → '00' then AArch32.TakeHypTrapException(0x05); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGWVR[m] = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x05); elsif DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGWVR[m] = R[t]; elsif PSTATE.EL == EL3 then if DBGOSLSR.OSLK == '0' && HaltingAllowed() && EDSCR.TDA == '1' then Halt(DebugHalt_SoftwareAccess); else DBGWVR[m] = R[t];
```

## G8.3.29 DLR, Debug Link Register

The DLR characteristics are:

## Purpose

In Debug state, holds the address to restart from.

## Configuration

AArch32 System register DLR bits [31:0] are architecturally mapped to AArch64 System register DLR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DLR are UNDEFINED.

## Attributes

DLRis a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## ADDR, bits [31:0]

Restart address.

## Accessing DLR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b011  | 0b0100 | 0b0101 | 0b001  |

if !IsFeatureImplemented(FEAT\_AA32) then

```
UNDEFINED; elsif !Halted() then UNDEFINED; else R[t] = DLR;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b011  | 0b0100 | 0b0101 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif !Halted() then UNDEFINED; else DLR = R[t];
```

## G8.3.30 DSPSR, Debug Saved Program Status Register

The DSPSR characteristics are:

## Purpose

Holds the saved process state for Debug state. On entering Debug state, PSTATE information is written to this register. On exiting Debug state, values are copied from this register to PSTATE.

## Configuration

AArch32 System register DSPSR bits [31:0] are architecturally mapped to AArch64 System register DSPSR\_EL0[31:0].

This register is present only when FEAT\_AA32 is implemented. Otherwise, direct accesses to DSPSR are UNDEFINED.

## Attributes

DSPSR is a 32-bit register.

## Field descriptions

<!-- image -->

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

## Q, bit [27]

Overflow or saturation flag. Set to the value of PSTATE.Q on entering Debug state, and copied to PSTATE.Q on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IT, bits [15:10, 26:25]

If-Then. Set to the value of PSTATE.IT on entering Debug state, and copied to PSTATE.IT on exiting Debug state.

On exiting Debug state, DSPSR.IT must contain a value that is valid for the instruction being returned to.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DIT, bit [24]

## When FEAT\_DIT is implemented:

Data Independent Timing. Set to the value of PSTATE.DIT on entering Debug state, and copied to PSTATE.DIT on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SSBS, bit [23]

## When FEAT\_SSBS is implemented:

Speculative Store Bypass. Set to the value of PSTATE.SSBS on entering Debug state, and copied to PSTATE.SSBS on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## PAN, bit [22]

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

## GE, bits [19:16]

Greater than or Equal flags. Set to the value of PSTATE.GE on entering Debug state, and copied to PSTATE.GE on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## E, bit [9]

Endianness. Set to the value of PSTATE.E on entering Debug state, and copied to PSTATE.E on exiting Debug state.

If the implementation does not support big-endian operation, DSPSR.E is RES0. If the implementation does not support little-endian operation, DSPSR.E is RES1. On exiting Debug state, if the implementation does not support big-endian operation at the Exception level being returned to, DSPSR.E is RES0, and if the implementation does not support little-endian operation at the Exception level being returned to, DSPSR.E is RES1.

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

## T, bit [5]

T32 Instruction set state. Set to the value of PSTATE.T on entering Debug state, and copied to PSTATE.T on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M[4:0], bits [4:0]

Mode. Set to the value of PSTATE.M[4:0] on entering Debug state, and copied to PSTATE.M[4:0] on exiting Debug state.

| M[4:0]   | Meaning     | Applies when            |
|----------|-------------|-------------------------|
| 0b10000  | User.       |                         |
| 0b10001  | FIQ.        |                         |
| 0b10010  | IRQ.        |                         |
| 0b10011  | Supervisor. |                         |
| 0b10110  | Monitor.    | FEAT_EL3 is implemented |
| 0b10111  | Abort.      |                         |
| 0b11010  | Hyp.        |                         |
| 0b11011  | Undefined.  |                         |
| 0b11111  | System.     |                         |

Other values are reserved. If DSPSR.M[4:0] has a Reserved value, or a value for an unimplemented Exception level, exiting Debug state is an illegal return event, as described in 'Illegal return events from AArch32 state'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DSPSR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b011  | 0b0100 | 0b0101 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif !Halted() then UNDEFINED; else R[t] = DSPSR;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b011  | 0b0100 | 0b0101 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32) then UNDEFINED; elsif !Halted() then UNDEFINED; else DSPSR = R[t];
```

## G8.3.31 DSPSR2, Debug Saved Process State Register 2

The DSPSR2 characteristics are:

## Purpose

Holds the saved process state for Debug state. On entering Debug state, PSTATE information is written to this register. On exiting Debug state, values are copied from this register to PSTATE.

## Configuration

When FEAT\_Debugv8p9 is implemented, AArch32 System register DSPSR2 bits [31:0] are architecturally mapped to AArch64 System register DSPSR\_EL0[63:32].

This register is present only when FEAT\_Debugv8p9 is implemented and FEAT\_AA32 is implemented. Otherwise, direct accesses to DSPSR2 are UNDEFINED.

## Attributes

DSPSR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:5]

Reserved, RES0.

## UINJ, bit [4]

## When FEAT\_UINJ is implemented:

Inject Undefined Instruction exception. Set to the value of PSTATE.UINJ on entering Debug state, and copied to PSTATE.UINJ on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [3:2]

Reserved, RES0.

## PPEND, bit [1]

## When FEAT\_SEBEP is implemented:

PMUProfiling exception pending bit. Set to the value of PSTATE.PPEND on entering Debug state, and conditionally copied to PSTATE.PPEND on exiting Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [0]

Reserved, RES0.

## Accessing DSPSR2

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b011  | 0b0100 | 0b0101 | 0b010  |

```
if !(IsFeatureImplemented(FEAT_Debugv8p9) && IsFeatureImplemented(FEAT_AA32)) then UNDEFINED; elsif !Halted() then UNDEFINED; else R[t] = DSPSR2;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b011  | 0b0100 | 0b0101 | 0b010  |

## G8.3.32 HDCR, Hyp Debug Control Register

The HDCR characteristics are:

## Purpose

Controls the trapping to Hyp mode of Non-secure accesses, at EL1 or lower, to functions provided by the debug and trace architectures and the Performance Monitors Extension.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3, and other than for a direct read of the register, the PE behaves as if HDCR.HPMN == PMCR.N.

AArch32 System register HDCR bits [31:0] are architecturally mapped to AArch64 System register MDCR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HDCR are UNDEFINED.

## Attributes

HDCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:30]

Reserved, RES0.

HPMFZO,bit [29]

## When FEAT\_PMUv3p7 is implemented:

Hyp Performance Monitors Freeze-on-overflow. Stop event counters on overflow.

| HPMFZO   | Meaning                                                                   |
|----------|---------------------------------------------------------------------------|
| 0b0      | Do not freeze on overflow.                                                |
| 0b1      | Event counters do not count when PMOVSR[(PMCR.N-1):HDCR.HPMN] is nonzero. |

If HDCR.HPMN is less than PMCR.N, this field affects the operation of event counters in the range [HDCR.HPMN .. (PMCR.N-1)].

This field does not affect the operation of other event counters and PMCCNTR.

The operation of this field applies even when EL2 is disabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MTPME,bit [28]

## When FEAT\_MTPMU is implemented and EL3 is not implemented:

Multi-threaded PMU Enable. Enables use of the PMEVTYPER&lt;n&gt;.MT bits.

| MTPME   | Meaning                                                                 |
|---------|-------------------------------------------------------------------------|
| 0b0     | FEAT_MTPMU is disabled. The Effective value of PMEVTYPER<n>.MT is zero. |
| 0b1     | PMEVTYPER<n>.MT bits not affected by this bit.                          |

If FEAT\_MTPMU is disabled for any other PE in the system that has the same level 1 Affinity as the PE, it is IMPLEMENTATION DEFINED whether the PE behaves as if this bit is 0b0 .

The reset behavior of this field is:

- On a Cold reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '1' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TDCC, bit [27]

## When FEAT\_FGT is implemented:

Trap DCC. Traps use of the Debug Comms Channel at EL1 and EL0 to EL2.

| TDCC   | Meaning                                                                                                                                                                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any register accesses to be trapped.                                                                                                                                                                                                                             |
| 0b1    | If EL2 is implemented and enabled in the current Security state, accesses to the DCCregisters at EL1 and EL0 generate a Hyp Trap exception, unless the access also generates a higher priority exception. Traps on the DCCdata transfer registers are ignored when the PE is in Debug state. |

The DCC registers trapped by this control are:

- DBGDTRRXext, DBGDTRTXext, DBGDSCRint, DBGDCCINT, and, when the PE is in Non-debug state, DBGDTRRXint and DBGDTRTXint.

The traps are reported with EC syndrome value:

- 0x05 for trapped MRC and MCR accesses with coproc == 0b1110 .
- 0x06 for trapped LDC to DBGDTRTXint and STC from DBGDTRRXint.

When the PE is in Debug state, HDCR.TDCC does not trap any accesses to:

- DBGDTRRXint and DBGDTRTXint.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HLP, bit [26]

## When FEAT\_PMUv3p5 is implemented:

Hypervisor Long event counter enable. Determines when unsigned overflow is recorded by an event counter overflow bit.

| HLP   | Meaning                                                                                 |
|-------|-----------------------------------------------------------------------------------------|
| 0b0   | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>[31:0]. |
| 0b1   | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>[63:0]. |

If the highest implemented Exception level is using AArch32, it is IMPLEMENTATION DEFINED whether this bit is read/write or RAZ/WI.

If HDCR.HPMN is less than PMCR.N, this bit affects the operation of event counters in the range [HDCR.HPMN..(PMCR.N-1)].

This field does not affect the operation of other event counters.

The operation of this field applies even when EL2 is disabled in the current Security state.

Note

PMEVCNTR&lt;n&gt;[63:32] cannot be accessed directly in AArch32 state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [25:24]

Reserved, RES0.

## HCCD, bit [23]

## When FEAT\_PMUv3p5 is implemented:

Hypervisor Cycle Counter Disable. Prohibits PMCCNTR from counting at EL2.

| HCCD   | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0    | Cycle counting by PMCCNTRis not affected by this mechanism. |
| 0b1    | Cycle counting by PMCCNTRis prohibited at EL2.              |

This field does not affect the CPU\_CYCLES event or any other event that counts cycles.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [22:20]

Reserved, RES0.

## TTRF, bit [19]

## When FEAT\_TRF is implemented:

Traps use of the Trace Filter Control registers at EL1 to EL2 for MRC or MCR accesses, reported using EC syndrome value 0x03 .

| TTRF   | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0    | Accesses to TRFCR at EL1 are not affected by this control bit. |
| 0b1    | Accesses to TRFCR at EL1 generate a Hyp Trap exception.        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [18]

Reserved, RES0.

## HPMD,bit [17]

## When FEAT\_PMUv3p1 is implemented and FEAT\_Debugv8p2 is implemented:

Guest Performance Monitors Disable. Controls PMU operation in Hyp mode.

| HPMD   | Meaning                                                                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Counters are not affected by this mechanism.                                                                                                                           |
| 0b1    | Affected counters are prohibited from counting in Hyp mode. If PMCR.DP is 1, then PMCCNTRis disabled in Hyp mode. Otherwise, PMCCNTRis not affected by this mechanism. |

The counters affected by this field are:

- Event counters PMEVCNTR&lt;n&gt; for values of n less than HDCR.HPMN.
- If PMCR.DP is 1, the cycle counter PMCCNTR.

Other event counters are not affected by this field.

When PMCR.DP is 0, PMCCNTR is not affected by this field.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## When FEAT\_PMUv3p1 is implemented:

Guest Performance Monitors Disable. Controls PMU operation in Hyp mode when ExternalSecureNoninvasiveDebugEnabled() is FALSE.

| HPMD   | Meaning                                                                                                                                                                                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Counters are not affected by this mechanism.                                                                                                                                                                                                                        |
| 0b1    | If ExternalSecureNoninvasiveDebugEnabled() is FALSE, then all the following apply: • Affected event counters are prohibited from counting in Hyp mode. • If PMCR.DP is 1, then PMCCNTRis disabled in Hyp mode. Otherwise, PMCCNTRis not affected by this mechanism. |

If ExternalSecureNoninvasiveDebugEnabled() is TRUE, then the event counters and PMCCNTR are not affected by this field.

Otherwise, the counters affected by this field are:

- Event counters PMEVCNTR&lt;n&gt; for values of n less than HDCR.HPMN.
- If PMCR.DP is 1, the cycle counter, PMCCNTR.

Other event counters are not affected by this field. When PMCR.DP is 0, PMCCNTR is not affected by this field.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:12]

Reserved, RES0.

## TDRA, bit [11]

Trap Debug ROM Address register access. Traps Non-secure EL0 and EL1 System register MRC or MCR accesses, reported using EC syndrome value 0x05 , and MRRC accesses, reported using EC syndrome value 0x0C , to the Debug ROM registers to Hyp mode.

| TDRA   | Meaning                                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                 |
| 0b1    | Non-secure EL0 and EL1 System register accesses to theDBGDRARor DBGDSARare trapped to Hyp mode, unless it is trapped by DBGDSCRext.UDCCdis. |

If HCR.TGE or HDCR.TDE is 1, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TDOSA, bit [10]

## When FEAT\_DoubleLock is implemented:

Trap debug OS-related register access. Traps Non-secure EL1 System register MRC or MCR accesses, reported using EC syndrome value 0x05 , to the powerdown debug registers to Hyp mode.

| TDOSA   | Meaning                                                                                           |
|---------|---------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                       |
| 0b1     | Non-secure EL1 System register accesses to the powerdown debug registers are trapped to Hyp mode. |

The registers for which accesses are trapped are as follows:

- DBGOSLSR, DBGOSLAR, DBGOSDLR, and DBGPRCR.
- Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this bit.

Note

These registers are not accessible at EL0.

If HCR.TGE or HDCR.TDE is 1, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Trap debug OS-related register access. Traps Non-secure EL1 System register MRC or MCR accesses, reported using EC syndrome value 0x05 , to the powerdown debug registers to Hyp mode.

| TDOSA   | Meaning                                                     |
|---------|-------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped. |

| TDOSA   | Meaning                                                                                           |
|---------|---------------------------------------------------------------------------------------------------|
| 0b1     | Non-secure EL1 System register accesses to the powerdown debug registers are trapped to Hyp mode. |

The registers for which accesses are trapped are as follows:

- DBGOSLSR, DBGOSLAR, and DBGPRCR.
- Any IMPLEMENTATION DEFINED register with similar functionality that the implementation specifies as trapped by this bit.

It is IMPLEMENTATION DEFINED whether accesses to DBGOSDLR are trapped.

| Note                                       |
|--------------------------------------------|
| These registers are not accessible at EL0. |

If HCR.TGE or HDCR.TDE is 1, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TDA, bit [9]

Trap debug access. Traps Non-secure EL0 and EL1 System register MRC or MCR accesses, reported using EC syndrome value 0x05 , to those debug System registers in the (coproc== 0b1110 ) encoding space that are not trapped by either of the following:

- HDCR.TDRA.
- HDCR.TDOSA.

| TDA   | Meaning                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                               |
| 0b1   | Non-secure EL0 or EL1 System register accesses to the debug registers, other than the registers trapped by HDCR.TDRA and HDCR.TDOSA, are trapped to Hyp mode, unless it is trapped by DBGDSCRext.UDCCdis. |

Traps of AArch32 accesses to DBGDTRRXint and DBGDTRTXint are ignored in Debug state.

If HCR.TGE or HDCR.TDE is 1, behavior is as if this bit is 1 other than for the purpose of a direct read.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TDE, bit [8]

Trap Debug exceptions. Controls routing of Debug exceptions, and defines the debug target Exception level, ELD.

| TDE   | Meaning                                                                                                                                                                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The debug target Exception level is EL1.                                                                                                                                                                                                                                                              |
| 0b1   | If EL2 is enabled for the current Effective value of SCR.NS, the debug target Exception level is EL2, otherwise the debug target Exception level is EL1. The HDCR.{TDRA, TDOSA, TDA} fields are treated as being 1 for all purposes other than returning the result of a direct read of the register. |

For more information, see 'Routing debug exceptions'.

When HCR.TGE == 1, the PE behaves as if the value of this field is 1 for all purposes other than returning the value of a direct read of the register.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## HPME, bit [7]

## When FEAT\_PMUv3 is implemented:

Hyp Enable.

| HPME   | Meaning                                          |
|--------|--------------------------------------------------|
| 0b0    | Affected counters are disabled and do not count. |
| 0b1    | Affected counters are enabled by PMCNTENSET.     |

The counters affected by this field are event counters PMEVCNTR&lt;n&gt; for values of n greater than or equal to HDCR.HPMN and less than PMCR.N. This applies even when EL2 is disabled in the current Security state.

Other event counters and PMCCNTR are not affected by this field.

If HDCR.HPMN is equal to PMCR.N, then this field has no effect.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TPM, bit [6]

## When FEAT\_PMUv3 is implemented:

Trap accesses of PMU registers. Enables a trap to EL2 on accesses of PMU registers.

| TPM   | Meaning                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses of the specified PMUregisters are not trapped by this mechanism.                                                               |
| 0b1   | Accesses of the specified PMUregisters at EL1 and EL0 are trapped to EL2, unless the instruction generates a higher priority exception. |

The instructions affected by this control are:

- MRC and MCR accesses to PMCCFILTR, PMCCNTR, PMCNTENCLR, PMCNTENSET, PMCR, PMEVCNTR&lt;n&gt;, PMEVTYPER&lt;n&gt;, PMINTENCLR, PMINTENSET, PMOVSR, PMOVSSET, PMSELR, PMSWINC, PMUSERENR, PMXEVCNTR, and PMXEVTYPER.
- MRC accesses to PMCEID0 and PMCEID1.
- MRRC and MCRR accesses to PMCCNTR.
- If FEAT\_PMUv3p1 is implemented, MRC accesses to PMCEID2 and PMCEID3.
- If FEAT\_PMUv3p4 is implemented, MRC accesses to PMMIR.

Unless the instruction generates a higher priority exception, trapped instructions generate a Hyp Trap exception.

Trapped instructions are reported using EC syndrome value 0x03 for MRC and MCR accesses, and 0x04 for MRRC and MCRR accesses.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TPMCR, bit [5]

## When FEAT\_PMUv3 is implemented:

Trap PMCR accesses. Traps Non-secure EL0 and EL1 MCR or MRC accesses to the PMCR to Hyp mode, reported using EC syndrome value 0x03 .

| TPMCR   | Meaning                                                                                                   |
|---------|-----------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                               |
| 0b1     | Non-secure EL0 and EL1 accesses to the PMCRare trapped to Hyp mode, unless it is trapped by PMUSERENR.EN. |

Note

EL2 does not provide traps on Performance Monitor register accesses through the optional memory-mapped external debug interface.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HPMN,bits [4:0]

## When FEAT\_PMUv3 is implemented:

Defines the number of event counters PMEVCNTR&lt;n&gt; that are accessible from EL1 and, if permitted, from EL0.

HDCR.HPMN divides the event counters into a first range and a second range.

If HDCR.HPMN is not 0 and is less than the number of PMU event counters implemented by the PE, NUM\_PMU\_COUNTERS , then event counters [0..(HDCR.HPMN-1)] are in the first range, and the remaining event counters [HDCR.HPMN..( NUM\_PMU\_COUNTERS -1)] are in the second range.

If FEAT\_HPMN0 is implemented and HDCR.HPMN is 0, then all of the following apply:

- No event counters are in the first range.
- All event counters are in the second range.

If HDCR.HPMN is equal to NUM\_PMU\_COUNTERS , or EL2 is not implemented, then all of the following apply:

- All event counters are in the first range.
- No event counters are in the second range.

All of the following apply for an event counter PMEVCNTR&lt;n&gt; in the first range:

- The counter is accessible from EL1, EL2, and EL3.
- The counter is accessible from EL0 if permitted by PMUSERENR.
- If FEAT\_PMUv3p5 is implemented, then PMCR.LP determines whether the counter overflow flag PMOVSSET[n] is set on unsigned overflow of PMEVCNTR&lt;n&gt;[31:0] or PMEVCNTR&lt;n&gt;[63:0]. PMEVCNTR&lt;n&gt;[63:32] cannot be accessed directly in AArch32 state.
- PMCR.E and PMCNTENSET[n] enable the operation of the event counter.

All of the following apply for an event counter PMEVCNTR&lt;n&gt; in the second range:

- The counter is accessible from EL2 and EL3.
- If EL2 is disabled in the current Security state, then the event counter is accessible from EL1, and from EL0 if permitted by PMUSERENR.
- If FEAT\_PMUv3p5 is implemented, HDCR.HLP determines whether the counter overflow flag PMOVSSET[n] is set on unsigned overflow of PMEVCNTR&lt;n&gt;[31:0] or PMEVCNTR&lt;n&gt;[63:0]. PMEVCNTR&lt;n&gt;[63:32] cannot be accessed directly in AArch32 state.
- HDCR.HPME and PMCNTENSET[n] enable the operation of the event counter.

Values greater than NUM\_PMU\_COUNTERS are reserved. If FEAT\_HPMN0 is not implemented, then the value 0 is reserved.

If this field is set to a reserved value, then the following CONSTRAINED UNPREDICTABLE behaviors apply:

- The value returned by a direct read of HDCR.HPMN is UNKNOWN.
- The number of event counters in each of the first and second ranges is UNKNOWN. That is, either:
- The PE behaves as if HDCR.HPMN is set to an UNKNOWN nonzero value less than or equal to NUM\_PMU\_COUNTERS .
- All counters are in the second range and none are in the first range.

The reset behavior of this field is:

- On a Warm reset, this field resets to the expression NUM\_PMU\_COUNTERS .

## Otherwise:

Reserved, RES0.

## Accessing HDCR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = HDCR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HDCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

```
if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TDA == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else HDCR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HDCR = R[t];
```

## G8.3.33 HTRFCR, Hyp Trace Filter Control Register

The HTRFCR characteristics are:

## Purpose

Provides EL2 controls for Trace.

## Configuration

If EL2 is not implemented, this register is RES0 from Monitor mode when SCR.NS == 1.

AArch32 System register HTRFCR bits [31:0] are architecturally mapped to AArch64 System register TRFCR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented and FEAT\_TRF is implemented. Otherwise, direct accesses to HTRFCR are UNDEFINED.

## Attributes

HTRFCR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control. Controls which timebase is used for trace timestamps.

| TS   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | The timestamp is controlled by TRFCR.TS.                                                          |
| 0b01 | Virtual timestamp. The traced timestamp is the physical counter value minus the value of CNTVOFF. |
| 0b11 | Physical timestamp. The traced timestamp is the physical counter value.                           |

When SelfHostedTraceEnabled() == FALSE, this field is ignored.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [4]

Reserved, RES0.

## CX, bit [3]

VMIDTrace Enable.

| CX   | Meaning                     |
|------|-----------------------------|
| 0b0  | VMIDtracing is not allowed. |
| 0b1  | VMIDtracing is allowed.     |

When SelfHostedTraceEnabled() == FALSE, this field is ignored.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [2]

Reserved, RES0.

## E2TRE, bit [1]

EL2 Trace Enable.

| E2TRE   | Meaning                       |
|---------|-------------------------------|
| 0b0     | Tracing is prohibited at EL2. |
| 0b1     | Tracing is allowed at EL2.    |

When SelfHostedTraceEnabled() == FALSE, this field is ignored.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## E0HTRE, bit [0]

EL0 Trace Enable.

| E0HTRE   | Meaning                                         |
|----------|-------------------------------------------------|
| 0b0      | Tracing is prohibited at EL0 when HCR.TGE == 1. |
| 0b1      | Tracing is allowed at EL0 when HCR.TGE == 1.    |

This field is ignored if any of the following are true:

- The PE is in Secure state.

- SelfHostedTraceEnabled() == FALSE.
- HCR.TGE == 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HTRFCR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0010 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL2) && IsFeatureImplemented(FEAT_TRF)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TTRF == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = HTRFCR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HTRFCR;
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0010 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL2) && IsFeatureImplemented(FEAT_TRF)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TTRF == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else HTRFCR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HTRFCR = R[t];
```

## G8.3.34 PMMIR, Performance Monitors Machine Identification Register

The PMMIR characteristics are:

## Purpose

Describes Performance Monitors parameters specific to the implementation to software.

## Configuration

AArch32 System register PMMIR bits [31:0] are architecturally mapped to AArch64 System register PMMIR\_EL1[31:0].

When FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p4 is implemented, AArch32 System register PMMIRbits [31:0] are architecturally mapped to External register PMMIR[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_PMUv3p4 is implemented. Otherwise, direct accesses to PMMIR are UNDEFINED.

## Attributes

PMMIRis a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 28 27   | 24 23   | 20 19     | 16 15     | 8 7   |
|------|---------|---------|-----------|-----------|-------|
| RES0 | EDGE    | THWIDTH | BUS_WIDTH | BUS_SLOTS | SLOTS |

## Bits [31:28]

Reserved, RES0.

## EDGE, bits [27:24]

PMUevent edge detection. With PMMIR.THWIDTH, indicates implementation of event counter thresholding features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EDGE   | Meaning                             |
|--------|-------------------------------------|
| 0b0000 | FEAT_PMUv3_EDGE is not implemented. |
| 0b0001 | FEAT_PMUv3_EDGE is implemented.     |

All other values are reserved.

If FEAT\_PMUv3\_TH is not implemented, the only permitted value is 0b0000 .

FEAT\_PMUv3\_EDGE implements the functionality identified by the value 0b0001 .

Note

PMEVTYPER&lt;n&gt;\_EL0.TE cannot be accessed through PMEVTYPER&lt;n&gt;.

Access to this field is RO.

## THWIDTH, bits [23:20]

PMEVTYPER&lt;n&gt;\_EL0.TH width. Indicates implementation of the FEAT\_PMUv3\_TH feature, and, if implemented, the size of the PMEVTYPER&lt;n&gt;\_EL0.TH field.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| THWIDTH   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0000    | FEAT_PMUv3_TH is not implemented.             |
| 0b0001    | 1 bit. PMEVTYPER<n>_EL0.TH[11:1] are RES0.    |
| 0b0010    | 2 bits. PMEVTYPER<n>_EL0.TH[11:2] are RES0.   |
| 0b0011    | 3 bits. PMEVTYPER<n>_EL0.TH[11:3] are RES0.   |
| 0b0100    | 4 bits. PMEVTYPER<n>_EL0.TH[11:4] are RES0.   |
| 0b0101    | 5 bits. PMEVTYPER<n>_EL0.TH[11:5] are RES0.   |
| 0b0110    | 6 bits. PMEVTYPER<n>_EL0.TH[11:6] are RES0.   |
| 0b0111    | 7 bits. PMEVTYPER<n>_EL0.TH[11:7] are RES0.   |
| 0b1000    | 8 bits. PMEVTYPER<n>_EL0.TH[11:8] are RES0.   |
| 0b1001    | 9 bits. PMEVTYPER<n>_EL0.TH[11:9] are RES0.   |
| 0b1010    | 10 bits. PMEVTYPER<n>_EL0.TH[11:10] are RES0. |
| 0b1011    | 11 bits. PMEVTYPER<n>_EL0.TH[11] is RES0.     |
| 0b1100    | 12 bits.                                      |

All other values are reserved.

If FEAT\_PMUv3\_TH is not implemented, this field is zero.

Otherwise, the largest value that can be written to PMEVTYPER&lt;n&gt;\_EL0.TH is 2 (PMMIR.THWIDTH) minus one.

Note

PMEVTYPER&lt;n&gt;\_EL0.TH cannot be accessed through PMEVTYPER&lt;n&gt;.

Access to this field is RO.

## BUS\_WIDTH, bits [19:16]

Bus width. Indicates the number of bytes each BUS\_ACCESS event relates to. Encoded as Log2(number of bytes), plus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BUS_WIDTH   | Meaning                           |
|-------------|-----------------------------------|
| 0b0000      | The information is not available. |
| 0b0011      | Four bytes.                       |
| 0b0100      | 8 bytes.                          |
| 0b0101      | 16 bytes.                         |
| 0b0110      | 32 bytes.                         |

All other values are reserved.

Each transfer is up to this number of bytes. An access might be smaller than the bus width.

When this field is nonzero, each access counted by BUS\_ACCESS is at most BUS\_WIDTH bytes. An implementation might treat a wide bus as multiple narrower buses, such that a wide access on the bus increments the BUS\_ACCESS counter by more than one.

Access to this field is RO.

## BUS\_SLOTS, bits [15:8]

Bus count. The largest value by which the BUS\_ACCESS event might increment in a single BUS\_CYCLES cycle.

This field has an IMPLEMENTATION DEFINED value.

When this field is nonzero, the largest value by which the BUS\_ACCESS event might increment in a single BUS\_CYCLES cycle is BUS\_SLOTS.

If the bus count information is not available, this field will read as zero.

Access to this field is RO.

## SLOTS, bits [7:0]

Operation width. The largest value by which the STALL\_SLOT event might increment by in a single cycle. If the STALL\_SLOT event is not implemented, this field might read as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMMIR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1001 | 0b1110 | 0b110  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_PMUv3p4)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then
```

| BUS_WIDTH   | Meaning     |
|-------------|-------------|
| 0b0111      | 64 bytes.   |
| 0b1000      | 128 bytes.  |
| 0b1001      | 256 bytes.  |
| 0b1010      | 512 bytes.  |
| 0b1011      | 1024 bytes. |
| 0b1100      | 2048 bytes. |

```
UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T9 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T9 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TPM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TPM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMMIR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TPM == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TPM == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = PMMIR; elsif PSTATE.EL == EL3 then R[t] = PMMIR;
```

## G8.3.35 SDCR, Secure Debug Control Register

The SDCR characteristics are:

## Purpose

Provides EL3 configuration options for self-hosted debug, trace, and the Performance Monitors Extension.

## Configuration

This register is present only when FEAT\_AA32EL3 is implemented. Otherwise, direct accesses to SDCR are UNDEFINED.

## Attributes

SDCR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:29]

Reserved, RES0.

MTPME,bit [28]

## When FEAT\_MTPMU is implemented:

Multi-threaded PMU Enable. Enables use of the PMEVTYPER&lt;n&gt;.MT bits.

| MTPME   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | FEAT_MTPMU is disabled. The Effective value of PMEVTYPER<n>.MT is 0. |
| 0b1     | PMEVTYPER<n>.MT bits not affected by this field.                     |

If FEAT\_MTPMU is disabled for any other PE in the system that has the same level 1 Affinity as the PE, it is IMPLEMENTATION DEFINED whether the PE behaves as if this field is 0.

The reset behavior of this field is:

- On a Cold reset:
- When the highest implemented Exception level is EL3, this field resets to '1' .

## Otherwise:

Reserved, RES0.

TDCC, bit [27]

## When FEAT\_FGT is implemented:

Trap DCC. Traps use of the Debug Comms Channel in modes other than Monitor mode to Monitor mode.

| TDCC   | Meaning                                                                                                                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any register accesses to be trapped.                                                                                                                                                                                  |
| 0b1    | Accesses to the DCCregisters in modes other than Monitor mode generate a Monitor Trap exception, unless the access also generates a higher priority exception. Traps on the DCCdata transfer registers are ignored when the PE is in Debug state. |

The DCC registers trapped by this control are:

- DBGDTRRXext, DBGDTRTXext, DBGDSCRint, DBGDCCINT, and, when the PE is in Non-debug state, DBGDTRRXint and DBGDTRTXint.

When the PE is in Debug state, SDCR.TDCC does not trap any accesses to:

- DBGDTRRXint and DBGDTRTXint.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [26:24]

Reserved, RES0.

## SCCD, bit [23]

## When FEAT\_PMUv3p5 is implemented:

Secure Cycle Counter Disable. Prohibits PMCCNTR from counting in Secure state and EL3.

| SCCD   | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0    | Cycle counting by PMCCNTRis not affected by this mechanism.     |
| 0b1    | Cycle counting by PMCCNTRis prohibited in Secure state and EL3. |

This field does not affect the CPU\_CYCLES event or any other event that counts cycles.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [22]

Reserved, RES0.

## EPMAD, bit [21]

## When FEAT\_Debugv8p4 is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Non-secure access disable. Controls Non-secure access to Performance Monitors registers by an external debugger.

| EPMAD   | Meaning                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------|
| 0b0     | No accesses from an external debugger to the Performance Monitor registers are prohibited by this control.  |
| 0b1     | Non-secure accesses from an external debugger to the affected Performance Monitor registers are prohibited. |

Otherwise, if EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## When FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors access disable. Controls access to Performance Monitors registers by an external debugger.

| EPMAD   | Meaning                                                                                                                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | No accesses from an external debugger to the Performance Monitor registers are prohibited by this control.                                                                                                                |
| 0b1     | If the IMPLEMENTATION DEFINED authentication interface function ExternalSecureInvasiveDebugEnabled() returns FALSE, then accesses from an external debugger to the affected Performance Monitor registers are prohibited. |

Otherwise, if EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EDAD, bit [20]

## When FEAT\_Debugv8p4 is implemented:

External debug Non-secure access disable. Controls Non-secure access to breakpoint, watchpoint, and OSLAR\_EL1 registers by an external debugger.

| EDAD   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the debug registers are prohibited by this control.  |
| 0b1    | Non-secure accesses from an external debugger to the affected debug registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## When FEAT\_Debugv8p2 is implemented:

External debug access disable. Controls access to breakpoint, watchpoint, and OSLAR\_EL1 registers by an external debugger.

| EDAD   | Meaning                                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the debug registers are prohibited by this control.                                                                                                                |
| 0b1    | If the IMPLEMENTATION DEFINED authentication interface function ExternalSecureInvasiveDebugEnabled() returns FALSE, then accesses from an external debugger to the affected debug registers are prohibited. |

If EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Otherwise:

External debug access disable. Controls access to breakpoint, watchpoint, and optionally OSLAR\_EL1 registers by an external debugger.

| EDAD   | Meaning                                                                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No accesses from an external debugger to the debug registers are prohibited by this control.                                                                                                                |
| 0b1    | If the IMPLEMENTATION DEFINED authentication interface function ExternalSecureInvasiveDebugEnabled() returns FALSE, then accesses from an external debugger to the affected debug registers are prohibited. |

It is IMPLEMENTATION DEFINED whether accesses to OSLAR\_EL1 from an external debugger are affected by this control.

If EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

TTRF, bit [19]

## When FEAT\_TRF is implemented:

Trap Trace Filter controls. Controls whether accesses in modes other than Monitor mode to the trace filter control registers generate a Monitor Trap exception.

| TTRF   | Meaning                                                                                                                                            |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses to HTRFCR and TRFCR are not affected by this control bit.                                                                                 |
| 0b1    | When not in Monitor mode, accesses to HTRFCR and TRFCR generate a Monitor Trap exception, unless the access generates a higher priority exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## STE, bit [18]

## When FEAT\_TRF is implemented:

Secure Trace Enable. This field enables tracing in Secure state and controls the level of authentication required by an external debugger to enable external tracing.

| STE   | Meaning                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0b0   | Trace is prohibited in Secure state unless overridden by the IMPLEMENTATION DEFINED authentication interface. |
| 0b1   | Trace in Secure state is not affected by this field.                                                          |

This field also controls the level of authentication required by an external debugger to enable external tracing. See 'Register controls to enable self-hosted trace'.

If EL3 is not implemented and the Effective value of SCR.NS is 0, the PE behaves as if this field is set to 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## SPME, bit [17]

## When FEAT\_PMUv3 is implemented and FEAT\_Debugv8p2 is implemented:

Secure Performance Monitors Enable. Controls event counting in Secure state.

| SPME   | Meaning                                                                                                                                                 |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Event counting is prohibited in Secure state. If PMCR.DP is 1, PMCCNTRis disabled in Secure state. Otherwise, PMCCNTRis not affected by this mechanism. |
| 0b1    | Event counting and PMCCNTRare not affected by this mechanism.                                                                                           |

This field affects the operation of all event counters in Secure state, and if PMCR.DP is 1, the operation of PMCCNTRin Secure state. When PMCR.DP is 0, PMCCNTR is not affected by this field.

If EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## When FEAT\_PMUv3 is implemented:

Secure Performance Monitors Enable. Controls event counting in Secure state.

| SPME   | Meaning                                                                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If ExternalSecureNoninvasiveDebugEnabled() is FALSE, event counting is prohibited in Secure state, and if PMCR.DP is 1, PMCCNTRis disabled in Secure state. |
| 0b1    | Event counting and PMCCNTRare not affected by this mechanism.                                                                                               |

If ExternalSecureNoninvasiveDebugEnabled() is TRUE, the event counters and PMCCNTR are not affected by this field.

Otherwise, this field affects the operation of all event counters in Secure state, and if PMCR.DP is 1, the operation of PMCCNTR in Secure state. When PMCR.DP is 0, PMCCNTR is not affected by this field.

If EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [16]

Reserved, RES0.

## SPD, bits [15:14]

AArch32 Secure self-hosted Privileged Debug. Enables or disables debug exceptions from EL3, other than Breakpoint Instruction exceptions.

| SPD   | Meaning                                                                             |
|-------|-------------------------------------------------------------------------------------|
| 0b00  | Legacy mode. Debug exceptions from EL3 are enabled by the authentication interface. |
| 0b10  | Secure privileged debug disabled. Debug exceptions from EL3 are disabled.           |

| SPD   | Meaning                                                                 |
|-------|-------------------------------------------------------------------------|
| 0b11  | Secure privileged debug enabled. Debug exceptions from EL3 are enabled. |

Other values are reserved, and have the CONSTRAINED UNPREDICTABLE behavior that they must have the same behavior as 0b00 . Software must not rely on this property as the behavior of reserved values might change in a future revision of the architecture.

This field has no effect on Breakpoint Instruction exceptions. These are always enabled.

This field is ignored in Non-secure state.

If debug exceptions from EL3 are enabled, then debug exceptions from Secure EL0 are also enabled.

Otherwise, debug exceptions from Secure EL0 are enabled only if the value of SDER.SUIDEN is 1.

If EL3 is not implemented and the Effective value of SCR.NS is 0, then the Effective value of this field is 0b11 .

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '00' .

## Bits [13:0]

Reserved, RES0.

## Accessing SDCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0011 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL3) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then R[t] = SDCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0011 | 0b001  |

if !IsFeatureImplemented(FEAT\_AA32EL3) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HSTR\_EL2.T1 == '1'

↪ → then

AArch64.AArch32SystemAccessTrap(EL2, 0x03);

elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HSTR.T1 == '1'

↪ → then

AArch32.TakeHypTrapException(0x03);

elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp;

↪ → IsCurrentSecurityState(SS\_Secure) then

AArch64.AArch32SystemAccessTrap(EL2, 0x03);

elsif IsFeatureImplemented(FEAT\_AA64EL3) &amp;&amp; !ELUsingAArch32(EL3) &amp;&amp;

↪ → IsCurrentSecurityState(SS\_Secure) then

AArch64.AArch32SystemAccessTrap(EL3, 0x03);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

if CP15SDISABLE2 == HIGH then

UNDEFINED;

else

SDCR = R[t];

## G8.3.36 SDER, Secure Debug Enable Register

The SDER characteristics are:

## Purpose

Controls invasive and non-invasive debug in the Secure EL0 mode.

## Configuration

When EL2 is implemented and FEAT\_SEL2 is implemented, AArch32 System register SDER bits [31:0] are architecturally mapped to AArch64 System register SDER32\_EL2[31:0].

When EL3 is implemented, AArch32 System register SDER bits [31:0] are architecturally mapped to AArch64 System register SDER32\_EL3[31:0].

This register is present only when (HaveEL(EL3) &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL3)) || (IsFeatureImplemented(FEAT\_AA32EL1) &amp;&amp; HaveELUsingSecurityState(EL1, TRUE)). Otherwise, direct accesses to SDER are UNDEFINED.

## Attributes

SDER is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## SUNIDEN, bit [1]

Secure User Non-Invasive Debug Enable.

| SUNIDEN   | Meaning                                                    |
|-----------|------------------------------------------------------------|
| 0b0       | This bit has no effect on non-invasive debug.              |
| 0b1       | Non-invasive debug is allowed in Secure EL0 using AArch32. |

When EL3 or Secure EL1 is using AArch32, the forms of non-invasive debug affected by this control are:

- The PC Sample-based Profiling Extension. See About the PC Sample-based Profiling Extension.
- When SelfHostedTraceEnabled() == FALSE, processor trace.
- When EL3 is implemented, Performance Monitors.

When Secure EL1 is using AArch64, this bit has no effect.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## SUIDEN, bit [0]

## When EL3 is implemented:

Secure User Invasive Debug Enable.

| SUIDEN   | Meaning                                                                       |
|----------|-------------------------------------------------------------------------------|
| 0b0      | This bit does not affect the generation of debug exceptions at Secure EL0.    |
| 0b1      | If EL3 or EL1 is using AArch32, debug exceptions from Secure EL0 are enabled. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Accessing SDER

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0001 | 0b001  |

```
if !((HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3)) || (IsFeatureImplemented(FEAT_AA32EL1) && ↪ → HaveELUsingSecurityState(EL1, TRUE))) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = SDER; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then R[t] = SDER;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0001 | 0b001  |

```
if !((HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3)) || (IsFeatureImplemented(FEAT_AA32EL1) && ↪ → HaveELUsingSecurityState(EL1, TRUE))) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif !IsCurrentSecurityState(SS_Secure) then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → MDCR_EL2.<TDE,TDA> != '00' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TDA == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else SDER = R[t]; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CP15SDISABLE2 == HIGH then UNDEFINED; else SDER = R[t];
```

## G8.3.37 TRFCR, Trace Filter Control Register

The TRFCR characteristics are:

## Purpose

Provides EL1 controls for Trace.

## Configuration

AArch32 System register TRFCR bits [31:0] are architecturally mapped to AArch64 System register TRFCR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_TRF is implemented. Otherwise, direct accesses to TRFCR are UNDEFINED.

## Attributes

TRFCR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:7]

Reserved, RES0.

## TS, bits [6:5]

Timestamp Control. Controls which timebase is used for trace timestamps.

| TS   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Applies when            |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 0b01 | Virtual timestamp. The traced timestamp is the physical counter value minus the value of CNTVOFF.                                                                                                                                                                                                                                                                                                                                                          |                         |
| 0b10 | Guest physical timestamp. The traced timestamp is the physical counter value minus a physical offset. If any of the following are true, the physical offset is zero, otherwise the physical offset is the value of CNTPOFF_EL2: • EL3 is implemented and is using AArch32. • EL3 is implemented, using AArch64, and SCR_EL3.ECVEn == 0b0 . • EL2 is using AArch32. • EL2 is using AArch64 and CNTHCTL_EL2.ECV == 0b0 . • FEAT_ECV_POFF is not implemented. | FEAT_ECV is implemented |
| 0b11 | Physical timestamp. The traced timestamp is the physical counter value.                                                                                                                                                                                                                                                                                                                                                                                    |                         |

All other values are reserved.

This field is ignored by the PE when any of the following are true:

- EL2 is implemented and HTRFCR.TS != 0b00 .
- SelfHostedTraceEnabled() == FALSE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [4:2]

Reserved, RES0.

## E1TRE, bit [1]

EL1 Trace Enable.

| E1TRE   | Meaning                             |
|---------|-------------------------------------|
| 0b0     | Tracing is prohibited in PL1 modes. |
| 0b1     | Tracing is allowed in PL1 modes.    |

This field is ignored if SelfHostedTraceEnabled () == FALSE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## E0TRE, bit [0]

EL0 Trace Enable.

This field is ignored if any of the following are true:

- SelfHostedTraceEnabled () == FALSE.
- EL2 is implemented and enabled in the current security state and HCR.TGE == 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRFCR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0010 | 0b001  |

| E0TRE   | Meaning                       |
|---------|-------------------------------|
| 0b0     | Tracing is prohibited at EL0. |
| 0b1     | Tracing is allowed at EL0.    |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_TRF)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && PSTATE.M != M32_Monitor && SDCR.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TTRF == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TTRF == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SDCR.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = TRFCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TTRF == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else R[t] = TRFCR; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TTRF == '1' then AArch32.TakeMonitorTrapException(); else R[t] = TRFCR;
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0010 | 0b001  |

```
if !(IsFeatureImplemented(FEAT_AA32EL1) && IsFeatureImplemented(FEAT_TRF)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && PSTATE.M != M32_Monitor && SDCR.TTRF == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && MDCR_EL2.TTRF == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HDCR.TTRF == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && PSTATE.M != ↪ → M32_Monitor && SDCR.TTRF == '1' then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException(); else TRFCR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA32EL3) && ↪ → ELUsingAArch32(EL3) && SDCR.TTRF == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && MDCR_EL3.TTRF == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SDCR.TTRF == '1' ↪ → then if EL3SDDUndef() then UNDEFINED; else AArch32.TakeMonitorTrapException();
```

```
else TRFCR = R[t]; elsif PSTATE.EL == EL3 then if PSTATE.M != M32_Monitor && SDCR.TTRF == '1' then AArch32.TakeMonitorTrapException(); else TRFCR = R[t];
```