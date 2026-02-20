## H9.4 External Trace Buffer registers

## H9.4.1 TRBAUTHSTATUS, Authentication Status Register

The TRBAUTHSTATUS characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for debug.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBAUTHSTATUS is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBAUTHSTATUS are RES0.

## Attributes

TRBAUTHSTATUS is a 32-bit register.

## Field descriptions

| 31   | 28 27 26 25 24 23   | 28 27 26 25 24 23   | 28 27 26 25 24 23   | 16 15 14 13 12 11   | 16 15 14 13 12 11   | 16 15 14 13 12 11   | 8 7 6 5 4 3   | 2     | 1 0   |
|------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------|-------|-------|
| RES0 | RTNID               | RTID                | RES0                | RLNID               | RLID                | RES0                | SNID          | NSNID | NSID  |

Bits [31:28]

Reserved, RES0.

## RTNID, bits [27:26]

Root non-invasive debug.

## RTID, bits [25:24]

Root invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RTID.

## Bits [23:16]

Reserved, RES0.

## RLNID, bits [15:14]

Realm non-invasive debug.

| RTNID   | Meaning          |
|---------|------------------|
| 0b00    | Not implemented. |

## RLID, bits [13:12]

Realm invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.RLID.

## Bits [11:8]

Reserved, RES0.

## SNID, bits [7:6]

Secure non-invasive debug.

## SID, bits [5:4]

Secure invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.SID.

## NSNID, bits [3:2]

Non-secure non-invasive debug.

## NSID, bits [1:0]

Non-secure invasive debug.

This field has the same value as DBGAUTHSTATUS\_EL1.NSID.

## Accessing TRBAUTHSTATUS

TRBAUTHSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| TRBE        | 0xFB8    | TRBAUTHSTATUS |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| RLNID   | Meaning          |
|---------|------------------|
| 0b00    | Not implemented. |

| SNID   | Meaning          |
|--------|------------------|
| 0b00   | Not implemented. |

| NSNID   | Meaning          |
|---------|------------------|
| 0b00    | Not implemented. |

## H9.4.2 TRBBASER\_EL1, Trace Buffer Base Address Register

The TRBBASER\_EL1 characteristics are:

## Purpose

Defines the base address for the trace buffer.

## Configuration

TRBBASER\_EL1 is in the Core power domain

External register TRBBASER\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBBASER\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBBASER\_EL1 are RES0.

## Attributes

TRBBASER\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## BASE, bits [63:12]

Trace Buffer Base pointer address. (TRBBASER\_EL1.BASE « 12) is the address of the first byte in the trace buffer. Bits [11:0] of the Base pointer address are always zero. If the smallest implemented translation granule is not 4KB, then TRBBASER\_EL1[N-1:12] are RES0, where N is the IMPLEMENTATION DEFINED value Log2(smallest implemented translation granule).

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Accessing TRBBASER\_EL1

The PE might ignore a write to TRBBASER\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 and the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 and the Trace Buffer Unit is using External mode.

TRBBASER\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance     |
|-------------|----------|--------------|
| TRBE        | 0x000    | TRBBASER_EL1 |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.4.3 TRBCIDR0, Component Identification Register 0

The TRBCIDR0 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBCIDR0 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBCIDR0 are RES0.

## Attributes

TRBCIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_0, bits [7:0]

Component identification preamble, segment 0.

Reads as 0x0D

Access to this field is RO.

## Accessing TRBCIDR0

TRBCIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFF0    | TRBCIDR0   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.4 TRBCIDR1, Component Identification Register 1

The TRBCIDR1 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBCIDR1 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBCIDR1 are RES0.

## Attributes

TRBCIDR1 is a 32-bit register.

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

Access to this field is RO.

## PRMBL\_1, bits [3:0]

Component identification preamble, segment 1.

Reads as

0b0000

Access to this field is RO.

## Accessing TRBCIDR1

TRBCIDR1 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFF4    | TRBCIDR1   |

## H9.4.5 TRBCIDR2, Component Identification Register 2

The TRBCIDR2 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBCIDR2 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBCIDR2 are RES0.

## Attributes

TRBCIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_2, bits [7:0]

Component identification preamble, segment 2.

Reads as

0x05

Access to this field is RO.

## Accessing TRBCIDR2

TRBCIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFF8    | TRBCIDR2   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.6 TRBCIDR3, Component Identification Register 3

The TRBCIDR3 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBCIDR3 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBCIDR3 are RES0.

## Attributes

TRBCIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_3, bits [7:0]

Component identification preamble, segment 3.

Reads as 0xB1

Access to this field is RO.

## Accessing TRBCIDR3

TRBCIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFFC    | TRBCIDR3   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.7 TRBCR, Trace Buffer Control Register

The TRBCR characteristics are:

## Purpose

Provides trace buffer controls for an external debugger.

## Configuration

TRBCR is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBCR are RES0.

## Attributes

TRBCR is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:1]

Reserved, RES0.

## ManStop, bit [0]

Flush and Stop collection. A write of 1 to this field causes a trace buffer flush, and on completion of the flush, Collection is stopped and the Trace Buffer Unit writes all trace data it has Accepted from the trace unit to memory, adding padding data if necessary.

Access to this field is WO/RAZ.

## Accessing TRBCR

TRBCR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0x038    | TRBCR      |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.4.8 TRBDEVAFF, Device Affinity Register

The TRBDEVAFF characteristics are:

## Purpose

For additional information, see the CoreSight Architecture Specification.

Reads the same value as the MPIDR\_EL1 register for the PE that this trace buffer has affinity with.

Depending on the IMPLEMENTATION DEFINED nature of the system, it might be possible that TRBDEV AFF is read before system firmware has configured the trace buffer and/or the PE or group of PEs that the trace buffer has affinity with. When this is the case, TRBDEV AFF reads as zero.

## Configuration

TRBDEVAFF is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBDEVAFF are RES0.

## Attributes

TRBDEVAFF is a 64-bit register.

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

## Accessing TRBDEVAFF

TRBDEVAFF can be accessed through the external debug interface:

| U   | Meaning                                       |
|-----|-----------------------------------------------|
| 0b0 | Processor is part of a multiprocessor system. |
| 0b1 | Processor is part of a uniprocessor system.   |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFA8    | TRBDEVAFF  |

## H9.4.9 TRBDEVARCH, Trace Buffer Device Architecture Register

The TRBDEVARCH characteristics are:

## Purpose

Provides discovery information for the component.

## Configuration

TRBDEVARCHis in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBDEVARCHare RES0.

## Attributes

TRBDEVARCHis a 32-bit register.

## Field descriptions

<!-- image -->

