## H9.5 Cross-Trigger Interface registers

This section lists the Cross-Trigger Interface registers.

## H9.5.1 ASICCTL, CTI External Multiplexer Control register

The ASICCTL characteristics are:

## Purpose

Can be used to provide IMPLEMENTATION DEFINED controls for the CTI. For example, the register might be used to control multiplexors for additional IMPLEMENTATION DEFINED triggers. The IMPLEMENTATION DEFINED controls provided by this register might modify the architecturally defined behavior of the CTI.

Note

The architecturally-defined triggers must not be multiplexed.

## Configuration

It is IMPLEMENTATION DEFINED whether ASICCTL is implemented in the Core power domain or in the Debug power domain

If it is implemented in the Core power domain, then it is IMPLEMENTATION DEFINED whether it is in the Cold reset domain or the Warm reset domain.

This register must reset to a value that supports the architecturally-defined behavior of the CTI. Changing the value of the register from its reset value causes IMPLEMENTATION DEFINED behavior that might differ from the architecturally-defined behavior of the CTI.

Other than the requirements listed in this register description, all aspects of the reset behavior of the ASICCTL are IMPLEMENTATION DEFINED.

## Attributes

ASICCTL is a 32-bit register.

## Field descriptions

| 31                     | 0                      |
|------------------------|------------------------|
| IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

## Accessing ASICCTL

ASICCTL can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0x144    | ASICCTL    |

Accessible as follows:

- When IsCorePowered(), !DoubleLockStatus(), !OSLockStatus(), AllowExternalDebugAccess(addrdesc), and SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are IMPLEMENTATION DEFINED.

## H9.5.2 CTIAPPCLEAR, CTI Application Trigger Clear register

The CTIAPPCLEAR characteristics are:

## Purpose

Clears the application triggers.

## Configuration

CTIAPPCLEAR is in the Debug power domain

External register CTIAPPCLEAR bits [31:0] are architecturally mapped to External register CTIAPPSET[31:0].

## Attributes

CTIAPPCLEAR is a 32-bit register.

## Field descriptions

<!-- image -->

## APPCLEAR&lt;x&gt; , bits [x], for x = 31 to 0

Application trigger &lt;x&gt; disable.

Writing to this bit has the following effect:

| APPCLEAR<x>   | Meaning                                                                                 |
|---------------|-----------------------------------------------------------------------------------------|
| 0b0           | No effect.                                                                              |
| 0b1           | Clear corresponding application trigger to 0 and clear the corresponding channel event. |

If the ECT does not support multicycle channel events, use of CTIAPPCLEAR is deprecated and the debugger must only use CTIAPPPULSE.

Accessing this field has the following behavior:

- When x &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is RAZ/W1C.

## Accessing CTIAPPCLEAR

CTIAPPCLEAR can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| CTI         | 0x018    | CTIAPPCLEAR |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

## H9.5.3 CTIAPPPULSE, CTI Application Pulse register

The CTIAPPPULSE characteristics are:

## Purpose

Causes event pulses to be generated on ECT channels.

## Configuration

CTIAPPPULSE is in the Debug power domain

## Attributes

CTIAPPPULSE is a 32-bit register.

## Field descriptions

<!-- image -->

## APPPULSE&lt;x&gt; , bits [x], for x = 31 to 0

Generate event pulse on ECT channel &lt;x&gt;.

| APPPULSE<x>   | Meaning                            |
|---------------|------------------------------------|
| 0b0           | No effect.                         |
| 0b1           | Channel <x> event pulse generated. |

## Note

- The CTIAPPPULSE operation does not affect the state of the application trigger. If the channel is active, either because of an earlier event or from the application trigger, then the value written to CTIAPPPULSE might have no effect.
- Multiple pulse events that occur close together might be merged into a single pulse event.

Accessing this field has the following behavior:

- When x &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is WO/UNKNOWN.

## Accessing CTIAPPPULSE

It is CONSTRAINED UNPREDICTABLE whether a write to CTIAPPPULSE generates an event on a channel if CTICONTROL.GLBEN is 0.

CTIAPPPULSE can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| CTI         | 0x01C    | CTIAPPPULSE |

Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

## H9.5.4 CTIAPPSET, CTI Application Trigger Set register

The CTIAPPSET characteristics are:

## Purpose

Sets the application triggers.

## Configuration

CTIAPPSET is in the Debug power domain

External register CTIAPPSET bits [31:0] are architecturally mapped to External register CTIAPPCLEAR[31:0].

## Attributes

CTIAPPSET is a 32-bit register.

## Field descriptions

<!-- image -->

## APPSET&lt;x&gt; , bits [x], for x = 31 to 0

Application trigger &lt;x&gt; enable.

| APPSET<x>   | Meaning                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Reading this means the application trigger is inactive. Writing this has no effect.                                                               |
| 0b1         | Reading this means the application trigger is active. Writing this sets the corresponding application trigger to 1 and generates a channel event. |

