## H9.2 External debug registers

This section describes the debug registers that are accessible through the external debug interface and are used for external debug.

## H9.2.1 DBGAUTHSTATUS\_EL1, Debug Authentication Status Register

The DBGAUTHSTATUS\_EL1 characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for debug.

## Configuration

When FEAT\_DoPD is implemented, DBGAUTHSTATUS\_EL1 is in the Core power domain. Otherwise, DBGAUTHSTATUS\_EL1 is in the Debug power domain

External register DBGAUTHSTATUS\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGAUTHSTATUS\_EL1[31:0].

External register DBGAUTHSTATUS\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGAUTHSTATUS[31:0].

## Attributes

DBGAUTHSTATUS\_EL1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 28 27 26 25 24 23   | 28 27 26 25 24 23   | 28 27 26 25 24 23   | 16 15 14 13 12 11   | 16 15 14 13 12 11   | 16 15 14 13 12 11   | 8 7 6 5 4 3   | 2     | 1 0   |
|------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------|-------|-------|
| RES0 | RTNID               | RTID                | RES0                | RLNID               | RLID                | RES0                | SNID          | NSNID | NSID  |

## Bits [31:28]

Reserved, RES0.

## RTNID, bits [27:26]

Root non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RTID.

## RTID, bits [25:24]

Root invasive debug.

All other values are reserved.

If FEAT\_RME is not implemented, the only permitted value is 0b00 .

## Bits [23:16]

Reserved, RES0.

| RTID   | Meaning                                                                |
|--------|------------------------------------------------------------------------|
| 0b00   | Not implemented.                                                       |
| 0b10   | Implemented and disabled. ExternalRootInvasiveDebugEnabled() == FALSE. |
| 0b11   | Implemented and enabled. ExternalRootInvasiveDebugEnabled() == TRUE.   |

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

SNID, bits [7:6]

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

SID, bits [5:4]

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

| NSNID   | Meaning                                                             |
|---------|---------------------------------------------------------------------|
| 0b00    | Non-secure state is not implemented.                                |
| 0b11    | Implemented and enabled. ExternalNoninvasiveDebugEnabled() == TRUE. |

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

DBGAUTHSTATUS\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance          |
|-------------|----------|-------------------|
| Debug       | 0xFB8    | DBGAUTHSTATUS_EL1 |

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.2 DBGBCR&lt;n&gt;\_EL1, Debug Breakpoint Control Registers, n = 0 - 63

The DBGBCR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds control information for a breakpoint. Forms breakpoint n together with value register DBGBVR&lt;n&gt;\_EL1.

## Configuration

DBGBCR&lt;n&gt;\_EL1 is in the Core power domain

If breakpoint n is not implemented, then accesses to this register are:

- RES0 when IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalDebugAccess().
- ACONSTRAINED UNPREDICTABLE choice of RES0 or ERROR otherwise.

External register DBGBCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGBCR&lt;n&gt;\_EL1[31:0].

When FEAT\_Debugv8p9 is implemented, External register DBGBCR&lt;n&gt;\_EL1 bits [63:32] are architecturally mapped to AArch64 System register DBGBCR&lt;n&gt;\_EL1[63:32].

External register DBGBCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGBCR&lt;n&gt;[31:0].

## Attributes

DBGBCR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

When the E field is zero, all the other fields in the register are ignored.

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

## SSCE, bit [29]

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

All other values are reserved.

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

BT, bits [23:20]

Breakpoint Type.

With DBGBCR&lt;n&gt;\_EL1.BT2 when implemented, specifies breakpoint type.

| BT     | Meaning                                                                                                                                                                                                                                                                                                      | Applies when                                                                         |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| 0b0000 | Unlinked instruction address match. DBGBVR<n>_EL1 is the address of an instruction.                                                                                                                                                                                                                          |                                                                                      |
| 0b0001 | Linked instruction address match. As 0b0000 , but linked to a breakpoint that has linking enabled.                                                                                                                                                                                                           |                                                                                      |
| 0b0010 | Unlinked Context ID match. If the Effective value of HCR_EL2.E2H is 1 and either the PE is executing at EL0 with HCR_EL2.TGE set to 1 or the PE is executing at EL2, then DBGBVR<n>_EL1.ContextID is compared against CONTEXTIDR_EL2. Otherwise, DBGBVR<n>_EL1.ContextID is compared against CONTEXTIDR_EL1. | breakpoint n is context-aware                                                        |
| 0b0011 | As 0b0010 , with linking enabled.                                                                                                                                                                                                                                                                            | breakpoint n is context-aware                                                        |
| 0b0100 | Unlinked instruction address mismatch. DBGBVR<n>_EL1 is the address of an instruction.                                                                                                                                                                                                                       | FEAT_BWE is implemented or EL1 is using AArch32                                      |
| 0b0101 | Linked instruction address mismatch. As 0b0100 , but linked to a breakpoint that has linking enabled.                                                                                                                                                                                                        | FEAT_BWE is implemented or EL1 is using AArch32                                      |
| 0b0110 | Unlinked CONTEXTIDR_EL1 match. DBGBVR<n>_EL1.ContextID is a Context ID compared against CONTEXTIDR_EL1.                                                                                                                                                                                                      | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b0111 | As 0b0110 , with linking enabled.                                                                                                                                                                                                                                                                            | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1000 | Unlinked VMIDmatch. DBGBVR<n>_EL1.VMID isaVMID compared against VTTBR_EL2.VMID.                                                                                                                                                                                                                              | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1001 | As 0b1000 , with linking enabled.                                                                                                                                                                                                                                                                            | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1010 | Unlinked VMIDand Context ID match. DBGBVR<n>_EL1.ContextID is a Context ID compared against CONTEXTIDR_EL1, and DBGBVR<n>_EL1.VMID isaVMID compared against VTTBR_EL2.VMID.                                                                                                                                  | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1011 | As 0b1010 , with linking enabled.                                                                                                                                                                                                                                                                            | EL2 is implemented and breakpoint n is context-aware                                 |
| 0b1100 | Unlinked CONTEXTIDR_EL2 match. DBGBVR<n>_EL1.ContextID2 is a Context ID compared against CONTEXTIDR_EL2.                                                                                                                                                                                                     | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1101 | As 0b1100 , with linking enabled.                                                                                                                                                                                                                                                                            | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |
| 0b1110 | Unlinked Full Context ID match. DBGBVR<n>_EL1.ContextID is compared against CONTEXTIDR_EL1, and DBGBVR<n>_EL1.ContextID2 is compared against CONTEXTIDR_EL2.                                                                                                                                                 | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |

| BT     | Meaning                           | Applies when                                                                         |
|--------|-----------------------------------|--------------------------------------------------------------------------------------|
| 0b1111 | As 0b1110 , with linking enabled. | EL2 is implemented, FEAT_Debugv8p1 is implemented, and breakpoint n is context-aware |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## LBN, bits [19:16]

Linked Breakpoint Number.

For Linked address matching breakpoints, with DBGBCR&lt;n&gt;\_EL1.LBNX when implemented, specifies the index of the breakpoint linked to.

For all other breakpoint types, this field is ignored and reads of the register return an UNKNOWN value.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## SSC, bits [15:14]

Security state control. Determines the Security states under which a Breakpoint debug event for breakpoint n is generated. This field must be interpreted along with the HMC and PMC fields, and there are constraints on the permitted values of the {HMC, SSC, PMC} fields. For more information, including the effect of programming the fields to a reserved set of values, see 'Reserved DBGBCR&lt;n&gt;\_EL1.{SSC, HMC, PMC} values'.

For more information on the operation of the SSC, HMC, and PMC fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## HMC,bit [13]

Higher mode control. Determines the debug perspective for deciding when a Breakpoint debug event for breakpoint n is generated. This field must be interpreted along with the SSC and PMC fields, and there are constraints on the permitted values of the {HMC, SSC, PMC} fields. For more information see DBGBCR&lt;n&gt;\_EL1.SSC description.

For more information on the operation of the SSC, HMC, and PMC fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [12:9]

Reserved, RES0.

## BAS, bits [8:5]

## When FEAT\_AA32 is implemented:

Byte address select. Defines which half-words an address-matching breakpoint matches, regardless of the instruction set and Execution state.

The permitted values depend on the breakpoint type.

For Address match breakpoints in either AArch32 or AArch64 state, the permitted values are:

| BAS    | Match instruction at   | Constraint for debuggers          |
|--------|------------------------|-----------------------------------|
| 0b0011 | DBGBVR<n>_EL1          | Use for T32 instructions.         |
| 0b1100 | DBGBVR<n>_EL1 + 2      | Use for T32 instructions.         |
| 0b1111 | DBGBVR<n>_EL1          | Use for A64 and A32 instructions. |

All other values are reserved.

For more information, see 'Using the BAS field in Address Match breakpoints'.

For Address mismatch breakpoints in an AArch32 stage 1 translation regime, the permitted values are:

| BAS    | Match instruction at   | Constraint for debuggers                   |
|--------|------------------------|--------------------------------------------|
| 0b0000 | •                      | Use for a match anywhere breakpoint.       |
| 0b0011 | DBGBVR<n>_EL1          | Use for stepping T32 instructions.         |
| 0b1100 | DBGBVR<n>_EL1 + 2      | Use for stepping T32 instructions.         |
| 0b1111 | DBGBVR<n>_EL1          | Use for stepping A64 and A32 instructions. |

All other values are reserved.

For more information, see 'Using the BAS field in Address Match breakpoints'.

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

Privilege mode control. Determines the Exception level or levels at which a Breakpoint debug event for breakpoint n is generated. This field must be interpreted along with the SSC and HMC fields, and there are constraints on the permitted values of the {HMC, SSC, PMC} fields. For more information see the DBGBCR&lt;n&gt;\_EL1.SSC description.

For more information on the operation of the SSC, HMC, and PMC fields, see 'Execution conditions for which a breakpoint generates Breakpoint exceptions'.

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

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalDebugAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

When FEAT\_Debugv8p9 is not implemented, this register is 32-bits wide and offset 0x40C + (16 * n) is reserved.

DBGBCR&lt;n&gt;\_EL1 can be accessed through the external debug interface:

| Component   | Offset Instance                |
|-------------|--------------------------------|
| Debug       | 0x408 + (16 * n) DBGBCR<n>_EL1 |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalDebugAccess(addrdesc), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.3 DBGBVR&lt;n&gt;\_EL1, Debug Breakpoint Value Registers, n = 0 - 63

The DBGBVR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds a virtual address, or a VMID and/or a context ID, for use in breakpoint matching. Forms breakpoint n together with control register DBGBCR&lt;n&gt;\_EL1.

## Configuration

DBGBVR&lt;n&gt;\_EL1 is in the Core power domain

How this register is interpreted depends on the value of DBGBCR&lt;n&gt;\_EL1.BT.

- When DBGBCR&lt;n&gt;\_EL1.BT is 0b0x0x , this register holds a virtual address.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b001x , 0b011x , or 0b110x , this register holds a Context ID.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b100x , this register holds a VMID.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b101x , this register holds a VMID and a Context ID.
- When DBGBCR&lt;n&gt;\_EL1.BT is 0b111x , this register holds two Context ID values.

For other values of DBGBCR&lt;n&gt;\_EL1.BT, this register is RES0.

If breakpoint n is not implemented, then accesses to this register are:

- RES0 when IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalDebugAccess().
- ACONSTRAINED UNPREDICTABLE choice of RES0 or ERROR otherwise.

External register DBGBVR&lt;n&gt;\_EL1 bits [63:0] are architecturally mapped to AArch64 System register DBGBVR&lt;n&gt;\_EL1[63:0].

External register DBGBVR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGBVR&lt;n&gt;[31:0].

External register DBGBVR&lt;n&gt;\_EL1 bits [63:32] are architecturally mapped to AArch32 System register DBGBXVR&lt;n&gt;[31:0].

## Attributes

DBGBVR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

When DBGBCR&lt;n&gt;\_EL1.BT IN {' 0x0 x'}:

<!-- image -->

## RESS[14:8], bits [63:57]

Reserved, Sign extended. Software must treat this field as RES0 if the most significant bit of V A is 0 or RES0, and as RES1 if the most significant bit of V A is 1.

Hardware always ignores the value of these bits and it is IMPLEMENTATION DEFINED whether:

- The bits are hardwired to a copy of the most significant bit of V A, meaning writes to these bits are ignored, and reads to the bits always return the hardwired value.
- The value in those bits can be written, and reads will return the last value written. The value held in those bits is ignored by hardware.

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

If the address is being matched in an AArch64 stage 1 translation regime:

- This field contains bits[48:2] of the address for comparison.
- When FEAT\_LVA3 is implemented, (VA[56:53]:VA[52:49]) forms the upper part of the address value. If FEAT\_LVA3 is not implemented, bits VA[56:53] are part of the RESS field.
- When FEAT\_LVA is implemented, VA[52:49] forms the upper part of the address value. If FEAT\_LVA is not implemented, bits [52:49] are part of the RESS field.

If the address is being matched in an AArch32 stage 1 translation regime, the first 20 bits of this field are RES0, and the rest of the field contains bits[31:2] of the address for comparison.

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

Otherwise, the value is compared against the following:

- CONTEXTIDR when the PE is executing at AArch32.
- CONTEXTIDR\_EL1 when the PE is executing at AArch64.

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

Bits [63:48]

Reserved, RES0.

VMID[15:8], bits [47:40]

## When FEAT\_VMID16 is implemented and VTCR\_EL2.VS == '1':

Extension to VMID[7:0]. For more information, see DBGBVR&lt;n&gt;\_EL1.VMID[7:0].

If EL2 is using AArch32, this field is RES0.

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

When DBGBCR&lt;n&gt;\_EL1.BT IN {'101x'} and EL2 is implemented:

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## VMID[15:8], bits [47:40]

## When FEAT\_VMID16 is implemented and VTCR\_EL2.VS == '1':

Extension to VMID[7:0]. For more information, see DBGBVR&lt;n&gt;\_EL1.VMID[7:0].

If EL2 is using AArch32, or if the implementation has an 8-bit VMID, this field is RES0.

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

When DBGBCR&lt;n&gt;\_EL1.BT IN {'110x'}, EL2 is implemented, and FEAT\_Debugv8p1 is implemented:

ContextID2

63

32

RES0

31

0

<!-- image -->

## ContextID2, bits [63:32]

Context ID value for comparison against CONTEXTIDR\_EL2.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [31:0]

Reserved, RES0.

When DBGBCR&lt;n&gt;\_EL1.BT IN {'111x'}, EL2 is implemented, and FEAT\_Debugv8p1 is implemented:

<!-- image -->

## ContextID2, bits [63:32]

Context ID value for comparison against CONTEXTIDR\_EL2.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## ContextID, bits [31:0]

Context ID value for comparison against CONTEXTIDR\_EL1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGBVR&lt;n&gt;\_EL1

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalDebugAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

DBGBVR&lt;n&gt;\_EL1 can be accessed through the external debug interface:

| Component   | Offset           | Instance      | Range   |
|-------------|------------------|---------------|---------|
| Debug       | 0x400 + (16 * n) | DBGBVR<n>_EL1 | 63:0    |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalDebugAccess(addrdesc), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.4 DBGCLAIMCLR\_EL1, Debug CLAIM Tag Clear Register

The DBGCLAIMCLR\_EL1 characteristics are:

## Purpose

Used by software to read the values of the CLAIM tag bits, and to clear CLAIM tag bits to 0.

The architecture does not define any functionality for the CLAIM tag bits.

Note

CLAIM tags are typically used for communication between the debugger and target software.

Used in conjunction with the DBGCLAIMSET\_EL1 register.

## Configuration

DBGCLAIMCLR\_EL1 is in the Core power domain

An implementation must include eight CLAIM tag bits.

External register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMCLR\_EL1[31:0].

External register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMSET\_EL1[31:0].

External register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMCLR[31:0].

External register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMSET[31:0].

External register DBGCLAIMCLR\_EL1 bits [31:0] are architecturally mapped to External register DBGCLAIMSET\_EL1[31:0].

## Attributes

DBGCLAIMCLR\_EL1 is a 32-bit register.

## Field descriptions

<!-- image -->

Bits [31:8]

Reserved, RAZ/WI.

CLAIM&lt;m&gt;, bits [m], for m = 7 to 0

Claim Tag Clear. Indicates the current status of Claim Tag bit &lt;m&gt;, and is used to clear Claim Tag bit &lt;m&gt; to 0.

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| CLAIM<m>   | Meaning                                                                        |
|------------|--------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not set. On a write: Ignored.                  |
| 0b1        | On a read: Claim Tag bit <m> is set. On a write: Clear Claim tag bit <m> to 0. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is W1C.

## Accessing DBGCLAIMCLR\_EL1

DBGCLAIMCLR\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance        |
|-------------|----------|-----------------|
| Debug       | 0xFA4    | DBGCLAIMCLR_EL1 |

## H9.2.5 DBGCLAIMSET\_EL1, Debug CLAIM Tag Set Register

The DBGCLAIMSET\_EL1 characteristics are:

## Purpose

Used by software to set the CLAIM tag bits to 1.

The architecture does not define any functionality for the CLAIM tag bits.

Note

CLAIM tags are typically used for communication between the debugger and target software.

Used in conjunction with the DBGCLAIMCLR\_EL1 register.

## Configuration

DBGCLAIMSET\_EL1 is in the Core power domain

An implementation must include eight CLAIM tag bits.

External register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMSET\_EL1[31:0].

External register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGCLAIMCLR\_EL1[31:0].

External register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMSET[31:0].

External register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGCLAIMCLR[31:0].

External register DBGCLAIMSET\_EL1 bits [31:0] are architecturally mapped to External register DBGCLAIMCLR\_EL1[31:0].

## Attributes

DBGCLAIMSET\_EL1 is a 32-bit register.

## Field descriptions

<!-- image -->

Bits [31:8]

Reserved, RAZ/WI.

CLAIM&lt;m&gt;, bits [m], for m = 7 to 0

Claim Tag Set. Used to set Claim Tag bit &lt;m&gt; to 1.

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| CLAIM<m>   | Meaning                                 |
|------------|-----------------------------------------|
| 0b0        | On a write: Ignored.                    |
| 0b1        | On a write: Set Claim Tag bit <m> to 1. |

Access to this field is RAO/W1S.

## Accessing DBGCLAIMSET\_EL1

DBGCLAIMSET\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance        |
|-------------|----------|-----------------|
| Debug       | 0xFA0    | DBGCLAIMSET_EL1 |

## H9.2.6 DBGDTRRX\_EL0, Debug Data Transfer Register, Receive

The DBGDTRRX\_EL0 characteristics are:

## Purpose

Transfers data from an external debugger to the PE. For example, it is used by a debugger transferring commands and data to a debug target. See DBGDTR\_EL0 for additional architectural mappings. It is a component of the Debug Communications Channel.

## Configuration

DBGDTRRX\_EL0 is in the Core power domain

External register DBGDTRRX\_EL0 bits [31:0] are architecturally mapped to AArch64 System register DBGDTRRX\_EL0[31:0].

External register DBGDTRRX\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRRXint[31:0].

## Attributes

DBGDTRRX\_EL0 is a 32-bit register.

## Field descriptions

<!-- image -->

## DTRRX, bits [31:0]

Update DTRRX.

Writes to this register:

- If RXfull is 0, update the value in DTRRX and set RXfull to 1.
- If RXfull is 1, the written value is ignored and RXO is set to 1.

Reads of this register return the last value written to DTRRX and do not change RXfull.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRRX\_EL0

If EDSCR.ITE == 0 when the PE exits Debug state on receiving a Restart request trigger event, the behavior of any operation issued by a DTR access in Memory access mode that has not completed execution is CONSTRAINED UNPREDICTABLE, and must do one of the following:

- It must complete execution in Debug state before the PE executes the restart sequence.
- It must complete execution in Non-debug state before the PE executes the restart sequence.
- It must be abandoned. This means that the instruction does not execute. Any registers or memory accessed by the instruction are left in an UNKNOWN state.

DBGDTRRX\_EL0 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| Debug       | 0x080    | DBGDTRRX_EL0 |

## H9.2.7 DBGDTRTX\_EL0, Debug Data Transfer Register, Transmit

The DBGDTRTX\_EL0 characteristics are:

## Purpose

