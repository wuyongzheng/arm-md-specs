## I5.3 Performance Monitors external register descriptions

This section describes the external view of the Performance Monitors registers. External Performance Monitors registers summary lists these registers in offset order.

## I5.3.1 PMAUTHSTATUS, Performance Monitors Authentication Status register

The PMAUTHSTATUS characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for Performance Monitors.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is OPTIONAL, and is required for CoreSight compliance. Arm recommends that this register is implemented.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMAUTHSTATUS are RES0.

## Attributes

PMAUTHSTATUS is a 32-bit register.

## Field descriptions

<!-- image -->

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

| RTID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

## RLID, bits [13:12]

Realm invasive debug.

## Bits [11:8]

Reserved, RES0.

## SNID, bits [7:6]

Holds the same value as DBGAUTHSTATUS\_EL1.SNID.

## SID, bits [5:4]

Secure invasive debug.

All other values are reserved.

Access to this field is RO.

## NSNID, bits [3:2]

Holds the same value as DBGAUTHSTATUS\_EL1.NSNID.

## NSID, bits [1:0]

Non-secure invasive debug.

All other values are reserved.

Access to this field is RO.

## Accessing PMAUTHSTATUS

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFB8 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

| RLID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

| SID   | Meaning          |
|-------|------------------|
| 0b00  | Not implemented. |

| NSID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

## I5.3.2 PMCCFILTR\_EL0, Performance Monitors Cycle Counter Filter Register

The PMCCFILTR\_EL0 characteristics are:

## Purpose

Determines the modes in which the Cycle Counter, PMCCNTR\_EL0, increments.

## Configuration

PMCCFILTR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCCFILTR\_EL0 are RES0.

## Attributes

PMCCFILTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:58]

Reserved, RES0.

## VS, bits [57:56]

## When FEAT\_PMUv3\_SME is implemented:

SVE mode filtering. Controls counting cycles in Streaming and Non-streaming SVE modes.

| VS   | Meaning                                                  |
|------|----------------------------------------------------------|
| 0b00 | This mechanism has no effect on the filtering of cycles. |
| 0b01 | The PE does not count cycles in Streaming SVE mode.      |
| 0b10 | The PE does not count cycles in Non-streaming SVE mode.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [55:32]

Reserved, RES0.

## P, bit [31]

EL1 filtering. Controls counting cycles in EL1.

| P   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of cycles. |
| 0b1 | The PE does not count cycles in EL1.                 |

If Secure and Non-secure states are implemented, then counting cycles in Non-secure EL1 is further controlled by PMCCFILTR\_EL0.NSK.

If FEAT\_RME is implemented, then counting cycles in Realm EL1 is further controlled by PMCCFILTR\_EL0.RLK.

If EL3 is implemented, then counting cycles in EL3 is further controlled by PMCCFILTR\_EL0.M.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

EL0 filtering. Controls counting cycles in EL0.

| U   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of cycles. |
| 0b1 | The PE does not count cycles in EL0.                 |

If Secure and Non-secure states are implemented, then counting cycles in Non-secure EL0 is further controlled by PMCCFILTR\_EL0.NSU.

If FEAT\_RME is implemented, then counting cycles in Realm EL0 is further controlled by PMCCFILTR\_EL0.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting cycles in Non-secure EL1. If PMCCFILTR\_EL0.NSK is not equal to PMCCFILTR\_EL0.P, then the PE does not count cycles in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of cycles in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.P == 1, the PE does not count cycles in Non-secure EL1. |
| 0b1   | When PMCCFILTR_EL0.P == 0, the PE does not count cycles in Non-secure EL1. When PMCCFILTR_EL0.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting cycles in Non-secure EL0. If PMCCFILTR\_EL0.NSU is not equal to PMCCFILTR\_EL0.U, then the PE does not count cycles in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of cycles in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.U == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.U == 1, the PE does not count cycles in Non-secure EL0. |
| 0b1   | When PMCCFILTR_EL0.U == 0, the PE does not count cycles in Non-secure EL0. When PMCCFILTR_EL0.U == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting cycles in EL2.

| NSH   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE does not count cycles in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of cycles. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting cycles in Secure EL2 is further controlled by PMCCFILTR\_EL0.SH.

If FEAT\_RME is implemented, then counting cycles in Realm EL2 is further controlled by PMCCFILTR\_EL0.RLH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## M, bit [26]

## When EL3 is implemented and FEAT\_AA64 is implemented:

EL3 filtering. Controls counting cycles in EL3. If PMCCFILTR\_EL0.M is not equal to PMCCFILTR\_EL0.P, then the PE does not count cycles in EL3. Otherwise, this mechanism has no effect on filtering of cycles in EL3.

| M   | Meaning                                                                                                                                         |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When PMCCFILTR_EL0.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.P == 1, the PE does not count cycles in EL3. |
| 0b1 | When PMCCFILTR_EL0.P == 0, the PE does not count cycles in EL3. When PMCCFILTR_EL0.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [25]

Reserved, RES0.

## SH, bit [24]

## When EL3 is implemented and FEAT\_SEL2 is implemented:

Secure EL2 filtering. Controls counting cycles in Secure EL2. If PMCCFILTR\_EL0.SH is equal to PMCCFILTR\_EL0.NSH, then the PE does not count cycles in Secure EL2. Otherwise, this mechanism has no effect on filtering of cycles in Secure EL2.

| SH   | Meaning                                                                                                                                                    |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMCCFILTR_EL0.NSH == 0, the PE does not count cycles in Secure EL2. When PMCCFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of cycles. |
| 0b1  | When PMCCFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.NSH == 1, the PE does not count cycles in Secure EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

When Secure EL2 is not implemented, access to this field is RES0.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## RLK, bit [22]

## When FEAT\_RME is implemented:

Realm EL1 filtering. Controls counting cycles in Realm EL1. If PMCCFILTR\_EL0.RLK is not equal to PMCCFILTR\_EL0.P, then the PE does not count cycles in Realm EL1. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL1.

| RLK   | Meaning                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.P == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.P == 1, the PE does not count cycles in Realm EL1. |
| 0b1   | When PMCCFILTR_EL0.P == 0, the PE does not count cycles in Realm EL1. When PMCCFILTR_EL0.P == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:

- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting cycles in Realm EL0. If PMCCFILTR\_EL0.RLU is not equal to PMCCFILTR\_EL0.U, then the PE does not count cycles in Realm EL0. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL0.

| RLU   | Meaning                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.U == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.U == 1, the PE does not count cycles in Realm EL0. |
| 0b1   | When PMCCFILTR_EL0.U == 0, the PE does not count cycles in Realm EL0. When PMCCFILTR_EL0.U == 1, this mechanism has no effect on filtering of cycles. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLH, bit [20]

## When FEAT\_RME is implemented:

Realm EL2 filtering. Controls counting cycles in Realm EL2. If PMCCFILTR\_EL0.RLH is equal to PMCCFILTR\_EL0.NSH, then the PE does not count cycles in Realm EL2. Otherwise, this mechanism has no effect on filtering of cycles in Realm EL2.

| RLH   | Meaning                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMCCFILTR_EL0.NSH == 0, the PE does not count cycles in Realm EL2. When PMCCFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of cycles. |
| 0b1   | When PMCCFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of cycles. When PMCCFILTR_EL0.NSH == 1, the PE does not count cycles in Realm EL2. |

The reset behavior of this field is:

- On a Cold reset:

- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [19:0]

Reserved, RES0.

## Accessing PMCCFILTR\_EL0

If FEAT\_PMUv3\_EXT32 is implemented, and any of the following apply, then bits [63:32] of this register are accessible at offset 0xA7C :

- FEAT\_PMUv3\_TH is implemented.
- FEAT\_PMUv3p8 is implemented.
- FEAT\_PMUv3\_SME is implemented.

Otherwise accesses at this offset are IMPLEMENTATION DEFINED.

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

[31:0] Accessible at offset 0x47C from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x4F8 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## When IsFeatureImplemented(FEAT\_PMUv3\_EXT32) &amp;&amp; ((IsFeatureImplemented(FEAT\_PMUv3\_TH) || IsFeatureImplemented(FEAT\_PMUv3p8)) || IsFeatureImplemented(FEAT\_PMUv3\_SME))

[63:32] Accessible at offset 0xA7C from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.3 PMCCIDSR, CONTEXTIDR\_ELx Sample Register

The PMCCIDSR characteristics are:

## Purpose

Contains the sampled value of CONTEXTIDR\_EL1 and CONTEXTIDR\_EL2, captured on reading PMPCSR.

## Configuration

This register is a PC Sample-based Profiling Extension register.

This register is present only when FEAT\_PMUv3\_EXT64 is implemented and FEAT\_PCSRv8p2 is implemented.

## Attributes

PMCCIDSR is a 64-bit register.

## Field descriptions

<!-- image -->

## CONTEXTIDR\_EL2, bits [63:32]

Context ID. The value of CONTEXTIDR\_EL2 that is associated with the most recent PMPCSR sample. When the most recent PMPCSR sample is generated:

- If the PE is not executing at EL3, EL2 is using AArch64, and EL2 is enabled in the current Security state, then this field is set to the Context ID sampled from CONTEXTIDR\_EL2.
- Otherwise, this field is set to an UNKNOWN value.

Because the value written to this field is an indirect read of CONTEXTIDR\_EL2, it is CONSTRAINED UNPREDICTABLE whether this field is set to the original or new value if PMPCSR samples:

- An instruction that writes to CONTEXTIDR\_EL2.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## CONTEXTIDR\_EL1, bits [31:0]

Context ID. The value of CONTEXTIDR that is associated with the most recent PMPCSR sample. When the most recent PMPCSR sample is generated:

- If EL1 is using AArch64, then the Context ID is sampled from CONTEXTIDR\_EL1.
- If EL1 is using AArch32, then the Context ID is sampled from CONTEXTIDR.
- If EL3 is implemented and is using AArch32, then CONTEXTIDR is a banked register and this register samples the current banked copy of CONTEXTIDR for the Security state that is associated with the most recent PMPCSR sample.

Because the value written to this register is an indirect read of CONTEXTIDR, it is CONSTRAINED UNPREDICTABLE whether this register is set to the original or new value if PMPCSR samples:

- An instruction that writes to CONTEXTIDR.

- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMCCIDSR

If FEAT\_PCSRv8p2 and FEAT\_PMUv3\_EXT32 are implemented, then the same content is present in the same locations, and can be accessed using PMCID2SR[31:0] and PMCID1SR[31:0].

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0x228 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.4 PMCCNTR\_EL0, Performance Monitors Cycle Counter

The PMCCNTR\_EL0 characteristics are:

## Purpose

Holds the value of the processor Cycle Counter, CCNT, that counts processor clock cycles. For more information, see 'Time as measured by the Performance Monitors cycle counter'.

PMCCFILTR\_EL0 determines the modes and states in which the PMCCNTR\_EL0 can increment.

## Configuration

PMCCNTR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCCNTR\_EL0 are RES0.

## Attributes

PMCCNTR\_EL0 is a 64-bit register.

## Field descriptions

CCNT

63

32

CCNT

31

0

<!-- image -->

## CCNT, bits [63:0]

Cycle count. Depending on the values of PMCR\_EL0.{LC,D}, the cycle count increments in one of the following ways:

- Every processor clock cycle.
- Every 64th processor clock cycle.

Writing 1 to PMCR\_EL0.C sets this field to 0.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMCCNTR\_EL0

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x0F8 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented

[31:0] Accessible at offset 0x0F8 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented

[63:32] Accessible at offset 0x0FC from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.5 PMCCNTSVR\_EL1, Performance Monitors Cycle Count Saved Value Register

The PMCCNTSVR\_EL1 characteristics are:

## Purpose

Captures the PMU Cycle counter, PMCCNTR\_EL0.

## Configuration

This register is present only when FEAT\_PMUv3\_SS is implemented and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCCNTSVR\_EL1 are RES0.

## Attributes

PMCCNTSVR\_EL1 is a 64-bit register.

## Field descriptions

CCNT

63

32

CCNT

31

0

<!-- image -->

## CCNT, bits [63:0]

Sampled Cycle Count. The value of PMCCNTR\_EL0 at the last successful Capture event.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMCCNTSVR\_EL1

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_SS is implemented

Accessible at offset 0x6F8 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMSSAccess(addrdesc), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.6 PMCEID0, Performance Monitors Common Event Identification register 0

The PMCEID0 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x0000 to 0x001F .

For more information about the Common events and the use of the PMCEIDn registers, see 'The PMU event number space and common events'.

Use of this register is deprecated.

Note

This view of the register was previously called PMCEID0\_EL0.

## Configuration

PMCEID0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented. Otherwise, direct accesses to PMCEID0 are RES0.

## Attributes

PMCEID0 is a 32-bit register.

## Field descriptions

<!-- image -->

## ID&lt;n&gt; , bits [n], for n = 31 to 0

ID[n] corresponds to Common event n.

For each bit:

| ID<n>   | Meaning                                              |
|---------|------------------------------------------------------|
| 0b0     | The Common event is not implemented, or not counted. |
| 0b1     | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID0

Note

AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

Accessible at offset 0xE20 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.7 PMCEID1, Performance Monitors Common Event Identification register 1

The PMCEID1 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x020 to 0x03F .

For more information about the Common events and the use of the PMCEIDn registers, see 'The PMU event number space and common events'.

Use of this register is deprecated.

Note

This view of the register was previously called PMCEID1\_EL0.

## Configuration

PMCEID1 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented. Otherwise, direct accesses to PMCEID1 are RES0.

## Attributes

PMCEID1 is a 32-bit register.

## Field descriptions

<!-- image -->

## ID&lt;n&gt; , bits [n], for n = 31 to 0

ID[n] corresponds to Common event ( 0x0020 + n).

For each bit:

| ID<n>   | Meaning                                              |
|---------|------------------------------------------------------|
| 0b0     | The Common event is not implemented, or not counted. |
| 0b1     | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID1

Note

AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

Accessible at offset 0xE24 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.8 PMCEID2, Performance Monitors Common Event Identification register 2

The PMCEID2 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x4000 to 0x401F .

For more information about the Common events and the use of the PMCEIDn registers, see 'The PMU event number space and common events'.

Use of this register is deprecated.

## Configuration

PMCEID2 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p1 is implemented. Otherwise, direct accesses to PMCEID2 are RES0.

## Attributes

PMCEID2 is a 32-bit register.

## Field descriptions

<!-- image -->

## IDhi&lt;n&gt; , bits [n], for n = 31 to 0

IDhi[n] corresponds to Common event ( 0x4000 + n).

For each bit:

| IDhi<n>   | Meaning                                              |
|-----------|------------------------------------------------------|
| 0b0       | The Common event is not implemented, or not counted. |
| 0b1       | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID2

Note

AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p1 is implemented

Accessible at offset 0xE28 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.9 PMCEID3, Performance Monitors Common Event Identification register 3

The PMCEID3 characteristics are:

## Purpose

Defines which Common architectural events and Common microarchitectural events are implemented, or counted, using PMU events in the range 0x4020 to 0x403F .

For more information about the Common events and the use of the PMCEIDn registers, see 'The PMU event number space and common events'.

Use of this register is deprecated.

## Configuration

PMCEID3 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p1 is implemented. Otherwise, direct accesses to PMCEID3 are RES0.

## Attributes

PMCEID3 is a 32-bit register.

## Field descriptions

<!-- image -->

## IDhi&lt;n&gt; , bits [n], for n = 31 to 0

IDhi[n] corresponds to Common event ( 0x4020 + n).

For each bit:

| IDhi<n>   | Meaning                                              |
|-----------|------------------------------------------------------|
| 0b0       | The Common event is not implemented, or not counted. |
| 0b1       | The Common event is implemented.                     |

When the value of a bit in the field is 1, the corresponding Common event is implemented and counted.

Note

Arm recommends that if a Common event is never counted, the value of the corresponding bit is 0.

Abit that corresponds to a reserved event number is reserved. The value might be used in a future revision of the architecture to identify an additional Common event.

Note

Such an event might be added retrospectively to an earlier version of the PMU architecture, provided the event does not require any additional PMU features and has an event number that can be represented in the PMCEID&lt;n&gt; registers of that earlier version of the PMU architecture.

## Accessing PMCEID3

Note

AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p1 is implemented

Accessible at offset 0xE2C from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.10 PMCGCR0, Counter Group Configuration Register 0

The PMCGCR0 characteristics are:

## Purpose

Encodes the number of counters accessible.

## Configuration

PMCGCR0is in the Core power domain.

This register is present only when FEAT\_PMUv3\_ICNTR is implemented and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCGCR0 are RES0.

## Attributes

PMCGCR0is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented:

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## CG1NC, bits [15:8]

Number of counters in group 1, which comprises the instruction counter PMICNTR\_EL0.

| CG1NC   | Meaning                  |
|---------|--------------------------|
| 0x01    | PMICNTR_EL0 implemented. |

Other values are reserved.

Access to this field is RO.

## CG0NC, bits [7:0]

Number of counters in group 0, which comprises the event counters PMEVCNTR&lt;n&gt;\_EL0 and the cycle counter PMCCNTR\_EL0.

This field has an IMPLEMENTATION DEFINED value.

When FEAT\_PMUv3\_EXTPMN is implemented and the external access to this register is not a Most secure access, this field reads as the Effective value of PMCCR.EPMN plus one.

Otherwise, this field reads as the number of event counters implemented plus one.

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## CG1NC, bits [15:8]

Number of counters in group 1, which comprises the instruction counter PMICNTR\_EL0.

| CG1NC   | Meaning                  |
|---------|--------------------------|
| 0x01    | PMICNTR_EL0 implemented. |

Other values are reserved.

Access to this field is RO.

## CG0NC, bits [7:0]

Number of counters in group 0, which comprises the event counters PMEVCNTR&lt;n&gt;\_EL0 and the cycle counter PMCCNTR\_EL0.

This field has an IMPLEMENTATION DEFINED value.

When FEAT\_PMUv3\_EXTPMN is implemented and the external access to this register is not a Most secure access, this field reads as the Effective value of PMCCR.EPMN plus one.

Otherwise, this field reads as the number of event counters implemented plus one.

Access to this field is RO.

## Accessing PMCGCR0

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3\_ICNTR is implemented

[31:0] Accessible at offset 0xCE0 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT64 is implemented and FEAT\_PMUv3\_ICNTR is implemented

[63:0] Accessible at offset 0xCE0 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.11 PMCFGR, Performance Monitors Configuration Register

The PMCFGR characteristics are:

## Purpose

Contains PMU-specific configuration data.

## Configuration

PMCFGRis in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCFGR are RES0.

## Attributes