If the ECT does not support multicycle channel events, use of CTIAPPSET is deprecated and the debugger must only use CTIAPPPULSE.

The reset behavior of this field is:

- On a External debug reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When x &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is W1S.

## Accessing CTIAPPSET

CTIAPPSET can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0x014    | CTIAPPSET  |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.5 CTIAUTHSTATUS, CTI Authentication Status register

The CTIAUTHSTATUS characteristics are:

## Purpose

Provides information about the state of the IMPLEMENTATION DEFINED authentication interface for CTI.

## Configuration

CTIAUTHSTATUS is in the Debug power domain

This register is OPTIONAL, and is required for CoreSight compliance.

## Attributes

CTIAUTHSTATUS is a 32-bit register.

## Field descriptions

| 31   | 28 27   | 24 23   | 16 15   | 12 11   | 8 7   | 4 3 2   | 1 0   |
|------|---------|---------|---------|---------|-------|---------|-------|
| RES0 | RAZ     | RES0    | RAZ     | RES0    | RAZ   | NSNID   | NSID  |

## Bits [31:28]

Reserved, RES0.

## Bits [27:24]

Reserved, RAZ.

## Bits [23:16]

Reserved, RES0.

## Bits [15:12]

Reserved, RAZ.

## Bits [11:8]

Reserved, RES0.

## Bits [7:4]

Reserved, RAZ.

## NSNID, bits [3:2]

If EL3 is implemented, this field holds the same value as DBGAUTHSTATUS\_EL1.NSNID.

If EL3 is not implemented and the implemented Security state is Secure state, this field holds the same value as DBGAUTHSTATUS\_EL1.SNID.

## NSID, bits [1:0]

If EL3 is implemented, this field holds the same value as DBGAUTHSTATUS\_EL1.NSID.

If EL3 is not implemented and the implemented Security state is Secure state, this field holds the same value as DBGAUTHSTATUS\_EL1.SID.

## Accessing CTIAUTHSTATUS

CTIAUTHSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| CTI         | 0xFB8    | CTIAUTHSTATUS |

Accesses to this register are RO.

## H9.5.6 CTICHINSTATUS, CTI Channel In Status register

The CTICHINSTATUS characteristics are:

## Purpose

Provides the raw status of the ECT channel inputs to the CTI.

## Configuration

CTICHINSTATUS is in the Debug power domain

## Attributes

CTICHINSTATUS is a 32-bit register.

## Field descriptions

<!-- image -->

## CHIN&lt;n&gt; , bits [n], for n = 31 to 0

Input channel &lt;n&gt; status.

| CHIN<n>   | Meaning                        |
|-----------|--------------------------------|
| 0b0       | Input channel <n> is inactive. |
| 0b1       | Input channel <n> is active.   |

If the ECT channels do not support multicycle events, then it is IMPLEMENTATION DEFINED whether an input channel can be observed as active.

Accessing this field has the following behavior:

- When n &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is RO.

## Accessing CTICHINSTATUS

CTICHINSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance      |
|-------------|----------|---------------|
| CTI         | 0x138    | CTICHINSTATUS |

Accesses to this register are RO.

## H9.5.7 CTICHOUTSTATUS, CTI Channel Out Status register

The CTICHOUTSTATUS characteristics are:

## Purpose

Provides the status of the ECT channel outputs from the CTI.

## Configuration

CTICHOUTSTATUS is in the Debug power domain

## Attributes

CTICHOUTSTATUS is a 32-bit register.

## Field descriptions

<!-- image -->

## CHOUT&lt;n&gt;, bits [n], for n = 31 to 0

Output channel &lt;n&gt; status.

| CHOUT<n>   | Meaning                         |
|------------|---------------------------------|
| 0b0        | Output channel <n> is inactive. |
| 0b1        | Output channel <n> is active.   |

If the ECT channels do not support multicycle events, then it is IMPLEMENTATION DEFINED whether an output channel can be observed as active.

Note

The value in CTICHOUTSTATUS is after gating by the channel gate. For more information, see CTIGATE.

Accessing this field has the following behavior:

- When n &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is RO.

## Accessing CTICHOUTSTATUS

CTICHOUTSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance       |
|-------------|----------|----------------|
| CTI         | 0x13C    | CTICHOUTSTATUS |

Accesses to this register are RO.

## H9.5.8 CTICIDR0, CTI Component Identification Register 0

The CTICIDR0 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Component Identification scheme'.

## Configuration

CTICIDR0 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTICIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_0, bits [7:0]

Preamble.

Reads as 0x0D

Access to this field is RO.

## Accessing CTICIDR0

CTICIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFF0    | CTICIDR0   |

Accesses to this register are RO.

## H9.5.9 CTICIDR1, CTI Component Identification Register 1

The CTICIDR1 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Component Identification scheme'.

## Configuration

CTICIDR1 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTICIDR1 is a 32-bit register.

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

## Accessing CTICIDR1

CTICIDR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFF4    | CTICIDR1   |