Transfers data from the PE to an external debugger. For example, it is used by a debug target to transfer data to the debugger. See DBGDTR\_EL0 for additional architectural mappings. It is a component of the Debug Communication Channel.

## Configuration

DBGDTRTX\_EL0 is in the Core power domain

External register DBGDTRTX\_EL0 bits [31:0] are architecturally mapped to AArch64 System register DBGDTRTX\_EL0[31:0].

External register DBGDTRTX\_EL0 bits [31:0] are architecturally mapped to AArch32 System register DBGDTRTXint[31:0].

## Attributes

DBGDTRTX\_EL0 is a 32-bit register.

## Field descriptions

<!-- image -->

## DTRTX, bits [31:0]

Return DTRTX.

Reads of this register:

- If TXfull is 1, return the value in DTRTX and clear TXfull to 0.
- If TXfull is 0, return an UNKNOWN value and set TXU to 1.

Writes of this register update the value in DTRTX and do not change TXfull.

For the full behavior of the Debug Communications Channel, see 'The Debug Communication Channel and Instruction Transfer Register'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing DBGDTRTX\_EL0

If EDSCR.ITE == 0 when the PE exits Debug state on receiving a Restart request trigger event, the behavior of any operation issued by a DTR access in Memory access mode that has not completed execution is CONSTRAINED UNPREDICTABLE, and must do one of the following:

- It must complete execution in Debug state before the PE executes the restart sequence.
- It must complete execution in Non-debug state before the PE executes the restart sequence.
- It must be abandoned. This means that the instruction does not execute. Any registers or memory accessed by the instruction are left in an UNKNOWN state.

DBGDTRTX\_EL0 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalDebugAccess(addrdesc), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| Debug       | 0x08C    | DBGDTRTX_EL0 |

## H9.2.8 DBGWCR&lt;n&gt;\_EL1, Debug Watchpoint Control Registers, n = 0 - 63

The DBGWCR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds control information for a watchpoint. Forms watchpoint n together with value register DBGWVR&lt;n&gt;\_EL1.

## Configuration

DBGWCR&lt;n&gt;\_EL1 is in the Core power domain

If watchpoint n is not implemented, then accesses to this register are:

- When IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalDebugAccess(), RES0.
- Otherwise, a CONSTRAINED UNPREDICTABLE choice of RES0 or ERROR.

External register DBGWCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch64 System register DBGWCR&lt;n&gt;\_EL1[31:0].

When FEAT\_Debugv8p9 is implemented, External register DBGWCR&lt;n&gt;\_EL1 bits [63:32] are architecturally mapped to AArch64 System register DBGWCR&lt;n&gt;\_EL1[63:32].

External register DBGWCR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGWCR&lt;n&gt;[31:0].

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

## SSCE, bit [29]

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

Security state control. Determines the Security states under which a Watchpoint debug event for watchpoint n is generated. This field must be interpreted along with the HMC and PAC fields.

For more information on the operation of the SSC, HMC, and PAC fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## HMC,bit [13]

Higher mode control. Determines the debug perspective for deciding when a Watchpoint debug event for watchpoint n is generated. This field must be interpreted along with the SSC and PAC fields.

For more information on the operation of the SSC, HMC, and PAC fields, see 'Execution conditions for which a watchpoint generates Watchpoint exceptions'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## BAS, bits [12:5]

Byte address select. Each bit of this field selects whether a byte from within the word or double-word addressed by DBGWVR&lt;n&gt;\_EL1 is being watched.

| WT   | Meaning                      |
|------|------------------------------|
| 0b0  | Unlinked data address match. |
| 0b1  | Linked data address match.   |

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

If DBGWVR&lt;n&gt;\_EL1[2] == 1, only BAS[3:0] is used. Arm deprecates setting DBGWVR&lt;n&gt;\_EL1[2] == 1.

The valid values for BAS are nonzero binary number all of whose set bits are contiguous. All other values are reserved and must not be used by software. See 'Reserved DBGWCR&lt;n&gt;.BAS values'.

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

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalDebugAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

When FEAT\_Debugv8p9 is not implemented, this register is 32-bits wide and offset 0x80C + (16 * n) is reserved.

DBGWCR&lt;n&gt;\_EL1 can be accessed through the external debug interface:

| Component   | Offset Instance                |
|-------------|--------------------------------|
| Debug       | 0x808 + (16 * n) DBGWCR<n>_EL1 |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalDebugAccess(addrdesc), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.9 DBGWVR&lt;n&gt;\_EL1, Debug Watchpoint Value Registers, n = 0 - 63

The DBGWVR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Holds a data address value for use in watchpoint matching. Forms watchpoint n together with control register DBGWCR&lt;n&gt;\_EL1.

## Configuration

DBGWVR&lt;n&gt;\_EL1 is in the Core power domain

If watchpoint n is not implemented, then accesses to this register are:

- When IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalDebugAccess(), RES0.
- Otherwise, a CONSTRAINED UNPREDICTABLE choice of RES0 or ERROR.

External register DBGWVR&lt;n&gt;\_EL1 bits [63:0] are architecturally mapped to AArch64 System register DBGWVR&lt;n&gt;\_EL1[63:0].

External register DBGWVR&lt;n&gt;\_EL1 bits [31:0] are architecturally mapped to AArch32 System register DBGWVR&lt;n&gt;[31:0].

## Attributes

DBGWVR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## RESS[14:8], bits [63:57]

Reserved, Sign extended. Hardware and software must treat this field as RES0 if the most significant bit of V A is 0 or RES0, and as RES1 if the most significant bit of V A is 1.

Hardware always ignores the value of these bits and it is IMPLEMENTATION DEFINED whether:

- The bits are hardwired to a copy of the most significant bit of V A, meaning writes to these bits are ignored, and reads to the bits always return the hardwired value.
- The value in those bits can be written, and reads will return the last value written. The value held in those bits is ignored by hardware.

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

VA[52:49], bits [52:49]

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

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalDebugAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

DBGWVR&lt;n&gt;\_EL1 can be accessed through the external debug interface:

| Component   | Offset           | Instance      | Range   |
|-------------|------------------|---------------|---------|
| Debug       | 0x800 + (16 * n) | DBGWVR<n>_EL1 | 63:0    |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalDebugAccess(addrdesc), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.10 EDAA32PFR, External Debug Auxiliary Processor Feature Register

The EDAA32PFR characteristics are:

## Purpose

Provides information about implemented PE features.

Note

The register mnemonic, EDAA32PFR, is derived from previous definitions of this register that defined this register only when AArch64 was not supported.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

There are no configuration notes.

## Attributes

EDAA32PFR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:20]

Reserved, RES0.

## MSA\_frac, bits [19:16]

## When EDAA32PFR.PMSA == '0000' and EDAA32PFR.VMSA == '1111':

Memory System Architecture fractional field. This holds the information on additional Memory System Architectures supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MSA_frac   | Meaning                                                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 0b0001     | PMSAv8-64 supported in all translation regimes. VMSAv8-64 not supported.                                                            |
| 0b0010     | PMSAv8-64 supported in all translation regimes. In addition to PMSAv8-64, stage 1 EL1&0 translation regime also supports VMSAv8-64. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## EL3, bits [15:12]

## When EDPFR.EL3 == '0000':

AArch32 EL3 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL3    | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0000 | EL3 is not implemented or can be executed in AArch64 state. |
| 0b0001 | EL3 can be executed in AArch32 state only.                  |

All other values are reserved.

Note

EDPFR.{EL1, EL0} indicate whether EL1 and EL0 can only be executed in AArch32 state.

Access to this field is RO.

## Otherwise:

Reserved, RAZ.

## EL2, bits [11:8]

## When EDPFR.EL2 == '0000':

AArch32 EL2 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL2    | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0000 | EL2 is not implemented or can be executed in AArch64 state. |
| 0b0001 | EL2 can be executed in AArch32 state only.                  |

All other values are reserved.

Note

EDPFR.{EL1, EL0} indicate whether EL1 and EL0 can only be executed in AArch32 state.

Access to this field is RO.

## Otherwise:

Reserved, RAZ.

## PMSA, bits [7:4]

Indicates support for a 32-bit PMSA.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

Access to this field is RO.

## When EDAA32PFR.PMSA == '0000':

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMSA   | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0000 | VMSAv8-64 supported.                                        |
| 0b1111 | Memory system architecture described by EDAA32PFR.MSA_frac. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## Otherwise:

Reserved, RAZ.

## Accessing EDAA32PFR

EDAA32PFR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xD60    | EDAA32PFR  |

Accessible as follows:

| PMSA   | Meaning                |
|--------|------------------------|
| 0b0000 | PMSA-32 not supported. |
| 0b0100 | PMSAv8-32 supported.   |

In Armv8-A, the only permitted value is 0b0000 . All other values are reserved. Access to this field is RO.

## VMSA, bits [3:0]

## When EDAA32PFR.PMSA != '0000':

Indicates support for a VMSA in addition to a 32-bit PMSA.

| VMSA   | Meaning            |
|--------|--------------------|
| 0b0000 | VMSAnot supported. |

- When IsCorePowered() and !DoubleLockStatus(), accesses to this register are RO.
- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.

## H9.2.11 EDACR, External Debug Auxiliary Control Register

The EDACR characteristics are:

## Purpose

Allows implementations to support IMPLEMENTATION DEFINED controls.

## Configuration

When FEAT\_DoPD is implemented, EDACR is in the Core power domain. Otherwise, it is IMPLEMENTATION DEFINED whether EDACR is implemented in the Core power domain or in the Debug power domain

If this register is implemented, EDDEVID.AuxRegs == 0b0001 .

If FEAT\_DoPD is implemented, any mechanism to preserve control bits in EDACR over power down is optional and IMPLEMENTATION DEFINED.

If FEAT\_DoPD is not implemented and EDACR contains any control bits that must be preserved over power down, then these bits must be accessible by the external debug interface when the OS Lock is locked, OSLSR\_EL1.OSLK == 1, and when the Core is powered off.

Changing this register from its reset value causes IMPLEMENTATION DEFINED behavior, including possible deviation from the architecturally-defined behavior.

Implementation of this register is OPTIONAL.

## Attributes

EDACRis a 32-bit register.

## Field descriptions

| 31                     | 0                      |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

The following resets apply:

- If the register is implemented in the Core power domain:
- On a Cold reset, this field resets to an architecturally UNKNOWN value.
- On an External debug reset, the value of this field is unchanged.
- On a Warm reset, the value of this field is unchanged.
- If the register is implemented in the External debug power domain:
- On a Cold reset, the value of this field is unchanged.
- On an External debug reset, this field resets to an architecturally UNKNOWN value.
- On a Warm reset, the value of this field is unchanged.

## Accessing EDACR

EDACRcan be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x094    | EDACR      |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register are IMPLEMENTATION DEFINED.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.12 EDCIDR0, External Debug Component Identification Register 0

The EDCIDR0 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Component Identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDCIDR0 is in the Core power domain. Otherwise, EDCIDR0 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDCIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_0, bits [7:0]

Preamble.

Reads as 0x0D

Access to this field is RO.

## Accessing EDCIDR0

EDCIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFF0    | EDCIDR0    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.13 EDCIDR1, External Debug Component Identification Register 1

The EDCIDR1 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Component Identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDCIDR1 is in the Core power domain. Otherwise, EDCIDR1 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDCIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## CLASS, bits [7:4]

Component class.

| CLASS   | Meaning              |
|---------|----------------------|
| 0b1001  | CoreSight component. |

Other values are defined by the CoreSight Architecture.

This field reads as 0x9 .

Access to this field is RO.

## PRMBL\_1, bits [3:0]

Preamble.

Reads as 0b0000

Access to this field is RO.

## Accessing EDCIDR1

EDCIDR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFF4    | EDCIDR1    |

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.14 EDCIDR2, External Debug Component Identification Register 2

The EDCIDR2 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Component Identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDCIDR2 is in the Core power domain. Otherwise, EDCIDR2 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDCIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_2, bits [7:0]

Preamble.

Reads as 0x05

Access to this field is RO.

## Accessing EDCIDR2

EDCIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFF8    | EDCIDR2    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.15 EDCIDR3, External Debug Component Identification Register 3

The EDCIDR3 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Component Identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDCIDR3 is in the Core power domain. Otherwise, EDCIDR3 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDCIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_3, bits [7:0]

Preamble.

Reads as 0xB1

Access to this field is RO.

## Accessing EDCIDR3

EDCIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFFC    | EDCIDR3    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.16 EDCIDSR, External Debug Context ID Sample Register

The EDCIDSR characteristics are:

## Purpose

Contains the sampled value of the Context ID, captured on reading EDPCSR[31:0].

## Configuration

EDCIDSR is in the Core power domain

Implemented only if the OPTIONAL PC Sample-based Profiling Extension is implemented in the external debug registers space.

Note

FEAT\_PCSRv8p2 implements the PC Sample-based Profiling Extension in the Performance Monitors registers space.

This register is present only when FEAT\_PCSRv8 is implemented and FEAT\_PCSRv8p2 is not implemented. Otherwise, direct accesses to EDCIDSR are RES0.

## Attributes

EDCIDSR is a 32-bit register.

## Field descriptions

CONTEXTIDR

31

0

## CONTEXTIDR, bits [31:0]

Context ID. The value of CONTEXTIDR that is associated with the most recent EDPCSR sample. When the most recent EDPCSR sample is generated:

- If EL1 is using AArch64, then the Context ID is sampled from CONTEXTIDR\_EL1.
- If EL1 is using AArch32, then the Context ID is sampled from CONTEXTIDR.
- If EL3 is implemented and is using AArch32, then CONTEXTIDR is a banked register, and EDCIDSR samples the current banked copy of CONTEXTIDR for the Security state that is associated with the most recent EDPCSR sample.

Because the value written to EDCIDSR is an indirect read of CONTEXTIDR, it is CONSTRAINED UNPREDICTABLE whether EDCIDSR is set to the original or new value if EDPCSR samples:

- An instruction that writes to CONTEXTIDR.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing EDCIDSR

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

EDCIDSR can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x0A4    | EDCIDSR    |

## H9.2.17 EDDEVAFF0, External Debug Device Affinity register 0

The EDDEVAFF0 characteristics are:

## Purpose

Copy of the low half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the external debug component relates to.

## Configuration

When FEAT\_DoPD is implemented, EDDEVAFF0 is in the Core power domain. Otherwise, EDDEVAFF0 is in the Debug power domain

## Attributes

EDDEVAFF0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RAO/WI.

## U, bit [30]

Indicates a Uniprocessor system, as distinct from PE 0 in a multiprocessor system.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| U   | Meaning                                       |
|-----|-----------------------------------------------|
| 0b0 | Processor is part of a multiprocessor system. |
| 0b1 | Processor is part of a uniprocessor system.   |

Access to this field is RO.

## Bits [29:25]

Reserved, RES0.

## MT, bit [24]

Indicates whether the lowest level of affinity consists of logical PEs that are implemented using an interdependent approach, such as multithreading. See the description of Aff0 for more information about affinity levels.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MT   | Meaning                                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Performance of PEs with different affinity level 0 values, and the same values for affinity level 1 and higher, is largely independent. |
| 0b1  | Performance of PEs with different affinity level 0 values, and the same values for affinity level 1 and higher, is very interdependent. |

## Note

This field does not indicate that multithreading is implemented and does not indicate that PEs with different affinity level 0 values, and the same values for affinity level 1 and higher are implemented.

Access to this field is RO.

## Aff2, bits [23:16]

Affinity level 2. See the description of Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Aff1, bits [15:8]

Affinity level 1. See the description of Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Aff0, bits [7:0]

Affinity level 0. The value of the MPIDR.{Aff2, Aff1, Aff0} or MPIDR\_EL1.{Aff3, Aff2, Aff1, Aff0} set of fields of each PE must be unique within the system as a whole.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDDEVAFF0

EDDEVAFF0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFA8    | EDDEVAFF0  |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.18 EDDEVAFF1, External Debug Device Affinity register 1

The EDDEVAFF1 characteristics are:

## Purpose

Copy of the high half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the external debug component relates to.

## Configuration

When FEAT\_DoPD is implemented, EDDEVAFF1 is in the Core power domain. Otherwise, EDDEVAFF1 is in the Debug power domain

## Attributes

EDDEVAFF1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7   |
|------|-------|
| RES0 | Aff3  |

## Bits [31:8]

Reserved, RES0.

## Aff3, bits [7:0]

Affinity level 3. See the description of EDDEV AFF0.Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDDEVAFF1

EDDEVAFF1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFAC    | EDDEVAFF1  |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.19 EDDEVARCH, External Debug Device Architecture Register

The EDDEVARCH characteristics are:

## Purpose

Identifies the programmers' model architecture of the external debug component.

## Configuration

When FEAT\_DoPD is implemented, EDDEVARCH is in the Core power domain. Otherwise, EDDEVARCH is in the Debug power domain

Implementation of this register is OPTIONAL.

## Attributes

EDDEVARCHis a 32-bit register.

## Field descriptions

<!-- image -->

## ARCHITECT, bits [31:21]

Defines the architect of the component. For External Debug, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as

0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the EDDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Defines the architecture revision. For architectures defined by Arm this is the minor revision.

For debug, the revision defined by Armv8 is 0x0 .

All other values are reserved.

Reads as 0b0000

Access to this field is RO.

## ARCHVER,bits [15:12]

Architecture Version. Defines the architecture version of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ARCHVER   | Meaning                                     |
|-----------|---------------------------------------------|
| 0b0110    | Armv8 debug architecture.                   |
| 0b0111    | Armv8.1 debug architecture, FEAT_Debugv8p1. |
| 0b1000    | Armv8.2 debug architecture, FEAT_Debugv8p2. |
| 0b1001    | Armv8.4 debug architecture, FEAT_Debugv8p4. |
| 0b1010    | Armv8.8 debug architecture, FEAT_Debugv8p8. |
| 0b1011    | Armv8.9 debug architecture, FEAT_Debugv8p9. |

EDDEVARCH.ARCHVER and EDDEVARCH.ARCHPART are also defined as a single field, EDDEVARCH.ARCHID, so that EDDEVARCH.ARCHVER is EDDEVARCH.ARCHID[15:12].

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

## ARCHPART, bits [11:0]

Architecture Part. Defines the architecture of the component.

| ARCHPART   | Meaning                     |
|------------|-----------------------------|
| 0xA15      | Armv8-A debug architecture. |

EDDEVARCH.ARCHVER and EDDEVARCH.ARCHPART are also defined as a single field, EDDEVARCH.ARCHID, so that EDDEVARCH.ARCHPART is EDDEVARCH.ARCHID[11:0].

Armv8-A debug architecture.

Access to this field is RO.

## Accessing EDDEVARCH

EDDEVARCHcan be accessed through the external debug interface:

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFBC    | EDDEVARCH  |

## H9.2.20 EDDEVID, External Debug Device ID register 0

The EDDEVID characteristics are:

## Purpose

Provides extra information for external debuggers about features of the debug implementation.

## Configuration

When FEAT\_DoPD is implemented, EDDEVID is in the Core power domain. Otherwise, EDDEVID is in the Debug power domain

## Attributes

EDDEVID is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 28 27   | 24 23   | 8 7        | 4 3      |
|------|---------|---------|------------|----------|
| RES0 | AuxRegs | RES0    | DebugPower | PCSample |

## Bits [31:28]

Reserved, RES0.

## AuxRegs, bits [27:24]

Indicates support for Auxiliary registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AuxRegs   | Meaning                                                       |
|-----------|---------------------------------------------------------------|
| 0b0000    | None supported.                                               |
| 0b0001    | Support for External Debug Auxiliary Control Register, EDACR. |

All other values are reserved.

Access to this field is RO.

## Bits [23:8]

Reserved, RES0.

## DebugPower, bits [7:4]

Indicates support for the FEAT\_DoPD feature.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DebugPower   | Meaning                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000       | FEAT_DoPD not implemented. Registers in the external debug interface register map are implemented in a mix of the Debug and Core power domains. |
| 0b0001       | FEAT_DoPD implemented. All registers in the external debug interface register map are implemented in the Core power domain.                     |

FEAT\_DoPD implements the functionality added by the value 0b0001 .

All other values are reserved.

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

## Accessing EDDEVID

EDDEVID can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFC8    | EDDEVID    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.21 EDDEVID1, External Debug Device ID Register 1