## PMCFGRis a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## NCG, bits [31:28]

Defines the number of counter groups implemented, minus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NCG    | Meaning                         |
|--------|---------------------------------|
| 0b0000 | One counter group implemented.  |
| 0b0001 | Two counter groups implemented. |

All other values are reserved.

FEAT\_PMUv3\_ICNTR implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Bits [27:23]

Reserved, RES0.

## SS, bit [22]

Snapshot supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SS   | Meaning                                                                                                                                                                                                                                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Snapshot mechanism not supported. The locations 0x600 - 0x7FC and 0xE30 - 0xE3C are IMPLEMENTATION DEFINED.                                                                                                                                                                                                                   |
| 0b1  | Snapshot mechanism supported. If FEAT_PMUv3_SS is implemented, then the following registers are implemented: • PMEVCNTSVR<n>_EL1. • PMCCNTSVR_EL1. • If FEAT_PMUv3_ICNTR is implemented, PMICNTSVR_EL1. • PMSSCR_EL1. Otherwise, locations 0x600 - 0x7FC and 0xE30 - 0xE3C contain IMPLEMENTATION DEFINED snapshot registers. |

FEAT\_PMUv3\_SS implements the functionality identified by the value 1.

If FEAT\_PMUv3\_SS is not implemented, a PMU might include an IMPLEMENTATION DEFINED snapshot mechanism, including one using the IMPLEMENTATION DEFINED registers 0x600 -0x7FC and 0xE30 -0xE3C .

Access to this field is RO.

## FZO, bit [21]

Freeze-on-overflow supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FZO   | Meaning                                                              |
|-------|----------------------------------------------------------------------|
| 0b0   | Freeze-on-overflow mechanism is not supported. PMCR_EL0.FZO is RES0. |
| 0b1   | Freeze-on-overflow mechanism is supported. PMCR_EL0.FZO is RW.       |

FEAT\_PMUv3p7 implements the functionality added by the value 0b1 .

From Armv8.7, if FEAT\_PMUv3 is implemented, the only permitted value is 0b1 .

Access to this field is RO.

## Bit [20]

Reserved, RES0.

## UEN, bit [19]

User-mode Enable Register supported. PMUSERENR\_EL0 is not visible in the external debug interface, so this bit is RAZ.

Reads as 0b0

Access to this field is RO.

## WT, bit [18]

This feature is not supported, so this bit is RAZ.

Reads as 0b0

Access to this field is RO.

## NA, bit [17]

This feature is not supported, so this bit is RAZ.

Reads as 0b0

Access to this field is RO.

## EX, bit [16]

Export supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EX   | Meaning                   |
|------|---------------------------|
| 0b0  | PMCR_EL0.X is RES0.       |
| 0b1  | PMCR_EL0.X is read/write. |

Access to this field is RO.

## CCD, bit [15]

Cycle counter has prescale.

This is RES1 if AArch32 is supported, and RAZ otherwise.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCD   | Meaning                   |
|-------|---------------------------|
| 0b0   | PMCR_EL0.D is RES0.       |
| 0b1   | PMCR_EL0.D is read/write. |

Access to this field is RO.

## CC, bit [14]

Dedicated cycle counter (counter 31) supported.

Reads as 0b1

Access to this field is RO.

## SIZE, bits [13:8]

Size of counters, minus one. This field defines the size of the largest counter implemented by the Performance Monitors Unit.

From Armv8.0, the largest counter is 64-bits, so the value of this field is 0b111111 .

This field is used by software to determine the spacing of the counters in the memory-map. From Armv8.0, the counters are a doubleword-aligned addresses.

Reads as

0b111111

Access to this field is RO.

## N, bits [7:0]

Number of counters accessible, minus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| N            | Meaning                                            |
|--------------|----------------------------------------------------|
| 0x00         | Only PMCCNTR_EL0 accessible.                       |
| 0x01 .. 0x20 | Number of counters accessible, 2 to 33, minus one. |

All other values are reserved.

If FEAT\_PMUv3\_ICNTR is implemented, then the value 0x00 is not permitted.

The count includes:

- The cycle counter, PMCCNTR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, the Instruction Counter, PMICNTR\_EL0.

When FEAT\_PMUv3\_EXTPMN is implemented and the access to this register is not a Most secure access, the following apply:

- If FEAT\_PMUv3\_ICNTR is not implemented, this field reads as the Effective value of PMCCR.EPMN.
- If FEAT\_PMUv3\_ICNTR is implemented, this field reads as the Effective value of PMCCR.EPMN plus one.

Otherwise, the following apply:

- If FEAT\_PMUv3\_ICNTR is not implemented, this field reads as the number of event counters implemented.
- If FEAT\_PMUv3\_ICNTR is implemented, this field reads as the number of event counters implemented plus one.

For example, if PMCFGR.N == 0x07 , then:

- There are eight counters in total.
- If FEAT\_PMUv3\_ICNTR is not implemented, this comprises 7 event counters and the cycle counter.
- If FEAT\_PMUv3\_ICNTR is implemented, this comprises 6 event counters, the cycle counter, and the instruction counter.

The maximum number of event counters is 31.

Access to this field is RO.

## Otherwise:

<!-- image -->

## NCG, bits [31:28]

Defines the number of counter groups implemented, minus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NCG    | Meaning                         |
|--------|---------------------------------|
| 0b0000 | One counter group implemented.  |
| 0b0001 | Two counter groups implemented. |

All other values are reserved.

FEAT\_PMUv3\_ICNTR implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Bits [27:23]

Reserved, RES0.

## SS, bit [22]

Snapshot supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SS   | Meaning                                                                                                      |
|------|--------------------------------------------------------------------------------------------------------------|
| 0b0  | Snapshot mechanism not supported. The locations 0x600 - 0x7FC and 0xE30 - 0xE3C are IMPLEMENTATION DEFINED.  |
| 0b1  | Snapshot mechanism supported. If FEAT_PMUv3_SS is implemented, then the following registers are implemented: |
|      | • PMEVCNTSVR<n>_EL1.                                                                                         |
|      | • PMCCNTSVR_EL1.                                                                                             |
|      | • If FEAT_PMUv3_ICNTR is implemented, PMICNTSVR_EL1.                                                         |
|      | • PMSSCR_EL1.                                                                                                |
|      | Otherwise, locations 0x600 - 0x7FC and 0xE30 - 0xE3C contain IMPLEMENTATION DEFINED snapshot registers.      |

FEAT\_PMUv3\_SS implements the functionality identified by the value 1.

If FEAT\_PMUv3\_SS is not implemented, a PMU might include an IMPLEMENTATION DEFINED snapshot mechanism, including one using the IMPLEMENTATION DEFINED registers 0x600 -0x7FC and 0xE30 -0xE3C .

Access to this field is RO.

## FZO, bit [21]

Freeze-on-overflow supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FZO   | Meaning                                                              |
|-------|----------------------------------------------------------------------|
| 0b0   | Freeze-on-overflow mechanism is not supported. PMCR_EL0.FZO is RES0. |
| 0b1   | Freeze-on-overflow mechanism is supported. PMCR_EL0.FZO is RW.       |

FEAT\_PMUv3p7 implements the functionality added by the value 0b1 .

From Armv8.7, if FEAT\_PMUv3 is implemented, the only permitted value is 0b1 .

Access to this field is RO.

## Bit [20]

Reserved, RES0.

## UEN, bit [19]

User-mode Enable Register supported. PMUSERENR\_EL0 is not visible in the external debug interface, so this bit is RAZ.

Reads as 0b0

Access to this field is RO.

## WT, bit [18]

This feature is not supported, so this bit is RAZ.

Reads as 0b0

Access to this field is RO.

## NA, bit [17]

This feature is not supported, so this bit is RAZ.

Reads as 0b0

Access to this field is RO.

## EX, bit [16]

Export supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EX   | Meaning                   |
|------|---------------------------|
| 0b0  | PMCR_EL0.X is RES0.       |
| 0b1  | PMCR_EL0.X is read/write. |

Access to this field is RO.

## CCD, bit [15]

Cycle counter has prescale.

This is RES1 if AArch32 is supported, and RAZ otherwise.

The value of this field is an IMPLEMENTATION DEFINED choice of:

Access to this field is RO.

## CC, bit [14]

Dedicated cycle counter (counter 31) supported.

Reads as 0b1

Access to this field is RO.

## SIZE, bits [13:8]

Size of counters, minus one. This field defines the size of the largest counter implemented by the Performance Monitors Unit.

From Armv8.0, the largest counter is 64-bits, so the value of this field is 0b111111 .

This field is used by software to determine the spacing of the counters in the memory-map. From Armv8.0, the counters are a doubleword-aligned addresses.

Reads as 0b111111

Access to this field is RO.

## N, bits [7:0]

Number of counters accessible, minus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| N            | Meaning                                            |
|--------------|----------------------------------------------------|
| 0x00         | Only PMCCNTR_EL0 accessible.                       |
| 0x01 .. 0x20 | Number of counters accessible, 2 to 33, minus one. |

All other values are reserved.

If FEAT\_PMUv3\_ICNTR is implemented, then the value 0x00 is not permitted.

The count includes:

- The cycle counter, PMCCNTR\_EL0.
- If FEAT\_PMUv3\_ICNTR is implemented, the Instruction Counter, PMICNTR\_EL0.

When FEAT\_PMUv3\_EXTPMN is implemented and the access to this register is not a Most secure access, the following apply:

- If FEAT\_PMUv3\_ICNTR is not implemented, this field reads as the Effective value of PMCCR.EPMN.
- If FEAT\_PMUv3\_ICNTR is implemented, this field reads as the Effective value of PMCCR.EPMN plus one.

Otherwise, the following apply:

- If FEAT\_PMUv3\_ICNTR is not implemented, this field reads as the number of event counters implemented.
- If FEAT\_PMUv3\_ICNTR is implemented, this field reads as the number of event counters implemented plus one.

For example, if PMCFGR.N == 0x07 , then:

| CCD   | Meaning                   |
|-------|---------------------------|
| 0b0   | PMCR_EL0.D is RES0.       |
| 0b1   | PMCR_EL0.D is read/write. |

- There are eight counters in total.
- If FEAT\_PMUv3\_ICNTR is not implemented, this comprises 7 event counters and the cycle counter.
- If FEAT\_PMUv3\_ICNTR is implemented, this comprises 6 event counters, the cycle counter, and the instruction counter.

The maximum number of event counters is 31.

Access to this field is RO.

## Accessing PMCFGR

Note

AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0xE00 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT32 is implemented

[31:0] Accessible at offset 0xE00 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- •
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.12 PMCID1SR, CONTEXTIDR\_EL1 Sample Register

The PMCID1SR characteristics are:

## Purpose

Contains the sampled value of CONTEXTIDR\_EL1, captured on reading PMPCSR[31:0].

## Configuration

PMCID1SR is in the Core power domain.

This register is a PC Sample-based Profiling Extension register.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented.

## Attributes

PMCID1SR is a 32-bit register.

## Field descriptions

CONTEXTIDR\_EL1

31

0

<!-- image -->

## CONTEXTIDR\_EL1, bits [31:0]

Context ID. The value of CONTEXTIDR that is associated with the most recent PMPCSR sample. When the most recent PMPCSR sample is generated:

- If EL1 is using AArch64, then the Context ID is sampled from CONTEXTIDR\_EL1.
- If EL1 is using AArch32, then the Context ID is sampled from CONTEXTIDR.
- If EL3 is implemented and is using AArch32, then CONTEXTIDR is a banked register and this register samples the current banked copy of CONTEXTIDR for the Security state that is associated with the most recent PMPCSR sample.

Because the value written to this register is an indirect read of CONTEXTIDR, it is CONSTRAINED UNPREDICTABLE whether this register is set to the original or new value if PMPCSR samples:

- An instruction that writes to CONTEXTIDR.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMCID1SR

If FEAT\_PCSRv8p2 and FEAT\_PMUv3\_EXT64 are implemented, then the same content is present in the same locations, and can be accessed using PMCCIDSR[31:0] or PMCVIDSR[31:0].

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

Accessible at offset 0x208 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.

- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

Accessible at offset 0x228 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.13 PMCID2SR, CONTEXTIDR\_EL2 Sample Register

The PMCID2SR characteristics are:

## Purpose

Contains the sampled value of CONTEXTIDR\_EL2, captured on reading PMPCSR[31:0].

## Configuration

PMCIDR2SR is in the Core power domain.

This register is a PC Sample-based Profiling Extension register.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented.

## Attributes

PMCID2SR is a 32-bit register.

## Field descriptions

CONTEXTIDR\_EL2

31

0

<!-- image -->

## CONTEXTIDR\_EL2, bits [31:0]

Context ID. The value of CONTEXTIDR\_EL2 that is associated with the most recent PMPCSR sample. When the most recent PMPCSR sample is generated:

- If the PE is not executing at EL3, EL2 is using AArch64, and EL2 is enabled in the current Security state, then this field is set to the Context ID sampled from CONTEXTIDR\_EL2.
- Otherwise, this field is set to an UNKNOWN value.

Because the value written to this field is an indirect read of CONTEXTIDR\_EL2, it is CONSTRAINED UNPREDICTABLE whether this field is set to the original or new value if PMPCSR samples:

- An instruction that writes to CONTEXTIDR\_EL2.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMCID2SR

If FEAT\_PMUv3\_EXT64 is implemented, then the same content is present in the same location, and can be accessed using PMCCIDSR[63:32].

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

Accessible at offset 0x22C from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.14 PMCIDR0, Performance Monitors Component Identification Register 0

The PMCIDR0 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Component Identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMCIDR0. Otherwise, direct accesses to PMCIDR0 are RES0.

## Attributes

PMCIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_0, bits [7:0]

Preamble.

Reads as 0x0D

Access to this field is RO.

## Accessing PMCIDR0

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFF0 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.15 PMCIDR1, Performance Monitors Component Identification Register 1

The PMCIDR1 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Component Identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMCIDR1. Otherwise, direct accesses to PMCIDR1 are RES0.

## Attributes

PMCIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

Bits [31:8]

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

## Accessing PMCIDR1

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFF4 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.16 PMCIDR2, Performance Monitors Component Identification Register 2

The PMCIDR2 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Component Identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMCIDR2. Otherwise, direct accesses to PMCIDR2 are RES0.

## Attributes

PMCIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_2, bits [7:0]

Preamble.

Reads as 0x05

Access to this field is RO.

## Accessing PMCIDR2

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFF8 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.17 PMCIDR3, Performance Monitors Component Identification Register 3

The PMCIDR3 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Component Identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMCIDR3. Otherwise, direct accesses to PMCIDR3 are RES0.

## Attributes

PMCIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_3, bits [7:0]

Preamble.

Reads as 0xB1

Access to this field is RO.

## Accessing PMCIDR3

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFFC from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.18 PMCNTEN, Performance Monitors Count Enable register

The PMCNTEN characteristics are:

## Purpose

Enables the Cycle Count Register, PMCCNTR\_EL0, and any implemented event counters PMEVCNTR&lt;n&gt;.

## Configuration

This register is present only when FEAT\_PMUv3\_EXT64 is implemented. Otherwise, direct accesses to PMCNTENare RES0.

## Attributes

PMCNTENis a 64-bit register.

## Field descriptions

<!-- image -->

| 63   |
|------|

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

PMICNTR\_EL0 counter enable. Enables the instruction counter.

| F0   | Meaning               |
|------|-----------------------|
| 0b0  | PMICNTR_EL0 disabled. |
| 0b1  | PMICNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## C, bit [31]

PMCCNTR\_EL0 enable. Enables the cycle counter register. Possible values are:

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Event counter enable for PMEVCNTR&lt;m&gt;\_EL0.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- Otherwise, access to this field is RW.

## Accessing PMCNTEN

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0xC10 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

| C   | Meaning                  |
|-----|--------------------------|
| 0b0 | PMCCNTR_EL0 is disabled. |
| 0b1 | PMCCNTR_EL0 enabled.     |

| P<m>   | Meaning                      |
|--------|------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 is disabled. |
| 0b1    | PMEVCNTR<m>_EL0 is enabled.  |

## I5.3.19 PMCNTENCLR\_EL0, Performance Monitors Count Enable Clear Register

The PMCNTENCLR\_EL0 characteristics are:

## Purpose

Allows software to disable the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which counters are enabled.

## Configuration

PMCNTENCLR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCNTENCLR\_EL0 are RES0.

## Attributes

PMCNTENCLR\_EL0 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

PMICNTR\_EL0 disable. On writes, allows software to disable PMICNTR\_EL0. On reads, returns the PMICNTR\_EL0 enable status.

| F0   | Meaning               |
|------|-----------------------|
| 0b0  | PMICNTR_EL0 disabled. |
| 0b1  | PMICNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Otherwise:

Reserved, RES0.

## C, bit [31]

PMCCNTR\_EL0 disable. On writes, allows software to disable PMCCNTR\_EL0. On reads, returns the PMCCNTR\_EL0 enable status.

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | PMCCNTR_EL0 disabled. |
| 0b1 | PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;\_EL0 disable. On writes, allows software to disable PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                   |
|--------|---------------------------|
| 0b0    | PMEVCNTR<m>_EL0 disabled. |
| 0b1    | PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:

- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Otherwise:

| 30 29 28 27 26      | 25 24 23 22   |     | 12   | 21 20 19   | 18      | 17          | 16 15   | 14      | 13   |     | 11 10   |    | 9 8   | 7   | 6   | 5     | 4 3 2   | 1 0   |
|---------------------|---------------|-----|------|------------|---------|-------------|---------|---------|------|-----|---------|----|-------|-----|-----|-------|---------|-------|
| P30 P29 P28 P27 P26 | P25 P24       | P23 | P22  | P21        | P20 P19 | P18 P17 P16 | P15     | P14 P13 | P12  | P11 | P10     | P9 | P8    | P7  | P6  | P5 P4 | P3 P2   | P1 P0 |

## C, bit [31]

PMCCNTR\_EL0 disable. On writes, allows software to disable PMCCNTR\_EL0. On reads, returns the PMCCNTR\_EL0 enable status.

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | PMCCNTR_EL0 disabled. |
| 0b1 | PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;\_EL0 disable. On writes, allows software to disable PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                   |
|--------|---------------------------|
| 0b0    | PMEVCNTR<m>_EL0 disabled. |
| 0b1    | PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Accessing PMCNTENCLR\_EL0

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_ICNTR is implemented, or FEAT\_PMUv3p9 is implemented

[63:0] Accessible at offset 0xC20 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXT32 is implemented and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3\_ICNTR is not implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xC20 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.20 PMCNTENSET\_EL0, Performance Monitors Count Enable Set Register