Accesses to this register are RO.

## H9.5.10 CTICIDR2, CTI Component Identification Register 2

The CTICIDR2 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Component Identification scheme'.

## Configuration

CTICIDR2 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTICIDR2 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_2, bits [7:0]

Preamble.

Reads as 0x05

Access to this field is RO.

## Accessing CTICIDR2

CTICIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFF8    | CTICIDR2   |

Accesses to this register are RO.

## H9.5.11 CTICIDR3, CTI Component Identification Register 3

The CTICIDR3 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Component Identification scheme'.

## Configuration

CTICIDR3 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTICIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:8]

Reserved, RES0.

## PRMBL\_3, bits [7:0]

Preamble.

Reads as 0xB1

Access to this field is RO.

## Accessing CTICIDR3

CTICIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFFC    | CTICIDR3   |

Accesses to this register are RO.

## H9.5.12 CTICLAIMCLR, CTI CLAIM Tag Clear register

The CTICLAIMCLR characteristics are:

## Purpose

Used by software to read the values of the CLAIM bits, and to clear CLAIM tag bits to 0.

## Configuration

CTICLAIMCLR is in the Debug power domain

External register CTICLAIMCLR bits [31:0] are architecturally mapped to External register CTICLAIMSET[31:0].

Implementation of this register is OPTIONAL.

## Attributes

CTICLAIMCLR is a 32-bit register.

## Field descriptions

<!-- image -->

## CLAIM&lt;m&gt;, bits [m], for m = 31 to 0

Claim Tag Clear. Indicates the current status of Claim Tag bit &lt;m&gt;, and is used to clear Claim Tag bit &lt;m&gt; to 0.

| CLAIM<m>   | Meaning                                                                        |
|------------|--------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not set. On a write: Ignored.                  |
| 0b1        | On a read: Claim Tag bit <m> is set. On a write: Clear Claim tag bit <m> to 0. |

The number of Claim Tag bits implemented is indicated in CTICLAIMSET.

An External Debug reset clears the CLAIM tag bits to 0.

Accessing this field has the following behavior:

- When m &gt;= NUM\_CTI\_CLAIM\_TAGS, access to this field is RAZ/WI.
- Otherwise, access to this field is W1C.

## Accessing CTICLAIMCLR

CTICLAIMCLR can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| CTI         | 0xFA4    | CTICLAIMCLR |

Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.13 CTICLAIMSET, CTI CLAIM Tag Set register

The CTICLAIMSET characteristics are:

## Purpose

Used by software to set CLAIM bits to 1.

## Configuration

CTICLAIMSET is in the Debug power domain

External register CTICLAIMSET bits [31:0] are architecturally mapped to External register CTICLAIMCLR[31:0].

Implementation of this register is OPTIONAL.

## Attributes

CTICLAIMSET is a 32-bit register.

## Field descriptions

<!-- image -->

## CLAIM&lt;m&gt;, bits [m], for m = 31 to 0

Claim Tag Set. Indicates whether Claim Tag bit &lt;m&gt; is implemented, and is used to set Claim Tag bit &lt;m&gt; to 1.

| CLAIM<m>   | Meaning                                                                              |
|------------|--------------------------------------------------------------------------------------|
| 0b0        | On a read: Claim Tag bit <m> is not implemented. On a write: Ignored.                |
| 0b1        | On a read: Claim Tag bit <m> is implemented. On a write: Set Claim Tag bit <m> to 1. |

An External Debug reset clears the CLAIM tag bits to 0.

Accessing this field has the following behavior:

- When m &gt;= NUM\_CTI\_CLAIM\_TAGS, access to this field is RAZ/WI.
- Otherwise, access to this field is RAO/W1S.

## Accessing CTICLAIMSET

CTICLAIMSET can be accessed through the external debug interface:

| Component   | Offset   | Instance    |
|-------------|----------|-------------|
| CTI         | 0xFA0    | CTICLAIMSET |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.14 CTICONTROL, CTI Control register

The CTICONTROL characteristics are:

## Purpose

Controls whether the CTI is enabled.

## Configuration

CTICONTROL is in the Debug power domain

## Attributes

CTICONTROL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:1]

Reserved, RES0.

## GLBEN, bit [0]

Enables or disables the CTI mapping functions. Possible values of this field are:

| GLBEN   | Meaning                                                 |
|---------|---------------------------------------------------------|
| 0b0     | CTI mapping functions and application trigger disabled. |
| 0b1     | CTI mapping functions and application trigger enabled.  |

When GLBEN is 0, the input channel to output trigger, input trigger to output channel, and application trigger functions are disabled and do not signal new events on either output triggers or output channels. If a previously asserted output trigger has not been acknowledged, it is CONSTRAINED UNPREDICTABLE which of the following occurs:

- The output trigger remains asserted after the mapping functions are disabled.
- The output trigger is deasserted after the mapping functions are disabled.

All output triggers are disabled by CTI reset.

