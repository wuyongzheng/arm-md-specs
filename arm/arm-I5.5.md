## I5.5 Activity Monitors external register descriptions

This section lists the external Activity Monitors registers.

## I5.5.1 AMCFGR, Activity Monitors Configuration Register

The AMCFGR characteristics are:

## Purpose

Global configuration register for the activity monitors.

Provides information on supported features, the number of counter groups implemented, the total number of activity monitor event counters implemented, and the size of the counters. AMCFGR is applicable to both the architected and the auxiliary counter groups.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCFGR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCFGR are RES0.

## Attributes

AMCFGRis a:

- 64-bit register when FEAT\_AMU\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_AMU\_EXT64 is implemented:

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

Access to this field is RO.

## Bits [27:25]

Reserved, RES0.

## HDBG, bit [24]

Halt-on-debug supported.

This feature must be supported, and so this bit is 0b1 .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HDBG   | Meaning                 |
|--------|-------------------------|
| 0b0    | AMCR.HDBGis RES0.       |
| 0b1    | AMCR.HDBGis read/write. |

Access to this field is RO.

## Bits [23:14]

Reserved, RAZ.

## SIZE, bits [13:8]

Defines the size of the activity monitor event counters, minus one.

The counters are 64-bit, so the value of this field is 0b111111 .

This field is used by software to determine the spacing of the counters in the memory-map. The counters are at doubleword-aligned addresses.

Reads as

0b111111

Access to this field is RO.

## N, bits [7:0]

Defines the number of activity monitor event counters implemented in all groups, minus one.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

<!-- image -->

## NCG, bits [31:28]

Defines the number of counter groups implemented, minus one.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

Access to this field is RO.

## Bits [27:25]

Reserved, RES0.

## HDBG, bit [24]

Halt-on-debug supported.

This feature must be supported, and so this bit is 0b1 .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HDBG   | Meaning                 |
|--------|-------------------------|
| 0b0    | AMCR.HDBGis RES0.       |
| 0b1    | AMCR.HDBGis read/write. |

Access to this field is RO.

## Bits [23:14]

Reserved, RAZ.

## SIZE, bits [13:8]

Defines the size of the activity monitor event counters, minus one.

The counters are 64-bit, so the value of this field is 0b111111 .

This field is used by software to determine the spacing of the counters in the memory-map. The counters are at doubleword-aligned addresses.

Reads as 0b111111

Access to this field is RO.

## N, bits [7:0]

Defines the number of activity monitor event counters implemented in all groups, minus one.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMCFGR

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xE00 from AMU

| NCG    | Meaning                         |
|--------|---------------------------------|
| 0b0000 | One counter group implemented.  |
| 0b0001 | Two counter groups implemented. |

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xE00 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.2 AMCGCR, Activity Monitors Counter Group Configuration Register

The AMCGCR characteristics are:

## Purpose

Provides information on the number of activity monitor event counters implemented within each counter group.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCGCR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCGCR are RES0.

## Attributes

AMCGCRis a:

- 64-bit register when FEAT\_AMU\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_AMU\_EXT64 is implemented:

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## CG1NC, bits [15:8]

Counter Group 1 Number of Counters. The number of counters in the auxiliary counter group.

In an implementation that includes FEAT\_AMUv1, the permitted range of values is 0 to 16.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CG0NC, bits [7:0]

Counter Group 0 Number of Counters. The number of counters in the architected counter group.

Reads as 0x04

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## CG1NC, bits [15:8]

Counter Group 1 Number of Counters. The number of counters in the auxiliary counter group.

In an implementation that includes FEAT\_AMUv1, the permitted range of values is 0 to 16.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CG0NC, bits [7:0]

Counter Group 0 Number of Counters. The number of counters in the architected counter group.

Reads as 0x04

Access to this field is RO.

## Accessing AMCGCR

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xCE0 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xCE0 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.3 AMCIDR0, Activity Monitors Component Identification Register 0

The AMCIDR0 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Component identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCIDR0 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMCIDR0, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCIDR0 are RES0.

## Attributes

AMCIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_0, bits [7:0]

Preamble.

Reads as 0x0D

Access to this field is RO.

## Accessing AMCIDR0

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFF0 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.4 AMCIDR1, Activity Monitors Component Identification Register 1

The AMCIDR1 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Component identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCIDR1 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMCIDR1, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCIDR1 are RES0.

## Attributes

AMCIDR1 is a 32-bit register.

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

## Accessing AMCIDR1

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFF4 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.5 AMCIDR2, Activity Monitors Component Identification Register 2