## ARCHITECT, bits [31:21]

Defines the architect of the component. For Trace Buffer, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as 0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the TRBDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Revision. Defines the architecture revision of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| REVISION   | Meaning                                                                                                                                                                                                                  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | First revision.                                                                                                                                                                                                          |
| 0b0001     | As 0b0000 , and adds:                                                                                                                                                                                                    |
|            | • If EL2 and FEAT_FGT are implemented, a fine-grained trap on the TSB CSYNC instruction. • If EL2 is implemented, an EL2 control to override TRBLIMITR_EL1.nVM. • The TRBE Profiling exception extension, FEAT_TRBE_EXC. |

All other values are reserved.

FEAT\_TRBE implements the functionality identified by the value 0b0000 .

FEAT\_TRBEv1p1 implements the functionality identified by the value 0b0001 .

From Armv9.6, the value 0b0000 is not permitted.

Access to this field is RO.

## ARCHVER,bits [15:12]

Architecture Version. Defines the architecture version of the component.

| ARCHVER   | Meaning                           |
|-----------|-----------------------------------|
| 0b0000    | Trace Buffer Extension version 1. |

All other values are reserved.

TRBDEVARCH.ARCHVER and TRBDEVARCH.ARCHPART are also defined as a single field, TRBDEVARCH.ARCHID, so that TRBDEVARCH.ARCHVER is TRBDEVARCH.ARCHID[15:12].

Access to this field is RO.

## ARCHPART, bits [11:0]

Architecture Part. Defines the architecture of the component.

| ARCHPART   | Meaning                         |
|------------|---------------------------------|
| 0xA18      | Armv9-A Trace Buffer Extension. |

TRBDEVARCH.ARCHVER and TRBDEVARCH.ARCHPART are also defined as a single field, TRBDEVARCH.ARCHID, so that TRBDEVARCH.ARCHPART is TRBDEVARCH.ARCHID[11:0].

Access to this field is RO.

## Accessing TRBDEVARCH

TRBDEVARCHcan be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFBC    | TRBDEVARCH |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.10 TRBDEVID, Device Configuration Register

The TRBDEVID characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBDEVID is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBDEVID are RES0.

## Attributes

TRBDEVID is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRBDEVID

TRBDEVID can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFC8    | TRBDEVID   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.11 TRBDEVID1, Device Configuration Register 1

The TRBDEVID1 characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBDEVID1 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBDEVID1 are RES0.

## Attributes

TRBDEVID1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:24]

Reserved, RES0.

## PMG\_MAX,bits [23:16]

## When FEAT\_TRBE\_MPAM is implemented:

Largest permitted PMG value. The TRBMPAM\_EL1.PMG field must implement at least enough bits to represent TRBDEVID1.PMG\_MAX.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## PARTID\_MAX, bits [15:0]

## When FEAT\_TRBE\_MPAM is implemented:

Largest permitted PARTID value. The TRBMPAM\_EL1.PARTID field must implement at least enough bits to represent TRBDEVID1.PARTID\_MAX.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## Accessing TRBDEVID1

TRBDEVID1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFC4    | TRBDEVID1  |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.12 TRBDEVID2, Device Configuration Register 2

The TRBDEVID2 characteristics are:

## Purpose

Provides discovery information for the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBDEVID2 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBDEVID2 are RES0.

## Attributes

TRBDEVID2 is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRBDEVID2

TRBDEVID2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFC0    | TRBDEVID2  |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.13 TRBDEVTYPE, Device Type Register

The TRBDEVTYPE characteristics are:

## Purpose

Provides discovery information for the component. If the part number field is not recognized, a debugger can report the information that is provided by TRBDEVTYPE about the component instead.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBDEVTYPE is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBDEVTYPE are RES0.

## Attributes

TRBDEVTYPE is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SUB, bits [7:4]

Component sub-type.

| SUB    | Meaning                                               |
|--------|-------------------------------------------------------|
| 0b0010 | WhenMAJOR== 0x1 (Trace sink), Trace buffer or router. |

This field reads as 0x2 .

Access to this field is RO.

## MAJOR, bits [3:0]

Component major type.

This field reads as 0x1 .

Access to this field is RO.

| MAJOR   | Meaning     |
|---------|-------------|
| 0b0001  | Trace sink. |

## Accessing TRBDEVTYPE

TRBDEVTYPE can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFCC    | TRBDEVTYPE |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.14 TRBIDR\_EL1, Trace Buffer ID Register

The TRBIDR\_EL1 characteristics are:

## Purpose

Describes constraints on using the Trace Buffer Unit to an external debugger.

## Configuration

TRBIDR\_EL1 is in the Core power domain

External register TRBIDR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBIDR\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBIDR\_EL1 are RES0.

## Attributes

TRBIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## MaxBuffSize, bits [47:32]

Maximum supported trace buffer size. Reserved for software use.

Reads as 0x0000

The only permitted value is 0x0000 , indicating there is no limit to the maximum buffer size.

Access to this field is RO.

## Bits [31:16]

Reserved, RES0.

## MPAM,bits [15:12]

## When FEAT\_TRBE\_EXT is implemented:

FEAT\_MPAMv0p1 or FEAT\_MPAMv1p0 extensions. Indicates Memory Partitioning and Monitoring (MPAM) support in the Trace Buffer Unit when using External mode.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MPAM   | Meaning                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Trace Buffer External Mode is not implemented or the version of MPAMsupported by this field is not implemented by the PE.    |
| 0b0001 | FEAT_MPAMv0p1 or FEAT_MPAMv1p0 is implemented by the Trace Buffer Unit, using default PARTID and PMGvalues in External mode. |
| 0b0010 | Trace Buffer MPAMextensions implemented, using FEAT_MPAMv0p1 or FEAT_MPAMv1p0.                                               |

When FEAT\_MPAMv0p1 and FEAT\_MPAMv1p0 are not implemented by the PE, the only permitted value is 0b0000 .

When at least one of FEAT\_MPAMv0p1 and FEAT\_MPAMv1p0 are implemented by the PE, the value 0b0000 is not permitted.

FEAT\_TRBE\_MPAM implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## EA, bits [11:8]

External Abort handling. Describes how the PE manages External aborts on writes made by the Trace Buffer Unit to the trace buffer.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EA     | Meaning                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not described.                                                                                                   |
| 0b0001 | The PE ignores External aborts on writes made by the Trace Buffer Unit.                                          |
| 0b0010 | An External abort on a write made by the Trace Buffer Unit generates an asynchronous SError exception at the PE. |

All other values are reserved.

From Armv9.3, the value 0b0000 is not permitted.