If the ECT supports multicycle channel events any existing output channel events will be terminated.

The reset behavior of this field is:

- On a External debug reset, this field resets to '0' .

## Accessing CTICONTROL

CTICONTROL can be accessed through the external debug interface:

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0x000    | CTICONTROL |

## H9.5.15 CTIDEVAFF0, CTI Device Affinity register 0

The CTIDEVAFF0 characteristics are:

## Purpose

Copy of the low half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the CTI component relates to.

## Configuration

CTIDEVAFF0 is in the Debug power domain

If the CTI is CTIv1, this register is OPTIONAL. If the CTI is CTIv2, this register is mandatory.

Arm recommends that the CTI is CTIv2.

In an Armv8.5 compliant implementation, the CTI must be CTIv2.

If this register is implemented, then CTIDEV AFF1 must also be implemented. If the CTI of a PE does not implement the CTI Device Affinity registers, the CTI block of the external debug memory map must be located 64KB above the debug registers in the external debug interface.

## Attributes

CTIDEVAFF0 is a 32-bit register.

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

## Accessing CTIDEVAFF0

CTIDEVAFF0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFA8    | CTIDEVAFF0 |

Accesses to this register are RO.

## H9.5.16 CTIDEVAFF1, CTI Device Affinity register 1

The CTIDEVAFF1 characteristics are:

## Purpose

Copy of the high half of the PE MPIDR\_EL1 register that allows a debugger to determine which PE in a multiprocessor system the CTI component relates to.

## Configuration

CTIDEVAFF1 is in the Debug power domain

If the CTI is CTIv1, this register is OPTIONAL. If the CTI is CTIv2, this register is mandatory.

Arm recommends that the CTI is CTIv2.

In an Armv8.5 compliant implementation, the CTI must be CTIv2.

If this register is implemented, then CTIDEV AFF0 must also be implemented. If the CTI of a PE does not implement the CTI Device Affinity registers, the CTI block of the external debug memory map must be located 64KB above the debug registers in the external debug interface.

## Attributes

CTIDEVAFF1 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7   |
|------|-------|
| RES0 | Aff3  |

## Bits [31:8]

Reserved, RES0.

## Aff3, bits [7:0]

Affinity level 3. See the description of CTIDEV AFF0.Aff0 for more information.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing CTIDEVAFF1

CTIDEVAFF1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFAC    | CTIDEVAFF1 |

Accesses to this register are RO.

## H9.5.17 CTIDEVARCH, CTI Device Architecture register

The CTIDEVARCH characteristics are:

## Purpose

Identifies the programmers' model architecture of the CTI component.

## Configuration

CTIDEVARCH is in the Debug power domain

If the CTI is CTIv1, this register is OPTIONAL. If the CTI is CTIv2, this register is mandatory.

Arm recommends that the CTI is CTIv2.

In an Armv8.5 compliant implementation, the CTI must be CTIv2.

If this register is not implemented, CTIDEV AFF0 and CTIDEVAFF1 are also not implemented.

## Attributes

CTIDEVARCH is a 32-bit register.

## Field descriptions

<!-- image -->

## ARCHITECT, bits [31:21]

Defines the architect of the component. For CTI, this is Arm Limited.

Bits [31:28] are the JEP106 continuation code, 0b0100 .

Bits [27:21] are the JEP106 identification code, 0b0111011 .

Reads as 0b01000111011

Access to this field is RO.

## PRESENT, bit [20]

DEVARCHpresent. Indicates that the CTIDEVARCH register is present.

Reads as 0b1

Access to this field is RO.

## REVISION, bits [19:16]

Revision. Defines the architecture revision of the component.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| REVISION   | Meaning         |
|------------|-----------------|
| 0b0000     | First revision. |

0b0001

All other values are reserved.

When FEAT\_DoPD is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## ARCHID, bits [15:0]

Defines this part to be an Armv8 debug component. For architectures defined by Arm this is further subdivided.

For CTI:

- Bits [15:12] are the architecture version, 0x1 .
- Bits [11:0] are the architecture part number, 0xA14 .

This corresponds to CTI architecture version CTIv2.

Reads as

0x1A14

Access to this field is RO.

## Accessing CTIDEVARCH

CTIDEVARCH can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFBC    | CTIDEVARCH |

Accesses to this register are RO.

As 0b0000 , and also adds support for CTIDEVCTL.

## H9.5.18 CTIDEVCTL, CTI Device Control register

The CTIDEVCTL characteristics are:

## Purpose

Provides target-specific device controls

## Configuration

CTIDEVCTL is in the Debug power domain

This register is present only when FEAT\_DoPD is implemented. Otherwise, direct accesses to CTIDEVCTL are RES0.

## Attributes

CTIDEVCTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:2]

Reserved, RES0.

## RCE, bit [1]

Reset Catch Enable.

| RCE   | Meaning                           |
|-------|-----------------------------------|
| 0b0   | Reset Catch debug event disabled. |
| 0b1   | Reset Catch debug event enabled.  |