The AMCIDR2 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Component identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCIDR2 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMCIDR2, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCIDR2 are RES0.

## Attributes

AMCIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_2, bits [7:0]

Preamble.

Reads as 0x05

Access to this field is RO.

## Accessing AMCIDR2

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFF8 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.6 AMCIDR3, Activity Monitors Component Identification Register 3

The AMCIDR3 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Component identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCIDR3 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMCIDR3, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCIDR3 are RES0.

## Attributes

AMCIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_3, bits [7:0]

Preamble.

Reads as 0xB1

Access to this field is RO.

## Accessing AMCIDR3

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFFC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.7 AMCNTEN, Activity Monitors Count Set and Clear Register

The AMCNTEN characteristics are:

## Purpose

Control bits for the architected and auxiliary activity monitors event counters, AMEVCNTR0&lt;n&gt;. and AMEVCNTR1&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTEN is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT64 is implemented. Otherwise, direct accesses to AMCNTEN are RES0.

## Attributes

AMCNTENis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## P1&lt;n&gt; , bits [n+32], for n = 15 to 0

Activity monitor event counter control bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P1<n>   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | When read, means that AMEVCNTR1<n> is disabled. |
| 0b1     | When read, means that AMEVCNTR1<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMU.AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P0&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter control bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P0<n>   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | When read, means that AMEVCNTR0<n> is disabled. |
| 0b1     | When read, means that AMEVCNTR0<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTEN

If there are no auxiliary monitor event counters implemented, reads of AMCNTEN[63:32] are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xC10 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.8 AMCNTENCLR, Activity Monitors Count Enable Clear Register

The AMCNTENCLR characteristics are:

## Purpose

Disable control bits for the architected and auxiliary activity monitors event counters, AMEVCNTR0&lt;n&gt; and AMEVCNTR1&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTENCLR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT64 is implemented. Otherwise, direct accesses to AMCNTENCLR are RES0.

## Attributes

AMCNTENCLRis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## P1&lt;n&gt; , bits [n+32], for n = 15 to 0

Activity monitor event counter disable bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P1<n>   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | When read, means that AMEVCNTR1<n> is disabled. |
| 0b1     | When read, means that AMEVCNTR1<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMU.AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P0&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter disable bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P0<n>   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | When read, means that AMEVCNTR0<n> is disabled. |
| 0b1     | When read, means that AMEVCNTR0<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR

If there are no auxiliary monitor event counters implemented, reads of AMCNTENCLR[63:32] are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xC20 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.9 AMCNTENCLR0, Activity Monitors Count Enable Clear Register 0

The AMCNTENCLR0 characteristics are:

## Purpose

Disable control bits for the architected activity monitors event counters, AMEVCNTR0&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTENCLR0 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT32 is implemented. Otherwise, direct accesses to AMCNTENCLR0 are RES0.

## Attributes

AMCNTENCLR0is a 32-bit register.

## Field descriptions

| 31   | 16 15 4 3 2 1 0    |
|------|--------------------|
| RES0 | RAZ/WI P3 P2 P1 P0 |

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

## Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter disable bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P<n>   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR0<n> is disabled. |
| 0b1    | When read, means that AMEVCNTR0<n> is enabled.  |

The reset behavior of this field is:

· On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR0

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xC20 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.10 AMCNTENCLR1, Activity Monitors Count Enable Clear Register 1

The AMCNTENCLR1 characteristics are:

## Purpose

Disable control bits for the auxiliary activity monitors event counters, AMEVCNTR1&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTENCLR1 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCNTENCLR1 are RES0.

## Attributes

AMCNTENCLR1is a 32-bit register.

## Field descriptions

| 31   | 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------|

## Bits [31:16]

Reserved, RES0.

## P&lt;n&gt; , bits [n], for n = 15 to 0

Activity monitor event counter disable bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P<n>   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR1<n> is disabled. |
| 0b1    | When read, means that AMEVCNTR1<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMU.AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing AMCNTENCLR1

If there are no auxiliary monitor event counters implemented, reads of AMCNTENCLR1 are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xC24 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.11 AMCNTENSET, Activity Monitors Count Enable Set Register

The AMCNTENSET characteristics are:

## Purpose

Enable control bits for the architected and auxiliary activity monitors event counters, AMEVCNTR0&lt;n&gt; and AMEVCNTR1&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTENSET is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT64 is implemented. Otherwise, direct accesses to AMCNTENSET are RES0.

## Attributes

AMCNTENSETis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:48]

Reserved, RES0.

## P1&lt;n&gt; , bits [n+32], for n = 15 to 0