The EDDEVID1 characteristics are:

## Purpose

Provides extra information for external debuggers about features of the debug implementation.

## Configuration

When FEAT\_DoPD is implemented, EDDEVID1 is in the Core power domain. Otherwise, EDDEVID1 is in the Debug power domain

## Attributes

EDDEVID1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7   | 4 3 0      |
|------|-------|------------|
| RES0 | HSR   | PCSROffset |

## Bits [31:8]

Reserved, RES0.

## HSR, bits [7:4]

Indicates support for the External Debug Halt Status Register, EDHSR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HSR    | Meaning                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------|
| 0b0000 | EDHSR not implemented, and the PE follows behaviors consistent with all of the EDHSR fields having a zero value. |
| 0b0001 | EDHSR implemented.                                                                                               |
| 0b0010 | As 0b0001 , but extends EDHSR to include the VNCR, CM, and WnRfields.                                            |

All other values are reserved.

FEAT\_EDHSR implements the functionality identified by the value 0b0001 .

FEAT\_Debugv8p9 implements the functionality identified by the value 0b0010 .

When FEAT\_Debugv8p2 is not implemented, the only permitted value is 0b0000 .

From Armv8.9, the values 0b0000 and 0b0001 are not permitted.

Access to this field is RO.

## PCSROffset, bits [3:0]

Indicates the offset applied to PC samples returned by reads of EDPCSR.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PCSROffset   | Meaning                                                                                                              |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| 0b0000       | EDPCSR not implemented.                                                                                              |
| 0b0010       | EDPCSR implemented, and samples have no offset applied and do not sample the instruction set state in AArch32 state. |

When FEAT\_PCSRv8p2 is implemented, the only permitted value is 0b0000 .

Note

FEAT\_PCSRv8p2 implements the PC Sample-based Profiling Extension in the Performance Monitors register space, as indicated by the value of PMDEVID.PCSample.

Access to this field is RO.

## Accessing EDDEVID1

EDDEVID1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFC4    | EDDEVID1   |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.22 EDDEVID2, External Debug Device ID register 2

The EDDEVID2 characteristics are:

## Purpose

Reserved for future descriptions of features of the debug implementation.

## Configuration

When FEAT\_DoPD is implemented, EDDEVID2 is in the Core power domain. Otherwise, EDDEVID2 is in the Debug power domain

## Attributes

EDDEVID2 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing EDDEVID2

EDDEVID2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFC0    | EDDEVID2   |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.23 EDDEVTYPE, External Debug Device Type register

The EDDEVTYPE characteristics are:

## Purpose

Indicates to a debugger that this component is part of a PE's debug logic.

## Configuration

When FEAT\_DoPD is implemented, EDDEVTYPE is in the Core power domain. Otherwise, EDDEVTYPE is in the Debug power domain

Implementation of this register is OPTIONAL.

## Attributes

EDDEVTYPE is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SUB, bits [7:4]

Subtype. Indicates this is a component within a PE.

Reads as

0b0001

Access to this field is RO.

## MAJOR, bits [3:0]

Major type. Indicates this is a debug logic component.

Reads as

0b0101

Access to this field is RO.

## Accessing EDDEVTYPE

EDDEVTYPE can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFCC    | EDDEVTYPE  |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.24 EDDFR, External Debug Feature Register

The EDDFR characteristics are:

## Purpose

Provides top-level information about the debug system.

Note

Debuggers must use EDDEVARCH to determine the Debug architecture version.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

There are no configuration notes.

## Attributes

EDDFR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 60 59      | 56 55   | 56 55   | 48 47       | 44 43     | 40 39    | 32      |
|----------|------------|---------|---------|-------------|-----------|----------|---------|
| UNKNOWN  | ExtTrcBuff | UNKNOWN |         | TraceBuffer | TraceFilt | UNKNOWN  |         |
| 31       | 28 27      | 24 23   | 20 19   | 16 15       | 12 11 8   | 7 4      | 3 0     |
| CTX_CMPs | SEBEP      | WRPs    | PMSS    | BRPs        | PMUVer    | TraceVer | UNKNOWN |

## Bits [63:60]

Reserved, UNKNOWN.

## ExtTrcBuff, bits [59:56]

Trace Buffer External Mode Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ExtTrcBuff   | Meaning                                                                               |
|--------------|---------------------------------------------------------------------------------------|
| 0b0000       | Trace Buffer Extension not implemented or Trace Buffer External Mode not implemented. |
| 0b0001       | Trace Buffer Extension implemented and Trace Buffer External Mode implemented.        |

All other values are reserved.

If FEAT\_TRBE is not implemented, the only permitted value is 0b0000 .

FEAT\_TRBE\_EXT implements the functionality identified by the value 0b0001 .

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR0\_EL1.ExtTrcBuff.

Access to this field is RO.

## Bits [55:48]

Reserved, UNKNOWN.

## TraceBuffer, bits [47:44]

## When FEAT\_TRBE\_EXT is implemented:

Trace Buffer Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TraceBuffer   | Meaning                                                                                                                                                                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000        | Trace Buffer Extension not implemented.                                                                                                                                                                                                        |
| 0b0001        | Trace Buffer Extension implemented.                                                                                                                                                                                                            |
| 0b0010        | As 0b0001 , and adds: • If EL2 and FEAT_FGT are implemented, a fine-grained trap on the TSB CSYNC instruction. • If EL2 is implemented, an EL2 control to override TRBLIMITR_EL1.nVM. • The TRBE Profiling exception extension, FEAT_TRBE_EXC. |

All other values are reserved.

FEAT\_TRBE implements the functionality identified by the value 0b0001 .

FEAT\_TRBEv1p1 implements the functionality identified by the value 0b0010 .

In any Armv9 implementation, if FEAT\_ETE is implemented, the value 0b0000 is not permitted.

From Armv9.6, if FEAT\_TRBE is implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## Otherwise:

Reserved, UNKNOWN.

## TraceFilt, bits [43:40]

Armv8.4 Self-hosted Trace Extension version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TraceFilt   | Meaning                                              |
|-------------|------------------------------------------------------|
| 0b0000      | Armv8.4 Self-hosted Trace Extension not implemented. |
| 0b0001      | Armv8.4 Self-hosted Trace Extension implemented.     |

All other values are reserved.

FEAT\_TRF implements the functionality identified by the value 0b0001 .

From Armv8.4, if FEAT\_ETMv4 is implemented, the value 0b0000 is not permitted.

If FEAT\_ETE is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## Bits [39:32]

Reserved, UNKNOWN.

## CTX\_CMPs, bits [31:28]

Number of context-aware breakpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CTX_CMPs         | Meaning                                           |
|------------------|---------------------------------------------------|
| 0b0000 .. 0b1111 | The number of context-aware breakpoints, minus 1. |

The value of this field is never greater than EDDFR.BRPs.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR0\_EL1.CTX\_CMPs.

If FEAT\_Debugv8p9 is implemented and 16 or more context-aware breakpoints are implemented, then this field reads as 0b1111 and EDDFR1.CTX\_CMPs indicates the number of context-aware breakpoints.

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 breakpoints.

Access to this field is RO.

## SEBEP, bits [27:24]

This field either has the same value as ID\_AA64DFR0\_EL1.SEBEP or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## WRPs, bits [23:20]

Number of watchpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WRPs             | Meaning                             |
|------------------|-------------------------------------|
| 0b0001 .. 0b1111 | The number of watchpoints, minus 1. |

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR0\_EL1.WRPs.

If FEAT\_Debugv8p9 is implemented and 16 or more watchpoints are implemented, then this field reads as 0b1111 and EDDFR1.WRPs indicates the number of watchpoints.

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 watchpoints.

The value 0b0000 is reserved.

Access to this field is RO.

## PMSS, bits [19:16]

This field either has the same value as ID\_AA64DFR0\_EL1.PMSS or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## BRPs, bits [15:12]

Number of breakpoints, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BRPs             | Meaning                             |
|------------------|-------------------------------------|
| 0b0001 .. 0b1111 | The number of breakpoints, minus 1. |

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR0\_EL1.BRPs.

If FEAT\_Debugv8p9 is implemented and 16 or more breakpoints are implemented, then this field reads as 0b1111 and EDDFR1.BRPs indicates the number of breakpoints.

Note

If AArch32 is supported at EL1, then the PE does not implement more than 16 breakpoints.

The value 0b0000 is reserved.

Access to this field is RO.

## PMUVer, bits [11:8]

Performance Monitors Extension version.

This field does not follow the standard ID scheme, but uses the alternative ID scheme described in 'Alternative ID scheme used for the Performance Monitors Extension version'

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PMUVer   | Meaning                                                                                                                                                                               |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000   | Performance Monitors Extension not implemented.                                                                                                                                       |
| 0b0001   | Performance Monitors Extension, PMUv3 implemented.                                                                                                                                    |
| 0b0100   | PMUv3 for Armv8.1. As 0b0001 , and adds support for: • Extended 16-bit PMEVTYPER<n>_EL0.evtCount field. • If EL2 is implemented, the MDCR_EL2.HPMD control.                           |
| 0b0101   | PMUv3 for Armv8.4. As 0b0100 , and adds support for the PMMIR_EL1 register.                                                                                                           |
| 0b0110   | PMUv3 for Armv8.5. As 0b0101 , and adds support for: • 64-bit event counters. • If EL2 is implemented, the MDCR_EL2.HCCD control. • If EL3 is implemented, the MDCR_EL3.SCCD control. |

| PMUVer   | Meaning                                                                                                                                                                                                                                      |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0111   | PMUv3 for Armv8.7. As 0b0110 , and adds support for: • The PMCR_EL0.FZO and, if EL2 is implemented, MDCR_EL2.HPMFZO controls. • If EL3 is implemented, the MDCR_EL3.{MPMX,MCCD} controls.                                                    |
| 0b1000   | PMUv3 for Armv8.8. As 0b0111 , and: • Extends the Common event number space to include 0x0040 to 0x00BF and 0x4040 to 0x40BF . • Removes the CONSTRAINED UNPREDICTABLE behaviors if a reserved or unimplemented PMUevent number is selected. |
| 0b1001   | PMUv3 for Armv8.9. As 0b1000 , and: • Updates the definitions of existing PMUevents. • Adds support for the PMUSERENR_EL0.UEN control and the PMUACR_EL1 register. • Adds support for the EDECR.PME control.                                 |
| 0b1111   | IMPLEMENTATION DEFINED form of performance monitors supported, PMUv3 not supported. Arm does not recommend this value for new implementations.                                                                                               |

## All other values are reserved.

FEAT\_PMUv3 implements the functionality identified by the value 0b0001 .

FEAT\_PMUv3p1 implements the functionality identified by the value 0b0100 .

FEAT\_PMUv3p4 implements the functionality identified by the value 0b0101 .

FEAT\_PMUv3p5 implements the functionality identified by the value 0b0110 .

FEAT\_PMUv3p7 implements the functionality identified by the value 0b0111 .

FEAT\_PMUv3p8 implements the functionality identified by the value 0b1000 .

FEAT\_PMUv3p9 implements the functionality identified by the value 0b1001 .

From Armv8.1, if FEAT\_PMUv3 is implemented, the value 0b0001 is not permitted.

From Armv8.4, if FEAT\_PMUv3 is implemented, the value 0b0100 is not permitted.

From Armv8.5, if FEAT\_PMUv3 is implemented, the value 0b0101 is not permitted.

From Armv8.7, if FEAT\_PMUv3 is implemented, the value 0b0110 is not permitted.

From Armv8.8, if FEAT\_PMUv3 is implemented, the value 0b0111 is not permitted.

From Armv8.9, if FEAT\_PMUv3 is implemented, the value 0b1000 is not permitted.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR0\_EL1.PMUVer.

Access to this field is RO.

## TraceVer, bits [7:4]

Trace support. Indicates whether System register interface to a trace unit is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TraceVer   | Meaning                                      |
|------------|----------------------------------------------|
| 0b0000     | Trace unit System registers not implemented. |
| 0b0001     | Trace unit System registers implemented.     |

All other values are reserved.

Avalue of 0b0000 only indicates that no System register interface to a trace unit is implemented. A trace unit might nevertheless be implemented without a System register interface.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64DFR0\_EL1.TraceVer.

Access to this field is RO.

## Bits [3:0]

Reserved, UNKNOWN.

## Accessing EDDFR

EDDFR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xD28    | EDDFR      |

## Accessible as follows:

- When IsCorePowered() and !DoubleLockStatus(), accesses to this register are RO.
- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.

## H9.2.25 EDDFR1, External Debug Feature Register 1

The EDDFR1 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch64.

## Configuration

There are no configuration notes.

## Attributes

EDDFR1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35    | 32   |
|----------|---------|---------|---------|---------|---------|----------|------|
| ABL_CMPs | DPFZS   | EBEP    | ITE     | ABLE    | PMICNTR | SPMU     |      |
| 31       | 24 23   | 16 15   |         |         | 8 7     | 0        |      |
| CTX_CMPs | WRPs    |         |         | BRPs    |         | SYSPMUID |      |

## ABL\_CMPs, bits [63:56]

## When FEAT\_ABLE is implemented:

Number of breakpoints that support address linking, minus 1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ABL_CMPs     | Meaning                                                     |
|--------------|-------------------------------------------------------------|
| 0x00 .. 0x3F | Number of breakpoints that support address linking minus 1. |

All other values are reserved.

The number of breakpoints that support address linking is never more than either the number of breakpoints or the number of watchpoints.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR1\_EL1.ABL\_CMPs.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## DPFZS, bits [55:52]

This field either has the same value as ID\_AA64DFR1\_EL1.DPFZS or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## EBEP, bits [51:48]

This field either has the same value as ID\_AA64DFR1\_EL1.EBEP or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## ITE, bits [47:44]

This field either has the same value as ID\_AA64DFR1\_EL1.ITE or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## ABLE, bits [43:40]

Address Breakpoint Linking Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ABLE   | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0000 | Address Breakpoint Linking Extension not implemented. |
| 0b0001 | Address Breakpoint Linking Extension implemented.     |

All other values are reserved.

FEAT\_BWE implements the address range breakpoints and mismatch breakpoints part of the functionality identified by the value 0b0001 .

FEAT\_ABLE implements the functionality identified by the value 0b0001 .

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR1\_EL1.ABLE.

Access to this field is RO.

## PMICNTR, bits [39:36]

This field either has the same value as ID\_AA64DFR1\_EL1.PMICNTR or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SPMU, bits [35:32]

This field either has the same value as ID\_AA64DFR1\_EL1.SPMU or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CTX\_CMPs, bits [31:24]

Context-aware breakpoints.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CTX_CMPs     | Meaning                                                             |
|--------------|---------------------------------------------------------------------|
| 0x00         | EDDFR.CTX_CMPs is the number of context-aware breakpoints, minus 1. |
| 0x01 .. 0x3F | Number of context-aware breakpoints minus 1.                        |

All other values are reserved.

The value of this field is never greater than EDDFR1.BRPs.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR1\_EL1.CTX\_CMPs. Access to this field is RO.

## WRPs, bits [23:16]

Watchpoints.

| WRPs         | Meaning                                           |
|--------------|---------------------------------------------------|
| 0x00         | EDDFR.WRPs is the number of watchpoints, minus 1. |
| 0x01 .. 0x3F | Number of watchpoints minus 1.                    |

All other values are reserved.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR1\_EL1.WRPs.

## BRPs, bits [15:8]

Breakpoints.

| BRPs         | Meaning                                           |
|--------------|---------------------------------------------------|
| 0x00         | EDDFR.BRPs is the number of breakpoints, minus 1. |
| 0x01 .. 0x3F | Number of breakpoints minus 1.                    |

All other values are reserved.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR1\_EL1.BRPs.

## SYSPMUID, bits [7:0]

This field either has the same value as ID\_AA64DFR1\_EL1.SYSPMUID or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDDFR1

EDDFR1 can be accessed through the external debug interface:

## Accessible as follows:

- When (IsCorePowered() &amp;&amp; (!DoubleLockStatus())) &amp;&amp; ((!IsZero(EDDFR1())) || (!OSLockStatus())), accesses to this register are RO.
- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xD48    | EDDFR1     |

## H9.2.26 EDDFR2, External Debug Feature Register 2

The EDDFR2 characteristics are:

## Purpose

Provides top-level information about the debug system in AArch64.

## Configuration

There are no configuration notes.

## Attributes

EDDFR2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:28]

Reserved, RES0.

## TRBE\_EXC, bits [27:24]

This field either has the same value as ID\_AA64DFR2\_EL1.TRBE\_EXC or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SPE\_nVM, bits [23:20]

This field either has the same value as ID\_AA64DFR2\_EL1.SPE\_nVM or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SPE\_EXC, bits [19:16]

This field either has the same value as ID\_AA64DFR2\_EL1.SPE\_EXC or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bits [15:8]

Reserved, RES0.

## BWE, bits [7:4]

Breakpoints and watchpoint enhancements.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BWE    | Meaning                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------|
| 0b0000 | This field does not indicate whether DBGBCR<n>_EL1.MASK and address mismatch breakpoints are implemented. |
| 0b0001 | DBGBCR<n>_EL1.MASK and address mismatch breakpoints are implemented.                                      |
| 0b0010 | As 0b0001 , and address mismatch watchpoints are implemented.                                             |

All other values are reserved.

FEAT\_BWE implements the functionality identified by the value 0b0001 .

FEAT\_BWE2 implements the functionality identified by the value 0b0010 .

When this field is 0b0000 , ID\_AA64DFR1\_EL1.ABLE might indicate the presence of support for DBGBCR&lt;n&gt;\_EL1.MASK and address mismatch breakpoints.

From Armv9.5, the value 0b0001 is not permitted.

In an implementation that supports AArch64, this field has the same value as ID\_AA64DFR2\_EL1.BWE.

Access to this field is RO.

## STEP, bits [3:0]

This field either has the same value as ID\_AA64DFR2\_EL1.STEP or reads as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDDFR2

EDDFR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xD50    | EDDFR2     |

Accessible as follows:

- When (IsCorePowered() &amp;&amp; (!DoubleLockStatus())) &amp;&amp; ((!IsZero(EDDFR2())) || (!OSLockStatus())), accesses to this register are RO.
- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.

## H9.2.27 EDECCR, External Debug Exception Catch Control Register

The EDECCR characteristics are:

## Purpose

Controls Exception Catch debug events. For more information, see 'Exception Catch debug event'.

## Configuration

EDECCR is in the Core power domain

External register EDECCR bits [31:0] are architecturally mapped to AArch64 System register OSECCR\_EL1[31:0].

External register EDECCR bits [31:0] are architecturally mapped to AArch32 System register DBGOSECCR[31:0].

## Attributes

EDECCR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:23]

Reserved, RES0.

## RLR2, bit [22]

## When FEAT\_RME is implemented:

Controls exception catch on exception return to Realm EL2 in conjunction with EDECCR.RLE2.

| RLR2   | Meaning                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.RLE2 is 0, then Exception Catch debug events are disabled for Realm EL2. If EDECCR.RLE2 is 1, then Exception Catch debug events are enabled for exception entry and exception return to Realm EL2. |
| 0b1    | If EDECCR.RLE2 is 0, then Exception Catch debug events are enabled for exception returns to Realm EL2. If EDECCR.RLE2 is 1, then Exception Catch debug events are enabled for exception entry to Realm EL2.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

RLR1, bit [21]

## When FEAT\_RME is implemented:

Controls exception catch on exception return to Realm EL1 in conjunction with EDECCR.RLE1.

| RLR1   | Meaning                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.RLE1 is 0, then Exception Catch debug events are disabled for Realm EL1. If EDECCR.RLE1 is 1, then Exception Catch debug events are enabled for exception entry and exception return to Realm EL1. |
| 0b1    | If EDECCR.RLE1 is 0, then Exception Catch debug events are enabled for exception returns to Realm EL1. If EDECCR.RLE1 is 1, then Exception Catch debug events are enabled for exception entry to Realm EL1.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

RLR0, bit [20]

## When FEAT\_RME is implemented:

Controls exception catch on exception return to Realm EL0.

| RLR0   | Meaning                                                                      |
|--------|------------------------------------------------------------------------------|
| 0b0    | Exception Catch debug events are disabled for Realm EL0.                     |
| 0b1    | Exception Catch debug events are enabled for exception returns to Realm EL0. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