The PMCNTENSET\_EL0 characteristics are:

## Purpose

Allows software to enable the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which counters are enabled.

## Configuration

PMCNTENSET\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCNTENSET\_EL0 are RES0.

## Attributes

PMCNTENSET\_EL0 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

PMICNTR\_EL0 enable. On writes, allows software to enable PMICNTR\_EL0. On reads, returns the PMICNTR\_EL0 enable status.

| F0   | Meaning               |
|------|-----------------------|
| 0b0  | PMICNTR_EL0 disabled. |
| 0b1  | PMICNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Otherwise:

Reserved, RES0.

## C, bit [31]

PMCCNTR\_EL0 enable. On writes, allows software to enable PMCCNTR\_EL0. On reads, returns the PMCCNTR\_EL0 enable status.

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | PMCCNTR_EL0 disabled. |
| 0b1 | PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;\_EL0 enable. On writes, allows software to enable PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                   |
|--------|---------------------------|
| 0b0    | PMEVCNTR<m>_EL0 disabled. |
| 0b1    | PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:

- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Otherwise:

| 30 29 28 27 26      | 25 24 23 22   |     | 12   | 21 20 19   | 18      | 17          | 16 15   | 14      | 13   |     | 11 10   |    | 9 8   | 7   | 6   | 5     | 4 3 2   | 1 0   |
|---------------------|---------------|-----|------|------------|---------|-------------|---------|---------|------|-----|---------|----|-------|-----|-----|-------|---------|-------|
| P30 P29 P28 P27 P26 | P25 P24       | P23 | P22  | P21        | P20 P19 | P18 P17 P16 | P15     | P14 P13 | P12  | P11 | P10     | P9 | P8    | P7  | P6  | P5 P4 | P3 P2   | P1 P0 |

## C, bit [31]

PMCCNTR\_EL0 enable. On writes, allows software to enable PMCCNTR\_EL0. On reads, returns the PMCCNTR\_EL0 enable status.

| C   | Meaning               |
|-----|-----------------------|
| 0b0 | PMCCNTR_EL0 disabled. |
| 0b1 | PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

PMEVCNTR&lt;m&gt;\_EL0 enable. On writes, allows software to enable PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                   |
|--------|---------------------------|
| 0b0    | PMEVCNTR<m>_EL0 disabled. |
| 0b1    | PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Accessing PMCNTENSET\_EL0

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_ICNTR is implemented, or FEAT\_PMUv3p9 is implemented

[63:0] Accessible at offset 0xC00 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXT32 is implemented and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3\_ICNTR is not implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xC00 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.21 PMCR\_EL0, Performance Monitors Control Register

The PMCR\_EL0 characteristics are:

## Purpose

Configures and controls the Performance Monitors counters.

## Configuration

PMCR\_EL0 is in the Core power domain.

This register is only partially mapped to the internal PMCR System register. An external agent must use other means to discover the information held in PMCR[31:11], such as accessing PMCFGR and the ID registers.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMCR\_EL0 are RES0.

## Attributes

PMCR\_EL0 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

FZS, bit [32]

## When FEAT\_SPEv1p2 is implemented:

Freeze-on-SPE event. Stop counters when PMBLIMITR\_EL1.{PMFZ,E} is {1,1} and profiling is stopped.

| FZS   | Meaning                                                                                   |
|-------|-------------------------------------------------------------------------------------------|
| 0b0   | Do not freeze on a Statistical Profiling Buffer Management event.                         |
| 0b1   | Affected counters do not count following a Statistical Profiling Buffer Management event. |

The pseudocode function SPEProfilingStopped describes when profiling is stopped.

The counters affected by this field are:

- The event counters in the first range.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- If FEAT\_SPE\_DPFZS is implemented and PMCR\_EL0.DP is 1, the cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

When FEAT\_SPE\_DPFZS is not implemented or PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA32 is implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [31:11]

Reserved, RAZ/WI.

Hardware must implement this field as RAZ/WI. Software must not rely on the register reading as zero, and must use a read-modify-write sequence to write to the register.

## Bit [10]

Reserved, RES0.

## FZO, bit [9]

## When FEAT\_PMUv3p7 is implemented:

Freeze-on-overflow. Stop event counters on overflow.

| FZO   | Meaning                                                                                                                                                                                                                                     |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Do not freeze on overflow.                                                                                                                                                                                                                  |
| 0b1   | Affected counters do not count when any of the following applies:                                                                                                                                                                           |
| 0b1   | • For any event counter PMEVCNTR<m>_EL0 in the first range, PMOVSCLR_EL0[m] is 1, and either FEAT_SEBEP is not implemented or PMEVTYPER<m>_EL0.SYNC is 0. • FEAT_PMUv3_ICNTR is implemented, PMOVSCLR_EL0.F0 is 1, and either FEAT_SEBEP is |
| 0b1   | not implemented or PMICFILTR_EL0.SYNC is 0.                                                                                                                                                                                                 |

The counters affected by this field are:

- The event counters in the first range.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- If PMCR\_EL0.DP is 1, the cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [8]

Reserved, RES0.

## LP, bit [7]

## When FEAT\_PMUv3p5 is implemented:

Long event counter enable. Determines when unsigned overflow is recorded by PMOVSCLR\_EL0.P[n].

| LP   | Meaning                                                                                     |
|------|---------------------------------------------------------------------------------------------|
| 0b0  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[31:0]. |
| 0b1  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

The counters affected by this field are the event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

Other event counters and PMCCNTR\_EL0 are not affected by this field.

When FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0 is not affected by this field.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LC, bit [6]

## When FEAT\_AA32 is implemented:

Long cycle counter enable. Determines when unsigned overflow is recorded by PMOVSCLR\_EL0.C.

| LC   | Meaning                                                                                 |
|------|-----------------------------------------------------------------------------------------|
| 0b0  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR_EL0[31:0]. |
| 0b1  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

Arm deprecates use of PMCR\_EL0.LC = 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## DP, bit [5]

## When ((HaveEL(EL3) || (IsFeatureImplemented(FEAT\_PMUv3p1) &amp;&amp; HaveEL(EL2))) || IsFeatureImplemented(FEAT\_PMUv3p7)) || IsFeatureImplemented(FEAT\_SPE\_DPFZS):

Disable cycle counter when event counting is prohibited.

| DP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Cycle counting by PMCCNTR_EL0 is not affected by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 0b1  | Cycle counting by PMCCNTR_EL0 is disabled in prohibited regions and when event counting is frozen: • If FEAT_PMUv3p1 is implemented, EL2 is implemented, and MDCR_EL2.HPMD or HDCR.HPMD is 1, then cycle counting by PMCCNTR_EL0 is disabled at EL2. • If FEAT_SPE_DPFZS is implemented and event counting is frozen by PMCR_EL0.FZS, then cycle counting by PMCCNTR_EL0 is disabled. • If FEAT_PMUv3p7 is implemented and event counting is frozen by PMCR_EL0.FZO, then cycle counting by PMCCNTR_EL0 is disabled. • If FEAT_PMUv3p7 is implemented, EL3 is implemented and using AArch64, and MDCR_EL3.MPMX is 1, then cycle counting by PMCCNTR_EL0 is disabled at EL3. • If EL3 is implemented, MDCR_EL3.SPME or SDCR.SPME is 0, and one of FEAT_PMUv3p7 is not implemented, EL3 is using AArch32, or MDCR_EL3.MPMX is 0, then cycle counting by PMCCNTR_EL0 is disabled at EL3 and in Secure state. |

The conditions when this field disables the cycle counter are the same as when event counting by an event counter in the first range is prohibited or frozen. For more information about event counter ranges, see MDCR\_EL2.HPMN.

If FEAT\_PMUv3p7 and FEAT\_SPEv1p2 are implemented, meaning PMCR\_EL0.FZS is implemented, and FEAT\_SPE\_DPFZS is not implemented, then cycle counting by PMCCNTR\_EL0 is not affected by PMCR\_EL0.FZS.

For more information, see 'Prohibiting event and cycle counting'.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## X, bit [4]

## When the implementation includes a PMU event export bus:

Enable export of events in an IMPLEMENTATION DEFINED PMU event export bus.

| X   | Meaning                             |
|-----|-------------------------------------|
| 0b0 | Do not export events.               |
| 0b1 | Export events where not prohibited. |

This field enables the exporting of events over an IMPLEMENTATION DEFINED PMU event export bus to another device.

No events are exported when counting is prohibited.

This field does not affect the generation of Performance Monitors overflow interrupt requests or signaling to a cross-trigger interface (CTI) that can be implemented as signals exported from the PE.

If FEAT\_ETE is implemented, this field does not affect the use of PMU events as an External Input by the trace unit.

If FEAT\_ETMv4 is implemented, this field does affect the use of PMU events as an External Input by the trace unit.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## D, bit [3]

## When FEAT\_AA32 is implemented:

Clock divider.

| D   | Meaning                                                      |
|-----|--------------------------------------------------------------|
| 0b0 | When enabled, PMCCNTR_EL0 counts every clock cycle.          |
| 0b1 | When enabled, PMCCNTR_EL0 counts once every 64 clock cycles. |

If the Effective value of PMCR\_EL0.LC is 1, then this field is ignored and the cycle counter counts every clock cycle.

Arm deprecates use of PMCR\_EL0.D = 1.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## C, bit [2]

Cycle counter reset. The effects of writing to this field are:

| C   | Meaning                    |
|-----|----------------------------|
| 0b0 | No action.                 |
| 0b1 | Reset PMCCNTR_EL0 to zero. |

Note

Resetting PMCCNTR\_EL0 does not change the cycle counter overflow field. The value of PMCR\_EL0.LC is ignored, and bits [63:0] of the cycle counter are reset.

Access to this field is WO/RAZ.

## P, bit [1]

Event counter reset.

| P   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | No action.                                                 |
| 0b1 | Reset all affected event counters PMEVCNTR<n>_EL0 to zero. |

The event counters affected by this field are:

- If FEAT\_PMUv3\_EXTPMN is implemented and the access to this register is a Most secure access, all event counters.
- Otherwise, only event counters in the first and second ranges.

Writes to this field do not affect other event counters, the cycle counter PMCCNTR\_EL0, or the instruction counter PMICNTR\_EL0.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

Note

Resetting the event counters does not change the event counter overflow fields. If FEAT\_PMUv3p5 is implemented, the values of MDCR\_EL2.HLP or HDCR.HLP and PMCR\_EL0.LP are ignored, and bits [63:0] of all affected event counters are reset.

Access to this field is WO/RAZ.

## E, bit [0]

Enable.

| E   | Meaning                                          |
|-----|--------------------------------------------------|
| 0b0 | Affected counters are disabled and do not count. |
| 0b1 | Affected counters are enabled by PMCNTENSET_EL0. |

The counters affected by this field are:

- The event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- The cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

<!-- image -->

| 31     | 11 10   | 9   | 8 7   |    | 6   | 5   | 4 3   | 2   | 1 0   |
|--------|---------|-----|-------|----|-----|-----|-------|-----|-------|
| RAZ/WI |         | FZO | LP    | LC | DP  | X   | D C   | P   | E     |

## Bits [31:11]

Reserved, RAZ/WI.

Hardware must implement this field as RAZ/WI. Software must not rely on the register reading as zero, and must use a read-modify-write sequence to write to the register.

## Bit [10]

Reserved, RES0.

## FZO, bit [9]

## When FEAT\_PMUv3p7 is implemented:

Freeze-on-overflow. Stop event counters on overflow.

| FZO   | Meaning                                                                                                                                                                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Do not freeze on overflow.                                                                                                                                                                                                                                                              |
| 0b1   | Affected counters do not count when any of the following applies:                                                                                                                                                                                                                       |
|       | • For any event counter PMEVCNTR<m>_EL0 in the first range, PMOVSCLR_EL0[m] is 1, and either FEAT_SEBEP is not implemented or PMEVTYPER<m>_EL0.SYNC is 0. • FEAT_PMUv3_ICNTR is implemented, PMOVSCLR_EL0.F0 is 1, and either FEAT_SEBEP is not implemented or PMICFILTR_EL0.SYNC is 0. |

The counters affected by this field are:

- The event counters in the first range.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- If PMCR\_EL0.DP is 1, the cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

When PMCR\_EL0.DP is 0, PMCCNTR\_EL0 is not affected by this field.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bit [8]

Reserved, RES0.

LP, bit [7]

## When FEAT\_PMUv3p5 is implemented:

Long event counter enable. Determines when unsigned overflow is recorded by PMOVSCLR\_EL0.P[n].

| LP   | Meaning                                                                                     |
|------|---------------------------------------------------------------------------------------------|
| 0b0  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[31:0]. |
| 0b1  | Event counter overflow on increment that causes unsigned overflow of PMEVCNTR<n>_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

The counters affected by this field are the event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

Other event counters and PMCCNTR\_EL0 are not affected by this field.

When FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0 is not affected by this field.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LC, bit [6]

## When FEAT\_AA32 is implemented:

Long cycle counter enable. Determines when unsigned overflow is recorded by PMOVSCLR\_EL0.C.

| LC   | Meaning                                                                                 |
|------|-----------------------------------------------------------------------------------------|
| 0b0  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR_EL0[31:0]. |
| 0b1  | Cycle counter overflow on increment that causes unsigned overflow of PMCCNTR_EL0[63:0]. |

When FEAT\_EBEP is implemented and the PMU Profiling exception is enabled, the Effective value of this field is 1.

Arm deprecates use of PMCR\_EL0.LC = 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## DP, bit [5]

When ((HaveEL(EL3) || (IsFeatureImplemented(FEAT\_PMUv3p1) &amp;&amp; HaveEL(EL2))) || IsFeatureImplemented(FEAT\_PMUv3p7)) || IsFeatureImplemented(FEAT\_SPE\_DPFZS):

Disable cycle counter when event counting is prohibited.

| DP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Cycle counting by PMCCNTR_EL0 is not affected by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 0b1  | Cycle counting by PMCCNTR_EL0 is disabled in prohibited regions and when event counting is frozen: • If FEAT_PMUv3p1 is implemented, EL2 is implemented, and MDCR_EL2.HPMD or HDCR.HPMD is 1, then cycle counting by PMCCNTR_EL0 is disabled at EL2. • If FEAT_SPE_DPFZS is implemented and event counting is frozen by PMCR_EL0.FZS, then cycle counting by PMCCNTR_EL0 is disabled. • If FEAT_PMUv3p7 is implemented and event counting is frozen by PMCR_EL0.FZO, then cycle counting by PMCCNTR_EL0 is disabled. • If FEAT_PMUv3p7 is implemented, EL3 is implemented and using AArch64, and MDCR_EL3.MPMX is 1, then cycle counting by PMCCNTR_EL0 is disabled at EL3. • If EL3 is implemented, MDCR_EL3.SPME or SDCR.SPME is 0, and one of FEAT_PMUv3p7 is not implemented, EL3 is using AArch32, or MDCR_EL3.MPMX is 0, then cycle counting by PMCCNTR_EL0 is disabled at EL3 and in Secure state. |

The conditions when this field disables the cycle counter are the same as when event counting by an event counter in the first range is prohibited or frozen. For more information about event counter ranges, see MDCR\_EL2.HPMN.

If FEAT\_PMUv3p7 and FEAT\_SPEv1p2 are implemented, meaning PMCR\_EL0.FZS is implemented, and FEAT\_SPE\_DPFZS is not implemented, then cycle counting by PMCCNTR\_EL0 is not affected by PMCR\_EL0.FZS.

For more information, see 'Prohibiting event and cycle counting'.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## X, bit [4]

## When the implementation includes a PMU event export bus:

Enable export of events in an IMPLEMENTATION DEFINED PMU event export bus.

| X   | Meaning                             |
|-----|-------------------------------------|
| 0b0 | Do not export events.               |
| 0b1 | Export events where not prohibited. |

This field enables the exporting of events over an IMPLEMENTATION DEFINED PMU event export bus to another device.

No events are exported when counting is prohibited.

This field does not affect the generation of Performance Monitors overflow interrupt requests or signaling to a cross-trigger interface (CTI) that can be implemented as signals exported from the PE.

If FEAT\_ETE is implemented, this field does not affect the use of PMU events as an External Input by the trace unit.

If FEAT\_ETMv4 is implemented, this field does affect the use of PMU events as an External Input by the trace unit.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAZ/WI.

## D, bit [3]

## When FEAT\_AA32 is implemented:

Clock divider.

| D   | Meaning                                                      |
|-----|--------------------------------------------------------------|
| 0b0 | When enabled, PMCCNTR_EL0 counts every clock cycle.          |
| 0b1 | When enabled, PMCCNTR_EL0 counts once every 64 clock cycles. |

If the Effective value of PMCR\_EL0.LC is 1, then this field is ignored and the cycle counter counts every clock cycle.

Arm deprecates use of PMCR\_EL0.D = 1.

The reset behavior of this field is:

- On a Warm reset:
- When FEAT\_AA64 is not implemented, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## C, bit [2]

Cycle counter reset. The effects of writing to this field are:

| C   | Meaning                    |
|-----|----------------------------|
| 0b0 | No action.                 |
| 0b1 | Reset PMCCNTR_EL0 to zero. |

Note

Resetting PMCCNTR\_EL0 does not change the cycle counter overflow field. The value of PMCR\_EL0.LC is ignored, and bits [63:0] of the cycle counter are reset.

Access to this field is WO/RAZ.

## P, bit [1]

Event counter reset.

| P   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | No action.                                                 |
| 0b1 | Reset all affected event counters PMEVCNTR<n>_EL0 to zero. |

The event counters affected by this field are:

- If FEAT\_PMUv3\_EXTPMN is implemented and the access to this register is a Most secure access, all event counters.
- Otherwise, only event counters in the first and second ranges.

Writes to this field do not affect other event counters, the cycle counter PMCCNTR\_EL0, or the instruction counter PMICNTR\_EL0.

For more information about event counter ranges, see MDCR\_EL2.HPMN.

Note

Resetting the event counters does not change the event counter overflow fields. If FEAT\_PMUv3p5 is implemented, the values of MDCR\_EL2.HLP or HDCR.HLP and PMCR\_EL0.LP are ignored, and bits [63:0] of all affected event counters are reset.

Access to this field is WO/RAZ.

## E, bit [0]

Enable.

| E   | Meaning                                          |
|-----|--------------------------------------------------|
| 0b0 | Affected counters are disabled and do not count. |
| 0b1 | Affected counters are enabled by PMCNTENSET_EL0. |

The counters affected by this field are:

- The event counters in the first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.
- If FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.
- The cycle counter PMCCNTR\_EL0.

Other event counters are not affected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing PMCR\_EL0

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