The behavior described by this field does not apply for External aborts on a translation table walk, translation table update, or GPT walk made by the Trace Buffer Unit that are reported as MMU faults using TRBSR\_ELx. For more information, see 'External aborts'.

Access to this field is RO.

## AddrMode, bits [7:6]

This field reads as an UNKNOWN value.

## F, bit [5]

Flag updates. Describes how address translations performed by the Trace Buffer Unit manage the Access flag and dirty state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| F   | Meaning                                                                                                                                                                                                    |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | Hardware management of the Access flag and dirty state for accesses made by the Trace Buffer Unit is always disabled for all translation stages.                                                           |
| 0b1 | Hardware management of the Access flag and dirty state for accesses made by the Trace Buffer Unit is controlled in the same way as explicit memory accesses in the trace buffer owning translation regime. |

## Note

If hardware management of the Access flag is disabled for a stage of translation, an access to a Page or Block with the Access flag bit not set in the descriptor will generate an Access Flag fault.

If hardware management of the dirty state is disabled for a stage of translation, an access to a Page or Block will ignore the Dirty Bit Modifier in the descriptor and might generate a Permission fault, depending on the values of the access permission bits in the descriptor.

From Armv9.3, the value 0 is not permitted.

Access to this field is RO.

## P, bit [4]

This field reads as an UNKNOWN value.

## Align, bits [3:0]

Defines the minimum alignment constraint for writes to TRBPTR\_EL1 and TRBTRG\_EL1.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Align   | Meaning     |
|---------|-------------|
| 0b0000  | Byte.       |
| 0b0001  | Halfword.   |
| 0b0010  | Word.       |
| 0b0011  | Doubleword. |
| 0b0100  | 16 bytes.   |
| 0b0101  | 32 bytes.   |
| 0b0110  | 64 bytes.   |
| 0b0111  | 128 bytes.  |
| 0b1000  | 256 bytes.  |
| 0b1001  | 512 bytes.  |
| 0b1010  | 1KB.        |
| 0b1011  | 2KB.        |

All other values are reserved.

Access to this field is RO.

## Accessing TRBIDR\_EL1

TRBIDR\_EL1 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0x030    | TRBIDR_EL1 |

## H9.4.15 TRBITCTRL, Integration Mode Control Register

The TRBITCTRL characteristics are:

## Purpose

Acomponent can use TRBITCTRL to dynamically switch between functional mode and integration mode. In integration mode, topology detection is enabled. After switching to integration mode and performing integration tests or topology detection, reset the system to ensure correct behavior of CoreSight and other connected system components.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBITCTRL is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBITCTRL are RES0.

## Attributes

TRBITCTRL is a 32-bit register.

## Field descriptions

| 31   | 1 0   |
|------|-------|
|      | IME   |

## Bits [31:1]

Reserved, RES0.

## IME, bit [0]

When topology detection or integration functionality is implemented:

Integration Mode Enable.

| IME   | Meaning                                                                                        |
|-------|------------------------------------------------------------------------------------------------|
| 0b0   | Component functional mode.                                                                     |
| 0b1   | Component integration mode. Support for topology detection and integration testing is enabled. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TRBITCTRL

The PE might ignore a write to TRBITCTRL if any of the following apply:

- TRBLIMITR\_EL1.E == 1, and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 1, FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

TRBITCTRL can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xF00    | TRBITCTRL  |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.4.16 TRBLAR, Lock Access Register

The TRBLAR characteristics are:

## Purpose

For components that implement the Software Lock, used to lock and unlock the Software Lock. This component does not implement the Software Lock.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBLAR is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBLAR are RES0.

## Attributes

TRBLAR is a 32-bit register.

## Field descriptions

| 31   | 0   |
|------|-----|
| WI   |     |

## Bits [31:0]

Reserved, WI.

Software Lock Key. The Software Lock is not implemented.

This field ignores writes.

## Accessing TRBLAR

TRBLAR can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFB0    | TRBLAR     |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are WO.

## H9.4.17 TRBLIMITR\_EL1, Trace Buffer Limit Address Register

The TRBLIMITR\_EL1 characteristics are:

## Purpose

Defines the top address for the trace buffer, and controls the trace buffer modes and enable.

## Configuration

TRBLIMITR\_EL1 is in the Core power domain

External register TRBLIMITR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBLIMITR\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBLIMITR\_EL1 are RES0.

## Attributes

TRBLIMITR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## LIMIT, bits [63:12]

Trace buffer Limit pointer address. (TRBLIMITR\_EL1.LIMIT « 12) is the address of the last byte in the trace buffer plus one. Bits [11:0] of the Limit pointer address are always zero. If the smallest implemented translation granule is not 4KB, then TRBLIMITR\_EL1[N-1:12] are RES0, where N is the IMPLEMENTATION DEFINED value Log2(smallest implemented translation granule).

The reset behavior of this field is:

· On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:7]

Reserved, RES0.

## XE, bit [6]

Trace Buffer Unit External mode enable. Controls whether the Trace Buffer Unit is enabled when SelfHostedTraceEnabled() == FALSE.

| XE   | Meaning                                                                 |
|------|-------------------------------------------------------------------------|
| 0b0  | Trace Buffer Unit is not enabled by this control.                       |
| 0b1  | If SelfHostedTraceEnabled() is FALSE, the Trace Buffer Unit is enabled. |

If SelfHostedTraceEnabled() == TRUE, then TRBLIMITR\_EL1.E controls whether the Trace Buffer Unit is enabled.

All output is discarded by the Trace Buffer Unit when the Trace Buffer Unit is disabled.

The reset behavior of this field is:

- On a Cold reset, this field resets to '0' .

## nVM, bit [5]

Address mode.

| nVM   | Meaning                                                                                                                                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The trace buffer pointers are virtual addresses.                                                                                                                                                                                       |
| 0b1   | The trace buffer pointers are:                                                                                                                                                                                                         |
|       | • Physical address in the owning security state if the owning translation regime has no stage 2 translation. • Intermediate physical addresses in the owning security state if the owning translation regime has stage 2 translations. |

If SelfHostedTraceEnabled() == FALSE, then the PE ignores the value of this field and the trace buffer pointers are always physical addresses.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When !SelfHostedTraceEnabled(), access to this field is RES1.
- Otherwise, access to this field is RW.

## TM, bits [4:3]

Trigger mode.

| TM   | Meaning                                                                                         |
|------|-------------------------------------------------------------------------------------------------|
| 0b00 | Stop on trigger. Flush trace, then stop collection and set TRBSR_EL1.IRQ to 1 on Trigger Event. |
| 0b01 | IRQ on trigger. Continue collection and set TRBSR_EL1.IRQ to 1 on Trigger Event.                |
| 0b11 | Ignore trigger. Continue collection and leave TRBSR_EL1.IRQ unchanged on Trigger Event.         |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## FM, bits [2:1]