Bit [19]

Reserved, RES0.

RLE2, bit [18]

## When FEAT\_RME is implemented:

Controls exception catch on exception entry to Realm EL2. Also controls exception catch on exception return to Realm EL2 in conjunction with EDECCR.RLR2.

| RLE2   | Meaning                                                                                                                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.RLR2 is 0, then Exception Catch debug events are disabled for Realm EL2. If EDECCR.RLR2 is 1, then Exception Catch debug events are enabled for exception returns to Realm EL2.                                      |
| 0b1    | If EDECCR.RLR2 is 0, then Exception Catch debug events are enabled for exception entry and exception return to Realm EL2. If EDECCR.RLR2 is 1, then Exception Catch debug events are enabled for exception entry to Realm EL2. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

RLE1, bit [17]

## When FEAT\_RME is implemented:

Controls exception catch on exception entry to Realm EL1. Also controls exception catch on exception return to Realm EL1 in conjunction with EDECCR.RLR1.

| RLE1   | Meaning                                                                                                                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.RLR1 is 0, then Exception Catch debug events are disabled for Realm EL1. If EDECCR.RLR1 is 1, then Exception Catch debug events are enabled for exception returns to Realm EL1.                                      |
| 0b1    | If EDECCR.RLR1 is 0, then Exception Catch debug events are enabled for exception entry and exception return to Realm EL1. If EDECCR.RLR1 is 1, then Exception Catch debug events are enabled for exception entry to Realm EL1. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## RLE0, bit [16]

Access to this field is RES0.

## NSR3, bit [15]

Access to this field is RES0.

NSR2, bit [14]

## When FEAT\_Debugv8p2 is implemented and Non-secure EL2 is implemented:

Controls exception catch on exception return to Non-secure EL2 in conjunction with EDECCR.NSE2.

| NSR2   | Meaning                                                                                                                                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.NSE2 is 0, then Exception Catch debug events are disabled for Non-secure EL2. If EDECCR.NSE2 is 1, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Non-secure EL2.  |
| 0b1    | If EDECCR.NSE2 is 0, then Exception Catch debug events are enabled for exception returns to Non-secure EL2. If EDECCR.NSE2 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Non-secure EL2. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

NSR1, bit [13]

## When FEAT\_Debugv8p2 is implemented and Non-secure EL1 is implemented:

Controls exception catch on exception return to Non-secure EL1 in conjunction with EDECCR.NSE1.

| NSR1   | Meaning                                                                                                                                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.NSE1 is 0, then Exception Catch debug events are disabled for Non-secure EL1. If EDECCR.NSE1 is 1, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Non-secure EL1.  |
| 0b1    | If EDECCR.NSE1 is 0, then Exception Catch debug events are enabled for exception returns to Non-secure EL1. If EDECCR.NSE1 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Non-secure EL1. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

NSR0, bit [12]

## When FEAT\_Debugv8p2 is implemented and Non-secure EL0 is implemented:

Controls exception catch on exception return to Non-secure EL0.

| NSR0   | Meaning                                                                           |
|--------|-----------------------------------------------------------------------------------|
| 0b0    | Exception Catch debug events are disabled for Non-secure EL0.                     |
| 0b1    | Exception Catch debug events are enabled for exception returns to Non-secure EL0. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SR3, bit [11]

## When FEAT\_Debugv8p2 is implemented and EL3 is implemented:

Controls exception catch on exception return to EL3 in conjunction with EDECCR.SE3.

| SR3   | Meaning                                                                                                                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDECCR.SE3 is 0, then Exception Catch debug events are disabled for EL3. If EDECCR.SE3 is 1, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to EL3.  |
| 0b1   | If EDECCR.SE3 is 0, then Exception Catch debug events are enabled for exception returns to EL3. If EDECCR.SE3 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to EL3. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SR2, bit [10]

## When FEAT\_Debugv8p2 is implemented and FEAT\_SEL2 is implemented:

Controls exception catch on exception return to Secure EL2 in conjunction with EDECCR.SE2.

| SR2   | Meaning                                                                                                                                                                                                                     |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDECCR.SE2 is 0, then Exception Catch debug events are disabled for Secure EL2. If EDECCR.SE2 is 1, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Secure EL2.  |
| 0b1   | If EDECCR.SE2 is 0, then Exception Catch debug events are enabled for exception returns to Secure EL2. If EDECCR.SE2 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Secure EL2. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SR1, bit [9]

## When FEAT\_Debugv8p2 is implemented and Secure EL1 is implemented:

Controls exception catch on exception return to Secure EL1 in conjunction with EDECCR.SE1.

| SR1   | Meaning                                                                                                                                                                                                                     |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDECCR.SE1 is 0, then Exception Catch debug events are disabled for Secure EL1. If EDECCR.SE1 is 1, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Secure EL1.  |
| 0b1   | If EDECCR.SE1 is 0, then Exception Catch debug events are enabled for exception returns to Secure EL1. If EDECCR.SE1 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Secure EL1. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

SR0, bit [8]

## When FEAT\_Debugv8p2 is implemented and Secure EL0 is implemented:

Controls exception catch on exception return to Secure EL0.

| SR0   | Meaning                                                                       |
|-------|-------------------------------------------------------------------------------|
| 0b0   | Exception Catch debug events are disabled for Secure EL0.                     |
| 0b1   | Exception Catch debug events are enabled for exception returns to Secure EL0. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## NSE3, bit [7]

Access to this field is RES0.

## NSE2, bit [6]

## When FEAT\_Debugv8p2 is implemented and Non-secure EL2 is implemented:

Controls exception catch on exception entry to Non-secure EL2. Also controls exception catch on exception return to Non-secure EL2 in conjunction with EDECCR.NSR2.

| NSE2   | Meaning                                                                                                                                                                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.NSR2 is 0, then Exception Catch debug events are disabled for Non-secure EL2. If EDECCR.NSR2 is 1, then Exception Catch debug events are enabled for exception returns to Non-secure EL2.                                                                    |
| 0b1    | If EDECCR.NSR2 is 0, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Non-secure EL2. If EDECCR.NSR2 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Non-secure EL2. |

Note

It is IMPLEMENTATION DEFINED whether a reset entry to an Exception level will generate an Exception Catch debug event.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## When Non-secure EL2 is implemented:

Coarse-grained exception catch for Non-secure EL2. Controls Exception Catch debug events for Non-secure EL2.

| NSE2   | Meaning                                                       |
|--------|---------------------------------------------------------------|
| 0b0    | Exception Catch debug events are disabled for Non-secure EL2. |
| 0b1    | Exception Catch debug events are enabled for Non-secure EL2.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## NSE1, bit [5]

## When FEAT\_Debugv8p2 is implemented and Non-secure EL1 is implemented:

Controls exception catch on exception entry to Non-secure EL1. Also controls exception catch on exception return to Non-secure EL1 in conjunction with EDECCR.NSR1.

| NSE1   | Meaning                                                                                                                                                                                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | If EDECCR.NSR1 is 0, then Exception Catch debug events are disabled for Non-secure EL1. If EDECCR.NSR1 is 1, then Exception Catch debug events are enabled for exception returns to Non-secure EL1.                                                                    |
| 0b1    | If EDECCR.NSR1 is 0, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Non-secure EL1. If EDECCR.NSR1 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Non-secure EL1. |

Note

It is IMPLEMENTATION DEFINED whether a reset entry to an Exception level will generate an Exception Catch debug event.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## When Non-secure EL1 is implemented:

Coarse-grained exception catch for Non-secure EL1. Controls Exception Catch debug events for Non-secure EL1.

| NSE1   | Meaning                                                       |
|--------|---------------------------------------------------------------|
| 0b0    | Exception Catch debug events are disabled for Non-secure EL1. |
| 0b1    | Exception Catch debug events are enabled for Non-secure EL1.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## NSE0, bit [4]

Access to this field is RES0.

## SE3, bit [3]

## When FEAT\_Debugv8p2 is implemented and EL3 is implemented:

Controls exception catch on exception entry to EL3. Also controls exception catch on exception return to EL3 in conjunction with EDECCR.SR3.

| SE3   | Meaning                                                                                                                                                                                                                                        |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDECCR.SR3 is 0, then Exception Catch debug events are disabled for EL3. If EDECCR.SR3 is 1, then Exception Catch debug events are enabled for exception returns to EL3.                                                                    |
| 0b1   | If EDECCR.SR3 is 0, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to EL3. If EDECCR.SR3 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to EL3. |

## Note

It is IMPLEMENTATION DEFINED whether a reset entry to an Exception level will generate an Exception Catch debug event.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## When FEAT\_Debugv8p2 is not implemented and EL3 is implemented:

Coarse-grained exception catch for EL3. Controls Exception Catch debug events for EL3.

| SE3   | Meaning                                            |
|-------|----------------------------------------------------|
| 0b0   | Exception Catch debug events are disabled for EL3. |
| 0b1   | Exception Catch debug events are enabled for EL3.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## SE2, bit [2]

## When FEAT\_Debugv8p2 is implemented and FEAT\_SEL2 is implemented:

Controls exception catch on exception entry to Secure EL2. Also controls exception catch on exception return to Secure EL2 in conjunction with EDECCR.SR2.

| SE2   | Meaning                                                                                                                                                                                                                                                      |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDECCR.SR2 is 0, then Exception Catch debug events are disabled for Secure EL2. If EDECCR.SR2 is 1, then Exception Catch debug events are enabled for exception returns to Secure EL2.                                                                    |
| 0b1   | If EDECCR.SR2 is 0, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Secure EL2. If EDECCR.SR2 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Secure EL2. |

Note

It is IMPLEMENTATION DEFINED whether a reset entry to an Exception level will generate an Exception Catch debug event.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## SE1, bit [1]

## When FEAT\_Debugv8p2 is implemented and Secure EL1 is implemented:

Controls exception catch on exception entry to Secure EL1. Also controls exception catch on exception return to Secure EL1 in conjunction with EDECCR.SR1.

| SE1   | Meaning                                                                                                                                                                                                                                                      |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDECCR.SR1 is 0, then Exception Catch debug events are disabled for Secure EL1. If EDECCR.SR1 is 1, then Exception Catch debug events are enabled for exception returns to Secure EL1.                                                                    |
| 0b1   | If EDECCR.SR1 is 0, then Exception Catch debug events are enabled for exception entry, reset entry, and exception return to Secure EL1. If EDECCR.SR1 is 1, then Exception Catch debug events are enabled for exception entry and reset entry to Secure EL1. |

Note

It is IMPLEMENTATION DEFINED whether a reset entry to an Exception level will generate an Exception Catch debug event.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## When Secure EL1 is implemented:

Coarse-grained exception catch for Secure EL1. Controls Exception Catch debug events for Secure EL1.

| SE1   | Meaning                                                   |
|-------|-----------------------------------------------------------|
| 0b0   | Exception Catch debug events are disabled for Secure EL1. |
| 0b1   | Exception Catch debug events are enabled for Secure EL1.  |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## SE0, bit [0]

Access to this field is RES0.

## Accessing EDECCR

EDECCR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x098    | EDECCR     |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.28 EDECR, External Debug Execution Control Register

The EDECR characteristics are:

## Purpose

Controls Halting debug events.

## Configuration

When FEAT\_DoPD is implemented, EDECR is in the Core power domain. Otherwise, EDECR is in the Debug power domain

## Attributes

EDECR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:7]

Reserved, RES0.

## TRBE, bit [6]

## When FEAT\_Debugv8p9 is implemented and FEAT\_TRBE\_EXT is implemented:

Trace Buffer External Debug Request Enable.

| TRBE   | Meaning                                       |
|--------|-----------------------------------------------|
| 0b0    | Trace Buffer External Debug Request disabled. |
| 0b1    | Trace Buffer External Debug Request enabled.  |

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## TRCE, bit [5]

When FEAT\_ETEv1p3 is implemented and FEAT\_Debugv8p9 is implemented:

ETE External Debug Request Enable.

| TRCE   | Meaning                              |
|--------|--------------------------------------|
| 0b0    | ETE External Debug Request disabled. |
| 0b1    | ETE External Debug Request enabled.  |

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

PME, bit [4]

## When FEAT\_Debugv8p9 is implemented and FEAT\_PMUv3p9 is implemented:

PMUOverflow External Debug Request Enable.

| PME   | Meaning                                      |
|-------|----------------------------------------------|
| 0b0   | PMUOverflow External Debug Request disabled. |
| 0b1   | PMUOverflow External Debug Request enabled.  |

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [3]

Reserved, RES0.

## SS, bit [2]

Halting step enable. Possible values of this field are:

| SS   | Meaning                            |
|------|------------------------------------|
| 0b0  | Halting step debug event disabled. |
| 0b1  | Halting step debug event enabled.  |

If the value of EDECR.SS is changed when the PE is in Non-debug state, behavior is CONSTRAINED UNPREDICTABLE as described in 'Changing the value of EDECR.SS when not in Debug state'.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_DoPD is implemented, this field resets to '0' .

- On a External debug reset:
- When FEAT\_DoPD is not implemented, this field resets to '0' .

RCE, bit [1]

## When FEAT\_DoPD is not implemented:

Reset Catch Enable.

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| RCE   | Meaning                           |
|-------|-----------------------------------|
| 0b0   | Reset Catch debug event disabled. |
| 0b1   | Reset Catch debug event enabled.  |

The reset behavior of this field is:

- On a External debug reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

OSUCE, bit [0]

## When FEAT\_DoPD is not implemented:

OS Unlock Catch Enable.

| OSUCE   | Meaning                               |
|---------|---------------------------------------|
| 0b0     | OS Unlock Catch debug event disabled. |
| 0b1     | OS Unlock Catch debug event enabled.  |

The reset behavior of this field is:

- On a External debug reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Accessing EDECR

EDECR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x024    | EDECR      |

## H9.2.29 EDESR, External Debug Event Status Register

The EDESR characteristics are:

## Purpose

Indicates the status of internally pending Halting debug events.

## Configuration

EDESR is in the Core power domain

## Attributes

EDESR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:4]

Reserved, RES0.

## EC, bit [3]

## When FEAT\_Debugv8p8 is implemented:

Exception Catch debug event pending.

| EC   | Meaning                                     |
|------|---------------------------------------------|
| 0b0  | Exception Catch debug event is not pending. |
| 0b1  | Exception Catch debug event is pending.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Access to this field is W1C.

## Otherwise:

Reserved, RES0.

## SS, bit [2]

## When FEAT\_DoPD is implemented:

Halting step debug event pending. Possible values of this field are:

| SS   | Meaning                                                                                                                  |
|------|--------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Reading this means that a Halting step debug event is not pending. Writing this means no action.                         |
| 0b1  | Reading this means that a Halting step debug event is pending. Writing this clears the pending Halting step debug event. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Halting step debug event pending. Possible values of this field are:

| SS   | Meaning                                                                                                                  |
|------|--------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Reading this means that a Halting step debug event is not pending. Writing this means no action.                         |
| 0b1  | Reading this means that a Halting step debug event is pending. Writing this clears the pending Halting step debug event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to the value in EDECR.SS.

## RC, bit [1]

Reset Catch debug event pending. Possible values of this field are:

| RC   | Meaning                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Reading this means that a Reset Catch debug event is not pending. Writing this means no action.                        |
| 0b1  | Reading this means that a Reset Catch debug event is pending. Writing this clears the pending Reset Catch debug event. |

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_DoPD is implemented, this field resets to the value in CTIDEVCTL.RCE.
- When FEAT\_DoPD is not implemented, this field resets to the value in EDECR.RCE.

## OSUC, bit [0]

OS Unlock Catch debug event pending. Possible values of this field are:

| OSUC   | Meaning                                                                                                                         |
|--------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Reading this means that an OS Unlock Catch debug event is not pending. Writing this means no action.                            |
| 0b1    | Reading this means that an OS Unlock Catch debug event is pending. Writing this clears the pending OS Unlock Catch debug event. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing EDESR

If a request to clear a pending Halting debug event is received at or about the time when halting becomes allowed, it is CONSTRAINED UNPREDICTABLE whether the event is taken.

If Core power is removed while a Halting debug event is pending, it is lost. However, it might become pending again when the Core is powered back on and Cold reset.

EDESR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x020    | EDESR      |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.30 EDHSR, External Debug Halting Syndrome Register

The EDHSR characteristics are:

## Purpose

Holds syndrome information for a debug event.

## Configuration

EDHSR is in the Core power domain

The value of this register is UNKNOWN if the PE is in Non-debug state, or if EDSCR.STATUS is not 0b101011 .

This register is present only when FEAT\_EDHSR is implemented. Otherwise, direct accesses to EDHSR are RES0.

## Attributes

EDHSR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:41]

Reserved, RES0.

## GCS, bit [40]

## When FEAT\_GCS is implemented and FEAT\_Debugv8p9 is implemented:

Guarded control stack data access.

Indicates that the Watchpoint debug event is due to a Guarded control stack data access.

| GCS   | Meaning                                                                       |
|-------|-------------------------------------------------------------------------------|
| 0b0   | The Watchpoint debug event is not due to a Guarded control stack data access. |
| 0b1   | The Watchpoint debug event is due to a Guarded control stack data access.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [39:24]

Reserved, RES0.

## WPT, bits [23:18]

Watchpoint number. When EDHSR.WPTV is 1, holds the index of a watchpoint that triggered the Watchpoint debug event.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## WPTV, bit [17]

Watchpoint number valid.

| WPTV   | Meaning                                                                                                   | Applies when                      |
|--------|-----------------------------------------------------------------------------------------------------------|-----------------------------------|
| 0b0    | EDHSR.WPT field is not valid, and holds an UNKNOWN value.                                                 | FEAT_Debugv8p9 is not implemented |
| 0b1    | EDHSR.WPT field is valid, and holds the number of a watchpoint that triggered the Watchpoint debug event. |                                   |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## WPF, bit [16]

Watchpoint might be false-positive.

| WPF   | Meaning                                                                                                  | Applies when                                       |
|-------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 0b0   | The watchpoint matched an address or address range that was accessed by the instruction.                 |                                                    |
| 0b1   | The watchpoint matched an address or address range that might not have been accessed by the instruction. | FEAT_SVE is implemented or FEAT_SME is implemented |

Arm strongly recommends that this bit is set to 0, other than when one of the following instructions might generate a watchpoint match for an address or address range that the instruction does not access:

- An SVE contiguous vector load/store instruction, when the PE is in Streaming SVE mode.
- An SME load/store instruction.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FnP, bit [15]

EDWARnot Precise.

| FnP   | Meaning                                                                                                                                                                                                                        | Applies when                                       |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 0b0   | If the EDWARis valid, it holds the virtual address of an access or sequence of contiguous accesses that triggered the Watchpoint debug event.                                                                                  |                                                    |
| 0b1   | If the EDWARis valid, it holds any virtual address within the smallest implemented translation granule that contains the virtual address of an access or set of contiguous accesses that triggered the Watchpoint debug event. | FEAT_SME is implemented or FEAT_SVE is implemented |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [14]

Reserved, RES0.

## VNCR, bit [13]

## When FEAT\_Debugv8p9 is implemented:

VNCR\_EL2 access. Indicates that the Watchpoint debug event came from use of VNCR\_EL2 register by EL1 code.

| VNCR   | Meaning                                                                          | Applies when            |
|--------|----------------------------------------------------------------------------------|-------------------------|
| 0b0    | The Watchpoint debug event was not generated by the use of VNCR_EL2 by EL1 code. |                         |
| 0b1    | The Watchpoint debug event was generated by the use of VNCR_EL2 by EL1 code.     | FEAT_NV2 is implemented |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [12:11]

Reserved, RES0.

## FnV, bit [10]

EDWARnot Valid.

| FnV   | Meaning                                        | Applies when                                       |
|-------|------------------------------------------------|----------------------------------------------------|
| 0b0   | EDWARis valid.                                 |                                                    |
| 0b1   | EDWARis not valid, and holds an UNKNOWN value. | FEAT_SME is implemented or FEAT_SVE is implemented |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## CM, bit [8]

## When FEAT\_Debugv8p9 is implemented:

Cache maintenance. Indicates whether the Watchpoint debug event came from a cache maintenance instruction.