Accessible at offset 0xE04 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0xE10 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## I5.3.22 PMDEVAFF0, Performance Monitors Device Affinity register 0

The PMDEVAFF0 characteristics are:

## Purpose

Copy of the low half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the Performance Monitor component relates to.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented.

## Attributes

PMDEVAFF0 is a 32-bit register.

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

## Accessing PMDEVAFF0

If FEAT\_PMUv3\_EXT64 is implemented, then the same content is present in the same location, and can be accessed using PMDEVAFF[31:0].

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

Accessible at offset 0xFA8 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.23 PMDEVAFF1, Performance Monitors Device Affinity register 1

The PMDEVAFF1 characteristics are:

## Purpose

Copy of the high half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the Performance Monitor component relates to.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented.

## Attributes

PMDEVAFF1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## Aff3, bits [7:0]

Affinity level 3. See the description of PMDEV AFF0.Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMDEVAFF1

If FEAT\_PMUv3\_EXT64 is implemented, then the same content is present in the same location, and can be accessed using PMDEVAFF[63:32].

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

Accessible at offset 0xFAC from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.24 PMDEVAFF, Performance Monitors Device Affinity register

The PMDEVAFF characteristics are:

## Purpose

Copy of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the Performance Monitor component relates to.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is present only when FEAT\_PMUv3\_EXT64 is implemented.

## Attributes

PMDEVAFF is a 64-bit register.

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

RAO/WI

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

## Accessing PMDEVAFF

If FEAT\_PMUv3\_EXT32 is implemented, then the same content is present in the same locations, and can be accessed using PMDEVAFF0[31:0] and PMDEVAFF1[31:0].

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0xFA8 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.25 PMDEVARCH, Performance Monitors Device Architecture register

The PMDEVARCH characteristics are:

## Purpose

Identifies the programmers' model architecture of the Performance Monitor component.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMDEVARCHareRES0.

## Attributes

PMDEVARCHis a 32-bit register.

## Field descriptions

<!-- image -->

## ARCHITECT, bits [31:21]

Defines the architect of the component. For Performance Monitors, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as

0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the PMDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Defines the architecture revision. For architectures defined by Arm this is the minor revision.

For Performance Monitors, the revision defined by Armv8 is 0x0 .

All other values are reserved.

Reads as 0b0000

Access to this field is RO.

## ARCHVER,bits [15:12]

When UInt(PMU.PMDEVARCH.ARCHPART) == 0xA16 or UInt(PMU.PMDEVARCH.ARCHPART) == 0xA26 :

Architecture Version. Defines the architecture version of the component.

| ARCHVER   | Meaning                                          |
|-----------|--------------------------------------------------|
| 0b0010    | Performance Monitors Extension version 3, PMUv3. |

All other values are reserved.

PMDEVARCH.ARCHVER and PMDEVARCH.ARCHPART are also defined as a single field, PMDEVARCH.ARCHID, so that PMDEVARCH.ARCHVER is PMDEVARCH.ARCHID[15:12].

Access to this field is RO.

## Otherwise:

Architecture Version. Defines the architecture version of the component.

| ARCHVER   | Meaning                                             |
|-----------|-----------------------------------------------------|
| 0b0000    | PC Sample-based Profiling version 2, FEAT_PCSRv8p2. |

All other values are reserved.

PMDEVARCH.ARCHVER and PMDEVARCH.ARCHPART are also defined as a single field, PMDEVARCH.ARCHID, so that PMDEVARCH.ARCHVER is PMDEVARCH.ARCHID[15:12].

## ARCHPART, bits [11:0]

Architecture Part. Defines the architecture of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ARCHPART   | Meaning                                                                             |
|------------|-------------------------------------------------------------------------------------|
| 0xA10      | PC Sample-based Profiling, including the 32-bit programmers' model extension.       |
| 0xA16      | Armv8-A PE performance monitors, including the 32-bit programmers' model extension. |
| 0xA20      | PC Sample-based Profiling, including the 64-bit programmers' model extension.       |
| 0xA26      | Armv8-A PE performance monitors, including the 64-bit programmers' model extension. |

FEAT\_PMUv3\_EXT32 implements the functionality described by the values 0xA10 and 0xA16 .

FEAT\_PMUv3\_EXT64 implements the functionality described by the values 0xA20 and 0xA26 .

The values 0xA10 and 0xA20 indicate that FEAT\_PCSRv8p2 is implemented but the Performance Monitors Extension is not implemented.

PMDEVARCH.ARCHVER and PMDEVARCH.ARCHPART are also defined as a single field, PMDEVARCH.ARCHID, so that PMDEVARCH.ARCHPART is PMDEVARCH.ARCHID[11:0].

Access to this field is RO.

## Accessing PMDEVARCH

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFBC from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.26 PMDEVID, Performance Monitors Device ID register

The PMDEVID characteristics are:

## Purpose

Provides information about features of the Performance Monitors implementation.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is present only when (v8Ap2 or FEAT\_PCSRv8p2 is implemented) and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMDEVID are RES0.

## Attributes

PMDEVID is a 32-bit register.

## Field descriptions

| 31   | 12 11   | 8 7   | 4 3      |
|------|---------|-------|----------|
| RES0 | EXTPMN  | PMSS  | PCSample |

## Bits [31:12]

Reserved, RES0.

## EXTPMN, bits [11:8]

Reserving PMU event counters for external agents.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EXTPMN   | Meaning                                                                              |
|----------|--------------------------------------------------------------------------------------|
| 0b0000   | PMUv3 Extension for reserving PMUevent counters for external agents not implemented. |
| 0b0001   | PMUv3 Extension for reserving PMUevent counters for external agents implemented.     |

All other values are reserved.

FEAT\_PMUv3\_EXTPMN implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## PMSS, bits [7:4]

PMUSnapshot extension.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

FEAT\_PMUv3\_SS implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## PCSample, bits [3:0]

Indicates the level of PC Sample-based Profiling support using Performance Monitors registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PCSample   | Meaning                                                                                            |
|------------|----------------------------------------------------------------------------------------------------|
| 0b0000     | PC Sample-based Profiling Extension is not implemented in the Performance Monitors register space. |
| 0b0001     | PC Sample-based Profiling Extension is implemented in the Performance Monitors register space.     |
| 0b0010     | As 0b0001 , and adds support for PMPCSCTL.                                                         |

All other values are reserved.

FEAT\_PCSRv8p2 implements the functionality identified by the value 0b0001 .

FEAT\_PCSRv8p9 implements the functionality identified by the value 0b0010 .

If FEAT\_PCSRv8p2 is not implemented, then the only permitted value is 0b0000 .

From Armv8.2, when FEAT\_PCSRv8p2 is implemented, the value 0b0000 is not permitted.

From Armv8.9, when FEAT\_PCSRv8p9 is implemented, the value 0b0001 is not permitted.

Access to this field is RO.

## Accessing PMDEVID

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented and (v8Ap2 or FEAT\_PCSRv8p2 is implemented)

Accessible at offset 0xFC8 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

| PMSS   | Meaning                                |
|--------|----------------------------------------|
| 0b0000 | PMUsnapshot extension not implemented. |
| 0b0001 | PMUsnapshot extension implemented.     |

## I5.3.27 PMDEVTYPE, Performance Monitors Device Type register

The PMDEVTYPE characteristics are:

## Purpose

Indicates to a debugger that this component is part of a PE's performance monitor interface.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMDEVTYPE. Otherwise, direct accesses to PMDEVTYPE are RES0.

## Attributes

PMDEVTYPEis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SUB, bits [7:4]

Subtype. Indicates this is a component within a PE.

Reads as 0b0001

Access to this field is RO.

## MAJOR, bits [3:0]

Major type.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MAJOR   | Meaning                        |
|---------|--------------------------------|
| 0b0000  | Unspecified.                   |
| 0b0110  | Performance monitor component. |

FEAT\_PMUv3 implements the functionality described by the value 0b0110 .

Access to this field is RO.

## Accessing PMDEVTYPE

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFCC from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.28 PMEVCNTR&lt;n&gt;\_EL0, Performance Monitors Event Count Registers, n = 0 - 30

The PMEVCNTR&lt;n&gt;\_EL0 characteristics are:

## Purpose

Holds event counter &lt;n&gt;, which counts events, where &lt;n&gt; is 0 to 30.

## Configuration

PMEVCNTR&lt;n&gt;\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMEVCNTR&lt;n&gt;\_EL0 are RES0.

## Attributes

PMEVCNTR&lt;n&gt;\_EL0 is a:

- 64-bit register when FEAT\_PMUv3p5 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3p5 is implemented:

Event counter n

63

32

Event counter n

31

0

<!-- image -->

## EVCNT, bits [63:0]

Event counter n. Value of event counter n, where n is the number of this register and is a number from 0 to 30.

If the highest implemented Exception level is using AArch32, the optional external interface to the performance monitors is implemented, and the PMCR.LP and HDCR.HLP bits are RAZ/WI, then locations in the external interface to the performance monitors that map to PMEVCNTR&lt;n&gt;\_EL0[63:32] return UNKNOWN values on reads.

If the implementation does not support AArch64, bits [63:32] of the event counters are not required to be implemented.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

## EVCNT, bits [31:0]

Event counter n. Value of event counter n, where n is the number of this register and is a number from 0 to 30.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVCNTR&lt;n&gt;\_EL0