The reset behavior of this field is:

- On a External debug reset, this field resets to '0' .

## OSUCE, bit [0]

OS Unlock Catch Enable

| OSUCE   | Meaning                               |
|---------|---------------------------------------|
| 0b0     | OS Unlock Catch debug event disabled. |
| 0b1     | OS Unlock Catch debug event enabled.  |

The reset behavior of this field is:

- On a External debug reset, this field resets to '0' .

## Accessing CTIDEVCTL

CTIDEVCTL can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0x150    | CTIDEVCTL  |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.19 CTIDEVID, CTI Device ID register 0

The CTIDEVID characteristics are:

## Purpose

Describes the CTI component to the debugger.

## Configuration

CTIDEVID is in the Debug power domain

## Attributes

CTIDEVID is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:26]

Reserved, RES0.

## INOUT, bits [25:24]

Input/output options. Indicates presence of the input gate. If the CTM is not implemented or CTIv2 is not implemented, this field is RAZ.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| INOUT   | Meaning                                                                   |
|---------|---------------------------------------------------------------------------|
| 0b00    | CTIGATE does not mask propagation of input events from external channels. |
| 0b01    | CTIGATE masks propagation of input events from external channels.         |

All other values are reserved.

Access to this field is RO.

## Bits [23:22]

Reserved, RES0.

## NUMCHAN,bits [21:16]

Number of ECT channels implemented. For Armv8, valid values are:

- 0b000011 3 channels (0..2) implemented.
- 0b000100 4 channels (0..3) implemented.
- 0b000101 5 channels (0..4) implemented.
- 0b000110 6 channels (0..5) implemented.

This field has an IMPLEMENTATION DEFINED value.

and so on up to 0b100000 , 32 channels (0..31) implemented.

All other values are reserved.

Access to this field is RO.

## Bits [15:14]

Reserved, RES0.

## NUMTRIG, bits [13:8]

Upper bound for number of triggers. The indices of all implemented input and output triggers are less than this value.

This field has an IMPLEMENTATION DEFINED value.

There is no guarantee that all of the input and output triggers, including the highest numbered, are connected to any components, or that the implementation of input and output triggers is symmetrical.

Access to this field is RO.

## Bits [7:5]

Reserved, RES0.

## EXTMUXNUM,bits [4:0]

Number of multiplexors available on triggers. This value is used in conjunction with External Control register, ASICCTL.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing CTIDEVID

CTIDEVID can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFC8    | CTIDEVID   |

Accesses to this register are RO.

## H9.5.20 CTIDEVID1, CTI Device ID register 1

The CTIDEVID1 characteristics are:

## Purpose

Reserved for future information about the CTI component to the debugger.

## Configuration

CTIDEVID1 is in the Debug power domain

## Attributes

CTIDEVID1 is a 32-bit register.

## Field descriptions

## Bits [31:0]

Reserved, RES0.

## Accessing CTIDEVID1

CTIDEVID1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFC4    | CTIDEVID1  |

Accesses to this register are RO.

31

RES0

0

## H9.5.21 CTIDEVID2, CTI Device ID register 2

The CTIDEVID2 characteristics are:

## Purpose

Reserved for future information about the CTI component to the debugger.

## Configuration

CTIDEVID2 is in the Debug power domain

## Attributes

CTIDEVID2 is a 32-bit register.

## Field descriptions

## Bits [31:0]

Reserved, RES0.

## Accessing CTIDEVID2

CTIDEVID2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFC0    | CTIDEVID2  |

Accesses to this register are RO.

31

RES0

0

## H9.5.22 CTIDEVTYPE, CTI Device Type register

The CTIDEVTYPE characteristics are:

## Purpose

Indicates to a debugger that this component is part of a PE's cross-trigger interface.

## Configuration

CTIDEVTYPE is in the Debug power domain

Implementation of this register is OPTIONAL.

## Attributes

CTIDEVTYPE is a 32-bit register.

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

Major type. Indicates this is a cross-trigger component.

Reads as

0b0100

Access to this field is RO.

## Accessing CTIDEVTYPE

CTIDEVTYPE can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFCC    | CTIDEVTYPE |

Accesses to this register are RO.

## H9.5.23 CTIGATE, CTI Channel Gate Enable register

The CTIGATE characteristics are:

## Purpose

Determines whether events on channels propagate through the CTM to other ECT components, or from the CTM into the CTI.

## Configuration

CTIGATE is in the Debug power domain

## Attributes

CTIGATE is a 32-bit register.

## Field descriptions

GATE&lt;x&gt; , bits [x], for x = 31 to 0

<!-- image -->

Channel &lt;x&gt; gate enable.

| GATE<x>   | Meaning                                                                        |
|-----------|--------------------------------------------------------------------------------|
| 0b0       | Disable output and, if CTIDEVID.INOUT == 0b01 , input channel <x> propagation. |
| 0b1       | Enable output and, if CTIDEVID.INOUT == 0b01 , input channel <x> propagation.  |

