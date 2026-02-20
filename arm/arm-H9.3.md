## H9.3 External trace registers

This section lists the external Trace unit registers.

## H9.3.1 TRCACATR&lt;n&gt;, Trace Address Comparator Access Type Register &lt;n&gt;, n = 0 - 15

The TRCACATR&lt;n&gt; characteristics are:

## Purpose

Defines the type of access for the corresponding TRCACVR&lt;n&gt; Register. This register configures the context type, Exception levels, alignment, masking that is applied by the Address Comparator, and how the Address Comparator behaves when it is one half of an Address Range Comparator.

## Configuration

External register TRCACATR&lt;n&gt; bits [63:0] are architecturally mapped to AArch64 System register TRCACATR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and (UInt(TRCIDR4.NUMACPAIRS) * 2) &gt; n. Otherwise, direct accesses to TRCACATR&lt;n&gt; are RES0.

## Attributes

TRCACATR&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:19]

Reserved, RES0.

## EXLEVEL\_RL\_EL2, bit [18]

## When FEAT\_RME is implemented:

Realm EL2 address comparison control. Controls whether a comparison can occur at EL2 in Realm state.

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL2 is 0 the Address Comparator performs comparisons in Realm EL2. When TRCACATR<n>.EXLEVEL_NS_EL2 is 1 the Address Comparator does not perform comparisons in Realm EL2. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL2 is 0 the Address Comparator does not perform comparisons in Realm EL2. When TRCACATR<n>.EXLEVEL_NS_EL2 is 1 the Address Comparator performs comparisons in Realm EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL1, bit [17]

## When FEAT\_RME is implemented:

Realm EL1 address comparison control. Controls whether a comparison can occur at EL1 in Realm state.

| EXLEVEL_RL_EL1   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL1 is 0 the Address Comparator performs comparisons in Realm EL1. When TRCACATR<n>.EXLEVEL_NS_EL1 is 1 the Address Comparator does not perform comparisons in Realm EL1. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL1 is 0 the Address Comparator does not perform comparisons in Realm EL1. When TRCACATR<n>.EXLEVEL_NS_EL1 is 1 the Address Comparator performs comparisons in Realm EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL0, bit [16]

## When FEAT\_RME is implemented:

Realm EL0 address comparison control. Controls whether a comparison can occur at EL0 in Realm state.

| EXLEVEL_RL_EL0   | Meaning                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCACATR<n>.EXLEVEL_NS_EL0 is 0 the Address Comparator performs comparisons in Realm EL0. When TRCACATR<n>.EXLEVEL_NS_EL0 is 1 the Address Comparator does not perform comparisons in Realm EL0. |
| 0b1              | When TRCACATR<n>.EXLEVEL_NS_EL0 is 0 the Address Comparator does not perform comparisons in Realm EL0. When TRCACATR<n>.EXLEVEL_NS_EL0 is 1 the Address Comparator performs comparisons in Realm EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [15]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [14]

## When Non-secure EL2 is implemented:

Non-secure EL2 address comparison control. Controls whether a comparison can occur at EL2 in Non-secure state.

| EXLEVEL_NS_EL2   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL2.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL1, bit [13]

## When Non-secure EL1 is implemented:

Non-secure EL1 address comparison control. Controls whether a comparison can occur at EL1 in Non-secure state.

| EXLEVEL_NS_EL1   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL1.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL0, bit [12]

## When Non-secure EL0 is implemented:

Non-secure EL0 address comparison control. Controls whether a comparison can occur at EL0 in Non-secure state.

| EXLEVEL_NS_EL0   | Meaning                                                                |
|------------------|------------------------------------------------------------------------|
| 0b0              | The Address Comparator performs comparisons in Non-secure EL0.         |
| 0b1              | The Address Comparator does not perform comparisons in Non-secure EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL3, bit [11]

## When EL3 is implemented:

EL3 address comparison control. Controls whether a comparison can occur at EL3.

| EXLEVEL_S_EL3   | Meaning                                                     |
|-----------------|-------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons at EL3.         |
| 0b1             | The Address Comparator does not perform comparisons at EL3. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL2, bit [10]

## When Secure EL2 is implemented:

Secure EL2 address comparison control. Controls whether a comparison can occur at EL2 in Secure state.

| EXLEVEL_S_EL2   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL2.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL2. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL1, bit [9]

## When Secure EL1 is implemented:

Secure EL1 address comparison control. Controls whether a comparison can occur at EL1 in Secure state.

| EXLEVEL_S_EL1   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL1.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL1. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL0, bit [8]

## When Secure EL0 is implemented:

Secure EL0 address comparison control. Controls whether a comparison can occur at EL0 in Secure state.

| EXLEVEL_S_EL0   | Meaning                                                            |
|-----------------|--------------------------------------------------------------------|
| 0b0             | The Address Comparator performs comparisons in Secure EL0.         |
| 0b1             | The Address Comparator does not perform comparisons in Secure EL0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [7]

Reserved, RES0.

## CONTEXT, bits [6:4]

## When TRCIDR4.NUMCIDC != '0000' or TRCIDR4.NUMVMIDC != '0000':

Selects a Context Identifier Comparator or Virtual Context Identifier Comparator:

| CONTEXT   | Meaning       | Applies when                                            |
|-----------|---------------|---------------------------------------------------------|
| 0b000     | Comparator 0. |                                                         |
| 0b001     | Comparator 1. | UInt(TRCIDR4.NUMCIDC) > 1 or UInt(TRCIDR4.NUMVMIDC) > 1 |
| 0b010     | Comparator 2. | UInt(TRCIDR4.NUMCIDC) > 2 or UInt(TRCIDR4.NUMVMIDC) > 2 |
| 0b011     | Comparator 3. | UInt(TRCIDR4.NUMCIDC) > 3 or UInt(TRCIDR4.NUMVMIDC) > 3 |
| 0b100     | Comparator 4. | UInt(TRCIDR4.NUMCIDC) > 4 or UInt(TRCIDR4.NUMVMIDC) > 4 |
| 0b101     | Comparator 5. | UInt(TRCIDR4.NUMCIDC) > 5 or UInt(TRCIDR4.NUMVMIDC) > 5 |
| 0b110     | Comparator 6. | UInt(TRCIDR4.NUMCIDC) > 6 or UInt(TRCIDR4.NUMVMIDC) > 6 |
| 0b111     | Comparator 7. | UInt(TRCIDR4.NUMCIDC) > 7 or UInt(TRCIDR4.NUMVMIDC) > 7 |

The width of this field is dependent on the maximum number of Context Identifier Comparators or Virtual Context Identifier Comparators implemented. Unimplemented bits are RES0.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CONTEXTTYPE, bits [3:2]

## When TRCIDR4.NUMCIDC != '0000' or TRCIDR4.NUMVMIDC != '0000':

Controls whether the Address Comparator is dependent on a Context Identifier Comparator, a Virtual Context Identifier Comparator, or both comparisons.

| CONTEXTTYPE   | Meaning                                                                                                                                                                                                                                              | Applies when               |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| 0b00          | The Address Comparator is not dependent on the Context Identifier Comparators or Virtual Context Identifier Comparators.                                                                                                                             |                            |
| 0b01          | The Address Comparator is dependent on the Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if both the Context Identifier Comparator and the address comparison match.                 | TRCIDR4.NUMCIDC != '0000'  |
| 0b10          | The Address Comparator is dependent on the Virtual Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if both the Virtual Context Identifier Comparator and the address comparison match. | TRCIDR4.NUMVMIDC != '0000' |

| CONTEXTTYPE   | Meaning                                                                                                                                                                                                                                                                                                               | Applies when                                             |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b11          | The Address Comparator is dependent on the Context Identifier Comparator and Virtual Context Identifier Comparator that TRCACATR<n>.CONTEXT specifies. The Address Comparator signals a match only if the Context Identifier Comparator, the Virtual Context Identifier Comparator, and address comparison all match. | TRCIDR4.NUMCIDC != '0000' and TRCIDR4.NUMVMIDC != '0000' |

If TRCIDR4.NUMCIDC == 0b0000 , then bit [2] is RES0.

If TRCIDR4.NUMVMIDC == 0b0000 , then bit [3] is RES0.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [1:0]

Reserved, RES0.

## Accessing TRCACATR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCBBCTLR.RANGE[n/2] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0100 and TRCRSCTLR&lt;a&gt;.SAC[n] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0101 and TRCRSCTLR&lt;a&gt;.ARC[n/2] == 1.
- TRCVIIECTLR.EXCLUDE[n/2] == 1.
- TRCVIIECTLR.INCLUDE[n/2] == 1.
- TRCVISSCTLR.START[n] == 1.
- TRCVISSCTLR.STOP[n] == 1.
- TRCSSCCR&lt;&gt;.ARC[n/2] == 1.
- TRCSSCCR&lt;&gt;.SAC[n] == 1.
- TRCQCTLR.RANGE[n/2] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCACATR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance             |
|-------------|-----------------------------|
| ETE         | 0x480 + (8 * n) TRCACATR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.2 TRCACVR&lt;n&gt;, Trace Address Comparator Value Register &lt;n&gt;, n = 0 - 15

The TRCACVR&lt;n&gt; characteristics are:

## Purpose

Contains the address value.

## Configuration

External register TRCACVR&lt;n&gt; bits [63:0] are architecturally mapped to AArch64 System register TRCACVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and (UInt(TRCIDR4.NUMACPAIRS) * 2) &gt; n. Otherwise, direct accesses to TRCACVR&lt;n&gt; are RES0.

## Attributes

TRCACVR&lt;n&gt; is a 64-bit register.

## Field descriptions

ADDRESS

63

32

ADDRESS

31

0

<!-- image -->

## ADDRESS, bits [63:0]

Address Value.

The Address Comparators can support implementations that use multiple address widths. When the trace unit compares the ADDRESS field with an address that has a width less than this field, then the address must be zero-extended to the ADDRESS field width. The trace unit then compares all implemented bits. For example, in a system that supports both 32-bit and 64-bit addresses, when the PE is in AArch32 state the comparator must zero-extend the 32-bit address and compare against the full 64 bits that are stored in TRCACVR.ADDRESS. This requires that the trace analyzer always programs all implemented bits of TRCACVR.ADDRESS.

The result of writing a value other than all zeros or all ones to ADDRESS at bits[63:P] is an UNKNOWN value, where P is defined as:

- 56, when FEAT\_LVA3 is implemented.
- 52, when FEAT\_LVA is implemented.
- 48, otherwise.

The result of writing a value of all zeros or all ones to ADDRESS at bits[63:P] is the written value, and a read of the register returns the written value.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCACVR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCBBCTLR.RANGE[n/2] == 1. · TRCRSCTLR&lt;a&gt;.GROUP == 0b0100 and TRCRSCTLR&lt;a&gt;.SAC[n] == 1.
- TRCRSCTLR&lt;a&gt;.GROUP == 0b0101 and TRCRSCTLR&lt;a&gt;.ARC[n/2] == 1.
- TRCVIIECTLR.EXCLUDE[n/2] == 1.

- TRCVIIECTLR.INCLUDE[n/2] == 1.
- TRCVISSCTLR.START[n] == 1.
- TRCVISSCTLR.STOP[n] == 1.
- TRCSSCCR&lt;a&gt;.ARC[n/2] == 1.
- TRCSSCCR&lt;a&gt;.SAC[n] == 1.
- TRCQCTLR.RANGE[n/2] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCACVR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance            |
|-------------|----------------------------|
| ETE         | 0x400 + (8 * n) TRCACVR<n> |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.3 TRCAUTHSTATUS, Trace Authentication Status Register

The TRCAUTHSTATUS characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for debug.

For additional information, see the CoreSight Architecture Specification.

## Configuration

External register TRCAUTHSTATUS bits [31:0] are architecturally mapped to AArch64 System register TRCAUTHSTATUS[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCAUTHSTATUS are RES0.

## Attributes

TRCAUTHSTATUS is a 32-bit register.

## Field descriptions

| 31   | 28 27 26 25 24 23   | 6 5 4    | 15 14 13 12 11 10 9 8 7 3 2 1 0   |
|------|---------------------|----------|-----------------------------------|
| RES0 | RTNID RTID          | SNID SID | RLNID RLID HNID HID NSNID NSID    |

## Bits [31:28]

Reserved, RES0.

## RTNID, bits [27:26]

Root non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RTNID.

## RTID, bits [25:24]

Root invasive debug.

## Bits [23:16]

Reserved, RES0.

## RLNID, bits [15:14]

Realm non-invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RLNID.

## RLID, bits [13:12]

Realm invasive debug.

| RTID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

## HNID, bits [11:10]

Hyp Non-invasive Debug. Indicates whether a separate enable control for EL2 non-invasive debug features is implemented and enabled.

| HNID   | Meaning                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------|
| 0b00   | Separate Hyp non-invasive debug enable not implemented, or EL2 non-invasive debug features not implemented. |
| 0b10   | Implemented and disabled.                                                                                   |
| 0b11   | Implemented and enabled.                                                                                    |

All other values are reserved.

This field reads as 0b00 .

## HID, bits [9:8]

Hyp Invasive Debug. Indicates whether a separate enable control for EL2 invasive debug features is implemented and enabled.

| HID   | Meaning                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------|
| 0b00  | Separate Hyp invasive debug enable not implemented, or EL2 invasive debug features not implemented. |
| 0b10  | Implemented and disabled.                                                                           |
| 0b11  | Implemented and enabled.                                                                            |

All other values are reserved.

This field reads as 0b00 .

## SNID, bits [7:6]

Secure Non-invasive Debug. Indicates whether Secure non-invasive debug features are implemented and enabled.

| SNID   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b00   | Secure non-invasive debug features not implemented. |
| 0b10   | Implemented and disabled.                           |
| 0b11   | Implemented and enabled.                            |

All other values are reserved.

| RLID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

When Secure state is implemented, this field reads as 0b10 or 0b11 depending whether Secure non-invasive debug is enabled.

When Secure state is not implemented, this field reads as 0b00 .

## SID, bits [5:4]

Secure Invasive Debug. Indicates whether Secure invasive debug features are implemented and enabled.

| SID   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b00  | Secure invasive debug features not implemented. |
| 0b10  | Implemented and disabled.                       |
| 0b11  | Implemented and enabled.                        |

All other values are reserved.

This field reads as 0b00 .

## NSNID, bits [3:2]

Non-secure Non-invasive Debug. Indicates whether Non-secure non-invasive debug features are implemented and enabled.

| NSNID   | Meaning                                                 |
|---------|---------------------------------------------------------|
| 0b00    | Non-secure non-invasive debug features not implemented. |
| 0b10    | Implemented and disabled.                               |
| 0b11    | Implemented and enabled.                                |

All other values are reserved.

When Non-secure state is implemented, this field reads as 0b11 .

When Non-secure state is not implemented, this field reads as 0b00 .

## NSID, bits [1:0]

Non-secure Invasive Debug. Indicates whether Non-secure invasive debug features are implemented and enabled.

| NSID   | Meaning                                             |
|--------|-----------------------------------------------------|
| 0b00   | Non-secure invasive debug features not implemented. |
| 0b10   | Implemented and disabled.                           |
| 0b11   | Implemented and enabled.                            |

All other values are reserved.

This field reads as 0b00 .

## Accessing TRCAUTHSTATUS

For implementations that support multiple access mechanisms, different access mechanisms can return different values for reads of TRCAUTHSTATUS if the authentication signals have changed and that change has not yet been synchronized by a Context synchronization event. This scenario can happen if, for example, the external debugger view is implemented separately from the system instruction view to allow for separate power domains, and so observes changes on the signals differently.

External debugger accesses to this register are unaffected by the OS Lock.

TRCAUTHSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| ETE         | 0xFB8    | TRCAUTHSTATUS |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.4 TRCAUXCTLR, Trace Auxiliary Control Register

The TRCAUXCTLR characteristics are:

## Purpose

The function of this register is IMPLEMENTATION DEFINED.

## Configuration

External register TRCAUXCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCAUXCTLR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCAUXCTLR are RES0.

## Attributes

TRCAUXCTLRis a 32-bit register.

## Field descriptions

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

This field reads as an IMPLEMENTATION DEFINED value and writes to this field have IMPLEMENTATION DEFINED behavior.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to 0x00000000 .

## Accessing TRCAUXCTLR

If this register is nonzero then it might cause the behavior of a trace unit to contradict this architecture specification. See the documentation of the specific implementation for information about the IMPLEMENTATION DEFINED support for this register.

TRCAUXCTLRcan be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x018    | TRCAUXCTLR |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.5 TRCBBCTLR, Trace Branch Broadcast Control Register

The TRCBBCTLR characteristics are:

## Purpose

Controls the regions in the memory map where branch broadcasting is active.

## Configuration

External register TRCBBCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCBBCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, TRCIDR0.TRCBB == '1', and UInt(TRCIDR4.NUMACPAIRS) &gt; 0. Otherwise, direct accesses to TRCBBCTLR are RES0.

## Attributes

TRCBBCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:9]

Reserved, RES0.

## MODE,bit [8]

Mode.