If FEAT\_PMUv3p5 is not implemented, when IsCorePowered(), DoubleLockStatus(), OSLockStatus() or !AllowExternalPMUAccess(), 32-bit accesses to 0x004 +8 × n have a CONSTRAINED UNPREDICTABLE behavior.

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x000 + (8 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p5 is implemented

[63:0] Accessible at offset 0x000 + (8 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p5 is not implemented

[31:0] Accessible at offset 0x000 + (8 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.29 PMEVCNTSVR&lt;n&gt;\_EL1, Performance Monitors Event Count Saved Value Registers, n = 0 - 30

The PMEVCNTSVR&lt;n&gt;\_EL1 characteristics are:

## Purpose

Captures the PMU Event counter &lt;n&gt;, PMEVCNTR&lt;n&gt;\_EL0.

## Configuration

PMEVCNTSVR&lt;n&gt;\_EL1 is in the Core power domain.

If event counter n is not implemented:

- When IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalPMUAccess(addrdesc), accesses are RES0.
- Otherwise, it is CONSTRAINED UNPREDICTABLE whether accesses to this register are RES0 or generate an error response.

This register is present only when FEAT\_PMUv3\_SS is implemented and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMEVCNTSVR&lt;n&gt;\_EL1 are RES0.

## Attributes

PMEVCNTSVR&lt;n&gt;\_EL1 is a 64-bit register.

## Field descriptions

EVCNT

63

32

EVCNT

31

0

<!-- image -->

## EVCNT, bits [63:0]

Sampled Event Count. The value of PMEVCNTR&lt;n&gt;\_EL0 at the last successful Capture event.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVCNTSVR&lt;n&gt;\_EL1

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_SS is implemented

Accessible at offset 0x600 + (8 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMSSAccess(addrdesc), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.3.30 PMEVTYPER&lt;n&gt;\_EL0, Performance Monitors Event Type Registers, n = 0 - 30

The PMEVTYPER&lt;n&gt;\_EL0 characteristics are:

## Purpose

Configures event counter n, where n is 0 to 30.

## Configuration

PMEVTYPER&lt;n&gt;\_EL0 is in the Core power domain.

If event counter n is not implemented:

- When IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalPMUAccess(), accesses are RES0.
- Otherwise, it is CONSTRAINED UNPREDICTABLE whether accesses to this register are RES0 or generate an error response.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMEVTYPER&lt;n&gt;\_EL0 are RES0.

## Attributes

PMEVTYPER&lt;n&gt;\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## TC, bits [63:61]

When (IsFeatureImplemented(FEAT\_PMUv3\_TH) &amp;&amp; ((!IsFeatureImplemented(FEAT\_PMUv3\_EDGE)) || (PMU.PMEVTYPER&lt;n&gt;\_EL0.TE == '0'))) &amp;&amp; (((!IsFeatureImplemented(FEAT\_PMUv3\_TH2)) || ((n MOD2)==0)) || (PMU.PMEVTYPER&lt;n&gt;\_EL0.TLC IN {'0x'})):

Threshold Control. Defines the threshold function. In the description of this field:

- VB[n] is the value the event specified by PMEVTYPER&lt;n&gt;\_EL0 would increment event counter n by on a processor cycle if the threshold function is disabled.
- For odd values of n, V[n-1] is the value that event counter n-1 increments by on the same processor cycle. V[n-1] is the result of applying the threshold and edge functions on event counter n-1. If event counter n-1 is disabled, then V[n-1] is zero. V[n-1] is not defined for even values of n.
- TH[n] is the value of PMEVTYPER&lt;n&gt;\_EL0.TH.

| TC    | Meaning                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------|
| 0b000 | Not-equal. The counter increments byV B [n] on each processor cycle whenV B [n] is not equal to TH[n].   |
| 0b001 | Not-equal, count. The counter increments by 1 on each processor cycle whenV B [n] is not equal to TH[n]. |

| TC    | Meaning                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------|
| 0b010 | Equals. The counter increments byV B [n] on each processor cycle whenV B [n] is equal to TH[n].                                  |
| 0b011 | Equals, count. The counter increments by 1 on each processor cycle whenV B [n] is equal to TH[n].                                |
| 0b100 | Greater-than-or-equal. The counter increments byV B [n] on each processor cycle whenV B [n] is greater than or equal to TH[n].   |
| 0b101 | Greater-than-or-equal, count. The counter increments by 1 on each processor cycle whenV B [n] is greater than or equal to TH[n]. |
| 0b110 | Less-than. The counter increments byV B [n] on each processor cycle whenV B [n] is less than TH[n].                              |
| 0b111 | Less-than, count. The counter increments by 1 on each processor cycle whenV B [n] is less than TH[n].                            |

Comparisons treat VB[n] and TH[n] as unsigned integer values.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC[2:1] is true:

- If PMEVTYPER&lt;n&gt;\_EL0.TC[0] is 0, then the counter increments by VB[n].
- If PMEVTYPER&lt;n&gt;\_EL0.TC[0] is 1, then the counter increments by 1.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC[2:1] is false:

- If FEAT\_PMUv3\_TH2 is implemented, n is odd, and PMEVTYPER&lt;n&gt;\_EL0.TLC is 0b01 , then the counter increments by V[n-1].
- Otherwise, the counter does not increment.

If PMEVTYPER&lt;n&gt;\_EL0.{TC, TLC, TH} are zero, then the threshold function is disabled.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '000' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## When FEAT\_PMUv3\_TH2 is implemented, PMU.PMEVTYPER&lt;n&gt;\_EL0.TE == '0', (n MOD 2) == 1, and PMU.PMEVTYPER&lt;n&gt;\_EL0.TLC == '10':

Threshold Control. Defines the threshold function. In the description of this field:

- VB[n] is the value the event specified by PMEVTYPER&lt;n&gt;\_EL0 would increment event counter n by on a processor cycle if the threshold function is disabled.
- V[n-1] is the value that event counter n-1 increments by on the same processor cycle. V[n-1] is the result of applying the threshold and edge functions on event counter n-1. If event counter n-1 is disabled, then V[n-1] is zero.
- TH[n] is the value of PMEVTYPER&lt;n&gt;\_EL0.TH.

| TC    | Meaning                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b000 | Not-equal. The counter increments by V[n-1] on each processor cycle whenV B [n] is not equal to TH[n].                         |
| 0b010 | Equals. The counter increments by V[n-1] on each processor cycle whenV B [n] is equal to TH[n].                                |
| 0b100 | Greater-than-or-equal. The counter increments by V[n-1] on each processor cycle whenV B [n] is greater than or equal to TH[n]. |
| 0b110 | Less-than. The counter increments by V[n-1] on each processor cycle whenV B [n] is less than TH[n].                            |

All other values are reserved.

Comparisons treat VB[n] and TH[n] as unsigned integer values.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is true, the counter increments by V[n-1].

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is false, the counter does not increment.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '000' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## When FEAT\_PMUv3\_EDGE is implemented and PMU.PMEVTYPER&lt;n&gt;\_EL0.TE == '1':

Threshold Control. Defines the threshold function. In the description of this field:

- VB[n] is the value the event specified by PMEVTYPER&lt;n&gt;\_EL0 would increment event counter n by on a processor cycle if the threshold function is disabled.
- For odd values of n, V[n-1] is the value that event counter n-1 increments by on the same processor cycle. V[n-1] is the result of applying the threshold and edge functions on event counter n-1. If event counter n-1 is disabled, then V[n-1] is zero. V[n-1] is not defined for even values of n.
- TH[n] is the value of PMEVTYPER&lt;n&gt;\_EL0.TH.

| TC    | Meaning                                                                                                                                                                                                                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b001 | Equal to not-equal. The counter increments on each processor cycle whenV B [n] is not equal to TH[n] andV B [n] was equal to TH[n] on the previous processor cycle.                                                                                                                                                          |
| 0b010 | Equal to/from not-equal. The counter increments on each processor cycle when either: • V B [n] is not equal to TH[n] andV B [n] was equal to TH[n] on the previous processor cycle. • V B [n] is equal to TH[n] andV B [n] was not equal to TH[n] on the previous processor cycle.                                           |
| 0b011 | Not-equal to equal. The counter increments on each processor cycle whenV B [n] is equal to TH[n] and V B [n] was not equal to TH[n] on the previous processor cycle.                                                                                                                                                         |
| 0b101 | Less-than to greater-than-or-equal. The counter increments on each processor cycle whenV B [n] is greater than or equal to TH[n] andV B [n] was less than TH[n] on the previous processor cycle.                                                                                                                             |
| 0b110 | Less-than to/from greater-than-or-equal. The counter increments on each processor cycle when either: • V B [n] is greater than or equal to TH[n] andV B [n] was less than TH[n] on the previous processor cycle. • V B [n] is less than TH[n] andV B [n] was greater than or equal to TH[n] on the previous processor cycle. |
| 0b111 | Greater-than-or-equal to less-than. The counter increments on each processor cycle whenV B [n] is less than TH[n] andV B [n] was greater than or equal to TH[n] on the previous processor cycle.                                                                                                                             |

All other values are reserved.

Comparisons treat VB[n] and TH[n] as unsigned integer values.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is true:

- If FEAT\_PMUv3\_TH2 is implemented, n is odd, and PMEVTYPER&lt;n&gt;\_EL0.TLC is 0b10 , then the counter increments by V[n-1].
- Otherwise, the counter increments by 1.

On each processor cycle when the condition specified by PMEVTYPER&lt;n&gt;\_EL0.TC is false, the counter does not increment.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '000' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TE, bit [60]

## When FEAT\_PMUv3\_EDGE is implemented:

Threshold Edge. Enables the edge condition. When PMEVTYPER&lt;n&gt;\_EL0.TE is 1, the event counter increments on cycles when the result of the threshold condition changes. See PMEVTYPER&lt;n&gt;\_EL0.TC for more information.

| TE   | Meaning                            |
|------|------------------------------------|
| 0b0  | Threshold edge condition disabled. |
| 0b1  | Threshold edge condition enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to '0' .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [59]

Reserved, RES0.

## SYNC, bit [58]

## When FEAT\_SEBEP is implemented:

Synchronous mode. Controls whether a PMU Profiling exception generated by the counter is synchronous or asynchronous.

| SYNC   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Asynchronous PMUProfiling exception is enabled. |
| 0b1    | Synchronous PMUProfiling exception is enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VS, bits [57:56]

## When FEAT\_PMUv3\_SME is implemented:

SVE mode filtering. Controls counting events in Streaming and Non-streaming SVE modes.

| VS   | Meaning                                                  |
|------|----------------------------------------------------------|
| 0b00 | This mechanism has no effect on the filtering of events. |
| 0b01 | The PE does not count events in Streaming SVE mode.      |
| 0b10 | The PE does not count events in Non-streaming SVE mode.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLC, bits [55:54]

## When FEAT\_PMUv3\_TH2 is implemented and (n MOD 2) == 1:

Threshold Linking Control. Extends PMEVTYPER&lt;n&gt;\_EL0.TC with additional controls for event linking. See PMEVTYPER&lt;n&gt;\_EL0.TC.

| TLC   | Meaning                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | Threshold linking disabled.                                                                                                                                                                               |
| 0b01  | Threshold linking enabled. If the threshold condition described by PMEVTYPER<n>_EL0.TC is false, the counter increments by V[n-1]. Otherwise, the counter increments as described by PMEVTYPER<n>_EL0.TC. |
| 0b10  | Threshold linking enabled. If the threshold condition described by PMEVTYPER<n>_EL0.TC is true, the counter increments by V[n-1]. Otherwise, the counter does not increment.                              |

All other values are reserved.

See PMEVTYPER&lt;n&gt;\_EL0.TC for more information

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [53:44]

Reserved, RES0.

## TH, bits [43:32]

## When FEAT\_PMUv3\_TH is implemented:

Threshold value. Provides the unsigned value for the threshold function defined by PMEVTYPER&lt;n&gt;\_EL0.TC.

If PMEVTYPER&lt;n&gt;\_EL0.{TC, TH} are both zero and either FEAT\_PMUv3\_TH2 is not implemented or PMEVTYPER&lt;n&gt;\_EL0.TLC is also zero, then the threshold function is disabled.

If PMU.PMMIR\_EL1.THWIDTH is less than 12, then bits

PMEVTYPER&lt;n&gt;\_EL0.TH[11:UInt(PMU.PMMIR\_EL1.THWIDTH)] are RES0. This accounts for the behavior when writing a value greater-than-or-equal-to 2 UInt(PMU.PMMIR\_EL1.THWIDTH) .

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_AA32EL1 is implemented, this field resets to 0x000 .
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## P, bit [31]

EL1 filtering. Controls counting events in EL1.

| P   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of events. |
| 0b1 | The PE does not count events in EL1.                 |

If Secure and Non-secure states are implemented, then counting events in Non-secure EL1 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.NSK.

If FEAT\_RME is implemented, then counting events in Realm EL1 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.RLK.

If EL3 is implemented, then counting events in EL3 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.M.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

EL0 filtering. Controls counting events in EL0.

| U   | Meaning                                              |
|-----|------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of events. |
| 0b1 | The PE does not count events in EL0.                 |

If Secure and Non-secure states are implemented, then counting events in Non-secure EL0 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.NSU.

If FEAT\_RME is implemented, then counting events in Realm EL0 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting events in Non-secure EL1. If PMEVTYPER&lt;n&gt;\_EL0.NSK is not equal to PMEVTYPER&lt;n&gt;\_EL0.P, then the PE does not count events in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of events in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.P == 1, the PE does not count events in Non-secure EL1. |
| 0b1   | When PMEVTYPER<n>_EL0.P == 0, the PE does not count events in Non-secure EL1. When PMEVTYPER<n>_EL0.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting events in Non-secure EL0. If PMEVTYPER&lt;n&gt;\_EL0.NSU is not equal to PMEVTYPER&lt;n&gt;\_EL0.U, then the PE does not count events in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of events in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.U == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.U == 1, the PE does not count events in Non-secure EL0. |
| 0b1   | When PMEVTYPER<n>_EL0.U == 0, the PE does not count events in Non-secure EL0. When PMEVTYPER<n>_EL0.U == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting events in EL2.

| NSH   | Meaning                                              |
|-------|------------------------------------------------------|
| 0b0   | The PE does not count events in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of events. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting events in Secure EL2 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.SH.

If FEAT\_RME is implemented, then counting events in Realm EL2 is further controlled by PMEVTYPER&lt;n&gt;\_EL0.RLH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## M, bit [26]

## When EL3 is implemented and FEAT\_AA64 is implemented:

EL3 filtering. Controls counting events in EL3. If PMEVTYPER&lt;n&gt;\_EL0.M is not equal to PMEVTYPER&lt;n&gt;\_EL0.P, then the PE does not count events in EL3. Otherwise, this mechanism has no effect on filtering of events in EL3.

| M   | Meaning                                                                                                                                               |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When PMEVTYPER<n>_EL0.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.P == 1, the PE does not count events in EL3. |
| 0b1 | When PMEVTYPER<n>_EL0.P == 0, the PE does not count events in EL3. When PMEVTYPER<n>_EL0.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MT, bit [25]

## When FEAT\_MTPMU is implemented or an IMPLEMENTATION DEFINED multi-threaded PMU extension is implemented:

Multithreading.

| MT   | Meaning                                                                          |
|------|----------------------------------------------------------------------------------|
| 0b0  | Count events only on controlling PE.                                             |
| 0b1  | Count events from any PE with the same affinity at level 1 and above as this PE. |

## Unless otherwise stated:

- If the event counts PE cycles when a stall condition is true and a second condition is true, then the counter counts Processor cycles when the stall condition is true for all of these PEs, and the second condition is true for any of these PEs.
- If the event counts PE cycles when any other condition is true, then the counter counts Processor cycles when the condition is true for any of these PEs.
- Otherwise, the event counts by the sum of the count across all of these PEs.

For the stall events, the stall condition means the applicable condition described by the STALL, STALL\_FRONTEND, or STALL\_BACKEND event.

The second condition is any condition in addition to this.

For example, for the STALL\_FRONTEND\_L1I event, the stall condition is STALL\_FRONTEND, and the second condition is when there is a demand instruction miss in the first level of instruction cache.

For the STALL, STALL\_FRONTEND, and STALL\_BACKEND events themselves, the second condition is the null TRUE condition.

See 'Multithreaded implementations' and 'Cycle event counting in multithreaded implementations'.

From Armv8.6, the IMPLEMENTATION DEFINED multi-threaded PMU extension is not permitted, meaning if FEAT\_MTPMU is not implemented, this field is RES0. See ID\_AA64DFR0\_EL1.MTPMU.

This field is ignored by the PE and treated as zero when FEAT\_MTPMU is implemented and disabled.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SH, bit [24]

## When EL3 is implemented and FEAT\_SEL2 is implemented:

Secure EL2 filtering. Controls counting events in Secure EL2. If PMEVTYPER&lt;n&gt;\_EL0.SH is equal to PMEVTYPER&lt;n&gt;\_EL0.NSH, then the PE does not count events in Secure EL2. Otherwise, this mechanism has no effect on filtering of events in Secure EL2.

| SH   | Meaning                                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMEVTYPER<n>_EL0.NSH == 0, the PE does not count events in Secure EL2. When PMEVTYPER<n>_EL0.NSH == 1, this mechanism has no effect on filtering of events. |

| SH   | Meaning                                                                                                                                                          |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1  | When PMEVTYPER<n>_EL0.NSH == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.NSH == 1, the PE does not count events in Secure EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

When Secure EL2 is not implemented, access to this field is RES0.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## RLK, bit [22]

## When FEAT\_RME is implemented:

Realm EL1 filtering. Controls counting events in Realm EL1. If PMEVTYPER&lt;n&gt;\_EL0.RLK is not equal to PMEVTYPER&lt;n&gt;\_EL0.P, then the PE does not count events in Realm EL1. Otherwise, this mechanism has no effect on filtering of events in Realm EL1.

| RLK   | Meaning                                                                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.P == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.P == 1, the PE does not count events in Realm EL1. |
| 0b1   | When PMEVTYPER<n>_EL0.P == 0, the PE does not count events in Realm EL1. When PMEVTYPER<n>_EL0.P == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting events in Realm EL0. If PMEVTYPER&lt;n&gt;\_EL0.RLU is not equal to PMEVTYPER&lt;n&gt;\_EL0.U, then the PE does not count events in Realm EL0. Otherwise, this mechanism has no effect on filtering of events in Realm EL0.

| RLU   | Meaning                                                                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.U == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.U == 1, the PE does not count events in Realm EL0. |
| 0b1   | When PMEVTYPER<n>_EL0.U == 0, the PE does not count events in Realm EL0. When PMEVTYPER<n>_EL0.U == 1, this mechanism has no effect on filtering of events. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLH, bit [20]

## When FEAT\_RME is implemented:

Realm EL2 filtering. Controls counting events in Realm EL2. If PMEVTYPER&lt;n&gt;\_EL0.RLH is equal to PMEVTYPER&lt;n&gt;\_EL0.NSH, then the PE does not count events in Realm EL2. Otherwise, this mechanism has no effect on filtering of events in Realm EL2.

| RLH   | Meaning                                                                                                                                                         |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMEVTYPER<n>_EL0.NSH == 0, the PE does not count events in Realm EL2. When PMEVTYPER<n>_EL0.NSH == 1, this mechanism has no effect on filtering of events. |
| 0b1   | When PMEVTYPER<n>_EL0.NSH == 0, this mechanism has no effect on filtering of events. When PMEVTYPER<n>_EL0.NSH == 1, the PE does not count events in Realm EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [19:16]

Reserved, RES0.

evtCount[15:10], bits [15:10]

## When FEAT\_PMUv3p1 is implemented:

Extension to evtCount[9:0]. For more information, see evtCount[9:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## evtCount[9:0], bits [9:0]

Event to count.

The event number of the event that is counted by event counter PMU.PMEVCNTR&lt;n&gt;\_EL0.

The ranges of event numbers allocated to each type of event are shown in 'Allocation of the PMU event number space'.

If FEAT\_PMUv3p8 is implemented and PMEVTYPER&lt;n&gt;\_EL0.evtCount is programmed to an event that is reserved or not supported by the PE, no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is the value written to the field.

Note

Arm recommends this behavior for all implementations of FEAT\_PMUv3.

Otherwise, if PMEVTYPER&lt;n&gt;\_EL0.evtCount is programmed to an event that is reserved or not supported by the PE, the behavior depends on the value written:

- For the range 0x0000 to 0x003F , no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is the value written to the field.
- If FEAT\_PMUv3p1 is implemented, for the range 0x4000 to 0x403F , no events are counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is the value written to the field.
- For other values, it is UNPREDICTABLE what event, if any, is counted and the value returned by a direct or external read of the PMEVTYPER&lt;n&gt;\_EL0.evtCount field is UNKNOWN.

Note

UNPREDICTABLE means the event must not expose privileged information.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMEVTYPER&lt;n&gt;\_EL0

If FEAT\_PMUv3\_EXT32 is implemented and any of the following apply, then bits [63:32] of this register are accessible at offset 0xA00 + (4*n):

- FEAT\_PMUv3\_TH is implemented.
- FEAT\_PMUv3p8 is implemented.
- FEAT\_PMUv3\_SME is implemented.

Otherwise accesses at this offset are IMPLEMENTATION DEFINED.

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x400 + (8 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented

[31:0] Accessible at offset 0x400 + (4 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When IsFeatureImplemented(FEAT\_PMUv3\_EXT32) &amp;&amp; ((IsFeatureImplemented(FEAT\_PMUv3\_TH) || IsFeatureImplemented(FEAT\_PMUv3p8)) || IsFeatureImplemented(FEAT\_PMUv3\_SME))

[63:32] Accessible at offset 0xA00 + (4 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.31 PMEVFILT2R&lt;n&gt;, Performance Monitors Event Filter Registers, n = 0 - 63

The PMEVFILT2R&lt;n&gt; characteristics are:

## Purpose

Provides additional IMPLEMENTATION DEFINED configuration controls for PMU counters.

Each PMEVFILT2R&lt;n&gt; register can provide additional configuration controls for a PMU counter, where:

- For values of n less than 31, if event counter n is implemented, then the controls are for PMU event counter &lt;n&gt;.
- For n equal to 31, the controls are for the cycle counter, PMCCNTR\_EL0;
- For n equal to 32, if FEAT\_PMUv3\_ICNTR is implemented, the controls are for the instruction counter, PMICNTR\_EL0;
- For all other values of n, PMEVFILT2R&lt;n&gt; is not implemented.

Although this mapping is recommended, it is not required and the function of each register is IMPLEMENTATION DEFINED.

## Configuration

PMEVFILT2R&lt;n&gt; is in the Core power domain.

If PMEVFILT2R&lt;n&gt; is not implemented:

- When IsCorePowered() &amp;&amp; !DoubleLockStatus() &amp;&amp; !OSLockStatus() &amp;&amp; AllowExternalPMUAccess(), accesses are RES0.
- Otherwise, it is CONSTRAINED UNPREDICTABLE whether accesses to this register are RES0 or generate an error response.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMEVFILT2R&lt;n&gt;. Otherwise, direct accesses to PMEVFILT2R&lt;n&gt; are RES0.

## Attributes

PMEVFILT2R&lt;n&gt; is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented:

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [63:0]

IMPLEMENTATION DEFINED.

## Otherwise:

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

## Accessing PMEVFILT2R&lt;n&gt;

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented

[31:0] Accessible at offset 0x800 + (4 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x800 + (8 * n) from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXTPMN is implemented, IsRange3Counter(n), and !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## I5.3.32 PMICFILTR\_EL0, Performance Monitors Instruction Counter Filter Register

The PMICFILTR\_EL0 characteristics are:

## Purpose

Configures the Instruction Counter.

## Configuration

PMICFILTR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_ICNTR is implemented and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMICFILTR\_EL0 are RES0.

## Attributes

PMICFILTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:59]

Reserved, RES0.

## SYNC, bit [58]

## When FEAT\_SEBEP is implemented:

Synchronous mode. Controls whether a PMU Profiling exception generated by the counter is synchronous or asynchronous.

| SYNC   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | Asynchronous PMUProfiling exception is enabled. |
| 0b1    | Synchronous PMUProfiling exception is enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VS, bits [57:56]

## When FEAT\_PMUv3\_SME is implemented:

SVE mode filtering. Controls counting instructions in Streaming and Non-streaming SVE modes.

| VS   | Meaning                                                        |
|------|----------------------------------------------------------------|
| 0b00 | This mechanism has no effect on the filtering of instructions. |
| 0b01 | The PE does not count instructions in Streaming SVE mode.      |
| 0b10 | The PE does not count instructions in Non-streaming SVE mode.  |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [55:32]

Reserved, RES0.

## P, bit [31]

EL1 filtering. Controls counting instructions in EL1.

| P   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of instructions. |
| 0b1 | The PE does not count instructions in EL1.                 |

If Secure and Non-secure states are implemented, then counting instructions in Non-secure EL1 is further controlled by PMICFILTR\_EL0.NSK.

If FEAT\_RME is implemented, then counting instructions in Realm EL1 is further controlled by PMICFILTR\_EL0.RLK.

If EL3 is implemented, then counting instructions in EL3 is further controlled by PMICFILTR\_EL0.M.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## U, bit [30]

EL0 filtering. Controls counting instructions in EL0.

| U   | Meaning                                                    |
|-----|------------------------------------------------------------|
| 0b0 | This mechanism has no effect on filtering of instructions. |
| 0b1 | The PE does not count instructions in EL0.                 |

If Secure and Non-secure states are implemented, then counting instructions in Non-secure EL0 is further controlled by PMICFILTR\_EL0.NSU.

If FEAT\_RME is implemented, then counting instructions in Realm EL0 is further controlled by PMICFILTR\_EL0.RLU.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## NSK, bit [29]

## When EL3 is implemented:

Non-secure EL1 filtering. Controls counting instructions in Non-secure EL1. If PMICFILTR\_EL0.NSK is not equal to PMICFILTR\_EL0.P, then the PE does not count instructions in Non-secure EL1. Otherwise, this mechanism has no effect on filtering of instructions in Non-secure EL1.

| NSK   | Meaning                                                                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.P == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.P == 1, the PE does not count instructions in Non-secure EL1. |
| 0b1   | When PMICFILTR_EL0.P == 0, the PE does not count instructions in Non-secure EL1. When PMICFILTR_EL0.P == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSU, bit [28]

## When EL3 is implemented:

Non-secure EL0 filtering. Controls counting instructions in Non-secure EL0. If PMICFILTR\_EL0.NSU is not equal to PMICFILTR\_EL0.U, then the PE does not count instructions in Non-secure EL0. Otherwise, this mechanism has no effect on filtering of instructions in Non-secure EL0.

| NSU   | Meaning                                                                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.U == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.U == 1, the PE does not count instructions in Non-secure EL0. |
| 0b1   | When PMICFILTR_EL0.U == 0, the PE does not count instructions in Non-secure EL0. When PMICFILTR_EL0.U == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NSH, bit [27]

## When EL2 is implemented:

EL2 filtering. Controls counting instructions in EL2.

| NSH   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | The PE does not count instructions in EL2.                 |
| 0b1   | This mechanism has no effect on filtering of instructions. |

If EL3 is implemented and FEAT\_SEL2 is implemented, then counting instructions in Secure EL2 is further controlled by PMICFILTR\_EL0.SH.

If FEAT\_RME is implemented, then counting instructions in Realm EL2 is further controlled by PMICFILTR\_EL0.RLH.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

M, bit [26]

## When EL3 is implemented:

EL3 filtering. Controls counting instructions in EL3. If PMICFILTR\_EL0.M is not equal to PMICFILTR\_EL0.P, then the PE does not count instructions in EL3. Otherwise, this mechanism has no effect on filtering of instructions in EL3.

| M   | Meaning                                                                                                                                                     |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When PMICFILTR_EL0.P == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.P == 1, the PE does not count instructions in EL3. |
| 0b1 | When PMICFILTR_EL0.P == 0, the PE does not count instructions in EL3. When PMICFILTR_EL0.P == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [25]

Reserved, RES0.

## SH, bit [24]

## When EL3 is implemented and FEAT\_SEL2 is implemented:

Secure EL2 filtering. Controls counting instructions in Secure EL2. If PMICFILTR\_EL0.SH is equal to PMICFILTR\_EL0.NSH, then the PE does not count instructions in Secure EL2. Otherwise, this mechanism has no effect on filtering of instructions in Secure EL2.

| SH   | Meaning                                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When PMICFILTR_EL0.NSH == 0, the PE does not count instructions in Secure EL2. When PMICFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of instructions. |
| 0b1  | When PMICFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.NSH == 1, the PE does not count instructions in Secure EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

When Secure EL2 is not implemented, access to this field is RES0.

## Otherwise:

Reserved, RES0.

## Bit [23]

Reserved, RES0.

## RLK, bit [22]

## When FEAT\_RME is implemented:

Realm EL1 filtering. Controls counting instructions in Realm EL1. If PMICFILTR\_EL0.RLK is not equal to PMICFILTR\_EL0.P, then the PE does not count instructions in Realm EL1. Otherwise, this mechanism has no effect on filtering of instructions in Realm EL1.

| RLK   | Meaning                                                                                                                                                           |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.P == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.P == 1, the PE does not count instructions in Realm EL1. |
| 0b1   | When PMICFILTR_EL0.P == 0, the PE does not count instructions in Realm EL1. When PMICFILTR_EL0.P == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## RLU, bit [21]

## When FEAT\_RME is implemented:

Realm EL0 filtering. Controls counting instructions in Realm EL0. If PMICFILTR\_EL0.RLU is not equal to PMICFILTR\_EL0.U, then the PE does not count instructions in Realm EL0. Otherwise, this mechanism has no effect on filtering of instructions in Realm EL0.

| RLU   | Meaning                                                                                                                                                           |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.U == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.U == 1, the PE does not count instructions in Realm EL0. |
| 0b1   | When PMICFILTR_EL0.U == 0, the PE does not count instructions in Realm EL0. When PMICFILTR_EL0.U == 1, this mechanism has no effect on filtering of instructions. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

RLH, bit [20]

## When FEAT\_RME is implemented:

Realm EL2 filtering. Controls counting instructions in Realm EL2. If PMICFILTR\_EL0.RLH is equal to PMICFILTR\_EL0.NSH, then the PE does not count instructions in Realm EL2. Otherwise, this mechanism has no effect on filtering of instructions in Realm EL2.

| RLH   | Meaning                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When PMICFILTR_EL0.NSH == 0, the PE does not count instructions in Realm EL2. When PMICFILTR_EL0.NSH == 1, this mechanism has no effect on filtering of instructions. |
| 0b1   | When PMICFILTR_EL0.NSH == 0, this mechanism has no effect on filtering of instructions. When PMICFILTR_EL0.NSH == 1, the PE does not count instructions in Realm EL2. |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [19:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count.

Reads as 0x0008

Access to this field is RO.

## Accessing PMICFILTR\_EL0

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3\_ICNTR is implemented

[31:0] Accessible at offset 0x480 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT64 is implemented and FEAT\_PMUv3\_ICNTR is implemented

[63:0] Accessible at offset 0x500 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3\_ICNTR is implemented

[63:32] Accessible at offset 0xA80 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.33 PMICNTR\_EL0, Performance Monitors Instruction Counter Register

The PMICNTR\_EL0 characteristics are:

## Purpose

If event counting is not prohibited and the instruction counter is enabled, the counter increments for each architecturally-executed instruction, according to the configuration specified by PMICFILTR\_EL0.

## Configuration

PMICNTR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_ICNTR is implemented. Otherwise, direct accesses to PMICNTR\_EL0 are RES0.

## Attributes

PMICNTR\_EL0 is a 64-bit register.

## Field descriptions

ICNT

63

32

ICNT

31

0

## ICNT, bits [63:0]

Instruction Counter.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMICNTR\_EL0

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_ICNTR is implemented

Accessible at offset 0x100 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.34 PMICNTSVR\_EL1, Performance Monitors Instruction Count Saved Value Register

The PMICNTSVR\_EL1 characteristics are:

## Purpose

Captures the PMU Instruction counter, PMICNTR\_EL0.

## Configuration

This register is present only when FEAT\_PMUv3\_ICNTR is implemented, FEAT\_PMUv3\_SS is implemented, and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMICNTSVR\_EL1 are RES0.

## Attributes

PMICNTSVR\_EL1 is a 64-bit register.

## Field descriptions

ICNT

63

32

ICNT

31

0

<!-- image -->

## ICNT, bits [63:0]

Sampled Instruction Count. The value of PMICNTR\_EL0 at the last successful Capture event.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## Accessing PMICNTSVR\_EL1

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_SS is implemented and FEAT\_PMUv3\_ICNTR is implemented

Accessible at offset 0x700 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMSSAccess(addrdesc), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.35 PMIIDR, Performance Monitors Implementation Identification Register

The PMIIDR characteristics are:

## Purpose

Provides discovery information about the Performance Monitor component.

## Configuration

This register is present only when (FEAT\_PMUv3\_EXT32 is implemented and an implementation implements PMIIDR) or FEAT\_PMUv3\_EXT64 is implemented. Otherwise, direct accesses to PMIIDR are RES0.

## Attributes

PMIIDR is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

## When FEAT\_PMUv3\_EXT64 is implemented:

<!-- image -->

| 63   |       |          |       |             | 32   |
|------|-------|----------|-------|-------------|------|
|      |       | RES0     |       |             |      |
| 31   | 20 19 | 16 15    | 12 11 |             | 0    |
|      |       | Revision |       | Implementer |      |

## Bits [63:32]

Reserved, RES0.

## ProductID, bits [31:20]

Part number, bits [11:0]. The part number is selected by the designer of the component.

Matches the PMPIDR1.PART\_1, PMPIDR0.PART\_0 fields if present.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Variant, bits [19:16]

Component major revision.

Defines either a variant of the component defined by PMIIDR.ProductID, or the major revision of the component.

When defining a major revision, PMIIDR.Variant and PMIIDR.Revision together form the revision number of the component, with this field being the most significant part.

When a component is changed, PMIIDR.Variant or PMIIDR.Revision is increased to ensure that software can differentiate between different revisions of the component. If this field is increased, PMIIDR.Revision should be set to 0b0000 .

Matches the PMPIDR2.REVISION field, if present.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Revision, bits [15:12]

Component minor revision.

PMIIDR.Variant and PMIIDR.Revision together form the revision number of the component, with this field being the least significant part.

When a component is changed, PMIIDR.Variant or PMIIDR.Revision is increased to ensure that software can differentiate between different revisions of the component. If PMIIDR.Variant field is increased, this field should be set to 0b0000 , otherwise the value in this field should be increased.

Matches the PMPIDR3.REVAND field, if present.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Implementer, bits [11:0]

Contains the JEP106 manufacturer's identification code of the designer of the PMU.

The code identifies the designer of the component, which might not be the same as the implementer of the device containing the component.

Zero is not a valid JEP106 identification code, meaning a value of zero for PMIIDR indicates this register is not implemented.

For an implementation designed by Arm, this field reads as 0x43B .

This field has an IMPLEMENTATION DEFINED value.

Bits [11:8] contain the JEP106 bank identifier of the designer minus 1.

Bit 7 is RES0.

Bits [6:0] contain bits [6:0] of the JEP106 manufacturer's identification code of the designer.

If PMPIDR4 is implemented, PMPIDR4.DES\_2 matches bits [11:8] of this field.

If PMPIDR2 is implemented, PMPIDR2.DES\_1 matches bits [6:4] of this field.

If PMPIDR1 is implemented, PMPIDR1.DES\_0 matches bits [3:0] of this field.

Access to this field is RO.

## Otherwise:

| 31        | 20 19   | 16 15    | 12 11       |
|-----------|---------|----------|-------------|
| ProductID | Variant | Revision | Implementer |

## ProductID, bits [31:20]

Part number, bits [11:0]. The part number is selected by the designer of the component.

Matches the PMPIDR1.PART\_1, PMPIDR0.PART\_0 fields if present.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Variant, bits [19:16]

Component major revision.

Defines either a variant of the component defined by PMIIDR.ProductID, or the major revision of the component.

When defining a major revision, PMIIDR.Variant and PMIIDR.Revision together form the revision number of the component, with this field being the most significant part.

When a component is changed, PMIIDR.Variant or PMIIDR.Revision is increased to ensure that software can differentiate between different revisions of the component. If this field is increased, PMIIDR.Revision should be set to 0b0000 .

Matches the PMPIDR2.REVISION field, if present.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Revision, bits [15:12]

Component minor revision.

PMIIDR.Variant and PMIIDR.Revision together form the revision number of the component, with this field being the least significant part.

When a component is changed, PMIIDR.Variant or PMIIDR.Revision is increased to ensure that software can differentiate between different revisions of the component. If PMIIDR.Variant field is increased, this field should be set to 0b0000 , otherwise the value in this field should be increased.

Matches the PMPIDR3.REVAND field, if present.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Implementer, bits [11:0]

Contains the JEP106 manufacturer's identification code of the designer of the PMU.

The code identifies the designer of the component, which might not be the same as the implementer of the device containing the component.

Zero is not a valid JEP106 identification code, meaning a value of zero for PMIIDR indicates this register is not implemented.

For an implementation designed by Arm, this field reads as 0x43B .

This field has an IMPLEMENTATION DEFINED value.

Bits [11:8] contain the JEP106 bank identifier of the designer minus 1.

Bit 7 is RES0.

Bits [6:0] contain bits [6:0] of the JEP106 manufacturer's identification code of the designer.

If PMPIDR4 is implemented, PMPIDR4.DES\_2 matches bits [11:8] of this field.

If PMPIDR2 is implemented, PMPIDR2.DES\_1 matches bits [6:4] of this field.

If PMPIDR1 is implemented, PMPIDR1.DES\_0 matches bits [3:0] of this field.

Access to this field is RO.

## Accessing PMIIDR

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xE08 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.36 PMINTENCLR\_EL1, Performance Monitors Interrupt Enable Clear Register

The PMINTENCLR\_EL1 characteristics are:

## Purpose

Allows software to disable the generation of interrupt requests or, when FEAT\_EBEP is implemented, PMU Profiling exceptions on overflows from the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which overflow interrupt requests or PMU Profiling exceptions are enabled.

## Configuration

PMINTENCLR\_EL1 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMINTENCLR\_EL1 are RES0.

## Attributes

PMINTENCLR\_EL1 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 enable status.

| F0   | Meaning                                                                                   |
|------|-------------------------------------------------------------------------------------------|
| 0b0  | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 disabled. |

| 0b1   | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 enabled.   |
|-------|--------------------------------------------------------------------------------------------|

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable status.

| C   | Meaning                                                                                   |
|-----|-------------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 disabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Otherwise:

<!-- image -->

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------------------------------------------------|

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable status.

| C   | Meaning                                                                                   |
|-----|-------------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 disabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 disable. On writes, allows software to disable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Accessing PMINTENCLR\_EL1

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_ICNTR is implemented, or FEAT\_PMUv3p9 is implemented

[63:0] Accessible at offset 0xC60 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXT32 is implemented and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3\_ICNTR is not implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xC60 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.37 PMINTEN, Performance Monitors Interrupt Enable register

The PMINTEN characteristics are:

## Purpose

Enables the generation of interrupt requests on overflows from the Cycle Count Register, PMCCNTR\_EL0, and the event counters PMEVCNTR&lt;n&gt;\_EL0.

## Configuration

This register is present only when FEAT\_PMUv3\_EXT64 is implemented. Otherwise, direct accesses to PMINTEN are RES0.

## Attributes

PMINTEN is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Interrupt request on unsigned overflow of PMICNTR\_EL0 enable.

| F0   | Meaning                                                         |
|------|-----------------------------------------------------------------|
| 0b0  | Interrupt request on unsigned overflow of PMICNTR_EL0 disabled. |
| 0b1  | Interrupt request on unsigned overflow of PMICNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## C, bit [31]

PMCCNTR\_EL0 unsigned overflow interrupt request enable bit. Possible values are:

| C   | Meaning                                                   |
|-----|-----------------------------------------------------------|
| 0b0 | The cycle counter overflow interrupt request is disabled. |
| 0b1 | The cycle counter overflow interrupt request is enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Event counter unsigned overflow interrupt request enable bit for PMEVCNTR&lt;m&gt;\_EL0.

| P<m>   | Meaning                                                          |
|--------|------------------------------------------------------------------|
| 0b0    | The PMEVCNTR<m>_EL0 event counter interrupt request is disabled. |
| 0b1    | The PMEVCNTR<m>_EL0 event counter interrupt request is enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- Otherwise, access to this field is RW.

## Accessing PMINTEN

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0xC50 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## I5.3.38 PMINTENSET\_EL1, Performance Monitors Interrupt Enable Set Register

The PMINTENSET\_EL1 characteristics are:

## Purpose

Allows software to enable the generation of interrupt requests or, when FEAT\_EBEP is implemented, PMU Profiling exceptions on overflows from the following counters:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows which overflow interrupt requests or PMU Profiling exceptions are enabled.

## Configuration

PMINTENSET\_EL1 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMINTENSET\_EL1 are RES0.

## Attributes

PMINTENSET\_EL1 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMICNTR\_EL0 enable status.

| F0   | Meaning                                                                                   |
|------|-------------------------------------------------------------------------------------------|
| 0b0  | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 disabled. |

| 0b1   | Interrupt request or PMUProfiling exception on unsigned overflow of PMICNTR_EL0 enabled.   |
|-------|--------------------------------------------------------------------------------------------|

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable status.

| C   | Meaning                                                                                   |
|-----|-------------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 disabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Otherwise:

<!-- image -->

| 31   | 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------------------------------------------------|

## C, bit [31]

Interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMCCNTR\_EL0 enable status.

| C   | Meaning                                                                                   |
|-----|-------------------------------------------------------------------------------------------|
| 0b0 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 disabled. |
| 0b1 | Interrupt request or PMUProfiling exception on unsigned overflow of PMCCNTR_EL0 enabled.  |

## The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable. On writes, allows software to enable the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0. On reads, returns the interrupt request or PMU Profiling exception on unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0 enable status.

| P<m>   | Meaning                                                                                       |
|--------|-----------------------------------------------------------------------------------------------|
| 0b0    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 disabled. |
| 0b1    | Interrupt request or PMUProfiling exception on unsigned overflow of PMEVCNTR<m>_EL0 enabled.  |

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Accessing PMINTENSET\_EL1

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_ICNTR is implemented, or FEAT\_PMUv3p9 is implemented

[63:0] Accessible at offset 0xC40 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXT32 is implemented and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3\_ICNTR is not implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xC40 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.39 PMITCTRL, Performance Monitors Integration mode Control register

The PMITCTRL characteristics are:

## Purpose

Enables the Performance Monitors to switch from default mode into integration mode, where test software can control directly the inputs and outputs of the PE, for integration testing or topology detection.

## Configuration

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMITCTRL. Otherwise, direct accesses to PMITCTRL are RES0.

## Attributes

PMITCTRL is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 1 0   |
|------|-------|
|      | IME   |

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

- If the register is implemented in the Core power domain:
- On a Cold reset, this field resets to 0.
- On an External debug reset, the value of this field is unchanged.
- On a Warm reset, the value of this field is unchanged.
- If the register is implemented in the External debug power domain:
- On a Cold reset, the value of this field is unchanged.
- On an External debug reset, this field resets to 0.
- On a Warm reset, the value of this field is unchanged.

## Accessing PMITCTRL

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xF00 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.40 PMLAR, Performance Monitors Lock Access Register

The PMLAR characteristics are:

## Purpose

Allows or disallows access to the Performance Monitors registers through a memory-mapped interface.

The optional Software Lock provides a lock to prevent memory-mapped writes to the Performance Monitors registers. Use of this lock mechanism reduces the risk of accidental damage to the contents of the Performance Monitors registers. It does not, and cannot, prevent all accidental or malicious damage.

## Configuration

If FEAT\_DoPD is implemented, Software Lock is not implemented by the architecturally-defined debug components of the PE in the Core power domain.

If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

Software uses PMLAR to set or clear the lock, and PMLSR to check the current status of the lock.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMLAR are RES0.

## Attributes

PMLARis a 32-bit register.

## Field descriptions

When PMU Software Lock is implemented:

<!-- image -->

## KEY, bits [31:0]

Lock Access control. Writing the key value 0xC5ACCE55 to this field unlocks the lock, enabling write accesses to this component's registers through a memory-mapped interface.

Writing any other value to this register locks the lock, disabling write accesses to this component's registers through a memory mapped interface.

## Otherwise:

<!-- image -->

Otherwise

## Bits [31:0]

Reserved, RES0.

## Accessing PMLAR

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFB0 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are WO.

## I5.3.41 PMLSR, Performance Monitors Lock Status Register

The PMLSR characteristics are:

## Purpose

Indicates the current status of the software lock for Performance Monitors registers.

The optional Software Lock provides a lock to prevent memory-mapped writes to the Performance Monitors registers. Use of this lock mechanism reduces the risk of accidental damage to the contents of the Performance Monitors registers. It does not, and cannot, prevent all accidental or malicious damage.

## Configuration

If FEAT\_DoPD is implemented, Software Lock is not implemented by the architecturally-defined debug components of the PE in the Core power domain.

If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

Software uses PMLAR to set or clear the lock, and PMLSR to check the current status of the lock.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMLSR are RES0.

## Attributes

PMLSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## nTT, bit [2]

Not thirty-two bit access required.

Reads as 0b0

Access to this field is RO.

## SLK, bit [1]

## When PMU Software Lock is implemented and FEAT\_DoPD is not implemented:

Software Lock status for this component. For an access to LSR that is not a memory-mapped access, or when Software Lock is not implemented, this field is RES0.

For memory-mapped accesses when Software Lock is implemented, possible values of this field are:

| SLK   | Meaning                                                         |
|-------|-----------------------------------------------------------------|
| 0b0   | Lock clear. Writes are permitted to this component's registers. |

0b1

Lock set. Writes to this component's registers are ignored, and reads have no side effects.

The reset behavior of this field is:

- On a External debug reset, this field resets to '1' .

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

## Accessing PMLSR

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFB4 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.42 PMMIR, Performance Monitors Machine Identification Register

The PMMIR characteristics are:

## Purpose

Describes Performance Monitors parameters specific to the implementation.

## Configuration

PMMIRis in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p4 is implemented. Otherwise, direct accesses to PMMIR are RES0.

## Attributes

PMMIRis a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented or FEAT\_PMUv3p9 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented or FEAT\_PMUv3p9 is implemented:

<!-- image -->

## Bits [63:29]

Reserved, RES0.

## SME, bit [28]

PMUv3 for SME. Adds support for the Streaming SVE mode filter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SME   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Streaming SVE mode filter not implemented.      |
| 0b1   | Adds support for the Streaming SVE mode filter. |

All other values are reserved.

FEAT\_PMUv3\_SME implements the functionality identified by the value 1.

Access to this field is RO.

## EDGE, bits [27:24]

PMUevent edge detection. With PMMIR\_EL1.THWIDTH, indicates implementation of event counter thresholding features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EDGE   | Meaning                                                                              |
|--------|--------------------------------------------------------------------------------------|
| 0b0000 | FEAT_PMUv3_EDGE is not implemented.                                                  |
| 0b0001 | FEAT_PMUv3_EDGE is implemented.                                                      |
| 0b0010 | As 0b0001 , and adds support for threshold value linking between a pair of counters. |

All other values are reserved.

If FEAT\_PMUv3\_TH is not implemented, the only permitted value is 0b0000 .

FEAT\_PMUv3\_EDGE implements the functionality identified by the value 0b0001 .

FEAT\_PMUv3\_TH2 implements the functionality identified by the value 0b0010 .

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
| 0b0111      | 64 bytes.                         |
| 0b1000      | 128 bytes.                        |
| 0b1001      | 256 bytes.                        |
| 0b1010      | 512 bytes.                        |
| 0b1011      | 1024 bytes.                       |
| 0b1100      | 2048 bytes.                       |

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

Operation width. The largest value by which the STALL\_SLOT event might increment in a single cycle. If the STALL\_SLOT event is not implemented, this field might read as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

| 31   | 29 28 27   | 24 23   | 20 19   | 16 15     |           | 8 7   |
|------|------------|---------|---------|-----------|-----------|-------|
| RES0 | SME        | EDGE    | THWIDTH | BUS_WIDTH | BUS_SLOTS | SLOTS |

## Bits [31:29]

Reserved, RES0.

## SME, bit [28]

PMUv3 for SME. Adds support for the Streaming SVE mode filter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SME   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | Streaming SVE mode filter not implemented.      |
| 0b1   | Adds support for the Streaming SVE mode filter. |

All other values are reserved.

FEAT\_PMUv3\_SME implements the functionality identified by the value 1.

Access to this field is RO.

## EDGE, bits [27:24]

PMUevent edge detection. With PMMIR\_EL1.THWIDTH, indicates implementation of event counter thresholding features.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EDGE   | Meaning                                                                              |
|--------|--------------------------------------------------------------------------------------|
| 0b0000 | FEAT_PMUv3_EDGE is not implemented.                                                  |
| 0b0001 | FEAT_PMUv3_EDGE is implemented.                                                      |
| 0b0010 | As 0b0001 , and adds support for threshold value linking between a pair of counters. |

All other values are reserved.

If FEAT\_PMUv3\_TH is not implemented, the only permitted value is 0b0000 .

FEAT\_PMUv3\_EDGE implements the functionality identified by the value 0b0001 .

FEAT\_PMUv3\_TH2 implements the functionality identified by the value 0b0010 .

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
| 0b0111      | 64 bytes.                         |
| 0b1000      | 128 bytes.                        |
| 0b1001      | 256 bytes.                        |
| 0b1010      | 512 bytes.                        |
| 0b1011      | 1024 bytes.                       |
| 0b1100      | 2048 bytes.                       |

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

Operation width. The largest value by which the STALL\_SLOT event might increment in a single cycle. If the STALL\_SLOT event is not implemented, this field might read as zero.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMMIR

If the Core power domain is off or in a low-power state, access to this register returns an Error.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3p4 is implemented and (FEAT\_PMUv3\_EXT64 is implemented or FEAT\_PMUv3p9 is implemented)

[63:0] Accessible at offset 0xE40 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3p4 is implemented, FEAT\_PMUv3\_EXT32 is implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xE40 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.43 PMOVSCLR\_EL0, Performance Monitors Overflow Flag Status Clear register

The PMOVSCLR\_EL0 characteristics are:

## Purpose

Allows software to clear the unsigned overflow flags for the following counters to 0:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows the current unsigned overflow flag values.

## Configuration

PMOVSCLR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMOVSCLR\_EL0 are RES0.

## Attributes

PMOVSCLR\_EL0 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Unsigned overflow flag for PMICNTR\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMICNTR\_EL0 to 0. On reads, returns the unsigned overflow flag for PMICNTR\_EL0.

| F0   | Meaning                         |
|------|---------------------------------|
| 0b0  | PMICNTR_EL0 has not overflowed. |
| 0b1  | PMICNTR_EL0 has overflowed.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Unsigned overflow flag for PMCCNTR\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMCCNTR\_EL0 to 0. On reads, returns the unsigned overflow flag for PMCCNTR\_EL0 overflow status.

| C   | Meaning                         |
|-----|---------------------------------|
| 0b0 | PMCCNTR_EL0 has not overflowed. |
| 0b1 | PMCCNTR_EL0 has overflowed.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 to 0. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 overflow status.

| P<m>   | Meaning                             |
|--------|-------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

When FEAT\_PMUv3\_EXTPMN is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP are applicable only for event counters in the second and first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Otherwise:

<!-- image -->

| 31   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|-----------------------------------------------------------------------------------|

## C, bit [31]

Unsigned overflow flag for PMCCNTR\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMCCNTR\_EL0 to 0. On reads, returns the unsigned overflow flag for PMCCNTR\_EL0 overflow status.

| C   | Meaning                         |
|-----|---------------------------------|
| 0b0 | PMCCNTR_EL0 has not overflowed. |
| 0b1 | PMCCNTR_EL0 has overflowed.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 clear. On writes, allows software to clear the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 to 0. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 overflow status.

| P<m>   | Meaning                             |
|--------|-------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

When FEAT\_PMUv3\_EXTPMN is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP are applicable only for event counters in the second and first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1C.

## Accessing PMOVSCLR\_EL0

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_ICNTR is implemented, or FEAT\_PMUv3p9 is implemented

[63:0] Accessible at offset 0xC80 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXT32 is implemented and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3\_ICNTR is not implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xC80 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.44 PMOVS, Performance Monitors Overflow Flag Status register

The PMOVS characteristics are:

## Purpose

The unsigned overflow flags for the Cycle Count Register, PMCCNTR\_EL0, and each of the implemented event counters PMEVCNTR&lt;n&gt;.

## Configuration

This register is present only when FEAT\_PMUv3\_EXT64 is implemented. Otherwise, direct accesses to PMOVS are RES0.

## Attributes

PMOVSis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

PMICNTR\_EL0 unsigned overflow flag.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## C, bit [31]

Cycle counter unsigned overflow flag.

| F0   | Meaning                         |
|------|---------------------------------|
| 0b0  | PMICNTR_EL0 has not overflowed. |
| 0b1  | PMICNTR_EL0 has overflowed.     |

| C   | Meaning                                                                    |
|-----|----------------------------------------------------------------------------|
| 0b0 | The cycle counter has not overflowed since this bit was last cleared to 0. |
| 0b1 | The cycle counter has overflowed since this bit was last cleared to 0.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Event counter unsigned overflow bit for PMEVCNTR&lt;m&gt;\_EL0.

| P<m>   | Meaning                                                                  |
|--------|--------------------------------------------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed since this bit was last cleared to 0. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed since this bit was last cleared to 0.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

When FEAT\_PMUv3\_EXTPMN is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP are applicable only for event counters in the second and first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- Otherwise, access to this field is RW.

## Accessing PMOVS

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0xC90 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## I5.3.45 PMOVSSET\_EL0, Performance Monitors Overflow Flag Status Set Register

The PMOVSSET\_EL0 characteristics are:

## Purpose

Allows software to set the unsigned overflow flags for the following counters to 1:

- The cycle counter PMCCNTR\_EL0.
- The event counters PMEVCNTR&lt;n&gt;\_EL0.
- When FEAT\_PMUv3\_ICNTR is implemented, the instruction counter PMICNTR\_EL0.

Reading from this register shows the current unsigned overflow flag values.

## Configuration

PMOVSSET\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMOVSSET\_EL0 are RES0.

## Attributes

PMOVSSET\_EL0 is a:

- 64-bit register when FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3p9 is implemented, or FEAT\_PMUv3\_ICNTR is implemented:

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Unsigned overflow flag for PMICNTR\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMICNTR\_EL0 to 1. On reads, returns the unsigned overflow flag for PMICNTR\_EL0.

| F0   | Meaning                         |
|------|---------------------------------|
| 0b0  | PMICNTR_EL0 has not overflowed. |
| 0b1  | PMICNTR_EL0 has overflowed.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Unsigned overflow flag for PMCCNTR\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMCCNTR\_EL0 to 1. On reads, returns the unsigned overflow flag for PMCCNTR\_EL0 overflow status.

| C   | Meaning                         |
|-----|---------------------------------|
| 0b0 | PMCCNTR_EL0 has not overflowed. |
| 0b1 | PMCCNTR_EL0 has overflowed.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 to 1. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 overflow status.

| P<m>   | Meaning                             |
|--------|-------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

When FEAT\_PMUv3\_EXTPMN is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP are applicable only for event counters in the second and first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Otherwise:

<!-- image -->

| 31   | 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|-----------------------------------------------------------------------------------|

## C, bit [31]

Unsigned overflow flag for PMCCNTR\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMCCNTR\_EL0 to 1. On reads, returns the unsigned overflow flag for PMCCNTR\_EL0 overflow status.

| C   | Meaning                         |
|-----|---------------------------------|
| 0b0 | PMCCNTR_EL0 has not overflowed. |
| 0b1 | PMCCNTR_EL0 has overflowed.     |

PMCR\_EL0.LC controls whether an overflow is detected from unsigned overflow of PMCCNTR\_EL0[31:0] or unsigned overflow of PMCCNTR\_EL0[63:0].

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 set. On writes, allows software to set the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 to 1. On reads, returns the unsigned overflow flag for PMEVCNTR&lt;m&gt;\_EL0 overflow status.

| P<m>   | Meaning                             |
|--------|-------------------------------------|
| 0b0    | PMEVCNTR<m>_EL0 has not overflowed. |
| 0b1    | PMEVCNTR<m>_EL0 has overflowed.     |

If FEAT\_PMUv3p5 is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP control whether an overflow is detected from unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[31:0] or unsigned overflow of PMEVCNTR&lt;m&gt;\_EL0[63:0].

When FEAT\_PMUv3\_EXTPMN is implemented, MDCR\_EL2.HLP and PMCR\_EL0.LP are applicable only for event counters in the second and first range. For more information about event counter ranges, see MDCR\_EL2.HPMN.

The reset behavior of this field is:

- On a Cold reset:
- When FEAT\_PMUv3\_EXTPMN is implemented, this field resets to an architecturally UNKNOWN value.
- On a Warm reset:
- When FEAT\_PMUv3\_EXTPMN is not implemented, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RO.
- Otherwise, access to this field is W1S.

## Accessing PMOVSSET\_EL0

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented, or FEAT\_PMUv3\_ICNTR is implemented, or FEAT\_PMUv3p9 is implemented

[63:0] Accessible at offset 0xCC0 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When FEAT\_PMUv3\_EXT32 is implemented and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## When FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3\_ICNTR is not implemented, and FEAT\_PMUv3p9 is not implemented

[31:0] Accessible at offset 0xCC0 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## I5.3.46 PMPCSCTL, PC Sample-based Profiling Control Register

The PMPCSCTL characteristics are:

## Purpose

Controls the PC Sample-based Profiling feature.

## Configuration

PMPCSCTL is in the Core power domain.

This register is present only when FEAT\_PCSRv8p9 is implemented and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMPCSCTL are RES0.

## Attributes

PMPCSCTL is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:5]

Reserved, RES0.

## SS, bit [4]

## When FEAT\_PMUv3\_SS is implemented:

Sample on Snapshot.

Controls whether the following registers are sampled on a PMU snapshot Capture event:

- If FEAT\_PMUv3\_EXT32 is implemented: PMCID1SR, PMCID2SR, PMPCSR, and PMVIDSR.
- If FEAT\_PMUv3\_EXT64 is implemented: PMCCIDSR, PMPCSR, and PMVCIDSR.

| SS   | Meaning             |
|------|---------------------|
| 0b0  | Sample on Read.     |
| 0b1  | Sample on Snapshot. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bits [3:2]

Reserved, RES0.

## IMP, bit [1]

Profiling enable implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IMP   | Meaning                                       |
|-------|-----------------------------------------------|
| 0b0   | PMPCSCTL.EN reads-as-zero and ignores writes. |
| 0b1   | PMPCSCTL.EN is a read-write control bit.      |

Access to this field is RO.

## EN, bit [0]

## When PMU.PMPCSCTL.IMP == '1':

PC Sample-based Profiling Enable.

| EN   | Meaning                                 |
|------|-----------------------------------------|
| 0b0  | PC Sample-based Profiling is suspended. |
| 0b1  | PC Sample-based Profiling is active.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Otherwise:

Reserved, RAZ/WI.

## Accessing PMPCSCTL

Accesses to this register use the following encodings:

## When FEAT\_PCSRv8p9 is implemented

Accessible at offset 0xE50 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## I5.3.47 PMCCR, PMU Configuration Control Register

The PMCCR characteristics are:

## Purpose

Contains PMU configuration controls.

## Configuration

This register is present only when FEAT\_PMUv3\_EXTPMN is implemented. Otherwise, direct accesses to PMCCRare RES0.

## Attributes

PMCCRis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:9]

Reserved, RES0.

## OSLO, bit [8]

## When FEAT\_PMUv3\_EXTPMN is implemented:

OS Lock Override.

| OSLO   | Meaning                                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No external access to any Performance Monitor register is affected by this control.                                                                             |
| 0b1    | For the purpose of determining the access permissions of Performance Monitor registers, an external access that is a Most secure access ignores OSLSR_EL1.OSLK. |

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## EPME, bit [7]

## When FEAT\_PMUv3\_EXTPMN is implemented:

External Enable.

| EPME   | Meaning                                          |
|--------|--------------------------------------------------|
| 0b0    | Affected counters are disabled and do not count. |
| 0b1    | Affected counters are enabled by PMCNTENSET_EL0. |

The counters affected by this field are the event counters in the third range.

Other event counters, PMCCNTR\_EL0, and, if FEAT\_PMUv3\_ICNTR is implemented, PMICNTR\_EL0 are not affected by this field.

If the Effective value of PMCCR.EPMN is equal to NUM\_PMU\_COUNTERS, then this field has no effect.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## Otherwise:

Reserved, RES0.

## Bits [6:5]

Reserved, RES0.

## EPMN, bits [4:0]

## When FEAT\_PMUv3\_EXTPMN is implemented:

Defines the number of event counters PMEVCNTR&lt;n&gt;\_EL0 and, if FEAT\_PMUv3\_SS is implemented, snapshot registers PMEVCNTSVR&lt;n&gt;\_EL1, that are reserved for external use.

PMCCR.EPMN divides the event counters into event counters that are accessible from self-hosted software, and which might be further divided into first and second ranges by MDCR\_EL2.HPMN, and a third range that is inaccessible from self-hosted software.

If PMCCR.EPMN is not 0 and is less than the number of PMU event counters implemented by the PE, NUM\_PMU\_COUNTERS , then event counters [0..(PMCCR.EPMN-1)] are in the first and second ranges, and event counters [PMCCR.EPMN..( NUM\_PMU\_COUNTERS -1)] are in the third range.

If PMCCR.EPMN is equal to NUM\_PMU\_COUNTERS , or FEAT\_PMUv3\_EXTPMN is not implemented, then all of the following apply:

- All counters are in the first and second ranges.
- No counters are in the third range.

If PMCCR.EPMN is zero, then all of the following apply:

- No counters are in the first and second ranges.
- All counters are in the third range.

All the following apply for an event counter PMEVCNTR&lt;n&gt;\_EL0 in the third range:

- The counter is accessible to a Most secure access of PMEVCNTR&lt;n&gt;\_EL0. That is, an external access which is one of the following:
- Root access, when FEAT\_RME is implemented.
- Secure access, when FEAT\_RME is not implemented and Secure state is implemented.
- Non-secure access, otherwise.
- The counter is not accessible to other external accesses, or as the System register PMEVCNTR&lt;n&gt;\_EL0 at any Exception level.
- The counter overflow flag PMOVSSET\_EL0[n] is set on unsigned overflow of PMEVCNTR&lt;n&gt;\_EL0[63:0].
- PMCCR.EPME and PMCNTENSET\_EL0 enable operation of the event counter.

If FEAT\_PMUv3\_SS is implemented, then all of the following apply for an event counter snapshot register PMEVCNTSVR&lt;n&gt;\_EL1 in the third range:

- The event counter snapshot register is accessible to a Most secure access of PMEVCNTSVR&lt;n&gt;\_EL1.
- The event counter snapshot register is not accessible to other external accesses, or as the System register PMEVCNTSVR&lt;n&gt;\_EL1 at any Exception level.

For information about counters in the first and second ranges, see the description of MDCR\_EL2.HPMN.

Values greater than NUM\_PMU\_COUNTERS are reserved.

If this field is set to a reserved value, then the following CONSTRAINED UNPREDICTABLE behaviors apply:

- The value returned by an external read of PMCCR.EPMN is UNKNOWN and less than or equal to 31.
- For the purpose of indirect reads of PMCCR.EPMN as a result of the following reads, the Effective value of PMCCR.EPMN is UNKNOWN and less than or equal to 31:
- Direct reads of PMCR\_EL0.N or PMCR.N.
- Direct reads of MDCR\_EL2.HPMN.
- External reads of PMCFGR.N.
- If FEAT\_PMUv3\_ICNTR is implemented, external reads of PMCGCR0.CG0NC.
- For all other purposes the Effective value of PMCCR.EPMN is UNKNOWN and less than or equal to NUM\_PMU\_COUNTERS .

If FEAT\_PMUv3\_EXTPMN is not implemented, then the Effective value of PMCCR.EPMN is NUM\_PMU\_COUNTERS .

The reset behavior of this field is:

- On a Cold reset, this field resets to the expression NUM\_PMU\_COUNTERS .

## Otherwise:

Reserved, RES0.

## Accessing PMCCR

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXTPMN is implemented

Accessible at offset 0xE58 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When !IsMostSecureAccess(addrdesc), accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RW.

## I5.3.48 PMPCSR, Program Counter Sample Register

The PMPCSR characteristics are:

## Purpose

Holds a sampled instruction address value.

## Configuration

PMPCSR is in the Core power domain.

This register is a PC Sample-based Profiling Extension register.

If FEAT\_PMUv3\_EXT32 is implemented, support for 64-bit atomic reads is IMPLEMENTATION DEFINED. If 64-bit atomic reads are implemented, a 64-bit read of PMPCSR has the same side-effect as a 32-bit read of PMCSR[31:0] followed by a 32-bit read of PMPCSR[63:32], returning the combined value. For example, if the PE is in Debug state, then a 64-bit atomic read returns bits[31:0] == 0xFFFFFFFF and bits[63:32] UNKNOWN.

This register is present only when FEAT\_PMUv3\_EXT is implemented and FEAT\_PCSRv8p2 is implemented. Otherwise, direct accesses to PMPCSR are RES0.

## Attributes

PMPCSR is a 64-bit register.

## Field descriptions

<!-- image -->

## NS, bit [63]

## When FEAT\_RME is implemented:

Together with the NSE field, indicates the Security state that is associated with the most recent PMPCSR sample or, when it is read as a single atomic 64-bit read, the current PMPCSR sample.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

## Otherwise:

Non-secure state sample. Indicates the Security state that is associated with the most recent PMPCSR sample or, when it is read as a single atomic 64-bit read, the current PMPCSR sample.

If EL3 is not implemented, this bit indicates the Effective value of SCR.NS.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## EL, bits [62:61]

Exception level status sample. Indicates the Exception level that is associated with the most recent PMPCSR sample or, when it is read as a single atomic 64-bit read, the current PMPCSR sample.

| EL   | Meaning             |
|------|---------------------|
| 0b00 | Sample is from EL0. |
| 0b01 | Sample is from EL1. |
| 0b10 | Sample is from EL2. |
| 0b11 | Sample is from EL3. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bit [60]

Reserved, RES0.

## NSE, bit [59]

## When FEAT\_RME is implemented:

Together with the NS field, indicates the Security state that is associated with the most recent PMPCSR sample or, when it is read as a single atomic 64-bit read, the current PMPCSR sample.

For a description of the values derived by evaluating NS and NSE together, see PMPCSR.NS.

## Otherwise:

Reserved, RES0.

## Bits [58:56]

Reserved, RES0.

## PCSample[55:32], bits [55:32]

Bits[55:32] of the sampled instruction address value. The translation regime that PMPCSR samples can be determined from PMPCSR.{NS,EL}.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

| NS   | Meaning                          |
|------|----------------------------------|
| 0b0  | Sample is from Secure state.     |
| 0b1  | Sample is from Non-secure state. |

## PCSample[31:0], bits [31:0]

Bits[31:0] of the sampled instruction address value.

PMPCSR[31:0] reads as 0xFFFFFFFF when any of the following are true:

- The PE is in Debug state.
- PC Sample-based profiling is prohibited.

If a branch instruction has retired since the PE left reset state, then the first read of PMPCSR[31:0] is permitted but not required to return 0xFFFFFFFF .

PMPCSR[31:0] reads as an UNKNOWN value when any of the following are true:

- The PE is in reset state.
- No branch instruction has retired since the PE left reset state, Debug state, or a state where PC Sample-based Profiling is prohibited.
- No branch instruction has retired since the last read of PMPCSR[31:0].

For the cases where a read of PMPCSR[31:0] returns 0xFFFFFFFF or an UNKNOWN value, the read has the side-effect of setting PMPCSR[63:32], PMCID1SR, PMCID2SR, and PMVIDSR to UNKNOWN values.

Otherwise, a read of PMPCSR[31:0] returns bits [31:0] of the sampled instruction address value and has the side-effect of indirectly writing to PMPCSR[63:32], PMCID1SR, PMCID2SR, and PMVIDSR. The translation regime that PMPCSR samples can be determined from PMPCSR.{NS,EL}.

For a read of PMPCSR[31:0] from the memory-mapped interface, if PMLSR.SLK == 1, meaning the OPTIONAL Software Lock is locked, then the side-effect of the access does not occur and PMPCSR[63:32], PMCID1SR, PMCID2SR, and PMVIDSR are unchanged.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMPCSR

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

Note

A 32-bit access to PMPCSR[63:32] does not update the PC sample registers. Only a 64-bit access to PMPCSR[63:0] or a 32-bit access to PMPCSR[31:0] updates the PC sample registers. This includes the value a subsequent 32-bit read of PMPCSR[63:32] will return.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x200 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

[31:0] Accessible at offset 0x200 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

[63:32] Accessible at offset 0x204 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT64 is implemented

[63:0] Accessible at offset 0x220 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

[31:0] Accessible at offset 0x220 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

[63:32] Accessible at offset 0x224 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.49 PMPIDR0, Performance Monitors Peripheral Identification Register 0

The PMPIDR0 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMPIDR0. Otherwise, direct accesses to PMPIDR0 are RES0.

## Attributes

PMPIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PART\_0, bits [7:0]

Part number, least significant byte.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMPIDR0

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFE0 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.50 PMPIDR1, Performance Monitors Peripheral Identification Register 1

The PMPIDR1 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMPIDR1. Otherwise, direct accesses to PMPIDR1 are RES0.

## Attributes

PMPIDR1 is a 32-bit register.

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

## Accessing PMPIDR1

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFE4 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.51 PMPIDR2, Performance Monitors Peripheral Identification Register 2

The PMPIDR2 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMPIDR2. Otherwise, direct accesses to PMPIDR2 are RES0.

## Attributes

PMPIDR2 is a 32-bit register.

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

## Accessing PMPIDR2

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFE8 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.52 PMPIDR3, Performance Monitors Peripheral Identification Register 3

The PMPIDR3 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMPIDR3. Otherwise, direct accesses to PMPIDR3 are RES0.

## Attributes

PMPIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    | 4 3   |
|------|--------|-------|
| RES0 | REVAND | CMOD  |

## Bits [31:8]

Reserved, RES0.

## REVAND, bits [7:4]

Part minor revision. Parts using PMPIDR2.REVISION as an extension to the Part number must use this field as a major revision number.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CMOD,bits [3:0]

Customer modified. Indicates someone other than the Designer has modified the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMPIDR3

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFEC from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.53 PMPIDR4, Performance Monitors Peripheral Identification Register 4

The PMPIDR4 characteristics are:

## Purpose

Provides information to identify a Performance Monitor component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

If FEAT\_DoPD is implemented, this register is in the Core power domain. If FEAT\_DoPD is not implemented, this register is in the Debug power domain.

This register is required for CoreSight compliance.

This register is present only when FEAT\_PMUv3\_EXT is implemented and an implementation implements PMPIDR4. Otherwise, direct accesses to PMPIDR4 are RES0.

## Attributes

PMPIDR4 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SIZE, bits [7:4]

Size of the component. Log2 of the number of 4KB pages from the start of the component to the end of the component ID registers.

Reads as 0b0000

Access to this field is RO.

## DES\_2, bits [3:0]

Designer, JEP106 continuation code, least significant nibble. For Arm Limited, this field is 0b0100 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing PMPIDR4

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented

Accessible at offset 0xFD0 from PMU

- When FEAT\_DoPD is implemented and !IsCorePowered(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.54 PMSSCR\_EL1, Performance Monitors Snapshot Status and Capture Register

The PMSSCR\_EL1 characteristics are:

## Purpose

Holds status information about the captured counters and provides a mechanism for software to initiate a sample.

## Configuration

This register is present only when FEAT\_PMUv3\_SS is implemented and FEAT\_PMUv3\_EXT is implemented. Otherwise, direct accesses to PMSSCR\_EL1 are RES0.

## Attributes

PMSSCR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 33 32   |
|------|---------|
| RES0 | NC      |
| 31   | 1 0     |
| RES0 | SS      |

## Bits [63:33]

Reserved, RES0.

## NC, bit [32]

No Capture. Indicates whether the PMU counters have been captured.

| NC   | Meaning                   |
|------|---------------------------|
| 0b0  | PMUcounters captured.     |
| 0b1  | PMUcounters not captured. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Bits [31:1]

Reserved, RES0.

## SS, bit [0]

Snapshot Capture and Status.

| SS   | Meaning                                                                              |
|------|--------------------------------------------------------------------------------------|
| 0b0  | On a read, the Capture event has completed.                                          |
| 0b1  | On a read, the Capture event has not completed. On a write, request a Capture event. |

Awrite of 0 to this field is ignored.

It is CONSTRAINED UNPREDICTABLE whether a Capture event has completed if this field is modified when the Capture event is ongoing.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RO.
- When PMU capture events are disabled, access to this field is RO.
- Otherwise, access to this field is RW.

## Accessing PMSSCR\_EL1

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_SS is implemented

Accessible at offset 0xE30 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMSSAccess(addrdesc), accesses to this register generate an error response.
- Otherwise, accesses to this register are RW.

## I5.3.55 PMSWINC\_EL0, Performance Monitors Software Increment Register

The PMSWINC\_EL0 characteristics are:

## Purpose

Increments a counter that is configured to count the Software increment event, event 0x00 . For more information, see 'SW\_INCR'.

## Configuration

PMSWINC\_EL0 is in the Core power domain.

If this register is implemented, use of it is deprecated.

If 1 is written to bit [n] from the external debug interface, it is CONSTRAINED UNPREDICTABLE whether or not a SW\_INCR event is created for counter n. This is consistent with not implementing the register in the external debug interface.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PMUv3p9 is not implemented, and an implementation implements PMSWINC\_EL0.

## Attributes

PMSWINC\_EL0 is a 32-bit register.

## Field descriptions

<!-- image -->

| 30 29 28 27         | 26 25 24   | 23   | 22   | 21   | 20      | 19      | 18   | 17 16   | 15          | 14 13   | 12   | 11 10   | 9   | 8   | 7     | 6   | 5   | 4 3   | 2 1   | 0   |
|---------------------|------------|------|------|------|---------|---------|------|---------|-------------|---------|------|---------|-----|-----|-------|-----|-----|-------|-------|-----|
| P30 P29 P28 P27 P26 | P25 P24    | P23  |      | P22  | P21 P20 | P19 P18 | P17  | P16     | P15 P14 P13 | P12     | P11  | P10     | P9  | P8  | P7 P6 | P5  | P4  | P3 P2 | P1    | P0  |

<!-- image -->

## Bit [31]

Reserved, RES0.

P&lt;m&gt; , bits [m], for m = 30 to 0

Event counter software increment bit for PMEVCNTR&lt;m&gt;\_EL0.

| P<m>   | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | No action. The write to this bit is ignored.                                              |
| 0b1    | It is CONSTRAINED UNPREDICTABLE whether a SW_INCR event is generated for event counter m. |

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- When SoftwareLockStatus(), access to this field is RAZ/WI.
- Otherwise, access to this field is WO/RAZ.

## Accessing PMSWINC\_EL0

If FEAT\_PMUv3p9 or FEAT\_PMUv3\_EXT64 are implemented, this location is used for accesses to PMZR\_EL0.

Note

SoftwareLockStatus() depends on the type of access attempted and AllowExternalPMUAccess() has a new definition from Armv8.4. Refer to the Pseudocode definitions for more information.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PMUv3p9 is not implemented

Accessible at offset 0xCA0 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

## I5.3.56 PMVIDSR, VMID Sample Register

The PMVIDSR characteristics are:

## Purpose

Contains the sampled VMID value that is captured on reading PMPCSR[31:0].

## Configuration

PMVIDSR is in the Core power domain.

This register is a PC Sample-based Profiling Extension register.

This register is present only when FEAT\_PMUv3\_EXT32 is implemented, FEAT\_PCSRv8p2 is implemented, and EL2 is implemented.

## Attributes

PMVIDSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## VMID[15:8], bits [15:8]

## When FEAT\_VMID16 is implemented:

Extension to VMID[7:0]. For more information, see VMID[7:0].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VMID, bits [7:0]

VMIDsample. The VMID associated with the most recent PMPCSR sample. When the most recent PMPCSR sample was generated:

- This field is set to an UNKNOWN value if any of the following apply:
- EL2 is disabled in the current Security state.
- The PE is executing at EL2.
- The PE is executing at EL0, and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.
- Otherwise:
- If EL2 is using AArch64 and either FEAT\_VMID16 is not implemented or VTCR\_EL2.VS is 1, this field is set to VTTBR\_EL2.VMID.
- If EL2 is using AArch64, FEAT\_VMID16 is implemented, and VTCR\_EL2.VS is 0, PMVIDSR.VMID[7:0] is set to VTTBR\_EL2.VMID[7:0] and PMVIDSR.VMID[15:8] is RES0.
- If EL2 is using AArch32, this field is set to VTTBR.VMID.

Because the value written to PMVIDSR is an indirect read of the VMID value, it is CONSTRAINED UNPREDICTABLE whether PMVIDSR is set to the original or new value if PMPCSR samples:

- An instruction that writes to the VMID value.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMVIDSR

If FEAT\_PMUv3\_EXT64 is implemented, then the same content is present in the same location, and can be accessed using PMVCIDSR[63:32].

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT32 is implemented and FEAT\_PCSRv8p2 is implemented

Accessible at offset 0x20C from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.57 PMVCIDSR, CONTEXTIDR\_EL1 and VMID Sample Register

The PMVCIDSR characteristics are:

## Purpose

Contains the sampled CONTEXTIDR\_EL1 and VMID values that are captured on reading PMPCSR.

## Configuration

This register is a PC Sample-based Profiling Extension register.

This register is present only when FEAT\_PMUv3\_EXT64 is implemented and FEAT\_PCSRv8p2 is implemented.

## Attributes

PMVCIDSR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## VMID[15:8], bits [47:40]

## When FEAT\_VMID16 is implemented:

Extension to VMID[7:0]. For more information, see VMID[7:0].

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## VMID, bits [39:32]

VMIDsample. The VMID associated with the most recent PMPCSR sample. When the most recent PMPCSR sample was generated:

- This field is set to an UNKNOWN value if any of the following apply:
- EL2 is disabled in the current Security state.
- The PE is executing at EL2.
- The PE is executing at EL0, and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.
- Otherwise:
- If EL2 is using AArch64 and either FEAT\_VMID16 is not implemented or VTCR\_EL2.VS is 1, this field is set to VTTBR\_EL2.VMID.
- If EL2 is using AArch64, FEAT\_VMID16 is implemented, and VTCR\_EL2.VS is 0, PMVIDSR.VMID[7:0] is set to VTTBR\_EL2.VMID[7:0] and PMVIDSR.VMID[15:8] is RES0.
- If EL2 is using AArch32, this field is set to VTTBR.VMID.

Because the value written to PMVIDSR is an indirect read of the VMID value, it is CONSTRAINED UNPREDICTABLE whether PMVIDSR is set to the original or new value if PMPCSR samples:

- An instruction that writes to the VMID value.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## CONTEXTIDR\_EL1, bits [31:0]

Context ID. The value of CONTEXTIDR that is associated with the most recent PMPCSR sample. When the most recent PMPCSR sample is generated:

- If EL1 is using AArch64, then the Context ID is sampled from CONTEXTIDR\_EL1.
- If EL1 is using AArch32, then the Context ID is sampled from CONTEXTIDR.
- If EL3 is implemented and is using AArch32, then CONTEXTIDR is a banked register and this register samples the current banked copy of CONTEXTIDR for the Security state that is associated with the most recent PMPCSR sample.

Because the value written to this register is an indirect read of CONTEXTIDR, it is CONSTRAINED UNPREDICTABLE whether this register is set to the original or new value if PMPCSR samples:

- An instruction that writes to CONTEXTIDR.
- The next Context synchronization event.
- Any instruction executed between these two instructions.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing PMVCIDSR

If FEAT\_PCSRv8p2 and FEAT\_PMUv3\_EXT32 are implemented, then the same content is present in the same locations, and can be accessed using PMVIDSR[31:0] and PMCID1SR[31:0].

IMPLEMENTATION DEFINED extensions to external debug might make the value of this register UNKNOWN, see 'Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN'.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT64 is implemented

Accessible at offset 0x208 from PMU

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- Otherwise, accesses to this register are RO.

## I5.3.58 PMZR\_EL0, Performance Monitors Zero with Mask

The PMZR\_EL0 characteristics are:

## Purpose

Zero the set of counters specified by the mask written to PMZR\_EL0.

## Configuration

PMZR\_EL0 is in the Core power domain.

This register is present only when FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p9 is implemented.

## Attributes

PMZR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:33]

Reserved, RES0.

## F0, bit [32]

## When FEAT\_PMUv3\_ICNTR is implemented:

Zero PMICNTR\_EL0.

| F0   | Meaning                  |
|------|--------------------------|
| 0b0  | Write is ignored.        |
| 0b1  | Set PMICNTR_EL0 to zero. |

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RAZ/WI.
- Otherwise, access to this field is WO/RAZ.

## Otherwise:

Reserved, RES0.

## C, bit [31]

Zero PMCCNTR\_EL0.

| C   | Meaning                  |
|-----|--------------------------|
| 0b0 | Write is ignored.        |
| 0b1 | Set PMCCNTR_EL0 to zero. |

Accessing this field has the following behavior:

- When SoftwareLockStatus(), access to this field is RAZ/WI.
- Otherwise, access to this field is WO/RAZ.

## P&lt;m&gt; , bits [m], for m = 30 to 0

Zero PMEVCNTR&lt;m&gt;\_EL0.

Accessing this field has the following behavior:

- When m &gt;= NUM\_PMU\_COUNTERS, access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- FEAT\_PMUv3\_EXTPMN is implemented
- m&gt;=UInt(EffectiveEPMN())
- !IsMostSecureAccess(addrdesc)
- When SoftwareLockStatus(), access to this field is RAZ/WI.
- Otherwise, access to this field is WO/RAZ.

## Accessing PMZR\_EL0

When FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p9 is not implemented, then this location might be used for PMSWINC\_EL0. If PMSWINC\_EL0 is not implemented, then accesses to this location are RES0.

Accesses to this register use the following encodings:

## When FEAT\_PMUv3\_EXT is implemented and FEAT\_PMUv3p9 is implemented

Accessible at offset 0xCA0 from PMU

- When DoubleLockStatus(), or !IsCorePowered(), or !AllowExternalPMUAccess(addrdesc), accesses to this register generate an error response.
- When (((!IsFeatureImplemented(FEAT\_PMUv3\_EXTPMN)) || (!IsMostSecureAccess(addrdesc))) || (PMCCR.OSLO == '0')) &amp;&amp; OSLockStatus(), accesses to this register generate an error response.
- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

| P<m>   | Meaning                      |
|--------|------------------------------|
| 0b0    | Write is ignored.            |
| 0b1    | Set PMEVCNTR<m>_EL0 to zero. |