| CM   | Meaning                                                                                                                                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | The Watchpoint debug event was not generated by the execution of one of the System instructions identified in the description of value 1.                                                                                            |
| 0b1  | The Watchpoint debug event was generated by the execution of a cache maintenance instruction. The DCZVA, DCGVA, and DCGZVAinstructions are not cache maintenance instructions, and therefore do not cause this field to be set to 1. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## WnR, bit [6]

## When FEAT\_Debugv8p9 is implemented:

Write not Read. Indicates whether the Watchpoint debug event was caused by an instruction writing to a memory location, or by an instruction reading from a memory location.

| WnR   | Meaning                                                                         |
|-------|---------------------------------------------------------------------------------|
| 0b0   | Watchpoint debug event caused by an instruction reading from a memory location. |
| 0b1   | Watchpoint debug event caused by an instruction writing to a memory location.   |

For Watchpoint debug events on cache maintenance instructions, this field is set to 1.

For Watchpoint debug events from an atomic instruction, this field is set to 0 if a read of the location would have generated the Watchpoint debug event, otherwise it is set to 1.

If multiple watchpoints match on the same access, it is UNPREDICTABLE which watchpoint generates the Watchpoint debug event.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [5:0]

Reserved, RES0.

## Accessing EDHSR

EDHSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x038    | EDHSR      |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.31 EDITCTRL, External Debug Integration mode Control register

The EDITCTRL characteristics are:

## Purpose

Enables the external debug to switch from its default mode into integration mode, where test software can control directly the inputs and outputs of the PE, for integration testing or topology detection.

## Configuration

The power domain of EDITCTRL is IMPLEMENTATION DEFINED

Implementation of this register is OPTIONAL.

## Attributes

EDITCTRL is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 1 0   |
|------|-------|

## Bits [31:1]

Reserved, RES0.

## IME, bit [0]

Integration mode enable. When IME == 1, the device reverts to an integration mode to enable integration testing or topology detection.

| IME   | Meaning                   |
|-------|---------------------------|
| 0b0   | Normal operation.         |
| 0b1   | Integration mode enabled. |

The integration mode behavior is IMPLEMENTATION DEFINED.

The following resets apply:

- Whichever power domain the register is implemented in, this field resets to 0.
- Otherwise, the value of this field is unchanged.

## Accessing EDITCTRL

EDITCTRL can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xF00    | EDITCTRL   |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register are IMPLEMENTATION DEFINED.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.32 EDITR, External Debug Instruction Transfer Register

The EDITR characteristics are:

## Purpose

Used in Debug state for passing instructions to the PE for execution.

## Configuration

EDITR is in the Core power domain

## Attributes

EDITR is a 32-bit register.

## Field descriptions

When FEAT\_AA32 is implemented and in AArch32 state:

hw2

31

16

hw1

15

0

<!-- image -->

## hw2, bits [31:16]

Second halfword of the T32 instruction to be executed on the PE. When EDITR contains a 16-bit T32 instruction, this field is ignored. For more information, see 'Behavior in Debug state'.

Note

The hw2 field is displayed on the left. This is not the usual convention for display of T32 instruction halfwords.

## hw1, bits [15:0]

First halfword of the T32 instruction to be executed on the PE.

Note

The hw1 field is displayed on the right. This is not the usual convention for display of T32 instruction halfwords.

When FEAT\_AA64 is implemented and in AArch64 state:

<!-- image -->

## A64\_Instruction, bits [31:0]

A64 instruction to be executed on the PE.

## Accessing EDITR

If EDSCR.ITE == 0 when the PE exits Debug state on receiving a Restart request trigger event, the behavior of any instruction issued through the ITR in Normal access mode that has not completed execution is CONSTRAINED UNPREDICTABLE, and must do one of the following:

- It must complete execution in Debug state before the PE executes the restart sequence.
- It must complete execution in Non-debug state before the PE executes the restart sequence.

- It must be abandoned. This means that the instruction does not execute. Any registers or memory accessed by the instruction are left in an UNKNOWN state.

EDITR ignores writes if the PE is in Non-debug state.

EDITR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x084    | EDITR      |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

## H9.2.33 EDLAR, External Debug Lock Access Register

The EDLAR characteristics are:

## Purpose

Allows or disallows access to the external debug registers through a memory-mapped interface.

The optional Software Lock provides a lock to prevent memory-mapped writes to the debug registers. Use of this lock mechanism reduces the risk of accidental damage to the contents of the debug registers. It does not, and cannot, prevent all accidental or malicious damage.

## Configuration

When FEAT\_DoPD is implemented, EDLAR is in the Core power domain. Otherwise, EDLAR is in the Debug power domain

If FEAT\_DoPD is implemented, Software Lock is not implemented by the architecturally-defined debug components of the PE.

Software uses EDLAR to set or clear the lock, and EDLSR to check the current status of the lock.

## Attributes

EDLARis a 32-bit register.

## Field descriptions

When Debug Software Lock is implemented:

KEY

31

0

## KEY, bits [31:0]

Lock Access control. Writing the key value 0xC5ACCE55 to this field unlocks the lock, enabling write accesses to this component's registers through a memory-mapped interface.

Writing any other value to this register locks the lock, disabling write accesses to this component's registers through a memory mapped interface.

## Otherwise:

<!-- image -->

Otherwise

## Bits [31:0]

Reserved, RES0.

## Accessing EDLAR

EDLARcan be accessed through the memory-mapped interface:

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are WO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFB0    | EDLAR      |

## H9.2.34 EDLSR, External Debug Lock Status Register

The EDLSR characteristics are:

## Purpose

Indicates the current status of the software lock for external debug registers.

The optional Software Lock provides a lock to prevent memory-mapped writes to the debug registers. Use of this lock mechanism reduces the risk of accidental damage to the contents of the debug registers. It does not, and cannot, prevent all accidental or malicious damage.

## Configuration

When FEAT\_DoPD is implemented, EDLSR is in the Core power domain. Otherwise, EDLSR is in the Debug power domain

If FEAT\_DoPD is implemented, Software Lock is not implemented by the architecturally-defined debug components of the PE.

Software uses EDLAR to set or clear the lock, and EDLSR to check the current status of the lock.

## Attributes

EDLSR is a 32-bit register.

## Field descriptions

| 31   | 3 2 1 0     |
|------|-------------|
| RES0 | nTT SLK SLI |

## Bits [31:3]

Reserved, RES0.

## nTT, bit [2]

Not thirty-two bit access required. RAZ.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SLK, bit [1]

## When Debug Software Lock is implemented:

Software Lock status for this component. For an access to LSR that is not a memory-mapped access, or when Software Lock is not implemented, this field is RES0.

For memory-mapped accesses when Software Lock is implemented, possible values of this field are:

| SLK   | Meaning                                                                                     |
|-------|---------------------------------------------------------------------------------------------|
| 0b0   | Lock clear. Writes are permitted to this component's registers.                             |
| 0b1   | Lock set. Writes to this component's registers are ignored, and reads have no side effects. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_DoPD is implemented, this field resets to '1' .
- On a External debug reset:
- When FEAT\_DoPD is not implemented, this field resets to '1' .

## Otherwise:

Reserved, RAZ.

## SLI, bit [0]

Software Lock implemented. For an access to LSR that is not a memory-mapped access, this field is RAZ.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SLI   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | Software Lock not implemented or not memory-mapped access. |
| 0b1   | Software Lock implemented and memory-mapped access.        |

Access to this field is RO.

## Accessing EDLSR

EDLSR can be accessed through the memory-mapped interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFB4    | EDLSR      |

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.35 EDPCSR, External Debug Program Counter Sample Register

The EDPCSR characteristics are:

## Purpose

Holds a sampled instruction address value.

## Configuration

EDPCSR is in the Core power domain

If FEAT\_Debugv8p1 is implemented, the format of this register differs depending on the value of EDSCR.SC2.

Note

FEAT\_PCSRv8p2 implements the PC Sample-based Profiling Extension in the Performance Monitors registers space.

This register is present only when FEAT\_PCSRv8 is implemented and FEAT\_PCSRv8p2 is not implemented. Otherwise, direct accesses to EDPCSR are RES0.

## Attributes

EDPCSR is a 64-bit register.

## Field descriptions

When FEAT\_Debugv8p1 is not implemented or EDSCR.SC2 == '0':

PC Sample high word, EDPCSRhi

63

32

PC Sample low word

31

0

<!-- image -->

## EDPCSRhi, bits [63:32]

PC Sample high word, EDPCSRhi. If EDVIDSR.HV == 0, then this field is RAZ, otherwise bits [63:32] of the sampled instruction address value. The translation regime that EDPCSR samples can be determined from EDVIDSR.{NS,E2,E3}.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## EDPCSRlo, bits [31:0]

PC Sample low word. EDPCSRlo, bits[31:0] of the sampled instruction address value.

EDPCSRlo reads as 0xFFFFFFFF when any of the following are true:

- The PE is in Debug state.
- PC Sample-based profiling is prohibited.

If a branch instruction has retired since the PE left reset state, then the first read of EDPCSR[31:0] is permitted but not required to return 0xFFFFFFFF .

EDPCSRlo reads as an UNKNOWN value when any of the following are true:

- The PE is in reset state.
- No branch instruction has retired since the PE left reset state, Debug state, or a state where PC Sample-based Profiling is prohibited.

- No branch instruction has retired since the last read of EDPCSR[31:0].

For the cases where a read of EDPCSR[31:0] returns 0xFFFFFFFF or an UNKNOWN value, the read has the side-effect of setting EDPCSRhi, EDCIDSR, and EDVIDSR to UNKNOWN values.

Otherwise, a read of EDPCSR[31:0] returns bits [31:0] of the sampled instruction address value and has the side-effect of indirectly writing to EDPCSRhi, EDCIDSR, and EDVIDSR. The translation regime that EDPCSR samples can be determined from EDVIDSR.{NS,E2,E3}.

For a read of EDPCSR[31:0] from the memory-mapped interface, if EDLSR.SLK == 1, meaning the OPTIONAL Software Lock is locked, then the side-effect of the access does not occur and EDPCSRhi, EDCIDSR, and EDVIDSR are unchanged.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_Debugv8p1 is implemented and EDSCR.SC2 == '1':

<!-- image -->

## NS, bit [63]

Non-secure state sample. Indicates the Security state that is associated with the most recent EDPCSR sample or, when it is read as a single atomic 64-bit read, the current EDPCSR sample. The translation regime that EDPCSR samples can be determined from EDPCSR.{NS,EL}.

If EL3 is not implemented, this bit indicates the Effective value of SCR.NS.

| NS   | Meaning                          |
|------|----------------------------------|
| 0b0  | Sample is from Secure state.     |
| 0b1  | Sample is from Non-secure state. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## EL, bits [62:61]

Exception level status sample. Indicates the Exception level that is associated with the most recent EDPCSR sample or, when it is read as a single atomic 64-bit read, the current EDPCSR sample. The translation regime that EDPCSR samples can be determined from EDPCSR.{NS,EL}.

| EL   | Meaning             |
|------|---------------------|
| 0b00 | Sample is from EL0. |
| 0b01 | Sample is from EL1. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [60:56]

Reserved, RES0.

## EDPCSRhi, bits [55:32]

PC Sample high word, EDPCSRhi. Bits [55:32] of the sampled instruction address value. The translation regime that EDPCSR samples can be determined from EDPCSR.{NS,EL}.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## EDPCSRlo, bits [31:0]

PC Sample low word. EDPCSRlo, bits[31:0] of the sampled instruction address value.

EDPCSRlo reads as 0xFFFFFFFF when any of the following are true:

- The PE is in Debug state.
- PC Sample-based profiling is prohibited.

If a branch instruction has retired since the PE left reset state, then the first read of EDPCSR[31:0] is permitted but not required to return 0xFFFFFFFF .

EDPCSRlo reads as an UNKNOWN value when any of the following are true:

- The PE is in reset state.
- No branch instruction has retired since the PE left reset state, Debug state, or a state where PC Sample-based Profiling is prohibited.
- No branch instruction has retired since the last read of EDPCSR[31:0].

For the cases where a read of EDPCSR[31:0] returns 0xFFFFFFFF or an UNKNOWN value, the read has the side-effect of setting EDPCSRhi, EDCIDSR, and EDVIDSR to UNKNOWN values.

Otherwise, a read of EDPCSR[31:0] returns bits [31:0] of the sampled instruction address value and has the side-effect of indirectly writing to EDPCSRhi, EDCIDSR, and EDVIDSR. The translation regime that EDPCSR samples can be determined from EDPCSR.{NS,EL}.

For a read of EDPCSR[31:0] from the memory-mapped interface, if EDLSR.SLK == 1, meaning the OPTIONAL Software Lock is locked, then the side-effect of the access does not occur and EDPCSRhi, EDCIDSR, and EDVIDSR are unchanged.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing EDPCSR

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'

EDPCSR[63:32] and EDPCSR[31:0] are accessed at 32-bit memory mapped addresses that are not contiguous.

EDPCSR can be accessed through the external debug interface:

| EL   | Meaning             |
|------|---------------------|
| 0b10 | Sample is from EL2. |
| 0b11 | Sample is from EL3. |

| Component   | Offset   | Instance   | Range   |
|-------------|----------|------------|---------|
| Debug       | 0x0A0    | EDPCSR     | 31:0    |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   | Range   |
|-------------|----------|------------|---------|
| Debug       | 0x0AC    | EDPCSR     | 63:32   |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.36 EDPFR, External Debug Processor Feature Register

The EDPFR characteristics are:

## Purpose

Provides information about implemented PE features.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

There are no configuration notes.

## Attributes

EDPFR is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      |         |         |         | 48    | 47   | 44 43   | 40 39   |      | 36 35   | 32   |
|---------|---------|---------|---------|-------|------|---------|---------|------|---------|------|
| UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | AMU   | AMU  | UNKNOWN | SEL2    | SEL2 | SVE     |      |
| 31      | 28 27   | 24 23   | 20      | 16 15 |      | 12 11   | 8 7     |      | 4 3     | 0    |
|         | UNKNOWN | GIC     | AdvSIMD | FP    | EL3  | EL2     |         | EL1  | EL0     |      |

## Bits [63:48]

Reserved, UNKNOWN.

## AMU,bits [47:44]

Indicates support for Activity Monitors Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AMU    | Meaning                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Activity Monitors Extension is not implemented.                                                                    |
| 0b0001 | FEAT_AMUv1 is implemented.                                                                                         |
| 0b0010 | FEAT_AMUv1p1 is implemented. As 0b0001 and adds support for virtualization of the activity monitor event counters. |

All other values are reserved.

FEAT\_AMUv1 implements the functionality identified by the value 0b0001 .

FEAT\_AMUv1p1 implements the functionality identified by the value 0b0010 .

In Armv8.0, the only permitted value is 0b0000 .

In Armv8.4, the permitted values are 0b0000 and 0b0001 .

From Armv8.6, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

Access to this field is RO.

## Bits [43:40]

Reserved, UNKNOWN.

## SEL2, bits [39:36]

Secure EL2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SEL2   | Meaning                        |
|--------|--------------------------------|
| 0b0000 | Secure EL2 is not implemented. |
| 0b0001 | Secure EL2 is implemented.     |

FEAT\_SEL2 implements the functionality identified by the value 0b0001

All other values are reserved.

Access to this field is RO.

## SVE, bits [35:32]

Scalable Vector Extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SVE    | Meaning                 |
|--------|-------------------------|
| 0b0000 | SVE is not implemented. |
| 0b0001 | SVE is implemented.     |

FEAT\_SVE implements the functionality identified by the value 0b0001 .

All other values are reserved.

Access to this field is RO.

## Bits [31:28]

Reserved, UNKNOWN.

## GIC, bits [27:24]

System register GIC interface support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GIC    | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b0000 | GIC CPU interface system registers not implemented.                                      |
| 0b0001 | System register interface to versions 3.0 and 4.0 of the GIC CPU interface is supported. |

0b0011

System register interface to version 4.1 of the GIC CPU interface is supported.

All other values are reserved.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.GIC. Access to this field is RO.

## AdvSIMD, bits [23:20]

Advanced SIMD.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AdvSIMD   | Meaning                                                                                                                                                                                                                                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | Advanced SIMD is implemented, including support for the following SISD and SIMD operations: • Integer byte, halfword, word and doubleword element operations. • Single-precision and double-precision floating-point arithmetic. • Conversions between single-precision and half-precision data types, and double-precision and half-precision data types. |
| 0b0001    | As for 0b0000 , and also includes support for half-precision floating-point arithmetic.                                                                                                                                                                                                                                                                    |
| 0b1111    | Advanced SIMD is not implemented.                                                                                                                                                                                                                                                                                                                          |

All other values are reserved.

This field must have the same value as the FP field.

The permitted values are:

- 0b0000 in an implementation with Advanced SIMD support, that does not include the FEAT\_FP16 extension.
- 0b0001 in an implementation with Advanced SIMD support, that includes the FEAT\_FP16 extension.
- 0b1111 in an implementation without Advanced SIMD support.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.AdvSIMD.

Access to this field is RO.

## FP, bits [19:16]

Floating-point.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FP     | Meaning                                                                                                                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Floating-point is implemented, and includes support for: • Single-precision and double-precision floating-point types. • Conversions between single-precision and half-precision data types, and double-precision and half-precision data types. |
| 0b0001 | As for 0b0000 , and also includes support for half-precision floating-point arithmetic.                                                                                                                                                          |

| FP     | Meaning                            |
|--------|------------------------------------|
| 0b1111 | Floating-point is not implemented. |

All other values are reserved.

This field must have the same value as the AdvSIMD field.

The permitted values are:

- 0b0000 in an implementation with floating-point support, that does not include the FEAT\_FP16 extension.
- 0b0001 in an implementation with floating-point support, that includes the FEAT\_FP16 extension.
- 0b1111 in an implementation without floating-point support.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.FP.

Access to this field is RO.

## EL3, bits [15:12]

AArch64 EL3 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL3    | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0000 | EL3 is not implemented or cannot be executed in AArch64 state. |
| 0b0001 | EL3 can be executed in AArch64 state only.                     |
| 0b0010 | EL3 can be executed in both Execution states.                  |

When the value of EDAA32PFR.EL3 is nonzero, this field must be 0b0000 .

All other values are reserved.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.EL3.

Access to this field is RO.

## EL2, bits [11:8]

AArch64 EL2 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL2    | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0000 | EL2 is not implemented or cannot be executed in AArch64 state. |
| 0b0001 | EL2 can be executed in AArch64 state only.                     |
| 0b0010 | EL2 can be executed in both Execution states.                  |

When the value of EDAA32PFR.EL2 is nonzero, this field must be 0b0000 .

All other values are reserved.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.EL2.

Access to this field is RO.

## EL1, bits [7:4]

AArch64 EL1 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL1    | Meaning                                                                             |
|--------|-------------------------------------------------------------------------------------|
| 0b0000 | EL1 cannot be executed in AArch64 state. EL1 can be executed in AArch32 state only. |
| 0b0001 | EL1 can be executed in AArch64 state only.                                          |
| 0b0010 | EL1 can be executed in both Execution states.                                       |

All other values are reserved.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.EL1. Access to this field is RO.

## EL0, bits [3:0]

AArch64 EL0 Exception level handling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EL0    | Meaning                                                                             |
|--------|-------------------------------------------------------------------------------------|
| 0b0000 | EL0 cannot be executed in AArch64 state. EL0 can be executed in AArch32 state only. |
| 0b0001 | EL0 can be executed in AArch64 state only.                                          |
| 0b0010 | EL0 can be executed in both Execution states.                                       |

All other values are reserved.

In an Armv8-A implementation that supports AArch64, this field returns the value of ID\_AA64PFR0\_EL1.EL0. Access to this field is RO.

## Accessing EDPFR

EDPFR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xD20    | EDPFR      |

Accessible as follows:

- When IsCorePowered() and !DoubleLockStatus(), accesses to this register are RO.
- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.

## H9.2.37 EDPIDR0, External Debug Peripheral Identification Register 0

The EDPIDR0 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDPIDR0 is in the Core power domain. Otherwise, EDPIDR0 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDPIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    |
|------|--------|
| RES0 | PART_0 |

## Bits [31:8]

Reserved, RES0.

## PART\_0, bits [7:0]

Part number, least significant byte.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDPIDR0

EDPIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFE0    | EDPIDR0    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.38 EDPIDR1, External Debug Peripheral Identification Register 1