If GATE&lt;x&gt; is set to 0, no new events will be propagated to the ECT, and if the ECT supports multicycle channel events any existing output channel events will be terminated.

The reset behavior of this field is:

- On a External debug reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When x &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is RW.

## Accessing CTIGATE

CTIGATE can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0x140    | CTIGATE    |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.24 CTIINEN&lt;n&gt;, CTI Input Trigger to Output Channel Enable registers, n = 0 - 31

The CTIINEN&lt;n&gt; characteristics are:

## Purpose

Enables the signaling of an event on output channels when input trigger event n is received by the CTI.

## Configuration

CTIINEN&lt;n&gt; is in the Debug power domain

If input trigger n is not implemented or not connected, CTIINEN&lt;n&gt; is RES0.

## Attributes

CTIINEN&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## INEN&lt;x&gt; , bits [x], for x = 31 to 0

Input trigger &lt;n&gt; to output channel &lt;x&gt; enable.

| INEN<x>   | Meaning                                                             |
|-----------|---------------------------------------------------------------------|
| 0b0       | Input trigger <n> will not generate an event on output channel <x>. |
| 0b1       | Input trigger <n> will generate an event on output channel <x>.     |

The reset behavior of this field is:

- On a External debug reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When x &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is RW.

## Accessing CTIINEN&lt;n&gt;

CTIINEN&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance            |
|-------------|----------------------------|
| CTI         | 0x020 + (4 * n) CTIINEN<n> |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.25 CTIINTACK, CTI Output Trigger Acknowledge register

The CTIINTACK characteristics are:

## Purpose

Can be used to deactivate the output triggers.

## Configuration

CTIINTACK is in the Debug power domain

## Attributes

CTIINTACK is a 32-bit register.

## Field descriptions

<!-- image -->

## ACK&lt;n&gt; , bits [n], for n = 31 to 0

Acknowledge for output trigger &lt;n&gt;.

If any of the following is true, writes to ACK&lt;n&gt; are ignored:

- n &gt;= CTIDEVID.NUMTRIG, the number of implemented triggers.
- Output trigger n is not active.
- The channel mapping function output, as controlled by CTIOUTEN&lt;n&gt;, is still active.

Otherwise, if any of the following are true, ACK&lt;n&gt; is RES0:

- Output trigger n is not implemented.
- Output trigger n is not connected.
- Output trigger n is self-acknowledging and does not require software acknowledge.

Otherwise, the behavior on writes to ACK&lt;n&gt; is as follows:

Accessing this field has the following behavior:

- When n &gt;= UInt(CTIDEVID.NUMTRIG), access to this field is RAZ/WI.
- Otherwise, access to this field is WO/UNKNOWN.

## Accessing CTIINTACK

Adebugger must read CTITRIGOUTSTATUS to confirm that the output trigger has been acknowledged before generating any event that must be ordered after the write to CTIINTACK, such as a write to CTIAPPPULSE to activate another trigger.

CTIINTACK can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0x010    | CTIINTACK  |

Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are WI.
- Otherwise, accesses to this register are WO.

| ACK<n>   | Meaning                 |
|----------|-------------------------|
| 0b0      | No effect               |
| 0b1      | Deactivate the trigger. |

## H9.5.26 CTIITCTRL, CTI Integration mode Control register

The CTIITCTRL characteristics are:

## Purpose

Enables the CTI to switch from its default mode into integration mode, where test software can control directly the inputs and outputs of the PE, for integration testing or topology detection.

## Configuration

The power domain of CTIITCTRL is IMPLEMENTATION DEFINED

Implementation of this register is OPTIONAL.

## Attributes

CTIITCTRL is a 32-bit register.

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

## Accessing CTIITCTRL

CTIITCTRL can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xF00    | CTIITCTRL  |

## Accessible as follows:

- When DoubleLockStatus(), or !IsCorePowered(), or OSLockStatus(), accesses to this register are IMPLEMENTATION DEFINED.
- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.27 CTILAR, CTI Lock Access Register

The CTILAR characteristics are:

## Purpose

Allows or disallows access to the CTI registers through a memory-mapped interface.

The optional Software Lock provides a lock to prevent memory-mapped writes to the Cross-Trigger Interface registers. Use of this lock mechanism reduces the risk of accidental damage to the contents of the Cross-Trigger Interface registers. It does not, and cannot, prevent all accidental or malicious damage.

## Configuration

CTILAR is in the Debug power domain

If FEAT\_Debugv8p4 is implemented, the Software Lock is not implemented.

Software uses CTILAR to set or clear the lock, and CTILSR to check the current status of the lock.

## Attributes

CTILAR is a 32-bit register.

## Field descriptions

When CTI Software Lock is implemented:

<!-- image -->

## KEY, bits [31:0]

Lock Access control. Writing the key value 0xC5ACCE55 to this field unlocks the lock, enabling write accesses to this component's registers through a memory-mapped interface.