Trace buffer mode.

| FM   | Meaning                                                                                                    |
|------|------------------------------------------------------------------------------------------------------------|
| 0b00 | Fill mode. Stop collection and set TRBSR_EL1.IRQ to 1 on current write pointer wrap.                       |
| 0b01 | Wrap mode. Continue collection and set TRBSR_EL1.IRQ to 1 on current write pointer wrap.                   |
| 0b11 | Circular Buffer mode. Continue collection and leave TRBSR_EL1.IRQ unchanged on current write pointer wrap. |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## E, bit [0]

Trace Buffer Unit enable. Controls whether the Trace Buffer Unit is enabled when SelfHostedTraceEnabled() == TRUE.

| E   | Meaning                                                                |
|-----|------------------------------------------------------------------------|
| 0b0 | Trace Buffer Unit is not enabled by this control.                      |
| 0b1 | If SelfHostedTraceEnabled() is TRUE, the Trace Buffer Unit is enabled. |

If FEAT\_TRBE\_EXT is implemented and SelfHostedTraceEnabled() == FALSE, then TRBLIMITR\_EL1.XE controls whether the Trace Buffer Unit is enabled.

If FEAT\_TRBE\_EXT is not implemented, then the Trace Buffer Unit is disabled when SelfHostedTraceEnabled() == FALSE.

All output is discarded by the Trace Buffer Unit when the Trace Buffer Unit is disabled.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing TRBLIMITR\_EL1

The PE might ignore a write to TRBLIMITR\_EL1, other than a write that modifies TRBLIMITR\_EL1.E or TRBLIMITR\_EL1.XE as appropriate, if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

TRBLIMITR\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| TRBE        | 0x010    | TRBLIMITR_EL1 |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.4.18 TRBLSR, Lock Status Register

The TRBLSR characteristics are:

## Purpose

Indicates the Software Lock is not implemented.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBLSR is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBLSR are RES0.

## Attributes

TRBLSR is a 32-bit register.

## Field descriptions

| 31   | 3 2 1 0   |
|------|-----------|
| RES0 | RAZ SLI   |

## Bits [31:3]

Reserved, RES0.

## Bits [2:1]

Reserved, RAZ.

Not thirty-two bit. Describes the size of the TRBLAR register.

This field reads-as-zero.

## SLI, bit [0]

Indicates the Software Lock is not implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SLI   | Meaning                                                            |
|-------|--------------------------------------------------------------------|
| 0b0   | Software Lock is not implemented. Writes to theTRBLAR are ignored. |
| 0b1   | Software Lock is implemented.                                      |

Access to this field is RAZ/WI.

## Accessing TRBLSR

TRBLSR can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFB4    | TRBLSR     |

## H9.4.19 TRBMAR\_EL1, Trace Buffer Memory Attribute Register

The TRBMAR\_EL1 characteristics are:

## Purpose

Controls Trace Buffer Unit accesses to memory.

## Configuration

TRBMAR\_EL1 is in the Core power domain

External register TRBMAR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBMAR\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBMAR\_EL1 are RES0.

## Attributes

TRBMAR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:12]

Reserved, RES0.

## PAS, bits [11:10]

Physical address specifier. Defines the PAS attribute for memory addressed by the buffer in External mode.

| PAS   | Meaning     | Applies when               |
|-------|-------------|----------------------------|
| 0b00  | Secure.     | FEAT_Secure is implemented |
| 0b01  | Non-secure. |                            |
| 0b10  | Root.       | FEAT_RME is implemented    |
| 0b11  | Realm.      | FEAT_RME is implemented    |

## All other values are reserved.

If the Trace Buffer Unit is using external mode and either TRBMAR\_EL1.PAS is set to a reserved value, or the IMPLEMENTATION DEFINED authentication interface prohibits invasive debug of the Security state corresponding to the physical address space selected by TRBMAR\_EL1.PAS, then when the Trace Buffer Unit receives trace data from the trace unit, it does not write the trace data to memory and generates a trace buffer management event. That is, if any of the following apply:

- ExternalInvasiveDebugEnabled() == FALSE.
- TRBMAR\_EL1.PAS is 0b00 , and either ExternalSecureInvasiveDebugEnabled() == FALSE or Secure state is not implemented.

- TRBMAR\_EL1.PAS is 0b10 , and either ExternalRootInvasiveDebugEnabled() == FALSE or FEAT\_RME is not implemented.
- TRBMAR\_EL1.PAS is 0b11 , and either ExternalRealmInvasiveDebugEnabled() == FALSE or FEAT\_RME is not implemented.

This field is ignored by the PE when SelfHostedTraceEnabled() == TRUE.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## SH, bits [9:8]

Trace buffer shareability domain. Defines the shareability domain for Normal memory used by the trace buffer.

| SH   | Meaning          |
|------|------------------|
| 0b00 | Non-shareable.   |
| 0b10 | Outer Shareable. |
| 0b11 | Inner Shareable. |

All other values are reserved.

This field is ignored when TRBMAR\_EL1.Attr specifies any of the following memory types:

- Any Device memory type.
- Normal memory, Inner Non-cacheable, Outer Non-cacheable.

All Device and Normal Inner Non-cacheable Outer Non-cacheable memory regions are always treated as Outer Shareable.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Attr, bits [7:0]

Trace buffer memory type and attributes. Defines the memory type and, for Normal memory, the cacheability attributes, for memory addressed by the trace buffer.

The encoding of this field is the same as that of a MAIR\_ELx.Attr&lt;n&gt; field, as follows:

| Attr        |                                     | Meaning                                                                                                                                                                                                          |
|-------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 dd00 |                                     | Device memory. See encoding of 'dd' for the type of Device memory.                                                                                                                                               |
| 0b0000 dd01 |                                     | If FEAT_XS is implemented: Device memory with the XS attribute set to 0. See encoding of 'dd' for the type of Device memory. Otherwise, UNPREDICTABLE.                                                           |
| 0b0000 dd1x |                                     | UNPREDICTABLE.                                                                                                                                                                                                   |
| 0booooiiii  | where oooo != 0000 and iiii != 0000 | Normal memory. See encoding of 'oooo' and 'iiii' for the type of Normal memory.                                                                                                                                  |
| 0b01000000  |                                     | If FEAT_XS is implemented: Normal Inner Non-cacheable, Outer Non-cacheable memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE.                                                                      |
| 0b10100000  |                                     | If FEAT_XS is implemented: Normal Inner Write-through Cacheable, Outer Write-through Cacheable, Read-Allocate, No-Write Allocate, Non-transient memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE. |