Activity monitor event counter enable bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P1<n>   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | When read, means that AMEVCNTR1<n> is disabled. |
| 0b1     | When read, means that AMEVCNTR1<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMU.AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P0&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter enable bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P0<n>   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | When read, means that AMEVCNTR0<n> is disabled. |
| 0b1     | When read, means that AMEVCNTR0<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET

If there are no auxiliary monitor event counters implemented, reads of AMCNTENSET[63:32] are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xC00 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.12 AMCNTENSET0, Activity Monitors Count Enable Set Register 0

The AMCNTENSET0 characteristics are:

## Purpose

Enable control bits for the architected activity monitors event counters, AMEVCNTR0&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTENSET0 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT32 is implemented. Otherwise, direct accesses to AMCNTENSET0 are RES0.

## Attributes

AMCNTENSET0 is a 32-bit register.

## Field descriptions

| 31   | 16 15 4 3 2 1 0    |
|------|--------------------|
| RES0 | RAZ/WI P3 P2 P1 P0 |

## Bits [31:16]

Reserved, RES0.

## Bits [15:4]

## Reserved, RAZ/WI.

This field is reserved for additional architected activity monitor event counters, which Arm might define in a future version of the Activity Monitors architecture.

## P&lt;n&gt; , bits [n], for n = 3 to 0

Activity monitor event counter enable bit for AMEVCNTR0&lt;n&gt;.

Note

AMCGCR.CG0NCidentifies the number of architected activity monitor event counters. In an implementation that includes FEAT\_AMUv1, the number of architected activity monitor event counters is 4.

Possible values of each bit are:

| P<n>   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR0<n> is disabled. |
| 0b1    | When read, means that AMEVCNTR0<n> is enabled.  |

The reset behavior of this field is:

· On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= 4, access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET0

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xC00 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.13 AMCNTENSET1, Activity Monitors Count Enable Set Register 1

The AMCNTENSET1 characteristics are:

## Purpose

Enable control bits for the auxiliary activity monitors event counters, AMEVCNTR1&lt;n&gt;.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCNTENSET1 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT32 is implemented. Otherwise, direct accesses to AMCNTENSET1 are RES0.

## Attributes

AMCNTENSET1 is a 32-bit register.

## Field descriptions

| 31   | 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|------|--------------------------------------------|

## Bits [31:16]

Reserved, RES0.

## P&lt;n&gt; , bits [n], for n = 15 to 0

Activity monitor event counter enable bit for AMEVCNTR1&lt;n&gt;.

Possible values of each bit are:

| P<n>   | Meaning                                         |
|--------|-------------------------------------------------|
| 0b0    | When read, means that AMEVCNTR1<n> is disabled. |
| 0b1    | When read, means that AMEVCNTR1<n> is enabled.  |

The reset behavior of this field is:

- On a AMU reset, this field resets to '0' .

Accessing this field has the following behavior:

- When n &gt;= UInt(AMU.AMCGCR.CG1NC), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing AMCNTENSET1

If there are no auxiliary monitor event counters implemented, reads of AMCNTENSET1 are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

There are no implemented auxiliary activity monitor event counters when AMCFGR.NCG == 0b0000 .

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xC04 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.14 AMCR, Activity Monitors Control Register

The AMCR characteristics are:

## Purpose

Global control register for the activity monitors implementation. AMCR is applicable to both the architected and the auxiliary counter groups.

## Configuration

It is IMPLEMENTATION DEFINED whether AMCR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMCR are RES0.

## Attributes

AMCRis a:

- 64-bit register when FEAT\_AMU\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_AMU\_EXT64 is implemented:

<!-- image -->

## Bits [63:18]

Reserved, RES0.

## CG1RZ, bit [17]

## When FEAT\_AMUv1p1 is implemented:

Counter Group 1 Read Zero.

| CG1RZ   | Meaning                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | System register reads of AMEVCNTR1<n> return the event count at all implemented and enabled Exception levels.                                                                                  |
| 0b1     | If the current Exception level is the highest implemented Exception level, System register reads of AMEVCNTR1<n> return the event count. Otherwise, reads of AMEVCNTR1<n> return a zero value. |

| Note                                                                            |
|---------------------------------------------------------------------------------|
| Reads from the memory-mapped view of AMEVCNTR1<n> are unaffected by this field. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:11]

Reserved, RES0.

## HDBG, bit [10]

This bit controls whether activity monitor counting is halted when the PE is halted in Debug state.