Writing any other value to this register locks the lock, disabling write accesses to this component's registers through a memory mapped interface.

## Otherwise:

<!-- image -->

Otherwise

## Bits [31:0]

Reserved, RES0.

## Accessing CTILAR

CTILAR can be accessed through the memory-mapped interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFB0    | CTILAR     |

Accesses to this register are WO.

## H9.5.28 CTILSR, CTI Lock Status Register

The CTILSR characteristics are:

## Purpose

Indicates the current status of the Software Lock for CTI registers.

The optional Software Lock provides a lock to prevent memory-mapped writes to the Cross-Trigger Interface registers. Use of this lock mechanism reduces the risk of accidental damage to the contents of the Cross-Trigger Interface registers. It does not, and cannot, prevent all accidental or malicious damage.

## Configuration

CTILSR is in the Debug power domain

If FEAT\_Debugv8p4 is implemented, the Software Lock is not implemented.

Software uses CTILAR to set or clear the lock, and CTILSR to check the current status of the lock.

## Attributes

CTILSR is a 32-bit register.

## Field descriptions

| 31   | 2 1 0       |
|------|-------------|
| RES0 | nTT SLK SLI |

## Bits [31:3]

Reserved, RES0.

## nTT, bit [2]

Not thirty-two bit access required. RAZ.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SLK, bit [1]

## When CTI Software Lock is implemented:

Software Lock status for this component. For an access to LSR that is not a memory-mapped access, or when the Software Lock is not implemented, this field is RES0.

For memory-mapped accesses when the Software Lock is implemented, possible values of this field are:

| SLK   | Meaning                                                                                     |
|-------|---------------------------------------------------------------------------------------------|
| 0b0   | Lock clear. Writes are permitted to this component's registers.                             |
| 0b1   | Lock set. Writes to this component's registers are ignored, and reads have no side effects. |

The reset behavior of this field is:

· On a External debug reset, this field resets to '1' .

## Otherwise:

Reserved, RAZ.

## SLI, bit [0]

Software Lock implemented. For an access to LSR that is not a memory-mapped access, this field is RAZ. The value of this field is an IMPLEMENTATION DEFINED choice of:

| SLI   | Meaning                                                    |
|-------|------------------------------------------------------------|
| 0b0   | Software Lock not implemented or not memory-mapped access. |
| 0b1   | Software Lock implemented and memory-mapped access.        |

Access to this field is RO.

## Accessing CTILSR

CTILSR can be accessed through the memory-mapped interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFB4    | CTILSR     |

Accesses to this register are RO.

## H9.5.29 CTIOUTEN&lt;n&gt;, CTI Input Channel to Output Trigger Enable registers, n = 0 - 31

The CTIOUTEN&lt;n&gt; characteristics are:

## Purpose

Defines which input channels generate output trigger n.

## Configuration

CTIOUTEN&lt;n&gt; is in the Debug power domain

If output trigger n is not implemented or not connected, CTIOUTEN&lt;n&gt; is RES0.

## Attributes

CTIOUTEN&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## OUTEN&lt;x&gt; , bits [x], for x = 31 to 0

Input channel &lt;x&gt; to output trigger &lt;n&gt; enable.

| OUTEN<x>   | Meaning                                                                         |
|------------|---------------------------------------------------------------------------------|
| 0b0        | An event on input channel <x> will not cause output trigger <n> to be asserted. |
| 0b1        | An event on input channel <x> will cause output trigger <n> to be asserted.     |

The reset behavior of this field is:

- On a External debug reset, this field resets to an architecturally UNKNOWN value.

Accessing this field has the following behavior:

- When x &gt;= UInt(CTIDEVID.NUMCHAN), access to this field is RAZ/WI.
- Otherwise, access to this field is RW.

## Accessing CTIOUTEN&lt;n&gt;

CTIOUTEN&lt;n&gt; can be accessed through the external debug interface:

| Component   | Offset Instance             |
|-------------|-----------------------------|
| CTI         | 0x0A0 + (4 * n) CTIOUTEN<n> |

## Accessible as follows:

- When SoftwareLockStatus(), accesses to this register are RO.
- Otherwise, accesses to this register are RW.

## H9.5.30 CTIPIDR0, CTI Peripheral Identification Register 0

The CTIPIDR0 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

CTIPIDR0 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTIPIDR0 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    |
|------|--------|
|      | PART_0 |

## Bits [31:8]

Reserved, RES0.

## PART\_0, bits [7:0]

Part number, least significant byte.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing CTIPIDR0

CTIPIDR0 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFE0    | CTIPIDR0   |

Accesses to this register are RO.

## H9.5.31 CTIPIDR1, CTI Peripheral Identification Register 1

The CTIPIDR1 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

CTIPIDR1 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTIPIDR1 is a 32-bit register.

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

## Accessing CTIPIDR1

CTIPIDR1 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFE4    | CTIPIDR1   |

Accesses to this register are RO.