The EDPIDR1 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDPIDR1 is in the Core power domain. Otherwise, EDPIDR1 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDPIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7 4 3      |
|------|--------------|
| RES0 | DES_0 PART_1 |

## Bits [31:8]

Reserved, RES0.

## DES\_0, bits [7:4]

Designer, least significant nibble of JEP106 ID code. For Arm Limited, this field is 0b1011 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## PART\_1, bits [3:0]

Part number, most significant nibble.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDPIDR1

EDPIDR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFE4    | EDPIDR1    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.39 EDPIDR2, External Debug Peripheral Identification Register 2

The EDPIDR2 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDPIDR2 is in the Core power domain. Otherwise, EDPIDR2 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDPIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## REVISION, bits [7:4]

Part major revision. Parts can also use this field to extend Part number to 16-bits.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## JEDEC, bit [3]

Indicates a JEP106 identity code is used.

Reads as 0b1

Access to this field is RO.

## DES\_1, bits [2:0]

Designer, most significant bits of JEP106 ID code. For Arm Limited, this field is 0b011 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDPIDR2

EDPIDR2 can be accessed through the external debug interface:

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFE8    | EDPIDR2    |

## H9.2.40 EDPIDR3, External Debug Peripheral Identification Register 3

The EDPIDR3 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDPIDR3 is in the Core power domain. Otherwise, EDPIDR3 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDPIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    | 4 3   |
|------|--------|-------|
| RES0 | REVAND | CMOD  |

## Bits [31:8]

Reserved, RES0.

## REVAND, bits [7:4]

Part minor revision. Parts using EDPIDR2.REVISION as an extension to the Part number must use this field as a major revision number.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CMOD,bits [3:0]

Customer modified. Indicates someone other than the Designer has modified the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDPIDR3

EDPIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFEC    | EDPIDR3    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.41 EDPIDR4, External Debug Peripheral Identification Register 4

The EDPIDR4 characteristics are:

## Purpose

Provides information to identify an external debug component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

When FEAT\_DoPD is implemented, EDPIDR4 is in the Core power domain. Otherwise, EDPIDR4 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

EDPIDR4 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SIZE, bits [7:4]

Size of the component. Log2 of the number of 4KB pages from the start of the component to the end of the component ID registers.

Reads as

0b0000

Access to this field is RO.

## DES\_2, bits [3:0]

Designer, JEP106 continuation code, least significant nibble. For Arm Limited, this field is 0b0100 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing EDPIDR4

EDPIDR4 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xFD0    | EDPIDR4    |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.42 EDPRCR, External Debug Power/Reset Control Register

The EDPRCR characteristics are:

## Purpose

Controls the PE functionality related to powerup, reset, and powerdown.

## Configuration

When FEAT\_DoPD is implemented, EDPRCR is in the Core power domain. Otherwise, EDPRCR contains fields that are in the Core power domain and fields that are in the Debug power domain

External register EDPRCR bit [0] is architecturally mapped to AArch64 System register DBGPRCR\_EL1[0].

External register EDPRCR bit [0] is architecturally mapped to AArch32 System register DBGPRCR[0].

## Attributes

EDPRCR is a 32-bit register.

## Field descriptions

When FEAT\_DoPD is implemented:

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## CWRR,bit [1]

## When FEAT\_RME is implemented:

Access to this field is RAZ/WI.

## Otherwise:

Warm reset request.

The extent of the reset is IMPLEMENTATION DEFINED, but must be one of:

- The request is ignored.
- Only this PE is Warm reset.
- This PE and other components of the system, possibly including other PEs, are Warm reset.

Arm deprecates use of this bit, and recommends that implementations ignore the request.

| CWRR   | Meaning             |
|--------|---------------------|
| 0b0    | No action.          |
| 0b1    | Request Warm reset. |

This field is in the Core power domain

In an implementation that includes the recommended external debug interface, this bit drives the DBGRSTREQ signal.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if any of the following are true:
- OSLockStatus()
- SoftwareLockStatus()
- Access to this field is RAZ/WI if all of the following are true:
- !ExternalSecureInvasiveDebugEnabled()
- FEAT\_Secure is implemented
- Access to this field is RAZ/WI if all of the following are true:
- !ExternalInvasiveDebugEnabled()
- FEAT\_Secure is not implemented
- Otherwise, access to this field is WO/RAZ.

## CORENPDRQ,bit [0]

Core no powerdown request. Requests emulation of powerdown.

This request is typically passed to an external power controller. This means that whether a request causes power up is dependent on the IMPLEMENTATION DEFINED nature of the system. The power controller must not allow the Core power domain to switch off while this bit is 1.

| CORENPDRQ   | Meaning                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If the system responds to a powerdown request, it powers down Core power domain.                                                             |
| 0b1         | If the system responds to a powerdown request, it does not powerdown the Core power domain, but instead emulates a powerdown of that domain. |

When this bit reads as UNKNOWN, the PE ignores writes to this bit.

This field is in the Core power domain, and permitted accesses to this field map to the DBGPRCR.CORENPDRQ and DBGPRCR\_EL1.CORENPDRQ fields.

In an implementation that includes the recommended external debug interface, this bit drives the DBGNOPWRDWN signal.

It is IMPLEMENTATION DEFINED whether this bit is reset to the Cold reset value on exit from an IMPLEMENTATION DEFINED software-visible retention state. For more information about retention states, see 'Core power domain power states'.

## Note

Writes to this bit are not prohibited by the IMPLEMENTATION DEFINED authentication interface. This means that a debugger can request emulation of powerdown regardless of whether invasive debug is permitted.

On a Cold reset, if the powerup request is implemented and the powerup request has been asserted, this field is an IMPLEMENTATION DEFINED choice of 0 or 1. If the powerup request is not asserted, this field is set to 0.

Accessing this field has the following behavior:

- When OSLockStatus(), access to this field is UNKNOWN/WI.
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RW.

## Otherwise:

<!-- image -->

## Bits [31:4]

Reserved, RES0.

## COREPURQ,bit [3]

Core powerup request. Allows a debugger to request that the power controller power up the core, enabling access to the debug register in the Core power domain, and that the power controller emulates powerdown.

This request is typically passed to an external power controller. This means that whether a request causes power up is dependent on the IMPLEMENTATION DEFINED nature of the system. The power controller must not allow the Core power domain to switch off while this bit is 1.

| COREPURQ   | Meaning                                                                |
|------------|------------------------------------------------------------------------|
| 0b0        | Do not request power up of the Core power domain.                      |
| 0b1        | Request power up of the Core power domain, and emulation of powerdown. |

In an implementation that includes the recommended external debug interface, this bit drives the DBGPWRUPREQ signal.

This field is in the Debug power domain and can be read and written when the Core power domain is powered off.

<!-- image -->

Writes to this bit are not prohibited by the IMPLEMENTATION DEFINED authentication interface. This means that a debugger can request emulation of powerdown regardless of whether invasive debug is permitted.

The reset behavior of this field is:

- On a External debug reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RW.

Bit [2]

Reserved, RES0.

## CWRR,bit [1]

## When FEAT\_RME is implemented:

Access to this field is RAZ/WI.

Otherwise:

Warm reset request.

The extent of the reset is IMPLEMENTATION DEFINED, but must be one of:

- The request is ignored.
- Only this PE is Warm reset.
- This PE and other components of the system, possibly including other PEs, are Warm reset.

Arm deprecates use of this bit, and recommends that implementations ignore the request.

| CWRR   | Meaning             |
|--------|---------------------|
| 0b0    | No action.          |
| 0b1    | Request Warm reset. |

This field is in the Core power domain

In an implementation that includes the recommended external debug interface, this bit drives the DBGRSTREQ signal.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if any of the following are true:
- !IsCorePowered()
- DoubleLockStatus()
- OSLockStatus()
- SoftwareLockStatus()
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_Secure is implemented
- !ExternalSecureInvasiveDebugEnabled()
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_Secure is not implemented
- !ExternalInvasiveDebugEnabled()
- Otherwise, access to this field is WO/RAZ.

## CORENPDRQ,bit [0]

Core no powerdown request. Requests emulation of powerdown.

This request is typically passed to an external power controller. This means that whether a request causes power up is dependent on the IMPLEMENTATION DEFINED nature of the system. The power controller must not allow the Core power domain to switch off while this bit is 1.

| CORENPDRQ   | Meaning                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | If the system responds to a powerdown request, it powers down Core power domain.                                                             |
| 0b1         | If the system responds to a powerdown request, it does not powerdown the Core power domain, but instead emulates a powerdown of that domain. |

When this bit reads as UNKNOWN, the PE ignores writes to this bit.

This field is in the Core power domain, and permitted accesses to this field map to the DBGPRCR.CORENPDRQ and DBGPRCR\_EL1.CORENPDRQ fields.

In an implementation that includes the recommended external debug interface, this bit drives the DBGNOPWRDWN signal.

It is IMPLEMENTATION DEFINED whether this bit is reset to the value of EDPRCR.COREPURQ on exit from an IMPLEMENTATION DEFINED software-visible retention state. For more information about retention states, see 'Core power domain power states'.

Note

Writes to this bit are not prohibited by the IMPLEMENTATION DEFINED authentication interface. This means that a debugger can request emulation of powerdown regardless of whether invasive debug is permitted.

The reset behavior of this field is:

- On a Cold reset, this field resets to the value in EDPRCR.COREPURQ.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- !IsCorePowered()
- DoubleLockStatus()
- OSLockStatus()
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RW.

## Accessing EDPRCR

On permitted accesses to the register, other access controls affect the behavior of some fields. See the field descriptions for more information.

EDPRCR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x310    | EDPRCR     |

Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.2.43 EDPRSR, External Debug Processor Status Register

The EDPRSR characteristics are:

## Purpose

Holds information about the reset and powerdown state of the PE.

## Configuration

When FEAT\_DoPD is implemented, EDPRSR is in the Core power domain. Otherwise, EDPRSR contains fields that are in the Core power domain and fields that are in the Debug power domain

If FEAT\_DoPD is implemented, then all fields in this register are in the Core power domain.

## Attributes

EDPRSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:17]

Reserved, RES0.

## EPMADE, bit [16]

## When FEAT\_RME is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable Extended status. Together with EDPRSR.EPMAD, reports whether access to Performance Monitor registers by an external debugger is prohibited by the MDCR\_EL3.{EPMAD, EPMADE} controls.

For a description of the values derived by evaluating EDPRSR.EPMAD and EDPRSR.EPMADE together, see EDPRSR.EPMAD.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## Otherwise:

Reserved, RES0.

ETADE, bit [15]

## When FEAT\_RME is implemented, FEAT\_TRC\_EXT is implemented, and FEAT\_TRBE is implemented:

External Trace Access Disable Extended status. Together with EDPRSR.ETAD, reports whether access to trace unit registers by an external debugger is prohibited by the MDCR\_EL3.{ETAD, ETADE} controls.

For a description of the values derived by evaluating EDPRSR.ETAD and EDPRSR.ETADE together, see EDPRSR.ETAD.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## Otherwise:

Reserved, RES0.

## EDADE, bit [14]

## When FEAT\_RME is implemented:

External Debug Access Disable Extended status. Together with EDPRSR.EDAD, reports whether access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger is prohibited by the MDCR\_EL3.{EDAD, EDADE} controls.

For a description of the values derived by evaluating EDPRSR.EDAD and EDPRSR.EDADE together, see EDPRSR.EDAD.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## Otherwise:

Reserved, RES0.

## STAD, bit [13]

## When FEAT\_TRC\_EXT is implemented and FEAT\_TRBE is implemented:

Sticky ETAD error. Set to 1 when a Non-secure external debug interface access to an external trace register returns an error because AllowExternalTraceAccess() == FALSE for the access.

| STAD   | Meaning                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Since EDPRSR was last read, no external accesses to the trace unit registers have failed because AllowExternalTraceAccess() was FALSE for the access.        |
| 0b1    | Since EDPRSR was last read, at least one external access to the trace unit registers has failed because AllowExternalTraceAccess() was FALSE for the access. |

If IsCorePowered() == TRUE, the Core power domain is powered up, then, following a read of EDPRSR, then this bit clears to 0.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- Otherwise, access to this field is RC/WI.

## Otherwise:

Reserved, RES0.

ETAD, bit [12]

## When FEAT\_RME is implemented, FEAT\_TRC\_EXT is implemented, and FEAT\_TRBE is implemented:

External Trace Access Disable status. Together with EDPRSR.ETADE, reports whether access to trace unit registers by an external debugger is prohibited by the MDCR\_EL3.{ETAD, ETADE} controls.

| ETADE   | ETAD   | Meaning                                                                                                                                                                                     |
|---------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | 0b0    | No accesses from an external debugger to trace unit registers are prohibited.                                                                                                               |
| 0b0     | 0b1    | Realm and Non-secure accesses from an external debugger to trace unit registers are prohibited. Other accesses from an external debugger to trace unit registers are not affected.          |
| 0b1     | 0b0    | Secure and Non-secure accesses from an external debugger to trace unit registers are prohibited. Other accesses from an external debugger to trace unit registers are not affected.         |
| 0b1     | 0b1    | Secure, Non-secure, and Realm accesses from an external debugger to trace unit registers are prohibited. Other accesses from an external debugger to trace unit registers are not affected. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## When FEAT\_TRC\_EXT is implemented and FEAT\_TRBE is implemented:

External Trace Access Disable status. Reports whether Non-secure access to trace unit registers by an external debugger is prohibited by the MDCR\_EL3.ETAD control.

| ETAD   | Meaning                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------|
| 0b0    | External Non-secure trace unit accesses not affected. AllowExternalTraceAccess() == TRUE for a Non-secure access.    |
| 0b1    | External Non-secure trace unit accesses are prohibited. AllowExternalTraceAccess() == FALSE for a Non-secure access. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## Otherwise:

Reserved, RES0.

## SDR, bit [11]

Sticky Debug Restart. Set to 1 when the PE exits Debug state.

| SDR   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE has not restarted since EDPRSR was last read. |
| 0b1   | The PE has restarted since EDPRSR was last read.     |

Note

If a reset occurs when the PE is in Debug state, the PE exits Debug state. SDR is UNKNOWN on Warm reset, meaning a debugger must also use the SR bit to determine whether the PE has left Debug state.

If the Core power domain is powered up, then following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether this bit clears to 0 or is unchanged.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RC/WI.

## SPMAD, bit [10]

## When FEAT\_Debugv8p4 is implemented and FEAT\_PMUv3\_EXT is implemented:

Sticky EPMAD error. Set to 1 if an external debug interface access to a Performance Monitors register returns an error because AllowExternalPMUAccess() == FALSE.

| SPMAD   | Meaning                                                                                                                                                                                                                     |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | No Non-secure external debug interface accesses to the external Performance Monitors registers have failed because AllowExternalPMUAccess() == FALSE for the access since EDPRSR was last read.                             |
| 0b1     | At least one Non-secure external debug interface access to the external Performance Monitors register has failed and returned an error because AllowExternalPMUAccess() == FALSE for the access since EDPRSR was last read. |

If the Core power domain is powered up, then following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether this bit clears to 0 or is unchanged.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RC/WI.

## When FEAT\_PMUv3\_EXT is implemented:

Sticky EPMAD error.

| SPMAD   | Meaning                                                                                                                                                                                   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | No external debug interface accesses to the Performance Monitors registers have failed because AllowExternalPMUAccess() == FALSE since EDPRSR was last read.                              |
| 0b1     | At least one external debug interface access to the Performance Monitors registers has failed and returned an error because AllowExternalPMUAccess() == FALSE since EDPRSR was last read. |

If the Core power domain is powered up, then, following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented, and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether this bit clears to 0 or is unchanged.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- When OSLockStatus(), access to this field is UNKNOWN/WI.
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RC/WI.

## Otherwise:

Reserved, RES0.

## EPMAD, bit [9]

## When FEAT\_RME is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable status. Together with EDPRSR.EPMADE, reports whether access to Performance Monitor registers by an external debugger is prohibited by the MDCR\_EL3.{EPMAD, EPMADE} controls.

See MDCR\_EL3.EPMAD for the list of affected external Performance Monitor registers.

| EPMADE   | EPMAD   | Meaning                                                                                                                                                                                                                         |
|----------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | 0b0     | No accesses from an external debugger to affected Performance Monitor registers are prohibited.                                                                                                                                 |
| 0b0      | 0b1     | Realm and Non-secure accesses from an external debugger to affected Performance Monitor registers are prohibited. Other accesses from an external debugger to affected Performance Monitor registers are not affected.          |
| 0b1      | 0b0     | Secure and Non-secure accesses from an external debugger to affected Performance Monitor registers are prohibited. Other accesses from an external debugger to affected Performance Monitor registers are not affected.         |
| 0b1      | 0b1     | Secure, Non-secure, and Realm accesses from an external debugger to affected Performance Monitor registers are prohibited. Other accesses from an external debugger to affected Performance Monitor registers are not affected. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## When FEAT\_Debugv8p4 is implemented and FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable status. Reports whether Non-secure access to Performance Monitor registers by an external debugger is prohibited by the MDCR\_EL3.EPMAD control.

See MDCR\_EL3.EPMAD for the list of affected external Performance Monitor registers.

| EPMAD   | Meaning                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | External Non-secure access to Performance Monitor registers not affected. AllowExternalPMUAccess() == TRUE for a Non-secure access.            |
| 0b1     | External Non-secure access to affected Performance Monitor registers is prohibited. AllowExternalPMUAccess() == FALSE for a Non-secure access. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## When FEAT\_PMUv3\_EXT is implemented:

External Performance Monitors Access Disable status. Reports whether access to Performance Monitor registers by an external debugger is prohibited by the MDCR\_EL3.EPMAD control.

See MDCR\_EL3.EPMAD for the list of affected external Performance Monitor registers.