| MODE   | Meaning                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Exclude Mode. Branch broadcasting is not active for instructions in the address ranges defined by TRCBBCTLR.RANGE. If TRCBBCTLR.RANGE == 0x00 then branch broadcasting is active for all instructions.                                                                                                                  |
| 0b1    | Include Mode. Branch broadcasting is active for instructions in the address ranges defined by TRCBBCTLR.RANGE. If TRCBBCTLR.RANGE == 0x00 then the behavior of the trace unit is CONSTRAINED UNPREDICTABLE. That is, the trace unit might or might not consider any instructions to be in a branch broadcasting region. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RANGE[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects whether Address Range Comparator &lt;m&gt; is used with branch broadcasting.

| RANGE[<m>]   | Meaning                                                                       |
|--------------|-------------------------------------------------------------------------------|
| 0b0          | The address range that Address Range Comparator <m> defines, is not selected. |
| 0b1          | The address range that Address Range Comparator <m> defines, is selected.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCBBCTLR

Must be programmed if TRCCONFIGR.BB == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCBBCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x03C    | TRCBBCTLR  |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.6 TRCCCCTLR, Trace Cycle Count Control Register

The TRCCCCTLR characteristics are:

## Purpose

Set the threshold value for cycle counting.

## Configuration

External register TRCCCCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCCCCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR0.TRCCCI == '1'. Otherwise, direct accesses to TRCCCCTLR are RES0.

## Attributes

TRCCCCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 12 11     |
|------|-----------|
| RES0 | THRESHOLD |

## Bits [31:12]

Reserved, RES0.

## THRESHOLD, bits [11:0]

Sets the threshold value for instruction trace cycle counting.

The minimum threshold value that can be programmed into THRESHOLD is given in TRCIDR3.CCITMIN. If the THRESHOLD value is smaller than the value in TRCIDR3.CCITMIN then the behavior is CONSTRAINED UNPREDICTABLE. That is, cycle counts might or might not be included in the trace and the cycle count threshold is not known.

Writing a value of zero when TRCCONFIGR.CCI enables instruction trace cycle counting results in CONSTRAINED UNPREDICTABLE behavior. That is, cycle counts might or might not be included in the trace and the cycle count threshold is not known.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCCCTLR

Must be programmed if TRCCONFIGR.CCI == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCCCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x038    | TRCCCCTLR  |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.7 TRCCIDCCTLR0, Trace Context Identifier Comparator Control Register 0

The TRCCIDCCTLR0 characteristics are:

## Purpose

Contains Context identifier mask values for the TRCCIDCVR&lt;n&gt; registers, for n = 0 to 3.

## Configuration

External register TRCCIDCCTLR0 bits [31:0] are architecturally mapped to AArch64 System register TRCCIDCCTLR0[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, UInt(TRCIDR4.NUMCIDC) &gt; 0x0 , and UInt(TRCIDR2.CIDSIZE) &gt; 0. Otherwise, direct accesses to TRCCIDCCTLR0 are RES0.

## Attributes

TRCCIDCCTLR0 is a 32-bit register.

## Field descriptions

<!-- image -->

COMP3[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 3:

TRCCIDCVR3 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR3. Each bit in this field corresponds to a byte in TRCCIDCVR3.

| COMP3[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR3[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR3[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP2[&lt;m&gt;] , bits [m+16], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 2:

TRCCIDCVR2 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR2. Each bit in this field corresponds to a byte in TRCCIDCVR2.

| COMP2[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR2[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR2[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP1[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 1:

TRCCIDCVR1 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR1. Each bit in this field corresponds to a byte in TRCCIDCVR1.

| COMP1[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR1[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR1[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP0[&lt;m&gt;] , bits [m], for m = 7 to 0

When UInt(TRCIDR4.NUMCIDC) &gt; 0:

TRCCIDCVR0 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR0. Each bit in this field corresponds to a byte in TRCCIDCVR0.

| COMP0[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR0[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR0[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCCIDCCTLR0

If software uses the TRCCIDCVR&lt;n&gt; registers, for n = 0 to 3, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCCIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCCIDCVR&lt;n&gt; is not 0x00 , the behavior of the Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCIDCCTLR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| ETE         | 0x680    | TRCCIDCCTLR0 |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.8 TRCCIDCCTLR1, Trace Context Identifier Comparator Control Register 1

The TRCCIDCCTLR1 characteristics are:

## Purpose

Contains Context identifier mask values for the TRCCIDCVR&lt;n&gt; registers, for n = 4 to 7.

## Configuration

External register TRCCIDCCTLR1 bits [31:0] are architecturally mapped to AArch64 System register TRCCIDCCTLR1[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, UInt(TRCIDR4.NUMCIDC) &gt; 0x4 , and UInt(TRCIDR2.CIDSIZE) &gt; 0. Otherwise, direct accesses to TRCCIDCCTLR1 are RES0.

## Attributes

TRCCIDCCTLR1 is a 32-bit register.

## Field descriptions

<!-- image -->

COMP7[&lt;m&gt;] , bits [m+24], for m = 7 to 0

When UInt(TRCIDR4.NUMCIDC) &gt; 7:

TRCCIDCVR7 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR7. Each bit in this field corresponds to a byte in TRCCIDCVR7.

| COMP7[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR7[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR7[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP6[&lt;m&gt;] , bits [m+16], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 6:

TRCCIDCVR6 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR6. Each bit in this field corresponds to a byte in TRCCIDCVR6.

| COMP6[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR6[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR6[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP5[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 5:

TRCCIDCVR5 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR5. Each bit in this field corresponds to a byte in TRCCIDCVR5.

| COMP5[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR5[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR5[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP4[&lt;m&gt;] , bits [m], for m = 7 to 0

## When UInt(TRCIDR4.NUMCIDC) &gt; 4:

TRCCIDCVR4 mask control. Specifies the mask value that the trace unit applies to TRCCIDCVR4. Each bit in this field corresponds to a byte in TRCCIDCVR4.

| COMP4[<m>]   | Meaning                                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCCIDCVR4[(m × 8+7):(m × 8)] when it performs the Context identifier comparison. |
| 0b1          | The trace unit ignores TRCCIDCVR4[(m × 8+7):(m × 8)] when it performs the Context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.CIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCCIDCCTLR1

If software uses the TRCCIDCVR&lt;n&gt; registers, for n = 4 to 7, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCCIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCCIDCVR&lt;n&gt; is not 0x00 , the behavior of the Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCIDCCTLR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| ETE         | 0x684    | TRCCIDCCTLR1 |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.9 TRCCIDCVR&lt;n&gt;, Trace Context Identifier Comparator Value Registers &lt;n&gt;, n = 0 - 7

The TRCCIDCVR&lt;n&gt; characteristics are:

## Purpose

Contains a Context identifier value.

## Configuration

External register TRCCIDCVR&lt;n&gt; bits [63:0] are architecturally mapped to AArch64 System register TRCCIDCVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMCIDC) &gt; n. Otherwise, direct accesses to TRCCIDCVR&lt;n&gt; are RES0.

## Attributes

TRCCIDCVR&lt;n&gt; is a 64-bit register.

## Field descriptions

VALUE

63

32

VALUE

31

0

<!-- image -->

## VALUE, bits [63:0]

Context identifier value. The width of this field is indicated by TRCIDR2.CIDSIZE. Unimplemented bits are RES0. After a PE Reset, the trace unit assumes that the Context identifier is zero until the PE updates the Context identifier.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCIDCVR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCRSCTLR&lt;a&gt;.GROUP == 0b0110 and TRCRSCTLR&lt;a&gt;.CID[n] == 1.
- TRCACATR&lt;a&gt;.CONTEXTTYPE == 0b01 or 0b11 and TRCACATR&lt;a&gt;.CONTEXT == n.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCIDCVR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance              |
|-------------|------------------------------|
| ETE         | 0x600 + (8 * n) TRCCIDCVR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.10 TRCCIDR0, Trace Component Identification Register 0

The TRCCIDR0 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCIDR0 are RES0.

## Attributes

TRCCIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_0, bits [7:0]

Component identification preamble, segment 0.

Reads as 0x0D

Access to this field is RO.

## Accessing TRCCIDR0

External debugger accesses to this register are unaffected by the OS Lock.

TRCCIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFF0    | TRCCIDR0   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.11 TRCCIDR1, Trace Component Identification Register 1

The TRCCIDR1 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCIDR1 are RES0.

## Attributes

TRCCIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## CLASS, bits [7:4]

Component class.

| CLASS   | Meaning               |
|---------|-----------------------|
| 0b1001  | CoreSight peripheral. |

Other values are defined by the CoreSight Architecture.

This field reads as 0x9 .

Access to this field is RO.

## PRMBL\_1, bits [3:0]

Component identification preamble, segment 1.

Reads as

0b0000

Access to this field is RO.

## Accessing TRCCIDR1

External debugger accesses to this register are unaffected by the OS Lock.

TRCCIDR1 can be accessed through the external debug interface:

## Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFF4    | TRCCIDR1   |

## H9.3.12 TRCCIDR2, Trace Component Identification Register 2

The TRCCIDR2 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCIDR2 are RES0.

## Attributes

TRCCIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_2, bits [7:0]

Component identification preamble, segment 2.

Reads as 0x05

Access to this field is RO.

## Accessing TRCCIDR2

External debugger accesses to this register are unaffected by the OS Lock.

TRCCIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFF8    | TRCCIDR2   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.13 TRCCIDR3, Trace Component Identification Register 3

The TRCCIDR3 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCIDR3 are RES0.

## Attributes

TRCCIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_3, bits [7:0]

Component identification preamble, segment 3.

Reads as 0xB1

Access to this field is RO.

## Accessing TRCCIDR3

External debugger accesses to this register are unaffected by the OS Lock.

TRCCIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFFC    | TRCCIDR3   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.14 TRCCLAIMCLR, Trace Claim Tag Clear Register

The TRCCLAIMCLR characteristics are:

## Purpose

In conjunction with TRCCLAIMSET, provides Claim Tag bits that can be separately set and cleared to indicate whether functionality is in use by a debug agent.

For additional information, see the CoreSight Architecture Specification.

## Configuration

External register TRCCLAIMCLR bits [31:0] are architecturally mapped to AArch64 System register TRCCLAIMCLR[31:0].

External register TRCCLAIMCLR bits [31:0] are architecturally mapped to AArch64 System register TRCCLAIMSET[31:0].

External register TRCCLAIMCLR bits [31:0] are architecturally mapped to External register TRCCLAIMSET[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCLAIMCLR are RES0.

## Attributes

TRCCLAIMCLR is a 32-bit register.

## Field descriptions

<!-- image -->

## CLR[&lt;m&gt;] , bits [m], for m = 31 to 0

Claim Tag Clear. Indicates the current status of Claim Tag bit &lt;m&gt;, and is used to clear Claim Tag bit &lt;m&gt; to 0.

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| CLR[<m>]   | Meaning                                                                        |
|------------|--------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not set. On a write: Ignored.                  |
| 0b1        | On a read: Claim Tag bit <m> is set. On a write: Clear Claim tag bit <m> to 0. |

The number of Claim Tag bits implemented is indicated in TRCCLAIMSET.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0' .

Accessing this field has the following behavior:

- When m &gt;= NUM\_TRC\_CLAIM\_TAGS, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing TRCCLAIMCLR

TRCCLAIMCLR can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| ETE         | 0xFA4    | TRCCLAIMCLR |

## H9.3.15 TRCCLAIMSET, Trace Claim Tag Set Register

The TRCCLAIMSET characteristics are:

## Purpose

In conjunction with TRCCLAIMCLR, provides Claim Tag bits that can be separately set and cleared to indicate whether functionality is in use by a debug agent.

For additional information, see the CoreSight Architecture Specification.

## Configuration

The number of claim tag bits implemented is IMPLEMENTATION DEFINED. Arm recommends that implementations support a minimum of four claim tag bits, that is, SET[3:0] reads as 0b1111 .

External register TRCCLAIMSET bits [31:0] are architecturally mapped to AArch64 System register TRCCLAIMSET[31:0].

External register TRCCLAIMSET bits [31:0] are architecturally mapped to AArch64 System register TRCCLAIMCLR[31:0].

External register TRCCLAIMSET bits [31:0] are architecturally mapped to External register TRCCLAIMCLR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCLAIMSET are RES0.

## Attributes

TRCCLAIMSET is a 32-bit register.

## Field descriptions

<!-- image -->

SET[&lt;m&gt;] , bits [m], for m = 31 to 0

Claim Tag Set. Indicates whether Claim Tag bit &lt;m&gt; is implemented, and is used to set Claim Tag bit &lt;m&gt; to 1.

## Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| SET[<m>]   | Meaning                                                                              |
|------------|--------------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not implemented. On a write: Ignored.                |
| 0b1        | On a read: Claim Tag bit <m> is implemented. On a write: Set Claim Tag bit <m> to 1. |

Accessing this field has the following behavior:

- When m &gt;= NUM\_TRC\_CLAIM\_TAGS, access to this field is RAZ/WI.
- Otherwise, access to this field is RAO/W1S.

## Accessing TRCCLAIMSET

TRCCLAIMSET can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| ETE         | 0xFA0    | TRCCLAIMSET |

## H9.3.16 TRCCNTCTLR&lt;n&gt;, Trace Counter Control Register &lt;n&gt;, n = 0 - 3

The TRCCNTCTLR&lt;n&gt; characteristics are:

## Purpose

Controls the operation of Counter &lt;n&gt;.

## Configuration

External register TRCCNTCTLR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCCNTCTLR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTCTLR&lt;n&gt; are RES0.

## Attributes

TRCCNTCTLR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:18]

Reserved, RES0.

## CNTCHAIN, bit [17]

## When (n MOD 2) != 0:

For TRCCNTCTLR3 and TRCCNTCTLR1, this field controls whether the Counter decrements when a reload event occurs for Counter &lt;n-1&gt;.

| CNTCHAIN   | Meaning                                                                                                                                                |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | The Counter does not decrement when a reload event for Counter <n-1> occurs.                                                                           |
| 0b1        | Counter <n> decrements when a reload event for Counter <n-1> occurs. This concatenates Counter <n> and Counter <n-1>, to provide a larger count value. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLDSELF, bit [16]

Controls whether a reload event occurs for the Counter, when the Counter reaches zero.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RLDEVENT\_TYPE, bit [15]

Selects an event, that when it occurs causes a reload event for Counter

Chooses the type of Resource Selector.

| RLDEVENT_TYPE   | Meaning                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Asingle Resource Selector. TRCCNTCTLR.RLDEVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                        |
| 0b1             | ABoolean-combined pair of Resource Selectors. TRCCNTCTLR.RLDEVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCCNTCTLR.RLDEVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [14:13]

Reserved, RES0.

## RLDEVENT\_SEL, bits [12:8]

Selects an event, that when it occurs causes a reload event for Counter

Defines the selected Resource Selector or pair of Resource Selectors. TRCCNTCTLR.RLDEVENT.TYPE controls whether TRCCNTCTLR.RLDEVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## CNTEVENT\_TYPE, bit [7]

| RLDSELF   | Meaning                                               |
|-----------|-------------------------------------------------------|
| 0b0       | Normal mode. The Counter is in Normal mode.           |
| 0b1       | Self-reload mode. The Counter is in Self-reload mode. |

Selects an event, that when it occurs causes Counter to decrement.

Chooses the type of Resource Selector.

| CNTEVENT_TYPE   | Meaning                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0             | Asingle Resource Selector. TRCCNTCTLR.CNTEVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                        |
| 0b1             | ABoolean-combined pair of Resource Selectors. TRCCNTCTLR.CNTEVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCCNTCTLR.CNTEVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## CNTEVENT\_SEL, bits [4:0]

Selects an event, that when it occurs causes Counter to decrement.

Defines the selected Resource Selector or pair of Resource Selectors. TRCCNTCTLR.CNTEVENT.TYPE controls whether TRCCNTCTLR.CNTEVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTCTLR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCNTCTLR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance               |
|-------------|-------------------------------|
| ETE         | 0x150 + (4 * n) TRCCNTCTLR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.

- Otherwise, accesses to this register are RW.

## H9.3.17 TRCCNTRLDVR&lt;n&gt;, Trace Counter Reload Value Register &lt;n&gt;, n = 0 - 3

The TRCCNTRLDVR&lt;n&gt; characteristics are:

## Purpose

This sets or returns the reload count value for Counter &lt;n&gt;.

## Configuration

External register TRCCNTRLDVR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCCNTRLDVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTRLDVR&lt;n&gt; are RES0.

## Attributes

TRCCNTRLDVR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 16 15   |
|------|---------|
| RES0 | VALUE   |

## Bits [31:16]

Reserved, RES0.

## VALUE, bits [15:0]

Contains the reload value for Counter &lt;n&gt;. When a reload event occurs for Counter &lt;n&gt; then the trace unit copies the VALUE&lt;n&gt; field into Counter &lt;n&gt;.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTRLDVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCNTRLDVR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance                |
|-------------|--------------------------------|
| ETE         | 0x140 + (4 * n) TRCCNTRLDVR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.18 TRCCNTVR&lt;n&gt;, Trace Counter Value Register &lt;n&gt;, n = 0 - 3

The TRCCNTVR&lt;n&gt; characteristics are:

## Purpose

This sets or returns the value of Counter &lt;n&gt;.

## Configuration

External register TRCCNTVR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCCNTVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR5.NUMCNTR) &gt; n. Otherwise, direct accesses to TRCCNTVR&lt;n&gt; are RES0.

## Attributes

TRCCNTVR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 16 15   |
|------|---------|
| RES0 | VALUE   |

## Bits [31:16]

Reserved, RES0.

## VALUE, bits [15:0]

Contains the count value of Counter.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCCNTVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.COUNTERS[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

TRCCNTVR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance             |
|-------------|-----------------------------|
| ETE         | 0x160 + (4 * n) TRCCNTVR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.19 TRCCONFIGR, Trace Configuration Register

The TRCCONFIGR characteristics are:

## Purpose

Controls the tracing options.

## Configuration

External register TRCCONFIGR bits [31:0] are architecturally mapped to AArch64 System register TRCCONFIGR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCCONFIGR are RES0.

## Attributes

TRCCONFIGR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:19]

Reserved, RES0.

## ITO, bit [18]

## When TRCIDR0.ITE == '1':

Instrumentation Trace Override.

| ITO   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Instrumentation Trace Override disabled. |
| 0b1   | Instrumentation Trace Override enabled.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [17:16]

Reserved, RES0.

VMIDOPT, bit [15]

## When TRCIDR2.VMIDOPT == '01':

Virtual context identifier selection control.

| VMIDOPT   | Meaning                                                          |
|-----------|------------------------------------------------------------------|
| 0b0       | VTTBR_EL2.VMID is used as the Virtual context identifier.        |
| 0b1       | CONTEXTIDR_EL2.PROCID is used as the Virtual context identifier. |

## When TRCIDR2.VMIDOPT == '00':

Reserved, RES0.

Virtual context identifier selection control.

VTTBR\_EL2.VMID is used as the Virtual context identifier.

## When TRCIDR2.VMIDOPT == '10':

Reserved, RES1.

Virtual context identifier selection control.

CONTEXTIDR\_EL2.PROCID is used as the Virtual context identifier.

## Otherwise:

Reserved, RES0.

QE, bits [14:13]

## When TRCIDR0.QSUPP == '01':

Qelement generation control.

| QE   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                           |
| 0b01 | Qelements with instruction counts are enabled. Qelements without instruction counts are disabled. |

All other values are reserved.

## When TRCIDR0.QSUPP == '10':

Qelement generation control.

| QE   | Meaning                                                                                          |
|------|--------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                          |
| 0b11 | Qelements with instruction counts are enabled. Qelements without instruction counts are enabled. |

All other values are reserved.

## When TRCIDR0.QSUPP == '11':

Qelement generation control.

| QE   | Meaning                                                                                           |
|------|---------------------------------------------------------------------------------------------------|
| 0b00 | Qelements are disabled.                                                                           |
| 0b01 | Qelements with instruction counts are enabled. Qelements without instruction counts are disabled. |
| 0b11 | Qelements with instruction counts are enabled. Qelements without instruction counts are enabled.  |

All other values are reserved.

## Otherwise:

Reserved, RES0.

## RS, bit [12]

## When TRCIDR0.RETSTACK == '1':

Return stack control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TS, bit [11]

## When TRCIDR0.TSSIZE != '00000':

Global timestamp tracing control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

| RS   | Meaning                   |
|------|---------------------------|
| 0b0  | Return stack is disabled. |
| 0b1  | Return stack is enabled.  |

| TS   | Meaning                               |
|------|---------------------------------------|
| 0b0  | Global timestamp tracing is disabled. |
| 0b1  | Global timestamp tracing is enabled.  |

## Otherwise:

Reserved, RES0.

## Bits [10:8]

Reserved, RES0.

## VMID, bit [7]

## When TRCIDR2.VMIDSIZE != '00000':

Virtual context identifier tracing control.

| VMID   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Virtual context identifier tracing is disabled. |
| 0b1    | Virtual context identifier tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

CID, bit [6]

## When TRCIDR2.CIDSIZE != '00000':

Context identifier tracing control.

| CID   | Meaning                                 |
|-------|-----------------------------------------|
| 0b0   | Context identifier tracing is disabled. |
| 0b1   | Context identifier tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [5]

Reserved, RES0.

CCI, bit [4]

When TRCIDR0.TRCCCI == '1':

Cycle counting instruction tracing control.

Accessible as follows:

- When OSLockStatus(), or !IsTraceCorePowered(), or !AllowExternalTraceAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| CCI   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Cycle counting instruction tracing is disabled. |
| 0b1   | Cycle counting instruction tracing is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

BB, bit [3]

## When TRCIDR0.TRCBB == '1':

Branch broadcasting control.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [2:1]

Reserved, RES0.

Bit [0]

Reserved, RES1.

## Accessing TRCCONFIGR

Must always be programmed.

TRCCONFIGR.QE must be set to 0b00 if TRCCONFIGR.BB is not 0.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCCONFIGR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x010    | TRCCONFIGR |

| BB   | Meaning                          |
|------|----------------------------------|
| 0b0  | Branch broadcasting is disabled. |
| 0b1  | Branch broadcasting is enabled.  |

## H9.3.20 TRCDEVAFF, Trace Device Affinity Register

The TRCDEVAFF characteristics are:

## Purpose

For additional information, see the CoreSight Architecture Specification.

Reads the same value as the MPIDR\_EL1 register for the PE that this trace unit has affinity with.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCDEVAFF are RES0.

## Attributes

TRCDEVAFF is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:40]

Reserved, RES0.

## Aff3, bits [39:32]

Affinity level 3. See the description of Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

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

Note

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

## Accessing TRCDEVAFF

External debugger accesses to this register are unaffected by the OS Lock.

TRCDEVAFF can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFA8    | TRCDEVAFF  |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.21 TRCDEVARCH, Trace Device Architecture Register

The TRCDEVARCH characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

External register TRCDEVARCH bits [31:0] are architecturally mapped to AArch64 System register TRCDEVARCH[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCDEVARCH are RES0.

## Attributes

TRCDEVARCHis a 32-bit register.

## Field descriptions

<!-- image -->

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

| REVISION   | Meaning                |
|------------|------------------------|
| 0b0000     | ETEv1.0, FEAT_ETE.     |
| 0b0001     | ETEv1.1, FEAT_ETEv1p1. |

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

External debugger accesses to this register are unaffected by the OS Lock.

TRCDEVARCHcan be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFBC    | TRCDEVARCH |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| REVISION   | Meaning                |
|------------|------------------------|
| 0b0010     | ETEv1.2, FEAT_ETEv1p2. |
| 0b0011     | ETEv1.3, FEAT_ETEv1p3. |

## H9.3.22 TRCDEVID, Trace Device Configuration Register

The TRCDEVID characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

External register TRCDEVID bits [31:0] are architecturally mapped to AArch64 System register TRCDEVID[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCDEVID are RES0.

## Attributes

TRCDEVID is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCDEVID

External debugger accesses to this register are unaffected by the OS Lock.

TRCDEVID can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFC8    | TRCDEVID   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.23 TRCDEVID1, Trace Device Configuration Register 1

The TRCDEVID1 characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCDEVID1 are RES0.

## Attributes

TRCDEVID1 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCDEVID1

External debugger accesses to this register are unaffected by the OS Lock.

TRCDEVID1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFC4    | TRCDEVID1  |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.24 TRCDEVID2, Trace Device Configuration Register 2

The TRCDEVID2 characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCDEVID2 are RES0.

## Attributes

TRCDEVID2 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCDEVID2

External debugger accesses to this register are unaffected by the OS Lock.

TRCDEVID2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFC0    | TRCDEVID2  |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.25 TRCDEVTYPE, Trace Device Type Register

The TRCDEVTYPE characteristics are:

## Purpose

Provides discovery information for the component. If the part number field is not recognized, a debugger can report the information that is provided by TRCDEVTYPE about the component instead.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCDEVTYPE are RES0.

## Attributes

TRCDEVTYPE is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SUB, bits [7:4]

Component sub-type.

| SUB    | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0001 | WhenMAJOR== 0x3 (Trace source): Associated with a PE. |

This field reads as 0x1 .

Access to this field is RO.

## MAJOR, bits [3:0]

Component major type.

| MAJOR   | Meaning       |
|---------|---------------|
| 0b0011  | Trace source. |

Other values are defined by the CoreSight Architecture.

This field reads as 0x3 .

Access to this field is RO.

## Accessing TRCDEVTYPE

External debugger accesses to this register are unaffected by the OS Lock.

TRCDEVTYPE can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFCC    | TRCDEVTYPE |

## Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.26 TRCEVENTCTL0R, Trace Event Control 0 Register

The TRCEVENTCTL0R characteristics are:

## Purpose

Controls the generation of ETEEvents.

## Configuration

External register TRCEVENTCTL0R bits [31:0] are architecturally mapped to AArch64 System register TRCEVENTCTL0R[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR4.NUMRSPAIR != '0000'. Otherwise, direct accesses to TRCEVENTCTL0R are RES0.

## Attributes

TRCEVENTCTL0R is a 32-bit register.

## Field descriptions

<!-- image -->

EVENT3\_TYPE, bit [31]

When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 3:

Chooses the type of Resource Selector.

| EVENT3_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT3.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT3.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT3.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [30:29]

Reserved, RES0.

EVENT3\_SEL, bits [28:24]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 3:

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[3] == 1, then Event element 3 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT3.TYPE controls whether TRCEVENTCTL0R.EVENT3.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT2\_TYPE, bit [23]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 2:

Chooses the type of Resource Selector.

| EVENT2_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT2.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT2.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT2.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [22:21]

Reserved, RES0.

## EVENT2\_SEL, bits [20:16]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 2:

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[2] == 1, then Event element 2 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT2.TYPE controls whether TRCEVENTCTL0R.EVENT2.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT1\_TYPE, bit [15]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 1:

Chooses the type of Resource Selector.

| EVENT1_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT1.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT1.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT1.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [14:13]

Reserved, RES0.

## EVENT1\_SEL, bits [12:8]

## When TRCIDR4.NUMRSPAIR != '0000' and UInt(TRCIDR0.NUMEVENT) &gt;= 1:

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[1] == 1, then Event element 1 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT1.TYPE controls whether TRCEVENTCTL0R.EVENT1.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EVENT0\_TYPE, bit [7]

## When TRCIDR4.NUMRSPAIR != '0000':

Chooses the type of Resource Selector.

| EVENT0_TYPE   | Meaning                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0           | Asingle Resource Selector. TRCEVENTCTL0R.EVENT0.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                         |
| 0b1           | ABoolean-combined pair of Resource Selectors. TRCEVENTCTL0R.EVENT0.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCEVENTCTL0R.EVENT0.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## EVENT0\_SEL, bits [4:0]

## When TRCIDR4.NUMRSPAIR != '0000':

When any of the selected resource events occurs and TRCEVENTCTL1R.INSTEN[0] == 1, then Event element 0 is generated in the instruction trace element stream.

Defines the selected Resource Selector or pair of Resource Selectors. TRCEVENTCTL0R.EVENT0.TYPE controls whether TRCEVENTCTL0R.EVENT0.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TRCEVENTCTL0R

Must be programmed if implemented.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCEVENTCTL0R can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| ETE         | 0x020    | TRCEVENTCTL0R |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.27 TRCEVENTCTL1R, Trace Event Control 1 Register

The TRCEVENTCTL1R characteristics are:

## Purpose

Controls the behavior of the ETEEvents that TRCEVENTCTL0R selects.

## Configuration

External register TRCEVENTCTL1R bits [31:0] are architecturally mapped to AArch64 System register TRCEVENTCTL1R[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCEVENTCTL1R are RES0.

## Attributes

TRCEVENTCTL1R is a 32-bit register.

## Field descriptions

<!-- image -->

Bits [31:14]

Reserved, RES0.

OE, bit [13]

When TRCIDR5.OE == '1':

ETE Trace Output Enable control.

| OE   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | Trace output to any IMPLEMENTATION DEFINED trace output interface is disabled. |
| 0b1  | Trace output to any IMPLEMENTATION DEFINED trace output interface is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## LPOVERRIDE, bit [12]

When TRCIDR5.LPOVERRIDE == '1':

Low-power Override Mode select.

| LPOVERRIDE   | Meaning                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Trace unit Low-power Override Mode is not enabled. That is, the trace unit is permitted to enter low-power state.                                |
| 0b1          | Trace unit Low-power Override Mode is enabled. That is, entry to a low-power state does not affect the trace unit resources or trace generation. |

## Otherwise:

Reserved, RES0.

## ATB, bit [11]

## When TRCIDR5.ATBTRIG == '1':

AMBATrace Bus (ATB) trigger enable.

If a CoreSight ATB interface is implemented then when ETEEvent 0 occurs the trace unit sets:

- ATID == 0x7D .
- ATDATA to the value of TRCTRACEIDR.

If the width of ATDATA is greater than the width of TRCTRACEIDR.TRACEID then the trace unit zeros the upper ATDATA bits.

If ETEEvent 0 is programmed to occur based on program execution, such as an Address Comparator, the ATB trigger might not be inserted into the ATB stream at the same time as any trace generated by that program execution is output by the trace unit. Typically, the generated trace might be buffered in a trace unit which means that the ATB trigger would be output before the associated trace is output.

If ETEEvent 0 is asserted multiple times in close succession, the trace unit is required to generate an ATB trigger for the first assertion, but might ignore one or more of the subsequent assertions. Arm recommends that the window in which ETEEvent 0 is ignored is limited only by the time taken to output an ATB trigger.

| ATB   | Meaning                  |
|-------|--------------------------|
| 0b0   | ATB trigger is disabled. |
| 0b1   | ATB trigger is enabled.  |

## Otherwise:

Reserved, RES0.

## Bits [10:4]

Reserved, RES0.

## INSTEN[&lt;m&gt;] , bits [m], for m = 3 to 0

Event element control.

| INSTEN[<m>]   | Meaning                                                                 |
|---------------|-------------------------------------------------------------------------|
| 0b0           | The trace unit does not generate an Event element <m>.                  |
| 0b1           | The trace unit generates an Event element <m> when ETEEvent <m> occurs. |

Accessing this field has the following behavior:

- When TRCIDR4.NUMRSPAIR == '0000', access to this field is RES0.
- Access to this field is RES0 if all of the following are true:
- TRCIDR4.NUMRSPAIR != '0000'
- m&gt;UInt(TRCIDR0.NUMEVENT)
- Otherwise, access to this field is RW.

## Accessing TRCEVENTCTL1R

Must be programmed.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCEVENTCTL1R can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| ETE         | 0x024    | TRCEVENTCTL1R |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.28 TRCEXTINSELR&lt;n&gt;, Trace External Input Select Register &lt;n&gt;, n = 0 - 3

The TRCEXTINSELR&lt;n&gt; characteristics are:

## Purpose

Use this to set, or read, which External Inputs are resources to the trace unit.

The name TRCEXTINSELR is an alias of TRCEXTINSELR0.

## Configuration

External register TRCEXTINSELR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCEXTINSELR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR5.NUMEXTINSEL) &gt; n. Otherwise, direct accesses to TRCEXTINSELR&lt;n&gt; are RES0.

## Attributes

TRCEXTINSELR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 16 15    |
|------|----------|
| RES0 | evtCount |

## Bits [31:16]

Reserved, RES0.

## evtCount, bits [15:0]

PMUevent to select.

The event number as defined by the Arm ARM.

Software must program this field with a PMU event that is supported by the PE being programmed.

There are three ranges of PMU event numbers:

- PMUevent numbers in the range 0x0000 to 0x003F are common architectural and microarchitectural events.
- PMUevent numbers in the range 0x0040 to 0x00BF are Arm recommended common architectural and microarchitectural PMU events.
- PMUevent numbers in the range 0x00C0 to 0x03FF are IMPLEMENTATION DEFINED PMU events.

If evtCount is programmed to a PMU event that is reserved or not supported by the PE, the behavior depends on the PMU event type:

- For the range 0x0000 to 0x003F , then the PMU event is not active, and the value returned by a direct or external read of the evtCount field is the value written to the field.
- For IMPLEMENTATION DEFINED PMU events, it is UNPREDICTABLE what PMU event, if any, is counted, and the value returned by a direct or external read of the evtCount field is UNKNOWN.

UNPREDICTABLE means the PMU event must not expose privileged information.

Arm recommends that the behavior across a family of implementations is defined such that if a given implementation does not include a PMU event from a set of common IMPLEMENTATION DEFINED PMU events, then no PMU event is counted and the value read back on evtCount is the value written.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCEXTINSELR&lt;n&gt;

Must be programmed if any of the following is true: TRCRSCTLR&lt;a&gt;.GROUP == 0b0000 and TRCRSCTLR&lt;a&gt;.EXTIN[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCEXTINSELR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance                 |
|-------------|---------------------------------|
| ETE         | 0x120 + (4 * n) TRCEXTINSELR<n> |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.29 TRCIDR0, Trace ID Register 0

The TRCIDR0 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR0 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR0[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR0 are RES0.

## Attributes

TRCIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES0.

## COMMTRANS,bit [30]

Transaction Start element behavior.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| COMMTRANS   | Meaning                                         |
|-------------|-------------------------------------------------|
| 0b0         | Transaction Start elements are P0 elements.     |
| 0b1         | Transaction Start elements are not P0 elements. |

Access to this field is RO.

## COMMOPT,bit [29]

Indicates the contents and encodings of Cycle count packets.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## ITE, bit [22]

Indicates whether Instrumentation Trace is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| COMMOPT   | Meaning        |
|-----------|----------------|
| 0b0       | Commit mode 0. |
| 0b1       | Commit mode 1. |

The Commit mode defines the contents and encodings of Cycle Count packets, in particular how Commit elements are indicated by these packets. See the descriptions of these packets for more details.

Accessing this field has the following behavior:

- Access to this field is RAO/WI if all of the following are true:
- TRCIDR0.TRCCCI == '1'
- UInt(TRCIDR8.MAXSPEC) == 0x0
- When TRCIDR0.TRCCCI == '0', access to this field is RAZ/WI.
- Otherwise, access to this field is RO.

## TSSIZE, bits [28:24]

Indicates that the trace unit implements Global timestamping and the size of the timestamp value.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TSSIZE   | Meaning                                                        |
|----------|----------------------------------------------------------------|
| 0b00000  | Global timestamping not implemented.                           |
| 0b01000  | Global timestamping implemented with a 64-bit timestamp value. |

All other values are reserved.

This field reads as 0b01000 .

Access to this field is RO.

## TSMARK,bit [23]

Indicates whether Timestamp Marker elements are generated.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TSMARK   | Meaning                                      |
|----------|----------------------------------------------|
| 0b0      | Timestamp Marker elements are not generated. |
| 0b1      | Timestamp Marker elements are generated.     |

| ITE   | Meaning                                |
|-------|----------------------------------------|
| 0b0   | Instrumentation Trace not implemented. |
| 0b1   | Instrumentation Trace implemented.     |

This field has the value 1 if FEAT\_ITE is implemented.

Access to this field is RO.

## Bits [21:18]

Reserved, RES0.

## TRCEXDATA, bit [17]

## When TRCIDR0.TRCDATA != '00':

Indicates if the trace unit implements tracing of data transfers for exceptions and exception returns. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCEXDATA   | Meaning                                                                         |
|-------------|---------------------------------------------------------------------------------|
| 0b0         | Tracing of data transfers for exceptions and exception returns not implemented. |
| 0b1         | Tracing of data transfers for exceptions and exception returns implemented.     |

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## QSUPP, bits [16:15]

Indicates that the trace unit implements Q element support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| QSUPP   | Meaning                                                                                                                     |
|---------|-----------------------------------------------------------------------------------------------------------------------------|
| 0b00    | Qelement support is not implemented.                                                                                        |
| 0b01    | Qelement support is implemented, and only supports Qelements with instruction counts.                                       |
| 0b10    | Qelement support is implemented, and only supports Qelements without instruction counts.                                    |
| 0b11    | Qelement support is implemented, and supports: • Qelements with instruction counts. • Qelements without instruction counts. |

Access to this field is RO.

## QFILT, bit [14]

Indicates if the trace unit implements Q element filtering.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| QFILT   | Meaning                                |
|---------|----------------------------------------|
| 0b0     | Qelement filtering is not implemented. |
| 0b1     | Qelement filtering is implemented.     |

If TRCIDR0.QSUPP == 0b00 then this field is 0.

Access to this field is RO.

## CONDTYPE, bits [13:12]

## When TRCIDR0.TRCCOND == '1':

Indicates how conditional instructions are traced. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CONDTYPE   | Meaning                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------|
| 0b00       | Conditional instructions are traced with an indication of whether they pass or fail their condition code check. |
| 0b01       | Conditional instructions are traced with an indication of the APSR condition flags.                             |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## NUMEVENT,bits [11:10]

## When TRCIDR4.NUMRSPAIR == '0000':

Indicates the number of ETEEvents implemented.

| NUMEVENT   | Meaning                              |
|------------|--------------------------------------|
| 0b00       | The trace unit supports 0 ETEEvents. |

All other values are reserved.

Access to this field is RO.

## When TRCIDR4.NUMRSPAIR != '0000':

Indicates the number of ETEEvents implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMEVENT   | Meaning                              |
|------------|--------------------------------------|
| 0b00       | The trace unit supports 1 ETEEvent.  |
| 0b01       | The trace unit supports 2 ETEEvents. |
| 0b10       | The trace unit supports 3 ETEEvents. |
| 0b11       | The trace unit supports 4 ETEEvents. |

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## RETSTACK, bit [9]

Indicates if the trace unit supports the return stack.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RETSTACK   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Return stack not implemented. |
| 0b1        | Return stack implemented.     |

Access to this field is RO.

## Bit [8]

Reserved, RES0.

## TRCCCI, bit [7]

Indicates if the trace unit implements cycle counting.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCCCI   | Meaning                         |
|----------|---------------------------------|
| 0b0      | Cycle counting not implemented. |
| 0b1      | Cycle counting implemented.     |

This field reads as 1.

Access to this field is RO.

## TRCCOND,bit [6]

Indicates if the trace unit implements conditional instruction tracing. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCCOND   | Meaning                                          |
|-----------|--------------------------------------------------|
| 0b0       | Conditional instruction tracing not implemented. |
| 0b1       | Conditional instruction tracing implemented.     |

This field reads as 0.

Access to this field is RO.

## TRCBB, bit [5]

Indicates if the trace unit implements branch broadcasting.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCBB   | Meaning                              |
|---------|--------------------------------------|
| 0b0     | Branch broadcasting not implemented. |
| 0b1     | Branch broadcasting implemented.     |

This field reads as 1.

Access to this field is RO.

## TRCDATA, bits [4:3]

Indicates if the trace unit implements data tracing. Data tracing is not implemented in ETE and this field is reserved for other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCDATA   | Meaning                       |
|-----------|-------------------------------|
| 0b00      | Data tracing not implemented. |
| 0b11      | Data tracing implemented.     |

All other values are reserved.

This field reads as 0b00 .

Access to this field is RO.

## INSTP0, bits [2:1]

Indicates if load and store instructions are P0 instructions. Load and store instructions as P0 instructions is not implemented in ETE and this field is reserved for other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| INSTP0   | Meaning                                              |
|----------|------------------------------------------------------|
| 0b00     | Load and store instructions are not P0 instructions. |
| 0b11     | Load and store instructions are P0 instructions.     |

All other values are reserved.

When FEAT\_ETE is implemented, the only permitted value is 0b00 .

Access to this field is RO.

## Bit [0]

Reserved, RES1.

## Accessing TRCIDR0

TRCIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1E0    | TRCIDR0    |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.30 TRCIDR1, Trace ID Register 1

The TRCIDR1 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR1 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR1[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR1 are RES0.

## Attributes

TRCIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

## DESIGNER, bits [31:24]

Indicates which company designed the trace unit. The permitted values of this field are the same as MIDR\_EL1.Implementer.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bits [23:16]

Reserved, RES0.

## Bits [15:12]

Reserved, RES1.

## TRCARCHMAJ,bits [11:8]

Major architecture version.

| TRCARCHMAJ   | Meaning                                                                            |
|--------------|------------------------------------------------------------------------------------|
| 0b1111       | If both TRCIDR1.TRCARCHMAJ and TRCIDR1.TRCARCHMIN == 0xF then refer to TRCDEVARCH. |

All other values are reserved.

This field reads as 0b1111 .

Access to this field is RO.

## TRCARCHMIN,bits [7:4]

Minor architecture version.

| TRCARCHMIN   | Meaning                                                                            |
|--------------|------------------------------------------------------------------------------------|
| 0b1111       | If both TRCIDR1.TRCARCHMAJ and TRCIDR1.TRCARCHMIN == 0xF then refer to TRCDEVARCH. |

All other values are reserved.

This field reads as 0b1111 .

Access to this field is RO.

## REVISION, bits [3:0]

Implementation revision.

Returns an IMPLEMENTATION DEFINED value that identifies the revision of the trace unit.

Arm deprecates any use of this field and recommends that implementations set this field to zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRCIDR1

TRCIDR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1E4    | TRCIDR1    |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.31 TRCIDR10, Trace ID Register 10

The TRCIDR10 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR10 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR10[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR10 are RES0.

## Attributes

TRCIDR10 is a 32-bit register.

## Field descriptions

| 31       | 0   |
|----------|-----|
| NUMP1KEY |     |

## NUMP1KEY, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of P1 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR10

TRCIDR10 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x188    | TRCIDR10   |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.32 TRCIDR11, Trace ID Register 11

The TRCIDR11 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR11 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR11[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR11 are RES0.

## Attributes

TRCIDR11 is a 32-bit register.

## Field descriptions

| 31       | 0   |
|----------|-----|
| NUMP1SPC |     |

## NUMP1SPC, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of special P1 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR11

TRCIDR11 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x18C    | TRCIDR11   |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.33 TRCIDR12, Trace ID Register 12

The TRCIDR12 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR12 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR12[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR12 are RES0.

## Attributes

TRCIDR12 is a 32-bit register.

## Field descriptions

| 31         | 0          |
|------------|------------|
| NUMCONDKEY | NUMCONDKEY |

## NUMCONDKEY,bits [31:0]

## When TRCIDR0.TRCCOND == '1':

Indicates the number of conditional instruction right-hand keys. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR12

TRCIDR12 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x190    | TRCIDR12   |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.34 TRCIDR13, Trace ID Register 13

The TRCIDR13 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR13 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR13[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR13 are RES0.

## Attributes

TRCIDR13 is a 32-bit register.

## Field descriptions

<!-- image -->

## NUMCONDSPC,bits [31:0]

## When TRCIDR0.TRCCOND == '1':

Indicates the number of special conditional instruction right-hand keys. Conditional instruction tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR13

TRCIDR13 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x194    | TRCIDR13   |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.35 TRCIDR2, Trace ID Register 2

The TRCIDR2 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR2 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR2[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR2 are RES0.

## Attributes

TRCIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## WFXMODE,bit [31]

Indicates whether WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions:

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WFXMODE   | Meaning                                                                         |
|-----------|---------------------------------------------------------------------------------|
| 0b0       | WFI , WFIT , WFE , and WFET instructions are not classified as P0 instructions. |
| 0b1       | WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions.     |

Access to this field is RO.

## VMIDOPT, bits [30:29]

Indicates the options for Virtual context identifier selection.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDOPT   | Meaning                                                                            |
|-----------|------------------------------------------------------------------------------------|
| 0b00      | Virtual context identifier selection not supported. TRCCONFIGR.VMIDOPT is RES0.    |
| 0b01      | Virtual context identifier selection supported. TRCCONFIGR.VMIDOPT is implemented. |
| 0b10      | Virtual context identifier selection not supported. TRCCONFIGR.VMIDOPT is RES1.    |

All other values are reserved.

If TRCIDR2.VMIDSIZE == 0b00000 then this field is 0b00 .

If TRCIDR2.VMIDSIZE != 0b00000 then this field is 0b10 .

Access to this field is RO.

## CCSIZE, bits [28:25]

## When TRCIDR0.TRCCCI == '1':

Indicates the size of the cycle counter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCSIZE   | Meaning                                 |
|----------|-----------------------------------------|
| 0b0000   | The cycle counter is 12 bits in length. |
| 0b0001   | The cycle counter is 13 bits in length. |
| 0b0010   | The cycle counter is 14 bits in length. |
| 0b0011   | The cycle counter is 15 bits in length. |
| 0b0100   | The cycle counter is 16 bits in length. |
| 0b0101   | The cycle counter is 17 bits in length. |
| 0b0110   | The cycle counter is 18 bits in length. |
| 0b0111   | The cycle counter is 19 bits in length. |
| 0b1000   | The cycle counter is 20 bits in length. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## DVSIZE, bits [24:20]

## When TRCIDR0.TRCDATA != '00':

Indicates the data value size in bytes. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DVSIZE   | Meaning                                                 |
|----------|---------------------------------------------------------|
| 0b00000  | Data value tracing not implemented.                     |
| 0b00100  | Data value tracing has a maximum of 32-bit data values. |
| 0b01000  | Data value tracing has a maximum of 64-bit data values. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## DASIZE, bits [19:15]

## When TRCIDR0.TRCDATA != '00':

Indicates the data address size in bytes. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DASIZE   | Meaning                                                      |
|----------|--------------------------------------------------------------|
| 0b00000  | Data address tracing not implemented.                        |
| 0b00100  | Data address tracing has a maximum of 32-bit data addresses. |
| 0b01000  | Data address tracing has a maximum of 64-bit data addresses. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## VMIDSIZE, bits [14:10]

Indicates the trace unit Virtual context identifier size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDSIZE   | Meaning                                              |
|------------|------------------------------------------------------|
| 0b00000    | Virtual context identifier tracing is not supported. |
| 0b00001    | 8-bit Virtual context identifier size.               |
| 0b00010    | 16-bit Virtual context identifier size.              |
| 0b00100    | 32-bit Virtual context identifier size.              |

All other values are reserved.

If the PE does not implement EL2 then this field is 0b00000 .

If the PE implements EL2 then this field is 0b00100 .

Access to this field is RO.

## CIDSIZE, bits [9:5]

Indicates the Context identifier size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CIDSIZE   | Meaning                                      |
|-----------|----------------------------------------------|
| 0b00000   | Context identifier tracing is not supported. |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| CIDSIZE   | Meaning                         |
|-----------|---------------------------------|
| 0b00100   | 32-bit Context identifier size. |

All other values are reserved.

This field reads as 0b00100 .

Access to this field is RO.

## IASIZE, bits [4:0]

Virtual instruction address size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IASIZE   | Meaning                                     |
|----------|---------------------------------------------|
| 0b00100  | Maximum of 32-bit instruction address size. |
| 0b01000  | Maximum of 64-bit instruction address size. |

All other values are reserved.

This field reads as 0b01000 .

Access to this field is RO.

## Accessing TRCIDR2

TRCIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1E8    | TRCIDR2    |

## H9.3.36 TRCIDR3, Trace ID Register 3

The TRCIDR3 characteristics are:

## Purpose

Returns the base architecture of the trace unit.

## Configuration

External register TRCIDR3 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR3[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR3 are RES0.

## Attributes

TRCIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## NOOVERFLOW,bit [31]

Indicates if overflow prevention is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NOOVERFLOW   | Meaning                                 |
|--------------|-----------------------------------------|
| 0b0          | Overflow prevention is not implemented. |
| 0b1          | Overflow prevention is implemented.     |

If TRCIDR3.STALLCTL == 0 then this field is 0.

Access to this field is RO.

## NUMPROC,bits [13:12, 30:28]

Indicates the number of PEs available for tracing.

This field reads as 0b00000 .

Access to this field is RO.

## SYSSTALL, bit [27]

Indicates if stalling of the PE is permitted.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYSSTALL   | Meaning                              |
|------------|--------------------------------------|
| 0b0        | Stalling of the PE is not permitted. |
| 0b1        | Stalling of the PE is permitted.     |

The value of this field might be dynamic and change based on system conditions.

If TRCIDR3.STALLCTL == 0 then this field is 0.

Access to this field is RO.

## STALLCTL, bit [26]

Indicates if trace unit implements stalling of the PE.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| STALLCTL   | Meaning                                |
|------------|----------------------------------------|
| 0b0        | Stalling of the PE is not implemented. |
| 0b1        | Stalling of the PE is implemented.     |

Access to this field is RO.

## SYNCPR, bit [25]

Indicates if an implementation has a fixed synchronization period.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SYNCPR   | Meaning                                                                    |
|----------|----------------------------------------------------------------------------|
| 0b0      | TRCSYNCPR is read/write so software can change the synchronization period. |
| 0b1      | TRCSYNCPR is read-only so the synchronization period is fixed.             |

This field reads as 0.

Access to this field is RO.

| NUMPROC   | Meaning                          |
|-----------|----------------------------------|
| 0b00000   | The trace unit can trace one PE. |

## TRCERR, bit [24]

Indicates forced tracing of System Error exceptions is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRCERR   | Meaning                                                       |
|----------|---------------------------------------------------------------|
| 0b0      | Forced tracing of System Error exceptions is not implemented. |
| 0b1      | Forced tracing of System Error exceptions is implemented.     |

This field reads as 1.

Access to this field is RO.

## Bit [23]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [22]

Indicates if Non-secure EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_NS_EL2   | Meaning                            |
|------------------|------------------------------------|
| 0b0              | Non-secure EL2 is not implemented. |
| 0b1              | Non-secure EL2 is implemented.     |

Access to this field is RO.

## EXLEVEL\_NS\_EL1, bit [21]

Indicates if Non-secure EL1 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_NS_EL1   | Meaning                            |
|------------------|------------------------------------|
| 0b0              | Non-secure EL1 is not implemented. |
| 0b1              | Non-secure EL1 is implemented.     |

Access to this field is RO.

## EXLEVEL\_NS\_EL0, bit [20]

Indicates if Non-secure EL0 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## EXLEVEL\_S\_EL3, bit [19]

Indicates if EL3 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL3   | Meaning                 |
|-----------------|-------------------------|
| 0b0             | EL3 is not implemented. |
| 0b1             | EL3 is implemented.     |

Access to this field is RO.

## EXLEVEL\_S\_EL2, bit [18]

Indicates if Secure EL2 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL2   | Meaning                        |
|-----------------|--------------------------------|
| 0b0             | Secure EL2 is not implemented. |
| 0b1             | Secure EL2 is implemented.     |

Access to this field is RO.

## EXLEVEL\_S\_EL1, bit [17]

Indicates if Secure EL1 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL1   | Meaning                        |
|-----------------|--------------------------------|
| 0b0             | Secure EL1 is not implemented. |
| 0b1             | Secure EL1 is implemented.     |

Access to this field is RO.

| EXLEVEL_NS_EL0   | Meaning                            |
|------------------|------------------------------------|
| 0b0              | Non-secure EL0 is not implemented. |
| 0b1              | Non-secure EL0 is implemented.     |

## EXLEVEL\_S\_EL0, bit [16]

Indicates if Secure EL0 is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXLEVEL_S_EL0   | Meaning                        |
|-----------------|--------------------------------|
| 0b0             | Secure EL0 is not implemented. |
| 0b1             | Secure EL0 is implemented.     |

Access to this field is RO.

## Bits [15:14]

Reserved, RES0.

## CCITMIN, bits [11:0]

## When TRCIDR0.TRCCCI == '0':

Indicates the minimum value that can be programmed in TRCCCCTLR.THRESHOLD.

Reads as 0x000

Access to this field is RO.

## When TRCIDR0.TRCCCI == '1':

Indicates the minimum value that can be programmed in TRCCCCTLR.THRESHOLD.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCITMIN        | Meaning                                                          |
|----------------|------------------------------------------------------------------|
| 0x001 .. 0xFFF | The minimum value that can be programmed in TRCCCCTLR.THRESHOLD. |

The minimum value of this field is 0x001 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR3

TRCIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1EC    | TRCIDR3    |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.37 TRCIDR4, Trace ID Register 4

The TRCIDR4 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR4 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR4[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR4 are RES0.

## Attributes

TRCIDR4 is a 32-bit register.

## Field descriptions

<!-- image -->

SUPPDAC

## NUMVMIDC,bits [31:28]

Indicates the number of Virtual Context Identifier Comparators that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMVMIDC         | Meaning                                                                      |
|------------------|------------------------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Virtual Context Identifier Comparators in this implementation. |

All other values are reserved.

If the PE does not implement EL2 then this field is 0b0000 .

Access to this field is RO.

## NUMCIDC, bits [27:24]

Indicates the number of Context Identifier Comparators that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMCIDC          | Meaning                                                              |
|------------------|----------------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Context Identifier Comparators in this implementation. |

All other values are reserved.

Access to this field is RO.

ARM DDI 0487 M.a.a

## NUMSSCC, bits [23:20]

Indicates the number of Single-shot Comparator Controls that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMSSCC          | Meaning                                                               |
|------------------|-----------------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Single-shot Comparator Controls in this implementation. |

All other values are reserved.

Access to this field is RO.

## NUMRSPAIR, bits [19:16]

Indicates the number of resource selector pairs that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMRSPAIR        | Meaning                                                                  |
|------------------|--------------------------------------------------------------------------|
| 0b0000           | This implementation has zero resource selector pairs.                    |
| 0b0001 .. 0b1111 | The number of resource selector pairs in this implementation, minus one. |

All other values are reserved.

Access to this field is RO.

## NUMPC,bits [15:12]

Indicates the number of PE Comparator Inputs that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMPC            | Meaning                                                    |
|------------------|------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of PE Comparator Inputs in this implementation. |

All other values are reserved.

Access to this field is RO.

## Bits [11:9]

Reserved, RES0.

## SUPPDAC, bit [8]

When TRCIDR4.NUMACPAIRS != '0000':

Indicates whether data address comparisons are implemented. Data address comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SUPPDAC   | Meaning                                   |
|-----------|-------------------------------------------|
| 0b0       | Data address comparisons not implemented. |
| 0b1       | Data address comparisons implemented.     |

This field reads as 0b0 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## NUMDVC,bits [7:4]

Indicates the number of data value comparators. Data value comparators are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMDVC           | Meaning                                                      |
|------------------|--------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of data value comparators in this implementation. |

All other values are reserved.

This field reads as 0b0000 .

Access to this field is RO.

## NUMACPAIRS, bits [3:0]

Indicates the number of Address Comparator pairs that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMACPAIRS       | Meaning                                                        |
|------------------|----------------------------------------------------------------|
| 0b0000 .. 0b1000 | The number of Address Comparator pairs in this implementation. |

All other values are reserved.

Access to this field is RO.

## Accessing TRCIDR4

TRCIDR4 can be accessed through the external debug interface:

## Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1F0    | TRCIDR4    |

## H9.3.38 TRCIDR5, Trace ID Register 5

The TRCIDR5 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR5 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR5[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR5 are RES0.

## Attributes

TRCIDR5 is a 32-bit register.

## Field descriptions

<!-- image -->

## OE, bit [31]

Indicates support for the ETE Trace Output Enable.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OE   | Meaning                                     |
|------|---------------------------------------------|
| 0b0  | ETE Trace Output Enable is not implemented. |
| 0b1  | ETE Trace Output Enable is implemented.     |

When FEAT\_ETEv1p3 is implemented and when any IMPLEMENTATION DEFINED trace output interface is implemented, this field is 1.

Access to this field is RO.

## NUMCNTR,bits [30:28]

Indicates the number of Counters that are available for tracing.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMCNTR        | Meaning                             |
|----------------|-------------------------------------|
| 0b000 .. 0b100 | The number of Counters implemented. |

All other values are reserved.

If TRCIDR4.NUMRSPAIR == 0b0000 then this field is 0b000 .

Access to this field is RO.

## NUMSEQSTATE, bits [27:25]

Indicates if the Sequencer is implemented and the number of Sequencer states that are implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMSEQSTATE   | Meaning                                |
|---------------|----------------------------------------|
| 0b000         | The Sequencer is not implemented.      |
| 0b100         | Four Sequencer states are implemented. |

All other values are reserved.

If TRCIDR4.NUMRSPAIR == 0b0000 then this field is 0b000 .

Access to this field is RO.

## Bit [24]

Reserved, RES0.

## LPOVERRIDE, bit [23]

Indicates support for Low-power Override Mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LPOVERRIDE   | Meaning                                                  |
|--------------|----------------------------------------------------------|
| 0b0          | The trace unit does not support Low-power Override Mode. |
| 0b1          | The trace unit supports Low-power Override Mode.         |

Access to this field is RO.

## ATBTRIG, bit [22]

Indicates if the implementation can support ATB triggers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ATBTRIG   | Meaning                                           |
|-----------|---------------------------------------------------|
| 0b0       | The implementation does not support ATB triggers. |
| 0b1       | The implementation supports ATB triggers.         |

If TRCIDR4.NUMRSPAIR == 0b0000 then this field is 0.

Access to this field is RO.

## TRACEIDSIZE, bits [21:16]

Indicates the trace ID width.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TRACEIDSIZE   | Meaning                                          |
|---------------|--------------------------------------------------|
| 0b000000      | The external trace interface is not implemented. |
| 0b000111      | The implementation supports a 7-bit trace ID.    |

All other values are reserved.

Note

AMBAATBrequires a 7-bit trace ID width.

Access to this field is RO.

## Bits [15:12]

Reserved, RES0.

## NUMEXTINSEL, bits [11:9]

Indicates how many External Input Selector resources are implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NUMEXTINSEL    | Meaning                                                      |
|----------------|--------------------------------------------------------------|
| 0b000 .. 0b100 | The number of External Input Selector resources implemented. |

All other values are reserved.

Access to this field is RO.

## NUMEXTIN, bits [8:0]

Indicates how many External Inputs are implemented.

| NUMEXTIN    | Meaning                     |
|-------------|-----------------------------|
| 0b111111111 | Unified PMUevent selection. |

All other values are reserved.

Access to this field is RO.

## Accessing TRCIDR5

TRCIDR5 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1F4    | TRCIDR5    |

## Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.39 TRCIDR6, Trace ID Register 6

The TRCIDR6 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR6 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR6[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR6 are RES0.

## Attributes

TRCIDR6 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

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

TRCIDR6 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1F8    | TRCIDR6    |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| EXLEVEL_RL_EL1   | Meaning                       |
|------------------|-------------------------------|
| 0b0              | Realm EL1 is not implemented. |
| 0b1              | Realm EL1 is implemented.     |

## H9.3.40 TRCIDR7, Trace ID Register 7

The TRCIDR7 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR7 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR7[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR7 are RES0.

## Attributes

TRCIDR7 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCIDR7

TRCIDR7 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1FC    | TRCIDR7    |

## Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.41 TRCIDR8, Trace ID Register 8

The TRCIDR8 characteristics are:

## Purpose

Returns the maximum speculation depth of the instruction trace element stream.

## Configuration

External register TRCIDR8 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR8[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR8 are RES0.

## Attributes

TRCIDR8 is a 32-bit register.

## Field descriptions

| 31      | 0   |
|---------|-----|
| MAXSPEC |     |

## MAXSPEC, bits [31:0]

Indicates the maximum speculation depth of the instruction trace element stream. This is the maximum number of P0 elements in the trace element stream that can be speculative at any time.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRCIDR8

TRCIDR8 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x180    | TRCIDR8    |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.42 TRCIDR9, Trace ID Register 9

The TRCIDR9 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

External register TRCIDR9 bits [31:0] are architecturally mapped to AArch64 System register TRCIDR9[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIDR9 are RES0.

## Attributes

TRCIDR9 is a 32-bit register.

## Field descriptions

| 31       | 0   |
|----------|-----|
| NUMP0KEY |     |

## NUMP0KEY, bits [31:0]

## When TRCIDR0.TRCDATA != '00':

Indicates the number of P0 right-hand keys. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRCIDR9

TRCIDR9 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x184    | TRCIDR9    |

Accessible as follows:

- When OSLockStatus() or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.43 TRCIMSPEC0, Trace IMP DEF Register 0

The TRCIMSPEC0 characteristics are:

## Purpose

TRCIMSPEC0 shows the presence of any IMPLEMENTATION DEFINED features, and provides an interface to enable the features that are provided.

## Configuration

External register TRCIMSPEC0 bits [31:0] are architecturally mapped to AArch64 System register TRCIMSPEC0[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIMSPEC0 are RES0.

## Attributes

TRCIMSPEC0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

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
| 0b1010 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |
| 0b1011 | The trace unit behavior is IMPLEMENTATION DEFINED.                                                                                           |

| EN     | Meaning                                            |
|--------|----------------------------------------------------|
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

TRCIMSPEC0 can be accessed through the external debug interface:

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x1C0    | TRCIMSPEC0 |

## H9.3.44 TRCIMSPEC&lt;n&gt;, Trace IMP DEF Register &lt;n&gt;, n = 1 - 7

The TRCIMSPEC&lt;n&gt; characteristics are:

## Purpose

These registers might return information that is specific to an implementation, or enable features specific to an implementation to be programmed. The product Technical Reference Manual describes these registers.

## Configuration

External register TRCIMSPEC&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCIMSPEC&lt;n&gt;[31:0].

This register is present only when an implementation implements TRCIMSPEC&lt;n&gt;, FEAT\_ETE is implemented, and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCIMSPEC&lt;n&gt; are RES0.

## Attributes

TRCIMSPEC&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

| 31                     | 0   |
|------------------------|-----|
| IMPLEMENTATION DEFINED |     |

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

This field reads as an IMPLEMENTATION DEFINED value and writes to this field have IMPLEMENTATION DEFINED behavior.

## Accessing TRCIMSPEC&lt;n&gt;

TRCIMSPEC&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance              |
|-------------|------------------------------|
| ETE         | 0x1C0 + (4 * n) TRCIMSPEC<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.45 TRCITCTRL, Trace Integration Mode Control Register

The TRCITCTRL characteristics are:

## Purpose

Acomponent can use TRCITCTRL to dynamically switch between functional mode and integration mode. In integration mode, topology detection is enabled. After switching to integration mode and performing integration tests or topology detection, reset the system to ensure correct behavior of CoreSight and other connected system components.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCITCTRL are RES0.

## Attributes

TRCITCTRL is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 1 0   |
|------|-------|
| RES0 | IME   |

## Bits [31:1]

Reserved, RES0.

## IME, bit [0]

When topology detection or integration functionality is implemented:

Integration Mode Enable.

| IME   | Meaning                                                                                        |
|-------|------------------------------------------------------------------------------------------------|
| 0b0   | Component functional mode.                                                                     |
| 0b1   | Component integration mode. Support for topology detection and integration testing is enabled. |

## Otherwise:

Reserved, RES0.

## Accessing TRCITCTRL

External debugger accesses to this register are IMPLEMENTATION DEFINED when the trace unit is not in the Idle state.

TRCITCTRL can be accessed through the external debug interface:

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xF00    | TRCITCTRL  |

## H9.3.46 TRCITEEDCR, Instrumentation Trace Extension External Debug Control Register

The TRCITEEDCR characteristics are:

## Purpose

Controls instrumentation trace filtering.

## Configuration

External register TRCITEEDCR bits [31:0] are architecturally mapped to AArch64 System register TRCITEEDCR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and FEAT\_ITE is implemented. Otherwise, direct accesses to TRCITEEDCR are RES0.

## Attributes

TRCITEEDCR is a 32-bit register.

## Field descriptions

| 31   | 7 6 5 4 3 2 1 0   |
|------|-------------------|

## Bits [31:7]

Reserved, RES0.

## RL, bit [6]

## When FEAT\_RME is implemented:

Instrumentation Trace in Realm state.

| RL   | Meaning                                          |
|------|--------------------------------------------------|
| 0b0  | Instrumentation trace prohibited in Realm state. |
| 0b1  | Instrumentation trace permitted in Realm state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Realm state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

S, bit [5]

## When Secure state is implemented:

Instrumentation Trace in Secure state.

| S   | Meaning                                           |
|-----|---------------------------------------------------|
| 0b0 | Instrumentation trace prohibited in Secure state. |
| 0b1 | Instrumentation trace permitted in Secure state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

When FEAT\_RME is not implemented, this field is used in conjunction with TRCCONFIGR.ITO, TRCITEEDCR.E3, and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Secure state.

When FEAT\_RME is implemented, this field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Secure state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NS, bit [4]

## When Non-secure state is implemented:

Instrumentation Trace in Non-secure state.

| NS   | Meaning                                               |
|------|-------------------------------------------------------|
| 0b0  | Instrumentation trace prohibited in Non-secure state. |
| 0b1  | Instrumentation trace permitted in Non-secure state.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This field is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.E&lt;m&gt; to control whether Instrumentation trace is permitted or prohibited in Non-secure state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E3, bit [3]

## When EL3 is implemented:

Instrumentation Trace Enable at EL3.

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| E3   | Meaning                                  |
|------|------------------------------------------|
| 0b0  | Instrumentation trace prohibited at EL3. |
| 0b1  | Instrumentation trace permitted at EL3.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

When FEAT\_RME is not implemented, TRCITEEDCR.E3 is used in conjunction with TRCCONFIGR.ITO and TRCITEEDCR.S to control whether Instrumentation trace is permitted or prohibited at EL3.

When FEAT\_RME is implemented, TRCITEEDCR.E3 is used in conjunction with TRCCONFIGR.ITO to control whether Instrumentation trace is permitted or prohibited at EL3.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E&lt;m&gt;, bits [m], for m = 2 to 0

Instrumentation Trace Enable at EL&lt;m&gt;.

| E<m>   | Meaning                                    |
|--------|--------------------------------------------|
| 0b0    | Instrumentation trace prohibited at EL<m>. |
| 0b1    | Instrumentation trace permitted at EL<m>.  |

This field is ignored when SelfHostedTraceEnabled() returns TRUE.

This bit is used in conjunction with TRCCONFIGR.ITO, TRCITEEDCR.NS, TRCITEEDCR.S, and TRCITEEDCR.RL to control whether Instrumentation trace is permitted or prohibited at EL&lt;m&gt; in the specified Security states.

TRCITEEDCR.E&lt;2&gt; is RES0 if EL2 is not implemented in any Security states.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCITEEDCR

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCITEEDCR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x048    | TRCITEEDCR |

## H9.3.47 TRCLAR, Trace Lock Access Register

The TRCLAR characteristics are:

## Purpose

Used to lock and unlock the Software Lock.

Note

ETE does not implement the Software Lock.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and ETE Software Lock is implemented. Otherwise, direct accesses to TRCLAR are RES0.

## Attributes

TRCLAR is a 32-bit register.

## Field descriptions

## KEY, bits [31:0]

## When ETE Software Lock is implemented:

Software Lock Key.

Avalue of 0xC5ACCE55 unlocks the Software Lock.

Any other value locks the Software Lock.

## Otherwise:

Reserved, RES0.

## Accessing TRCLAR

External debugger accesses to this register are unaffected by the OS Lock.

TRCLAR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFB0    | TRCLAR     |

31

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are WO.

KEY

0

## H9.3.48 TRCLSR, Trace Lock Status Register

The TRCLSR characteristics are:

## Purpose

Indicates whether the Software Lock is implemented, and the current status of the Software Lock.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCLSR are RES0.

## Attributes

TRCLSR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 3   | 2   | 1 0   |
|------|-----|-----|-------|
| RES0 | 0   | SLK | SLI   |
|      |     |     | nTT   |

## Bits [31:3]

Reserved, RES0.

## nTT, bit [2]

Software lock size.

Reads as 0b0

Access to this field is RO.

## SLK, bit [1]

The current Software Lock status.

| SLK   | Meaning                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0b0   | Software Lock is unlocked.                                                                                    |
| 0b1   | Software Lock is locked. Writes to the other registers in this component, except for the TRCLAR, are ignored. |

This field reads as 0.

## SLI, bit [0]

Indicates whether the Software Lock is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SLI   | Meaning                                                            |
|-------|--------------------------------------------------------------------|
| 0b0   | Software Lock is not implemented. Writes to theTRCLAR are ignored. |
| 0b1   | Software Lock is implemented.                                      |

This field reads as 0.

Access to this field is RO.

## Accessing TRCLSR

External debugger accesses to this register are unaffected by the OS Lock.

TRCLSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFB4    | TRCLSR     |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.49 TRCOSLSR, Trace OS Lock Status Register

The TRCOSLSR characteristics are:

## Purpose

Returns the status of the Trace OS Lock.

## Configuration

External register TRCOSLSR bits [31:0] are architecturally mapped to AArch64 System register TRCOSLSR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCOSLSR are RES0.

## Attributes

TRCOSLSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:5]

Reserved, RES0.

## OSLM, bits [4:3, 0]

OS Lock model.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OSLM   | Meaning                                                                               |
|--------|---------------------------------------------------------------------------------------|
| 0b000  | Trace OS Lock is not implemented.                                                     |
| 0b010  | Trace OS Lock is implemented.                                                         |
| 0b100  | Trace OS Lock is not implemented, and the trace unit is controlled by the PE OS Lock. |

All other values are reserved.

When FEAT\_ETE is implemented, the values 0b000 and 0b010 are not permitted.

Access to this field is RO.

## Bit [2]

Reserved, RES0.

## OSLK, bit [1]

OS Lock status.

## Accessible as follows:

- When !AllowExternalTraceAccess(addrdesc) or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| OSLK   | Meaning                  |
|--------|--------------------------|
| 0b0    | The OS Lock is unlocked. |
| 0b1    | The OS Lock is locked.   |

When FEAT\_ETE is implemented, this field indicates the state of the PE OS Lock.

When FEAT\_ETMv4 is implemented, this field indicates the state of the Trace OS Lock.

## Accessing TRCOSLSR

External debugger accesses to this register are unaffected by the OS Lock.

TRCOSLSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x304    | TRCOSLSR   |

## H9.3.50 TRCPDCR, Trace PowerDown Control Register

The TRCPDCR characteristics are:

## Purpose

Requests the system to provide power to the trace unit.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPDCR are RES0.

## Attributes

TRCPDCR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 4 3   | 0    |
|------|-------|------|
|      | PU    | RES0 |

## Bits [31:4]

Reserved, RES0.

## PU, bit [3]

Power Up Request.

| PU   | Meaning                                                                                                                                                                 |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | The system can remove power from the trace unit core power domain, or requests for power to the trace unit core power domain are implemented outside of the trace unit. |
| 0b1  | The system must provide power to the trace unit core power domain.                                                                                                      |

This field is RES0.

## Bits [2:0]

Reserved, RES0.

## Accessing TRCPDCR

External debugger accesses to this register are unaffected by the OS Lock.

TRCPDCR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x310    | TRCPDCR    |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.51 TRCPDSR, Trace PowerDown Status Register

The TRCPDSR characteristics are:

## Purpose

Indicates the power status of the trace unit.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPDSR are RES0.

## Attributes

TRCPDSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:6]

Reserved, RES0.

## OSLK, bit [5]

OS Lock Status.

Note

This field indicates the state of the PE OS Lock.

## Bits [4:2]

Reserved, RES0.

## STICKYPD, bit [1]

Sticky powerdown status. Indicates whether the trace register state is valid.

| STICKYPD   | Meaning                                                  |
|------------|----------------------------------------------------------|
| 0b0        | The state of TRCOSLSR and the trace registers are valid. |

| OSLK   | Meaning                  |
|--------|--------------------------|
| 0b0    | The OS Lock is unlocked. |
| 0b1    | The OS Lock is locked.   |

| STICKYPD   | Meaning                                                           |
|------------|-------------------------------------------------------------------|
| 0b1        | The state of TRCOSLSR and the trace registers might not be valid. |

This field is set to 1 if the power to the trace unit core power domain is removed and the trace unit register state is not valid.

The STICKYPD field is read-sensitive. On a read of the TRCPDSR, this field is cleared to 0 after the register has been read.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RC/WI.

## POWER,bit [0]

Power Status.

| POWER   | Meaning                                                                                                                             |
|---------|-------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | The trace unit core power domain is not powered. All trace unit registers are not accessible and they all return an error response. |
| 0b1     | The trace unit core power domain is powered. Trace unit registers are accessible.                                                   |

Access to this field is RAO/WI.

## Accessing TRCPDSR

External debugger accesses to this register are unaffected by the OS Lock.

TRCPDSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x314    | TRCPDSR    |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.52 TRCPIDR0, Trace Peripheral Identification Register 0

The TRCPIDR0 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR0 are RES0.

## Attributes

TRCPIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PART\_0, bits [7:0]

Part number, bits [7:0].

The part number is selected by the designer of the component, and is stored in TRCPIDR1.PART\_1 and TRCPIDR0.PART\_0.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRCPIDR0

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFE0    | TRCPIDR0   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.53 TRCPIDR1, Trace Peripheral Identification Register 1

The TRCPIDR1 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR1 are RES0.

## Attributes

TRCPIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## DES\_0, bits [7:4]

Designer, JEP106 identification code, bits [3:0].

JEP106 identification and continuation codes, which are stored as follows:

- TRCPIDR1.DES\_0: JEP106 identification code bits[3:0].
- TRCPIDR2.DES\_1: JEP106 identification code bits[6:4].
- TRCPIDR4.DES\_2: JEP106 continuation code.

These codes indicate the designer of the component and not the implementer, except where the two are the same.

To obtain a number, or to see the assignment of these codes, contact JEDEC http://www.jedec.org.

AJEDEC code takes the following form:

- Asequence of zero or more numbers, all having the value 0x7F .
- Afollowing 8-bit number, that is not 0x7F , and where bit[7] is an odd parity bit.

The parity bit in the JEP106 identification code is not included.

This field has an IMPLEMENTATION DEFINED value.

## Note

For example, Arm Limited is assigned the code 0x7F 0x7F 0x7F 0x7F 0x3B .

- The continuation code is the number of times 0x7F appears before the final number. For example, a component designed by Arm Limited has the code 0x4 .
- The identification code is bits[6:0] of the final number. For example, a component designed by Arm Limited has the code 0x3B .

Access to this field is RO.

## PART\_1, bits [3:0]

Part number, bits [11:8].

The part number is selected by the designer of the component, and is stored in TRCPIDR1.PART\_1 and TRCPIDR0.PART\_0.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRCPIDR1

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFE4    | TRCPIDR1   |

## Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.54 TRCPIDR2, Trace Peripheral Identification Register 2

The TRCPIDR2 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR2 are RES0.

## Attributes

TRCPIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## REVISION, bits [7:4]

Component major revision.

TRCPIDR2.REVISION and TRCPIDR3.REVAND together form the revision number of the component, with TRCPIDR2.REVISION being the most significant part and TRCPIDR3.REVAND the least significant part.

When a component is changed, TRCPIDR2.REVISION or TRCPIDR3.REVAND are increased to ensure that software can differentiate the different revisions of the component. TRCPIDR3.REV AND should be set to 0b0000 when TRCPIDR2.REVISION is increased.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## JEDEC, bit [3]

JEDEC-assigned JEP106 implementer code is used.

Reads as 0b1

Access to this field is RO.

## DES\_1, bits [2:0]

Designer, JEP106 identification code, bits [6:4].

JEP106 identification and continuation codes, which are stored as follows:

- TRCPIDR1.DES\_0: JEP106 identification code bits[3:0].
- TRCPIDR2.DES\_1: JEP106 identification code bits[6:4].
- TRCPIDR4.DES\_2: JEP106 continuation code.

These codes indicate the designer of the component and not the implementer, except where the two are the same. To obtain a number, or to see the assignment of these codes, contact JEDEC http://www.jedec.org.

AJEDEC code takes the following form:

- Asequence of zero or more numbers, all having the value 0x7F .
- Afollowing 8-bit number, that is not 0x7F , and where bit[7] is an odd parity bit.

The parity bit in the JEP106 identification code is not included.

This field has an IMPLEMENTATION DEFINED value.

Note

For example, Arm Limited is assigned the code 0x7F 0x7F 0x7F 0x7F 0x3B .

- The continuation code is the number of times 0x7F appears before the final number. For example, a component designed by Arm Limited has the code 0x4 .
- The identification code is bits[6:0] of the final number. For example, a component designed by Arm Limited has the code 0x3B .

Access to this field is RO.

## Accessing TRCPIDR2

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFE8    | TRCPIDR2   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.55 TRCPIDR3, Trace Peripheral Identification Register 3

The TRCPIDR3 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR3 are RES0.

## Attributes

TRCPIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## REVAND, bits [7:4]

Component minor revision.

TRCPIDR2.REVISION and TRCPIDR3.REVAND together form the revision number of the component, with TRCPIDR2.REVISION being the most significant part and TRCPIDR3.REVAND the least significant part. When a component is changed, TRCPIDR2.REVISION or TRCPIDR3.REVAND are increased to ensure that software can differentiate the different revisions of the component. TRCPIDR3.REV AND should be set to 0b0000 when TRCPIDR2.REVISION is increased.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CMOD,bits [3:0]

Customer Modified.

Indicates the component has been modified.

Avalue of 0b0000 means the component is not modified from the original design.

Any other value means the component has been modified in an IMPLEMENTATION DEFINED way.

This field has an IMPLEMENTATION DEFINED value.

For any two components with the same Unique Component Identifier:

- If the value of the CMOD fields of both components equals zero, the components are identical.
- If the CMOD fields of both components have the same nonzero value, it does not necessarily mean that they have the same modifications.
- If the value of the CMOD field of either of the two components is nonzero, they might not be identical, even though they have the same Unique Component Identifier.

Access to this field is RO.

## Accessing TRCPIDR3

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFEC    | TRCPIDR3   |

## Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.56 TRCPIDR4, Trace Peripheral Identification Register 4

The TRCPIDR4 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR4 are RES0.

## Attributes

TRCPIDR4 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7   | 4 3   |
|------|-------|-------|
| RES0 | SIZE  | DES_2 |

## Bits [31:8]

Reserved, RES0.

## SIZE, bits [7:4]

Size of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SIZE             | Meaning                                            |
|------------------|----------------------------------------------------|
| 0b0000           | One of the following is true:                      |
| 0b0001 .. 0b1111 | The component occupies 2 TRCPIDR4.SIZE 4KB blocks. |

Using this field to indicate the size of the component is deprecated. This field might not correctly indicate the size of the component. Arm recommends that software determine the size of the component from the Unique Component Identifier fields, and other IMPLEMENTATION DEFINED registers in the component.

This field has the value 0b0000 .

Access to this field is RO.

## DES\_2, bits [3:0]

Designer, JEP106 continuation code.

JEP106 identification and continuation codes, which are stored as follows:

- TRCPIDR1.DES\_0: JEP106 identification code bits[3:0].

- TRCPIDR2.DES\_1: JEP106 identification code bits[6:4].
- TRCPIDR4.DES\_2: JEP106 continuation code.

These codes indicate the designer of the component and not the implementer, except where the two are the same. To obtain a number, or to see the assignment of these codes, contact JEDEC http://www.jedec.org.

AJEDEC code takes the following form:

- Asequence of zero or more numbers, all having the value 0x7F .
- Afollowing 8-bit number, that is not 0x7F , and where bit[7] is an odd parity bit.

The parity bit in the JEP106 identification code is not included.

This field has an IMPLEMENTATION DEFINED value.

## Note

For example, Arm Limited is assigned the code 0x7F 0x7F 0x7F 0x7F 0x3B .

- The continuation code is the number of times 0x7F appears before the final number. For example, a component designed by Arm Limited has the code 0x4 .
- The identification code is bits[6:0] of the final number. For example, a component designed by Arm Limited has the code 0x3B .

Access to this field is RO.

## Accessing TRCPIDR4

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR4 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFD0    | TRCPIDR4   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.57 TRCPIDR5, Trace Peripheral Identification Register 5

The TRCPIDR5 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR5 are RES0.

## Attributes

TRCPIDR5 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCPIDR5

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR5 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFD4    | TRCPIDR5   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.58 TRCPIDR6, Trace Peripheral Identification Register 6

The TRCPIDR6 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR6 are RES0.

## Attributes

TRCPIDR6 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCPIDR6

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR6 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFD8    | TRCPIDR6   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.59 TRCPIDR7, Trace Peripheral Identification Register 7

The TRCPIDR7 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPIDR7 are RES0.

## Attributes

TRCPIDR7 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRCPIDR7

External debugger accesses to this register are unaffected by the OS Lock.

TRCPIDR7 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0xFDC    | TRCPIDR7   |

Accessible as follows:

- When !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.60 TRCPRGCTLR, Trace Programming Control Register

The TRCPRGCTLR characteristics are:

## Purpose

Enables the trace unit.

## Configuration

External register TRCPRGCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCPRGCTLR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCPRGCTLR are RES0.

## Attributes

TRCPRGCTLR is a 32-bit register.

## Field descriptions

| 31   | 1 0   |
|------|-------|
|      | EN    |

## Bits [31:1]

Reserved, RES0.

## EN, bit [0]

Trace unit enable.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to '0' .

## Accessing TRCPRGCTLR

Must be programmed.

TRCPRGCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x004    | TRCPRGCTLR |

Accessible as follows:

| EN   | Meaning                     |
|------|-----------------------------|
| 0b0  | The trace unit is disabled. |
| 0b1  | The trace unit is enabled.  |

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.61 TRCQCTLR, Trace Q Element Control Register

The TRCQCTLR characteristics are:

## Purpose

Controls when Q elements are enabled.

## Configuration

External register TRCQCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCQCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR0.QFILT == '1'. Otherwise, direct accesses to TRCQCTLR are RES0.

## Attributes

TRCQCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:9]

Reserved, RES0.

## MODE,bit [8]

Selects whether the Address Range Comparators selected by TRCQCTLR.RANGE indicate address ranges where the trace unit is permitted to generate Q elements or address ranges where the trace unit is not permitted to generate Qelements:

| MODE   | Meaning                                                                                                                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Exclude mode. The Address Range Comparators selected by TRCQCTLR.RANGE indicate address ranges where the trace unit must not generate Qelements. If no ranges are selected, Qelements are permitted across the entire memory map. |
| 0b1    | Include Mode. The Address Range Comparators selected by TRCQCTLR.RANGE indicate address ranges where the trace unit can generate Qelements. If all the implemented bits in RANGEare set to 0 thenQ elements are disabled.         |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## RANGE[&lt;m&gt;] , bits [m], for m = 7 to 0

Specifies whether Address Range Comparator &lt;m&gt; controls Q elements.

| RANGE[<m>]   | Meaning                                                                      |
|--------------|------------------------------------------------------------------------------|
| 0b0          | The address range that Address Range Comparator <m> defines is not selected. |
| 0b1          | The address range that Address Range Comparator <m> defines is selected.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCQCTLR

Must be programmed if TRCCONFIGR.QE != 0b00 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCQCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x044    | TRCQCTLR   |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.62 TRCRSCTLR&lt;n&gt;, Trace Resource Selection Control Register &lt;n&gt;, n = 2 - 31

The TRCRSCTLR&lt;n&gt; characteristics are:

## Purpose

Controls the selection of the resources in the trace unit.

## Configuration

Resource selector 0 always returns FALSE.

Resource selector 1 always returns TRUE.

Resource selectors are implemented in pairs. Each odd numbered resource selector is part of a pair with the even numbered resource selector that is numbered as one less than it. For example, resource selectors 2 and 3 form a pair.

External register TRCRSCTLR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCRSCTLR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and ((UInt(TRCIDR4.NUMRSPAIR) + 1) * 2) &gt; n. Otherwise, direct accesses to TRCRSCTLR&lt;n&gt; are RES0.

## Attributes

TRCRSCTLR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:22]

Reserved, RES0.

## PAIRINV, bit [21]

When (n MOD 2) == 0:

Controls whether the combined result from a resource selector pair is inverted.

| PAIRINV   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0       | Do not invert the combined output of the 2 resource selectors. |
| 0b1       | Invert the combined output of the 2 resource selectors.        |

If:

- Ais the register TRCRSCTLR&lt;n&gt;.
- Bis the register TRCRSCTLR&lt;n+1&gt;.

Then the combined output of the 2 resource selectors A and B depends on the value of (A.PAIRINV , A.INV , B.INV) as follows:

- 0b000 -&gt; A and B.

- 0b001 -&gt; Reserved.
- 0b010 -&gt; not(A) and B.
- 0b011 -&gt; not(A) and not(B).
- 0b100 -&gt; not(A) or not(B).
- 0b101 -&gt; not(A) or B.
- 0b110 -&gt; Reserved.
- 0b111 -&gt; A or B.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## INV, bit [20]

Controls whether the resource, that TRCRSCTLR&lt;n&gt;.GROUP and TRCRSCTLR&lt;n&gt;.SELECT selects, is inverted.

| INV   | Meaning                                    |
|-------|--------------------------------------------|
| 0b0   | Do not invert the output of this selector. |
| 0b1   | Invert the output of this selector.        |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## GROUP, bits [19:16]

Selects a group of resources.

| GROUP   | Meaning                                 | SELECT                                                     |
|---------|-----------------------------------------|------------------------------------------------------------|
| 0b0000  | External Input Selectors.               | SELECT encoding for External Input Selectors               |
| 0b0001  | PE Comparator Inputs.                   | SELECT encoding for PE Comparator Inputs                   |
| 0b0010  | Counters and Sequencer.                 | SELECT encoding for Counters and Sequencer                 |
| 0b0011  | Single-shot Comparator Controls.        | SELECT encoding for Single-shot Comparator Controls        |
| 0b0100  | Single Address Comparators.             | SELECT encoding for Single Address Comparators             |
| 0b0101  | Address Range Comparators.              | SELECT encoding for Address Range Comparators              |
| 0b0110  | Context Identifier Comparators.         | SELECT encoding for Context Identifier Comparators         |
| 0b0111  | Virtual Context Identifier Comparators. | SELECT encoding for Virtual Context Identifier Comparators |

All other values are reserved.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT, bits [15:0]

Resource Specific Controls. Contains the controls specific to the resource group selected by GROUP, described in the following sections.

## SELECT encoding for External Input Selectors

<!-- image -->

| EXTIN[<m>]   | Meaning           |
|--------------|-------------------|
| 0b0          | Ignore EXTIN <m>. |
| 0b1          | Select EXTIN <m>. |

This bit is RES0 if m &gt;= TRCIDR5.NUMEXTINSEL.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for PE Comparator Inputs

<!-- image -->

## Bits [15:4]

Reserved, RES0.

## EXTIN[&lt;m&gt;] , bits [m], for m = 3 to 0

Selects one or more External Inputs.

## Bits [15:8]

Reserved, RES0.

PECOMP[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more PE Comparator Inputs.

## Bits [15:8]

Reserved, RES0.

SEQUENCER[&lt;m&gt;] , bits [m+4], for m = 3 to 0

Sequencer states.

| PECOMP[<m>]   | Meaning                         |
|---------------|---------------------------------|
| 0b0           | Ignore PE Comparator Input <m>. |
| 0b1           | Select PE Comparator Input <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMPC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Counters and Sequencer

<!-- image -->

| SEQUENCER[<m>]   | Meaning                     |
|------------------|-----------------------------|
| 0b0              | Ignore Sequencer state <m>. |
| 0b1              | Select Sequencer state <m>. |

This bit is RES0 if m &gt;= TRCIDR5.NUMSEQSTATE.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## COUNTERS[&lt;m&gt;] , bits [m], for m = 3 to 0

Counters resources at zero.

| COUNTERS[<m>]   | Meaning             |
|-----------------|---------------------|
| 0b0             | Ignore Counter <m>. |

## Bits [15:8]

Reserved, RES0.

## SINGLE\_SHOT[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Single-shot Comparator Controls.

| SINGLE_SHOT[<m>]   | Meaning                                    |
|--------------------|--------------------------------------------|
| 0b0                | Ignore Single-shot Comparator Control <m>. |
| 0b1                | Select Single-shot Comparator Control <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMSSCC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Single Address Comparators

| COUNTERS[<m>]   | Meaning                     |
|-----------------|-----------------------------|
| 0b1             | Select Counter <m> is zero. |

This bit is RES0 if m &gt;= TRCIDR5.NUMCNTR.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Single-shot Comparator Controls

<!-- image -->

## Bits [15:8]

Reserved, RES0.

ARC[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Address Range Comparators.

| ARC[<m>]   | Meaning                              |
|------------|--------------------------------------|
| 0b0        | Ignore Address Range Comparator <m>. |
| 0b1        | Select Address Range Comparator <m>. |

<!-- image -->

## SAC[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects one or more Single Address Comparators.

| SAC[<m>]   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | Ignore Single Address Comparator <m>. |
| 0b1        | Select Single Address Comparator <m>. |

This bit is RES0 if m &gt;= 2 × TRCIDR4.NUMACPAIRS.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Address Range Comparators

<!-- image -->

This bit is RES0 if m &gt;= TRCIDR4.NUMACPAIRS.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Context Identifier Comparators

<!-- image -->

## Bits [15:8]

Reserved, RES0.

## CID[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Context Identifier Comparators.

| CID[<m>]   | Meaning                                   |
|------------|-------------------------------------------|
| 0b0        | Ignore Context Identifier Comparator <m>. |
| 0b1        | Select Context Identifier Comparator <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMCIDC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SELECT encoding for Virtual Context Identifier Comparators

<!-- image -->

## Bits [15:8]

Reserved, RES0.

VMID[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more Virtual Context Identifier Comparators.

| VMID[<m>]   | Meaning                                           |
|-------------|---------------------------------------------------|
| 0b0         | Ignore Virtual Context Identifier Comparator <m>. |
| 0b1         | Select Virtual Context Identifier Comparator <m>. |

This bit is RES0 if m &gt;= TRCIDR4.NUMVMIDC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCRSCTLR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCCNTCTLR&lt;a&gt;.RLDEVENT.TYPE == 0 and TRCCNTCTLR&lt;a&gt;.RLDEVENT.SEL == n.
- TRCCNTCTLR&lt;a&gt;.RLDEVENT.TYPE == 1 and TRCCNTCTLR&lt;a&gt;.RLDEVENT.SEL == n/2.
- TRCCNTCTLR&lt;a&gt;.CNTEVENT.TYPE == 0 and TRCCNTCTLR&lt;a&gt;.CNTEVENT.SEL == n.
- TRCCNTCTLR&lt;a&gt;.CNTEVENT.TYPE == 1 and TRCCNTCTLR&lt;a&gt;.CNTEVENT.SEL == n/2.
- TRCEVENTCTL0R.EVENT0.TYPE == 0 and TRCEVENTCTL0R.EVENT0.SEL == n.
- TRCEVENTCTL0R.EVENT0.TYPE == 1 and TRCEVENTCTL0R.EVENT0.SEL == n/2.
- TRCEVENTCTL0R.EVENT1.TYPE == 0 and TRCEVENTCTL0R.EVENT1.SEL == n.
- TRCEVENTCTL0R.EVENT1.TYPE == 1 and TRCEVENTCTL0R.EVENT1.SEL == n/2.
- TRCEVENTCTL0R.EVENT2.TYPE == 0 and TRCEVENTCTL0R.EVENT2.SEL == n.
- TRCEVENTCTL0R.EVENT2.TYPE == 1 and TRCEVENTCTL0R.EVENT2.SEL == n/2.
- TRCEVENTCTL0R.EVENT3.TYPE == 0 and TRCEVENTCTL0R.EVENT3.SEL == n.
- TRCEVENTCTL0R.EVENT3.TYPE == 1 and TRCEVENTCTL0R.EVENT3.SEL == n/2.
- TRCSEQEVR&lt;a&gt;.B.TYPE == 0 and TRCSEQEVR&lt;a&gt;.B.SEL = n.
- TRCSEQEVR&lt;a&gt;.B.TYPE == 1 and TRCSEQEVR&lt;a&gt;.B.SEL = n/2.
- TRCSEQEVR&lt;a&gt;.F.TYPE == 0 and TRCSEQEVR&lt;a&gt;.F.SEL = n.
- TRCSEQEVR&lt;a&gt;.F.TYPE == 1 and TRCSEQEVR&lt;a&gt;.F.SEL = n/2.
- TRCSEQRSTEVR.RST.TYPE == 0 and TRCSEQRSTEVR.RST.SEL == n.
- TRCSEQRSTEVR.RST.TYPE == 1 and TRCSEQRSTEVR.RST.SEL == n/2.
- TRCTSCTLR.EVENT.TYPE == 0 and TRCTSCTLR.EVENT.SEL == n.
- TRCTSCTLR.EVENT.TYPE == 1 and TRCTSCTLR.EVENT.SEL == n/2.
- TRCVICTLR.EVENT.TYPE == 0 and TRCVICTLR.EVENT.SEL == n.
- TRCVICTLR.EVENT.TYPE == 1 and TRCVICTLR.EVENT.SEL == n/2.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCRSCTLR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance              |
|-------------|------------------------------|
| ETE         | 0x200 + (4 * n) TRCRSCTLR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.63 TRCRSR, Trace Resources Status Register

The TRCRSR characteristics are:

## Purpose

Use this to set, or read, the status of the resources.

## Configuration

External register TRCRSR bits [31:0] are architecturally mapped to AArch64 System register TRCRSR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCRSR are RES0.

## Attributes

TRCRSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:13]

Reserved, RES0.

## TA, bit [12]

Tracing active.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## EVENT[&lt;m&gt;] , bits [m+8], for m = 3 to 0

Untraced status of ETEEvents.

| TA   | Meaning                |
|------|------------------------|
| 0b0  | Tracing is not active. |
| 0b1  | Tracing is active.     |

| EVENT[<m>]   | Meaning                                                                    |
|--------------|----------------------------------------------------------------------------|
| 0b0          | An ETEEvent <m> has not occurred.                                          |
| 0b1          | An ETEEvent <m> has occurred while the resources were in the Paused state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When TRCIDR4.NUMRSPAIR == '0000', access to this field is RES0.
- Access to this field is RES0 if all of the following are true:
- TRCIDR4.NUMRSPAIR != '0000'
- m&gt;UInt(TRCIDR0.NUMEVENT)
- Otherwise, access to this field is RW.

## Bits [7:4]

Reserved, RES0.

## EXTIN[&lt;m&gt;] , bits [m], for m = 3 to 0

The sticky status of the External Input Selectors.

| EXTIN[<m>]   | Meaning                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0          | An event selected by External Input Selector <m> has not occurred.                                                    |
| 0b1          | At least one event selected by External Input Selector <m> has occurred while the resources were in the Paused state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR5.NUMEXTINSEL), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCRSR

Must always be programmed.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

TRCRSR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x028    | TRCRSR     |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.64 TRCSEQEVR&lt;n&gt;, Trace Sequencer State Transition Control Register &lt;n&gt;, n = 0 - 2

The TRCSEQEVR&lt;n&gt; characteristics are:

## Purpose

Moves the Sequencer state:

- Backwards, from state n+1 to state n when a programmed resource event occurs.
- Forwards, from state n to state n+1 when a programmed resource event occurs.

## Configuration

External register TRCSEQEVR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCSEQEVR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQEVR&lt;n&gt; are RES0.

## Attributes

TRCSEQEVR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## B\_TYPE, bit [15]

Backward field. Selects an event that causes the Sequencer to move from state n+1 to state n. For example, if TRCSEQEVR2.B.SEL == 0x14 , then when event 0x14 occurs, the Sequencer moves from state 3 to state 2.

Chooses the type of Resource Selector.

| B_TYPE   | Meaning                                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Asingle Resource Selector. TRCSEQEVR.B.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                |
| 0b1      | ABoolean-combined pair of Resource Selectors. TRCSEQEVR.B.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQEVR.B.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [14:13]

Reserved, RES0.

## B\_SEL, bits [12:8]

Backward field. Selects an event that causes the Sequencer to move from state n+1 to state n. For example, if TRCSEQEVR2.B.SEL == 0x14 , then when event 0x14 occurs, the Sequencer moves from state 3 to state 2.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQEVR.B.TYPE controls whether TRCSEQEVR.B.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## F\_TYPE, bit [7]

Forward field. Selects an event that causes the Sequencer to move from state n to state n+1. For example, if TRCSEQEVR1.F.SEL == 0x12 , then when event 0x12 occurs, the Sequencer moves from state 1 to state 2.

Chooses the type of Resource Selector.

| F_TYPE   | Meaning                                                                                                                                                                                                                                              |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | Asingle Resource Selector. TRCSEQEVR.F.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                |
| 0b1      | ABoolean-combined pair of Resource Selectors. TRCSEQEVR.F.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQEVR.F.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## F\_SEL, bits [4:0]

Forward field. Selects an event that causes the Sequencer to move from state n to state n+1. For example, if TRCSEQEVR1.F.SEL == 0x12 , then when event 0x12 occurs, the Sequencer moves from state 1 to state 2.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQEVR.F.TYPE controls whether TRCSEQEVR.F.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQEVR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCSEQEVR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance              |
|-------------|------------------------------|
| ETE         | 0x100 + (4 * n) TRCSEQEVR<n> |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.65 TRCSEQRSTEVR, Trace Sequencer Reset Control Register

The TRCSEQRSTEVR characteristics are:

## Purpose

Moves the Sequencer to state 0 when a programmed resource event occurs.

## Configuration

External register TRCSEQRSTEVR bits [31:0] are architecturally mapped to AArch64 System register TRCSEQRSTEVR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQRSTEVR are RES0.

## Attributes

TRCSEQRSTEVR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## RST\_TYPE, bit [7]

Reset field. Selects an event that causes the Sequencer to move to state 0.

Chooses the type of Resource Selector.

| RST_TYPE   | Meaning                                                                                                                                                                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | Asingle Resource Selector. TRCSEQRSTEVR.RST.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                     |
| 0b1        | ABoolean-combined pair of Resource Selectors. TRCSEQRSTEVR.RST.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCSEQRSTEVR.RST.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [6:5]

Reserved, RES0.

## RST\_SEL, bits [4:0]

Reset field. Selects an event that causes the Sequencer to move to state 0.

Defines the selected Resource Selector or pair of Resource Selectors. TRCSEQRSTEVR.RST.TYPE controls whether TRCSEQRSTEVR.RST.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQRSTEVR

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCSEQRSTEVR can be accessed through the external debug interface:

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| ETE         | 0x118    | TRCSEQRSTEVR |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.66 TRCSEQSTR, Trace Sequencer State Register

The TRCSEQSTR characteristics are:

## Purpose

Use this to set, or read, the Sequencer state.

## Configuration

External register TRCSEQSTR bits [31:0] are architecturally mapped to AArch64 System register TRCSEQSTR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR5.NUMSEQSTATE != '000'. Otherwise, direct accesses to TRCSEQSTR are RES0.

## Attributes

TRCSEQSTR is a 32-bit register.

## Field descriptions

| 31   | 2    | 1 0   |
|------|------|-------|
|      | RES0 | STATE |

## Bits [31:2]

Reserved, RES0.

## STATE, bits [1:0]

Set or returns the state of the Sequencer.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSEQSTR

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0010 and TRCRSCTLR&lt;a&gt;.SEQUENCER != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

TRCSEQSTR can be accessed through the external debug interface:

| STATE   | Meaning   |
|---------|-----------|
| 0b00    | State 0.  |
| 0b01    | State 1.  |
| 0b10    | State 2.  |
| 0b11    | State 3.  |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x11C    | TRCSEQSTR  |

## H9.3.67 TRCSSCCR&lt;n&gt;, Trace Single-shot Comparator Control Register &lt;n&gt;, n = 0 - 7

The TRCSSCCR&lt;n&gt; characteristics are:

## Purpose

Controls the corresponding Single-shot Comparator Control resource.

## Configuration

External register TRCSSCCR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCSSCCR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMSSCC) &gt; n. Otherwise, direct accesses to TRCSSCCR&lt;n&gt; are RES0.

## Attributes

TRCSSCCR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:25]

Reserved, RES0.

## RST, bit [24]

Selects the Single-shot Comparator Control mode.

| RST   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | The Single-shot Comparator Control is in single-shot mode. |
| 0b1   | The Single-shot Comparator Control is in multi-shot mode.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## ARC[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Selects one or more Address Range Comparators for Single-shot control.

| ARC[<m>]   | Meaning                                                                    |
|------------|----------------------------------------------------------------------------|
| 0b0        | The Address Range Comparator <m>, is not selected for Single-shot control. |
| 0b1        | The Address Range Comparator <m>, is selected for Single-shot control.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## SAC[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects one or more Single Address Comparators for Single-shot control.

| SAC[<m>]   | Meaning                                                                     |
|------------|-----------------------------------------------------------------------------|
| 0b0        | The Single Address Comparator <m>, is not selected for Single-shot control. |
| 0b1        | The Single Address Comparator <m>, is selected for Single-shot control.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCSSCCR&lt;n&gt;

Must be programmed if any TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCSSCCR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance             |
|-------------|-----------------------------|
| ETE         | 0x280 + (4 * n) TRCSSCCR<n> |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.68 TRCSSCSR&lt;n&gt;, Trace Single-shot Comparator Control Status Register &lt;n&gt;, n = 0 - 7

The TRCSSCSR&lt;n&gt; characteristics are:

## Purpose

Returns the status of the corresponding Single-shot Comparator Control.

## Configuration

External register TRCSSCSR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCSSCSR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMSSCC) &gt; n. Otherwise, direct accesses to TRCSSCSR&lt;n&gt; are RES0.

## Attributes

TRCSSCSR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## STATUS, bit [31]

Single-shot Comparator Control status. Indicates if any of the comparators selected by this Single-shot Comparator control have matched. The selected comparators are defined by TRCSSCCR&lt;n&gt;.ARC, TRCSSCCR&lt;n&gt;.SAC, and TRCSSPCICR&lt;n&gt;.PC.

| STATUS   | Meaning                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | No match has occurred. When the first match occurs, this field takes a value of 1. It remains at 1 until explicitly modified by a write to this register. |
| 0b1      | One or more matches has occurred. If TRCSSCCR<n>.RST == 0 then:                                                                                           |

## The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## PENDING, bit [30]

Single-shot pending status. The Single-shot Comparator Control fired while the resources were in the Paused state.

| PENDING   | Meaning                |
|-----------|------------------------|
| 0b0       | No match has occurred. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [29:4]

Reserved, RES0.

## PC, bit [3]

PE Comparator Input support. Indicates if the Single-shot Comparator Control supports PE Comparator Inputs.

| PC   | Meaning                                                                                                                                                                                                                                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support PE Comparator Inputs. Selecting any PE Comparator Inputs using the associated TRCSSPCICR<n> results in CONSTRAINED UNPREDICTABLE behavior of the Single-shot Comparator Control resource. The Single-shot Comparator Control might match unexpectedly or might not match. |
| 0b1  | This Single-shot Comparator Control supports PE Comparator Inputs.                                                                                                                                                                                                                                                             |

Access to this field is RO.

## DV, bit [2]

Data value comparator support. Data value comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

| DV   | Meaning                                                                      |
|------|------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support data value comparisons. |
| 0b1  | This Single-shot Comparator Control supports data value comparisons.         |

This field reads as 0.

Access to this field is RO.

## DA, bit [1]

Data Address Comparator support. Data address comparisons are not implemented in ETE and are reserved for other trace architectures. Allocated in other trace architectures.

| DA   | Meaning                                                                        |
|------|--------------------------------------------------------------------------------|
| 0b0  | This Single-shot Comparator Control does not support data address comparisons. |
| 0b1  | This Single-shot Comparator Control supports data address comparisons.         |

This field reads as 0.

Access to this field is RO.

| PENDING   | Meaning                           |
|-----------|-----------------------------------|
| 0b1       | One or more matches has occurred. |

## INST, bit [0]

Instruction Address Comparator support. Indicates if the Single-shot Comparator Control supports instruction address comparisons.

| INST   | Meaning                                                                               |
|--------|---------------------------------------------------------------------------------------|
| 0b0    | This Single-shot Comparator Control does not support instruction address comparisons. |
| 0b1    | This Single-shot Comparator Control supports instruction address comparisons.         |

This field reads as 1.

Access to this field is RO.

## Accessing TRCSSCSR&lt;n&gt;

Must be programmed if TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

TRCSSCSR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance             |
|-------------|-----------------------------|
| ETE         | 0x2A0 + (4 * n) TRCSSCSR<n> |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.69 TRCSSPCICR&lt;n&gt;, Trace Single-shot Processing Element Comparator Input Control Register &lt;n&gt;, n = 0 - 7

The TRCSSPCICR&lt;n&gt; characteristics are:

## Purpose

Returns the status of the corresponding Single-shot Comparator Control.

## Configuration

External register TRCSSPCICR&lt;n&gt; bits [31:0] are architecturally mapped to AArch64 System register TRCSSPCICR&lt;n&gt;[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, UInt(TRCIDR4.NUMSSCC) &gt; n, UInt(TRCIDR4.NUMPC) &gt; 0, and TRCSSCSR&lt;n&gt;.PC == '1'. Otherwise, direct accesses to TRCSSPCICR&lt;n&gt; are RES0.

## Attributes

TRCSSPCICR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

PC[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects one or more PE Comparator Inputs for Single-shot control.

| PC[<m>]   | Meaning                                                                         |
|-----------|---------------------------------------------------------------------------------|
| 0b0       | The single PE Comparator Input <m>, is not selected as for Single-shot control. |
| 0b1       | The single PE Comparator Input <m>, is selected as for Single-shot control.     |

This bit is RES0 if m &gt;= TRCIDR4.NUMPC.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSSPCICR&lt;n&gt;

Must be programmed if implemented and any TRCRSCTLR&lt;a&gt;.GROUP == 0b0011 and TRCRSCTLR&lt;a&gt;.SINGLE\_SHOT[n] == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

TRCSSPCICR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance               |
|-------------|-------------------------------|
| ETE         | 0x2C0 + (4 * n) TRCSSPCICR<n> |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.70 TRCSTALLCTLR, Trace Stall Control Register

The TRCSTALLCTLR characteristics are:

## Purpose

Enables trace unit functionality that prevents trace unit buffer overflows.

## Configuration

External register TRCSTALLCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCSTALLCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR3.STALLCTL == '1'. Otherwise, direct accesses to TRCSTALLCTLR are RES0.

## Attributes

TRCSTALLCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:14]

Reserved, RES0.

## NOOVERFLOW,bit [13]

## When TRCIDR3.NOOVERFLOW == '1':

Trace overflow prevention.

| NOOVERFLOW   | Meaning                                            |
|--------------|----------------------------------------------------|
| 0b0          | Trace unit buffer overflow prevention is disabled. |
| 0b1          | Trace unit buffer overflow prevention is enabled.  |

Note

Enabling this feature might cause a significant performance impact.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [12:9]

Reserved, RES0.

## ISTALL, bit [8]

Instruction stall control. Controls if a trace unit can stall the PE when the trace buffer space is less than LEVEL.

| ISTALL   | Meaning                               |
|----------|---------------------------------------|
| 0b0      | The trace unit must not stall the PE. |
| 0b1      | The trace unit can stall the PE.      |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Bits [7:4]

Reserved, RES0.

## LEVEL, bits [3:0]

Threshold level field. The field can support 16 monotonic levels from 0b0000 to 0b1111 .

The value 0b0000 defines the Minimal invasion level. This setting has a greater risk of a trace unit buffer overflow.

The value 0b1111 defines the Maximum invasion level. This setting has a reduced risk of a trace unit buffer overflow.

Note

For some implementations, invasion might occur at the minimal invasion level.

One or more of the least significant bits of LEVEL are permitted to be RES0. Arm recommends that LEVEL[3:2] are fully implemented. Arm strongly recommends that LEVEL[3] is always implemented. If one or more bits are RES0 and are written with a nonzero value, the effective value of LEVEL is rounded down to the nearest power of 2 value which has the RES0 bits as zero. For example, if LEVEL[1:0] are RES0 and a value of 0b1110 is written to LEVEL, the effective value of LEVEL is 0b1100 .

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSTALLCTLR

Must be programmed if implemented.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCSTALLCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| ETE         | 0x02C    | TRCSTALLCTLR |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.71 TRCSTATR, Trace Status Register

The TRCSTATR characteristics are:

## Purpose

Returns the trace unit status.

## Configuration

External register TRCSTATR bits [31:0] are architecturally mapped to AArch64 System register TRCSTATR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCSTATR are RES0.

## Attributes

TRCSTATR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## PMSTABLE, bit [1]

Programmers' model stable.

| PMSTABLE   | Meaning                               |
|------------|---------------------------------------|
| 0b0        | The programmers' model is not stable. |
| 0b1        | The programmers' model is stable.     |

Accessing this field has the following behavior:

- When the trace unit is enabled, access to this field is UNKNOWN/WI.
- Otherwise, access to this field is RO.

## IDLE, bit [0]

Idle status.

| IDLE   | Meaning                     |
|--------|-----------------------------|
| 0b0    | The trace unit is not idle. |
| 0b1    | The trace unit is idle.     |

## Accessing TRCSTATR

TRCSTATR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x00C    | TRCSTATR   |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.3.72 TRCSYNCPR, Trace Synchronization Period Register

The TRCSYNCPR characteristics are:

## Purpose

Controls how often trace protocol synchronization requests occur.

## Configuration

External register TRCSYNCPR bits [31:0] are architecturally mapped to AArch64 System register TRCSYNCPR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCSYNCPR are RES0.

## Attributes

TRCSYNCPR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:5]

Reserved, RES0.

## PERIOD, bits [4:0]

Defines the number of bytes of trace between each periodic trace protocol synchronization request.

| PERIOD   | Meaning                                                                  |
|----------|--------------------------------------------------------------------------|
| 0b00000  | Trace protocol synchronization is disabled.                              |
| 0b01000  | Trace protocol synchronization request occurs after 2 8 bytes of trace.  |
| 0b01001  | Trace protocol synchronization request occurs after 2 9 bytes of trace.  |
| 0b01010  | Trace protocol synchronization request occurs after 2 10 bytes of trace. |
| 0b01011  | Trace protocol synchronization request occurs after 2 11 bytes of trace. |
| 0b01100  | Trace protocol synchronization request occurs after 2 12 bytes of trace. |
| 0b01101  | Trace protocol synchronization request occurs after 2 13 bytes of trace. |
| 0b01110  | Trace protocol synchronization request occurs after 2 14 bytes of trace. |
| 0b01111  | Trace protocol synchronization request occurs after 2 15 bytes of trace. |
| 0b10000  | Trace protocol synchronization request occurs after 2 16 bytes of trace. |
| 0b10001  | Trace protocol synchronization request occurs after 2 17 bytes of trace. |
| 0b10010  | Trace protocol synchronization request occurs after 2 18 bytes of trace. |
| 0b10011  | Trace protocol synchronization request occurs after 2 19 bytes of trace. |

0b10100

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

Trace protocol synchronization request occurs after 2 20 bytes of trace.

Other values are reserved. If a reserved value is programmed into PERIOD, then the behavior of the synchronization period counter is CONSTRAINED UNPREDICTABLE and one of the following behaviors occurs:

- No trace protocol synchronization requests are generated by this counter.
- Trace protocol synchronization requests occur at the specified period.
- Trace protocol synchronization requests occur at some other UNKNOWN period which can vary.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCSYNCPR

Must be programmed if TRCIDR3.SYNCPR == 0.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCSYNCPR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x034    | TRCSYNCPR  |

## H9.3.73 TRCTRACEIDR, Trace ID Register

The TRCTRACEIDR characteristics are:

## Purpose

Sets the trace ID for instruction trace.

## Configuration

External register TRCTRACEIDR bits [31:0] are architecturally mapped to AArch64 System register TRCTRACEIDR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCTRACEIDR are RES0.

## Attributes

TRCTRACEIDR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:7]

Reserved, RES0.

## TRACEID, bits [6:0]

Trace ID field. Sets the trace ID value for instruction trace. The width of the field is indicated by the value of TRCIDR5.TRACEIDSIZE. Unimplemented bits are RES0.

If an implementation supports AMBA ATB, then:

- The width of the field is 7 bits.
- Writing a reserved trace ID value does not affect behavior of the trace unit but it might cause UNPREDICTABLE behavior of the trace capture infrastructure.

See the AMBA ATB Protocol Specification for information about which ATID values are reserved.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCTRACEIDR

Must be programmed if implemented.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCTRACEIDR can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| ETE         | 0x040    | TRCTRACEIDR |

Accessible as follows:

- When OSLockStatus(), or !IsTraceCorePowered(), or !AllowExternalTraceAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.74 TRCTSCTLR, Trace Timestamp Control Register

The TRCTSCTLR characteristics are:

## Purpose

Controls the insertion of global timestamps in the trace stream.

## Configuration

External register TRCTSCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCTSCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and TRCIDR0.TSSIZE != '00000'. Otherwise, direct accesses to TRCTSCTLR are RES0.

## Attributes

TRCTSCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## EVENT\_TYPE, bit [7]

## When TRCIDR4.NUMRSPAIR != '0000':

Chooses the type of Resource Selector.

| EVENT_TYPE   | Meaning                                                                                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Asingle Resource Selector. TRCTSCTLR.EVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                    |
| 0b1          | ABoolean-combined pair of Resource Selectors. TRCTSCTLR.EVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCTSCTLR.EVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## EVENT\_SEL, bits [4:0]

## When TRCIDR4.NUMRSPAIR != '0000':

Defines the selected Resource Selector or pair of Resource Selectors. TRCTSCTLR.EVENT.TYPE controls whether TRCTSCTLR.EVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TRCTSCTLR

Must be programmed if TRCCONFIGR.TS == 1.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCTSCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x030    | TRCTSCTLR  |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.75 TRCVICTLR, Trace ViewInst Main Control Register

The TRCVICTLR characteristics are:

## Purpose

Controls instruction trace filtering.

## Configuration

External register TRCVICTLR bits [31:0] are architecturally mapped to AArch64 System register TRCVICTLR[31:0].

This register is present only when FEAT\_ETE is implemented and FEAT\_TRC\_EXT is implemented. Otherwise, direct accesses to TRCVICTLR are RES0.

## Attributes

TRCVICTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:27]

Reserved, RES0.

## EXLEVEL\_RL\_EL2, bit [26]

## When FEAT\_RME is implemented:

Filter instruction trace for EL2 in Realm state.

| EXLEVEL_RL_EL2   | Meaning                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCVICTLR.EXLEVEL_NS_EL2 is 0 the trace unit generates instruction trace for EL2 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL2 is 1 the trace unit does not generate instruction trace for EL2 in Realm state. |
| 0b1              | When TRCVICTLR.EXLEVEL_NS_EL2 is 0 the trace unit does not generate instruction trace for EL2 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL2 is 1 the trace unit generates instruction trace for EL2 in Realm state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL1, bit [25]

## When FEAT\_RME is implemented:

Filter instruction trace for EL1 in Realm state.

| EXLEVEL_RL_EL1   | Meaning                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCVICTLR.EXLEVEL_NS_EL1 is 0 the trace unit generates instruction trace for EL1 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL1 is 1 the trace unit does not generate instruction trace for EL1 in Realm state. |
| 0b1              | When TRCVICTLR.EXLEVEL_NS_EL1 is 0 the trace unit does not generate instruction trace for EL1 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL1 is 1 the trace unit generates instruction trace for EL1 in Realm state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_RL\_EL0, bit [24]

## When FEAT\_RME is implemented:

Filter instruction trace for EL0 in Realm state.

| EXLEVEL_RL_EL0   | Meaning                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0              | When TRCVICTLR.EXLEVEL_NS_EL0 is 0 the trace unit generates instruction trace for EL0 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL0 is 1 the trace unit does not generate instruction trace for EL0 in Realm state. |
| 0b1              | When TRCVICTLR.EXLEVEL_NS_EL0 is 0 the trace unit does not generate instruction trace for EL0 in Realm state. When TRCVICTLR.EXLEVEL_NS_EL0 is 1 the trace unit generates instruction trace for EL0 in Realm state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## EXLEVEL\_NS\_EL2, bit [22]

## When Non-secure EL2 is implemented:

Filter instruction trace for EL2 in Non-secure state.

| EXLEVEL_NS_EL2   | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| 0b0              | The trace unit generates instruction trace for EL2 in Non-secure state.         |
| 0b1              | The trace unit does not generate instruction trace for EL2 in Non-secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL1, bit [21]

## When Non-secure EL1 is implemented:

Filter instruction trace for EL1 in Non-secure state.

| EXLEVEL_NS_EL1   | Meaning                                                                         |
|------------------|---------------------------------------------------------------------------------|
| 0b0              | The trace unit generates instruction trace for EL1 in Non-secure state.         |
| 0b1              | The trace unit does not generate instruction trace for EL1 in Non-secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_NS\_EL0, bit [20]

## When Non-secure EL0 is implemented:

Filter instruction trace for EL0 in Non-secure state.

| EXLEVEL_NS_EL0   | Meaning                                                                 |
|------------------|-------------------------------------------------------------------------|
| 0b0              | The trace unit generates instruction trace for EL0 in Non-secure state. |

| 0b1   | The trace unit does not generate instruction trace for EL0 in Non-secure state.   |
|-------|-----------------------------------------------------------------------------------|

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL3, bit [19]

## When EL3 is implemented:

Filter instruction trace for EL3.

| EXLEVEL_S_EL3   | Meaning                                                     |
|-----------------|-------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL3.         |
| 0b1             | The trace unit does not generate instruction trace for EL3. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL2, bit [18]

## When Secure EL2 is implemented:

Filter instruction trace for EL2 in Secure state.

| EXLEVEL_S_EL2   | Meaning                                                                     |
|-----------------|-----------------------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL2 in Secure state.         |
| 0b1             | The trace unit does not generate instruction trace for EL2 in Secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL1, bit [17]

## When Secure EL1 is implemented:

Filter instruction trace for EL1 in Secure state.

| EXLEVEL_S_EL1   | Meaning                                                                     |
|-----------------|-----------------------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL1 in Secure state.         |
| 0b1             | The trace unit does not generate instruction trace for EL1 in Secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EXLEVEL\_S\_EL0, bit [16]

## When Secure EL0 is implemented:

Filter instruction trace for EL0 in Secure state.

| EXLEVEL_S_EL0   | Meaning                                                                     |
|-----------------|-----------------------------------------------------------------------------|
| 0b0             | The trace unit generates instruction trace for EL0 in Secure state.         |
| 0b1             | The trace unit does not generate instruction trace for EL0 in Secure state. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:12]

Reserved, RES0.

## TRCERR, bit [11]

## When TRCIDR3.TRCERR == '1':

Controls the forced tracing of System Error exceptions.

| TRCERR   | Meaning                                                |
|----------|--------------------------------------------------------|
| 0b0      | Forced tracing of System Error exceptions is disabled. |
| 0b1      | Forced tracing of System Error exceptions is enabled.  |

| TRCERR   | Meaning   |
|----------|-----------|

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TRCRESET, bit [10]

Controls the forced tracing of PE Resets.

| TRCRESET   | Meaning                                  |
|------------|------------------------------------------|
| 0b0        | Forced tracing of PE Resets is disabled. |
| 0b1        | Forced tracing of PE Resets is enabled.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## SSSTATUS, bit [9]

ViewInst start/stop function status.

| SSSTATUS   | Meaning                                                                  |
|------------|--------------------------------------------------------------------------|
| 0b0        | Stopped State. The ViewInst start/stop function is in the stopped state. |
| 0b1        | Started State. The ViewInst start/stop function is in the started state. |

Before software enables the trace unit, it must write to this field to set the initial state of the ViewInst start/stop function. If the ViewInst start/stop function is not used then set this field to 1. Arm recommends that the value of this field is set before each trace session begins.

If the trace unit becomes disabled while a start point or stop point is still speculative, then the value of TRCVICTLR.SSSTATUS is UNKNOWN and might represent the result of a speculative start point or stop point.

If software which is running on the PE being traced disables the trace unit, either by clearing TRCPRGCTLR.EN or locking the OS Lock, Arm recommends that a DSB and an ISB instruction are executed before disabling the trace unit to prevent any start points or stop points being speculative at the point of disabling the trace unit. This procedure assumes that all start points or stop points occur before the barrier instructions are executed. The procedure does not guarantee that there are no speculative start points or stop points when disabling, although it helps minimize the probability.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- Access to this field is RES1 if all of the following are true:
- TRCIDR4.NUMACPAIRS == '0000'

- TRCIDR4.NUMPC == '0000'
- Otherwise, access to this field is RW.

## Bit [8]

Reserved, RES0.

## EVENT\_TYPE, bit [7]

## When TRCIDR4.NUMRSPAIR != '0000':

Chooses the type of Resource Selector.

| EVENT_TYPE   | Meaning                                                                                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0          | Asingle Resource Selector. TRCVICTLR.EVENT.SEL[4:0] selects the single Resource Selector, from 0-31, used to activate the resource event.                                                                                                                    |
| 0b1          | ABoolean-combined pair of Resource Selectors. TRCVICTLR.EVENT.SEL[3:0] selects the Resource Selector pair, from 0-15, that has a Boolean function that is applied to it whose output is used to activate the resource event. TRCVICTLR.EVENT.SEL[4] is RES0. |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## Bits [4:0]

## When TRCIDR4.NUMRSPAIR != '0000':

## EVENT\_SEL, bits [4:0]

Defines the selected Resource Selector or pair of Resource Selectors. TRCVICTLR.EVENT.TYPE controls whether TRCVICTLR.EVENT.SEL is the index of a single Resource Selector, or the index of a pair of Resource Selectors.

If an unimplemented Resource Selector is selected using this field, the behavior of the resource event is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

If an unimplemented Resource Selector is selected using this field, the value returned on a direct read of this field is UNKNOWN.

Selecting Resource Selector pair 0 using this field is UNPREDICTABLE, and the resource event might fire or might not fire when the resources are not in the Paused state.

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## When TRCIDR4.NUMRSPAIR == '0000':

## Reserved, bits [4:0]

This field is reserved:

- Bits [4:1] are RES0.
- Bit [0] is RES1.

## Otherwise:

Reserved, RES0.

## Accessing TRCVICTLR

Must be programmed.

Reads from this register might return an UNKNOWN value if the trace unit is not in either of the Idle or Stable states.

TRCVICTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| ETE         | 0x080    | TRCVICTLR  |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.76 TRCVIIECTLR, Trace ViewInst Include/Exclude Control Register

The TRCVIIECTLR characteristics are:

## Purpose

Use this to select, or read, the Address Range Comparators for the ViewInst include/exclude function.

## Configuration

External register TRCVIIECTLR bits [31:0] are architecturally mapped to AArch64 System register TRCVIIECTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMACPAIRS) &gt; 0. Otherwise, direct accesses to TRCVIIECTLR are RES0.

## Attributes

TRCVIIECTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:24]

Reserved, RES0.

## EXCLUDE[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Exclude Address Range Comparator &lt;m&gt;. Selects whether Address Range Comparator &lt;m&gt; is in use with the ViewInst exclude function.

| EXCLUDE[<m>]   | Meaning                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| 0b0            | The address range that Address Range Comparator <m> defines, is not selected for the ViewInst exclude function. |
| 0b1            | The address range that Address Range Comparator <m> defines, is selected for the ViewInst exclude function.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Bits [15:8]

Reserved, RES0.

## INCLUDE[&lt;m&gt;] , bits [m], for m = 7 to 0

Include Address Range Comparator &lt;m&gt;.

Selects whether Address Range Comparator &lt;m&gt; is in use with the ViewInst include function.

Selecting no comparators for the ViewInst include function indicates that all instructions are included by default.

The ViewInst exclude function then indicates which ranges are excluded.

| INCLUDE[<m>]   | Meaning                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| 0b0            | The address range that Address Range Comparator <m> defines, is not selected for the ViewInst include function. |
| 0b1            | The address range that Address Range Comparator <m> defines, is selected for the ViewInst include function.     |

## The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMACPAIRS), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCVIIECTLR

Must be programmed if TRCIDR4.NUMACPAIRS &gt; 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCVIIECTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| ETE         | 0x084    | TRCVIIECTLR |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.77 TRCVIPCSSCTLR, Trace ViewInst Start/Stop PE Comparator Control Register

The TRCVIPCSSCTLR characteristics are:

## Purpose

Use this to select, or read, which PE Comparator Inputs can control the ViewInst start/stop function.

## Configuration

External register TRCVIPCSSCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCVIPCSSCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMPC) &gt; 0. Otherwise, direct accesses to TRCVIPCSSCTLR are RES0.

## Attributes

TRCVIPCSSCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:24]

Reserved, RES0.

## STOP[&lt;m&gt;] , bits [m+16], for m = 7 to 0

Selects whether PE Comparator Input &lt;m&gt; is in use with the ViewInst start/stop function for the purpose of stopping trace.

| STOP[<m>]   | Meaning                                                         |
|-------------|-----------------------------------------------------------------|
| 0b0         | The PE Comparator Input <m> is not selected as a stop resource. |
| 0b1         | The PE Comparator Input <m> is selected as a stop resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMPC), access to this field is RES0.
- Otherwise, access to this field is RW.

## Bits [15:8]

Reserved, RES0.

## START[&lt;m&gt;] , bits [m], for m = 7 to 0

Selects whether PE Comparator Input &lt;m&gt; is in use with the ViewInst start/stop function for the purpose of starting trace.

| START[<m>]   | Meaning                                                          |
|--------------|------------------------------------------------------------------|
| 0b0          | The PE Comparator Input <m> is not selected as a start resource. |
| 0b1          | The PE Comparator Input <m> is selected as a start resource.     |

## The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR4.NUMPC), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCVIPCSSCTLR

Must be programmed if TRCIDR4.NUMPC != 0b0000 .

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCVIPCSSCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| ETE         | 0x08C    | TRCVIPCSSCTLR |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.78 TRCVISSCTLR, Trace ViewInst Start/Stop Control Register

The TRCVISSCTLR characteristics are:

## Purpose

Use this to select, or read, the Single Address Comparators for the ViewInst start/stop function.

## Configuration

External register TRCVISSCTLR bits [31:0] are architecturally mapped to AArch64 System register TRCVISSCTLR[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMACPAIRS) &gt; 0. Otherwise, direct accesses to TRCVISSCTLR are RES0.

## Attributes

TRCVISSCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## STOP[&lt;m&gt;] , bits [m+16], for m = 15 to 0

Selects whether Single Address Comparator &lt;m&gt; is used with the ViewInst start/stop function for the purpose of stopping trace.

| STOP[<m>]   | Meaning                                                               |
|-------------|-----------------------------------------------------------------------|
| 0b0         | The Single Address Comparator <m> is not selected as a stop resource. |
| 0b1         | The Single Address Comparator <m> is selected as a stop resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## START[&lt;m&gt;] , bits [m], for m = 15 to 0

Selects whether Single Address Comparator &lt;m&gt; is used with the ViewInst start/stop function for the purpose of starting trace.

| START[<m>]   | Meaning                                                                |
|--------------|------------------------------------------------------------------------|
| 0b0          | The Single Address Comparator <m> is not selected as a start resource. |
| 0b1          | The Single Address Comparator <m> is selected as a start resource.     |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= (UInt(TRCIDR4.NUMACPAIRS) * 2), access to this field is RES0.
- Otherwise, access to this field is RW.

## Accessing TRCVISSCTLR

Must be programmed if TRCIDR4.NUMACPAIRS &gt; 0b0000 .

For any 2 comparators selected for the ViewInst start/stop function, the comparator containing the lower address must be a lower numbered comparator.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCVISSCTLR can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| ETE         | 0x088    | TRCVISSCTLR |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.79 TRCVMIDCCTLR0, Trace Virtual Context Identifier Comparator Control Register 0

The TRCVMIDCCTLR0 characteristics are:

## Purpose

Virtual Context Identifier Comparator mask values for the TRCVMIDCVR&lt;n&gt; registers, where n=0-3.

## Configuration

External register TRCVMIDCCTLR0 bits [31:0] are architecturally mapped to AArch64 System register TRCVMIDCCTLR0[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, UInt(TRCIDR4.NUMVMIDC) &gt; 0x0 , and UInt(TRCIDR2.VMIDSIZE) &gt; 0. Otherwise, direct accesses to TRCVMIDCCTLR0 are RES0.

## Attributes

TRCVMIDCCTLR0 is a 32-bit register.

## Field descriptions

<!-- image -->

COMP3[&lt;m&gt;] , bits [m+24], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 3:

TRCVMIDCVR3 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR3. Each bit in this field corresponds to a byte in TRCVMIDCVR3.

| COMP3[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR3[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR3[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP2[&lt;m&gt;] , bits [m+16], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 2:

TRCVMIDCVR2 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR2. Each bit in this field corresponds to a byte in TRCVMIDCVR2.

| COMP2[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR2[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR2[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP1[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 1:

TRCVMIDCVR1 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR1. Each bit in this field corresponds to a byte in TRCVMIDCVR1.

| COMP1[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR1[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR1[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP0[&lt;m&gt;] , bits [m], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 0:

TRCVMIDCVR0 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR0. Each bit in this field corresponds to a byte in TRCVMIDCVR0.

| COMP0[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR0[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR0[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCVMIDCCTLR0

If software uses the TRCVMIDCVR&lt;n&gt; registers, where n=0-3, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCVMIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCVMIDCVR&lt;n&gt; is not 0x00 , the behavior of the Virtual Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCVMIDCCTLR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| ETE         | 0x688    | TRCVMIDCCTLR0 |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.80 TRCVMIDCCTLR1, Trace Virtual Context Identifier Comparator Control Register 1

The TRCVMIDCCTLR1 characteristics are:

## Purpose

Virtual Context Identifier Comparator mask values for the TRCVMIDCVR&lt;n&gt; registers, where n=4-7.

## Configuration

External register TRCVMIDCCTLR1 bits [31:0] are architecturally mapped to AArch64 System register TRCVMIDCCTLR1[31:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, UInt(TRCIDR4.NUMVMIDC) &gt; 0x4 , and UInt(TRCIDR2.VMIDSIZE) &gt; 0. Otherwise, direct accesses to TRCVMIDCCTLR1 are RES0.

## Attributes

TRCVMIDCCTLR1 is a 32-bit register.

## Field descriptions

<!-- image -->

COMP7[&lt;m&gt;] , bits [m+24], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 7:

TRCVMIDCVR7 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR7. Each bit in this field corresponds to a byte in TRCVMIDCVR7.

| COMP7[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR7[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR7[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP6[&lt;m&gt;] , bits [m+16], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 6:

TRCVMIDCVR6 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR6. Each bit in this field corresponds to a byte in TRCVMIDCVR6.

| COMP6[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR6[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR6[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP5[&lt;m&gt;] , bits [m+8], for m = 7 to 0

## When UInt(TRCIDR4.NUMVMIDC) &gt; 5:

TRCVMIDCVR5 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR5. Each bit in this field corresponds to a byte in TRCVMIDCVR5.

| COMP5[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR5[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR5[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

COMP4[&lt;m&gt;] , bits [m], for m = 7 to 0

When UInt(TRCIDR4.NUMVMIDC) &gt; 4:

TRCVMIDCVR4 mask control. Specifies the mask value that the trace unit applies to TRCVMIDCVR4. Each bit in this field corresponds to a byte in TRCVMIDCVR4.

| COMP4[<m>]   | Meaning                                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0          | The trace unit includes TRCVMIDCVR4[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison. |
| 0b1          | The trace unit ignores TRCVMIDCVR4[(m × 8+7):(m × 8)] when it performs the Virtual context identifier comparison.  |

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= UInt(TRCIDR2.VMIDSIZE), access to this field is RES0.
- Otherwise, access to this field is RW.

## Otherwise:

Reserved, RES0.

## Accessing TRCVMIDCCTLR1

If software uses the TRCVMIDCVR&lt;n&gt; registers, where n=4-7, then it must program this register.

If software sets a mask bit to 1 then it must program the relevant byte in TRCVMIDCVR&lt;n&gt; to 0x00 .

If any bit is 1 and the relevant byte in TRCVMIDCVR&lt;n&gt; is not 0x00 , the behavior of the Virtual Context Identifier Comparator is CONSTRAINED UNPREDICTABLE. In this scenario the comparator might match unexpectedly or might not match.

Writes are CONSTRAINED UNPREDICTABLE if the trace unit is not in the Idle state.

TRCVMIDCCTLR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| ETE         | 0x68C    | TRCVMIDCCTLR1 |

## Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.3.81 TRCVMIDCVR&lt;n&gt;, Trace Virtual Context Identifier Comparator Value Register &lt;n&gt;, n = 0 - 7

The TRCVMIDCVR&lt;n&gt; characteristics are:

## Purpose

Contains the Virtual Context Identifier Comparator value.

## Configuration

External register TRCVMIDCVR&lt;n&gt; bits [63:0] are architecturally mapped to AArch64 System register TRCVMIDCVR&lt;n&gt;[63:0].

This register is present only when FEAT\_ETE is implemented, FEAT\_TRC\_EXT is implemented, and UInt(TRCIDR4.NUMVMIDC) &gt; n. Otherwise, direct accesses to TRCVMIDCVR&lt;n&gt; are RES0.

## Attributes

TRCVMIDCVR&lt;n&gt; is a 64-bit register.

## Field descriptions

VALUE

63

32

VALUE

31

0

<!-- image -->

## VALUE, bits [63:0]

Virtual context identifier value. The width of this field is indicated by TRCIDR2.VMIDSIZE. Unimplemented bits are RES0. After a PE Reset, the trace unit assumes that the Virtual context identifier is zero until the PE updates the Virtual context identifier .

The reset behavior of this field is:

- On a Trace unit reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRCVMIDCVR&lt;n&gt;

Must be programmed if any of the following are true:

- TRCRSCTLR&lt;a&gt;.GROUP == 0b0111 and TRCRSCTLR&lt;a&gt;.VMID[n] == 1.
- TRCACATR&lt;a&gt;.CONTEXTTYPE == 0b10 or 0b11 and TRCACATR&lt;a&gt;.CONTEXT == n.

TRCVMIDCVR&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance               |
|-------------|-------------------------------|
| ETE         | 0x640 + (8 * n) TRCVMIDCVR<n> |

Accessible as follows:

- When OSLockStatus(), or !AllowExternalTraceAccess(addrdesc), or !IsTraceCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.