| Attr       |                                                                       | Meaning                                                                                                                                                      |
|------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b11110000 |                                                                       | If FEAT_MTE2 is implemented: Tagged Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory. Otherwise, UNPREDICTABLE. |
| 0bxxxx0000 | where xxxx != 0000 and xxxx != 0100 and xxxx != 1010 and xxxx != 1111 | UNPREDICTABLE.                                                                                                                                               |

dd is encoded as follows:

oooo is encoded as follows:

| 'oooo'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Outer Write-Through Transient.     |
| 0b0100   |              | Normal memory, Outer Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Outer Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Outer Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Outer Write-Back Non-transient.    |

R encodes the Outer Read-Allocate policy and W encodes the Outer Write-Allocate policy.

iiii is encoded as follows:

| 'iiii'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Inner Write-Through Transient.     |
| 0b0100   |              | Normal memory, Inner Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Inner Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Inner Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Inner Write-Back Non-transient.    |

R encodes the Inner Read-Allocate policy and W encodes the Inner Write-Allocate policy.

In oooo and iiii , R and W are encoded as follows:

| 'dd'   | Meaning               |
|--------|-----------------------|
| 0b00   | Device-nGnRnE memory. |
| 0b01   | Device-nGnRE memory.  |
| 0b10   | Device-nGRE memory.   |
| 0b11   | Device-GRE memory.    |

Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| 'R' or 'W'   | Meaning      |
|--------------|--------------|
| 0b0          | No Allocate. |
| 0b1          | Allocate.    |

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable, Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBMAR\_EL1

The PE might ignore a write to TRBMAR\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 and the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 and the Trace Buffer Unit is using External mode.

TRBMAR\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0x028    | TRBMAR_EL1 |

## H9.4.20 TRBMPAM\_EL1, Trace Buffer MPAM Configuration Register

The TRBMPAM\_EL1 characteristics are:

## Purpose

Defines the PARTID, PMG, and MPAM\_SP values used by the trace buffer unit in external mode.

## Configuration

TRBMPAM\_EL1 is in the Core power domain

External register TRBMPAM\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBMPAM\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented and FEAT\_TRBE\_MPAM is implemented. Otherwise, direct accesses to TRBMPAM\_EL1 are RES0.

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

- TRBLIMITR\_EL1.E == 0b1 and the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 and the Trace Buffer Unit is using External mode.

TRBMPAM\_EL1 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| TRBE        | 0x040    | TRBMPAM_EL1 |

## H9.4.21 TRBPIDR0, Peripheral Identification Register 0

The TRBPIDR0 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR0 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR0 are RES0.

## Attributes

TRBPIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PART\_0, bits [7:0]

Part number, bits [7:0].

The part number is selected by the designer of the component, and is stored in TRBPIDR1.PART\_1 and TRBPIDR0.PART\_0.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRBPIDR0

TRBPIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFE0    | TRBPIDR0   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.22 TRBPIDR1, Peripheral Identification Register 1

The TRBPIDR1 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR1 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR1 are RES0.

## Attributes

TRBPIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## DES\_0, bits [7:4]

Designer, JEP106 identification code, bits [3:0]. TRBPIDR1.DES\_0 and TRBPIDR2.DES\_1 together form the JEDEC-assigned JEP106 identification code for the designer of the component. The parity bit in the JEP106 identification code is not included. The code identifies the designer of the component, which might not be not the same as the implementer of the device containing the component. To obtain a number, or to see the assignment of these codes, contact JEDEC http://www.jedec.org.

This field has an IMPLEMENTATION DEFINED value.

Note

For a component designed by Arm Limited, the JEP106 identification code is 0x3B .

Access to this field is RO.

## PART\_1, bits [3:0]

Part number, bits [11:8].

The part number is selected by the designer of the component, and is stored in TRBPIDR1.PART\_1 and TRBPIDR0.PART\_0.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing TRBPIDR1

TRBPIDR1 can be accessed through the external debug interface:

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFE4    | TRBPIDR1   |

## H9.4.23 TRBPIDR2, Peripheral Identification Register 2

The TRBPIDR2 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR2 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR2 are RES0.

## Attributes

TRBPIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## REVISION, bits [7:4]

Component major revision. TRBPIDR2.REVISION and TRBPIDR3.REVAND together form the revision number of the component, with TRBPIDR2.REVISION being the most significant part and TRBPIDR3.REVAND the least significant part. When a component is changed, TRBPIDR2.REVISION or TRBPIDR3.REVAND are increased to ensure that software can differentiate the different revisions of the component. TRBPIDR3.REV AND should be set to 0b0000 when TRBPIDR2.REVISION is increased.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## JEDEC, bit [3]

JEDEC-assigned JEP106 implementer code is used.

Reads as 0b1

Access to this field is RO.

## DES\_1, bits [2:0]

Designer, JEP106 identification code, bits [6:4]. TRBPIDR1.DES\_0 and TRBPIDR2.DES\_1 together form the JEDEC-assigned JEP106 identification code for the designer of the component. The parity bit in the JEP106 identification code is not included. The code identifies the designer of the component, which might not be not the same as the implementer of the device containing the component. To obtain a number, or to see the assignment of these codes, contact JEDEC http://www.jedec.org.

This field has an IMPLEMENTATION DEFINED value.

Note

For a component designed by Arm Limited, the JEP106 identification code is 0x3B .

Access to this field is RO.

## Accessing TRBPIDR2

TRBPIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFE8    | TRBPIDR2   |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.24 TRBPIDR3, Peripheral Identification Register 3

The TRBPIDR3 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR3 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR3 are RES0.

## Attributes

TRBPIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## REVAND, bits [7:4]

Component minor revision. TRBPIDR2.REVISION and TRBPIDR3.REVAND together form the revision number of the component, with TRBPIDR2.REVISION being the most significant part and TRBPIDR3.REVAND the least significant part. When a component is changed, TRBPIDR2.REVISION or TRBPIDR3.REVAND are increased to ensure that software can differentiate the different revisions of the component. TRBPIDR3.REV AND should be set to 0b0000 when TRBPIDR2.REVISION is increased.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CMOD,bits [3:0]

Customer Modified.

Indicates the component has been modified.

Avalue of 0b0000 means the component is not modified from the original design.

Any other value means the component has been modified in an IMPLEMENTATION DEFINED way.

This field has an IMPLEMENTATION DEFINED value.

For any two components with the same Unique Component Identifier:

- If TRBPIDR3.CMOD is zero in both components, then the components are identical.
- If TRBPIDR3.CMOD has the same nonzero value in both components, then this does not necessarily mean that they have the same modifications.
- If TRBPIDR3.CMOD is nonzero in either component, the two components might not be identical despite having the same Unique Component Identifier.

Access to this field is RO.

## Accessing TRBPIDR3

TRBPIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFEC    | TRBPIDR3   |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.25 TRBPIDR4, Peripheral Identification Register 4

The TRBPIDR4 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR4 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR4 are RES0.

## Attributes

TRBPIDR4 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SIZE, bits [7:4]

Size of the component.

The distance from the start of the address space used by this component to the end of the component identification registers.

Avalue of 0b0000 means one of the following is true:

- The component uses a single 4KB block.
- The component uses an IMPLEMENTATION DEFINED number of 4KB blocks.

Any other value means the component occupies 2 TRBPIDR4.SIZE 4KB blocks.

Reads as 0b0000

Using this field to indicate the size of the component is deprecated. This field might not correctly indicate the size of the component. Arm recommends that software determine the size of the component from the Unique Component Identifier fields, and other IMPLEMENTATION DEFINED registers in the component.

Access to this field is RO.

## DES\_2, bits [3:0]

Designer, JEP106 continuation code. This is the JEDEC-assigned JEP106 bank identifier for the designer of the component, minus 1. The code identifies the designer of the component, which might not be not the same as the implementer of the device containing the component. To obtain a number, or to see the assignment of these codes, contact JEDEC http://www.jedec.org.

This field has an IMPLEMENTATION DEFINED value.

Note

For a component designed by Arm Limited, the JEP106 bank is 5, meaning this field has the value 0x4 .

Access to this field is RO.

## Accessing TRBPIDR4

TRBPIDR4 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFD0    | TRBPIDR4   |

## Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.26 TRBPIDR5, Peripheral Identification Register 5

The TRBPIDR5 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR5 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR5 are RES0.

## Attributes

TRBPIDR5 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 0   |
|------|-----|

## Bits [31:0]

Reserved, RES0.

## Accessing TRBPIDR5

TRBPIDR5 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFD4    | TRBPIDR5   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.27 TRBPIDR6, Peripheral Identification Register 6

The TRBPIDR6 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR6 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR6 are RES0.

## Attributes

TRBPIDR6 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:0]

Reserved, RES0.

## Accessing TRBPIDR6

TRBPIDR6 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFD8    | TRBPIDR6   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.28 TRBPIDR7, Peripheral Identification Register 7

The TRBPIDR7 characteristics are:

## Purpose

Provides discovery information about the component.

For additional information, see the CoreSight Architecture Specification.

## Configuration

TRBPIDR7 is in the Core power domain

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPIDR7 are RES0.

## Attributes

TRBPIDR7 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:0]

Reserved, RES0.

## Accessing TRBPIDR7

TRBPIDR7 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0xFDC    | TRBPIDR7   |

Accessible as follows:

- When DoubleLockStatus() or !IsCorePowered(), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RO.

## H9.4.29 TRBPTR\_EL1, Trace Buffer Write Pointer Register

The TRBPTR\_EL1 characteristics are:

## Purpose

Defines the current write pointer for the trace buffer.

## Configuration

TRBPTR\_EL1 is in the Core power domain

External register TRBPTR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBPTR\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBPTR\_EL1 are RES0.

## Attributes

TRBPTR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |     |
|------|------|-----|
| PTR  | PTR  | PTR |
| 31   | 0    |     |
| PTR  | PTR  | PTR |

## PTR, bits [63:0]

Trace Buffer current write pointer address.

Defines the virtual address of the next entry to be written to the trace buffer.

If TRBIDR\_EL1.Align is not zero, then it is IMPLEMENTATION DEFINED whether bits [M-1:0] are RES0 or read/write, where M is an integer between 1 and TRBIDR\_EL1.Align inclusive.

The architecture places restrictions on the values that software can write to the pointer. For more information see Restrictions on Programming the Trace Buffer Unit.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBPTR\_EL1

The PE might ignore a write to TRBPTR\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 and the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 and the Trace Buffer Unit is using External mode.

TRBPTR\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0x008    | TRBPTR_EL1 |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.4.30 TRBSR\_EL1, Trace Buffer Status/syndrome Register

The TRBSR\_EL1 characteristics are:

## Purpose

Provides syndrome information to software for a trace buffer management event.

## Configuration

TRBSR\_EL1 is in the Core power domain

External register TRBSR\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBSR\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBSR\_EL1 are RES0.

## Attributes

TRBSR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## MSS2, bits [55:32]

Management event Specific Syndrome 2. Contains syndrome specific to the management event.

The syndrome contents for each management event are described in the following sections.

MSS2 encoding for other trace buffer management events

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for stage 1 or stage 2 Data Aborts on write to trace buffer

<!-- image -->

## Bits [23:9]

Reserved, RES0.

## TopLevel, bit [8]

## When FEAT\_THE is implemented:

TopLevel. Indicates if the fault was due to TopLevel.

| TopLevel   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Fault is not due to TopLevel. |
| 0b1        | Fault is due to TopLevel.     |

## Otherwise:

Reserved, RES0.

## AssuredOnly, bit [7]

## When FEAT\_THE is implemented, TRBSR\_EL1.EC == '100101', and GetTRBSR\_EL1\_FSC() IN {'0011xx'}:

AssuredOnly flag. If a memory access generates a stage 2 Data Abort, then this field holds information about the fault.

| AssuredOnly   | Meaning                               |
|---------------|---------------------------------------|
| 0b0           | Data Abort is not due to AssuredOnly. |
| 0b1           | Data Abort is due to AssuredOnly.     |

## Otherwise:

Reserved, RES0.

## Overlay, bit [6]

## When (FEAT\_S1POE is implemented or FEAT\_S2POE is implemented) and GetTRBSR\_EL1\_FSC() IN {'0011xx'}:

Overlay flag. If a memory access generates a Data Abort for a Permission fault, then this field holds information about the fault.

| Overlay   | Meaning                                       |
|-----------|-----------------------------------------------|
| 0b0       | Data Abort is not due to Overlay Permissions. |
| 0b1       | Data Abort is due to Overlay Permissions.     |

## Otherwise:

Reserved, RES0.

## DirtyBit, bit [5]

## When (FEAT\_S1PIE is implemented or FEAT\_S2PIE is implemented) and GetTRBSR\_EL1\_FSC() IN {'0011xx'}:

DirtyBit flag. If a write access to memory generates a Data Abort for a Permission fault using Indirect Permission, then this field holds information about the fault.