| EPMAD   | Meaning                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------|
| 0b0     | External access to Performance Monitor registers not affected. AllowExternalPMUAccess() == TRUE.            |
| 0b1     | External access to affected Performance Monitor registers is prohibited. AllowExternalPMUAccess() == FALSE. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- When OSLockStatus(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## When FEAT\_PMUv3 is implemented:

Reserved, UNKNOWN.

## Otherwise:

Reserved, RES0.

## SDAD, bit [8]

## When FEAT\_Debugv8p4 is implemented:

Sticky EDAD error. Set to 1 if an external debug interface access to a debug register returns an error because AllowExternalDebugAccess() == FALSE.

| SDAD   | Meaning                                                                                                                                                                                                |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No Non-secure external debug interface accesses to the debug registers have failed because AllowExternalDebugAccess() == FALSE for the access since EDPRSR was last read.                              |
| 0b1    | At least one Non-secure external debug interface access to the debug registers has failed and returned an error because AllowExternalDebugAccess() == FALSE for the access since EDPRSR was last read. |

If the Core power domain is powered up, then, following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether this bit clears to 0 or is unchanged.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## Otherwise:

Sticky EDAD error. Set to 1 if an external debug interface access to a debug register returns an error because AllowExternalDebugAccess() == FALSE.

| SDAD   | Meaning                                                                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No external debug interface accesses to the debug registers have failed because AllowExternalDebugAccess() == FALSE since EDPRSR was last read.                              |
| 0b1    | At least one external debug interface access to the debug registers has failed and returned an error because AllowExternalDebugAccess() == FALSE since EDPRSR was last read. |

If the Core power domain is powered up, then, following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether this bit clears to 0 or is unchanged.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()

- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Access to this field is UNKNOWN/WI if all of the following are true:
- OSLockStatus()
- external debug writes to OSLAR\_EL1 do not return an error when AllowExternalDebugAccess(addrdesc) == FALSE
- Otherwise, access to this field is RO.

## EDAD, bit [7]

## When FEAT\_RME is implemented:

External Debug Access Disable status. Together with EDPRSR.EDADE, reports whether access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger is prohibited by the MDCR\_EL3.{EDAD, EDADE} controls.

See MDCR\_EL3.EDAD for the list of affected external debug registers.

| EDADE   | EDAD   | Meaning                                                                                                                                                                                             |
|---------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | 0b0    | No accesses from an external debugger to affected debug registers are prohibited.                                                                                                                   |
| 0b0     | 0b1    | Realm and Non-secure accesses from an external debugger to affected debug registers are prohibited. Other accesses from an external debugger to affected debug registers are not affected.          |
| 0b1     | 0b0    | Secure and Non-secure accesses from an external debugger to affected debug registers are prohibited. Other accesses from an external debugger to affected debug registers are not affected.         |
| 0b1     | 0b1    | Secure, Non-secure, and Realm accesses from an external debugger to affected debug registers are prohibited. Other accesses from an external debugger to affected debug registers are not affected. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- Otherwise, access to this field is RO.

## When FEAT\_Debugv8p4 is implemented:

External Debug Access Disable status. Reports whether Non-secure access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger is prohibited by the MDCR\_EL3.EDAD control.

See MDCR\_EL3.EDAD for the list of affected external debug registers.

| EDAD   | Meaning                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | External Non-secure access to debug registers not affected. AllowExternalDebugAccess() ==TRUE for a Non-secure access.             |
| 0b1    | External Non-secure access to affected debug registers is prohibited. AllowExternalDebugAccess() == FALSE for a Non-secure access. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## When FEAT\_Debugv8p2 is implemented:

External Debug Access Disable status. Reports whether access to breakpoint registers, watchpoint registers, and OSLAR\_EL1 by an external debugger is prohibited by the MDCR\_EL3.EDAD control.

See MDCR\_EL3.EDAD for the list of affected external debug registers.

| EDAD   | Meaning                                                                                         |
|--------|-------------------------------------------------------------------------------------------------|
| 0b0    | External access to debug registers not affected. AllowExternalDebugAccess() == TRUE.            |
| 0b1    | External access to affected debug registers is prohibited. AllowExternalDebugAccess() == FALSE. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Access to this field is UNKNOWN/WI if all of the following are true:
- OSLockStatus()
- external debug writes to OSLAR\_EL1 do not return an error when AllowExternalDebugAccess(addrdesc) == FALSE
- Otherwise, access to this field is RO.

## Otherwise:

External Debug Access Disable status. Reports whether access to breakpoint registers, watchpoint registers, and optionally OSLAR\_EL1 by an external debugger is prohibited by the MDCR\_EL3.EDAD control.

See MDCR\_EL3.EDAD for the list of affected external debug registers.

| EDAD   | Meaning                                                                                         |
|--------|-------------------------------------------------------------------------------------------------|
| 0b0    | External access to debug registers not affected. AllowExternalDebugAccess() == TRUE.            |
| 0b1    | External access to affected debug registers is prohibited. AllowExternalDebugAccess() == FALSE. |

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()

## DLK, bit [6]

## When FEAT\_Debugv8p4 is implemented:

This field is RES0.

## When FEAT\_Debugv8p2 is implemented and FEAT\_DoubleLock is implemented:

Double Lock. From Armv8.2, use of this field is deprecated.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- !IsCorePowered()
- DoubleLockStatus()
- Otherwise, access to this field is RAZ/WI.

## When FEAT\_DoubleLock is implemented:

Double Lock.

This field returns the result of the pseudocode function DoubleLockStatus() .

If the Core power domain is powered up and DoubleLockStatus() == TRUE, it is IMPLEMENTATION DEFINED whether:

- EDPRSR.PU reads as 1, EDPRSR.DLK reads as 1, and EDPRSR.SPD is UNKNOWN.
- EDPRSR.PU reads as 0, EDPRSR.DLK is UNKNOWN, and EDPRSR.SPD reads as 0.

This field is in the Core power domain.

| DLK   | Meaning                                                                  |
|-------|--------------------------------------------------------------------------|
| 0b0   | DoubleLockStatus() returns FALSE.                                        |
| 0b1   | DoubleLockStatus() returns TRUE and the Core power domain is powered up. |

Accessing this field has the following behavior:

- When !IsCorePowered(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## Otherwise:

Reserved, RES0.

## OSLK, bit [5]

OS Lock status bit.

Aread of this bit returns the value of OSLSR\_EL1.OSLK.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

- !IsCorePowered()
- EDPRSR.R == '1'
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## HALTED, bit [4]

Halted status bit.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- Otherwise, access to this field is RO.

## SR, bit [3]

Sticky core Reset status bit.

| SR   | Meaning                                                                                                         |
|------|-----------------------------------------------------------------------------------------------------------------|
| 0b0  | The non-debug logic of the PE is not in reset state and has not been reset since the last time EDPRSR was read. |
| 0b1  | The non-debug logic of the PE is in reset state or has been reset since the last time EDPRSR was read.          |

If EDPRSR.PU reads as 1 and EDPRSR.R reads as 0, which means that the Core power domain is in a powerup state and that the non-debug logic of the PE is not in reset state, then following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented and DoubleLockStatus()

UNPREDICTABLE whether this bit clears to 0 or is unchanged.

This field is in the Core power domain.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- When DoubleLockStatus(), access to this field is UNKNOWN/WI.
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is RC/WI.
- == TRUE, it is CONSTRAINED

| HALTED   | Meaning                   |
|----------|---------------------------|
| 0b0      | PE is in Non-debug state. |
| 0b1      | PE is in Debug state.     |

## R, bit [2]

PE Reset status bit.

| R   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | The non-debug logic of the PE is not in reset state. |
| 0b1 | The non-debug logic of the PE is in reset state.     |

If FEAT\_DoubleLock is implemented, the PE is in reset state, and the PE entered reset state with the OS Double Lock locked this bit has a CONSTRAINED UNPREDICTABLE value. For more information, see 'EDPRSR.{DLK, R} and reset state'.

This field is in the Core power domain.

Accessing this field has the following behavior:

- Access to this field is UNKNOWN/WI if any of the following are true:
- All of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- DoubleLockStatus()
- Otherwise, access to this field is RO.

## SPD, bit [1]

Sticky core Powerdown status bit.

If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, then:

- If FEAT\_Debugv8p2 is implemented, this bit reads as 0.
- If FEAT\_Debugv8p2 is not implemented, this bit might read as 0 or 1.

For more information, see 'EDPRSR.{DLK, SPD, PU} and the Core power domain'.

| SPD   | Meaning                                                                                                                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If EDPRSR.PU is 0, it is not known whether the state of the debug registers in the Core power domain is lost. If EDPRSR.PU is 1, the state of the debug registers in the Core power domain has not been lost. |
| 0b1   | The state of the debug registers in the Core power domain has been lost.                                                                                                                                      |

If the Core power domain is powered up, then, following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, this bit clears to 0.
- If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether this bit clears to 0 or is unchanged.

EDPRSR.{DLK, SPD, PU} describe whether registers in the Core power domain can be accessed, and whether their state has been lost since the last time the register was read. For more information, see 'EDPRSR.{DLK, SPD, PU} and the Core power domain'.

When FEAT\_DoPD is not implemented and the Core power domain is in either retention or powerdown state, the value of EDPRSR.SPD is IMPLEMENTATION DEFINED. For more information, see 'EDPRSR.SPD when the Core domain is in either retention or powerdown state'.

The reset behavior of this field is:

- On a Cold reset, this field resets to '1' .

Accessing this field has the following behavior:

- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_DoPD is not implemented
- !IsCorePowered()
- Access to this field is UNKNOWN/WI if all of the following are true:
- IsCorePowered()
- DoubleLockStatus()
- Otherwise, access to this field is RC/WI.

PU, bit [0]

## When FEAT\_DoPD is implemented:

Core powerup status bit.

Access to this field is RAO/WI.

## When FEAT\_Debugv8p2 is implemented:

Core Powerup status bit. Indicates whether the debug registers in the Core power domain can be accessed.

| PU   | Meaning                                                                                                                                                                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Either the Core power domain is in a low-power or powerdown state, or FEAT_DoubleLock is implemented and DoubleLockStatus() == TRUE, meaning the debug registers in the Core power domain cannot be accessed. |
| 0b1  | The Core power domain is in a powerup state, and either FEAT_DoubleLock is not implemented or DoubleLockStatus() == FALSE, meaning the debug registers in the Core power domain can be accessed.              |

If FEAT\_DoubleLock is implemented, the PE is in reset state, and the PE entered reset state with the OS Double Lock locked this bit has a CONSTRAINED UNPREDICTABLE value. For more information, see 'EDPRSR.{DLK, R} and reset state'

EDPRSR.{DLK, SPD, PU} describe whether registers in the Core power domain can be accessed, and whether their state has been lost since the last time the register was read. For more information, see 'EDPRSR.{DLK, SPD, PU} and the Core power domain'

Access to this field is RO.

## Otherwise:

Core Powerup status bit. Indicates whether the debug registers in the Core power domain can be accessed.

| PU   | Meaning                                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Core power domain is in a low-power or powerdown state where the debug registers in the Core power domain cannot be accessed. |
| 0b1  | Core power domain is in a powerup state where the debug registers in the Core power domain can be accessed.                   |

If FEAT\_DoubleLock is implemented, the PE is in reset state, and the PE entered reset state with the OS Double Lock locked this bit has a CONSTRAINED UNPREDICTABLE value. For more information see 'EDPRSR.{DLK, R} and reset state'

EDPRSR.{DLK, SPD, PU} describe whether registers in the Core power domain can be accessed, and whether their state has been lost since the last time the register was read. For more information, see 'EDPRSR.{DLK, SPD, PU} and the Core power domain'.

When the Core power domain is powered-up and DoubleLockStatus() == TRUE, then the value of EDPRSR.PU is IMPLEMENTATION DEFINED. See the description of the DLK bit for more information.

If FEAT\_DoubleLock is implemented, the Core power domain is powered up, and DoubleLockStatus() == TRUE, it is IMPLEMENTATION DEFINED whether this bit reads as 0 or 1.

Access to this field is RO.

## Accessing EDPRSR

On permitted accesses to the register, other access controls affect the behavior of some fields. See the field descriptions for more information.

If the Core power domain is powered up (EDPRSR.PU == 1), then following a read of EDPRSR:

- If FEAT\_DoubleLock is not implemented or DoubleLockStatus() == FALSE, then:
- EDPRSR.{SDR, SPMAD, SDAD, SPD} are cleared to 0.
- EDPRSR.SR is cleared to 0 if the non-debug logic of the PE is not in reset state (EDPRSR.R == 0).
- If FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE, it is CONSTRAINED UNPREDICTABLE whether or not this clearing occurs.

If FEAT\_DoPD is not implemented and the Core power domain is powered down (EDPRSR.PU == 0), then:

- EDPRSR.{SDR, SPMAD, SDAD, SR} are all UNKNOWN, and are either reset or restored on being powered up.
- EDPRSR.SPD is not cleared following a read of EDPRSR. See the SPD bit description for more information.

The clearing of bits is an indirect write to EDPRSR.

EDPRSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x314    | EDPRSR     |

## Accessible as follows:

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.44 EDRCR, External Debug Reserve Control Register

The EDRCR characteristics are:

## Purpose

This register is used to allow imprecise entry to Debug state and clear sticky bits in EDSCR.

## Configuration

EDRCRis in the Core power domain

## Attributes

EDRCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:5]

Reserved, RES0.

## CBRRQ, bit [4]

Allow imprecise entry to Debug state. The actions on writing to this bit are:

| CBRRQ   | Meaning                                                                              |
|---------|--------------------------------------------------------------------------------------|
| 0b0     | No action.                                                                           |
| 0b1     | Allow imprecise entry to Debug state, for example by canceling pending bus accesses. |

Setting this bit to 1 allows a debugger to request imprecise entry to Debug state. An External Debug Request debug event must be pending before the debugger sets this bit to 1.

This feature is optional. If this feature is not implemented, writes to this bit are ignored.

## CSPA, bit [3]

Clear Sticky Pipeline Advance. This bit is used to clear the EDSCR.PipeAdv bit to 0. The actions on writing to this bit are:

| CSPA   | Meaning                           |
|--------|-----------------------------------|
| 0b0    | No action.                        |
| 0b1    | Clear the EDSCR.PipeAdv bit to 0. |

## CSE, bit [2]

Clear Sticky Error. Used to clear the EDSCR cumulative error bits to 0. The actions on writing to this bit are:

| CSE   | Meaning                                                                                          |
|-------|--------------------------------------------------------------------------------------------------|
| 0b0   | No action.                                                                                       |
| 0b1   | Clear the EDSCR.{TXU, RXO, ERR} bits, and, if the PE is in Debug state, the EDSCR.ITO bit, to 0. |

## Bits [1:0]

Reserved, RES0.

## Accessing EDRCR

EDRCRcan be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x090    | EDRCR      |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

## H9.2.45 EDSCR, External Debug Status and Control Register

The EDSCR characteristics are:

## Purpose

Main control register for the debug implementation.

## Configuration

EDSCR is in the Core power domain

When FEAT\_AA64 is implemented, External register EDSCR bits [31:29, 27:26, 23:21, 19, 14, 6] are architecturally mapped to AArch64 System register MDSCR\_EL1[31:29, 27:26, 23:21, 19, 14, 6].

External register EDSCR bits [31:29, 27:26, 23:21, 19, 14, 6] are architecturally mapped to AArch32 System register DBGDSCRext[31:29, 27:26, 23:21, 19, 14, 6].

When FEAT\_AA64 is implemented, External register EDSCR bits [30:29] are architecturally mapped to AArch64 System register MDCCSR\_EL0[30:29].

External register EDSCR bits [30:29] are architecturally mapped to AArch32 System register DBGDSCRint[30:29].

## Attributes

EDSCR is a 32-bit register.

## Field descriptions

<!-- image -->

## TFO, bit [31]

## When FEAT\_TRF is implemented:

Trace Filter Override. Overrides the Trace Filter controls allowing the external debugger to trace any visible Exception level.

| TFO   | Meaning                                                                                                           |
|-------|-------------------------------------------------------------------------------------------------------------------|
| 0b0   | Trace Filter controls are not affected.                                                                           |
| 0b1   | Trace Filter controls in TRFCR_EL1 and TRFCR_EL2 are ignored. Trace Filter controls TRFCR and HTRFCR are ignored. |

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

This bit is ignored by the PE when any of the following is true:

- ExternalSecureNoninvasiveDebugEnabled() is FALSE and the Effective value of MDCR\_EL3.STE is 1.
- FEAT\_RME is implemented, ExternalRealmNoninvasiveDebugEnabled() is FALSE, and the Effective value of MDCR\_EL3.RLTE is 1.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## RXfull, bit [30]

DTRRXfull.

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is RO.

## TXfull, bit [29]

DTRTX full.

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is RO.

## ITO, bit [28]

ITR overrun. Set to 0 on entry to Debug state.

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## RXO, bit [27]

DTRRXoverrun.

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is RO.

## TXU, bit [26]

DTRTX underrun.

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is RO.

## PipeAdv, bit [25]

Pipeline Advance. Indicates that software execution is progressing.

| PipeAdv   | Meaning                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------|
| 0b0       | No progress has been made by the PE since the last time this field was cleared to zero by writing 1 to EDRCR.CSPA. |
| 0b1       | Progress has been made by the PE since the last time this field was cleared to zero by writing 1 to EDRCR.CSPA.    |

The architecture does not define precisely when this field is set to 1. It requires only that this happen periodically in Non-debug state to indicate that software execution is progressing. For example, a PE might set this field to 1 each time the PE retires one or more instructions, or at periodic intervals during the progression of an instruction.

When FEAT\_MOPS is implemented, CPY , CPYF , SET , and SETG are examples of instructions that periodically make forward progress.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## ITE, bit [24]

ITR empty.

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## INTdis, bits [23:22]

## When FEAT\_RME is implemented:

Interrupt and SError exception disable. Disables taking interrupts and SError exceptions in Non-debug state.

| INTdis   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00     | This bit has no effect on the masking of interrupts and SError exceptions.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0b01     | If ExternalInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Non-secure state are masked. If ExternalSecureInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Secure state are masked. If ExternalRootInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Root state are masked. If ExternalRealmInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Realm state are masked. |

Note

This control affects both physical and virtual interrupts and SError exceptions.

When OSLSR\_EL1.OSLK is 1, this field can be indirectly read and written through the following System registers:

- MDSCR\_EL1.
- DBGDSCRext.

The Effective value of this field is 0b00 when ExternalInvasiveDebugEnabled() is FALSE.

When FEAT\_RME is implemented, bit[23] of this register is RES0.

The reset behavior of this field is:

- On a Cold reset, this field resets to '00' .

## When FEAT\_Debugv8p4 is implemented:

Interrupt and SError exception disable. Disables taking interrupts and SError exceptions in Non-debug state.

| INTdis   | Meaning                                                                                                                                                                                                                                                 |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00     | Masking of interrupts and SError exceptions is controlled by PSTATE and interrupt routing controls.                                                                                                                                                     |
| 0b01     | If ExternalInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Non-secure state are masked. If ExternalSecureInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Secure state are masked. |

Note

This control affects both physical and virtual interrupts and SError exceptions.

When OSLSR\_EL1.OSLK is 1, this field can be indirectly read and written through the following System registers:

- MDSCR\_EL1.
- DBGDSCRext.

The Effective value of this field is 0b00 when ExternalInvasiveDebugEnabled() is FALSE.

When FEAT\_Debugv8p4 is implemented, bit[23] of this register is RES0.

The reset behavior of this field is:

- On a Cold reset, this field resets to '00' .

## Otherwise:

Interrupt and SError exception disable. Disables taking interrupts and SError exceptions in Non-debug state.

| INTdis   | Meaning                                                                                                                                                                                                                                                 |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00     | Masking of interrupts and SError exceptions is controlled by PSTATE and interrupt routing controls.                                                                                                                                                     |
| 0b01     | If ExternalInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Non-secure EL1 are masked.                                                                                                                                |
| 0b10     | If ExternalInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Non-secure state are masked. If ExternalSecureInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Secure EL1 are masked.   |
| 0b11     | If ExternalInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Non-secure state are masked. If ExternalSecureInvasiveDebugEnabled() is TRUE, then all interrupts and SError exceptions taken to Secure state are masked. |

Note

This control affects both physical and virtual interrupts and SError exceptions.

When OSLSR\_EL1.OSLK is 1, this field can be indirectly read and written through the following System registers:

- MDSCR\_EL1.
- DBGDSCRext.

The Effective value of this field is 0b00 when ExternalInvasiveDebugEnabled() is FALSE.

Support for the values 0b01 and 0b10 is IMPLEMENTATION DEFINED. If these values are not supported, they are reserved. If programmed with a reserved value, the PE behaves as if EDSCR.INTdis has been programmed with a defined value, other than for a direct read of EDSCR, and the value returned by a read of EDSCR.INTdis is UNKNOWN.

The reset behavior of this field is:

- On a Cold reset, this field resets to '00' .

## TDA, bit [21]

Traps accesses to the following debug System registers:

- AArch64: DBGBCR&lt;n&gt;\_EL1, DBGBVR&lt;n&gt;\_EL1, DBGWCR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1.
- AArch32: DBGBCR&lt;n&gt;, DBGBVR&lt;n&gt;, DBGBXVR&lt;n&gt;, DBGWCR&lt;n&gt;, DBGWVR&lt;n&gt;.

| TDA   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses to debug System registers do not generate a Software Access Debug event.                                            |
| 0b1   | Accesses to debug System registers generate a Software Access Debug event, if OSLSR_EL1.OSLK is 0 and if halting is allowed. |

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## MA, bit [20]

Memory access mode. Controls the use of Memory access mode for accessing ITR and the DCC. This bit is ignored if in Non-debug state and set to zero on entry to Debug state.

Possible values of this field are:

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

SC2, bit [19]

| MA   | Meaning             |
|------|---------------------|
| 0b0  | Normal access mode. |
| 0b1  | Memory access mode. |

## When FEAT\_PCSRv8 is implemented, EL2 is implemented, FEAT\_Debugv8p1 is implemented, and FEAT\_PCSRv8p2 is not implemented:

Sample CONTEXTIDR\_EL2. Controls whether the PC Sample-based Profiling Extension samples CONTEXTIDR\_EL2 or VTTBR\_EL2.VMID.

| SC2   | Meaning                |
|-------|------------------------|
| 0b0   | Sample VTTBR_EL2.VMID. |
| 0b1   | Sample CONTEXTIDR_EL2. |

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

NS, bit [18]

## When FEAT\_RME is implemented:

Non-secure status. Together with the NSE field, gives the current Security state:

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## Otherwise:

Non-secure status. In Debug state, gives the current Security state:

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is UNKNOWN/WI.

- Otherwise, access to this field is RO.

## Bit [17]

Reserved, RES0.

## SDD, bit [16]

## When FEAT\_RME is implemented:

EL3 debug disabled.

On entry to Debug state:

- If entering from EL3, SDD is set to 0.
- Otherwise, SDD is set to the inverse of ExternalRootInvasiveDebugEnabled() .

In Debug state, the value of SDD does not change, even if ExternalRootInvasiveDebugEnabled() changes.

In Non-debug state, SDD returns the inverse of ExternalRootInvasiveDebugEnabled() .

Access to this field is RO.

## Otherwise:

Secure debug disabled.

On entry to Debug state:

- If entering in Secure state, SDD is set to 0.
- If entering in Non-secure state, SDD is set to the inverse of ExternalSecureInvasiveDebugEnabled() .

## In Debug state, the value of the SDD bit does not change, even if

ExternalSecureInvasiveDebugEnabled() changes.

In Non-debug state:

- SDDreturns the inverse of ExternalSecureInvasiveDebugEnabled() . If the authentication signals that control ExternalSecureInvasiveDebugEnabled() change, a context synchronization event is required to guarantee their effect.
- This bit is unaffected by the Security state of the PE.

If EL3 is not implemented and the implementation is Non-secure, this bit is RES1.

Access to this field is RO.

## NSE, bit [15]

## When FEAT\_RME is implemented:

Together with the NS field, this field gives the current Security state.

For a description of the values derived by evaluating NS and NSE together, see EDSCR.NS.

In Non-debug state, this bit is UNKNOWN.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## HDE, bit [14]

Halting debug enable.

| HDE   | Meaning                                                                        |
|-------|--------------------------------------------------------------------------------|
| 0b0   | Halting disabled for Breakpoint, Watchpoint and Halt Instruction debug events. |
| 0b1   | Halting enabled for Breakpoint, Watchpoint and Halt Instruction debug events.  |

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## RW, bits [13:10]

Exception level Execution state status. In Debug state, each bit gives the current Execution state of each Exception level.

| RW     | Meaning                                                                                                                                                                                                                            | Applies when                                    |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| 0b1111 | Any of the following: • The PE is in Non-debug state. • The PE is at EL0 using AArch64. • The PE is not at EL0, and EL1 is using AArch64. If implemented and enabled in the current Security state, EL2 and EL3 are using AArch64. |                                                 |
| 0b1110 | The PE is in Debug state at EL0. EL0 is using AArch32. EL1 is using AArch64. If implemented and enabled in the current Security state, EL2 and EL3 are using AArch64.                                                              | FEAT_AA32 is implemented                        |
| 0b110x | The PE is in Debug state. EL0 and EL1 are using AArch32. EL2 is enabled in the current Security state and is using AArch64. If implemented, EL3 is using AArch64.                                                                  | FEAT_AA32 is implemented and EL2 is implemented |
| 0b10xx | The PE is in Debug state. EL0 and EL1 are using AArch32. EL2 is not implemented, disabled in the current Security state, or using AArch32. EL3 is using AArch64.                                                                   | FEAT_AA32 is implemented and EL3 is implemented |
| 0b0xxx | The PE is in Debug state. All Exception levels are using AArch32.                                                                                                                                                                  | FEAT_AA32 is implemented                        |

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is RAO/WI.
- Otherwise, access to this field is RO.

## EL, bits [9:8]

Exception level. In Debug state, gives the current Exception level of the PE.

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is RAZ/WI.
- Otherwise, access to this field is RO.

## A, bit [7]

SError exception pending. In Debug state, indicates whether an SError exception is pending:

- If EL2 is enabled in the current Security state, the PE is executing at EL0 or EL1, HCR\_EL2.TGE is 0 and either HCR\_EL2.AMO is 1 or FEAT\_DoubleFault2 is implemented and the Effective value of HCRX\_EL2.TMEA is 1, a virtual SError exception.
- Otherwise, if FEAT\_E3DSE is implemented, the PE is executing at EL0, EL1, or EL2, and SCR\_EL3.EnDSE is 1, a delegated SError exception.
- Otherwise, a physical SError exception.

| A   | Meaning                      |
|-----|------------------------------|
| 0b0 | No SError exception pending. |
| 0b1 | SError exception pending.    |

Adebugger can read EDSCR to check whether an SError exception is pending without having to execute further instructions. A pending SError might indicate data from target memory is corrupted.

Accessing this field has the following behavior:

- When the PE is in Non-debug state, access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## ERR, bit [6]

Cumulative error flag. This bit is set to 1 following exceptions in Debug state and on any signaled overrun or underrun on the DTR or EDITR.

When OSLSR\_EL1.OSLK is 1, this bit can be indirectly read and written through MDSCR\_EL1 and DBGDSCRext.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

Access to this field is RO.

## STATUS, bits [5:0]

On entering Debug state, the PE sets this field to indicate the reason for halting.

| STATUS   | Meaning                                |
|----------|----------------------------------------|
| 0b000001 | PE is restarting, exiting Debug state. |
| 0b000010 | PE is in Non-debug state.              |
| 0b000111 | Breakpoint.                            |
| 0b010011 | External debug request.                |
| 0b011011 | Halting step, normal.                  |
| 0b011111 | Halting step, exclusive.               |
| 0b100011 | OS Unlock Catch.                       |
| 0b100111 | Reset Catch.                           |
| 0b101011 | Watchpoint.                            |

All other values are reserved.

The PE resets into Non-debug state. However, if the PE enters Debug state immediately after reset, then the reset value is overwritten with the reason for halting.

The reset behavior of this field is:

- On a Cold reset, this field resets to '000010' .

Access to this field is RO.

## Accessing EDSCR

EDSCR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x088    | EDSCR      |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| STATUS   | Meaning                            |
|----------|------------------------------------|
| 0b101111 | HLT instruction.                   |
| 0b110011 | Software access to debug register. |
| 0b110111 | Exception Catch.                   |
| 0b111011 | Halting step, no syndrome.         |

## H9.2.46 EDSCR2, External Debug Status and Control Register 2

The EDSCR2 characteristics are:

## Purpose

Main control register 2 for the debug implementation.

## Configuration

EDSCR2 is in the Core power domain

External register EDSCR2 bits [3, 1] are architecturally mapped to AArch64 System register MDSCR\_EL1[35, 33].

This register is present only when FEAT\_Debugv8p9 is implemented or FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to EDSCR2 are RES0.

## Attributes

EDSCR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:4]