## H9.5.32 CTIPIDR2, CTI Peripheral Identification Register 2

The CTIPIDR2 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

CTIPIDR2 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTIPIDR2 is a 32-bit register.

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

## Accessing CTIPIDR2

CTIPIDR2 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFE8    | CTIPIDR2   |

Accesses to this register are RO.

## H9.5.33 CTIPIDR3, CTI Peripheral Identification Register 3

The CTIPIDR3 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

CTIPIDR3 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTIPIDR3 is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 8 7    | 4 3   |
|------|--------|-------|
| RES0 | REVAND | CMOD  |

## Bits [31:8]

Reserved, RES0.

## REVAND, bits [7:4]

Part minor revision. Parts using CTIPIDR2.REVISION as an extension to the Part number must use this field as a major revision number.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## CMOD,bits [3:0]

Customer modified. Indicates someone other than the Designer has modified the component.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing CTIPIDR3

CTIPIDR3 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFEC    | CTIPIDR3   |

Accesses to this register are RO.

## H9.5.34 CTIPIDR4, CTI Peripheral Identification Register 4

The CTIPIDR4 characteristics are:

## Purpose

Provides information to identify a CTI component.

For more information, see 'About the Peripheral identification scheme'.

## Configuration

CTIPIDR4 is in the Debug power domain

This register is required for CoreSight compliance.

Implementation of this register is OPTIONAL.

## Attributes

CTIPIDR4 is a 32-bit register.

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

## Accessing CTIPIDR4

CTIPIDR4 can be accessed through the external debug interface:

| Component   | Offset   | Instance   |
|-------------|----------|------------|
| CTI         | 0xFD0    | CTIPIDR4   |

Accesses to this register are RO.

## H9.5.35 CTITRIGINSTATUS, CTI Trigger In Status register

The CTITRIGINSTATUS characteristics are:

## Purpose

Provides the status of the trigger inputs.

## Configuration

CTITRIGINSTATUS is in the Debug power domain

## Attributes

CTITRIGINSTATUS is a 32-bit register.

## Field descriptions

TRIN&lt;n&gt; , bits [n], for n = 31 to 0

<!-- image -->

Trigger input &lt;n&gt; status.

| TRIN<n>   | Meaning                      |
|-----------|------------------------------|
| 0b0       | Input trigger n is inactive. |
| 0b1       | Input trigger n is active.   |

Not implemented and not-connected input triggers are always inactive.

It is IMPLEMENTATION DEFINED whether an input trigger that does not support multicycle events can be observed as active.

Accessing this field has the following behavior:

- When n &gt;= UInt(CTIDEVID.NUMTRIG), access to this field is RAZ/WI.
- Otherwise, access to this field is RO.

## Accessing CTITRIGINSTATUS

CTITRIGINSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance        |
|-------------|----------|-----------------|
| CTI         | 0x130    | CTITRIGINSTATUS |

Accesses to this register are RO.

## H9.5.36 CTITRIGOUTSTATUS, CTI Trigger Out Status register

The CTITRIGOUTSTATUS characteristics are:

## Purpose

Provides the raw status of the trigger outputs, after processing by any IMPLEMENTATION DEFINED trigger interface logic. For output triggers that are self-acknowledging, this is only meaningful if the CTI implements multicycle channel events.

## Configuration

CTITRIGOUTSTATUS is in the Debug power domain

## Attributes

CTITRIGOUTSTATUS is a 32-bit register.

## Field descriptions

<!-- image -->

## TROUT&lt;n&gt; , bits [n], for n = 31 to 0

Trigger output &lt;n&gt; status.

If n is less than CTIDEVID.NUMTRIG, and output trigger &lt;n&gt; is implemented and connected, and either the trigger is not self-acknowledging or the CTI implements multicycle channel events, then permitted values for TROUT&lt;n&gt; are:

| TROUT<n>   | Meaning                       |
|------------|-------------------------------|
| 0b0        | Output trigger n is inactive. |
| 0b1        | Output trigger n is active.   |

Otherwise when n is less than CTIDEVID.NUMTRIG, it is IMPLEMENTATION DEFINED whether TROUT&lt;n&gt; behaves as described here or is RAZ.

Accessing this field has the following behavior:

- When n &gt;= UInt(CTIDEVID.NUMTRIG), access to this field is RAZ/WI.
- Access to this field is RAZ/WI if all of the following are true:
- Any of the following are true:
- Output trigger &lt;n&gt; is not implemented or not connected
- All of the following are true:
- Output trigger &lt;n&gt; is self-acknowledging
- CTI does not implement multicycle channel events
- an implementation implements TROUT&lt;n&gt;
- Otherwise, access to this field is RO.

## Accessing CTITRIGOUTSTATUS

CTITRIGOUTSTATUS can be accessed through the external debug interface:

| Component   | Offset   | Instance         |
|-------------|----------|------------------|
| CTI         | 0x134    | CTITRIGOUTSTATUS |

Accesses to this register are RO.