| DirtyBit   | Meaning                                     |
|------------|---------------------------------------------|
| 0b0        | Permission Fault is not due to dirty state. |
| 0b1        | Permission Fault is due to dirty state.     |

## Otherwise:

Reserved, RES0.

## Bits [4:0]

Reserved, RES0.

MSS2 encoding for Granule Protection Check faults on write to trace buffer

<!-- image -->

## Bits [23:0]

Reserved, RES0.

MSS2 encoding for trace buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [23:0]

IMPLEMENTATION DEFINED.

## EC, bits [31:26]

Event class. Top-level description of the cause of the trace buffer management event.

| EC       | Meaning                                                                                                                                                                                                                                                                                                                                                                                                             | MSS                                                                                | MSS2                                                                                 | Applies when            |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|-------------------------|
| 0b000000 | Other trace buffer management event. All trace buffer management events other than those described by the other defined Event class codes.                                                                                                                                                                                                                                                                          | MSSencoding for other trace buffer management events                               | MSS2 encoding for other trace buffer management events                               |                         |
| 0b011110 | Granule Protection Check fault on write to trace buffer, other than Granule Protection Fault (GPF). That is, any of the following: • Granule Protection Table (GPT) address size fault. • GPT walk fault. • Synchronous External abort on GPT fetch. AGPFontranslation table walk or update is reported as either a Stage 1 or Stage 2 Data Abort, as appropriate. Other GPFs are reported as a Stage 1 Data Abort. | MSSencoding for Granule Protection Check faults on write to trace buffer           | MSS2 encoding for Granule Protection Check faults on write to trace buffer           | FEAT_RME is implemented |
| 0b011111 | Trace buffer management event for an IMPLEMENTATION DEFINED reason.                                                                                                                                                                                                                                                                                                                                                 | MSSencoding for trace buffer management event for an IMPLEMENTATION DEFINED reason | MSS2 encoding for trace buffer management event for an IMPLEMENTATION DEFINED reason |                         |
| 0b100100 | Stage 1 Data Abort on write to trace buffer.                                                                                                                                                                                                                                                                                                                                                                        | MSSencoding for stage 1 or stage 2 Data Aborts on write to trace buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to trace buffer            |                         |
| 0b100101 | Stage 2 Data Abort on write to trace buffer.                                                                                                                                                                                                                                                                                                                                                                        | MSSencoding for stage 1 or stage 2 Data Aborts on write to trace buffer            | MSS2 encoding for stage 1 or stage 2 Data Aborts on write to trace buffer            |                         |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [25:24]

Reserved, RES0.

## DAT, bit [23]

## When FEAT\_TRBE\_EXT is implemented:

Data. Indicates when the Trace Buffer Unit has trace data that has not yet been written to memory.

| DAT   | Meaning                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------|
| 0b0   | Internal buffers are empty. All Trace operations Accepted by the Trace Buffer Unit will Complete in finite time. |
| 0b1   | Internal buffers are not empty.                                                                                  |

When TRBSR\_EL1.{DAT, S} is {0, 1}, meaning Collection is stopped and the Trace Buffer Unit internal buffers are empty, then all trace data has been written to memory. An additional Data Synchronization Barrier may be required to ensure that the writes are Complete. When TRBSR\_EL1.DAT is 0 and Collection is not stopped, there may still be trace data held by the trace unit that the Trace Buffer Unit has not Accepted.

That is, TRBSR\_EL1.DAT reads as 1 when the Trace Buffer Unit has Accepted trace data from the trace unit, but has not yet written it to memory.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## IRQ, bit [22]

Maintenance status. Indicates that a trace buffer management event has been recorded.

| IRQ   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | No trace buffer management event for EL1 has been recorded. |
| 0b1   | Atrace buffer management event for EL1 has been recorded.   |

When FEAT\_TRBE\_EXC is implemented, this field indicates a management event for EL1.

If FEAT\_TRBE\_EXC is implemented and the TRBE Profiling exception for EL1 is enabled, then when this field is 1, a TRBE Profiling exception for EL1 is pending

If FEAT\_TRBE\_EXC is not implemented or the TRBE Profiling exception for EL1 is disabled, then this field drives the TRBIRQ trace buffer interrupt request signal.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## TRG, bit [21]

Triggered.

| TRG   | Meaning                                                                          |
|-------|----------------------------------------------------------------------------------|
| 0b0   | No Detected Trigger has been observed since this field was last cleared to zero. |
| 0b1   | ADetected Trigger has been observed since this field was last cleared to zero.   |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## WRAP, bit [20]

Wrapped.

| WRAP   | Meaning                                                                              |
|--------|--------------------------------------------------------------------------------------|
| 0b0    | The current write pointer has not wrapped since this field was last cleared to zero. |
| 0b1    | The current write pointer has wrapped since this field was last cleared to zero.     |

For each byte of trace the Trace Buffer Unit Accepts and writes to the trace buffer at the address in the current write pointer, if the current write pointer is equal to the Limit pointer minus one, the current write pointer is wrapped by setting it to the Base pointer, and this field is set to 1.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bit [19]

Reserved, RES0.

## EA, bit [18]

## When Armv9.3:

Reserved, RES0.

## When the PE sets this bit as the result of an External abort:

External Abort.

| EA   | Meaning                                                                    |
|------|----------------------------------------------------------------------------|
| 0b0  | An External abort has not been asserted.                                   |
| 0b1  | An External abort has been asserted and detected by the Trace Buffer Unit. |

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## S, bit [17]

Stopped.

The reset behavior of this field is:

| S   | Meaning                          |
|-----|----------------------------------|
| 0b0 | Collection has not been stopped. |
| 0b1 | Collection is stopped.           |

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bit [16]

Reserved, RES0.

## MSS, bits [15:0]

Management Event Specific Syndrome. Contains syndrome specific to the trace buffer management event.

The syndrome contents for each trace buffer management event are described in the following sections.

## MSSencoding for other trace buffer management events

<!-- image -->

## Bits [15:6]

Reserved, RES0.

## BSC, bits [5:0]

Trace buffer status code

| BSC      | Meaning                                                                                                                                       |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b000000 | Collection not stopped, or access not allowed.                                                                                                |
| 0b000001 | Trace buffer filled. Collection stopped because the current write pointer wrapped to the base pointer and the trace buffer mode is Fill mode. |
| 0b000010 | Trigger Event. Collection stopped because of a Trigger Event. See TRBTRG_EL1 for more information.                                            |
| 0b000011 | Manual Stop. Collection stopped because of a Manual Stop event. See TRBCR.ManStop for more information.                                       |
| 0b000100 | Buffer size. The requested trace buffer size was too large.                                                                                   |

All other values are reserved.