| HDBG   | Meaning                                                                      |
|--------|------------------------------------------------------------------------------|
| 0b0    | Activity monitors do not halt counting when the PE is halted in Debug state. |
| 0b1    | Activity monitors halt counting when the PE is halted in Debug state.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [9:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

## Bits [31:18]

Reserved, RES0.

## CG1RZ, bit [17]

## When FEAT\_AMUv1p1 is implemented:

Counter Group 1 Read Zero.

| CG1RZ   | Meaning                                                                                                                                                                                        |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | System register reads of AMEVCNTR1<n> return the event count at all implemented and enabled Exception levels.                                                                                  |
| 0b1     | If the current Exception level is the highest implemented Exception level, System register reads of AMEVCNTR1<n> return the event count. Otherwise, reads of AMEVCNTR1<n> return a zero value. |

Note

Reads from the memory-mapped view of AMEVCNTR1&lt;n&gt; are unaffected by this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [16:11]

Reserved, RES0.

## HDBG, bit [10]

This bit controls whether activity monitor counting is halted when the PE is halted in Debug state.

| HDBG   | Meaning                                                                      |
|--------|------------------------------------------------------------------------------|
| 0b0    | Activity monitors do not halt counting when the PE is halted in Debug state. |
| 0b1    | Activity monitors halt counting when the PE is halted in Debug state.        |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [9:0]

Reserved, RES0.

## Accessing AMCR

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xE04 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xE10 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.15 AMDEVAFF, Activity Monitors Device Affinity Register

The AMDEVAFF characteristics are:

## Purpose

Copy of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the AMUcomponent relates to.

## Configuration

It is IMPLEMENTATION DEFINED whether AMDEVAFF is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, FEAT\_AMU\_EXT64 is implemented, and an implementation implements AMDEVAFF1. Otherwise, direct accesses to AMDEVAFF are RES0.

## Attributes

AMDEVAFFis a 64-bit register.

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

## Accessing AMDEVAFF

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xFA8 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.16 AMDEVAFF0, Activity Monitors Device Affinity Register 0

The AMDEVAFF0 characteristics are:

## Purpose

Copy of the low half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the AMU component relates to.

## Configuration

It is IMPLEMENTATION DEFINED whether AMDEVAFF0 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, FEAT\_AMU\_EXT32 is implemented, and an implementation implements AMDEVAFF0. Otherwise, direct accesses to AMDEVAFF0 are RES0.

## Attributes

AMDEVAFF0 is a 32-bit register.

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

## Accessing AMDEVAFF0

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xFA8 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.17 AMDEVAFF1, Activity Monitors Device Affinity Register 1

The AMDEVAFF1 characteristics are:

## Purpose

Copy of the high half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the AMU component relates to.

## Configuration

It is IMPLEMENTATION DEFINED whether AMDEVAFF1 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, FEAT\_AMU\_EXT32 is implemented, and an implementation implements AMDEVAFF1. Otherwise, direct accesses to AMDEVAFF1 are RES0.

## Attributes

AMDEVAFF1 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## Aff3, bits [7:0]

Affinity level 3. See the description of AMDEV AFF0.Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMDEVAFF1

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xFAC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.18 AMDEVARCH, Activity Monitors Device Architecture Register

The AMDEVARCH characteristics are:

## Purpose

Identifies the programmers' model architecture of the AMU component.

## Configuration

It is IMPLEMENTATION DEFINED whether AMDEVARCH is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMDEVARCH, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMDEVARCH are RES0.

## Attributes

AMDEVARCHis a 32-bit register.

## Field descriptions

<!-- image -->

## ARCHITECT, bits [31:21]

Defines the architect of the component. For Activity Monitors, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as

0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the AMDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Defines the architecture revision. For architectures defined by Arm this is the minor revision.

| REVISION   | Meaning                         |
|------------|---------------------------------|
| 0b0000     | Architecture revision is AMUv1. |

All other values are reserved.

Access to this field is RO.

## ARCHID, bits [15:0]

Defines this part to be an AMU component. For architectures defined by Arm this is further subdivided.

For AMU:

- Bits [15:12] are the architecture version, also identified as AMDEV ARCH.ARCHVER.
- Bits [11:0] are the architecture part number, also identified as AMDEV ARCH.ARCHPART.

AMDEVARCH.ARCHVER= 0x0 , which corresponds to AMU architecture version AMUv1.

If FEAT\_AMU\_EXT32 is implemented, AMDEVARCH is 0xA66 .

If FEAT\_AMU\_EXT64 is implemented, AMDEVARCH is 0xA67 .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ARCHID   | Meaning                                 |
|----------|-----------------------------------------|
| 0x0A66   | AMUv1, with FEAT_AMU_EXT32 implemented. |
| 0x0A67   | AMUv1, with FEAT_AMU_EXT64 implemented. |

Access to this field is RO.

## Accessing AMDEVARCH

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xFBC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xFBC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.19 AMDEVTYPE, Activity Monitors Device Type Register

The AMDEVTYPE characteristics are:

## Purpose

Indicates to a debugger that this component is part of a PE's performance monitor interface.

## Configuration

It is IMPLEMENTATION DEFINED whether AMDEVTYPE is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMDEVTYPE, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMDEVTYPE are RES0.

## Attributes

AMDEVTYPEis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SUB, bits [7:4]

Subtype.

Access to this field is RO.

## MAJOR, bits [3:0]

Major type.

Access to this field is RO.

| SUB    | Meaning                |
|--------|------------------------|
| 0b0001 | Component within a PE. |

| MAJOR   | Meaning                        |
|---------|--------------------------------|
| 0b0110  | Performance monitor component. |

## Accessing AMDEVTYPE

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xFCC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xFCC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.20 AMEVCNTR0&lt;n&gt;, Activity Monitors Event Counter Registers 0, n = 0 - 3

The AMEVCNTR0&lt;n&gt; characteristics are:

## Purpose

Provides access to the architected activity monitor event counters.

## Configuration

It is IMPLEMENTATION DEFINED whether AMEVCNTR0&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMEVCNTR0&lt;n&gt; are RES0.

## Attributes

AMEVCNTR0&lt;n&gt; is a 64-bit register.

## Field descriptions

ACNT

63

32

ACNT

31

0

## ACNT, bits [63:0]

Architected activity monitor event counter n.

Value of architected activity monitor event counter n, where n is the number of this register and is a number from 0 to 3.

The reset behavior of this field is:

- On a AMU reset, this field resets to 0x0000000000000000 .

## Accessing AMEVCNTR0&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of architected activity monitor event counters, reads of AMEVCNTR0&lt;n&gt; are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

AMCGCR.CG0NC identifies the number of architected activity monitor event counters.

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

[63:0] Accessible at offset 0x000 + (8 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.

- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

[63:0] Accessible at offset 0x000 + (8 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.21 AMEVCNTR1&lt;n&gt;, Activity Monitors Event Counter Registers 1, n = 0 - 15

The AMEVCNTR1&lt;n&gt; characteristics are:

## Purpose

Provides access to the auxiliary activity monitor event counters.

## Configuration

It is IMPLEMENTATION DEFINED whether AMEVCNTR1&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMEVCNTR1&lt;n&gt; are RES0.

## Attributes

AMEVCNTR1&lt;n&gt; is a 64-bit register.

## Field descriptions

ACNT

63

32

ACNT

31

0

## ACNT, bits [63:0]

Auxiliary activity monitor event counter n.

Value of auxiliary activity monitor event counter n, where n is the number of this register and is a number from 0 to 15.

The reset behavior of this field is:

- On a AMU reset, this field resets to 0x0000000000000000 .

## Accessing AMEVCNTR1&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of auxiliary activity monitor event counters, reads of AMEVCNTR1&lt;n&gt; are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

AMCGCR.CG1NC identifies the number of auxiliary activity monitor event counters.

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

[63:0] Accessible at offset 0x100 + (8 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.

- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

[63:0] Accessible at offset 0x100 + (8 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.22 AMEVTYPER0&lt;n&gt;, Activity Monitors Event Type Registers 0, n = 0 - 3

The AMEVTYPER0&lt;n&gt; characteristics are:

## Purpose

Provides information on the events that an architected activity monitor event counter AMEVCNTR0&lt;n&gt; counts.

## Configuration

It is IMPLEMENTATION DEFINED whether AMEVTYPER0&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMEVTYPER0&lt;n&gt; are RES0.

## Attributes

AMEVTYPER0&lt;n&gt; is a:

- 64-bit register when FEAT\_AMU\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_AMU\_EXT64 is implemented:

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the architected activity monitor event counter AMEVCNTR0&lt;n&gt;. The value of this field is architecturally mandated for each architected counter.

The following table shows the mapping between required event numbers and the corresponding counters:

| evtCount   | Meaning                     | Applies when   |
|------------|-----------------------------|----------------|
| 0x0011     | Processor frequency cycles. | n == 0         |
| 0x4004     | Constant frequency cycles.  | n == 1         |
| 0x0008     | Instructions retired.       | n == 2         |
| 0x4005     | Memory stall cycles.        | n == 3         |

Access to this field is RO.

## Otherwise:

| 31   | 16 15    |
|------|----------|
| RES0 | evtCount |

## Bits [31:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the architected activity monitor event counter AMEVCNTR0&lt;n&gt;. The value of this field is architecturally mandated for each architected counter.

The following table shows the mapping between required event numbers and the corresponding counters:

| evtCount   | Meaning                     | Applies when   |
|------------|-----------------------------|----------------|
| 0x0011     | Processor frequency cycles. | n == 0         |
| 0x4004     | Constant frequency cycles.  | n == 1         |
| 0x0008     | Instructions retired.       | n == 2         |
| 0x4005     | Memory stall cycles.        | n == 3         |

Access to this field is RO.

## Accessing AMEVTYPER0&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of architected activity monitor event counters, reads of AMEVTYPER0&lt;n&gt; are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

AMCGCR.CG0NC identifies the number of architected activity monitor event counters.

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0x400 + (8 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0x400 + (4 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.23 AMEVTYPER1&lt;n&gt;, Activity Monitors Event Type Registers 1, n = 0 - 15

The AMEVTYPER1&lt;n&gt; characteristics are:

## Purpose

Provides information on the events that an auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt; counts.

## Configuration

It is IMPLEMENTATION DEFINED whether AMEVTYPER1&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMEVTYPER1&lt;n&gt; are RES0.

## Attributes

AMEVTYPER1&lt;n&gt; is a:

- 64-bit register when FEAT\_AMU\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_AMU\_EXT64 is implemented:

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt;.

It is IMPLEMENTATION DEFINED what values are supported by each counter.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## evtCount, bits [15:0]

Event to count. The event number of the event that is counted by the auxiliary activity monitor event counter AMEVCNTR1&lt;n&gt;.

It is IMPLEMENTATION DEFINED what values are supported by each counter.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing AMEVTYPER1&lt;n&gt;

If &lt;n&gt; is greater than or equal to the number of auxiliary activity monitor event counters, reads of AMEVTYPER1&lt;n&gt; are RAZ. Software must treat reserved accesses as RES0. See Access requirements for reserved and unallocated registers.

Note

AMCGCR.CG1NC identifies the number of auxiliary activity monitor event counters.

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0x480 + (4 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0x500 + (8 * n) from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.24 AMIIDR, Activity Monitors Implementation Identification Register

The AMIIDR characteristics are:

## Purpose

Defines the implementer and revisions of the AMU.

## Configuration

It is IMPLEMENTATION DEFINED whether AMIIDR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMIIDR are RES0.

## Attributes

AMIIDR is a:

- 64-bit register when FEAT\_AMU\_EXT64 is implemented.
- 32-bit register otherwise.

## Field descriptions

When FEAT\_AMU\_EXT64 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## ProductID, bits [31:20]

This field is an AMU part identifier.

This field has an IMPLEMENTATION DEFINED value.

If AMPIDR0 is implemented, AMPIDR0.PART\_0 matches bits [27:20] of this field.

If AMPIDR1 is implemented, AMPIDR1.PART\_1 matches bits [31:28] of this field.

Access to this field is RO.

## Variant, bits [19:16]

This field distinguishes product variants or major revisions of the product.

This field has an IMPLEMENTATION DEFINED value.

If AMPIDR2 is implemented, AMPIDR2.REVISION matches AMIIDR.Variant.

Access to this field is RO.

## Revision, bits [15:12]

This field distinguishes minor revisions of the product.

This field has an IMPLEMENTATION DEFINED value.

If AMPIDR3 is implemented, AMPIDR3.REVAND matches AMIIDR.Revision.

Access to this field is RO.

## Implementer, bits [11:0]

Contains the JEP106 manufacturer's identification code of the designer of the AMU.

The code identifies the designer of the component, which might not be the same as the implementer of the device containing the component.

Zero is not a valid JEP106 identification code, meaning a value of zero for AMIIDR indicates this register is not implemented.

For an implementation designed by Arm, this field reads as 0x43B .

This field has an IMPLEMENTATION DEFINED value.

Bits [11:8] contain the JEP106 bank identifier of the designer minus 1.

Bit 7 is RES0.

Bits [6:0] contain bits [6:0] of the JEP106 manufacturer's identification code of the designer.

If AMPIDR4 is implemented, AMPIDR4.DES\_2 matches bits [11:8] of this field.

If AMPIDR2 is implemented, AMPIDR2.DES\_1 matches bits [6:4] of this field.

If AMPIDR1 is implemented, AMPIDR1.DES\_0 matches bits [3:0] of this field.

Access to this field is RO.

## Otherwise:

| 31        | 20 19   | 16 15    | 12 11       |
|-----------|---------|----------|-------------|
| ProductID | Variant | Revision | Implementer |

## ProductID, bits [31:20]

This field is an AMU part identifier.

This field has an IMPLEMENTATION DEFINED value.

If AMPIDR0 is implemented, AMPIDR0.PART\_0 matches bits [27:20] of this field.

If AMPIDR1 is implemented, AMPIDR1.PART\_1 matches bits [31:28] of this field.

Access to this field is RO.

## Variant, bits [19:16]

This field distinguishes product variants or major revisions of the product.

This field has an IMPLEMENTATION DEFINED value.

If AMPIDR2 is implemented, AMPIDR2.REVISION matches AMIIDR.Variant.

Access to this field is RO.

## Revision, bits [15:12]

This field distinguishes minor revisions of the product.

This field has an IMPLEMENTATION DEFINED value.

If AMPIDR3 is implemented, AMPIDR3.REVAND matches AMIIDR.Revision.

Access to this field is RO.

## Implementer, bits [11:0]

Contains the JEP106 manufacturer's identification code of the designer of the AMU.

The code identifies the designer of the component, which might not be the same as the implementer of the device containing the component.

Zero is not a valid JEP106 identification code, meaning a value of zero for AMIIDR indicates this register is not implemented.

For an implementation designed by Arm, this field reads as 0x43B .

This field has an IMPLEMENTATION DEFINED value.

Bits [11:8] contain the JEP106 bank identifier of the designer minus 1.

Bit 7 is RES0.

Bits [6:0] contain bits [6:0] of the JEP106 manufacturer's identification code of the designer.

If AMPIDR4 is implemented, AMPIDR4.DES\_2 matches bits [11:8] of this field.

If AMPIDR2 is implemented, AMPIDR2.DES\_1 matches bits [6:4] of this field.

If AMPIDR1 is implemented, AMPIDR1.DES\_0 matches bits [3:0] of this field.

Access to this field is RO.

## Accessing AMIIDR

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXT64 is implemented

Accessible at offset 0xE08 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## When FEAT\_AMU\_EXT32 is implemented

Accessible at offset 0xE08 from AMU

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.25 AMPIDR0, Activity Monitors Peripheral Identification Register 0

The AMPIDR0 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Peripheral identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMPIDR0 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMPIDR0, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMPIDR0 are RES0.

## Attributes

AMPIDR0 is a 32-bit register.

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

## Accessing AMPIDR0

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFE0 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.26 AMPIDR1, Activity Monitors Peripheral Identification Register 1

The AMPIDR1 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Peripheral identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMPIDR1 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMPIDR1, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMPIDR1 are RES0.

## Attributes

AMPIDR1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7 4 3      |
|------|--------------|
| RES0 | DES_0 PART_1 |

## Bits [31:8]

Reserved, RES0.

## DES\_0, bits [7:4]

Designer, least significant nibble of JEP106 ID code.

For Arm Limited, this field is 0b1011 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## PART\_1, bits [3:0]

Part number, most significant nibble.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMPIDR1

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFE4 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.27 AMPIDR2, Activity Monitors Peripheral Identification Register 2

The AMPIDR2 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Peripheral identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMPIDR2 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMPIDR2, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMPIDR2 are RES0.

## Attributes

AMPIDR2 is a 32-bit register.

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

Designer, most significant bits of JEP106 ID code.

For Arm Limited, this field is 0b011 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMPIDR2

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFE8 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.28 AMPIDR3, Activity Monitors Peripheral Identification Register 3

The AMPIDR3 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Peripheral identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMPIDR3 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMPIDR3, and FEAT\_AMU\_EXT is implemented. Otherwise, direct accesses to AMPIDR3 are RES0.

## Attributes

AMPIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    | 3    |
|------|--------|------|
| RES0 | REVAND | CMOD |

## Bits [31:8]

Reserved, RES0.

## REVAND, bits [7:4]

Part minor revision. Parts using AMPIDR2.REVISION as an extension to the Part number must use this field as a major revision number.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CMOD,bits [3:0]

Customer modified. Indicates someone other than the Designer has modified the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMPIDR3

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFEC from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.29 AMPIDR4, Activity Monitors Peripheral Identification Register 4

The AMPIDR4 characteristics are:

## Purpose

Provides information to identify an activity monitors component.

For more information, see About the Peripheral identification scheme.

## Configuration

It is IMPLEMENTATION DEFINED whether AMPIDR4 is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMUv1 is implemented, an implementation implements AMPIDR4, and FEAT\_AMU\_EXT. Otherwise, direct accesses to AMPIDR4 are RES0.

## Attributes

AMPIDR4 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## SIZE, bits [7:4]

Size of the component. Log2 of the number of 4KB pages from the start of the component to the end of the component ID registers.

Reads as 0b0000

Access to this field is RO.

## DES\_2, bits [3:0]

Designer. JEP106 continuation code, least significant nibble.

For Arm Limited, this field is 0b0100 .

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing AMPIDR4

Accesses to this register use the following encodings:

## When FEAT\_AMUv1 is implemented

Accessible at offset 0xFD0 from AMU

- When ImpDefBool('AMU CoreSight management registers ignore access controls'), accesses to this register are RO.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Secure, and AMROOTCR.RAIN {'001', '000'}, accesses to this register are RAZ/WI.

- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Realm, and AMROOTCR.RAIN {'010', '000'}, accesses to this register are RAZ/WI.
- When FEAT\_RME is implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMROOTCR.RA!= '011', accesses to this register are RAZ/WI.
- When FEAT\_RME is not implemented, FEAT\_AMU\_EXTACR is implemented, an access is Non-secure, and AMSCR.NSRA == '0', accesses to this register are RAZ/WI.
- Otherwise, accesses to this register are RO.

## I5.5.30 AMROOTCR, Activity Monitors Root Control Register

The AMROOTCR characteristics are:

## Purpose

Control register for Root, Realm, Secure, and Non-secure access to External AMU registers.

## Configuration

It is IMPLEMENTATION DEFINED whether AMROOTCR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMU\_EXTACR is implemented and FEAT\_RME is implemented. Otherwise, direct accesses to AMROOTCR are RES0.

## Attributes

AMROOTCRis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

IMPL, bit [31]

Access to this field is RAO/WI.

## Bits [30:7]

Reserved, RES0.

## RA, bits [6:4]

Register Access to all External Activity Monitors registers.

| IMPL   | Meaning                       |
|--------|-------------------------------|
| 0b1    | Indicates AMROOTCRis present. |

| RA    | Meaning                                                                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b000 | Root register access is enabled. Access from other address spaces is disabled, meaning accesses to all External AMUregisters are RAZ/WI.            |
| 0b001 | Root and Realm register access is enabled. Access from other address spaces is disabled, meaning accesses to all External AMUregisters are RAZ/WI.  |
| 0b010 | Root and Secure register access is enabled. Access from other address spaces is disabled, meaning accesses to all External AMUregisters are RAZ/WI. |
| 0b011 | Root, Secure, Non-secure and Realm register access is enabled.                                                                                      |

Other values are reserved.

For the CoreSight management registers, 0xFA8 to 0xFFC , it is IMPLEMENTATION DEFINED whether these registers are RO or RAZ/WI when register access is disabled by this field.

## Bits [3:0]

Reserved, RES0.

## Accessing AMROOTCR

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXTACR is implemented and FEAT\_RME is implemented

Accessible at offset 0xE48 from AMU

- When an access is Root, accesses to this register are RW.
- Otherwise, accesses to this register are RAZ/WI.

## I5.5.31 AMSCR, Activity Monitors Secure Control Register

The AMSCR characteristics are:

## Purpose

Control register for Secure, and Non-secure access to External AMU registers.

## Configuration

It is IMPLEMENTATION DEFINED whether AMSCR is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_AMU\_EXTACR is implemented and FEAT\_RME is not implemented. Otherwise, direct accesses to AMSCR are RES0.

## Attributes

AMSCRis a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

IMPL, bit [31]

Access to this field is RAO/WI.

## Bits [30:2]

Reserved, RES0.

## NSRA, bit [1]

Register Access to all External Activity Monitors registers.

| NSRA   | Meaning                                |
|--------|----------------------------------------|
| 0b0    | Non-secure access is disabled, RAZ/WI. |

| IMPL   | Meaning                    |
|--------|----------------------------|
| 0b1    | Indicates AMSCRis present. |

## Bit [0]

Reserved, RES0.

## Accessing AMSCR

Accesses to this register use the following encodings:

## When FEAT\_AMU\_EXTACR is implemented and FEAT\_RME is not implemented

Accessible at offset 0xE40 from AMU

- When an access is Secure or an access is Root, accesses to this register are RW.
- Otherwise, accesses to this register are RAZ/WI.

| NSRA   | Meaning                       |
|--------|-------------------------------|
| 0b1    | Non-Secure access is enabled. |