Reserved, RES0.

## EHBWE,bit [3]

## When FEAT\_Debugv8p9 is implemented:

Extended Halting Breakpoint and Watchpoint Enable. Enables use of additional breakpoints or watchpoints.

| EHBWE   | Meaning                                                                                                                                                  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Halting disabled for Breakpoint and Watchpoint debug events generated by each breakpoint <n> and Watchpoint <n>, where n is greater than or equal to 16. |
| 0b1     | Breakpoints and Watchpoint debug events are not affected by this mechanism.                                                                              |

When OSLSR\_EL1.OSLK is 1, this field can be read and written through the MDSCR\_EL1 System register.

It is IMPLEMENTATION DEFINED whether this field is implemented or is RES0 when 16 or fewer breakpoints are implemented, 16 or fewer watchpoints are implemented, and MDSELR\_EL1 is implemented as RAZ/WI.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [2]

Reserved, RES0.

## TTA, bit [1]

## When FEAT\_TRBE\_EXT is implemented or FEAT\_ETEv1p3 is implemented:

Trap Trace Accesses.

Traps access to the following System registers:

AArch64: TRBBASER\_EL1, TRBIDR\_EL1, TRBLIMITR\_EL1, TRBMAR\_EL1, TRBMPAM\_EL1, TRBPTR\_EL1, TRBSR\_EL1, TRBTRG\_EL1, TRCACATR&lt;n&gt;, TRCACVR&lt;n&gt;, TRCAUTHSTATUS, TRCAUXCTLR, TRCBBCTLR, TRCCCCTLR, TRCCIDCCTLR0, TRCCIDCCTLR1, TRCCIDCVR&lt;n&gt;, TRCCLAIMCLR, TRCCLAIMSET, TRCCNTCTLR&lt;n&gt;, TRCCNTRLDVR&lt;n&gt;, TRCCNTVR&lt;n&gt;, TRCCONFIGR, TRCDEVARCH, TRCDEVID, TRCEVENTCTL0R, TRCEVENTCTL1R, TRCEXTINSELR&lt;n&gt;, TRCIDR0, TRCIDR1, TRCIDR2, TRCIDR3, TRCIDR4, TRCIDR5, TRCIDR6, TRCIDR7, TRCIDR8, TRCIDR9, TRCIDR10, TRCIDR11, TRCIDR12, TRCIDR13, TRCIMSPEC0, TRCIMSPEC&lt;n&gt;, TRCITEEDCR, TRCOSLSR, TRCPRGCTLR, TRCQCTLR, TRCRSCTLR&lt;n&gt;, TRCRSR, TRCSEQEVR&lt;n&gt;, TRCSEQRSTEVR, TRCSEQSTR, TRCSSCCR&lt;n&gt;, TRCSSCSR&lt;n&gt;, TRCSSPCICR&lt;n&gt;, TRCSTALLCTLR, TRCSTATR, TRCSYNCPR, TRCTRACEIDR, TRCTSCTLR, TRCVICTLR, TRCVIIECTLR, TRCVIPCSSCTLR, TRCVISSCTLR, TRCVMIDCCTLR0,

TRCVMIDCCTLR1, and TRCVMIDCVR&lt;n&gt;.

| TTA   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses to trace System registers do not generate a Software Access debug event.                                            |
| 0b1   | Accesses to trace System registers generate a Software Access debug event, if OSLSR_EL1.OSLK is 0 and if halting is allowed. |

When OSLSR\_EL1.OSLK is 1, this field can be read and written through the MDSCR\_EL1 System register.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bit [0]

Reserved, RES0.

## Accessing EDSCR2

EDSCR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x028    | EDSCR2     |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.2.47 EDVIDSR, External Debug Virtual Context Sample Register

The EDVIDSR characteristics are:

## Purpose

Contains sampled values captured on reading EDPCSR[31:0].

## Configuration

EDVIDSR is in the Core power domain

If FEAT\_Debugv8p1 is implemented, the format of this register differs depending on the value of EDSCR.SC2.

Implemented only if the OPTIONAL PC Sample-based Profiling Extension is implemented in the external debug registers space.

When FEAT\_PCSRv8 is implemented in the external debug registers space, if EL2 is not implemented and EL3 is not implemented, it is IMPLEMENTATION DEFINED whether EDVIDSR is implemented.

Note

FEAT\_PCSRv8p2 implements the FEAT\_PCSRv8 in the Performance Monitors registers space.

This register is present only when FEAT\_PCSRv8 is implemented and FEAT\_PCSRv8p2 is not implemented. Otherwise, direct accesses to EDVIDSR are RES0.

## Attributes

EDVIDSR is a 32-bit register.

## Field descriptions

When FEAT\_Debugv8p1 is not implemented or EDSCR.SC2 == '0':

<!-- image -->

| 31 30 29 28   | 16 15   | 8 7   |
|---------------|---------|-------|
| NS E2 E3 HV   | RES0    | VMID  |

This format applies in all Armv8.0 implementations.

## NS, bit [31]

Non-secure state sample. Indicates the Security state associated with the most recent EDPCSR sample.

If EL3 is not implemented, this bit indicates the Effective value of SCR.NS.

| NS   | Meaning                          |
|------|----------------------------------|
| 0b0  | Sample is from Secure state.     |
| 0b1  | Sample is from Non-secure state. |

The reset behavior of this field is:

· On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E2, bit [30]

## When EL2 is implemented:

Exception level 2 status sample. Indicates whether the most recent EDPCSR sample was associated with EL2.

| E2   | Meaning                 |
|------|-------------------------|
| 0b0  | Sample is not from EL2. |
| 0b1  | Sample is from EL2.     |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E3, bit [29]

## When EL3 is implemented and FEAT\_AA64 is implemented:

Exception level 3 status sample. Indicates whether the most recent EDPCSR sample was associated with EL3 using AArch64.

| E3   | Meaning                               |
|------|---------------------------------------|
| 0b0  | Sample is not from EL3 using AArch64. |
| 0b1  | Sample is from EL3 using AArch64.     |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HV, bit [28]

EDPCSRhi (EDPCSR[63:32]) valid. Indicates whether bits [63:32] of the most recent EDPCSR sample might be nonzero:

| HV   | Meaning                                                        |
|------|----------------------------------------------------------------|
| 0b0  | Bits[63:32] of the most recent EDPCSR sample are zero.         |
| 0b1  | Bits[63:32] of the most recent EDPCSR sample might be nonzero. |

An EDVIDSR.HV value of 1 does not mean that the value of EDPCSRhi is nonzero. An EDVIDSR.HV value of 0 is a hint that EDPCSRhi (EDPCSR[63:32]) does not need to be read.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:16]

Reserved, RES0.

## VMID[15:8], bits [15:8]

## When FEAT\_VMID16 is implemented and EL2 is implemented:

Extension to VMID[7:0]. For more information, see VMID[7:0].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VMID, bits [7:0]

## When EL2 is implemented:

VMIDsample. The VMID associated with the most recent EDPCSRlo (EDPCSR[31:0]) sample. When the most recent EDPCSR sample was generated:

- This field is RES0 if any of the following apply:
- The PE is executing in Secure state.
- The PE is executing at EL2.
- Otherwise:
- If EL2 is using AArch64 and either FEAT\_VMID16 is not implemented or VTCR\_EL2.VS is 1, this field is set to VTTBR\_EL2.VMID.
- If EL2 is using AArch64, FEAT\_VMID16 is implemented, and VTCR\_EL2.VS is 0, PMVIDSR.VMID[7:0] is set to VTTBR\_EL2.VMID[7:0] and PMVIDSR.VMID[15:8] is RES0.
- If EL2 is using AArch32, this field is set to VTTBR.VMID.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

When EL2 is implemented, FEAT\_Debugv8p1 is implemented, and EDSCR.SC2 == '1':

CONTEXTIDR\_EL2

31

0

## CONTEXTIDR\_EL2, bits [31:0]

Context ID. The value of CONTEXTIDR\_EL2 that is associated with the most recent EDPCSR sample. When the most recent EDPCSR sample is generated:

- If the PE is not executing at EL3, EL2 is using AArch64, and EL2 is enabled in the current Security state, then this field is set to the Context ID sampled from CONTEXTIDR\_EL2.
- Otherwise, this field is set to an UNKNOWN value.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing EDVIDSR

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

EDVIDSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x0A8    | EDVIDSR    |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.48 EDWAR, External Debug Watchpoint Address Register

The EDWAR characteristics are:

## Purpose

Returns the virtual data address being accessed when a Watchpoint Debug Event was triggered.

## Configuration

EDWARis in the Core power domain

The value of this register is UNKNOWN if the PE is in Non-debug state, or if EDSCR.STATUS is not 0b101011 .

## Attributes

EDWARis a 64-bit register.

## Field descriptions

<!-- image -->

| 63                 | 32   |
|--------------------|------|
| Watchpoint address |      |
| 31                 | 0    |

## ADDR, bits [63:0]

Watchpoint address. The data virtual address being accessed when a Watchpoint Debug Event was triggered and caused entry to Debug state. This address must be within a naturally-aligned block of memory of power-of-two size no larger than the DC ZV A block size.

The value of this register is UNKNOWN if the PE is in Non-debug state, or if Debug state was entered other than for a Watchpoint debug event.

The value of EDWAR[63:32] is UNKNOWN if Debug state was entered for a Watchpoint debug event taken from AArch32 state.

The EDWAR is subject to the same alignment rules as the reporting of a watchpointed address in the FAR. See 'Exception syndrome information and preferred return address'.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing EDWAR

EDWARcan be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x030    | EDWAR      |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.2.49 MIDR\_EL1, Main ID Register

The MIDR\_EL1 characteristics are:

## Purpose

Provides identification information for the PE, including an implementer code for the device and a device ID number.

## Configuration

The power domain of MIDR\_EL1 is IMPLEMENTATION DEFINED

External register MIDR\_EL1 bits [31:0] are architecturally mapped to AArch64 System register MIDR\_EL1[31:0].

External register MIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register MIDR[31:0].

## Attributes

MIDR\_EL1 is a 32-bit register.

## Field descriptions

| 31          | 24 23   | 20 19        | 16 15   | 4 3      | 0   |
|-------------|---------|--------------|---------|----------|-----|
| Implementer | Variant | Architecture |         | Revision |     |

## Implementer, bits [31:24]

The Implementer code. This field must hold an implementer code that has been assigned by Arm.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Implementer   | Meaning                                  |
|---------------|------------------------------------------|
| 0x00          | Reserved for software use.               |
| 0x41          | Arm Limited.                             |
| 0x42          | Broadcom Corporation.                    |
| 0x43          | Cavium Inc.                              |
| 0x44          | Digital Equipment Corporation.           |
| 0x46          | Fujitsu Ltd.                             |
| 0x49          | Infineon Technologies AG.                |
| 0x4D          | Motorola or Freescale Semiconductor Inc. |
| 0x4E          | NVIDIA Corporation.                      |
| 0x50          | Applied Micro Circuits Corporation.      |
| 0x51          | Qualcomm Inc.                            |
| 0x56          | Marvell International Ltd.               |
| 0x69          | Intel Corporation.                       |
| 0xC0          | Ampere Computing.                        |

Arm can assign codes that are not published in this manual. All values not assigned by Arm are reserved and must not be used.

Access to this field is RO.

## Variant, bits [23:20]

Variant number. Typically, this field is used to distinguish between different product variants, or major revisions of a product.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Architecture, bits [19:16]

Architecture version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Architecture   | Meaning                                                                   |
|----------------|---------------------------------------------------------------------------|
| 0b0001         | Armv4.                                                                    |
| 0b0010         | Armv4T.                                                                   |
| 0b0011         | Armv5 (obsolete).                                                         |
| 0b0100         | Armv5T.                                                                   |
| 0b0101         | Armv5TE.                                                                  |
| 0b0110         | Armv5TEJ.                                                                 |
| 0b0111         | Armv6.                                                                    |
| 0b1111         | Architectural features are individually identified in the ID_* registers. |

All other values are reserved.

Access to this field is RO.

## PartNum, bits [15:4]

Primary Part Number for the device.

On processors implemented by Arm, if the top four bits of the primary part number are 0x0 or 0x7 , the variant and architecture are encoded differently.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Revision, bits [3:0]

Revision number for the device.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing MIDR\_EL1

MIDR\_EL1 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register are IMPLEMENTATION DEFINED.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0xD00    | MIDR_EL1   |

## H9.2.50 OSLAR\_EL1, OS Lock Access Register

The OSLAR\_EL1 characteristics are:

## Purpose

Used to lock or unlock the OS Lock.

## Configuration

OSLAR\_EL1 is in the Core power domain

The OS Lock can also be locked or unlocked using DBGOSLAR.

If FEAT\_Debugv8p2 is not implemented, it is IMPLEMENTATION DEFINED whether external debug accesses to OSLAR\_EL1 are ignored and return an error when AllowExternalDebugAccess() returns FALSE for the access.

If FEAT\_Debugv8p2 is implemented, external debug accesses to OSLAR\_EL1 are ignored and return an error when AllowExternalDebugAccess() returns FALSE for the access.

External register OSLAR\_EL1 bits [31:0] are architecturally mapped to AArch64 System register OSLAR\_EL1[31:0].

## Attributes

OSLAR\_EL1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## OSLK, bit [0]

On writes to OSLAR\_EL1, bit[0] is copied to the OS Lock.

Use EDPRSR.OSLK to check the current status of the lock.

## Accessing OSLAR\_EL1

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalDebugAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

OSLAR\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| Debug       | 0x300    | OSLAR_EL1  |

Accessible as follows:

- When (DoubleLockStatus() || (!IsCorePowered())) || ((!AllowExternalDebugAccess(addrdesc)) &amp;&amp; IsFeatureImplemented(FEAT\_Debugv8p2)), accesses to this register return an ERROR.
- When AllowExternalDebugAccess(addrdesc) and SoftwareLockStatus(), accesses to this register are WI.
- When AllowExternalDebugAccess(addrdesc) and !SoftwareLockStatus(), accesses to this register are WO.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.