## MSSencoding for stage 1 or stage 2 Data Aborts on write to trace buffer

<!-- image -->

## Bits [15:6]

Reserved, RES0.

## FSC, bits [5:0]

Fault status code

| FSC      | Meaning                                                                                                                       | Applies when                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 0b000000 | Address size fault, level 0 of translation or translation table base register.                                                |                                                          |
| 0b000001 | Address size fault, level 1.                                                                                                  |                                                          |
| 0b000010 | Address size fault, level 2.                                                                                                  |                                                          |
| 0b000011 | Address size fault, level 3.                                                                                                  |                                                          |
| 0b000100 | Translation fault, level 0.                                                                                                   |                                                          |
| 0b000101 | Translation fault, level 1.                                                                                                   |                                                          |
| 0b000110 | Translation fault, level 2.                                                                                                   |                                                          |
| 0b000111 | Translation fault, level 3.                                                                                                   |                                                          |
| 0b001001 | Access flag fault, level 1.                                                                                                   |                                                          |
| 0b001010 | Access flag fault, level 2.                                                                                                   |                                                          |
| 0b001011 | Access flag fault, level 3.                                                                                                   |                                                          |
| 0b001000 | Access flag fault, level 0.                                                                                                   | FEAT_LPA2 is implemented                                 |
| 0b001100 | Permission fault, level 0.                                                                                                    | FEAT_LPA2 is implemented                                 |
| 0b001101 | Permission fault, level 1.                                                                                                    |                                                          |
| 0b001110 | Permission fault, level 2.                                                                                                    |                                                          |
| 0b001111 | Permission fault, level 3.                                                                                                    |                                                          |
| 0b010000 | Synchronous External abort, not on translation table walk or hardware update of translation table.                            |                                                          |
| 0b010001 | Asynchronous External abort.                                                                                                  |                                                          |
| 0b010010 | Synchronous External abort on translation table walk or hardware update of translation table, level -2.                       | FEAT_D128 is implemented                                 |
| 0b010011 | Synchronous External abort on translation table walk or hardware update of translation table, level -1.                       | FEAT_LPA2 is implemented                                 |
| 0b010100 | Synchronous External abort on translation table walk or hardware update of translation table, level 0.                        |                                                          |
| 0b010101 | Synchronous External abort on translation table walk or hardware update of translation table, level 1.                        |                                                          |
| 0b010110 | Synchronous External abort on translation table walk or hardware update of translation table, level 2.                        |                                                          |
| 0b010111 | Synchronous External abort on translation table walk or hardware update of translation table, level 3.                        |                                                          |
| 0b011011 | Synchronous parity or ECC error on memory access on translation table walk or hardware update of translation table, level -1. | FEAT_LPA2 is implemented and FEAT_RAS is not implemented |
| 0b100001 | Alignment fault.                                                                                                              |                                                          |
| 0b100010 | Granule Protection Fault on translation table walk or hardware update of translation table, level -2.                         | FEAT_D128 is implemented and FEAT_RME is implemented     |

| FSC      | Meaning                                                                                               | Applies when                                         |
|----------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| 0b100011 | Granule Protection Fault on translation table walk or hardware update of translation table, level -1. | FEAT_RME is implemented and FEAT_LPA2 is implemented |
| 0b100100 | Granule Protection Fault on translation table walk or hardware update of translation table, level 0.  | FEAT_RME is implemented                              |
| 0b100101 | Granule Protection Fault on translation table walk or hardware update of translation table, level 1.  | FEAT_RME is implemented                              |
| 0b100110 | Granule Protection Fault on translation table walk or hardware update of translation table, level 2.  | FEAT_RME is implemented                              |
| 0b100111 | Granule Protection Fault on translation table walk or hardware update of translation table, level 3.  | FEAT_RME is implemented                              |
| 0b101000 | Granule Protection Fault, not on translation table walk or hardware update of translation table.      | FEAT_RME is implemented                              |
| 0b101001 | Address size fault, level -1.                                                                         | FEAT_LPA2 is implemented                             |
| 0b101010 | Translation fault, level -2.                                                                          | FEAT_D128 is implemented                             |
| 0b101011 | Translation fault, level -1.                                                                          | FEAT_LPA2 is implemented                             |
| 0b101100 | Address Size fault, level -2.                                                                         | FEAT_D128 is implemented                             |
| 0b110000 | TLB conflict abort.                                                                                   |                                                      |
| 0b110001 | Unsupported atomic hardware update fault.                                                             | FEAT_HAFDBS is implemented                           |

All other values are reserved.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## MSSencoding for Granule Protection Check faults on write to trace buffer

<!-- image -->

## Bits [15:0]

Reserved, RES0.

MSSencoding for trace buffer management event for an IMPLEMENTATION DEFINED reason

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [15:0]

IMPLEMENTATION DEFINED.

## Accessing TRBSR\_EL1

The PE might ignore a write to TRBSR\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 and the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 and the Trace Buffer Unit is using External mode.

TRBSR\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0x018    | TRBSR_EL1  |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.

## H9.4.31 TRBTRG\_EL1, Trace Buffer Trigger Counter Register

The TRBTRG\_EL1 characteristics are:

## Purpose

Specifies the number of bytes of trace to capture following a Detected Trigger before a Trigger Event.

## Configuration

TRBTRG\_EL1 is in the Core power domain

External register TRBTRG\_EL1 bits [63:0] are architecturally mapped to AArch64 System register TRBTRG\_EL1[63:0].

This register is present only when FEAT\_TRBE\_EXT is implemented. Otherwise, direct accesses to TRBTRG\_EL1 are RES0.

## Attributes

TRBTRG\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TRG, bits [31:0]

Trigger count.

Specifies the number of bytes of trace to capture following a Detected Trigger before a Trigger Event.

TRBTRG\_EL1 decrements by 1 for every byte of trace written to the trace buffer when all of the following are true:

- TRBTRG\_EL1 is nonzero.
- TRBSR\_EL1.TRG is 1.

The architecture places restrictions on the values that software can write to the counter.

Note

As a result of the restrictions an implementation might treat some of TRG[M:0] as RES0, where M is defined by TRBIDR\_EL1.Align.

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Accessing TRBTRG\_EL1

The PE might ignore a write to TRBTRG\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 and the Trace Buffer Unit is using Self-hosted mode.

- TRBLIMITR\_EL1.XE == 0b1 and the Trace Buffer Unit is using External mode.

TRBTRG\_EL1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| TRBE        | 0x020    | TRBTRG_EL1 |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), or !AllowExternalTraceBufferAccess(addrdesc), accesses to this register return an ERROR.
- Otherwise, accesses to this register are RW.